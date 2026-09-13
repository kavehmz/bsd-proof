# Odd analytic rank, Selmer corank, and full Kurihara vanishing

Date: 2026-09-12. This note supplements the
[continuation audit](continuation-2026-09-12.md). It closes the ordinary-prime
odd-rank case of the old GAP 5 in
[§2.3 of the obstruction document](../03-obstructions-rank-ge-2.md), under the
hypotheses stated below. It does not prove BSD in rank three or higher.

The mathematical implications here are deductions from existing theorems;
no novelty is claimed. The elementary group-ring calculation in §6 is written
out and marked for independent review under the charter.

## 1. Notation and the precise result

Write
$$
r=\operatorname{ord}_{s=1}L(E,s),\qquad
s_p(E)=\operatorname{corank}_{\mathbb Z_p}
       \operatorname{Sel}_{p^\infty}(E/\mathbb Q).
$$
For a negative fundamental discriminant $D$, write
$K=\mathbb Q(\sqrt D)$, $E^D$ for the quadratic twist, and $\chi_D$ for its
quadratic character. Signed discriminants are used throughout this note.

**[THEOREM, consequence of cited results] Proposition 1.** Suppose that
$E/\mathbb Q$ is non-CM, $p\ge5$ is a prime of good ordinary reduction, and
$E[p]$ is irreducible as a $G_{\mathbb Q}$-module. Then
$$
r\text{ odd and }r\ge3\quad\Longrightarrow\quad s_p(E)\ge3.
\tag{1}
$$
There is no assumption of finiteness of $\operatorname{Sha}[p^\infty]$,
residual surjectivity, non-anomalous reduction, or a $p$-adic regulator in (1).
The proof uses the **Heegner** part of BCGS, not their Theorem C about Kato
classes, which has a separate local-torsion hypothesis.

**[THEOREM, consequence of cited results] Proposition 2.** If $E/\mathbb Q$
is semistable and $p\ge5$ is a prime of good supersingular reduction, the same
implication (1) holds. Here semistability is imposed at every finite prime.
This statement does not require a separate residual-image assumption.

Neither proposition identifies $s_p(E)$ with the Mordell–Weil rank. The Kummer
sequence gives
$$
s_p(E)=\operatorname{rank}E(\mathbb Q)
       +\operatorname{corank}_{\mathbb Z_p}\operatorname{Sha}(E/\mathbb Q)[p^\infty].
\tag{2}
$$
In particular, the conclusion $s_p(E)\ge3$ does not produce three independent
rational points.

## 2. An auxiliary twist with all the required local conditions

**[THEOREM, specialization of quadratic-twist nonvanishing] Lemma 3.**
If $w(E)=-1$, then, for any finite set $S$ of rational primes containing those
dividing $2Np$, there are infinitely many negative fundamental discriminants
$D$ for which
$$
(D,2Np)=1,\qquad \chi_D(v)=1\ (v\in S),\qquad L(E^D,1)\ne0.
\tag{3}
$$
Consequently $D$ is odd, $D\ne-3$, every prime dividing $Np$ splits in $K$,
and $s_p(E^D)=0$.

*Proof, including compatibility of the local specifications.* Put
$M=8\prod_{v\in S,\ v\ne2}v$. Dirichlet's theorem supplies a prime
$q\equiv-1\pmod M$, $q>3$. Then $D_0=-q$ is a negative fundamental
discriminant, $D_0\equiv1\pmod8$, and $D_0\equiv1\pmod v$ for every odd
$v\in S$. Thus its quadratic character is trivial at each finite place in
$S$ and has the imaginary quadratic type at infinity. This constructs one
global character realizing the requested local specifications.

For discriminants coprime to $N$, the quadratic-twist functional equation gives
$$
w(E^D)=w(E)\chi_D(-N).
$$
For the specified characters $\chi_D(N)=1$ and $\chi_D(-1)=-1$, so
$w(E^D)=+1$. Apply the sign-$+1$ part of Friedberg–Hoffstein's Theorem B,
with these finitely many local components prescribed. It supplies infinitely
many such characters with nonzero central value. The resulting discriminants
need not be prime discriminants; the preliminary choice $D_0=-q$ proves only
compatibility of the local data. Since $2$ splits, $D\equiv1\pmod8$, excluding
$D=-3$. The analytic-rank-zero theorem of Kolyvagin and Kato gives
$s_p(E^D)=0$. $\square$

**Source verification.** Friedberg–Hoffstein, *Nonvanishing theorems for
automorphic $L$-functions on $\mathrm{GL}(2)$*, Ann. of Math. **142** (1995),
385–423, Theorem B, DOI
[10.2307/2118638](https://annals.math.princeton.edu/1995/142-2/p04).
The publisher's bibliographic record was read; the original theorem pages
could not be fetched in this session. The use of that theorem with compatible
finitely many local conditions and positive twist root number was directly
checked in the primary research application
[Castella–Wan, proof of Theorem 6.11, pp. 32–33](https://web.math.ucsb.edu/~castella/Perrin-Riou.pdf).
That proof also explicitly invokes the rank-zero Selmer conclusion used here.
Thus the verification of the local form of FH95 is through this primary
application, not a claimed direct reading of the 1995 theorem.

## 3. Proof of the ordinary-prime implication

We first check the hypotheses needed to apply the Heegner theorem.

**[THEOREM, elementary] Lemma 4.** If $p$ is odd and $E[p]$ is irreducible
over $G_{\mathbb Q}$, then $E(K)[p]=0$ for every quadratic extension
$K/\mathbb Q$.

*Proof.* Since $G_K$ is normal in $G_{\mathbb Q}$, the invariant subspace
$E[p]^{G_K}$ is $G_{\mathbb Q}$-stable. If nonzero, irreducibility makes it
all of $E[p]$. The representation would then factor through the group of
order two. Over $\mathbb F_p$ an involution is diagonalizable, with eigenvalues
$1,-1$, so a two-dimensional representation of that group is reducible.
This is a contradiction. $\square$

**[THEOREM, elementary descent] Lemma 5.** For odd $p$, restriction and
quadratic twisting identify the two complex-conjugation eigenspaces of
$\operatorname{Sel}_{p^\infty}(E/K)$ with
$\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$ and
$\operatorname{Sel}_{p^\infty}(E^D/\mathbb Q)$ respectively.

*Proof.* The operators $(1\pm c)/2$ give a direct-sum decomposition because
$2$ is invertible on a $p$-primary group. Inflation–restriction has no
higher cohomology contribution from a group of order two acting on a
$p$-primary module; hence restriction identifies the plus summand with
cohomology over $\mathbb Q$. Apply the same argument after twisting by
$\chi_D$ to identify the minus summand. These maps preserve local Kummer
conditions: restriction and norm on local points are compatible with Kummer
maps, and restriction followed by norm is multiplication by the local degree,
which divides two and is invertible on the $p$-primary groups. Taking the
kernels of the global-to-local maps gives the claimed Selmer identifications.
$\square$

**[THEOREM] BCGS input.** Let $p>3$ be good ordinary with $E[p]$
irreducible. For an imaginary quadratic field in which all primes dividing
$Np$ split, with odd discriminant different from $-3$ and $E(K)[p]=0$, the
Heegner Kolyvagin system is nonzero. If
$$
\nu_K=\min\{\nu(n):\kappa_n^{\mathrm{Heeg}}\ne0\},
$$
where $\nu(n)$ counts prime factors, then
$$
\nu_K=\max\{s_p(E),s_p(E^D)\}-1.
\tag{4}
$$
This is [BCGS, Theorem A and Corollary A, arXiv:2312.09301v2](https://arxiv.org/html/2312.09301v2).
The irreducible case in Theorem A is an unconditional instance of its more
general main-conjecture formulation. In the same introduction BCGS records
the Gross–Zagier equivalence
$\kappa_1^{\mathrm{Heeg}}\ne0\iff L'(E/K,1)\ne0$.

*Proof of Proposition 1.* The functional equation gives $w(E)=-1$. Choose
$D$ as in Lemma 3. Lemma 4 supplies the remaining torsion hypothesis of
BCGS. Lemma 5 and $s_p(E^D)=0$ specialize (4) to
$$
\nu_K=s_p(E)-1.
\tag{5}
$$
Artin factorization gives
$L(E/K,s)=L(E,s)L(E^D,s)$. Its order at the center is $r\ge3$, so
$L'(E/K,1)=0$. Gross–Zagier therefore gives
$\kappa_1^{\mathrm{Heeg}}=0$. Since the entire system is nonzero,
$\nu_K\ge1$, and (5) gives $s_p(E)\ge2$.

The unconditional $p$-parity theorem says
$$
s_p(E)\equiv r\pmod2.
\tag{6}
$$
It follows that $s_p(E)\ge3$, proving (1). The parity source is
[Dokchitser–Dokchitser, Ann. of Math. **172** (2010), 567–596, Theorem 1.4,
equivalently Theorem 4.19](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n1-p11-p.pdf),
also arXiv:math/0610290. The cited theorem concerns Selmer corank and is
unconditional; it does not assume finiteness of Sha. $\square$

This proof also shows
$$
\nu_K=s_p(E)-1\in\{2,4,6,\ldots\}.
\tag{7}
$$
One can replace (6) by the signed version of Kolyvagin's structure theorem:
the zero twist eigenspace and $w(E)=-1$ force the first nonzero index to be
even. The proof above uses the directly verified general parity theorem and
therefore needs no enlargement of Kim's residual-surjectivity hypotheses to
quote his presentation of the signed theorem.

*Proof of Proposition 2.* By (6), $s_p(E)$ is a positive odd integer. If it
were one, the rank-one converse of
[Castella–Wan, Theorem A, equivalently Theorem 6.11](https://web.math.ucsb.edu/~castella/Perrin-Riou.pdf)
would give $r=1$. This contradicts $r\ge3$, so $s_p(E)\ge3$. $\square$

The Castella–Wan source here is the 39-page author-hosted version read in
this session. Its Theorem A states the converse for a semistable rational
elliptic curve and $p>3$ good supersingular. The older
[arXiv:1607.02019v2 record](https://arxiv.org/abs/1607.02019v2)
describes a 34-page 2018 version; the precise theorem scope above is cited
to the author PDF, not silently assigned to that earlier version.

## 4. Full-modulus Kurihara vanishing

For the rest of this section assume also that $E[p]$ is **surjective** and
the Manin constant is prime to $p$. These are the hypotheses in Kim's
corank theorem. The latter condition holds in the good-reduction cases here,
as recorded in Kim's working hypotheses, but is retained explicitly to fix
the normalization of the modular symbols.

Let
$$
\mathcal P=\{\ell\nmid Np:\ell\equiv1\pmod p,
                         \ a_\ell\equiv\ell+1\pmod p\},
\quad I_\ell=(\ell-1,a_\ell-\ell-1)\mathbb Z_p,
$$
and let $\mathcal N$ be their squarefree products. Put
$I_n=\sum_{\ell\mid n}I_\ell$ and $I_1=0$. With the plus modular symbol
normalized by the positive real Néron period, set
$$
\widetilde\delta_n=
 \sum_{a\in(\mathbb Z/n\mathbb Z)^\times}[a/n]^+
        \prod_{\ell\mid n}\log_{\eta_\ell}(a)
 \quad\text{in }\mathbb Z_p/I_n,
\qquad
\widetilde\delta_1=\frac{L(E,1)}{\Omega_E^+}.
\tag{8}
$$
The primitive roots $\eta_\ell$ can be chosen arbitrarily; zero is independent
of these choices.

**[THEOREM] Kim's input.** If the family in (8) has any nonzero entry, then
$$
s_p(E)=\min\{\nu(n):\widetilde\delta_n\ne0
                         \text{ in }\mathbb Z_p/I_n\}.
\tag{9}
$$
Sources: [Kim, arXiv:2203.12159v6, Theorem 1.8(1)](https://arxiv.org/html/2203.12159v6),
and its restatement in
[Kim, arXiv:2203.12161v7, §§2.1–2.2, 3.1, Theorem 3.1(1)](https://arxiv.org/html/2203.12161v7).
There is no ordinary-reduction hypothesis in this theorem.

**[THEOREM, direct consequence] Corollary 6.** Under Kim's hypotheses,
for every integer $h\ge0$,
$$
s_p(E)>h\quad\Longrightarrow\quad
\widetilde\delta_n=0\text{ in }\mathbb Z_p/I_n
\quad(\nu(n)\le h).
\tag{10}
$$
Consequently, in either Proposition 1 or Proposition 2, with the additional
surjectivity and Manin hypotheses just stated,
$$
\boxed{\widetilde\delta_n=0\text{ in }\mathbb Z_p/I_n
       \quad\text{for every }\nu(n)<3.}
\tag{11}
$$

*Proof.* If such an entry were nonzero, the hypothesis of (9) would hold
automatically, and (9) would give $s_p(E)\le\nu(n)\le h$, a contradiction.
Apply this with $h=2$. $\square$

An independent theorem asserting that the whole Kurihara family is nonzero
is unnecessary for this implication. This is a contrapositive application
of the corank theorem, not a converse inferred from the failure of unit
witnesses.

In particular, write
$$
m_\ell=\min\{v_p(\ell-1),v_p(a_\ell-\ell-1)\}.
$$
Then the prime-conductor conclusion is the exact congruence
$$
\sum_{a\in(\mathbb Z/\ell\mathbb Z)^\times}
 [a/\ell]^+\log_{\eta_\ell}(a)\equiv0\pmod{p^{m_\ell}}.
\tag{12}
$$
It is stronger than vanishing modulo $p$ when $m_\ell>1$. For distinct
$\ell,q\in\mathcal P$, (11) also gives vanishing modulo
$p^{\min(m_\ell,m_q)}$ of the two-prime sum. This resolves the old
prime-conductor GAP 5 in the specified ordinary range and proves the stated
semistable supersingular extension. No assertion is made here for the
remaining supersingular or residual-image cases.

## 5. The next exact statement at analytic rank at least five

Keep the ordinary hypotheses of Proposition 1, now with $r$ odd and
$r\ge5$, and choose any $K$ as in Lemma 3. For inert Heegner Kolyvagin
primes $\ell\nmid Np$ put
$$
J_\ell=(\ell+1,a_\ell)\mathbb Z_p\subset p\mathbb Z_p,
\quad J_{\ell q}=J_\ell+J_q,
\quad T=T_pE.
$$
These anticyclotomic ideals differ from the cyclotomic $I_\ell$ in §4.

**[THEOREM, direct consequence] Proposition 7.** For this fixed $E,p,K$,
$$
s_p(E)\ge5
\quad\Longleftrightarrow\quad
\kappa_{\ell q}^{\mathrm{Heeg}}=0
\text{ in }H^1(K,T/J_{\ell q}T)
\text{ for every pair of distinct Heegner Kolyvagin primes }\ell,q.
\tag{13}
$$

*Proof.* Equation (7) gives $\nu_K\in\{2,4,6,\ldots\}$. By definition
$\nu_K=2$ exactly when at least one two-prime class is nonzero. Excluding
all such classes is therefore equivalent to $\nu_K\ge4$, and (5) identifies
this with $s_p(E)\ge5$. $\square$

**[GAP O5, exact remaining assertion].** Let $E/\mathbb Q$ be non-CM, let
$p\ge5$ be good ordinary with irreducible $E[p]$, and suppose that
$\operatorname{ord}_{s=1}L(E,s)$ is odd and at least five. For an imaginary
quadratic field $K$ of odd discriminant different from $-3$ in which every
prime dividing $Np$ splits and for which $L(E^K,1)\ne0$, prove the right
side of (13).

For these hypotheses, proving it for one such $K$ would prove it for all
such $K$, since the left side of (13) is independent of $K$. This gap is
strictly the next Selmer lower-bound step in this method; even its solution
would leave Mordell–Weil generation, Sha finiteness, and the BSD leading term.

The extra analytic vanishing available here is
$L^{(j)}(E/K,1)=0$ for $j<5$. The ordinary proof in §3 uses only the case
$j=1$. Reapplying that proof supplies no bound beyond (7): the possibility
$s_p(E)=3$, $\nu_K=2$ satisfies every equality used there. A further relation
between higher complex central derivatives and the two-prime classes is
required to exclude it.

## 6. A direct attempt using trace relations, and where it fails

Heegner Euler-system norm relations motivate the following approach: use
the vanishing bottom point to force the first derived traces to vanish, then
apply two Kolyvagin derivative operators and hope to obtain zero. The
underlying group-ring implication is false, even if both individual traces
vanish exactly. The following calculation isolates the failure before any
unjustified arithmetic inference is made.

**[NEW, elementary calculation; independently reviewed by the coordinator] Lemma 8.**
Let $R=\mathbb Z_p$, $k\ge1$, and let $m,n$ be positive integers divisible
by $p^k$. In $R[G]$ for
$G=C_m\times C_n=\langle\sigma\rangle\times\langle\tau\rangle$, define
$$
N_\sigma=\sum_{i=0}^{m-1}\sigma^i,\quad
D_\sigma=\sum_{i=0}^{m-1}i\sigma^i,
$$
and define $N_\tau,D_\tau$ analogously. There exists $x\in R[G]$ such that
$$
N_\sigma x=N_\tau x=0,
\qquad D_\sigma D_\tau x\ne0
\text{ in }(R/p^kR)[G].
\tag{14}
$$

*Proof.* Take $x=(\sigma-1)(\tau-1)$. Both norms kill $x$ because
$N_\sigma(\sigma-1)=\sigma^m-1=0$ and likewise for $\tau$. Computing
coefficients gives the exact identity
$$
D_\sigma(\sigma-1)=m-N_\sigma.
$$
As the two cyclic factors commute,
$$
D_\sigma D_\tau x=(m-N_\sigma)(n-N_\tau)
\equiv N_\sigma N_\tau\pmod{p^k}.
$$
The last group-ring element has coefficient one at every group element,
so it is nonzero in $(R/p^kR)[G]$. $\square$

The derivative in this example is even invariant under both cyclic factors
modulo $p^k$, just as the descent construction requires at the group-ring
stage. Thus neither exact norm-zero relations nor the resulting invariance
can supply the vanishing in O5 by formal algebra alone.

This is a counterexample to a proposed **formal implication**, not an
elliptic-curve counterexample and not a disproof of O5 or BSD. Actual Heegner
points have additional geometric and local-cohomological constraints. An
argument using those constraints must still connect the extra vanishing
$L'''(E/K,1)=0$ to the zero class in (13); the calculation shows why simply
iterating the trace relation is insufficient.

For comparison, the analytic-rank-two upper bound in
[Proposition 2.2 of the obstruction document](../03-obstructions-rank-ge-2.md)
asks for a **nonzero one-prime** Heegner class after choosing a rank-one
twist. The nonvanishing theorem for the entire system does not bound the
number of prime factors of its first nonzero entry. The present argument
closes an odd-rank lower bound and leaves that rank-two upper-bound
nonvanishing problem intact.

## 7. Verification boundary

The proof above directly checks BCGS v2 Theorem A, Corollary A, and the
Gross–Zagier equivalence in its introduction; Dokchitser–Dokchitser's general
$p$-parity theorem; Kim's full-quotient definition and corank theorem; and
Castella–Wan's supersingular converse and use of FH95 with local conditions.
The original FH95 pages remain the explicitly identified citation-reading
limitation in §2. No numerical analytic rank, global finiteness conjecture,
unproved height nondegeneracy, or unproved equality between analytic rank
and Selmer corank is used.
