#!/usr/bin/env sage -python
"""Independent CM-39 coefficient check and rigorous analytic-rank certificate.

Run from the repository root with the existing Sage runtime:
  DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39.py

Uses the reviewed Mellin proof at a second cutoff and precision. No BSD
leading-term or Sha-finiteness assumption is used.
"""
import json
import sys
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

from sage.all import EllipticCurve, prime_range

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root))
import compute.scripts.certify_mellin as m

E = EllipticCurve([0, 0, 0, 39, 0])
coeffs = list(map(int, E.anlist(1405)))
local = {}
for p0 in prime_range(2, 1406):
    p = int(p0)
    if p in (2, 3, 13):
        assert E.local_data(p).has_additive_reduction()
        local[p] = 0
        continue
    squares = [0] * p
    for y in range(p):
        squares[y*y % p] += 1
    count = 1 + sum(squares[(x*x*x + 39*x) % p] for x in range(p))
    local[p] = p + 1 - count
reconstructed = [0, 1]
for n in range(2, 1406):
    prime = next(p for p in local if n % p == 0)
    q, exponent = n, 0
    while q % prime == 0:
        q //= prime
        exponent += 1
    if prime in (2, 3, 13):
        power = 0
    else:
        prev, power = 1, local[prime]
        for k in range(2, exponent + 1):
            prev, power = power, local[prime]*power - prime*prev
    reconstructed.append(power * reconstructed[q])
assert reconstructed == coeffs

# The installed small Cremona database does not contain this model.
# This replacement is local to this process and leaves the source unchanged.
m.EllipticCurve = lambda unused_label: E
result = m.certify('CM-39', 112, 48)
result['independent_coefficient_check'] = {
    'through': 1405,
    'method': 'direct finite-field point counts, bad-prime additive factors, Hecke recurrences and multiplicativity',
    'pass': True,
}
result['certificate_script_sha256'] = sha256(
    (root / 'compute/scripts/certify_mellin.py').read_bytes()).hexdigest()

lo, hi = map(Fraction, result['L_leading_rational_endpoints'])
first_lo = Fraction(2679924907651496904488990337, 309485009821345068724781056)
first_hi = Fraction(2679924907662402912040072833, 309485009821345068724781056)
assert first_lo < lo < hi < first_hi

out = root / 'compute/data/cm39_analytic_rank_certificate.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
