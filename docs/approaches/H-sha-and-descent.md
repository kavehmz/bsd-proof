# H. Finiteness of Sha and descent

Updated 2026-09-12 after the [continuation audit](../synthesis/continuation-2026-09-12.md).
The September 11 identification of complex rationality with full Sha finiteness
has been withdrawn.

## 1. Exact finiteness criterion

**[THEOREM]** Sha is a torsion abelian group, so
$$\operatorname{Sha}(E/\mathbb Q)=\bigoplus_p\operatorname{Sha}(E/\mathbb Q)[p^\infty].$$
Consequently it is finite if and only if each primary group is finite and all
but finitely many primary groups vanish. For a primary torsion group,
$\operatorname{Sha}[p]=0$ is equivalent to $\operatorname{Sha}[p^\infty]=0$.

*Proof.* Every element has finite order and decomposes into its primary
components. A finite group has finite prime support. Conversely a finite
direct sum of finite groups is finite. A nonzero element of $p$-power order
has a multiple of order $p$. $\square$

For every fixed prime, the Kummer sequence gives
$$s_p=r_{\rm alg}+\operatorname{corank}_{\mathbb Z_p}\operatorname{Sha}[p^\infty].$$
Thus an exact rank computation and a matching Selmer corank establish primary
finiteness. They do not supply a finite set containing the support of the full group.

## 2. Completed primary calculations

**[THEOREM, certified computational applications]** For 389a1,
$\operatorname{Sha}[p^\infty]=0$ for $p=2,3,5,389$ in the present certificates.
The prime five uses the [exact Kurihara witness](../synthesis/continuation-2026-09-12.md).
The [other three primes](../synthesis/exceptional-prime-finiteness.md) use
two-descent, Kato's divisibility, and normalized $p$-adic regulators.
The extra zero at the split multiplicative prime 389 is retained.

## 3. The uniform task

The [unit-index theorem](../synthesis/uniform-witness-attack.md) gives
$$u_p=2+\dim_{\mathbb F_p}\operatorname{Sha}(389a1)[p]$$
for every $p\notin S_0=\{2,3,389\}$. Its hypotheses are checked uniformly:
the residual representation is surjective at every such prime, and
Castella–Sano's theorem supplies a primitive Kurihara family in both
ordinary and supersingular reduction.

**[GAP H.1 / PrimeIndex-389]** Prove $u_p=2$ for every $p\notin S_0$.
Together with the completed calculations at $S_0$, this would give
$\operatorname{Sha}(389a1)=0$.

If only an almost-all-prime version is proved, all additional exceptional
primes require separate primary-finiteness arguments. The existence of a
unit witness of unspecified index, which is already known here, does not
bound that index by two.

**[GAP H.2 / Degree-389, alternative]** Give a uniform bound on the least
degree of a closed point on every everywhere locally soluble torsor of
389a1. The [geometric proof attempt](../synthesis/genus-one-finiteness-attack.md)
proves that this is equivalent to full Sha finiteness. It distinguishes
fixed-polarization finiteness from a bound uniform over all polarizations.

## 4. The remaining leading-term comparison

Even after full Sha finiteness, the complex equality
$$\frac{L^{(r)}(E,1)}{r!\Omega_E\operatorname{Reg}_{\rm NT}}
=\frac{\prod_{q\mid N}c_q\cdot\#\operatorname{Sha}(E/\mathbb Q)}{\#E(\mathbb Q)_{\rm tors}^2}$$
needs its own proof. For 389a1 the real quotient on the left is
[rigorously between 0.9931 and 1.0077](../synthesis/bsd-archimedean-bound.md).
That interval does not establish rationality or integrality. The
[one-sided global criterion](../synthesis/derived-comparison-attack.md)
states precisely what arithmetic comparison would turn the bound into
the BSD formula.
