#!/usr/bin/env sage -python
"""Certify a nonzero quadratic MTT coefficient for E: y^2=x^3+39x at 5.

The proof is docs/synthesis/cm-derivative-nonvanishing-attack.md.
Every displayed residue is computed from exact rational modular symbols
and finite integer Hensel lifts. The infinite-measure error is proved in
the note; comparison of successive levels is only an independent check.

DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
    compute/scripts/certify_cm39_padic.py
"""

import hashlib
import json
from pathlib import Path

from sage.all import EllipticCurve, QQ, ZZ
from sage.env import SAGE_VERSION


def hensel(residue, prime, exponent, polynomial):
    """Unique simple-root lift, verified entirely with integer arithmetic."""
    root, modulus = residue, prime
    assert polynomial(root) % prime == 0
    for _ in range(1, exponent):
        roots = [
            root + j * modulus
            for j in range(prime)
            if polynomial(root + j * modulus) % (prime * modulus) == 0
        ]
        assert len(roots) == 1
        root = roots[0]
        modulus *= prime
    assert polynomial(root) % modulus == 0
    return root


def rational_mod(x, modulus):
    n, d = int(x.numerator()), int(x.denominator())
    assert ZZ(d).gcd(modulus) == 1
    return n * pow(d, -1, modulus) % modulus


def finite_level(E, exact_symbol, independent_symbol, level):
    p = 5
    pn, pn1 = p**level, p**(level - 1)
    # binom(t,2) is 5-integral and constant modulo 5^(level-1)
    # on each level-n measure ball, in the gamma=6 coordinate.
    error_exponent = level - 1
    modulus = p**error_exponent
    teich = {
        a: hensel(a, p, level, lambda x: x**(p-1) - 1)
        for a in range(1, p)
    }
    assert sorted({teich[a] * pow(6, j, pn) % pn
                   for j in range(pn1) for a in range(1, p)}) == [
                       b for b in range(1, pn) if b % p
                   ]
    alpha = hensel(3, p, error_exponent, lambda x: x*x + 2*x + 5)
    print(f"Checking all symbols at denominators {pn} and {pn1}", flush=True)
    num_high = independent_symbol.all_values_for_one_denominator(pn, sign=1)
    num_low = independent_symbol.all_values_for_one_denominator(pn1, sign=1)
    A, B = QQ(0), QQ(0)
    rows = []
    for j in range(pn1):
        weight = j * (j - 1) // 2
        for a in range(1, p):
            b = teich[a] * pow(6, j, pn) % pn
            high, low = QQ(b) / pn, QQ(b % pn1) / pn1
            mh, ml = exact_symbol(high), exact_symbol(low)
            # Both algorithms return rational modular-symbol values.
            nh, nl = num_high[high], num_low[low]
            assert (mh, ml) == (nh, nl)
            # With c_Manin=1 and these cusps mapping to O, the slanted
            # real-period lattice gives half-integral symbols.
            assert (2 * mh).denominator() == (2 * ml).denominator() == 1
            A += weight * mh
            B += weight * ml
            rows.append({
                "j": j, "teich_label": a, "residue": b,
                "binomial_j_2": weight,
                "symbol_high": str(mh), "symbol_low": str(ml),
            })
    inv_alpha = pow(alpha, -1, modulus)
    residue = pow(inv_alpha, level, modulus) * (
        rational_mod(A, modulus) - inv_alpha * rational_mod(B, modulus)
    ) % modulus
    assert residue != 0
    valuation = int(ZZ(residue).valuation(p))
    assert valuation < error_exponent
    # This is NOT used to establish the error bound.
    sage_series = E.padic_lseries(p, implementation="eclib").series(level, prec=4)
    sage_c2 = sage_series[2]
    assert sage_c2.precision_absolute() >= error_exponent
    assert rational_mod(QQ(sage_c2.lift()), modulus) == residue
    print(f"Level {level}: c2={residue} modulo {modulus}; A={A}, B={B}", flush=True)
    return {
        "level_n": level,
        "measure_modulus": pn,
        "cyclotomic_exponent_count": pn1,
        "gamma": 6,
        "teichmuller_residues": teich,
        "unit_root_modulus": modulus,
        "unit_root_residue": alpha,
        "unit_root_polynomial": [5, 2, 1],
        "exact_A": str(A),
        "exact_B": str(B),
        "formula": "alpha^(-n) * (A - alpha^(-1) * B)",
        "coefficient_residue": residue,
        "coefficient_modulus": modulus,
        "infinite_error_valuation_at_least": error_exponent,
        "c2_valuation_certified": valuation,
        "bin_count": len(rows),
        "all_symbols_cross_checked_eclib_vs_num": True,
        "sage_series_secondary_check": str(sage_series),
        "rational_symbol_rows": rows,
    }


def main():
    root = Path(__file__).resolve().parents[2]
    E = EllipticCurve([0, 0, 0, 39, 0])
    assert E.is_global_minimal_model()
    assert E.conductor() == 48672 and E.ap(5) == -2
    assert E.discriminant() < 0 and E.real_components() == 1
    assert E.has_good_reduction(5)
    rank_path = root / "compute/data/cm39_analytic_rank_certificate.json"
    rank_data = json.loads(rank_path.read_text())
    assert rank_data["ainvs"] == [0, 0, 0, 39, 0]
    assert rank_data["algebraic_rank"] == rank_data["analytic_rank_certified"] == 2
    table_path = root / ".tools/ecdata/allcurves/allcurves.40000-49999"
    table_row = "48672 i 1 [0,0,0,39,0] 2 2"
    assert table_row in table_path.read_text().splitlines()

    exact_symbol = E.modular_symbol(sign=1, implementation="eclib")
    independent_symbol = E.modular_symbol(sign=1, implementation="num")
    assert exact_symbol._scaling == QQ(1)/2
    assert exact_symbol(QQ(0)) == independent_symbol(QQ(0)) == 0
    records = [finite_level(E, exact_symbol, independent_symbol, n) for n in (3, 4)]
    assert records[0]["coefficient_residue"] == 20
    assert records[1]["coefficient_residue"] == 70
    assert records[1]["coefficient_residue"] % 25 == records[0]["coefficient_residue"]
    rows = records[0]["rational_symbol_rows"]
    A2 = sum(QQ(row["symbol_low"]) * row["binomial_j_2"]
             for row in rows if row["j"] < 5)
    carry = sum(QQ(row["symbol_high"]) * (row["j"] // 5)
                * (2 * (row["j"] % 5) - 1) for row in rows)
    alpha = records[0]["unit_root_residue"]
    ai = pow(alpha, -1, 25)
    carry_result = (ai**2 * rational_mod(A2, 25)
                    + 5 * pow(2, -1, 25) * ai**3 * rational_mod(carry, 25)) % 25
    assert (A2, carry, carry_result) == (-5, 237, 20)

    output = {
        "curve_label": "48672i1",
        "ainvs": [0, 0, 0, 39, 0],
        "conductor": 48672,
        "prime": 5,
        "a_p": -2,
        "N_p": 8,
        "sage_version": SAGE_VERSION,
        "neron_differential": "dx/(2*y) on the displayed global minimal model",
        "period": "full real Neron period; equals least positive real period",
        "real_components": 1,
        "eclib_to_neron_real_scaling": "1/2",
        "manin_constant": 1,
        "optimality_source": (
            "Cremona, Appendix Theorem 5.2 in Agashe-Ribet-Stein (2006): "
            "N<60000, index1 optimal except990h, Manin constant1"
        ),
        "primary_manin_pdf": (
            "https://wstein.org/papers/ars-manin/"
            "agashe-ribet-stein-the_manin_constant.pdf"
        ),
        "table_row": table_row,
        "table_url": (
            "https://raw.githubusercontent.com/JohnCremona/ecdata/master/"
            "allcurves/allcurves.40000-49999"
        ),
        "table_sha256": hashlib.sha256(table_path.read_bytes()).hexdigest(),
        "rank_certificate_sha256": hashlib.sha256(rank_path.read_bytes()).hexdigest(),
        "measure_integrality": (
            "5-integral Neron modular symbols; CM ordinary inertia and "
            "complex conjugation imply irreducibility, alternatively optimal "
            "Manin1 and rational unitary cusps give half-integral symbols"
        ),
        "c2_nonzero_certified": True,
        "c2_residue_mod_25": 20,
        "c2_valuation": 1,
        "normalization_constants_retained": {
            "T": "gamma-1, chi_cyc(gamma)=6",
            "tame_norm_degree": 18432,
            "auxiliary_a": 7,
            "q_a": "12*(a^2-u_a*(1+X)^lambda_a*(1+Y)^lambda_a)",
            "betti_coefficient": "2*pr_rho(gamma_E_plus)",
            "g_p": "log_5(6)",
            "e_p": "(1-alpha^(-1))^2",
            "k_alpha": "(1-alpha^(-1))^(-1)*(1-beta^(-1))",
            "c_cmp_p": "(156*i*Omega_p)^(-1)",
        },
        "records": records,
        "uniform_carry_identity_test": {
            "A_level_2": str(A2), "carry_C": str(carry),
            "formula_mod_p_squared": "alpha^(-2)*A2 + p/(2*alpha^3)*C",
            "result_mod_25": carry_result,
            "A2_div_p_mod_5": rational_mod(A2 / 5, 5),
            "C_mod_5": rational_mod(carry, 5),
            "alpha_A2_div_p_plus_C_div_2_mod_5": 3,
            "scope": "One exact instance of the proved uniform finite-sum identity; no extrapolation",
        },
        "scope": (
            "Certifies nonzero precisely normalized c2 at p=5; "
            "the linked proof deduces nonzero actual derived class. "
            "No all-prime or rational BSD conclusion is asserted."
        ),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    path = root / "compute/data/cm39_padic_derivative_certificate.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "output": str(path),
        "c2_mod_25": 20, "c2_mod_125": 70,
        "exact_sums": [{"n": r["level_n"], "A": r["exact_A"], "B": r["exact_B"]}
                       for r in records],
        "all_exact_symbol_checks_pass": True,
        "infinite_error_exponents": [2, 3],
    }, indent=2))


if __name__ == "__main__":
    main()
