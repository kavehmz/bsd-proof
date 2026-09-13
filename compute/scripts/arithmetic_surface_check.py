#!/usr/bin/env python3
"""Exact checks for the regular cubic surface model of 389a1 over Spec Z.

The cohomology statements are proved in weil-etale-lattice-attack.md, not
inferred from these numerical checks. No Brauer/Sha finiteness is assumed.
"""
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

p = 389
assert all(p % d for d in range(2, isqrt(p) + 1))
b2, b4, b6, b8 = 4, -4, 1, -3
discriminant = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
assert discriminant == p
c4, c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
F = lambda x, y: y*y+y-x*x*x-x*x+2*x
nodes = [(x, y) for x in range(p) for y in range(p)
         if F(x, y) % p == 0 and (-3*x*x-2*x+2) % p == 0 and (2*y+1) % p == 0]
assert nodes == [(299, 194)]
x, y = nodes[0]
quotient = F(x, y) // p
slopes = [a for a in range(p) if a*a % p == (3*x+1) % p]
point_count = 1 + sum(F(x, y) % p == 0 for x in range(p) for y in range(p))
assert quotient % p == 5 and slopes == [148, 241] and point_count == p

root = Path(__file__).resolve().parents[2]
source = root / "compute/data/analytic_rank_certificates.json"
source_bytes = source.read_bytes()
analytic = next(r for r in json.loads(source_bytes)["records"] if r["label"] == "389a1")
assert analytic["ainvs"] == [0, 1, 1, -2, 0]
assert analytic["algebraic_rank"] == analytic["analytic_rank_certified"] == 2
low, high = map(Fraction, analytic["L_leading_rational_endpoints"])
assert 0 < low < high
zeta_endpoints = [-1/(2*low), -1/(2*high)]
assert zeta_endpoints[0] < zeta_endpoints[1] < 0
result = {
    "curve": "389a1", "affine_equation_F": "y^2+y-x^3-x^2+2*x",
    "projective_equation": "Y^2*Z+Y*Z^2-X^3-X^2*Z+2*X*Z^2",
    "discriminant": discriminant, "c4": c4, "c6": c6,
    "unique_special_fiber_node": nodes[0], "F_at_integer_lift_divided_by_389": quotient,
    "regular_total_space_residue": quotient % p,
    "distinct_tangent_slopes": slopes, "special_fiber_point_count": point_count,
    "analytic_input_sha256": sha256(source_bytes).hexdigest(),
    "arithmetic_surface_zeta_identity_from_proof": "zeta(s)*zeta(s-1)/L(E,s)",
    "surface_pole_order_at_1_from_proof": 3,
    "surface_leading_coefficient_identity": "-1/(2*(L''(E,1)/2))",
    "surface_leading_coefficient_rational_endpoints": [str(v) for v in zeta_endpoints],
    "scope": "Regularity/fiber arithmetic and analytic identity only; no finite Brauer or Sha claim",
}
out = root / "compute/data/arithmetic_surface_389a1.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
