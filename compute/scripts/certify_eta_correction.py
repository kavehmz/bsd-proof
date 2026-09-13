#!/usr/bin/env sage -python
"""Certify the even eta correction integral for the normalized form of 389a1.

  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/certify_eta_correction.py

The Fricke fold and all three explicit error bounds are proved in
docs/synthesis/eta-correction-certificate.md. No floating-point eta
evaluation or assumed BSD equality is used.
"""

import argparse
import json
from pathlib import Path

from sage.all import ComplexBallField, EllipticCurve, QQ, RealBallField, divisors
from sage.env import SAGE_VERSION


def endpoints(ball):
    return [str(ball.lower().exact_rational()), str(ball.upper().exact_rational())]


def polynomial_without_constant(q, coefficients, C):
    answer = C(0)
    for a in reversed(coefficients[1:]):
        answer = answer * q + a
    return q * answer


def certify(bits=96, cutoff=40, decay=60):
    E = EllipticCurve([0, 1, 1, -2, 0])
    N = int(E.conductor())
    assert N == 389 and E.root_number() == 1
    R, C = RealBallField(bits), ComplexBallField(bits)
    pi = R.pi()
    c = 2 * pi / R(N).sqrt()
    T = R(cutoff)
    A = R(QQ(N + 1) / 24)
    assert T > c and A > 1 / (2 * c)
    M = K = int((R(decay) / c).upper().ceil())
    f_coefficients = list(map(int, E.anlist(M)))
    eta_coefficients = [QQ(0)] + [QQ(sum(divisors(n))) / n for n in range(1, K + 1)]
    assert f_coefficients[0] == 0 and f_coefficients[1] == 1
    assert all(abs(a) <= 2*n for n, a in enumerate(f_coefficients))
    assert all(0 < eta_coefficients[n] <= n for n in range(1, K + 1))
    cc, AA, cpi = C(c), C(A), C(pi)

    def integrand(t, analytic):
        q = (-t).exp()
        qN = (-N * t).exp()
        fM = polynomial_without_constant(q, f_coefficients, C)
        eta1 = polynomial_without_constant(q, eta_coefficients, C)
        etaN = polynomial_without_constant(qN, eta_coefficients, C)
        W = -AA * t + (t / cc).log(analytic=analytic) / 2 - eta1 - etaN
        return fM * W**2 / cpi

    tolerance = R(2) ** (-bits + 32)
    finite = C.integral(integrand, cc, C(T),
                        abs_tol=tolerance, rel_tol=tolerance,
                        eval_limit=100000)
    assert finite.real().is_finite() and finite.imag().is_finite()
    assert finite.imag().contains_zero()

    q = (-c).exp()
    B = 2 * q / (1 - q)**2
    P0 = A*c + B
    coefficient_error = (2/pi * q**(M+1)/(1-q)
                         * (P0**2 + 2*A*P0/(M+1) + 2*A**2/(M+1)**2))
    eta_error_uniform = (2 * q**(K+1)
                         * ((K+1)/(1-q) + q/(1-q)**2))
    eta_error = (4 * eta_error_uniform/pi * q/(1-q)**2
                 * (A*(c+1) + B))
    qT = (-T).exp()
    PT = A*T + B
    integration_error = (2/pi * qT/(1-qT)**2
                         * (PT**2 + 2*A*PT + 2*A**2))
    correction = finite.real().add_error(coefficient_error + eta_error + integration_error)
    assert correction > 0
    return {
        "curve": "389a1", "ainvs": [0, 1, 1, -2, 0], "conductor": N,
        "root_number": 1, "sage_version": SAGE_VERSION,
        "precision_bits": bits, "t_cutoff": cutoff, "decay_target": decay,
        "fourier_cutoff": M, "eta_cutoff": K,
        "normalization": "f=q+sum_(n>=2) a_n q^n; x=log(sqrt(N)*y); rho=y*f(iy); U=log(eta(iy)*eta(i*N*y))+x/2",
        "folded_integral": "(1/pi)*integral_(c,infinity) f(i*t/(2*pi))*W(t)^2 dt; c=2*pi/sqrt(N)",
        "eta_coefficients": "b_n=sigma_1(n)/n, computed as exact rational numbers; 0<b_n<=n",
        "finite_integral": str(finite),
        "coefficient_error_bound": str(coefficient_error),
        "eta_uniform_error_bound": str(eta_error_uniform),
        "eta_integral_error_bound": str(eta_error),
        "integration_error_bound": str(integration_error),
        "correction_integral": str(correction),
        "correction_rational_endpoints": endpoints(correction),
        "strictly_positive": True,
        "scope": "Proves the eta second-jet correction is nonzero on the actual curve; does not prove arithmetic rationality, integrality, or BSD.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=96)
    parser.add_argument("--cutoff", type=int, default=40)
    parser.add_argument("--decay", type=int, default=60)
    parser.add_argument("--out", default="compute/data/eta_correction_389a1.json")
    args = parser.parse_args()
    assert args.bits >= 64 and args.cutoff >= 20 and args.decay >= 30
    result = certify(args.bits, args.cutoff, args.decay)
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
