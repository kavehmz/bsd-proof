#!/usr/bin/env sage -python
"""Exact Kurihara witness for 389a1 at p=5; see the continuation report.

Run from the repository root:
  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/kurihara_witness.py

All modular-symbol, finite-field, and cyclotomic operations are exact.
Two independent modular-symbol backends must agree at every input cusp.
No floating-point L-value or conjectural Sha order enters the certificate.
"""

import json
from pathlib import Path

from sage.all import CyclotomicField, EllipticCurve, GF, QQ, gcd, primitive_root
from sage.env import SAGE_VERSION


def main():
    E = EllipticCurve("389a1")
    p, primes = 5, (41, 61)
    n = primes[0] * primes[1]
    symbols = [E.modular_symbol(sign=1, implementation=engine)
               for engine in ("eclib", "sage")]
    rank_certificate = E.pari_curve().ellrank()
    assert int(rank_certificate[0]) == int(rank_certificate[1]) == 2
    assert E.galois_representation().is_surjective(p) is True
    assert E.conductor() == 389 and E.ap(p) % p != 0
    assert not E.has_cm()

    roots = {l: int(primitive_root(l)) for l in primes}
    logs = {l: {pow(roots[l], k, l): k for k in range(l - 1)}
            for l in primes}
    assert all(len(logs[l]) == l - 1 for l in primes)
    prime_data = []
    checked_cusps = 0

    def symbol(a, denominator):
        nonlocal checked_cusps
        x = QQ(a) / denominator
        values = [m(x) for m in symbols]
        assert values[0] == values[1], (x, values)
        assert values[0].denominator() % p != 0
        checked_cusps += 1
        return values[0]

    zero = symbol(0, 1)
    assert zero == 0
    K = CyclotomicField(p)
    zeta = K.gen()
    pi = zeta - 1
    twisted_prime = {}
    for l in primes:
        ap = int(E.ap(l))
        ideal_exponent = int(gcd(l - 1, ap - l - 1).valuation(p))
        assert ideal_exponent == 1  # I_l = (5), so reduction mod 5 is sufficient.
        weighted_sum, augmentation, twist = QQ(0), QQ(0), K(0)
        for a in range(1, l):
            value = symbol(a, l)
            weighted_sum += value * logs[l][a]
            augmentation += value
            twist += value * zeta ** (logs[l][a] % p)
        assert augmentation == (ap - 2) * zero
        assert GF(p)(weighted_sum) == 0
        twisted_prime[l] = twist
        prime_data.append({"ell": l, "a_ell": ap, "primitive_root": roots[l],
                           "I_ell_exponent": ideal_exponent,
                           "weighted_sum": str(weighted_sum), "delta_mod_5": 0})

    # F[mask] evaluates the SAME modulus-n symbol sum at inflated characters.
    # Non-full masks are imprimitive; their Euler factors are checked below.
    F = [K(0) for _ in range(4)]
    weighted_sum = QQ(0)
    units = 0
    for a in range(1, n):
        if gcd(a, n) != 1:
            continue
        value = symbol(a, n)
        k, h = (logs[l][a % l] for l in primes)
        weighted_sum += value * k * h
        u, v = zeta ** (k % p), zeta ** (h % p)
        for mask, weight in enumerate((K(1), u, v, u * v)):
            F[mask] += value * weight
        units += 1
    delta = int(GF(p)(weighted_sum))
    assert units == 2400 and delta == 4 and weighted_sum == 244
    assert F[0] == (E.ap(41) - 2) * (E.ap(61) - 2) * zero
    for i, l in enumerate(primes):
        q = primes[1 - i]
        chi_q = zeta ** (logs[l][q % l] % p)
        assert F[1 + i] == (E.ap(q) - chi_q - chi_q ** -1) * twisted_prime[l]

    difference = F[3] - F[1] - F[2] + F[0]
    quotient = difference / pi ** 2
    # The unique prime above 5 has residue degree one: v_5(Norm D) = v_pi(D).
    valuation = int(difference.norm().valuation(p))
    assert valuation == 2
    assert all(c.denominator() % p != 0 for c in quotient.list())
    residue = int(GF(p)(sum(quotient.list())))  # zeta -> 1 in the residue field.
    assert residue == delta

    result = {
        "curve": "389a1", "ainvs": [int(a) for a in E.a_invariants()],
        "sage_version": SAGE_VERSION, "p": p, "a_p": int(E.ap(p)),
        "rank_certificate_pari": str(rank_certificate), "rank": 2,
        "mod_5_representation_surjective": True, "non_CM": True,
        "modular_symbol_normalization": "least positive real Neron period; sign +1",
        "backends": ["eclib", "sage"], "all_backend_values_equal": True,
        "checked_cusps": checked_cusps, "symbol_at_zero": str(zero),
        "primes": prime_data, "n": n, "unit_residues": units,
        "weighted_sum": str(weighted_sum), "delta_mod_5": delta,
        "cyclotomic_generator": "zeta = primitive fifth root; pi = zeta - 1",
        "character_sums_by_mask": [str(f) for f in F],
        "mixed_difference": str(difference), "mixed_difference_norm": str(difference.norm()),
        "mixed_difference_pi_valuation": valuation,
        "difference_divided_by_pi_squared": str(quotient),
        "mixed_derivative_residue": residue, "imprimitive_Euler_relations_checked": True,
        "arithmetic_conclusion_using_Kim_Theorem_3_1":
            "ord(delta)=2; Sel_5_infinity=(Q_5/Z_5)^2; Sha[5^infinity]=0",
        "scope": "one curve and one prime; no complex analytic rank certification or full BSD claim"
    }
    out = Path(__file__).resolve().parents[1] / "data" / "kurihara_389a1_p5.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
