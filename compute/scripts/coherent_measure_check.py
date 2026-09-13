#!/usr/bin/env python3
"""Exact arithmetic check for the coherent-measure proof attempt.

This is not an elliptic-curve or BSD counterexample. The mathematical
interpretation of the integers below is proved in coherent-moment-attack.md.
"""
import json
from pathlib import Path


def valuation(n, p):
    assert n != 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


records = []
for p in (5, 7, 11, 1093, 3511):
    v = valuation(2 ** (p - 1) - 1, p)
    k = v - 1
    assert k >= 0
    records.append({
        "p": p,
        "valuation_of_2_to_p_minus_1_minus_1": v,
        "valuation_of_log2_over_log1plusp": k,
        "central_order_from_proof": 2,
        "valuation_of_second_coefficient_from_proof": 2 * k,
        "mu_from_proof": 0,
        "lambda_from_proof": 2 * p ** k,
    })
assert records[3]["valuation_of_2_to_p_minus_1_minus_1"] == 2
assert records[4]["valuation_of_2_to_p_minus_1_minus_1"] == 2
result = {
    "fixed_integral_group_ring_element": "U + U^(-1) - 2 = (U-1)^2/U",
    "realization": "U -> (1+T)^(log_p(2)/log_p(1+p))",
    "records": records,
    "scope": "One coherent integral measure; not an elliptic L-function or BSD counterexample",
    "no_infinite_exception_claim": True,
}
out = Path(__file__).resolve().parents[1] / "data" / "coherent_measure_example.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
