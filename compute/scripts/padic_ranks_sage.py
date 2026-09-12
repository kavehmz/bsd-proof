#!/usr/bin/env sage -python
"""
padic_ranks_sage.py -- p-adic analytic ranks, leading coefficients, p-adic regulators and the p-adic BSD
prediction for |Sha|, computed with SageMath (E.padic_lseries(p).series(n): Mazur--Tate--Teitelbaum series via
Riemann sums of modular symbols, the algorithm of Stein--Wuthrich; E.padic_regulator(p)).

This is an implementation independent of PARI's overconvergent-symbol code (compute/scripts/padic_ranks.gp) and
is cheap in memory, so it covers all good ordinary primes up to 100 (PARI needs O(N^2 n^2 p) words).

Usage (repository root; Sage 10.7 installed in .tools/sage by micromamba, see compute/README.md):
    .tools/sage/bin/sage -python compute/scripts/padic_ranks_sage.py --curves 389a1,433a1 --pmax 100 \
        --out compute/data/padic_ranks_sage_1.jsonl
Defaults: the 19 rank-2 curves of the BSD table and 5077a1, 3 <= p <= 100.

Conventions:
  * L_p(E,T) = sum_k c_k T^k with T = gamma - 1, gamma the topological generator of 1+pZ_p with chi(gamma) = 1+p,
    normalised by the interpolation property L_p(E,0) = (1-1/alpha)^2 L(E,1)/Omega_E, with Omega_E the full real
    period (2 w1 if disc > 0).  Sage's series(n) uses Riemann sums at level p^n; each coefficient is returned with
    its own provable absolute precision O(p^{m_k}) (Stein--Wuthrich, Math. Comp. 82 (2013), Prop. 3.? / Sage source),
    m_k decreasing in k.
  * r_p^upper := min{k : c_k != 0 to the precision known}, a certified upper bound for r_p = ord_{T=0} L_p(E,T).
    All coefficients below it are O(p^{m_k}) (zero to the working precision).
  * p-adic BSD (Mazur--Tate--Teitelbaum, in the form of Stein--Wuthrich Conj. 3.?): for good ordinary p,
        c_r = (1-1/alpha)^2 * prod_v c_v * |Sha| * Reg_p / (|E(Q)_tors|^2 * log_p(1+p)^r),
    with Reg_p = E.padic_regulator(p) (determinant of the cyclotomic p-adic height pairing on a basis, Sage's
    normalisation coincides with PARI's ellpadicregulator, checked on 389a1 and 5077a1).  We report
        sha_pred := c_r * |T|^2 * log_p(1+p)^r / ((1-1/alpha)^2 * prod c_v * Reg_p),
    a p-adic number whose valuation is the p-adic BSD prediction for ord_p |Sha| and which should be congruent to
    the analytic order of Sha of the classical BSD table.
  * Precision policy: start at n0 = 6 (p <= 7), 4 (p <= 30), 3 (p > 30); increase n by one while the leading
    coefficient c_{r_alg} is not certified nonzero with >= 2 significant digits and p^n <= 6*10^6.
"""
import argparse
import json
import sys
import time

from sage.all import EllipticCurve, Qp, primes, Integer, factorial

DEFAULT_CURVES = ["389a1", "433a1", "446d1", "563a1", "571b1", "643a1", "655a1", "664a1", "681c1", "707a1",
                  "709a1", "718b1", "794a1", "817a1", "916c1", "944e1", "997b1", "1001c1", "5077a1"]
PN_CAP = 6 * 10**6


def val_prec(c):
    """[valuation or -1 if zero to precision, absolute precision]"""
    if c == 0:
        return [-1, int(c.precision_absolute())]
    return [int(c.valuation()), int(c.precision_absolute())]


def analyse_curve(label, pmax, out, primes_only=None, pn_cap=PN_CAP):
    E = EllipticCurve(label)
    N = E.conductor()
    r = E.rank()
    gens = E.gens()
    assert len(gens) == r
    T = E.torsion_order()
    cp = E.tamagawa_product()
    print("== %s  N=%s  rank %s  gens %s  |T|=%s  prod c_p=%s  disc sign %s" % (label, N, r, gens, T, cp, E.discriminant().sign()), flush=True)
    for p in primes(3, pmax + 1):
        t0 = time.time()
        if primes_only and p not in primes_only:
            continue
        if N % p == 0:
            print("  p=%d: bad, skipped" % p, flush=True)
            continue
        ap = E.ap(p)
        if ap % p == 0:
            print("  p=%d: supersingular (a_p=%s), skipped" % (p, ap), flush=True)
            continue
        anomalous = int((ap - 1) % p == 0)
        L = E.padic_lseries(p)
        n = 6 if p <= 7 else (4 if p <= 30 else 3)
        rec = {"label": label, "N": int(N), "p": int(p), "ap": int(ap), "anomalous": anomalous, "r_alg": int(r)}
        try:
            while True:
                s = L.series(n, prec=r + 3)
                coefs = [s[k] for k in range(r + 2)]
                lead = coefs[r]
                ok = (lead != 0) and (lead.precision_absolute() - lead.valuation() >= 2)
                if ok or p**(n + 1) > pn_cap or n >= 10:
                    break
                n += 1
            cv = [val_prec(c) for c in coefs]
            rp_up = next((k for k in range(r + 2) if coefs[k] != 0), -1)
            lower_zero = int(all(coefs[k] == 0 for k in range(r)))
            prec = max(int(lead.precision_absolute()), 5) + 4
            R = E.padic_regulator(p, prec)
            K = Qp(p, prec + 6)
            alpha = L.alpha(prec + 6)
            eps = (1 - 1 / alpha)**2
            logg = K(1 + p).log()
            sha_pred = K(lead) * T**2 * logg**r / (K(eps) * cp * K(R))
            rec.update({"n": n, "series": str(s), "coef_val_prec": cv, "rp_upper": int(rp_up), "lower_zero": lower_zero,
                        "lead": str(lead), "v_lead": (int(lead.valuation()) if lead != 0 else -1),
                        "prec_lead": int(lead.precision_absolute()), "reg": str(R), "v_reg": int(R.valuation()) if R != 0 else -99,
                        "sha_pred": str(sha_pred), "v_sha": (int(sha_pred.valuation()) if sha_pred != 0 else -99),
                        "certified_lead": int(bool(ok)), "time_s": round(time.time() - t0, 2)})
            print("  p=%d a_p=%d%s n=%d  L_p(T) = %s" % (p, ap, " ANOMALOUS" if anomalous else "", n, s), flush=True)
            print("     [val,prec] k=0..%d: %s  r_p^upper=%d  lower zero: %d   Reg_p = %s   sha_pred = %s   [%.1fs]"
                  % (r + 1, cv, rp_up, lower_zero, R, sha_pred, time.time() - t0), flush=True)
        except Exception as e:  # record and continue
            rec.update({"error": repr(e), "n": n})
            print("  p=%d: ERROR %r" % (p, e), flush=True)
        out.write(json.dumps(rec) + "\n")
        out.flush()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--curves", default=",".join(DEFAULT_CURVES))
    ap.add_argument("--pmax", type=int, default=100)
    ap.add_argument("--out", default="compute/data/padic_ranks_sage.jsonl")
    ap.add_argument("--primes", default="", help="comma-separated list: only these primes (e.g. to redo one prime)")
    ap.add_argument("--pn-cap", type=int, default=PN_CAP, help="do not go beyond p^n > PN_CAP Riemann-sum terms (default 6e6)")
    a = ap.parse_args()
    from sage.misc.banner import version
    print("padic_ranks_sage.py  %s  pmax=%d  out=%s  primes=%s  pn_cap=%d" % (version(), a.pmax, a.out, a.primes or "all", a.pn_cap), flush=True)
    primes_only = [int(x) for x in a.primes.split(",") if x.strip()] or None
    with open(a.out, "a") as out:
        for lab in a.curves.split(","):
            analyse_curve(lab.strip(), a.pmax, out, primes_only, a.pn_cap)


if __name__ == "__main__":
    main()
