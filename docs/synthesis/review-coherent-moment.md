# Independent review of the coherent integral moment construction

Date: 2026-09-12. Reviewer: `/root/higher_period_integrality`, GPT-6 Astra,
xhigh reasoning. Assigned by the coordinator after the higher-period task.

## Verdict and scope

**PASS** for Propositions 2.1 and 3.1 and Lemmas 4.1 and 4.2 of
[coherent-moment-attack.md](coherent-moment-attack.md). The example and
the positive tensor criterion have the scope claimed in that note.
They do not prove an elliptic-curve L-function comparison or BSD.

The entire note, script, and output were read. This review did not attempt
to establish the hypotheses of Banwait's preprint or rely on that preprint
for the elementary conclusions.

Reviewed SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `docs/synthesis/coherent-moment-attack.md` | `754e279b39588291ee9ba2cbd979ee301e4e22beef7ff124f991e2da0a4fcf2a` |
| `compute/scripts/coherent_measure_check.py` | `54154aac6a29187ca378dc21aa52bbcffc9a9a4f54024ef7bd6c6b42930a6d3f` |
| `compute/data/coherent_measure_example.json` | `be2a4baa104f9731ae26b23069b9d39ec54948f865b68249c9e04060955d3296` |

## 1. Proposition 2.1

**[NEW, independent verification]** For odd p the Iwasawa logarithm of
2 lies in p Z_p, and log_p(1+p) has valuation one. Thus m_p is integral.
If it were zero, log_p(2^(p-1)) would be zero. The injectivity of log on
1+p Z_p would force the nonzero rational integer 2^(p-1)-1 to vanish in
Q_p, which is impossible. No unproved distribution statement about p is
needed for m_p to be nonzero at each p.

Binomial powers with Z_p exponent have integral coefficients and obey
the exponent law. This follows coefficient by coefficient from polynomial
continuity and approximation of the exponent by nonnegative integers.
Therefore A=(1+T)^m and A^(-1)=(1+T)^(-m) are units, and the identity

$$F_p=(A-1)^2/A$$

immediately proves T-order two and coefficient m_p^2. Substitution
T maps to -T/(1+T) sends 1+T to (1+T)^(-1), so it interchanges A and
A^(-1) and preserves F_p exactly.

For m=p^k u with u a unit, reduction modulo p first gives

$$
\overline{(1+T)^m}=(1+T^{p^k})^u
=1+\bar u T^{p^k}+O(T^{2p^k}).
$$

Here exponent u on the right denotes the reduction of its integral
binomial series; it is not an assertion that only the residue of u
determines the entire series. Squaring A-1 and dividing by the unit A
puts its first unit coefficient in degree 2p^k. Hence mu=0 and
lambda=2p^k, as stated.

## 2. Proposition 3.1 and exact integer checks

**[NEW, independent verification]** If z is in 1+p Z_p and a=v_p(z-1)
is positive, the n-th logarithm term has valuation na-v_p(n). For every
n>=2 and odd p this is greater than a. Thus the first term uniquely
minimizes the valuation and v_p(log z)=v_p(z-1). Since p-1 is a unit,

$$
v_p(m_p)=v_p(\log_p(2^{p-1}))-1
=v_p(2^{p-1}-1)-1.
$$

The script's full-integer valuations were checked independently using
modular exponentiation, including primality by trial division. In particular:

| p | 2^(p-1) mod p^2 | 2^(p-1) mod p^3 | Valuation |
|---|---:|---:|---:|
| 1093 | 1 | 581794064 | 2 |
| 3511 | 1 | 628683172 | 2 |

The residues modulo p^3 are not one, so the valuations are **exactly**
two, not just at least two. All five records in the JSON file were also
checked by the same criterion, and the resulting coefficient valuations
and lambda values agree.

Reproduction of the independent exceptional-prime check:

```sh
python3 - <<'PY'
from math import isqrt
for p in (1093, 3511):
    assert all(p % d for d in range(2, isqrt(p) + 1))
    assert pow(2, p - 1, p**2) == 1
    residue = pow(2, p - 1, p**3)
    assert residue != 1
    print(p, residue)
PY
```

The source note explicitly denies an infinite-exception assertion and
does not use one. Its conclusion refutes an all-odd-primes implication
and a denominators-only exception rule for this fixed object. It does
not refute an unspecified almost-all-primes implication.

## 3. Lemma 4.1

**[NEW, independent verification]** Choose a basis of the free abelian
group M, so its group ring is a Laurent polynomial ring. The associated
graded ring at augmentation has basis monomials in the classes of X_i-1,
and is Sym M. Both proposed realizations take each X_i-1 to its stated
linear coefficient plus terms of degree at least two. Hence a product
of r such factors has leading coefficient equal to the evaluation of
its degree-r symbol. Any term in I^(r+1) has higher order. Linearity
proves the assertion for every theta in I^r.

There is no factorial missing: Q is an augmentation symbol, and the
coefficient is a Taylor coefficient, not the r-th derivative. Formal
exponentials over a characteristic-zero field are sufficient, without
any analytic convergence assertion.

## 4. Lemma 4.2 and its application boundary

**[NEW, independent verification]** Expand Q and D in the integral
monomial basis. If D is primitive, Bezout gives integers b_i with
sum b_i D_i=1. Equality Q=cD in the characteristic-zero coefficient
field then implies c=sum b_i Q_i, which is the image of an ordinary
integer in that field. This proves the lemma, including c=0.

The conclusion uses equality of **tensors**, not equality after a
single evaluation. For example, taking Q=X and D=Y gives a primitive
pair whose ratio under the evaluation X=1,Y=2 is 1/2; there is no scalar
c for which X=cY as tensors. Thus mere numerical normalization cannot
replace the tensor identity. The source note states this distinction.

For the proposed BSD application, the real regulator tensor must be
identified, shown primitive in the chosen integral module, and matched
to all Néron-period, torsion, Tamagawa and lattice-index factors. The
source's Gap Tensor comparison retains those obligations. Its formal
moment example is explicitly not an elliptic L-function. The normalized
ratio one illustrates a valid cancellation of an index but supplies no
arithmetic identification of that index with an elliptic regulator.

No changes to the reviewed proofs are required. This review adds no
BSD, full-Sha, or infinite-Wieferich-prime conclusion.

Coordinator metadata note: after this review, only the source note’s review-status introduction was updated to link this PASS. The displayed source hash records the reviewed version before that header-only edit; the mathematical proof body was unchanged.
