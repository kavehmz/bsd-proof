#!/usr/bin/env sage -python
"""Certify 0 < (L''(389a1,1)/2)/(Omega_full*Reg_BSD) < 2.

No rationality, BSD formula, or Sha finiteness is assumed. Full saturation
is proved by a finite rational-point search, explicit height bounds, and
rank-two lattice geometry; eclib provides an independent cross-check.
All real values in the inequality are rigorous Arb balls. Canonical heights
use exact doubling and a verified homogeneous Bezout error bound.

Run from the repository root:
  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/certify_bsd_interval.py

See docs/synthesis/bsd-archimedean-bound.md for the proof and normalizations.
"""

import argparse
import hashlib
import json
from pathlib import Path

from sage.all import (EllipticCurve, PolynomialRing, QQ, RealBallField, ZZ,
                      gcd, lcm, matrix, vector)
from sage.env import SAGE_VERSION
from sage.libs.eclib.all import mwrank_MordellWeil


def endpoints(ball):
    return [str(ball.lower().exact_rational()), str(ball.upper().exact_rational())]


def enclose_interval(R, low, high):
    low, high = QQ(low), QQ(high)
    assert low <= high
    return R((low + high) / 2).add_error(R((high - low) / 2))


def ball_record(ball):
    assert ball.is_finite()
    return {"ball": str(ball), "rational_endpoints": endpoints(ball)}


def bezout_certificate():
    """Find and verify integer identities A*F+B*G=D*X^7,D*Z^7."""
    ring = PolynomialRing(QQ, names=("X", "Z"))
    X, Z = ring.gens()
    F = X**4 + 4*X**2*Z**2 - 2*X*Z**3 + 3*Z**4
    G = 4*X**3*Z + 4*X**2*Z**2 - 8*X*Z**3 + Z**4
    cubic_monomials = [X**(3-i)*Z**i for i in range(4)]
    degree7_monomials = [X**(7-i)*Z**i for i in range(8)]
    polys = [m*F for m in cubic_monomials] + [m*G for m in cubic_monomials]
    M = matrix(QQ, [[polynomial.monomial_coefficient(monomial)
                     for polynomial in polys] for monomial in degree7_monomials])
    targets = [vector(QQ, [1] + [0]*7), vector(QQ, [0]*7 + [1])]
    solutions = [M.solve_right(target) for target in targets]
    D = ZZ(lcm([c.denominator() for solution in solutions for c in solution]))
    integral_solutions = [[ZZ(D*c) for c in solution] for solution in solutions]
    for coeffs, target in zip(integral_solutions, (X**7, Z**7)):
        assert sum(c*f for c, f in zip(coeffs, polys)) == D*target
    lower_constant = max(sum(abs(c) for c in coeffs) for coeffs in integral_solutions)
    upper_constant = max(sum(abs(c) for c in F.coefficients()),
                         sum(abs(c) for c in G.coefficients()))
    assert D > 0 and lower_constant >= 1 and upper_constant >= 1
    return D, ZZ(max(lower_constant, upper_constant)), {
        "F": str(F), "G": str(G), "D": int(D),
        "cubic_coefficient_order": [str(m) for m in cubic_monomials],
        "X7_identity_A_coefficients": list(map(int, integral_solutions[0][:4])),
        "X7_identity_B_coefficients": list(map(int, integral_solutions[0][4:])),
        "Z7_identity_A_coefficients": list(map(int, integral_solutions[1][:4])),
        "Z7_identity_B_coefficients": list(map(int, integral_solutions[1][4:])),
        "identities_checked_exactly": True,
        "archimedean_lower_constant": int(lower_constant),
        "archimedean_upper_constant": int(upper_constant),
        "height_step_bound": "abs(h_x(2P)-4*h_x(P)) <= log(C)",
        "C": int(max(lower_constant, upper_constant)),
    }


def canonical_height_ball(P, doublings, R, D, height_constant):
    """BSD normalization: limit 4^-k h_x(2^k P), not Silverman's half."""
    x = P[0]
    numerator, denominator = ZZ(x.numerator()), ZZ(x.denominator())
    assert denominator > 0 and gcd(numerator, denominator) == 1
    gcds = []
    for _ in range(doublings):
        X, Z = numerator, denominator
        new_numerator = X**4 + 4*X**2*Z**2 - 2*X*Z**3 + 3*Z**4
        new_denominator = 4*X**3*Z + 4*X**2*Z**2 - 8*X*Z**3 + Z**4
        assert new_denominator != 0
        cancellation = gcd(new_numerator, new_denominator)
        assert D % cancellation == 0
        gcds.append(int(cancellation))
        numerator, denominator = new_numerator // cancellation, new_denominator // cancellation
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
    # Independent exact group-law check of the rational duplication formula.
    assert QQ(numerator) / denominator == (2**doublings * P)[0]
    H = max(abs(numerator), denominator)
    approximate = R(H).log() / ZZ(4)**doublings
    error = R(height_constant).log() / (3 * ZZ(4)**doublings)
    height = approximate.add_error(error)
    return height, {
        "point": [str(a) for a in P.xy()],
        "doublings": doublings,
        "x_height_integer": str(H),
        "x_numerator_bits": int(abs(numerator).nbits()),
        "x_denominator_bits": int(denominator.nbits()),
        "cancelled_gcds": gcds,
        "group_law_crosscheck_exact": True,
        "finite_height_approximation": ball_record(approximate),
        "tail_error_bound": ball_record(error),
        "canonical_height": ball_record(height),
    }


def bisect_root(low, high, steps):
    """Rational sign bisection; three disjoint initial brackets exhaust cubic."""
    low, high = QQ(low), QQ(high)
    polynomial = lambda x: 4*x**3 + 4*x**2 - 8*x + 1
    flo, fhi = polynomial(low), polynomial(high)
    assert flo*fhi < 0
    for _ in range(steps):
        middle = (low + high) / 2
        fmid = polynomial(middle)
        assert fmid != 0
        if flo*fmid < 0:
            high, fhi = middle, fmid
        else:
            low, flo = middle, fmid
    assert polynomial(low)*polynomial(high) < 0
    return low, high


def minimum_height_certificate(E, R, D, height_constant, doublings):
    """Prove every nonzero rational point has BSD height greater than 3/10.

    The global bound |hat_h-h_x| <= log(1728)/3 = log(12) reduces any
    putative counterexample to all reduced rational x of height <=16.
    """
    assert height_constant == 1728
    threshold = QQ(3)/10
    assert R(threshold) + R(12).log() < R(17).log()
    records = []
    tested_rationals = 0
    for denominator in range(1, 17):
        for numerator in range(-16, 17):
            if gcd(numerator, denominator) != 1:
                continue
            tested_rationals += 1
            x = QQ(numerator)/denominator
            square = 4*x**3 + 4*x**2 - 8*x + 1
            if not square.is_square():
                continue
            square_root = QQ(square.sqrt())
            P = E(x, (square_root-1)/2)
            height, record = canonical_height_ball(P, doublings, R, D, height_constant)
            assert height > R(threshold)
            records.append(record)
    assert records
    minimum_lower_endpoint = min(QQ(record["canonical_height"]["rational_endpoints"][0])
                                 for record in records)
    return {
        "height_lower_bound_for_all_nonzero_points": "3/10",
        "global_height_difference_bound": "log(1728)/3 = log(12)",
        "naive_height_reduction": "3/10+log(12)<log(17)",
        "max_absolute_numerator_and_denominator": 16,
        "reduced_rational_x_values_tested": tested_rationals,
        "curve_points_up_to_negation_found": len(records),
        "negation_convention": "-(x,y)=(x,-1-y); x-height and canonical height are unchanged",
        "all_candidate_heights_strictly_above_threshold": True,
        "minimum_candidate_height_lower_endpoint": str(minimum_lower_endpoint),
        "candidate_height_certificates": records,
        "rank_two_lattice_regulator_lower_bound": "3/4*(3/10)^2 = 27/400",
    }


def real_period_ball(R, root_steps, agm_steps):
    brackets = [(-3, -1), (0, QQ(1)/4), (QQ(1)/2, 1)]
    roots = [bisect_root(a, b, root_steps) for a, b in brackets]
    e3, e2, e1 = [enclose_interval(R, a, b) for a, b in roots]
    assert e1 > e2 and e2 > e3
    gap = e1 - e3
    m = (e2 - e3) / gap
    assert m > 0 and m < 1
    arithmetic, geometric = R(1), (1-m).sqrt()
    for _ in range(agm_steps):
        arithmetic, geometric = ((arithmetic + geometric)/2,
                                 (arithmetic*geometric).sqrt())
    # The true AGM is bracketed by the geometric and arithmetic iterates.
    agm = enclose_interval(R, geometric.lower().exact_rational(),
                          arithmetic.upper().exact_rational())
    identity_period = R.pi() / (gap.sqrt()*agm)
    full_period = 2 * identity_period
    assert full_period > 4 and full_period < 6
    return full_period, {
        "completed_square_cubic": "u^2=x^3+x^2-2*x+1/4; u=y+1/2",
        "root_initial_brackets_increasing": [[str(a), str(b)] for a, b in brackets],
        "root_bisection_steps": root_steps,
        "root_rational_brackets_increasing": [[str(a), str(b)] for a, b in roots],
        "all_root_sign_checks_exact": True,
        "modulus_squared_m": ball_record(m),
        "agm_steps": agm_steps,
        "agm_enclosure": ball_record(agm),
        "identity_component_period": ball_record(identity_period),
        "real_components": 2,
        "full_real_period": ball_record(full_period),
        "formula": "Omega_full = 2*pi/(sqrt(e1-e3)*AGM(1,sqrt(1-m)))",
    }


def certify(args):
    E = EllipticCurve([0, 1, 1, -2, 0])
    input_path = Path(args.analytic_input)
    input_bytes = input_path.read_bytes()
    analytic = next(r for r in json.loads(input_bytes)["records"] if r["label"] == "389a1")
    assert analytic["ainvs"] == [0, 1, 1, -2, 0]
    assert analytic["algebraic_rank"] == analytic["analytic_rank_certified"] == 2
    leading_low, leading_high = map(QQ, analytic["L_leading_rational_endpoints"])
    R = RealBallField(args.bits)
    leading = enclose_interval(R, leading_low, leading_high)
    assert leading > 0

    assert E.discriminant() == 389 and E.c4() == 112
    point_counts = {str(p): 1 + sum((y*y+y-x*x*x-x*x+2*x) % p == 0
                                  for x in range(p) for y in range(p))
                    for p in (2, 3, 5)}
    assert point_counts == {"2": 5, "3": 6, "5": 9}
    # Prime-to-residue-characteristic torsion injection at these good primes
    # proves t=1; discriminant 389 and c4=112 give sole Kodaira type I1, c389=1.
    torsion_order, tamagawa_product = 1, 1

    raw_A, raw_B = E(-2, 0), E(4, 8)
    mw = mwrank_MordellWeil(E.mwrank_curve(), verbose=args.verbose)
    mw.process([[-2, 0, 1], [4, 8, 1]], saturation_bound=0)
    ok, index, unsaturated = mw.saturate(max_prime=-1, min_prime=2)
    assert ok and int(index) == 3 and str(unsaturated).replace(" ", "") == "[]"
    assert mw.rank() == 2
    P, Q = E(-1, 1), E(0, -1)
    assert raw_A == -P + 2*Q and raw_B == P + Q
    raw_matrix = matrix(ZZ, [[-1, 1], [2, 1]])
    assert abs(raw_matrix.det()) == index

    D, height_constant, bezout = bezout_certificate()
    computed = [canonical_height_ball(point, args.doublings, R, D, height_constant)
                for point in (P, Q, P+Q)]
    hP, hQ, hPQ = [pair[0] for pair in computed]
    pairing = (hPQ-hP-hQ) / 2
    regulator = hP*hQ-pairing**2
    assert hP > 0 and regulator > 0
    minimum_height = minimum_height_certificate(
        E, R, D, height_constant, max(5, args.doublings-1))
    # If this rank-two lattice had index >=2 in the full Mordell-Weil
    # lattice, its regulator would be >=4*(27/400)=27/100.
    assert regulator < R(QQ(27)/100)
    period, period_record = real_period_ball(R, args.root_steps, args.agm_steps)
    denominator = period*regulator*tamagawa_product
    quotient = leading*torsion_order**2 / denominator
    assert quotient > 0 and quotient < 2
    # Comfortable rational bounds for review, not just a decimal near 1.
    assert quotient > R(QQ(9)/10) and quotient < R(QQ(11)/10)
    package_versions = {}
    for name in ("eclib", "libflint"):
        for path in Path(".tools/sage/conda-meta").glob(name+"-*.json"):
            metadata = json.loads(path.read_text())
            package_versions[name] = metadata.get("version")

    return {
        "label": "389a1", "ainvs": [0, 1, 1, -2, 0],
        "sage_version": SAGE_VERSION, "package_versions": package_versions,
        "precision_bits": args.bits,
        "analytic_input": str(input_path),
        "analytic_input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "algebraic_and_analytic_rank": 2,
        "leading_L_coefficient": ball_record(leading),
        "minimal_discriminant": 389, "c4": 112,
        "good_prime_point_counts": point_counts,
        "torsion_order": torsion_order, "tamagawa_product": tamagawa_product,
        "saturation": {
            "input_basis": [[-2, 0], [4, 8]], "max_prime": -1, "min_prime": 2,
            "all_prime_saturation_certified": bool(ok), "exact_index": int(index),
            "unsaturated_primes": str(unsaturated),
            "eclib_output_basis": [list(map(int, point)) for point in mw.points()],
            "chosen_full_basis": [[-1, 1], [0, -1]],
            "raw_coordinates_in_chosen_basis_columns": [[-1, 1], [2, 1]],
            "coordinate_relations_checked_exactly": True,
        },
        "height_normalization": "BSD/Cremona height = lim_k 4^(-k)*h_x(2^k P); twice Silverman height",
        "bezout_height_certificate": bezout,
        "height_computations": [pair[1] for pair in computed],
        "independent_full_basis_certificate": {
            "method": "finite exact x-coordinate search, certified canonical heights, rank-two lattice inequality",
            "rank_upper_bound_from_analytic_input": 2,
            "positive_regulator_proves_point_independence": True,
            "minimum_height_certificate": minimum_height,
            "index_at_least_two_would_force_regulator_at_least": "27/100",
            "computed_regulator_strictly_below_27_over_100": True,
            "chosen_basis_has_index_one": True,
        },
        "off_diagonal_height_pairing": ball_record(pairing),
        "saturated_BSD_regulator": ball_record(regulator),
        "period_certificate": period_record,
        "Omega_full_times_regulator_times_Tam": ball_record(denominator),
        "bsd_real_quotient": ball_record(quotient),
        "certified_coarse_rational_interval": ["9/10", "11/10"],
        "zero_less_than_quotient_less_than_two": True,
        "scope": "Archimedean inequality only: no rationality, integrality, Sha finiteness, or BSD leading-term equality is inferred.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=128)
    parser.add_argument("--doublings", type=int, default=6)
    parser.add_argument("--root-steps", type=int, default=160)
    parser.add_argument("--agm-steps", type=int, default=8)
    parser.add_argument("--analytic-input", default="compute/data/analytic_rank_certificates.json")
    parser.add_argument("--out", default="compute/data/bsd_archimedean_interval.json")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    assert args.bits >= 64 and args.doublings >= 5 and args.root_steps >= 64 and args.agm_steps >= 4
    result = certify(args)
    Path(args.out).write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "label", "saturation", "saturated_BSD_regulator",
        "Omega_full_times_regulator_times_Tam", "bsd_real_quotient",
        "certified_coarse_rational_interval", "zero_less_than_quotient_less_than_two")}, indent=2))


if __name__ == "__main__":
    main()
