#!/usr/bin/env sage -python
"""Certify trivial primary groups at 2, 3, 389 for E=389a1.

The proof is in docs/synthesis/exceptional-prime-finiteness.md.
Nonzero finite-precision coefficients give upper bounds, not vanishing
of lower coefficients. Exact lower bounds come from rank and Kato's theorem.

  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/certify_exceptional_primes.py
"""

import json
from pathlib import Path
from sage.all import EllipticCurve, Qp, ZZ
from sage.env import SAGE_VERSION


def main():
    E = EllipticCurve([0, 1, 1, -2, 0])
    assert E.conductor() == 389
    rank_data = E.pari_curve().ellrank()
    assert int(rank_data[0]) == int(rank_data[1]) == 2
    assert E.torsion_order() == 1
    selmer_2_pari = int(E.selmer_rank(algorithm="pari"))
    # Call the eclib object directly to bypass Sage's algorithm-independent cache.
    selmer_2_mwrank = int(E.mwrank_curve().selmer_rank())
    assert selmer_2_pari == selmer_2_mwrank == 2
    assert E.galois_representation().is_surjective(389) is True
    basis_certificate = Path(__file__).resolve().parents[1] / "data" / "bsd_archimedean_interval.json"
    basis_data = json.loads(basis_certificate.read_text())["saturation"]
    assert basis_data["all_prime_saturation_certified"]
    assert basis_data["chosen_full_basis"] == [[-1, 1], [0, -1]]
    # Q and P+Q are another full basis; the 3-adic regulator must not use
    # the unsaturated raw descent points, whose index is divisible by 3.
    P, Q = E(-1, 1), E(0, -1)
    assert P + Q == E(4, 8)

    records = []
    for p, level, first_degree in ((3, 3, 2), (389, 2, 3)):
        split = bool(E.has_split_multiplicative_reduction(p))
        assert split == (p == 389)
        if p == 3:
            assert E.has_good_reduction(p) and E.ap(p) % p != 0
        series = E.padic_lseries(p, implementation="eclib").series(
            level, prec=first_degree + 2
        )
        lead = series[first_degree]
        assert lead != 0 and lead.valuation() == 0
        assert lead.precision_absolute() >= 1
        gamma_log_valuation = int(Qp(p, 12)(1 + p).log().valuation())
        assert gamma_log_valuation == 1
        if p == 3:
            regulator = E.pari_curve().ellpadicregulator(3, 10, [[0, -1], [4, 8]])
            regulator_valuation = int(regulator.valuation(3))
            regulator_precision = int(regulator.padicprec(3))
            multiplier_valuation = 2 * int(ZZ(E.Np(3)).valuation(3))
            algebraic_factor_valuation = multiplier_valuation + regulator_valuation - 2
            extra = {"epsilon_valuation": multiplier_valuation,
                     "regulator_engine": "PARI ellpadicregulator",
                     "regulator_basis": [[0, -1], [4, 8]]}
        else:
            regulator = E.padic_regulator(p, prec=8)
            regulator_valuation = int(regulator.valuation())
            regulator_precision = int(regulator.precision_absolute())
            linvariant = E.tate_curve(ZZ(p)).L_invariant(prec=8)
            assert linvariant != 0
            algebraic_factor_valuation = int(linvariant.valuation()) + regulator_valuation - 3
            independent_bound = int(E.sha().p_primary_bound(p))
            assert independent_bound == 0
            extra = {"L_invariant": str(linvariant),
                     "L_invariant_valuation": int(linvariant.valuation()),
                     "regulator_engine": "Sage Tate-curve p-adic regulator",
                     "sage_p_primary_bound_exponent": independent_bound}
        assert regulator_precision > regulator_valuation
        order_bound = int(lead.valuation()) - algebraic_factor_valuation
        assert order_bound == 0
        records.append({
            "p": p, "reduction": "split multiplicative" if split else "good ordinary",
            "a_p": int(E.ap(p)), "approximation_level": level,
            "series": str(series), "nonzero_coefficient_degree": first_degree,
            "nonzero_coefficient": str(lead),
            "valuation": int(lead.valuation()),
            "absolute_precision": int(lead.precision_absolute()),
            "p_adic_analytic_rank_certified": first_degree,
            "characteristic_series_order_certified": 2,
            "exceptional_T_factor_required": split,
            "sha_primary_finite": True,
            "regulator": str(regulator), "regulator_valuation": regulator_valuation,
            "regulator_absolute_precision": regulator_precision,
            "log_gamma_valuation": gamma_log_valuation,
            "algebraic_multiplier_times_regulator_valuation": algebraic_factor_valuation,
            "sha_primary_order_upper_exponent": order_bound,
            "sha_primary_order": 1,
            **extra,
        })
    result = {
        "curve": "389a1", "ainvs": [0, 1, 1, -2, 0], "sage_version": SAGE_VERSION,
        "rank_certificate": str(rank_data), "torsion_order": 1,
        "two_selmer_dimensions": {"pari": selmer_2_pari, "mwrank": selmer_2_mwrank},
        "sha_2_primary_order": 1, "mod_389_representation_surjective": True,
        "records": records,
        "basis_certificate": str(basis_certificate),
        "scope": "Trivial primary groups at {2,3,389}; no full Sha finiteness claim",
        "precision_warning": "Lower coefficients reported O(p^k) are not exact zero certificates",
    }
    out = Path(__file__).resolve().parents[1] / "data" / "exceptional_primes_389a1.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
