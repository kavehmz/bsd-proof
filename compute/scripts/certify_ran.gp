\\ certify_ran.gp -- how rigorously can PARI certify r_an for 389a1 (rank 2) and 5077a1 (rank 3)?
\\
\\ Usage (repository root):  compute/scripts/gp -q compute/scripts/certify_ran.gp
\\ Output: compute/data/certify_ran.log (everything printed below), compute/data/certify_ran.json
\\
\\ Structure, for each curve E:
\\  (1) [exact]   r_alg with certificate: ellrank returns [r1, r2, s, pts]; r1 == r2 pins the rank down
\\                unconditionally (2-descent + Cassels-Tate pairing on Sha[2]); independence of the points is
\\                witnessed by det(height matrix) != 0 (floating point, 60 digits) and by ellsaturation.
\\  (2) [exact]   L(E,1)/Omega^+ as an exact rational number from the modular symbol x^+ of E (msfromell, exact
\\                linear algebra over Q): x^+([0]-[oo]) = L(E,1)/Omega^+ (Manin / Birch--Manin--Drinfeld modular
\\                symbols, plus modularity of E).  For our curves the rational number is 0, which PROVES L(E,1) = 0.
\\                Sanity check on 11a1: x^+([0]-[oo]) = 1/5 = L(E,1)/Omega^+ (= |Sha| c_11 / |T|^2 = 5/25).
\\                Also exact values of the twisted L-values L(E,chi_D,1)/Omega^{sign(D)} for small |D|, exhibiting
\\                twists whose L-value is provably nonzero.
\\  (3) [exact]   root number w = ellrootno(E) (algebraic: local root numbers), giving the parity of r_an
\\                (Lambda(s) = w Lambda(2-s): if w = +1 all odd derivatives of Lambda at s=1 vanish, if w = -1
\\                all even ones; with L(E,1)=0 this transfers to L: L'(E,1) = 0 when w = +1).
\\  (4) [numeric] L^(k)(E,1)/k!, k = 0..r_alg+1, at 60 and 100 decimal digits with two independent PARI algorithms
\\                (lfun: generic approximate functional equation / theta series; ellL1: ellanal.c, specific to E/Q),
\\                the differences estimating the true error (PARI's documented advice), lfuncheckfeq, and
\\                ellanalyticrank with the default eps = 2^{-bits/2} and with eps = 2^{-3 bits/4}.
\\  What is rigorous and what is not is discussed in compute/RESULTS.md, section (d).

default(realprecision, 60);
LOG = "compute/data/certify_ran.log";
JS  = "compute/data/certify_ran.json";
fL = fileopen(LOG, "w");
fJ = fileopen(JS, "w");
say(s) = { filewrite(fL, s); print(s); }
fmt(x, d) = Strprintf(Str("%.", d, "g"), x);

\\ exact rational L(E,chi_D,1)/Omega^{sign D}: sum_{0<=a<|D|} (D|a) x^{sign D}([a/|D|]-[oo])
twistvalue(M, xs, D) = {
  my(s = 0, aD = abs(D));
  for (a = 0, aD - 1, if (kronecker(D, a), s += kronecker(D, a) * mseval(M, xs, [oo, a / aD])));
  s
}

certify(label) = {
  my(E = ellinit(label), N, w, rk, W, Reg, M, xp, xm, L0, tw, L, ser60, ser100, e60, e100, ran, ran2, chk, r, bits);
  N = ellglobalred(E)[1];
  say(Str("################ ", label, "   N = ", N, "   ainvs = ", [E.a1, E.a2, E.a3, E.a4, E.a6]));
  \\ (1) algebraic rank
  rk = ellrank(E);
  W = ellsaturation(E, rk[4], 1000);
  Reg = matdet(ellheightmatrix(E, W));
  say(Str("(1) ellrank(E) = ", rk, "  -> r_alg = ", rk[1], if (rk[1] == rk[2], " CERTIFIED (r1 = r2)", " NOT certified")));
  say(Str("    saturated basis (primes < 1000): ", W, "   det(height matrix) = ", Reg, " != 0"));
  \\ (2) exact L(E,1)/Omega^+ via modular symbols
  [M, xp] = msfromell(E, 1);
  L0 = mseval(M, xp, [oo, 0]);
  say(Str("(2) modular symbol x^+ = ", xp, "   x^+([0]-[oo]) = L(E,1)/Omega^+ = ", L0, "  (EXACT rational)"));
  [M, xm] = msfromell(E, -1);
  tw = vector(0);
  forstep (D = -3, -100, -1, if (isfundamental(D), my(v = twistvalue(M, xm, D)); tw = concat(tw, [[D, v]])));
  say(Str("    exact L(E,chi_D,1)/Omega^- for fundamental D<0, |D|<=100 (0 means provably zero): ", tw));
  tw = vector(0);
  forstep (D = 5, 100, 1, if (isfundamental(D), my(v = twistvalue(M, xp, D)); tw = concat(tw, [[D, v]])));
  say(Str("    exact L(E,chi_D,1)/Omega^+ for fundamental D>0, D<=100: ", tw));
  \\ (3) root number
  w = ellrootno(E);
  say(Str("(3) root number w = ", w, "  -> r_an is ", if (w == 1, "even", "odd"), " (functional equation)"));
  \\ (4) numerics
  r = rk[1];
  L = lfuncreate(E);
  say(Str("(4) lfuncheckfeq(L) at 60 digits: ", lfuncheckfeq(L), " (bits of agreement of the functional equation; -realbitprecision is perfect)"));
  ser60 = lfun(L, 1 + x + O(x^(r + 2)));
  e60 = vector(r + 2, k, ellL1(E, k - 1) / (k - 1)!);
  ran = ellanalyticrank(E);
  bits = default(realbitprecision);
  ran2 = ellanalyticrank(E, 2.^(-(3 * bits) \ 4));
  say(Str("    realprecision 60 (", bits, " bits): lfun Taylor coefficients L^(k)(1)/k!, k=0..", r + 1, ":"));
  for (k = 0, r + 1, say(Str("      k=", k, ": lfun ", fmt(polcoef(ser60, k), 45), "    ellL1 ", fmt(e60[k + 1], 45))));
  say(Str("    ellanalyticrank(E) = ", ran, "   with eps = 2^(-3 bits/4): ", ran2));
  default(realprecision, 100);
  E = ellinit(label); L = lfuncreate(E);
  ser100 = lfun(L, 1 + x + O(x^(r + 2)));
  e100 = vector(r + 2, k, ellL1(E, k - 1) / (k - 1)!);
  say(Str("    realprecision 100 (", default(realbitprecision), " bits): L^(k)(1)/k!:"));
  for (k = 0, r + 1, say(Str("      k=", k, ": lfun ", fmt(polcoef(ser100, k), 80), "    ellL1 ", fmt(e100[k + 1], 80))));
  say(Str("    |lfun_60 - lfun_100| for k=0..", r + 1, ": ", vector(r + 2, k, fmt(abs(polcoef(ser60, k - 1) - polcoef(ser100, k - 1)), 3))));
  say(Str("    |ellL1_60 - ellL1_100|: ", vector(r + 2, k, fmt(abs(e60[k] - e100[k]), 3)), "    |lfun_100 - ellL1_100|: ", vector(r + 2, k, fmt(abs(polcoef(ser100, k - 1) - e100[k]), 3))));
  say(Str("    leading term L^(", r, ")(E,1)/", r, "! = ", fmt(polcoef(ser100, r), 80)));
  default(realprecision, 60);
  filewrite(fJ, concat(["{\"label\":\"", label, "\",\"N\":", Str(N), ",\"ellrank\":\"", Str(rk), "\",\"r_alg\":", Str(rk[1]), ",\"rank_certified\":", Str(rk[1] == rk[2]),
     ",\"L1_over_Omega_exact\":\"", Str(L0), "\",\"rootno\":", Str(w), ",\"r_an\":", Str(ran[1]),
     ",\"lfun_taylor_60\":\"", Str(vector(r + 2, k, polcoef(ser60, k - 1))), "\",\"lfun_taylor_100\":\"", Str(vector(r + 2, k, polcoef(ser100, k - 1))),
     "\",\"ellL1_100\":\"", Str(e100), "\",\"leading_100\":\"", Str(polcoef(ser100, r)), "\"}"]));
}

say(Str("certify_ran.gp  PARI/GP ", version(), "   command: compute/scripts/gp -q compute/scripts/certify_ran.gp"));
{
  my(E = ellinit("11a1"), M, xp);
  [M, xp] = msfromell(E, 1);
  say(Str("sanity (11a1, rank 0): x^+([0]-[oo]) = ", mseval(M, xp, [oo, 0]), "   L(E,1)/Omega^+ numerically = ", ellL1(E) / E.omega[1]));
}
certify("389a1");
certify("5077a1");
fileclose(fL); fileclose(fJ);
