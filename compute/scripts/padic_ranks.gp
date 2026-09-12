\\ padic_ranks.gp -- p-adic analytic ranks r_p = ord_{T=0} L_p(E,T), leading coefficients, cyclotomic p-adic
\\ regulators and the p-adic BSD ratio (PARI's ellpadicbsd) for good ordinary primes p, using PARI/GP 2.17's
\\ overconvergent modular symbols (msfromell / mspadicinit / mstooms / mspadicmoments / mspadicseries).
\\
\\ Usage (repository root):
\\   PADIC_CURVES="389a1,433a1" PADIC_PMAX=31 PADIC_OUT=compute/data/padic_ranks_pari.jsonl \
\\       compute/scripts/gp -q compute/scripts/padic_ranks.gp
\\ Defaults: all 19 rank-2 curves of the BSD table with p <= 31, plus 5077a1 with p <= 17 (memory: PARI's
\\ mspadicinit needs O(N^2 (n+2)^2 p) words; for N = 5077 this exceeds 32 GB already at p ~ 17).
\\ Output: one JSON object per (E,p) appended to PADIC_OUT; human-readable log on stdout.
\\
\\ Conventions:
\\  * mspadicseries(mu) returns L_p(E,T) = sum_k c_k T^k, where (1+T)^{log_p(t)/log_p(1+p)} = <t>, i.e. T = gamma - 1
\\    for the topological generator gamma of 1+pZ_p with chi(gamma) = 1+p: the Mazur--Tate--Teitelbaum series in
\\    its standard normalisation (identical to Sage's E.padic_lseries(p).series()).  Each c_k comes with its own
\\    p-adic precision O(p^{m_k}), m_k decreasing with k.
\\  * mspadicL(mu,0,r) = int_{Z_p^*} log_p(a)^r dmu(a) = r! log_p(1+p)^r c_r  (the derivative in the s-variable,
\\    what ellpadicL(E,p,n,,r) returns); we check this identity numerically for every (E,p).
\\  * r_p^{upper} := min{k : c_k has a nonzero known digit} is a certified upper bound for r_p (the coefficient is
\\    provably nonzero given PARI's error bookkeeping).  Coefficients c_k, k < r_p^{upper}, are only known to be
\\    O(p^{m_k}), i.e. zero to the working precision; that r_p >= r_alg is a theorem for good ordinary p
\\    (Kato + Mazur's control theorem; see RESULTS.md), so r_p^{upper} = r_alg pins r_p down exactly.
\\  * ellpadicbsd(E,p,n) = [r, Lp] where Lp is conjecturally R_p * |Sha| with R_p = ellpadicregulator(E,p,n,basis)
\\    (PARI's normalisation absorbs (1-1/alpha)^{-2}, r!, log_p(1+p)^r, the Tamagawa product and the torsion).
\\    We report sha_bsd := Lp / R_p, whose p-adic valuation is the p-adic BSD prediction for ord_p |Sha|.
\\  * Independently, sha_series := c_r * |T|^2 * log_p(1+p)^r / ((1-1/alpha)^2 * elltamagawa(E) * R_p) is the
\\    Stein--Wuthrich form of the p-adic BSD prediction (alpha = unit root of x^2 - a_p x + p).  NB: PARI's
\\    L_p(E,T) interpolates (1-1/alpha)^2 L(E,1)/w1 with w1 = E.omega[1] the least real period, so it equals
\\    [E(R):E(R)^0] (= 2 if disc > 0) times the MTT/Sage series normalised with Omega_E; elltamagawa(E) contains
\\    exactly this factor at infinity (elltamagawa = prod_p c_p * [E(R):E(R)^0]).  Verified on 18 rank-0 curves.
\\  * Precision policy: start with n = N0 (n = 8 for p <= 7, 6 otherwise) and increase n by 3 until the leading
\\    coefficient c_{r_alg} is known with at least 3 significant p-adic digits (m_r - v_p(c_r) >= 3) or n > NMAX.

default(realprecision, 60);

PADIC_CURVES = getenv("PADIC_CURVES");
PADIC_PMAX = getenv("PADIC_PMAX");
PADIC_OUT = getenv("PADIC_OUT");
if (PADIC_OUT == 0, PADIC_OUT = "compute/data/padic_ranks_pari.jsonl");
NMAX = 15;   \\ maximal p-adic working precision exponent tried

{
DEFAULT_CURVES = [["389a1", 31], ["433a1", 31], ["446d1", 31], ["563a1", 31], ["571b1", 31], ["643a1", 31], ["655a1", 31],
                  ["664a1", 31], ["681c1", 31], ["707a1", 31], ["709a1", 31], ["718b1", 31], ["794a1", 31], ["817a1", 31],
                  ["916c1", 31], ["944e1", 31], ["997b1", 31], ["1001c1", 31], ["5077a1", 17]];
}

fOUT = fileopen(PADIC_OUT, "a");
jstr(s) = Str("\"", s, "\"");

\\ [valuation, precision] of a p-adic number (precision = absolute exponent of O())
vp(x) = if (x == 0, [oo, padicprec(x, x.p)], [valuation(x, x.p), padicprec(x, x.p)]);
isnonzero(x) = (x != 0);   \\ PARI: a t_PADIC equal to O(p^k) tests as 0

analyse(label, E, p, W, r, n) = {
  my(M, phi, Mp, PHI, mu, S, coefs, cv, rp_up, lead, lower_zero, derr, dr, R, B, alpha, eps, sha_series, sha_bsd, cp, T, t0 = getabstime(), ok);
  [M, phi] = msfromell(E, 1);
  Mp = mspadicinit(M, p, n, 0);          \\ flag 0: ordinary symbols only (p is good ordinary here)
  PHI = mstooms(Mp, phi);
  mu = mspadicmoments(Mp, PHI);
  S = mspadicseries(mu);                  \\ L_p(E,T) as a series in x = T
  coefs = vector(r + 2, k, polcoef(S, k - 1));
  cv = vector(r + 2, k, vp(coefs[k]));
  rp_up = -1; for (k = 1, r + 2, if (isnonzero(coefs[k]), rp_up = k - 1; break));
  lower_zero = 1; for (k = 1, r, if (isnonzero(coefs[k]), lower_zero = 0));
  lead = coefs[r + 1];
  dr = mspadicL(mu, 0, r);                \\ int log^r dmu
  derr = dr - r! * log(1 + p + O(p^(n + 6)))^r * lead;   \\ should be O(p^small)
  ok = (isnonzero(lead) && (cv[r + 1][2] - cv[r + 1][1] >= 3));
  [S, coefs, cv, rp_up, lead, lower_zero, dr, derr, ok, getabstime() - t0]
}

process(label, PMAX) = {
  my(E, N, W, r, T, cp, gr);
  E = ellinit(label);
  gr = ellglobalred(E); N = gr[1]; cp = gr[3]; T = elltors(E)[1];
  W = ellsaturation(E, if (#E.gen, E.gen, ellrank(E)[4]), 100);
  r = #W;
  print("== ", label, "  N=", N, "  rank ", r, "  saturated basis ", W, "  |T|=", T, "  prod c_p=", cp);
  forprime (p = 3, PMAX,
    my(ap, anomalous, n, res, S, coefs, cv, rp_up, lead, lower_zero, dr, derr, ok, tA, R, B, alpha, eps, sha_series, sha_bsd, t0 = getabstime(), errmsg = "");
    if (N % p == 0, print("  p=", p, ": bad reduction, skipped"); next);
    ap = ellap(E, p);
    if (ap % p == 0, print("  p=", p, ": supersingular (a_p=", ap, "), skipped"); next);
    anomalous = ((ap - 1) % p == 0);
    n = if (p <= 7, 8, 6);
    while (1,
      res = iferr(analyse(label, E, p, W, r, n), err, err);
      if (type(res) == "t_ERROR", errmsg = Str(res); break);
      [S, coefs, cv, rp_up, lead, lower_zero, dr, derr, ok, tA] = res;
      if (ok || n + 3 > NMAX, break);
      print("  p=", p, ": n=", n, " insufficient (leading coeff ", lead, "), increasing n"); n += 3);
    if (errmsg != "", print("  p=", p, ": ERROR ", errmsg);
        filewrite(fOUT, Str("{\"label\":", jstr(label), ",\"p\":", p, ",\"ap\":", ap, ",\"error\":", jstr(errmsg), "}")); next);
    \\ p-adic regulator, p-adic BSD (PARI), and the Stein-Wuthrich form from the series
    R = iferr(ellpadicregulator(E, p, n, W), err, err);
    B = iferr(ellpadicbsd(E, p, n), err, err);
    alpha = padicappr(x^2 - ap * x + p, ap + O(p^(n + 6)))[1];
    eps = (1 - 1 / alpha)^2;
    \\ PARI's L_p is normalised with the least real period w1 = E.omega[1], i.e. it is [E(R):E(R)^0] times the
    \\ MTT/Sage series normalised with Omega_E; elltamagawa(E) = prod_p c_p * [E(R):E(R)^0] absorbs this factor.
    sha_series = if (type(R) != "t_ERROR", lead * T^2 * log(1 + p + O(p^(n + 6)))^r / (eps * elltamagawa(E) * R), "error");
    sha_bsd = if (type(R) != "t_ERROR" && type(B) != "t_ERROR", B[2] / R, "error");
    print("  p=", p, " a_p=", ap, if (anomalous, " ANOMALOUS", ""), " n=", n, "  L_p(T) = ", S);
    print("     coefficient [val,prec] k=0..", r + 1, ": ", cv, "  r_p^upper=", rp_up, "  lower coefficients zero to precision: ", lower_zero);
    print("     int log^r dmu = ", dr, "   (check vs r! log(1+p)^r c_r: ", derr, ")");
    print("     R_p = ", R, "   ellpadicbsd = ", B);
    print("     sha_bsd = Lp/R_p = ", sha_bsd, "   sha_series = ", sha_series, "   [", getabstime() - t0, " ms]");
    filewrite(fOUT, concat(["{\"label\":", jstr(label), ",\"N\":", Str(N), ",\"p\":", Str(p), ",\"ap\":", Str(ap), ",\"anomalous\":", Str(anomalous),
      ",\"r_alg\":", Str(r), ",\"n\":", Str(n), ",\"series\":", jstr(Str(S)), ",\"coef_val_prec\":", Str(apply(v -> if (v[1] == oo, [-1, v[2]], v), cv)),
      ",\"rp_upper\":", Str(rp_up), ",\"lower_zero\":", Str(lower_zero), ",\"lead\":", jstr(Str(lead)),
      ",\"v_lead\":", Str(if (lead == 0, -1, valuation(lead, p))), ",\"prec_lead\":", Str(cv[r + 1][2]),
      ",\"deriv_r\":", jstr(Str(dr)), ",\"deriv_check\":", jstr(Str(derr)),
      ",\"reg\":", jstr(Str(R)), ",\"v_reg\":", Str(if (type(R) == "t_ERROR" || R == 0, -99, valuation(R, p))),
      ",\"bsd\":", jstr(Str(B)), ",\"sha_bsd\":", jstr(Str(sha_bsd)),
      ",\"v_sha_bsd\":", Str(if (type(sha_bsd) == "t_PADIC" && sha_bsd != 0, valuation(sha_bsd, p), -99)),
      ",\"sha_series\":", jstr(Str(sha_series)), ",\"certified_lead\":", Str(ok), ",\"time_ms\":", Str(getabstime() - t0), "}"])));
}

{
print("padic_ranks.gp  PARI/GP ", version(), "  output -> ", PADIC_OUT);
if (PADIC_CURVES == 0,
  for (i = 1, #DEFAULT_CURVES, process(DEFAULT_CURVES[i][1], DEFAULT_CURVES[i][2])),
  my(L = strsplit(PADIC_CURVES, ","), pm = if (PADIC_PMAX == 0, 31, eval(PADIC_PMAX)));
  for (i = 1, #L, process(L[i], pm)));
fileclose(fOUT);
}
