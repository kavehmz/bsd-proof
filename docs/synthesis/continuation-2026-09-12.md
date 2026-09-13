# Continuation: an exact Kurihara witness and repaired reductions

Date: 2026-09-12, initial continuation. This note supersedes conflicting implications in the September 11 synthesis.
Subsequent work supplies [analytic-rank certificates](analytic-rank-certificates.md),
[exceptional-prime calculations](exceptional-prime-finiteness.md), and the sharper
[unit-index equivalence](uniform-witness-attack.md); see the [current report](final-report.md).
The objective remains the charter's BSD proof program. No general BSD proof is claimed here.

## 1. A completed calculation

For $E=389a1$, with equation $y^2+y=x^3+x^2-2x$, take $p=5$ and
$n=41\cdot61=2501$. Use the least positive real Néron period for the plus modular
symbol and primitive roots $\eta_{41}=6$, $\eta_{61}=2$.

**[THEOREM, computational verification]** The exact modular-symbol sum is
$$
\sum_{a\in(\mathbb Z/2501\mathbb Z)^\times}
[a/2501]^+\log_6(a\bmod41)\log_2(a\bmod61)=244,
$$
where the logarithms are represented in $\{0,\ldots,39\}$ and
$\{0,\ldots,59\}$ respectively. Consequently $\widetilde\delta_{2501}=4$ in
$\mathbb F_5$. Changing primitive roots changes the nonzero residue by a unit.

The reproduction script uses exact rational arithmetic and checks agreement
between Sage's `eclib` and `sage` modular-symbol backends at all 2,501 evaluated
cusps (one base cusp, 100 prime-conductor cusps, and 2,400 product-conductor cusps).
It also verifies the character distribution identities below. The output is
[`kurihara_389a1_p5.json`](../../compute/data/kurihara_389a1_p5.json).

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/kurihara_witness.py
```

The cache stays inside the repository. No approximate complex or $p$-adic
$L$-value is used in this calculation.

## 2. What this proves arithmetically

**[THEOREM]** For the hypotheses and notation of Kim's Theorem 3.1, if the
Kurihara family is nonzero, its first nonzero index is the $p^\infty$-Selmer
corank; moreover
$$
\operatorname{length}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)_{/\mathrm{div}}
=\partial^{(s)}(\widetilde{\boldsymbol\delta})-
\partial^{(\infty)}(\widetilde{\boldsymbol\delta}),
\quad s=\operatorname{ord}(\widetilde{\boldsymbol\delta}).
$$
Here $p\ge5$, the residual representation is surjective, and the Manin constant
is prime to $p$. This theorem does **not** require ordinary reduction.
Source: [Kim, *A higher Gross–Zagier formula and the structure of Selmer groups*,
§§2.1, 3.1, Theorem 3.1](https://arxiv.org/html/2203.12161v5#S3.SS1).

**[THEOREM, application of the cited theorem and exact computation]** For our example:

1. PARI descent returns `[2, 2, 0, [[-2, 0], [4, 8]]]`. In particular there
   are two independent rational points. Saturation is unnecessary for this lower bound.
2. Sage verifies residual surjectivity at $5$. The curve has good reduction at
   $5$ ($a_5=-3$); the Manin-constant hypothesis follows from the semistability
   criterion recorded in Kim §2.1. The curve is non-CM.
3. $a_{41}=-3$ and $a_{61}=-8$. Both primes meet the cyclotomic prime conditions,
   and $I_{41}=I_{61}=5\mathbb Z_5$.
4. The nonzero product-conductor sum gives $s\le2$. Kummer theory and the two
   independent points give $s\ge2$. Thus $s=2$.
5. Because this index-two sum is a unit, $\partial^{(2)}=0$. All divisibilities
   are nonnegative, so $\partial^{(\infty)}=0$. The finite Selmer quotient is zero.
6. In
   $$0\to E(\mathbb Q)\otimes\mathbb Q_5/\mathbb Z_5
     \to\operatorname{Sel}_{5^\infty}(E/\mathbb Q)
     \to\operatorname{Sha}(E/\mathbb Q)[5^\infty]\to0,$$
   the first term is a divisible subgroup of corank two. The Selmer group has
   the same corank and no finite quotient by its maximal divisible subgroup.
   The inclusion of divisible groups splits; its complement has corank zero
   and is divisible, hence zero.

Therefore
$$
\operatorname{ord}(\widetilde{\boldsymbol\delta})=2,\qquad
\operatorname{Sel}_{5^\infty}(389a1/\mathbb Q)\simeq(\mathbb Q_5/\mathbb Z_5)^2,
\qquad\operatorname{Sha}(389a1/\mathbb Q)[5^\infty]=0.
$$

This conclusion about $\operatorname{Sha}[5^\infty]$ was already covered by
[Stein–Wuthrich, Theorem 1.1](https://www.wstein.org/papers/shark/shark.pdf).
The contribution to this repository is an explicit witness for the modular-symbol
route, with an independently checked calculation. No Heegner class has been computed.
The argument does not establish an upper bound on the complex analytic rank;
it therefore does not use the old numerical analytic-rank estimate as a theorem.

## 3. Extending the prime-conductor derivative calculation

**[NEW] Lemma (mixed character difference).** Let $p$ be odd and
$n=\ell_1\cdots\ell_m$ squarefree, with $p\mid\ell_i-1$. Assume the symbols
$[a/n]^+$ are $p$-integral. Choose order-$p$ characters
$\chi_i(a)=\zeta^{k_i(a)}$, where $\zeta$ is a primitive $p$th root and
$k_i(a)=\log_{\eta_{\ell_i}}(a)\bmod p$. Put $\pi=\zeta-1$ and, for each subset $S$,
$$
F_n(S)=\sum_{a\in(\mathbb Z/n\mathbb Z)^\times}[a/n]^+
                  \prod_{i\in S}\chi_i(a),\qquad
D_n=\sum_{S\subseteq\{1,\ldots,m\}}(-1)^{m-|S|}F_n(S).
$$
Then, in $\mathbb Z_p[\zeta]$,
$$
D_n\in\pi^m\mathbb Z_p[\zeta],\qquad
\frac{D_n}{\pi^m}\bmod\pi
=\sum_a\overline{[a/n]^+}\prod_i\overline{k_i(a)}.
$$
For cyclotomic Kurihara primes the right side is $\widetilde\delta_n\bmod p$.

*Proof.* Inclusion–exclusion gives
$D_n=\sum_a[a/n]^+\prod_i(\zeta^{k_i(a)}-1)$.
Every factor is divisible by $\pi$, and
$(\zeta^k-1)/\pi\equiv k\pmod\pi$. Divide the product by $\pi^m$ and
reduce using $\mathbb Z_p[\zeta]/\pi=\mathbb F_p$. This also proves independence
of integer lifts. $\square$

This is a finite difference of character values. It is not a formula for a
complex central derivative. In particular, terms for proper subsets are
imprimitive sums at the *same* modulus $n$; replacing them by primitive
twisted values without Euler factors would change the identity.

For two distinct primes $\ell,q\nmid N$, **[NEW]** the needed distribution identity is
$$
F_{\ell q}(\{\ell\})=
(a_q-\chi_\ell(q)-\chi_\ell(q)^{-1})F_\ell(\{\ell\}).
$$
*Proof.* The weight-two Hecke relation at a cusp $x$ reads
$\sum_{b=0}^{q-1}[(x+b)/q]^+=a_q[x]^+-[qx]^+$.
For $x=a/\ell$, remove the unique summand whose numerator is divisible by
$q$; it is $[aq^{-1}/\ell]^+$. Multiply by $\chi_\ell(a)$ and sum over $a$.
Changing variables in the last two terms gives the displayed factors. $\square$

For the computed example all three proper-subset sums vanish exactly, and
$$
D_{2501}=84\zeta^3+82\zeta^2+84\zeta,\qquad
D_{2501}/(\zeta-1)^2=-50\zeta^2-66\zeta-50.
$$
Its residue is $4\bmod5$ and its $\pi$-valuation is exactly two.
The script checks both the product expansion and the imprimitive Euler identities.
These elementary lemmas have been checked on the page and computationally;
independent adversarial review remains pending under the charter's `[NEW]` policy.
The arithmetic result in §2 uses Kim's theorem directly.

## 4. Errors found in the previous reduction

The previous report's claim that P1–P3 already form a complete reduction is withdrawn.
The following are logical corrections, not evidence against BSD.

* **Rank versus Selmer corank.** $s_p=r_{\rm alg}+t_p$, where $t_p$ is the
  corank of $\operatorname{Sha}[p^\infty]$. Knowing $s_p=2$ leaves $t_p$ undetermined.
  Two independent points, or $\mathrm{Fin}(p)$ together with $s_p=2$, supply
  the missing input. BSD(rank) by itself does not imply $\mathrm{Fin}(p)$.
  The implication also cannot be repaired by assuming only $s_p\le r_{\rm an}$:
  finiteness then gives $r_{\rm alg}=s_p\le r_{\rm an}$, not equality.
* **Kolyvagin index versus divisibility.** The corank bridge
  $\nu_\infty=1\iff s_p=2$ survives under its hypotheses. The additional claim
  $\nu_\infty=1\iff\mathscr M_1=\mathscr M_\infty$ conflates first nonvanishing
  with stabilization of divisibility. A nonzero class can remain divisible.
  Also, Kim's minimum formula requires the two Selmer coranks to differ by one;
  the maximum formula alone does not require this.
  Sources: [BCGS, Corollary A](https://arxiv.org/html/2312.09301v2),
  and [Kim, Theorem 2.3](https://arxiv.org/html/2203.12161v5#S2.SS6).
* **Complex rationality versus comparison.** Let
  $c_E=L^{(r)}(E,1)/(r!\Omega_E\operatorname{Reg}_{\rm NT})$.
  The assertion $c_E\in\mathbb Q^\times$ specifies neither $\#\operatorname{Sha}$ nor any
  $p$-adic realization of $c_E$. No implication from this assertion alone
  to $\mathrm U(E)$ is proved in the repository. An Iwasawa characteristic
  ideal identifies a series only up to a unit; it cannot remove this missing
  comparison of leading terms.
* **Prime coverage.** Proposition 3.3 concludes almost-all-prime vanishing
  *within its good ordinary set*. Its conclusion says nothing about primes
  outside that set. One must cover these primes too, and prove finiteness at
  every remaining exceptional prime, before concluding that the full group is finite.
* **Scope of the residual-image hypothesis.** The stated P2 demands a
  surjective residual representation. It must be restricted to the non-CM
  setting used by Kim. CM curves require another argument; the old
  “for every elliptic curve” package did not supply it.
* **Converse of a modular congruence.** Corollary 2.4's final sentence takes
  a converse of an implication. “A unit prime-conductor witness implies a
  small Selmer group” does not imply that the absence of such witnesses forces
  a large group. Reduction modulo $p$ can also lose nonzero classes modulo $p^k$.

Proposition 2.3's prime-conductor expansion passes this audit: the constant term
is $(a_\ell-2)[0]^+$ and is killed modulo $(\zeta-1)^2$ under its stated odd-$p$
congruences. Proposition 3.3's forward ordinary-prime implication also survives
with its explicit integral main-conjecture hypotheses. Its converse needs the
nonzero-height condition appearing in $\mathrm U(E)$, in addition to the two BSD formulas.

## 5. A more concrete uniform target

**[NEW] Proposition (unit witnesses bound Sha without a height comparison).**
Fix $E/\mathbb Q$, $p\ge5$, and assume Kim's Theorem 3.1 hypotheses.
Suppose $r$ independent rational points are exhibited and there is a squarefree
cyclotomic Kurihara index $n$ with exactly $r$ prime factors and
$\widetilde\delta_n\not\equiv0\pmod p$. Then
$$\operatorname{rank}E(\mathbb Q)=r,\qquad\operatorname{Sha}(E/\mathbb Q)[p^\infty]=0.$$

*Proof.* The witness makes the family nonzero and its order at most $r$.
The independent points and Kummer sequence bound its order below by $r$,
using the cited corank theorem. Both divisibility minima in the cited length
formula are zero, so the finite Selmer quotient is zero. The same split-divisible-group
argument as in §2 now gives $\operatorname{Sha}[p^\infty]=0$ and rank $r$. $\square$

This sufficient criterion uses neither the integral main conjecture nor a
$p$-adic regulator nor complex leading-term rationality. It applies to ordinary
and supersingular primes satisfying the stated theorem hypotheses. It is a
deduction from the existing structure theorem, not a new uniform nonvanishing theorem.
Its independent review status is the same as the other `[NEW]` deductions above.

**[GAP Uδ, explicit next target for 389a1].** Produce a finite, explicitly
determined set of primes $S$ containing $2,3,389$ and every residual-image
exception, and prove that for every prime $p\notin S$ there are distinct
$\ell_p,q_p\nmid389p$ with
$$
\ell_p\equiv q_p\equiv1\pmod p,\quad
a_{\ell_p}\equiv\ell_p+1\pmod p,\quad
a_{q_p}\equiv q_p+1\pmod p,\quad
\widetilde\delta_{\ell_pq_p}\not\equiv0\pmod p.
$$
Prove $\operatorname{Sha}(389a1)[p^\infty]$ finite for each $p\in S$ as the separate finite
set of obligations. Together these statements imply full Sha finiteness by
primary decomposition. The leading-term formula would still require its own proof.

The computation supplies $(p,\ell_p,q_p)=(5,41,61)$.
The mixed-character lemma converts the last condition into a concrete valuation
condition on twisted values, including all imprimitive corrections. A proof
uniform in $p$ must control these nonzero residues; merely selecting primes
with the displayed Frobenius congruences does not do that. Likewise, pairing
the two known points against local conditions controls their Kummer images,
but does not by itself bound additional Selmer classes. This identifies the
next nonvanishing statement without assuming away those classes.
