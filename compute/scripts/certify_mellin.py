#!/usr/bin/env sage -python
"""Rigorous Mellin-integral certificates of analytic ranks two and three.

The exact lower bound uses descent, Gross--Zagier--Kolyvagin, and root number.
The upper bound uses Arb integration, Hasse coefficient bounds, and explicit
tails. It does not use ellanalyticrank, numerical BSD, or GRH.

  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/certify_mellin.py

See docs/synthesis/analytic-rank-certificates.md for the full error proof.
"""

import argparse
import json
from pathlib import Path

from sage.all import ComplexBallField, EllipticCurve, QQ, RealBallField, factorial
from sage.env import SAGE_VERSION


def endpoints(ball):
    """Exact dyadic rational outward endpoints, rather than rounded decimals."""
    return [str(ball.lower().exact_rational()), str(ball.upper().exact_rational())]


def certify(label, bits, cutoff):
    E = EllipticCurve(label)
    rank_certificate = E.pari_curve().ellrank()
    rank_lower, rank_upper = int(rank_certificate[0]), int(rank_certificate[1])
    assert rank_lower == rank_upper and rank_lower in (2, 3)
    w = int(E.root_number())
    # Rank >=2 excludes analytic rank 0 and 1 by GZK. Functional equation
    # then gives analytic rank >=2 (w=+1), respectively >=3 (w=-1).
    k = 2 if w == 1 else 3
    assert k == rank_lower
    N = int(E.conductor())
    R, C = RealBallField(bits), ComplexBallField(bits)
    c = 2 * R.pi() / R(N).sqrt()
    cc = C(c)
    M = int((R(cutoff) / c).upper().ceil())
    T = R(cutoff)
    assert T > c
    coeffs = list(map(int, E.anlist(M)))
    assert len(coeffs) == M + 1 and coeffs[0] == 0 and coeffs[1] == 1
    assert all(abs(a) <= 2 * n for n, a in enumerate(coeffs))

    def integrand(t, analytic):
        q = (-t).exp()
        polynomial = C(0)
        for a in reversed(coeffs[1:]):
            polynomial = polynomial * q + a
        # Passing the analytic flag is essential for valid Arb quadrature.
        return 2 / cc * q * polynomial * (t / cc).log(analytic=analytic) ** k

    tolerance = R(2) ** (-bits + 24)
    finite_integral = C.integral(
        integrand, cc, C(T), abs_tol=tolerance, rel_tol=tolerance,
        eval_limit=100000,
    )
    assert finite_integral.real().is_finite() and finite_integral.imag().is_finite()
    assert finite_integral.imag().contains_zero()
    q, qT = (-c).exp(), (-T).exp()
    coefficient_tail = (4 * factorial(k) / c ** (k + 1) / (M + 1) ** k
                        * q ** (M + 1) / (1 - q))
    integration_tail = (4 * factorial(k) / c ** (k + 1) * qT / (1 - qT) ** 2
                        * sum(T ** j / factorial(j) for j in range(k + 1)))
    completed_derivative = finite_integral.real().add_error(
        coefficient_tail + integration_tail
    )
    assert completed_derivative > 0
    # All lower L derivatives vanish by the independent lower bound, so
    # Lambda^(k)(1) = c^(-1) L^(k)(1).
    leading = c * completed_derivative / factorial(k)
    coarse = {"389a1": (QQ(759) / 1000, QQ(760) / 1000),
              "5077a1": (QQ(1731) / 1000, QQ(1733) / 1000)}
    if label in coarse:
        lo, hi = coarse[label]
        assert leading > R(lo) and leading < R(hi)

    return {
        "label": label, "ainvs": [int(a) for a in E.a_invariants()],
        "conductor": N, "root_number": w,
        "algebraic_rank_certificate_pari": str(rank_certificate),
        "algebraic_rank": rank_lower, "analytic_rank_certified": k,
        "lower_bound_inputs": ["exact descent rank at least two",
                               "Gross--Zagier--Kolyvagin analytic-rank-zero/one theorem",
                               "exact root number and functional equation"],
        "precision_bits": bits, "t_cutoff": cutoff, "coefficient_cutoff": M,
        "coefficient_bound": "abs(a_n) <= d(n)*sqrt(n) <= 2*n",
        "finite_integral": str(finite_integral),
        "coefficient_tail_bound": str(coefficient_tail),
        "integration_tail_bound": str(integration_tail),
        "completed_derivative": str(completed_derivative),
        "completed_derivative_rational_endpoints": endpoints(completed_derivative),
        "L_derivative_divided_by_factorial": str(leading),
        "L_leading_rational_endpoints": endpoints(leading),
        "completed_derivative_positive": True,
        "conclusion": "BSD rank equality for this curve",
        "scope": "Does not prove full Sha finiteness or the BSD leading-term formula",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curves", default="389a1,5077a1")
    parser.add_argument("--bits", type=int, default=128)
    parser.add_argument("--cutoff", type=int, default=80)
    parser.add_argument("--out", default="compute/data/analytic_rank_certificates.json")
    args = parser.parse_args()
    assert args.bits >= 64 and args.cutoff >= 20
    records = [certify(label, args.bits, args.cutoff) for label in args.curves.split(",")]
    result = {"sage_version": SAGE_VERSION,
              "method": "rigorous Arb integration with separately bounded infinite tails",
              "records": records}
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
