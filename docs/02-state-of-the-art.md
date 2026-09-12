# State of the art, with exact hypotheses, through September 2026

This document records what is **proved** about the Birch and Swinnerton-Dyer conjecture for
elliptic curves over $\mathbb{Q}$ (and, more briefly, over other fields), with the exact
hypotheses of each theorem. It follows the conventions of `00-charter.md`: every substantive
claim carries an epistemic tag; every reference carries an arXiv identifier, a DOI, or a full
journal citation that was confirmed by fetching the source (arXiv API / Crossref / the article
itself) during the preparation of this document (searches were run 2026-09-11). Items marked
`[unverified]` could not be confirmed at the source and should be re-checked before being relied
on. The cross-references `[Xxx00]` point to the bibliography in §15.

Notation is that of the charter: $E/\mathbb{Q}$ of conductor $N$, $r_{\mathrm{an}}=\operatorname{ord}_{s=1}L(E,s)$,
$r_{\mathrm{alg}}=\operatorname{rank}E(\mathbb{Q})$, $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$,
$\operatorname{Sha}(E/\mathbb{Q})$, $\bar\rho_{E,p}:G_\mathbb{Q}\to\mathrm{GL}_2(\mathbb{F}_p)$ the action on $E[p]$,
$c_\ell$ the Tamagawa numbers, $\Omega_E$ the Néron period, $\operatorname{Reg}(E/\mathbb{Q})$ the regulator.
"The $p$-part of the BSD formula" (for $r_{\mathrm{an}}=r\in\{0,1\}$) means
$$
\operatorname{ord}_p\Big(\frac{L^{(r)}(E,1)}{r!\,\Omega_E\operatorname{Reg}(E/\mathbb{Q})}\Big)
=\operatorname{ord}_p\Big(\frac{\#\operatorname{Sha}(E/\mathbb{Q})\prod_{\ell\mid N}c_\ell}{\#E(\mathbb{Q})_{\mathrm{tors}}^2}\Big),
$$
which makes sense because the left side is a nonzero rational number when $r_{\mathrm{an}}\le 1$
(Gross–Zagier for $r=1$, [GZ86, Thm. 7.3]; the Manin–Drinfeld theorem for $r=0$).

---

## 0. Standing hypotheses used throughout

The theorems below are stated with the following named hypotheses on a pair $(E,p)$ or a
triple $(E,p,K)$, $K$ an imaginary quadratic field of discriminant $-D_K$.

- **(irr)** $E[p]$ is irreducible as a $G_\mathbb{Q}$-module (equivalently, $E$ has no rational
  $p$-isogeny). For $p$ odd this implies $E(\mathbb{Q})[p]=0$.
- **(sur)** $\bar\rho_{E,p}$ is surjective onto $\mathrm{GL}_2(\mathbb{F}_p)$. For non-CM $E$ this holds
  for all but finitely many $p$ (Serre's open image theorem [Ser72]).
- **(ram)** there exists a prime $\ell\,\|\,N$ (multiplicative reduction) such that $E[p]$ is
  ramified at $\ell$. By the theory of the Tate curve, for $\ell\,\|\,N$ the module $E[p]$ is
  unramified at $\ell$ iff $p\mid \operatorname{ord}_\ell(\Delta_{\min})$; for $\ell$ of *split*
  multiplicative reduction $c_\ell=\operatorname{ord}_\ell(\Delta_{\min})$, so **(ram)** at a split
  $\ell$ says exactly $p\nmid c_\ell$. CM curves never satisfy **(ram)** (they have no multiplicative primes).
- **(im)** there exists $\sigma\in G_{\mathbb{Q}(\mu_{p^\infty})}$ with $T_pE/(\sigma-1)T_pE\simeq\mathbb{Z}_p$
  (used in [BCS25]); implied by **(sur)** for $p\ge5$; fails for residually dihedral $p$.
- **Eisenstein prime**: $p$ such that $E[p]$ is reducible, $E[p]^{ss}\simeq\mathbb{F}_p(\varphi)\oplus\mathbb{F}_p(\psi)$
  with $\varphi\psi=\omega$ (mod-$p$ cyclotomic character). If $p>2$ is a good Eisenstein prime
  then $p$ is ordinary (Fontaine) and $p\in\{3,5,7,13,37\}$ (Mazur), as recalled in [CGLS22, §0.1].
- **(Heeg)** every prime $\ell\mid N$ splits in $K$; **(disc)** $D_K$ odd and $D_K\ne3$;
  **(spl)** $p$ splits in $K$. The *generalised Heegner hypothesis* writes $N=N^+N^-$ with $N^-$
  squarefree, $\ell\mid N^+$ split and $\ell\mid N^-$ inert in $K$.
- **semistable** means $N$ squarefree; **good ordinary** at $p$ means $p\nmid N$, $p\nmid a_p$;
  **supersingular** means $p\nmid N$, $p\mid a_p$ (for $p\ge5$ this forces $a_p=0$).

Two facts that are used silently everywhere:

- `[THEOREM]` Every $E/\mathbb{Q}$ is modular: $L(E,s)=L(f,s)$ for a weight-2 newform $f$ of level $N$
  ([Wil95], [TW95], [BCDT01]). Hence $L(E,s)$ is entire, satisfies the functional equation with
  root number $w(E)\in\{\pm1\}$, and $r_{\mathrm{an}}\equiv \frac{1-w(E)}{2}\pmod 2$.
- `[THEOREM]` (Cassels) If $\operatorname{Sha}(E/\mathbb{Q})$ is finite its order is a square; more
  generally $\operatorname{Sha}(E/\mathbb{Q})/\operatorname{Sha}(E/\mathbb{Q})_{\mathrm{div}}$ carries a nondegenerate
  alternating pairing [Cas62].

---

## 1. The unconditional backbone: analytic rank $\le 1$

### 1.1 Gross–Zagier

`[THEOREM]` (Gross–Zagier [GZ86]) Let $E/\mathbb{Q}$ have conductor $N$ and let $K$ be an imaginary
quadratic field satisfying **(Heeg)** with $(D_K,2N)=1$. Let $y_K\in E(K)$ be the Heegner point
(trace to $K$ of the image under a modular parametrisation $X_0(N)\to E$ of a Heegner point of
conductor one). Then
$$L'(E/K,1)=c\cdot\hat h(y_K),\qquad c=c(E,K)\in\mathbb{R}_{>0}\ \text{explicit},$$
where $\hat h$ is the Néron–Tate height. In particular $y_K$ is non-torsion iff $L'(E/K,1)\neq0$;
and $\operatorname{ord}_{s=1}L(E/K,s)=1$ iff $y_K$ is non-torsion (the sign of $L(E/K,s)$ is $-1$ under **(Heeg)**).

`[THEOREM]` (S. Zhang [Zha01a], [Zha01b]; Yuan–Zhang–Zhang [YZZ13]) The Gross–Zagier formula holds
for CM points on Shimura curves over totally real fields $F$, for arbitrary level and arbitrary
CM extension $K/F$ (no restriction on the discriminant, no squarefreeness of the level), in the
form $L'(1/2,\pi_K)\doteq\hat h(P_K(f))$ up to an explicit nonzero constant (Waldspurger-type
period pairing). For $F=\mathbb{Q}$ this removes the hypothesis $(D_K,2N)=1$ and allows the
generalised Heegner hypothesis $N=N^+N^-$ with $N^-$ having an even number of prime factors.

### 1.2 Kolyvagin

`[THEOREM]` (Kolyvagin [Kol88], [Kol89], [Kol90], [Kol91a], [Kol91b]; exact form as in [MN19, Thm. 0.3])
Let $E/\mathbb{Q}$, $K$ satisfying **(Heeg)**, $D_K\ne-3,-4$, and suppose $y_K\notin E(K)_{\mathrm{tors}}$.
Then $E(K)/\mathbb{Z}y_K$ and $\operatorname{Sha}(E/K)$ are finite; in particular $\operatorname{rank}E(K)=1$.
More precisely, for every prime $p\ne2$ such that

1. $H^1(K(E[p^{n_1+n_2}])/K,E[p^{n_1}])=0$ for all $n_1,n_2\ge0$ (automatic when **(irr)** holds, by [LW16], cf. [MN19, (0.11)]),
2. **(irr)** holds, and
3. $E(K)[p]=0$ (implied by (2) for $p\ne2$),

one has $p^{m_0}\operatorname{Sha}(E/K)[p^\infty]=0$ and $\#\operatorname{Sha}(E/K)[p^\infty]\mid p^{2m_0}$, where
$m_0=\sup\{m: y_K\in p^mE(K)\}$, i.e. $p^{m_0}=[E(K)\otimes\mathbb{Z}_p:\mathbb{Z}_p y_K]$.
If moreover $\rho_{E,p}:G_\mathbb{Q}\to\mathrm{GL}_2(\mathbb{Z}_p)$ has "big image" (e.g. is surjective), then
$\operatorname{Sha}(E/K)[p^\infty]\simeq X\oplus X$ with $X\simeq\bigoplus_{i\ge0}\mathbb{Z}/p^{m_i-m_{i+1}}$
for a nonincreasing sequence $m_0\ge m_1\ge\cdots\ge m_\infty$ defined by divisibilities of
derived Heegner points, so $\#\operatorname{Sha}(E/K)[p^\infty]=p^{2(m_0-m_\infty)}$ [Kol91b], [MN19, Thm. 0.7].

**Caution.** The upper bound $\#\operatorname{Sha}(E/K)[p^\infty]\mid p^{2m_0}$ is a *bound*, not an
equality; equality is the content of Kolyvagin's conjecture $m_\infty=0$ refined by W. Zhang
(§5). Also, [MN19, (0.10)] records that the cohomological lemmas [GJPST09, Lemma 5.7, 5.9] and
the proof of [GJPST09, Prop. 5.4] are incorrect (numbering as in [MN19]), so that [GJPST09, Thm. 3.7]
"remains unproved"; the corrected statement is [LW16, Thm. 14]. See §9.

### 1.3 The Gross–Zagier–Kolyvagin theorem over $\mathbb{Q}$

`[THEOREM]` For every elliptic curve $E/\mathbb{Q}$:
$$r_{\mathrm{an}}\le1\ \Longrightarrow\ r_{\mathrm{alg}}=r_{\mathrm{an}}\ \text{ and }\ \operatorname{Sha}(E/\mathbb{Q})\ \text{is finite}.$$
Ingredients: modularity; the existence, for each $E$ and each sign, of infinitely many $K$
satisfying **(Heeg)** with $L(E^{K},1)\ne0$ (Waldspurger [Wal85], Bump–Friedberg–Hoffstein
[BFH90], Murty–Murty [MM91]) or with $L'(E^K,1)\ne0$ [BFH90], [MM91]; Gross–Zagier (§1.1) applied
to $L(E/K,s)=L(E,s)L(E^K,s)$; Kolyvagin (§1.2); and descent from $K$ to $\mathbb{Q}$ using the
$\pm$-eigenspaces for complex conjugation. No hypothesis on $E$ is needed. The original statement
in [Kol88] assumed modularity ("Weil curves"); that hypothesis is now vacuous.

### 1.4 Kato's theorem

`[THEOREM]` (Kato [Kat04, Thm. 14.2(2), Cor. 14.3]) Let $A/\mathbb{Q}$ be a quotient of $J_1(N)$ (in
particular any $E/\mathbb{Q}$), $L/\mathbb{Q}$ finite abelian, $\chi$ a character of $\operatorname{Gal}(L/\mathbb{Q})$ with
$L(A,\chi,1)\ne0$. Then the $\chi$-parts of $A(L)$ and of $\operatorname{Sel}(L,A[p^\infty])$ are finite for
every prime $p$, and the $\chi$-part of $\operatorname{Sel}(L,A[p^\infty])$ is $0$ for all but finitely many $p$.
For $L=\mathbb{Q}$: $L(E,1)\ne0\Rightarrow E(\mathbb{Q})$ finite and $\operatorname{Sha}(E/\mathbb{Q})$ finite. This is a proof
of the $r_{\mathrm{an}}=0$ case of §1.3 that uses Beilinson–Kato elements instead of Heegner points
and no nonvanishing theorem for twists. (The CM case in Kato's proof relies on Rubin [Rub91].)

`[THEOREM]` (Kato [Kat04, Thm. 17.4, Thm. 12.5(4)]) Let $p\nmid N$ be a prime of good ordinary
reduction. Then the Pontryagin dual $X$ of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)$ is a torsion
$\Lambda$-module and $\operatorname{char}_\Lambda(X)$ divides $p^n\cdot L_p(E)$ for some $n\ge0$ (i.e. divides
$L_p(E)$ in $\Lambda\otimes\mathbb{Q}_p$). If moreover $p\ne2$ and there is a $\mathbb{Z}_p$-basis of $T_pE$
in which the image of $G_{\mathbb{Q}(\mu_{p^\infty})}$ contains $\mathrm{SL}_2(\mathbb{Z}_p)$ (condition (12.5.2)),
the divisibility holds in $\Lambda$. (Wüthrich [Wut14] later established integrality of $L_p(E)$
and integral divisibility under weaker hypotheses; see [CGS25, §1].)

`[THEOREM]` (Kato [Kat04, Thm. 18.4]; Perrin-Riou) For $p$ ordinary (good ordinary or multiplicative),
$\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le\operatorname{ord}_{s=1}L_p(E,s)$ if $E$ is not a Tate
curve at $p$, and $\le\operatorname{ord}_{s=1}L_p(E,s)-1$ if $E$ has split multiplicative reduction at $p$
(exceptional zero of [MTT86]). In particular $r_{\mathrm{alg}}\le r_p$ in the notation of the charter.

---

## 2. Analytic rank 0

### 2.1 CM curves: Coates–Wiles, Rubin

`[THEOREM]` (Coates–Wiles [CW77]) Let $E/\mathbb{Q}$ have complex multiplication by (an order in) an
imaginary quadratic field $K$ of class number one. If $L(E,1)\ne0$ then $E(\mathbb{Q})$ is finite.
(Extended to $E$ defined over $K$ and to general $K$ by Arthaud and by Rubin; see [Rub99, Thm. 10.1].)

`[THEOREM]` (Rubin [Rub87]) Let $E/K$ have CM by $K$ (imaginary quadratic). If $L(E/K,1)\ne0$ then
$\operatorname{Sha}(E/K)$ is finite. For $E/\mathbb{Q}$ with CM by $K$ one has $L(E/K,s)=L(E,s)^2$, so
$L(E,1)\ne0\Rightarrow\operatorname{Sha}(E/\mathbb{Q})$ finite (a CM special case of §1.3, proved earlier and by
elliptic units).

`[THEOREM]` (Rubin [Rub91]; formulation as recalled in [Rub99, Introduction] and [BT25, (1.2)]) Let
$E/K$ have CM by $\mathcal{O}_K$ with $L(E/K,1)\ne0$. Then $\operatorname{Sha}(E/K)$ is finite and for every prime
$p\nmid\#\mathcal{O}_K^\times$ (so every $p\ge5$; also $p=3$ unless $K=\mathbb{Q}(\sqrt{-3})$; never $p=2$)
the $p$-part of the BSD formula for $E/K$ holds, with no assumption of good reduction at $p$
([Rub99] proves the weaker statement for $p>7$ of good reduction and attributes the general one to
[Rub91]). Rubin's proof is via his main conjectures for $K$ (two-variable for $p$ split, one-variable
for $p$ inert), proved for $p\nmid\#\mathcal{O}_K^\times$. For $E/\mathbb{Q}$ with CM by $K$ one has
$L(E/K,s)=L(E,s)^2$ and $E^{K}$ is $\mathbb{Q}$-isogenous to $E$, so by isogeny invariance of the BSD
formula the $p$-part for $E/\mathbb{Q}$ follows for the same $p$.
**Missing:** $p=2$ for all CM curves, and $p=3$ for CM by $\mathbb{Q}(\sqrt{-3})$. `[GAP]`-type
statement: *for $E/\mathbb{Q}$ with CM by $\mathbb{Z}[i]$ (resp. $\mathbb{Z}[\zeta_3]$) and $L(E,1)\ne0$, prove
$\operatorname{ord}_2$ (resp. $\operatorname{ord}_3$) of the BSD formula*; this is known only for explicit families
(§6.6, [CLTZ15], [Zha25], [GJM26]).

### 2.2 Kolyvagin and Kato in rank 0

Both §1.3 and §1.4 give: $L(E,1)\ne0\Rightarrow E(\mathbb{Q})$ and $\operatorname{Sha}(E/\mathbb{Q})$ finite, for
**every** $E/\mathbb{Q}$. Kato in addition bounds $\operatorname{Sha}$ from above:

`[THEOREM]` (Kato; in the form [JSW17, Thm. 7.2.1(i)]) Let $p$ be an odd prime at which $E$ has
good or multiplicative reduction, assume **(irr)**, and $L(E,1)\ne0$. Then
$$\operatorname{ord}_p\#\operatorname{Sha}(E/\mathbb{Q})[p^\infty]\ \le\ \operatorname{ord}_p\Big(\frac{L(E,1)}{\Omega_E\prod_\ell c_\ell}\Big).$$
(Note that **(irr)** with $p$ odd forces $\#E(\mathbb{Q})[p]=1$, so the torsion term is absent.)

### 2.3 The cyclotomic main conjecture at good ordinary primes and the $p$-part in rank 0

`[THEOREM]` (Skinner–Urban [SU14, Thm. 1 = Thm. 3.6.4]) Let $p$ be an odd prime and $f\in S_k(N)$ a
$p$-ordinary newform with trivial character, $k\equiv2\pmod{p-1}$, $p\nmid N$, such that
$\bar\rho_f$ is irreducible and there exists $q\ne p$, $q\,\|\,N$, with $\bar\rho_f$ ramified at $q$.
Then $\operatorname{Ch}_{\mathbb{Q}_\infty}(f)=(\mathcal{L}_f)$ in $\Lambda\otimes\mathbb{Q}_p$; if moreover the image of $\rho_f$
contains $\mathrm{SL}_2(\mathbb{Z}_p)$ in some basis, the equality holds in $\Lambda$ (Mazur's main conjecture).

`[THEOREM]` (Skinner–Urban [SU14, Thm. 2 = Thm. 3.6.11]) Let $E/\mathbb{Q}$ have good ordinary reduction
at the odd prime $p$, with **(irr)** and **(ram)**. Then
(a) if $L(E,1)\ne0$ and **(sur)** holds, $\big|L(E,1)/\Omega_E\big|_p^{-1}=\#\operatorname{Sha}(E/\mathbb{Q})[p^\infty]\cdot\prod_{\ell\mid N}|c_\ell|_p^{-1}$
(the $p$-part of the BSD formula);
(b) if $L(E,1)=0$ then $\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ge1$.
The hypotheses hold for every semistable $E$ and every good ordinary $p\ge11$ [SU14, §1.2].

`[THEOREM]` (Skinner [Ski16, Thm. A, Thm. B]) The main conjecture of [SU14, Thm. 1] also holds
when $p\,\|\,N$ ($E$ multiplicative at $p$, $p\ge3$, **(irr)**, **(ram)** at some $q\ne p$); consequently
the $p$-part of the BSD formula in rank 0 holds for such $p$.

`[THEOREM]` (summary form, [JSW17, Thm. 7.2.1(ii)]) Let $p$ be odd, $E$ good ordinary or
multiplicative at $p$, **(irr)**, and suppose there is a prime $q$ of multiplicative reduction
at which $E[p]$ is ramified (**(ram)**). If $L(E,1)\ne0$ then
$\operatorname{ord}_p\#\operatorname{Sha}(E/\mathbb{Q})[p^\infty]=\operatorname{ord}_p\big(L(E,1)/(\Omega_E\prod_\ell c_\ell)\big)$.

`[THEOREM]` (Burungale–Castella–Skinner [BCS25, Thm. 1.1.2, Cor. 1.3.1]) Let $E/\mathbb{Q}$ be non-CM and
$p>3$ a prime of good ordinary reduction with **(irr)**. Then Mazur's main conjecture holds in
$\Lambda\otimes\mathbb{Q}_p$; if also **(im)** holds it holds in $\Lambda$, and then for
$r_{\mathrm{an}}=r\in\{0,1\}$ the $p$-part of the BSD formula holds. **No ramification hypothesis
(ram) is needed**; **(im)** excludes only finitely many $p$ for non-CM $E$ (residually dihedral
$p$ are the essential excluded case). This uses base change to an imaginary quadratic $K$ with
all primes dividing $Np$ split and Wan's divisibility over a quartic CM field.

`[THEOREM]` (Yan–Zhu [YaZ26]) further cases of the main conjectures and of the $p$-part of BSD
for $r_{\mathrm{an}}\le1$ at good ordinary $p>2$ with **(irr)** (J. Algebra 693 (2026); statement
verified only at abstract level, exact additional hypotheses not reproduced here).

### 2.4 Eisenstein primes

`[THEOREM]` (Greenberg–Vatsal [GV00]; formulation as in [CGS25, §1]) Let $p$ be an odd good
ordinary prime with $E[p]\supset\mathbb{F}_p(\varphi)$ reducible and assume **(GV)**: $\varphi$ is either
unramified at $p$ and odd, or ramified at $p$ and even. Then $\mu$-invariants vanish and, with
Kato's divisibility, Mazur's main conjecture holds for $(E,p)$.

`[THEOREM]` (Castella–Grossi–Skinner [CGS25, Thm. A]) Let $p>2$ be a good prime with $E[p]$
reducible with kernel $\mathbb{F}_p(\varphi)$ of a rational $p$-isogeny, and assume $\varphi|_{G_p}\ne1,\omega$
($G_p$ a decomposition group at $p$). Then $X^{\mathrm{ord}}(E/\mathbb{Q}_\infty)$ is $\Lambda$-torsion and
$\operatorname{char}_\Lambda X^{\mathrm{ord}}(E/\mathbb{Q}_\infty)=(L_p^{\mathrm{MSD}}(E))$: Mazur's main conjecture holds
(no **(GV)** needed). Consequence (via the control theorem, with the torsion term now present):
the $p$-part of the BSD formula in rank 0 at such Eisenstein primes.

`[THEOREM]` (Keller–Yin [KY24a], abstract level) The condition $\varphi|_{G_p}\ne1,\omega$ can be
removed from [CGLS22] in the anticyclotomic setting, giving main conjectures and the $p$-part of
strong BSD in analytic rank 0 and 1 at Eisenstein primes with nontrivial rational $p$-torsion
allowed; also a main conjecture at Eisenstein primes of multiplicative reduction (weight 2).
`[unverified]` beyond the abstract.

### 2.5 Supersingular primes

`[THEOREM]` (Kobayashi [Kob03]; Pollack [Pol03]) For $p\nmid 2N$ supersingular with $a_p=0$ there are
signed Selmer groups $\operatorname{Sel}^\pm$ with $\Lambda$-torsion duals $X^\pm$ and signed $p$-adic
$L$-functions $L_p^\pm(E)\in\Lambda$; Kobayashi proved (from Kato) $\xi_\Lambda(X^\pm)\mid L_p^\pm(E)$ and
formulated the main conjecture $\xi_\Lambda(X^\pm)=(L_p^\pm(E))$.

`[THEOREM]` (Pollack–Rubin [PR04]) Kobayashi's $\pm$ main conjecture holds for CM elliptic curves
at supersingular (inert) primes $p\ge5$ [hypotheses as in the source; abstract-level verification].

`[THEOREM]` (Burungale–Skinner–Tian–Wan [BSTW24, Thm. 1.3, 1.5, 1.6]) Let $E/\mathbb{Q}$ be
**semistable** and $p>2$ supersingular ($a_3=0$ if $p=3$). Then Kobayashi's main conjecture
holds for $E$ and for every quadratic twist $E_K$ by a quadratic field of discriminant coprime to
$Np$ divisible only by primes of ordinary reduction for $E$. Consequently, if $r_{\mathrm{an}}\le1$ the
$p$-part of the BSD formula holds, and $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=0\Rightarrow L(E,1)\ne0$.
[BSTW24, Rem. 1.4] states that Wan's 2014 preprint [Wan14] announcing this "is no longer intended
for publication" and is superseded; **cite [BSTW24], not [Wan14]**.

`[THEOREM]` (Castella–Çiperiani–Skinner–Sprung [CCSS18], abstract level; preprint) Under "mild
hypotheses" the Lei–Loeffler–Zerbes main conjectures for weight-2 newforms at non-ordinary $p>2$
hold, giving the $p$-part of BSD in analytic rank $0$ or $1$ for $\mathrm{GL}_2$-type abelian
varieties over $\mathbb{Q}$. `[unverified]` publication status and exact hypotheses.

`[THEOREM]` (Ito–Sprung [IS24]) Main conjectures at supersingular primes "beyond the case
$a_p=0$" (relevant only for $p\in\{2,3\}$), Adv. Math. 449 (2024). Exact statements not reproduced
here (`[unverified]` beyond title/DOI). Sprung's 2016 preprint [Spr16] claims the main conjecture
at all odd supersingular primes; its publication status could not be confirmed.

`[THEOREM]` (Castella–Liu–Wan [CLW26], Aug 2026, preprint) Kato's main conjecture (in its signed
Selmer formulation) for modular forms at non-ordinary primes for weights in the Fontaine–Laffaille
range. For elliptic curves this is a second route to Kobayashi's conjecture; hypotheses not
reproduced (`[unverified]` beyond abstract).

### 2.6 Rank-zero converses ("$\operatorname{Sel}_{p^\infty}$ finite $\Rightarrow L(E,1)\ne0$")

- `[THEOREM]` [SU14, Thm. 2(b)]: $p$ odd good ordinary, **(irr)**, **(ram)**.
- `[THEOREM]` [BSTW24, Thm. 1.6]: $E$ semistable, $p>2$ supersingular ($a_3=0$ if $p=3$), and its quadratic twists as above.
- `[THEOREM]` [CGLS22, Thm. E] ($r=0$): $p>2$ good Eisenstein with $\varphi|_{G_p}\ne1,\omega$.
- `[THEOREM]` [BCS25]: $p>3$ good ordinary, non-CM, **(irr)** + **(im)** (from the integral main conjecture).
- `[THEOREM]` (Burungale–Tian [BT25, Thm. 1.1], preprint June 2025, v2 Oct 2025) Let $E/K$ have CM by
  an order of the imaginary quadratic field $K$ and let $p$ be **any** prime. Then
  $\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/K)=0\Rightarrow\operatorname{ord}_{s=1}L(E/K,s)=0$; in
  particular for $E/\mathbb{Q}$ with CM, $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=0\Rightarrow L(E,1)\ne0$
  for every $p$, including $p=2$. Proved via the CM case of Kato's main conjecture (elliptic units).
  Previously known for $p\nmid\#\mathcal{O}_K^\times$ by Rubin [Rub91].

---

## 3. Analytic rank 1

### 3.1 Rank and finiteness of Sha
`[THEOREM]` (§1.3) $r_{\mathrm{an}}=1\Rightarrow r_{\mathrm{alg}}=1$ and $\operatorname{Sha}(E/\mathbb{Q})$ finite, for all $E/\mathbb{Q}$.
The Kolyvagin bound (§1.2) gives, for $p\ne2$ with **(irr)** and a suitable $K$,
$\#\operatorname{Sha}(E/K)[p^\infty]\le[E(K)\otimes\mathbb{Z}_p:\mathbb{Z}_py_K]^2$, which by Gross–Zagier is the
**upper** bound predicted by BSD for $E/K$ up to Tamagawa factors. The **lower** bound is the
hard direction (§3.3).

### 3.2 $p$-adic Gross–Zagier formulas

- `[THEOREM]` (Perrin-Riou [PR87]) For $p$ good ordinary (and $K$ satisfying **(Heeg)**, $p$ split in $K$,
  $p\nmid 2N D_K$), the derivative of the cyclotomic $p$-adic $L$-function of $E/K$ at the central
  point equals (an explicit nonzero constant times) the cyclotomic $p$-adic height $\langle y_K,y_K\rangle_p$.
- `[THEOREM]` (Kobayashi [Kob13]) The same for supersingular $p$ ($a_p=0$) with Pollack's $\pm$
  $p$-adic $L$-functions and $\pm$ $p$-adic heights; the $p$-adic height of $y_K$ is shown to be
  nonzero when $y_K$ is non-torsion [Kob13, Thm. 1.1, Cor. 4.9] (as summarised in [JSW17, §1.2]).
- `[THEOREM]` (Rubin [Rub92]) $p$-adic Gross–Zagier for CM curves at split $p$ via elliptic units.
- `[THEOREM]` (Disegni [Dis17], [Dis22]) $p$-adic Gross–Zagier on Shimura curves over totally real
  fields, and a universal (Hida-family) version.
- `[THEOREM]` (Bertolini–Darmon–Prasanna [BDP13]; Brooks [Bro15]) The "$p$-adic Waldspurger formula":
  the value at the trivial character of the anticyclotomic $p$-adic $L$-function $L_p^{\mathrm{BDP}}(E/K)$
  (outside its interpolation range) equals $(1-a_pp^{-1}+p^{-1})^2\log_{\omega_E}(y_K)^2$ up to a unit,
  for $p$ split in $K$ satisfying **(Heeg)** (resp. the generalised Heegner hypothesis for Brooks).
  This is the key input for all rank-one $p$-converse theorems below.

### 3.3 The $p$-part of the BSD formula in analytic rank 1

`[THEOREM]` (W. Zhang [Zha14, Thm. 1.6]) Let $E/\mathbb{Q}$, $p\ge5$ good ordinary, with **(sur)**, and:
(2) if $\ell\,\|\,N$ and $\ell\equiv\pm1\pmod p$ then $E[p]$ is ramified at $\ell$; (3) if $N$ is not
squarefree then $\#\operatorname{Ram}(\bar\rho_{E,p})\ge1$, and when $\#\operatorname{Ram}(\bar\rho_{E,p})=1$ the number of
$\ell\,\|\,N$ is even (here $\operatorname{Ram}$ is the set of $\ell\,\|\,N$ at which $E[p]$ is ramified). If
$r_{\mathrm{an}}=1$ then the $p$-part of the BSD formula holds. (Condition (2) is equivalent to
$p\nmid c_\ell$ for such $\ell$, so Tamagawa factors divisible by $p$ are excluded.)

`[THEOREM]` (Jetchev–Skinner–Wan [JSW17, Thm. 1.2.1]) Let $E/\mathbb{Q}$ be **semistable** with
$r_{\mathrm{an}}=1$, and $p\ge3$ a prime of good reduction with **(irr)**. If $p\ge5$ then
$$\operatorname{ord}_p\Big(\frac{L'(E,1)}{\Omega_E\operatorname{Reg}(E/\mathbb{Q})}\Big)=\operatorname{ord}_p\Big(\#\operatorname{Sha}(E/\mathbb{Q})\prod_{\ell}c_\ell\Big);$$
for $p=3$ the same holds provided $a_3=0$ when $E$ is supersingular at $3$. Ordinary and
supersingular $p$ are treated uniformly, and Tamagawa numbers divisible by $p$ are allowed. The
lower bound on $\#\operatorname{Sha}[p^\infty]$ comes from Wan's divisibility in the anticyclotomic
(Bertolini–Darmon–Prasanna) main conjecture [Wan20] together with the $p$-adic Waldspurger formula
and an anticyclotomic control theorem; the upper bound from Kolyvagin over a second auxiliary field
and the rank-0 $p$-part (§2.3, §2.5) for the quadratic twist.

`[THEOREM]` (Castella [Cas18]) Same conclusion for semistable $E$ with $r_{\mathrm{an}}=1$ and $p>3$ a
prime of **multiplicative** reduction with **(irr)**.

`[THEOREM]` (Burungale–Skinner–Tian–Wan [BSTW24, Thm. 1.5, 1.9]) (i) $E$ semistable, $p>2$
supersingular ($a_3=0$ if $p=3$), $r_{\mathrm{an}}\le1$: $p$-part of BSD (also for the quadratic twists
in [BSTW24, Thm. 1.3]). (ii) $E/\mathbb{Q}$ arbitrary conductor, $p\nmid2N$ ordinary, **(irr)** (absolutely
irreducible) and **(ram)**, $r_{\mathrm{an}}=1$: $p$-part of BSD. By [BSTW24, Rem. 1.11], **(ram)** may be
replaced by the existence of an auxiliary real quadratic field as in [SU14, Thm. 4]. The CM case
is [BSTW24, Thm. 11.12].

`[THEOREM]` (Burungale–Castella–Skinner [BCS25, Cor. 1.3.1]) $E$ non-CM, $p>3$ good ordinary,
**(irr)** + **(im)**, $r_{\mathrm{an}}=1$: $p$-part of BSD, with no condition on the conductor.

`[THEOREM]` (Castella–Grossi–Lee–Skinner [CGLS22, Thm. F]) Let $p>2$ be a good Eisenstein prime,
$E[p]^{ss}=\mathbb{F}_p(\varphi)\oplus\mathbb{F}_p(\psi)$, with $\varphi|_{G_p}\ne1,\omega$ and $\varphi$ either
ramified at $p$ and odd or unramified at $p$ and even. If $r_{\mathrm{an}}=1$ then the $p$-part of the
BSD formula holds, in the form $\operatorname{ord}_p(L'(E,1)/(\operatorname{Reg}\cdot\Omega_E))=\operatorname{ord}_p(\#\operatorname{Sha}\prod c_\ell)$.
(No torsion term appears because $\varphi|_{G_p}\ne1,\omega$ forces $E(\mathbb{Q})[p]=0$: a rational
$p$-torsion point would make one of $\varphi,\psi$ trivial, hence $\varphi\in\{1,\omega\}$.) [KY24a]
claims the removal of $\varphi|_{G_p}\ne1,\omega$, allowing nontrivial rational $p$-torsion.

`[THEOREM]` (CM curves in rank 1) (a) Li–Liu–Tian [LLT16, preprint]: $E/\mathbb{Q}$ CM, $r_{\mathrm{an}}=1$, $p$
potentially good ordinary with $p\nmid\#\mu_K$: $\#\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ is as predicted.
(b) Castella [Cas24b, abstract]: for $E/F$ CM by $\mathcal{O}_K$ over a number field $F$ (torsion
points generating an abelian extension of $K$), the $p$-part of BSD in analytic rank 1 for $p>3$
split in $K$; for $F=\mathbb{Q}$ this "was previously known by work of Rubin as a consequence of his proof
of Mazur's main conjecture for rational CM elliptic curves" (together with [PR87]/[Rub92] and the
nonvanishing of $p$-adic heights on CM curves). (c) supersingular $p$: [JSW17, §1.2] records that
[Kob13, Cor. 1.4] gives the $p$-part for CM curves at supersingular primes from the $p$-adic
Gross–Zagier formula and the Pollack–Rubin main conjecture (hypotheses as in [Kob13]; not
reproduced).

**What is not covered in rank 1** (`[GAP]`-type list): $p=2$ (all curves); $p=3$ ordinary in many
configurations (e.g. [JSW17] needs $p\ge5$ for ordinary $p$, [BCS25] needs $p>3$); additive primes
$p^2\mid N$ (no result); residually dihedral $p$ without **(ram)**; Eisenstein primes outside
[CGLS22]/[KY24a]; CM curves at $p\mid\#\mathcal{O}_K^\times$.

### 3.4 Perrin-Riou's conjecture (Beilinson–Kato elements vs. Heegner points)

`[CONJECTURE]` (Perrin-Riou [PR93]) Let $z_E\in H^1(\mathbb{Q},V_pE)$ be the Beilinson–Kato element and
suppose $L(E,1)=0$. Then there is $P\in E(\mathbb{Q})$ with $\log_\omega(\operatorname{loc}_p z_E)\doteq\log_\omega(P)^2$
(equality up to $\mathbb{Q}^\times$) and $P$ non-torsion iff $r_{\mathrm{an}}=1$.

`[THEOREM]` (Bertolini–Darmon–Venerucci [BDV22]; Burungale–Skinner–Tian `[reference unverified]`;
and in full generality [BSTW24, Thm. 1.13]) Perrin-Riou's conjecture holds for every $E/\mathbb{Q}$ and
every $p\nmid2N$ (with $a_3=0$ if $p=3$ is supersingular). [BDV22] and the earlier results treat
good ordinary $p$ under additional hypotheses (not reproduced).

---

## 4. Converse theorems

The GZK theorem gives $r_{\mathrm{an}}\le1\Rightarrow$ ($r_{\mathrm{alg}}=r_{\mathrm{an}}$, Sha finite). A *$p$-converse*
is $\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r\Rightarrow r_{\mathrm{an}}=r$ ($r\in\{0,1\}$). Since
$\operatorname{corank}\operatorname{Sel}_{p^\infty}=r_{\mathrm{alg}}+\operatorname{corank}\operatorname{Sha}[p^\infty]$, a $p$-converse
yields: ($r_{\mathrm{alg}}=r$ and $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ finite) $\Rightarrow r_{\mathrm{an}}=r$.

**Rank 0.** See §2.6.

**Rank 1, non-CM, good ordinary $p$.**
- `[THEOREM]` (Skinner [Ski20, Thm. C]) $E$ semistable, with at least one odd prime of nonsplit
  multiplicative reduction or at least two odd primes of split multiplicative reduction; $p\ge5$ good
  ordinary with **(irr)**, $\operatorname{Sel}_p(E/\mathbb{Q})\simeq\mathbb{Z}/p$, and the image of
  $\operatorname{Sel}_p(E/\mathbb{Q})\to E(\mathbb{Q}_p)/pE(\mathbb{Q}_p)$ not contained in the image of $E(\mathbb{Q}_p)[p]$. Then
  $r_{\mathrm{an}}=1=r_{\mathrm{alg}}$ and $\operatorname{Sha}(E/\mathbb{Q})$ is finite. The general form [Ski20, Thm. B] is
  stated over an imaginary quadratic $K$ for $A_f$ ($N$ squarefree, $p\ge5$, $p\nmid N$, $f$ ordinary,
  $\bar\rho$ irreducible and ramified at an odd prime inert or ramified in $K$, $2$ and $p$ split in
  $K$, conditions on $(D_K,N)$, $\dim H^1_f(K,V)=1$ with injective localisation at $p$).
- `[THEOREM]` (Skinner [Ski20, Thm. A$'$]) $E$ semistable with at least one odd prime of nonsplit
  multiplicative reduction or two odd primes of split multiplicative reduction:
  $r_{\mathrm{alg}}=1$ and $\#\operatorname{Sha}(E/\mathbb{Q})<\infty\Rightarrow r_{\mathrm{an}}=1$ (unconditional in $p$: some $p$ is chosen in the proof).
- `[THEOREM]` (W. Zhang [Zha14, Thm. 1.4(i)]) $p\ge5$ good ordinary, **(sur)**, conditions (2),(3) of
  §3.3: $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow r_{\mathrm{an}}=r_{\mathrm{alg}}=1$, Sha finite.
  [Zha14, Thm. 1.4(ii)]: under the same hypotheses, $r_{\mathrm{an}}>1\Rightarrow\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ge2$
  (resp. $\ge3$) if $w(E)=+1$ (resp. $-1$).
- `[THEOREM]` (W. Zhang [Zha14, Thm. 1.5]) If $N$ is squarefree, or $N$ is not squarefree but has at
  least two prime factors $\ell\,\|\,N$, then: $r_{\mathrm{alg}}=1$ and $\#\operatorname{Sha}(E/\mathbb{Q})<\infty$ $\iff$ $r_{\mathrm{an}}=1$.
- `[THEOREM]` (Sweeting [Swe20, Cor. C], preprint v3 2022) Over $K$ with the generalised Heegner
  hypothesis, $\nu(N^-)$ even, $p\nmid2ND_K$ and Condition $\diamondsuit$ ($\bar T_f$ absolutely
  irreducible, not induced from $\mathbb{Q}(\sqrt{-3})$ if $p=3$; if $p$ inert in $K$ or $a_p$ a non-unit,
  some $\ell\,\|\,N$ exists, with a further condition when $a_p$ is a non-unit):
  $L'(f/K,1)\ne0\iff\operatorname{rank}_{\mathcal{O}}\operatorname{Sel}(K,T_f)=1\iff\operatorname{rank}A_f(K)=[\mathcal{O}_f:\mathbb{Z}]$. New cases
  include residually dihedral image and $p=3$. Publication status: not confirmed (`[unverified]`).
- `[THEOREM]` (Burungale–Castella–Grossi–Skinner [BCGS26, Cor. A]) $p$ odd good ordinary, $K$ with
  **(Heeg)**, **(disc)**, $E(K)[p]=0$, $p$ split in $K$, and either $E$ has a rational $p$-isogeny with
  kernel $\mathbb{F}_p(\varphi)$, $\varphi|_{G_p}\ne1,\omega$, or $p>3$ with **(irr)**:
  $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/K)=1\Rightarrow\operatorname{ord}_{s=1}L(E/K,s)=1$; also the $p$-parity conjecture for $E/\mathbb{Q}$.
- `[THEOREM]` [BSTW24, Thm. 1.10]: $p\nmid2N$ ordinary, **(sur)**, **(ram)** (or an auxiliary real quadratic field):
  $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow r_{\mathrm{an}}=1$.
- `[THEOREM]` [BCS25]: $p>3$ good ordinary, non-CM, **(irr)** + **(im)** (from the integral anticyclotomic
  main conjecture [BCS25, Thm. 1.2.4] and [BDP13]).

**Rank 1, non-CM, supersingular $p$.**
- `[THEOREM]` (Castella–Wan [CW23]) A strengthened version of Skinner's converse at supersingular
  primes, from the supersingular Perrin-Riou (Heegner point) main conjecture ("under mild
  hypotheses"; exact list in the source, Math. Ann. 389 (2023)).

**Rank 1, non-CM, multiplicative $p$.**
- `[THEOREM]` (Venerucci [Ven16]) $E$ with split multiplicative reduction at an odd $p$, "under some
  mild technical assumptions": $r_{\mathrm{alg}}=1$ and $\#\operatorname{Sha}(E/\mathbb{Q})[p^\infty]<\infty\Rightarrow r_{\mathrm{an}}=1$.
- `[THEOREM]` (Castella [Cas24a, Thm. 1.1]) $E$ multiplicative at $p>3$, **(irr)**, nonsplit
  multiplicative reduction at some $q\ne p$ where $E[p]$ is ramified, and $E(\mathbb{Q}_p)[p]=0$:
  $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow r_{\mathrm{an}}=1$ (so $r_{\mathrm{alg}}=1$, Sha finite).
  Skinner–Zhang [SZ14, preprint] obtained a similar result under additional ramification hypotheses.

**Eisenstein primes.**
- `[THEOREM]` (Castella–Grossi–Lee–Skinner [CGLS22, Thm. E]) $p>2$ good Eisenstein, $\varphi|_{G_p}\ne1,\omega$,
  $r\in\{0,1\}$: $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r\Rightarrow r_{\mathrm{an}}=r$, hence $r_{\mathrm{alg}}=r$ and Sha finite.
- `[THEOREM]` (Keller–Yin [KY24b], abstract level) $p\ge3$, $E$ of potentially good ordinary reduction at
  an Eisenstein prime $p$, $p$-Selmer rank $0$ or $1$: $p$-converse. `[unverified]` beyond abstract.

**CM curves.**
- `[THEOREM]` (Rubin [Rub91]) rank-0 converse for $p\nmid\#\mathcal{O}_K^\times$ (§2.6).
- `[THEOREM]` (Burungale–Tian [BT20]) $E/\mathbb{Q}$ CM, $p>3$ good ordinary (split in $K$):
  $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow r_{\mathrm{an}}=1$.
- `[THEOREM]` (Burungale–Castella–Skinner–Tian [BCST22]) $E/\mathbb{Q}$ CM, $p$ **any** prime of good ordinary
  reduction (including $p=2,3$): $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow E(\mathbb{Q})$ has a point of
  infinite order coming from a Heegner point, so $r_{\mathrm{an}}=1$.
- `[THEOREM]` (Burungale–Kobayashi–Ota [BKO23, Thm. 1.5]) $E/\mathbb{Q}$ CM, $p\ge5$ good supersingular (inert in $K$):
  if $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=1$ and $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ is finite then $r_{\mathrm{an}}=1$.
- `[THEOREM]` (Burungale–Skinner, appendix to [ABS24, Thm. A.1, Thm. A.3]) $E/\mathbb{Q}$ CM, $p$ **any** prime of
  supersingular reduction (including $p=2$): if $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E)=1$ and the localisation
  $\operatorname{Sel}_{p^\infty}(E)\to E(\mathbb{Q}_p)\otimes\mathbb{Q}_p/\mathbb{Z}_p$ is surjective, then $r_{\mathrm{an}}=1=r_{\mathrm{alg}}$;
  for $p$ good ordinary (any $p$) the surjectivity hypothesis is not needed [ABS24, Thm. A.3].
- `[THEOREM]` (Burungale–Tian [BT25]) rank-0 converse for CM curves at **every** prime (§2.6).
- `[CONDITIONAL]`/`[unverified]` (Kriz [Kri20], preprint v5 Oct 2022, not published as of 2026-09) claims:
  $E/\mathbb{Q}$ CM by $\mathcal{O}_K$, $p$ **ramified** in $K$, $r_p:=\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le1\Rightarrow
  r_{\mathrm{alg}}=r_{\mathrm{an}}=r_p$ and Sha finite (which would include $p=2$ for $y^2=x^3-x$). Given that
  [BT25] (2025) describes its rank-0 result as "the first instance of the even parity Goldfeld
  conjecture", the team should treat [Kri20] as not established.

**Over other fields.** `[THEOREM]` (Bansal–Jha–Pal–Venkat [BJPV25], abstract level) $E/F$, $F$ real
quadratic, $p>5$ inert in $F$, split multiplicative at $\mathfrak p\mid p$, "under some technical
assumptions": $r_{\mathrm{alg}}(E/F)=1$ and $\#\operatorname{Sha}(E/F)[p^\infty]<\infty\Rightarrow\operatorname{ord}_{s=1}L(E/F,s)=1$.
`[THEOREM]` (Castella [Cas24b]) an analogue of Skinner's $p$-converse for CM elliptic curves and CM
abelian varieties over number fields (abstract level).

---

## 5. Kolyvagin's conjecture

`[CONJECTURE]` (Kolyvagin [Kol91a]) With $(E,p,K)$ as in §1.2 and $\{\kappa_n^{\mathrm{Heeg}}\in H^1(K,T/I_nT)\}$
the derived Heegner classes indexed by squarefree products $n$ of Kolyvagin primes, the system
$\{\kappa_n^{\mathrm{Heeg}}\}_n$ is nonzero, i.e. $\kappa_n^{\mathrm{Heeg}}\ne0$ for some $n$, **whatever the analytic rank**.
Kolyvagin proved [Kol91a, Thm. 4] that this implies
$\operatorname{ord}(\kappa^{\mathrm{Heeg}})=\max\{r^+(E/K),r^-(E/K)\}-1$, where $r^\pm$ are the $\mathbb{Z}_p$-coranks of the
$\pm$-eigenspaces of $\operatorname{Sel}_{p^\infty}(E/K)$ under complex conjugation; so the conjecture gives a
Heegner-point description of Selmer coranks in *every* rank. W. Zhang's refinement
[Zha14, Conj. 4.5] predicts $M_\infty=\sum_{\ell\mid N}\operatorname{ord}_p(c_\ell)$ for the divisibility index
$M_\infty=\lim_r\min_{\nu(n)=r}M(n)$ (for a $p$-optimal parametrisation).

`[THEOREM]` (W. Zhang [Zha14, Thm. 1.1]) Let $E/\mathbb{Q}$, $p\ge5$ good ordinary, $K$ imaginary quadratic
with $N^-$ squarefree with an even number of prime factors, $p\nmid D_KN$, $(D_K,N)=1$, **(sur)**,
and Hypothesis $\spadesuit$: $\operatorname{Ram}(\bar\rho_{E,p})$ contains all $\ell\,\|\,N^+$ and all $\ell\mid N^-$
with $\ell\equiv\pm1\pmod p$; and if $N$ is not squarefree, $\#\operatorname{Ram}(\bar\rho_{E,p})\ge1$ and either
$\operatorname{Ram}$ contains a prime $\ell\,\|\,N^-$ or there are at least two primes $\ell\,\|\,N^+$. Then
$\kappa_1(n)\ne0$ for some $n$ (Kolyvagin's conjecture), and in fact $M_\infty=0$.

`[THEOREM]` (Skinner–Zhang [SZ14], preprint) The analogue for $E$ with multiplicative reduction at
$p\ge5$, $E[p]$ irreducible and not finite at $p$, $p$ split in $K$, plus $p$-indivisibility of certain Tamagawa factors.

`[THEOREM]` (Zanarella [Zan19], preprint) A proof of Kolyvagin's conjecture for modular abelian
varieties over $\mathbb{Q}$ via the BDP main conjecture instead of the cyclotomic one (hypotheses as in
the source), a route suited to totally real fields.

`[THEOREM]` (Sweeting [Swe20, Thm. A]) Kolyvagin's conjecture for $f\in S_2(N)$ under the generalised
Heegner hypothesis with $\nu(N^-)$ even, $p\nmid2ND_K$, the scalar condition (sclr) and Condition
$\diamondsuit$ (§4); covers residually dihedral image and $p=3$, and $p$ inert in $K$ or non-ordinary
$a_p$ when some $\ell\,\|\,N$ exists. A "definite" analogue ($\nu(N^-)$ odd) [Swe20, Thm. D] describes
Selmer ranks via modified $L$-values. Uses ultrapatching of bipartite Euler systems.

`[THEOREM]` (Burungale–Castella–Grossi–Skinner [BCGS26, Thm. A, B, C]; v2 Jan 2026) Let $p$ be an odd
prime of good ordinary reduction and $K$ satisfy **(Heeg)**, **(disc)**, $E(K)[p]=0$, $p$ split in $K$.
If the rational anticyclotomic main conjecture holds (known when $E$ has a rational $p$-isogeny
with kernel $\mathbb{F}_p(\varphi)$, $\varphi|_{G_p}\ne1,\omega$ [CGS25], or when $p>3$ and **(irr)** [BCS25]),
then $\{\kappa_n^{\mathrm{Heeg}}\}\ne0$. Under $p>3$, **(sur)**, the integral anticyclotomic main
conjecture and a $p$-optimal parametrisation, $M_\infty=\sum_{\ell\mid N}\operatorname{ord}_p(c_\ell)$ (W. Zhang's
refined conjecture); in rank one this gives the $p$-part of BSD for $E/K$. Analogues hold for the
Kolyvagin system derived from Kato's Euler system.

`[THEOREM]` (Castella–Sano [CS26], Jan 2026, preprint) Extends [BCGS26] to primes $p$ inert in $K$
(Kolyvagin) and to primes of any reduction type (Kurihara's refined conjectures), via determinants of Selmer complexes.

`[THEOREM]` (Kim–Pollack [KiP25], preprint) Nonvanishing of Kato's Kolyvagin system and a refined
BSD-type formula for Bloch–Kato Selmer groups of newforms ($p\ge3$, large image) assuming the main
conjecture localised at the augmentation ideal; yields higher-weight $p$-converses and $p$-parity.

`[THEOREM]` (Longo–Pati–Vigni [LPV24]; Da Ronche [DR25]) Kolyvagin's conjecture for newforms of even
weight $k\ge4$ ($p>k+1$ ordinary, mild hypotheses), and at non-ordinary primes under a rank-one
hypothesis (preprints).

**Consequences (Perrin-Riou's Heegner point main conjecture).** `[THEOREM]` Howard [How04] proved one
divisibility; Burungale–Castella–Kim [BCK21] proved the full conjecture for $p>3$ good ordinary,
**(Heeg)**, **(disc)**, **(sur)**, Hypothesis $\spadesuit$ and $p$ non-anomalous; [CGLS22, Thm. C] for
Eisenstein $p$ with $\varphi|_{G_p}\ne1,\omega$ (with **(spl)**); [BCS25, Thm. 1.2.4] for $p>3$, **(irr)**
(in $\Lambda\otimes\mathbb{Q}_p$) and **(sur)** (integrally); Bertolini–Longo–Venerucci [BLV26] (Math. Ann. 395
(2026)) for good ordinary and supersingular $p$ under "mild arithmetic assumptions".

**Status.** Kolyvagin's conjecture is a theorem for $p$ odd good ordinary and split in $K$ under
the hypotheses above (which cover all but finitely many $p$ for a non-CM curve once a suitable $K$
is fixed). Open: $p=2$; supersingular $p$ in general (partial: [DR25]); additive $p$; and the
unconditional statement for *all* $(E,p,K)$.

---

## 6. Statistical results

### 6.1 Average Selmer sizes and ranks (all curves ordered by naive height)
`[THEOREM]` (Bhargava–Shankar [BS15a], [BS15b], [BS13a], [BS13b]) When elliptic curves over $\mathbb{Q}$ are
ordered by height, the average size of $\operatorname{Sel}_n(E)$ is $\sigma(n)$ for $n=2,3,4,5$: $3,4,7,6$.
Consequently $\limsup$ of the average rank is $\le0.885$; at least $4/5$ of curves have rank $0$ or
$1$ and at least $1/5$ have rank $0$ (the rank-0 statement uses the $p$-parity theorem of the
Dokchitsers); a positive proportion of $2$-Selmer elements do not lift to $4$-Selmer elements
(nontrivial $\operatorname{Sha}[2]$). Combining with Skinner–Urban, a positive proportion have analytic rank 0
and hence satisfy the BSD rank conjecture [BS15b].

`[THEOREM]` (Bhargava–Skinner [BSk14]) A positive proportion of $E/\mathbb{Q}$ (ordered by height) have
both algebraic and analytic rank one (via [Ski20, Thm. B]).

`[THEOREM]` (Bhargava–Skinner–Zhang [BSZ14], preprint) More than $66\%$ of all $E/\mathbb{Q}$, ordered by
height, satisfy the BSD **rank** conjecture $r_{\mathrm{alg}}=r_{\mathrm{an}}$ (via 5-Selmer averages,
$p$-parity, and the converse theorems of Skinner and W. Zhang). **Not** $100\%$, and not the full formula.

### 6.2 Quadratic twist families: Smith
`[THEOREM]` (Smith [Smi17], preprint 2017, never published as such; superseded by [Smi25a],[Smi25b])
Let $E/\mathbb{Q}$ have full rational $2$-torsion and no rational cyclic subgroup of order $4$. Then the
$2^k$-Selmer ranks of the twists $E^{(d)}$, $|d|\le N$, follow the Markov chain predicted by
Delaunay/Poonen–Rains (transition probabilities $P^{\mathrm{Alt}}(j\mid n)$), and
$\#\{|d|\le N:\operatorname{corank}\operatorname{Sel}_{2^\infty}(E^{(d)})\ge2\}=o(N)$; in particular the set of congruent numbers
$\equiv1,2,3\pmod8$ has density zero. Corollary [Smi17, Cor. 1.3]: BSD for all twists $\Rightarrow$ Goldfeld's conjecture for $E$.

`[THEOREM]` (Smith [Smi25a, Thm. 1.2, 1.5], [Smi25b]; J. Amer. Math. Soc. 39 (2025) 1–72, 453–514)
Let $A/\mathbb{Q}$ satisfy Assumption 1.1: (1) $A(\mathbb{Q})[2]=0$; or (2) $A(\mathbb{Q})[2]\simeq\mathbb{Z}/2$ and, for the
$2$-isogeny $\varphi:A\to A_0$, $\mathbb{Q}(A_0[2])\ne\mathbb{Q}$ and $\mathbb{Q}(A_0[2])\ne\mathbb{Q}(A[2])$; or (3)
$A(\mathbb{Q})[2]\simeq(\mathbb{Z}/2)^2$ and no rational cyclic $4$-isogeny. Then the proportion of $d$ with
$r_{2^\infty}(A^{(d)})=0$ (resp. $1$, resp. $\ge2$) is $1/2$ (resp. $1/2$, resp. $0$); the
$\ge2$ proportion is $\le\exp(-c(\log\log\log H)^{1/2})$. Also: the average rank in the quadratic
twist family of any abelian variety over a number field is bounded [Smi25b].

`[THEOREM]` (Smith [Smi25c], preprint March 2025) For **every** $E/\mathbb{Q}$, $50\%$ of quadratic twists have
$2^\infty$-Selmer corank $0$ and $50\%$ have corank $1$. Consequently **BSD implies Goldfeld's
conjecture** for every $E/\mathbb{Q}$. The $2$-Selmer distribution in the remaining cases differs from the
Poonen–Rains model. (Pan–Tian [PT25] independently describe $2$-Selmer distributions for full
$2$-torsion twist families with "holes".)

**Warning.** Smith's theorems are about $2^\infty$-**Selmer** coranks (hence about $r_{\mathrm{alg}}\le1$
for $100\%$ of twists). They say nothing about analytic ranks unless a $2$-converse theorem is
available. This is why Goldfeld's conjecture is *not* a theorem in general (see §14).

### 6.3 Analytic-rank statements in twist families
- `[THEOREM]` (Kriz–Li [KL19]) If $E/\mathbb{Q}$ has a rational $3$-isogeny, Goldfeld's conjecture holds
  in the weak form: a positive proportion of quadratic twists have analytic rank $0$ and a positive
  proportion have analytic rank $1$ (via $3$-adic congruences of Heegner point logarithms); likewise
  for sextic twists of $j=0$ curves, with the $3$-part of BSD for those twists. For general $E$ the
  number of twists up to $X$ of analytic rank $0$ (resp. $1$) is $\gg X/\log^{5/6}X$. [KL16] (preprint)
  proves the $2$-part of BSD for many rank-0 and rank-1 twists.
- `[THEOREM]` (Tian [Tia14]; Tian–Yuan–Zhang [TYZ17]; Smith [Smi16]) For the congruent number curves
  $E^{(n)}:ny^2=x^3-x$: $E^{(n)}$ satisfies the full BSD conjecture for at least $41.9\%$ of positive
  squarefree $n\equiv1,2,3\pmod8$, and the rank BSD conjecture (with $r_{\mathrm{an}}=1$) for at least $55.9\%$
  of positive squarefree $n\equiv5,6,7\pmod8$; in particular at least $55.9\%$ of the latter are congruent numbers.
  (Survey of this circle of results: [BT22].)
- `[THEOREM]` (Burungale–Tian [BT25, Thm. 1.2], preprint) For a density-one subset of positive squarefree
  $n\equiv1,2,3\pmod8$, $\operatorname{ord}_{s=1}L(E^{(n)},s)=0$: the **even-parity Goldfeld conjecture for
  $y^2=x^3-x$** (Smith's $2^\infty$-Selmer distribution + the rank-0 $2$-converse for CM curves).
  Also [BT25, Prop. 1.3]: for $E/K$ CM over an imaginary quadratic $K$ with $3$ not inert, at least
  $50\%$ of $t\in K^\times/K^{\times2}$ have $\operatorname{ord}_{s=1}L(E^{(t)}/K,s)=0$.
- `[CONDITIONAL]` The odd-parity half ($100\%$ of $n\equiv5,6,7\pmod8$ have $r_{\mathrm{an}}=1$, hence are
  congruent) would follow from Smith plus a rank-1 $2$-converse for $E^{(n)}$ at the ramified prime
  $2$; this is exactly the claim of the unpublished [Kri20]. Unconditionally one has $55.9\%$ [Smi16].
- `[THEOREM]` (Bhargava–Klagsbrun–Lemke Oliver–Shnidman [BKLOS19]) For $E$ with a rational $3$-isogeny
  over a number field, the average size of the $3$-isogeny Selmer group in quadratic twist families
  is computed; a positive proportion of twists have rank $0$, and (with [CGLS22, Thm. E] at $p=3$)
  analytic rank statements follow, see [CGLS22, Cor. 5.2.3].
- `[THEOREM]` (Alpöge–Bhargava–Shnidman [ABS24], preprint v3 Oct 2024) In any cubic twist family
  $x^3+y^3=nz^3$ (curves with CM by $\mathbb{Z}[\zeta_3]$), the average size of $\operatorname{Sel}_2$ is $3$, also
  when restricted to either root number; hence at least $1/6$ of the twists have rank $0$ and at
  least $1/6$ of those with good reduction at $2$ have rank $1$ (using $p$-parity and the
  $2$-converse of the Burungale–Skinner appendix); a positive proportion of integers are (resp. are
  not) sums of two rational cubes. Koymans–Smith [KS24] obtain the $3$-Selmer distribution in the
  same family and improve the upper bound.

### 6.4 Rank results over number fields via Selmer groups
`[THEOREM]` (Koymans–Pagano [KoP24], [KoP25]) For every number field $K$ there are infinitely many
$E/K$ with $\operatorname{rank}E(K)=1$; and for suitable quadratic $L/K$ there are $E$ with full rational
$2$-torsion and no rank growth in $L/K$, which (via Poonen's criterion) gives a negative answer to
Hilbert's tenth problem over every ring of integers (independently Alpöge–Bhargava–Ho–Shnidman
[ABHS25], Invent. Math. 243 (2025), via rank stability of abelian varieties in quadratic extensions).
These are *algebraic-rank* results proved with $2$-descent and additive combinatorics; they use no $L$-functions.

### 6.5 Consequences for BSD
- `[THEOREM]` A positive proportion (indeed $>66\%$) of $E/\mathbb{Q}$ satisfy the rank conjecture [BSZ14].
- `[THEOREM]` For any $E/\mathbb{Q}$, $100\%$ of quadratic twists have $r_{\mathrm{alg}}\le1$ [Smi25c]; BSD for
  the family $\iff$ (given Smith) Goldfeld's conjecture for the family.
- `[THEOREM]` First infinite families of non-CM curves with the **full** BSD formula: [BSTW24, Thm. 1.7]:
  for $E$ one of $16$ listed curves (46a1, 62a1, 66b1, 69a1, 77c1, 94a1, 105a1, 106d1, 114b1, 115a1,
  118c1, 118d1, 141b1, 141c1, 141e1, 142c1) and squarefree $M>1$ coprime to $N$ with $L(E_M,1)\ne0$ and
  $E$ ordinary at all primes dividing $M$, the twist $E_M$ satisfies the full BSD conjecture;
  infinitely many such $M$ exist. Banwait–Huang [BH26] algorithmically identify all $E$ of
  conductor $\le500{,}000$ in the LMFDB to which the [BSTW24] criterion applies.
- `[THEOREM]` (CM families with the full formula, including $p=2$) Coates–Li–Tian–Zhai [CLTZ15],
  Li–Liu–Tian [LLT16], Zhai [Zha25], Gunri–Jha–Majumdar [GJM26] (Mordell curves $x^3+y^3=2p$, $2p^2$
  for $p\equiv4,7\pmod9$ under a cubic-residue condition; uses a result of Burungale–Flach at $p=2$).

### 6.6 Heuristics (not theorems)
`[HEURISTIC]` Goldfeld's conjecture [Gol79] ($50\%/50\%/0\%$ analytic ranks in quadratic twist
families), the Katz–Sarnak minimalist philosophy, Delaunay's and Poonen–Rains' models for Sha and
Selmer groups, and Park–Poonen–Voight–Wood's bounded-rank heuristic are heuristics; Smith's
theorems confirm the Selmer-side predictions but not the analytic ones.

---

## 7. Parity

`[CONJECTURE]` (Parity) $(-1)^{r_{\mathrm{alg}}}=w(E/K)$. `[CONJECTURE]` ($p$-parity)
$(-1)^{\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/K)}=w(E/K)$. They are equivalent for a given $p$ iff
$\operatorname{Sha}(E/K)[p^\infty]$ is finite. (Over $\mathbb{Q}$, $w(E)=(-1)^{r_{\mathrm{an}}}$ by modularity, so parity
is the "BSD mod 2" statement.)

- `[THEOREM]` (Monsky [Mon96]) $2$-parity for all $E/\mathbb{Q}$.
- `[THEOREM]` (Nekovář [Nek06, §0.17], [Nek07], [Nek09]) $p$-parity for $E/\mathbb{Q}$ at odd primes $p$ of
  ordinary type, as summarised in [Čes16, §1] ("known if $K=\mathbb{Q}$ thanks to Nekovář, Kim, and the
  Dokchitsers"); and, for a "large class" of $E$ over totally real fields $F$ and $p\ne2$, $p$-parity
  via potential modularity (Wintenberger's appendix to [Nek09]); the excluded cases are certain
  potentially-CM situations (cf. [Čes16, Rem. 1.7]: for $E/F$ with CM defined over an extension,
  [Nek09, Thm. A] covers $2\nmid[F:\mathbb{Q}]$ or $p$ split in the CM field).
- `[THEOREM]` (B. D. Kim [Kim07]) $p$-parity for $E/\mathbb{Q}$ at supersingular $p$.
- `[THEOREM]` (Dokchitser–Dokchitser [DD10, Thm. 1.4]) The $p$-parity conjecture holds for **all**
  $E/\mathbb{Q}$ and **all** primes $p$. Hence: if $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ is finite for **one** $p$,
  then $(-1)^{r_{\mathrm{alg}}}=w(E)$, i.e. $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod2$.
- `[THEOREM]` (Dokchitser–Dokchitser [DD11, Thm. 1.2]) For $E$ over a number field $K$: if
  $\operatorname{Sha}(E/K(E[2]))$ has finite $2$- and $3$-primary parts, then $(-1)^{\operatorname{rank}E(K)}=w(E/K)$.
  [DD10, Thm. 1.3]: assuming the Shafarevich–Tate conjecture, parity holds over all number fields
  for $E$ semistable at $v\mid6$ and not supersingular at $v\mid2$. [DD11, Cor. 1.6]: $2$-parity in
  quadratic extensions $F/K$ for every $E/K$ (Kramer–Tunnell conjecture in characteristic 0).
- `[THEOREM]` (Dokchitser–Dokchitser [DD09]) $p$-parity for twists of $E/\mathbb{Q}$ by orthogonal Artin
  representations of $\operatorname{Gal}(K^\infty/\mathbb{Q})$, $K/\mathbb{Q}$ abelian and $K^\infty$ its maximal pro-$p$
  extension, when $E$ is semistable at $2$ and $3$ (via "regulator constants").
- `[THEOREM]` (Česnavičius [Čes16, Thm. 1.4, 1.6]) $p$-parity holds for $E/K$ ($K$ any number field)
  whenever $E$ has a $p$-isogeny over $K$ (or acquires one over an odd-degree Galois extension);
  hence for every $E$ with CM defined over $K$, $p$-parity holds for all $p$ (and $\operatorname{rank}E(K)$ is even,
  $w(E/K)=1$). Earlier: [DD08, Thm. 2], [DD11, Cor. 5.8] for $p\le3$ or $E$ semistable above $p$
  (as cited in [Čes16, Thm. 1.3]).
- `[THEOREM]` (Green–Maistret [GM22]) $2$-parity for elliptic curves with isomorphic $2$-torsion
  (Proc. R. Soc. A 478 (2022)); (Dokchitser–Maistret [DM23]) parity for semistable principally
  polarised abelian surfaces assuming finiteness of Sha (Jacobians: good ordinary reduction at $2$-adic
  places); (Dokchitser–Green–Konstantinou–Morgan [DGKM25]) a new proof of the parity conjecture for
  elliptic curves (conditional on Sha) via Brauer relations; (V. Dokchitser [Dok24]) parity over all
  number fields for semistable p.p. abelian varieties over $\mathbb{Q}$ follows from parity over $\mathbb{Q}$ and
  quadratic fields (assuming Sha finite).

**Correct status.** Over $\mathbb{Q}$: $p$-parity is a theorem for all $(E,p)$; the parity conjecture for
$r_{\mathrm{alg}}$ is `[CONDITIONAL]` on the finiteness of $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ for some $p$ (unconditional
when $r_{\mathrm{an}}\le1$ by §1.3, where it is trivial). Over general number fields even $p$-parity is not
known in all cases (e.g. potentially supersingular situations outside the isogeny case).

---

## 8. Totally real and general number fields

**Modularity.** `[THEOREM]` Elliptic curves over real quadratic fields [FLHS15], totally real cubic
fields [DNS20], and totally real quartic fields not containing $\sqrt5$ [Box22] are modular. For
general totally real $F$, $E/F$ is potentially modular (Taylor; Wintenberger's appendix to [Nek09]),
so $L(E/F,s)$ has meromorphic continuation and functional equation; analytic continuation and
modularity in general are open. Over imaginary quadratic fields, modularity is known under
hypotheses (Caraiani–Newton [CN23, preprint]; Allen–Khare–Thorne) — `[unverified]` exact conditions.

**Gross–Zagier–Kolyvagin over totally real $F$.**
- `[THEOREM]` (Kolyvagin–Logachev [KL92]; S. Zhang [Zha01a], [Zha01b]; Nekovář [Nek07b], [Nek12]; Longo
  [Lon06]) Let $F$ be totally real, $E/F$ modular (attached to a Hilbert newform of parallel weight
  $2$), $K/F$ a CM quadratic extension with the Shimura-curve Heegner hypothesis (sign $-1$). If the
  CM point $P_K\in E(K)$ is non-torsion (equivalently $L'(E/K,1)\ne0$, by [Zha01a], [YZZ13]), then
  $\operatorname{rank}E(K)=1$ and $\operatorname{Sha}(E/K)$ is finite. Consequently, for modular $E/F$ with
  $\operatorname{ord}_{s=1}L(E/F,s)\le1$ one gets $\operatorname{rank}E(F)=\operatorname{ord}_{s=1}L(E/F,s)$ and $\operatorname{Sha}(E/F)$ finite
  **provided** a suitable $K$ exists with the required nonvanishing of the twisted $L$-value (the
  nonvanishing theorems of §1.3 have analogues over $F$ in the cases treated in these papers; Longo
  treats rank 0 when $[F:\mathbb{Q}]$ is even and the form is not new at any prime, a case excluded by
  [KL92]). The exact local hypotheses (on the level, on $K/F$, on $p$ for the $p$-primary bounds)
  differ between the cited papers and are **not reproduced here**; they must be read off from the
  source before use.
- `[THEOREM]` (Wan [Wan15]) One divisibility of the cyclotomic main conjecture for Hilbert modular
  forms (ordinary, under hypotheses); (Loeffler–Zerbes [LZ25a], v2 Feb 2025) for **quadratic** Hilbert
  modular forms the full cyclotomic main conjecture "under certain technical hypotheses" (Kato-type
  divisibility from an Euler system on Siegel threefolds, opposite divisibility from Wan), giving
  the equivariant BSD conjecture in analytic rank $0$ for elliptic curves over real quadratic fields
  twisted by Dirichlet characters, and finiteness of $\operatorname{Sha}[p^\infty]$ for all but finitely many
  ordinary $p$ for $E/\mathbb{Q}$ twisted by $2$-dimensional odd Artin representations.
- `[THEOREM]` (Castella [Cas24b]) $p$-part of BSD in analytic rank $1$ for CM elliptic curves (and CM
  abelian varieties) over number fields $F$, $p>3$ split in the CM field (abstract-level statement).
- `[THEOREM]` (Disegni [Dis20]) results toward the $p$-adic BSD conjecture over number fields;
  [Dis17], [Dis22] $p$-adic Gross–Zagier on Shimura curves.
- `[CONDITIONAL]` (H. Li [Li26], Aug 2026, preprint) a $p$-part BSD formula (with the congruence period)
  over CM quadratic extensions of totally real fields in analytic rank one, **assuming** the Iwasawa
  main conjecture and "a substantial number of assumptions".
- `[THEOREM]` (Mastella–Matar–Zerman [MMZ26], Aug 2026, preprint) Kolyvagin's vanishing of
  $\operatorname{Sha}[\mathfrak P^\infty]$ generalised to $\mathrm{GL}_2$-type abelian varieties over totally real $F$ and CM $K/F$.

**Imaginary quadratic fields.** `[THEOREM]` (Loeffler–Zerbes [LZ23, Thm. A]) For $E$ over an imaginary
quadratic field $K$ which is modular and not a $\mathbb{Q}$-curve, with $A=\operatorname{Res}_{K/\mathbb{Q}}E$ satisfying
hypotheses (1),(3)–(7) of §11 (in particular $L(E/K,1)\ne0$, an odd Dirichlet character $\chi^-$ with
$L(A,\chi^-,1)\ne0$, $p$ good ordinary with big image and "deformable"): $E(K)$ and $\operatorname{Sha}(E/K)[p^\infty]$ are finite.

---

## 9. Computational verifications of strong BSD

`[THEOREM]` (Grigorov–Jorza–Patrikis–Stein–Tarniţă [GJPST09]) For every non-CM $E/\mathbb{Q}$ with $N\le1000$
and $r_{\mathrm{an}}\le1$, the full BSD formula holds up to odd primes dividing a Tamagawa number or the
degree of a rational cyclic isogeny — **as originally stated**. [LW16, §5] and [MN19, (0.10)] point
out that the cohomological lemmas of [GJPST09, §5] are incorrect (Lemma 5.4 in the numbering used by
[LW16]; Lemmas 5.7, 5.9 and the proof of Prop. 5.4 in the numbering used by [MN19]), so that the
Kolyvagin-type bound [GJPST09, Thm. 3.5] (= Thm. 3.7 in [MN19]'s numbering) is unproved as stated;
[LW16, Thm. 14] is the corrected bound (requiring $p$ odd, $p$ unramified in the Heegner field, that
$(E,p)$ is not in the finite list of [LW16, Thm. 1] of pairs with $H^1(\mathbb{Q}(E[p])/\mathbb{Q},E[p])\ne0$, and
that $E$ is not isogenous to a curve whose dual isogeny contains a rational $p$-torsion point).

`[THEOREM]` (Miller [Mil11]; Miller–Stoll [MS13]; Creutz–Miller [CM12]; Lawson–Wuthrich [LW16, §5])
The full BSD conjecture (rank part and leading term, all primes $p$) holds for **every** $E/\mathbb{Q}$ of
conductor $N<5000$ and $r_{\mathrm{an}}\le1$. Miller proved it for $16714$ of the $16725$ such curves, using
Kolyvagin/Kato/Skinner–Urban bounds on the support of Sha and explicit $p$-descents; Miller–Stoll
(explicit isogeny descent) and Creutz–Miller (second isogeny descents for $p=5,7$) completed the
list; Lawson–Wuthrich re-verified the finitely many curves affected by the [GJPST09] error (a $5$-descent
for 42 listed curves; $p=3$ cases already covered by [MS13, Thm. 9.1]; 121c2 separately). This is the
summary given in [KS25, §1.3]. Method: Kolyvagin (or Kato) bounds the *support* of Sha to an
explicit finite set $S$ of primes; for $p\in S$, either Iwasawa theory ([SW13], using Kato's
divisibility and $p$-adic $L$-functions) or descent computes $\#\operatorname{Sha}[p^\infty]$; the analytic
side is computed exactly (rank 0: $L(E,1)/\Omega_E\in\mathbb{Q}$ via modular symbols; rank 1: Gross–Zagier
with a Heegner point of provably computed height).

`[THEOREM]` (Stein–Wuthrich [SW13]) $\operatorname{Sha}(E/\mathbb{Q})[p]=0$ for the $1{,}534{,}422$ pairs $(E,p)$ with $E$
non-CM, $N\le30{,}000$, $r_{\mathrm{alg}}\ge2$, $p$ good ordinary, $5\le p<1000$, **(sur)** — via Iwasawa theory
(Kato's divisibility + computation of the $p$-adic $L$-function), the only method that applies in rank $\ge2$.

`[THEOREM]` (Keller–Stoll [KS22], [KS25]) Strong BSD holds, unconditionally and exactly, for the
Jacobians $J/\mathbb{Q}$ of all $28$ Atkin–Lehner quotients of $X_0(N)$ of genus $2$ with absolutely simple
Jacobian ([KS22], C. R. Math. 360 (2022)), and for all $97$ genus-$2$ curves in the LMFDB whose
Jacobian is absolutely simple and modular (of $\mathrm{GL}_2$-type), plus six further curves of Wang
([KS25], Forum Math. Sigma 13 (2025)); $L$-ranks $0$ and $1$ occur; in one example
$\#\operatorname{Sha}(J/\mathbb{Q})=7^2$ is verified to agree with the BSD prediction. These are the first
absolutely simple abelian varieties of dimension $\ge2$ with strong BSD proved. Ingredients: exact
computation of $\#\operatorname{Sha}_{\mathrm{an}}$ (via Gross–Zagier on Shimura/modular curves and Petersson
norms), determination of images of residual representations, Heegner indices, support bounds for
Sha, isogeny descents, and $p$-adic $L$-functions.

`[THEOREM]` (Banwait–Huang [BH26], 2026, preprint) Algorithmic identification of all $E$ with
$N\le500{,}000$ in the LMFDB admitting infinitely many quadratic twists satisfying strong BSD via [BSTW24, Thm. 1.7].

**What computations do not give.** No curve of analytic rank $\ge2$ has strong BSD (or even
finiteness of $\operatorname{Sha}(E/\mathbb{Q})$) established; for such curves one can only prove $\operatorname{Sha}[p^\infty]$
finite (or trivial) for individual $p$ under $p$-adic hypotheses [SW13], and the analytic order of
Sha can only be computed numerically (LMFDB "analytic Sha"). Numerical agreement is `[HEURISTIC]`
evidence, not proof (charter rule 6).

---

## 10. Function fields (one paragraph; full treatment in `approaches/D-function-field-analogy.md`)

`[THEOREM]` (Tate [Tat66]; Milne [Mil75]; Schneider [Sch82]; Bauer [Bau92]; Kato–Trihan [KT03]) Let
$A$ be an abelian variety over a global function field $K$ of characteristic $p$. Then the BSD
conjecture for $A/K$ (rank and leading term, including the $p$-part) holds **if and only if**
$\operatorname{Sha}(A/K)[\ell^\infty]$ is finite for some prime $\ell$ ($\ell=p$ allowed, by [KT03]; the case
$\ell\ne p$ and the rank statement go back to [Tat66], [Sch82], the $p$-part of the leading term to
[Mil75], [Bau92] in the good-reduction case); for a Jacobian $A$ this is equivalent to the Artin–Tate
conjecture for a regular model surface (Artin–Tate's "Conjecture (d)", settled by [KT03] together
with [Mil75]). `[THEOREM]` (Ulmer [Ulm02]) There are non-isotrivial elliptic curves over
$\mathbb{F}_p(t)$ of arbitrarily large rank for which BSD holds (Tate conjecture known for the relevant
surfaces, dominated by Fermat surfaces). `[THEOREM]` (Yun–Zhang [YZ17], [YZ19]) For an unramified
(resp. Iwahori-level) cuspidal automorphic representation $\pi$ of $\mathrm{PGL}_2$ over the function
field of a curve over $\mathbb{F}_q$ and every $r\ge0$, the $r$-th central derivative $L^{(r)}(\pi,1/2)$ is
expressed as the self-intersection of a Heegner–Drinfeld cycle on the moduli of Shtukas with $r$
legs — a "higher Gross–Zagier formula" for all orders of vanishing, with no counterpart over number
fields. `[THEOREM]` (Tan [Tan26]; Tan–Trihan–Tsoi [TTT26a], [TTT26b], 2026 preprints) $p$-adic
$L$-functions and the Iwasawa main conjecture for ordinary semistable elliptic curves over global
function fields along $\mathbb{Z}_p^d$-extensions, subject to a $\mu$-invariant hypothesis shown to hold on a
Zariski-dense locus for $p>3$; [KTTT24] a BSD-type formula for Hasse–Weil–Artin $L$-functions in
characteristic $p$.

---

## 11. Higher-dimensional analogues relevant to method

- `[THEOREM]` (Loeffler–Skinner–Zerbes [LSZ22], J. Eur. Math. Soc. 24 (2022)) Construction of an Euler
  system for the $4$-dimensional spin Galois representations of cohomological cuspidal automorphic
  representations of $\mathrm{GSp}_4$, from pushforwards of $\mathrm{GL}_2\times\mathrm{GL}_2$ Eisenstein classes.
  [LZ26a] (Forum Math.) shows the classes are explicit multiples of a "universal" class.
- `[THEOREM]` (Loeffler–Zerbes [LZ26b], Camb. J. Math. 14 (2026) 603–784) Explicit reciprocity law for
  the $\mathrm{GSp}_4$ Euler system; one inclusion of the Iwasawa main conjecture for spin motives of
  genus-$2$ Siegel modular forms; Bloch–Kato in analytic rank $0$ for their critical twists.
  Strengthened in [LZ23, Thm. B] to globally generic $\pi$ with $\pi_p$ unramified Borel-ordinary,
  "deformable", big image, and (if $r_1=r_2$) an odd $\chi$ with $L(\Pi\times\chi,1/2)\ne0$.
- `[THEOREM]` (Loeffler–Zerbes [LZ23, Thm. A], preprint v3 2023) Let $A/\mathbb{Q}$ be an abelian surface with
  (1) $L(A,1)\ne0$; (2) $\operatorname{End}_{\bar{\mathbb{Q}}}A=\mathbb{Z}$, or $A=\operatorname{Res}_{K/\mathbb{Q}}E$ for $E$ over an imaginary
  quadratic $K$, modular, not a $\mathbb{Q}$-curve; (3) $A$ modular (attached to a cuspidal automorphic
  representation of $\mathrm{GSp}_4$); (4) an odd Dirichlet character $\chi^-$ with $L(A,\chi^-,1)\ne0$;
  and a prime $p$ with (5) good ordinary reduction, (6) big image of $V_p(A)(\chi)$ for all $\chi$
  in the sense of Mazur–Rubin, (7) the automorphic representation "deformable" at $p$ (smoothness of
  the eigenvariety). Then $A(\mathbb{Q})$ and $\operatorname{Sha}(A/\mathbb{Q})[p^\infty]$ are finite. Modularity of
  generic abelian surfaces is known only potentially [BCGP21]; hypothesis (3) is therefore a genuine restriction.
- `[THEOREM]` (Loeffler–Zerbes [LZ25b], Nov 2025, preprint) "Ultra-Kolyvagin systems": a Selmer-bounding
  machine in non-ordinary settings using Pottharst's $(\varphi,\Gamma)$-module Selmer groups and Sweeting's
  ultrafilter interpretation of Kolyvagin derivatives; new cases of the cyclotomic main conjecture for
  non-ordinary Rankin–Selberg convolutions.
- `[THEOREM]` (Sweeting [Swe25], preprint) For $\pi$ on $\mathrm{GSp}_4(\mathbb{A}_\mathbb{Q})$ with trivial central character
  and lowest cohomological weight, under mild conditions, $L(\pi,\mathrm{spin},1/2)\ne0\Rightarrow$ the Bloch–Kato
  Selmer group vanishes (bipartite Euler systems / level raising); a partial rank-one result via Kudla cycles.
- `[THEOREM]` (Liu–Tian–Xiao [LTX24]) One-sided divisibilities in the anticyclotomic Iwasawa main
  conjecture for Rankin–Selberg motives of $\mathrm{GL}_n\times\mathrm{GL}_{n+1}$ over CM fields (both root
  numbers); (Disegni–W. Zhang [DZ26]) $p$-adic arithmetic Gan–Gross–Prasad: first derivative of a
  cyclotomic $p$-adic $L$-function equals $p$-adic heights of arithmetic diagonal cycles.
- `[THEOREM]` (Kings–Loeffler–Zerbes; Loeffler–Zerbes [LZ25a]) Rankin–Selberg Euler systems
  (Beilinson–Flach) give finiteness of $\operatorname{Sha}[p^\infty]$ for $E/\mathbb{Q}$ twisted by $2$-dimensional odd
  Artin representations in analytic rank $0$, for all but finitely many ordinary $p$.

**Methodological upshot for rank $\ge2$.** All Euler-system methods above prove *upper* bounds on
Selmer groups from nonvanishing of an $L$-value (rank 0) or of a derivative/derived class (rank 1).
None produces a lower bound on $r_{\mathrm{alg}}$ or a finiteness statement for $\operatorname{Sha}$ when the
$L$-function vanishes to order $\ge2$; see `03-obstructions-rank-ge-2.md`. The only partial rank-$2$
statements are $p$-adic/conditional: Castella–Hsieh [CH22] and Castella [Cas23], [Cas26]:
for $p>3$ good ordinary (non-CM: [CH22],[Cas23]; CM: $p\ge5$ [Cas26]) and $L(E,s)$ vanishing at
$s=1$ with sign $+1$, Darmon–Rotger's generalised Kato class $\kappa_p\in\operatorname{Sel}(\mathbb{Q},V_pE)$ satisfies
$\kappa_p\ne0\Rightarrow\dim\operatorname{Sel}(\mathbb{Q},V_pE)=2$, and when $\dim=2$, $\kappa_p\ne0$ iff
$\operatorname{loc}_p:\operatorname{Sel}(\mathbb{Q},V_pE)\to E(\mathbb{Q}_p)\hat\otimes\mathbb{Q}_p$ is nonzero. No unconditional statement of
the form "$r_{\mathrm{an}}=2\Rightarrow r_{\mathrm{alg}}=2$" exists.

---

## 12. Summary table (elliptic curves over $\mathbb{Q}$)

| | rank statement | finiteness of $\operatorname{Sha}(E/\mathbb{Q})$ | $p$-part of leading term | full leading term |
|---|---|---|---|---|
| $r_{\mathrm{an}}=0$ | **THEOREM** for all $E$: $r_{\mathrm{alg}}=0$ (Kolyvagin [Kol88]+GZ+[BFH90],[MM91]; Kato [Kat04]). Converse "$\operatorname{Sel}_{p^\infty}$ finite $\Rightarrow L(E,1)\ne0$": odd good ord. $p$, (irr)+(ram) [SU14]; $p>3$ good ord. non-CM (irr)+(im) [BCS25]; semistable, ss $p>2$ [BSTW24]; Eisenstein $p>2$, $\varphi\vert_{G_p}\ne1,\omega$ [CGLS22]; CM, all $p$ [BT25]. | **THEOREM** for all $E$ (Kolyvagin; Kato). | **THEOREM** for: $p$ odd, good ord. or mult., (irr)+(ram) [SU14],[Ski16],[JSW17 7.2.1]; $p>3$ good ord. non-CM, (irr)+(im) [BCS25]; semistable, ss $p>2$ ($a_3=0$) [BSTW24]; good Eisenstein $p>2$, $\varphi\vert_{G_p}\ne1,\omega$ [CGS25] (+[KY24a]); CM, $p\nmid\#\mathcal O_K^\times$ [Rub91]. **Open:** $p=2$ (non-CM and CM); $p=3$ for CM by $\mathbb{Q}(\sqrt{-3})$; additive $p$; residually dihedral $p$ w/o (ram); many $p=3$ ordinary cases. | **THEOREM** only for: all $E$ with $N<5000$ [Mil11],[CM12],[LW16]; explicit infinite twist families [BSTW24 Thm 1.7]; explicit CM families [CLTZ15],[Zha25],[GJM26]. **Open** in general (missing: finitely many "bad" $p$ per curve, in particular $p=2$). |
| $r_{\mathrm{an}}=1$ | **THEOREM** for all $E$: $r_{\mathrm{alg}}=1$ (GZK, §1.3). Converse "$\operatorname{corank}\operatorname{Sel}_{p^\infty}=1\Rightarrow r_{\mathrm{an}}=1$": [Ski20] ($p\ge5$ good ord., semistable + local conditions), [Zha14] ($p\ge5$, (sur), Hyp. $\spadesuit$), [BSTW24 1.10] (ord. $p\nmid2N$, (sur)+(ram)), [BCS25] ($p>3$, (irr)+(im)), [Cas24a] (mult. $p>3$), [CGLS22] (Eisenstein), CM: [BT20],[BCST22] (all good ord. $p$), [BKO23] (ss $p\ge5$), [ABS24 App.] (ss, incl. $p=2$, with a localisation condition). | **THEOREM** for all $E$ (Kolyvagin). | **THEOREM** for: semistable, $p\ge5$ good, (irr) [JSW17] ($p=3$ if $a_3=0$ when ss); semistable, mult. $p>3$, (irr) [Cas18]; any $N$, ord. $p\nmid 2N$, (irr)+(ram) [BSTW24 1.9]; $p>3$ good ord. non-CM (irr)+(im) [BCS25]; semistable ss $p>2$ [BSTW24 1.5]; Eisenstein $p>2$ with [CGLS22 F] conditions; CM: $p\nmid\#\mu_K$ pot. good ord. [LLT16], ss $p$ [Kob13 Cor 1.4]. **Open:** $p=2$; additive $p$; residually dihedral $p$ w/o (ram); CM at $p\mid\#\mathcal O_K^\times$. | **THEOREM** only for $N<5000$ and for explicit CM families (e.g. [Smi16]: $\ge55.9\%$ of $n\equiv5,6,7$ (8) congruent-number twists have $r_{\mathrm{an}}=1$ — rank BSD, not the formula; [KL16] $2$-part for many twists). **Open** in general. |
| $r_{\mathrm{an}}\ge2$ | **OPEN.** Known: $L(E,1)=0\Rightarrow\operatorname{corank}\operatorname{Sel}_{p^\infty}\ge1$ [SU14 2(b)] (odd good ord. $p$, (irr)+(ram)); $r_{\mathrm{an}}>1\Rightarrow\operatorname{corank}\operatorname{Sel}_{p^\infty}\ge2$ ($\ge3$ if $w=-1$) [Zha14 1.4(ii)] (hyp. of §3.3); $r_{\mathrm{alg}}\le\operatorname{ord}_{T=0}L_p(E,T)$ [Kat04 18.4]. For individual curves $r_{\mathrm{an}}\in\{2,3\}$ can be certified (parity + rigorous nonvanishing of $L^{(2)}$ or $L^{(3)}$) and $r_{\mathrm{alg}}$ by descent; no general theorem in either direction. | **OPEN**; not known for a single $E$ with $r_{\mathrm{an}}\ge2$. Only $\operatorname{Sha}[p^\infty]$ for individual $p$ via Iwasawa theory [SW13] under $p$-adic hypotheses. | **OPEN**; no result. ($p$-adic analogue: conjectural [MTT86], [PR93], [BPR93]; Castella [Cas25] proves a Kundu–Ray formula for leading terms of signed characteristic series at ss $p$.) | **OPEN**; no result. |

Reading the table: every entry marked THEOREM in the "$p$-part" column requires the listed
hypotheses on $(E,p)$; for a given curve the set of primes $p$ *not* covered is finite but nonempty
(always containing $p=2$ for non-CM curves), which is exactly why the "full leading term" column is
open in general.

---

## 13. 2024–2026 developments (live search, 2026-09-11)

Searches were run against the arXiv API (`export.arxiv.org/api/query`, `submittedDate` restricted to
2024-01-01 – 2026-09-12, math categories) for the phrases: "Birch and Swinnerton-Dyer" /
"Birch–Swinnerton-Dyer"; "Heegner"; "Kolyvagin"; "main conjecture" AND "elliptic curve";
"Iwasawa main conjecture" AND (supersingular OR non-ordinary); "Selmer group" AND rank AND
"elliptic curves" AND (distribution OR twist family); "Selmer" AND "rank two" AND "elliptic";
"converse theorem"/"p-converse" AND "Gross-Zagier"; "Perrin-Riou" AND conjecture; "Kato classes";
"diagonal cycles"/"diagonal classes"; "Tamagawa number conjecture" AND ("elliptic curve" OR
"modular form"); "Mazur-Tate"; "Goldfeld"; "parity conjecture"; "Shafarevich-Tate" AND finite AND
"elliptic curve". Author searches: Burungale, Castella, Skinner, Tian, Wan, Sweeting, Zanarella,
Keller, Stoll, Smith, Koymans, Pagano, Alpöge, Loeffler, Zerbes, Kriz, Dokchitser, Česnavičius,
Trihan. Crossref was used to confirm journal data. Web searches were used for publication status.

### 13.1 Results directly about BSD for elliptic curves over $\mathbb{Q}$
- **arXiv:2409.01350** Burungale–Skinner–Tian–Wan, *Zeta elements for elliptic curves and applications* (Sep 2024).
  Two-variable zeta element for $(E,L)$, $p\nmid2N$ split in $L$; Kobayashi's main conjecture for semistable
  $E$ at all supersingular $p>2$ ($a_3=0$ if $p=3$); $p$-part of BSD for $r_{\mathrm{an}}\le1$ and rank-0
  $p$-converse at such $p$; rank-1 $p$-part and $p$-converse at ordinary $p\nmid2N$ with (irr)/(sur)+(ram);
  Perrin-Riou's conjecture for all $p\nmid2N$; first infinite families of non-CM curves with full BSD. Supersedes [Wan14].
- **arXiv:2405.00270** Burungale–Castella–Skinner, *Base change and Iwasawa Main Conjectures for GL2* (IMRN 2025).
  Cyclotomic and anticyclotomic main conjectures for $p>3$ good ordinary with (irr) (integrally with (im)),
  **no (ram)**; $p$-part of BSD for $r_{\mathrm{an}}\le1$ without conductor conditions.
- **arXiv:2312.09301** Burungale–Castella–Grossi–Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory* (v2 Jan 2026).
  Kolyvagin's conjecture for $p$ odd good ordinary split in $K$ (incl. Eisenstein $p$); W. Zhang's refined
  conjecture $M_\infty=\sum\operatorname{ord}_p c_\ell$; Kato analogue.
- **arXiv:2303.04373** Castella–Grossi–Skinner, *Mazur's main conjecture at Eisenstein primes* (Math. Ann. 393 (2025) 2451–2506).
  Cyclotomic main conjecture at good Eisenstein $p>2$ with $\varphi|_{G_p}\ne1,\omega$.
- **arXiv:2409.01360** Castella, *Exceptional zeros for Heegner points and p-converse* (Sep 2024). Rank-1
  $p$-converse at multiplicative $p>3$ with (irr), a nonsplit ramified $q$, $E(\mathbb{Q}_p)[p]=0$.
- **arXiv:2506.03465** Burungale–Tian, *A rank zero p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin* (Jun 2025; v2 Oct 2025).
  For CM $E/K$ and **every** prime $p$: $\operatorname{corank}\operatorname{Sel}_{p^\infty}=0\Rightarrow L(E/K,1)\ne0$; even-parity
  Goldfeld for $y^2=x^3-x$.
- **arXiv:2503.17619** A. Smith, *The BSD conjecture implies Goldfeld's conjecture* (Mar 2025). For every $E/\mathbb{Q}$,
  $50\%$ of quadratic twists have $2^\infty$-Selmer corank $0$ and $50\%$ corank $1$.
- **arXiv:2207.05674, 2207.05143** A. Smith, *Distribution of $\ell^\infty$-Selmer groups in degree $\ell$ twist families I, II* — now published: JAMS 39 (2025) 1–72 and 453–514.
- **arXiv:2410.23241**, **arXiv:2402.12781** Keller–Yin: $p$-converses and $p$-part of BSD at Eisenstein primes
  without $\varphi|_{G_p}\ne1,\omega$, potentially good ordinary and multiplicative cases; applications to Goldfeld
  for $3$-isogeny families (abstract level).
- **arXiv:2412.20078** Yan–Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes* (J. Algebra 693 (2026) 372–402). More cases of main conjectures, $p$-converse and $p$-part BSD for $r\le1$ (abstract level).
- **arXiv:2306.17784** Bertolini–Longo–Venerucci, *The anticyclotomic main conjectures for elliptic curves* (Math. Ann. 395 (2026)). Anticyclotomic main conjectures for good ordinary and supersingular $p$ under mild hypotheses.
- **arXiv:2601.14504** Castella–Sano (Jan 2026): refined Kurihara/Kolyvagin nonvanishing conjectures, inert primes, all reduction types.
- **arXiv:2505.09121** Kim–Pollack (May 2025): refined Tamagawa number conjectures for $\mathrm{GL}_2$; nonvanishing of Kato's Kolyvagin system; higher-weight $p$-converse and $p$-parity (assuming the localised main conjecture).
- **arXiv:2511.07203** Bullach–Honnor (Nov 2025): "a substantial part" of the Mazur–Tate refined BSD conjectures via the rank-zero component of the equivariant Tamagawa number conjecture (abstract level).
- **arXiv:2502.19618** Castella (Feb 2025): a Kundu–Ray formula for the leading term of characteristic power series of Kobayashi's signed Selmer groups at supersingular $p>2$, $a_p=0$.
- **arXiv:2608.29470** Castella–Liu–Wan (Aug 2026): Kato's main conjecture for nonordinary modular forms (Fontaine–Laffaille weights).
- **arXiv:2412.02303**, **arXiv:2603.22483** Longo–Pati–Vigni: Kolyvagin's conjecture and anticyclotomic main conjectures for newforms of weight $\ge4$; **arXiv:2503.09955** Da Ronche: Kolyvagin's conjecture at non-ordinary primes (rank-one hypothesis).
- **arXiv:2601.16044** Banwait–Huang (Jan 2026): all $E$ with $N\le500{,}000$ admitting infinitely many twists with strong BSD via [BSTW24].
- **arXiv:2510.00926** Barrios–Mok (Oct 2025): BSD formula modulo squares transfers between $E$ and quadratic twists $E^D$ of analytic rank $\le1$ under a modified Heegner hypothesis (semistable case: unconditional equivalence).
- **arXiv:2607.26774** Gunri–Jha–Majumdar (Jul 2026): explicit mock Heegner points and full BSD for Mordell curves $x^3+y^3=2p,2p^2$ ($p\equiv4,7\pmod9$, $2$ not a cube mod $p$).
- **arXiv:2609.08431** Banwait (Sep 2026): a cyclotomic criterion for $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]=0$ for rank-two CM curves via the second Taylor coefficient of the MTT $p$-adic $L$-function.
- **arXiv:2603.14234** Deng–Li (Mar 2026): rank-one quadratic twists with infinite Sha over the cyclotomic $\mathbb{Z}_2$-extension (Mazur–Tate elements at $2$).
- **arXiv:2504.21799** Bansal–Jha–Pal–Venkat: $p$-converse over real quadratic fields (split multiplicative inert $p>5$).
- **arXiv:2608.11969** H. Li (Aug 2026): conditional $p$-part BSD over CM quadratic extensions of totally real fields.
- **arXiv:2603.20886** Burungale–Skinner–Wan (Mar 2026): refined nonvanishing of $p$-adic logarithms of rational points on abelian varieties ($p$-adic analytic subgroup theorem).
- **arXiv:2608.06879**, **arXiv:2508.17776** Burungale–Kobayashi–Nakamura–Ota: local sign decomposition and an integral anticyclotomic main conjecture for CM elliptic curves at primes **ramified** in the CM field (first main conjecture for a deformation with no trianguline geometric specialisation).
- **arXiv:2412.07308** Hatley–Ray: Iwasawa-theoretic lower bounds for rank-$1$ twists (with $\lambda_2=0$, assuming Sha$[2^\infty]$ finite).
- **arXiv:2503.21462** Pan–Tian: $2$-Selmer rank distribution in quadratic twist families with full $2$-torsion (random alternating matrices with "holes").
- **arXiv:2210.10730** (v3 Oct 2024) Alpöge–Bhargava–Shnidman with the Burungale–Skinner appendix ($p$-converse for CM curves at supersingular $p$ including $p=2$, under a localisation condition).
- **arXiv:2405.09311** Koymans–Smith: $3$-Selmer in cubic twist families; **arXiv:2606.31649** Koymans–Smith (Jun 2026): Tamagawa ratios and unbounded Selmer moments.
- **arXiv:2412.01768**, **arXiv:2505.16910** Koymans–Pagano; **arXiv:2501.18774** Alpöge–Bhargava–Ho–Shnidman (Invent. Math. 243 (2025)): rank-one curves over every number field / rank stability; Hilbert's tenth problem.
- **arXiv:2407.18260** V. Dokchitser: parity and base change; **arXiv:2211.06357** DGKM (PLMS 131 (2025)).
- **arXiv:2411.12404**, **arXiv:2603.10576**, **arXiv:2603.11615**, **arXiv:2608.26791** Tan, Trihan, Tsoi (and Kim): function-field BSD-type formulas, $p$-adic $L$-functions and Iwasawa main conjecture for ordinary semistable elliptic curves over global function fields; specialisations of the [BCS25] two-variable main conjecture to $\mathbb{Z}_p$-lines.
- **arXiv:2003.05960** Loeffler–Zerbes, Bloch–Kato for $\mathrm{GSp}_4$ — published Camb. J. Math. 14 (2026) 603–784; **arXiv:2511.08793** Loeffler–Zerbes ultra-Kolyvagin systems; **arXiv:2503.19226** Sweeting, Bloch–Kato for $\mathrm{GSp}_4$ via bipartite Euler systems; **arXiv:2406.00624** Liu–Tian–Xiao; **arXiv:2410.08401** Disegni–Zhang.
- **arXiv:2312.07307** Keller–Stoll — published Forum Math. Sigma 13 (2025); **arXiv:2608.29337** Mastella–Matar–Zerman.
- Expository: **arXiv:2404.12644** Castella (Eisenstein primes), **arXiv:2404.05186** C.-H. Kim (Beilinson–Kato zeta elements), **arXiv:2602.04468** Koymans–Pagano (Hilbert 10).

### 13.2 Searches that returned nothing new (2024–2026)
- "generalised Kato classes"/"Kato class(es)": no new arithmetic results beyond Castella's 2023 note
  [Cas23] and the Feb 2026 revision of [Cas26]; all other hits were PDE/probability papers.
- "diagonal cycles rank two"/"rank two elliptic curve Selmer": no unconditional rank-two results; the
  hits (Marannino, Alonso–Castella–Rivero, Alonso–Omil-Pazos–Rivero, Büyükboduk et al.) construct or
  interpolate diagonal-cycle Euler systems and reciprocity laws but prove no statement of the form
  $r_{\mathrm{an}}=2\Rightarrow r_{\mathrm{alg}}=2$ or finiteness of Sha.
- "Shafarevich-Tate" AND finite AND "elliptic curve": no new finiteness theorem for Sha beyond the
  $r_{\mathrm{an}}\le1$ setting.
- "Iwasawa main conjecture" AND supersingular: only [LZ25b] and Corpuz–Lei (congruences); the
  supersingular main conjecture for elliptic curves in 2024–26 is [BSTW24] (and [CLW26]).
- No 2024–2026 result on the $2$-part of BSD for general (non-CM) curves; no result on additive primes $p^2\mid N$
  for the $p$-part; no publication of [Kri20], [Swe20], [SZ14], [Spr16], [CCSS18] could be confirmed.
- Wei Zhang's Kolyvagin paper and Skinner's converse have no 2024–26 successors removing the
  residually-dihedral restriction other than [Swe20] (preprint) and, for $p>3$ with (irr), [BCS25]
  (which needs (im) for the integral statement).

---

## 14. Statements widely believed to be proved but which are not (or are only conditional)

1. **"Sha is finite for rank $\le1$ curves."** Correct statement: $\operatorname{Sha}(E/\mathbb{Q})$ is finite whenever
   the **analytic** rank is $\le1$ (§1.3). If only $r_{\mathrm{alg}}\le1$ is known, finiteness of Sha is not a
   theorem: a curve with $r_{\mathrm{alg}}=0$ could, as far as theorems go, have $r_{\mathrm{an}}\ge2$ and infinite Sha.
   What is known is the converse direction *with* finiteness as hypothesis: $r_{\mathrm{alg}}=r\le1$ and
   $\operatorname{Sha}[p^\infty]$ finite for a suitable $p$ (satisfying the hypotheses of a $p$-converse theorem,
   §4) $\Rightarrow r_{\mathrm{an}}=r$, and then Sha is finite. Unconditionally in $p$: [Ski20, Thm. A$'$],
   [Zha14, Thm. 1.5] under their conductor hypotheses.

2. **"Strong BSD is known for all rank $\le1$ curves."** False. Known (§2–3): the rank part, finiteness
   of Sha, and the $p$-part of the formula for all $p$ outside an explicit finite set depending on $E$.
   Always missing for non-CM curves: $p=2$; frequently missing: $p=3$, additive primes $p$ ($p^2\mid N$),
   residually dihedral primes when no multiplicative prime is ramified for $E[p]$, Eisenstein primes
   outside [CGLS22]/[CGS25]/[KY24a]. The full formula is a theorem only for individual curves
   ($N<5000$, §9) and explicit infinite families ([BSTW24, Thm. 1.7]; CM families with $2$-part, §6.5).

3. **"BSD is known for CM curves."** For CM $E/\mathbb{Q}$ with $r_{\mathrm{an}}\le1$: rank part and finiteness of
   Sha are theorems (Coates–Wiles, Rubin, GZK), and the $p$-part is known for $p\nmid\#\mathcal{O}_K^\times$
   in rank 0 [Rub91], and in rank 1 for potentially good ordinary $p\nmid\#\mu_K$ [LLT16] and supersingular
   $p$ [Kob13, Cor. 1.4]. Missing: $p=2$ (all CM curves), $p=3$ for $K=\mathbb{Q}(\sqrt{-3})$; so **full**
   BSD is not known for a general CM curve of rank $\le1$ (only for explicit families). For CM curves
   with $r_{\mathrm{an}}\ge2$ nothing is known beyond $p$-adic criteria ([Ban26], Coates–Liang–Sujatha).
   The rank-0 $p$-converse for CM curves is now known for every $p$ [BT25]; the rank-1 $p$-converse at
   $p=2$ is known only under a localisation hypothesis [ABS24, App.] or in the unpublished [Kri20].

4. **"The parity conjecture is a theorem."** Over $\mathbb{Q}$ the **$p$-parity** conjecture (for
   $\operatorname{Sel}_{p^\infty}$) is a theorem for all $E$ and all $p$ [DD10]. The parity of the Mordell–Weil rank
   equals the root number only if $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ is finite for some $p$ — i.e. the parity
   conjecture is `[CONDITIONAL]` on (a weak form of) the Shafarevich–Tate conjecture. Over general
   number fields even $p$-parity is not fully known (§7).

5. **"BSD holds for 100% of curves."** Not known. Known: $>66\%$ of $E/\mathbb{Q}$ (by height) satisfy the
   rank conjecture [BSZ14]; a positive proportion satisfy rank BSD with $r_{\mathrm{an}}=0$ and $=1$
   ([BS15b], [BSk14]); in every quadratic twist family $100\%$ have $2^\infty$-Selmer corank $\le1$
   [Smi25c], but the analytic rank of $100\%$ of twists is known only for the congruent number family
   in even parity [BT25]. Also not known: that the average rank equals $1/2$; that $100\%$ have
   rank $\le1$ (the best bound on the average rank is $0.885$).

6. **"Goldfeld's conjecture is proved (for some curve)."** Only the even-parity half for $y^2=x^3-x$
   [BT25] (preprint) and positive-proportion versions ([KL19] for curves with a rational $3$-isogeny;
   [Smi16] $41.9\%/55.9\%$ for congruent numbers). "BSD $\Rightarrow$ Goldfeld" is a theorem [Smi25c],
   not Goldfeld itself.

7. **"Kolyvagin's conjecture is proved."** It is proved for $p$ odd, good ordinary, split in a Heegner
   field $K$, under (irr) with $p>3$, or at Eisenstein $p$ with $\varphi|_{G_p}\ne1,\omega$ [BCGS26], and
   in the earlier settings of [Zha14], [Swe20]; not for $p=2$, not in general at supersingular or
   additive $p$, and the $p$ inert in $K$ case only recently [CS26] (preprint).

8. **"The Iwasawa main conjecture for elliptic curves is a theorem."** For good ordinary $p$ it is
   known under (irr) (+(ram) [SU14], or $p>3$ + (im) [BCS25], or Eisenstein with $\varphi|_{G_p}\ne1,\omega$
   [CGS25]); for supersingular $p>2$ only for semistable curves [BSTW24] (and CM [PR04]); it is **not**
   known at $p=2$, at additive primes, or for residually dihedral $p$ without (ram)/(im). Kato proved one divisibility only.

9. **"Wan (2014) proved the supersingular main conjecture."** The preprint [Wan14] is "no longer intended
   for publication" [BSTW24, Rem. 1.4]; the theorem is [BSTW24, Thm. 1.3].

10. **"For a rank-2 curve like 389a1 BSD is known except for Sha."** For such curves $r_{\mathrm{an}}=r_{\mathrm{alg}}=2$ can be
    certified by computation, but finiteness of $\operatorname{Sha}(E/\mathbb{Q})$ is not known for any curve of rank
    $\ge2$; only $\operatorname{Sha}[p^\infty]$ for individual $p$ [SW13], and the leading-term formula is not proved
    for any $p$ in any rank-$\ge2$ example.

11. **"Kato's theorem needs no hypothesis."** Kato's finiteness theorem (§1.4) is hypothesis-free, but
    his *integral* Iwasawa divisibility needs $p\ne2$ and a large-image condition (12.5.2); the
    $p$-adic-rank bound $r_{\mathrm{alg}}\le r_p$ needs $p$ good ordinary (with the exceptional-zero shift at split multiplicative $p$).

---

## 15. References (identifiers verified 2026-09-11 unless marked)

- [ABHS25] L. Alpöge, M. Bhargava, W. Ho, A. Shnidman, *Rank stability in quadratic extensions and Hilbert's tenth problem for the ring of integers of a number field*, Invent. Math. 243 (2025) 1129–1139, DOI 10.1007/s00222-025-01392-3; arXiv:2501.18774.
- [ABS24] L. Alpöge, M. Bhargava, A. Shnidman (appendix by A. Burungale, C. Skinner), *Integers expressible as the sum of two rational cubes*, arXiv:2210.10730 (v3, Oct 2024).
- [Ban26] B. S. Banwait, *Second derivatives of p-adic L-functions and the Shafarevich–Tate group of rank-two CM elliptic curves*, arXiv:2609.08431.
- [Bau92] W. Bauer, *On the conjecture of Birch and Swinnerton-Dyer for abelian varieties over function fields in characteristic p>0*, Invent. Math. 108 (1992) 263–287, DOI 10.1007/BF02100606.
- [BCDT01] C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over Q: wild 3-adic exercises*, J. Amer. Math. Soc. 14 (2001) 843–939, DOI 10.1090/S0894-0347-01-00370-8.
- [BCGP21] G. Boxer, F. Calegari, T. Gee, V. Pilloni, *Abelian surfaces over totally real fields are potentially modular*, Publ. Math. IHÉS 134 (2021) 153–501, DOI 10.1007/s10240-021-00128-2.
- [BCGS26] A. Burungale, F. Castella, G. Grossi, C. Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory*, arXiv:2312.09301 (v2, Jan 2026).
- [BCK21] A. Burungale, F. Castella, C.-H. Kim, *A proof of Perrin-Riou's Heegner point main conjecture*, Algebra Number Theory 15 (2021) 1627–1653, DOI 10.2140/ant.2021.15.1627; arXiv:1908.09512.
- [BCS25] A. Burungale, F. Castella, C. Skinner, *Base change and Iwasawa Main Conjectures for GL2*, Int. Math. Res. Not. IMRN 2025, rnaf082, DOI 10.1093/imrn/rnaf082; arXiv:2405.00270.
- [BCST22] A. Burungale, F. Castella, C. Skinner, Y. Tian, *$p^\infty$-Selmer groups and rational points on CM elliptic curves*, Ann. Math. Québec 46 (2022) 325–346, DOI 10.1007/s40316-022-00203-y.
- [BDP13] M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles and p-adic Rankin L-series*, Duke Math. J. 162 (2013) 1033–1148 `[journal data not re-verified]`.
- [BDV22] M. Bertolini, H. Darmon, R. Venerucci, *Heegner points and Beilinson–Kato elements: a conjecture of Perrin-Riou*, Adv. Math. 398 (2022) 108172, DOI 10.1016/j.aim.2021.108172.
- [BFH90] D. Bump, S. Friedberg, J. Hoffstein, *Nonvanishing theorems for L-functions of modular forms and their derivatives*, Invent. Math. 102 (1990) 543–618, DOI 10.1007/BF01233440.
- [BH26] B. S. Banwait, X. Huang, *On the identification of elliptic curves that admit infinitely many twists satisfying the BSD conjecture*, arXiv:2601.16044.
- [BJPV25] M. Bansal, S. Jha, A. Pal, G. Venkat, *A p-converse theorem for real quadratic fields*, arXiv:2504.21799.
- [BKLOS19] M. Bhargava, Z. Klagsbrun, R. Lemke Oliver, A. Shnidman, *3-isogeny Selmer groups and ranks of abelian varieties in quadratic twist families over a number field*, Duke Math. J. 168 (2019), DOI 10.1215/00127094-2019-0031.
- [BKO23] A. Burungale, S. Kobayashi, K. Ota, *p-adic L-functions and rational points on CM elliptic curves at inert primes*, J. Inst. Math. Jussieu (published online 17 July 2023).
- [BLV26] M. Bertolini, M. Longo, R. Venerucci, *The anticyclotomic main conjectures for elliptic curves*, Math. Ann. 395 (2026), DOI 10.1007/s00208-026-03381-0; arXiv:2306.17784.
- [Box22] J. Box, *Elliptic curves over totally real quartic fields not containing √5 are modular*, Trans. Amer. Math. Soc. (2022), DOI 10.1090/tran/8557.
- [BPR93] D. Bernardi, B. Perrin-Riou, *Variante p-adique de la conjecture de Birch et Swinnerton-Dyer (le cas supersingulier)*, C. R. Acad. Sci. Paris 317 (1993) 227–232 `[unverified]`.
- [Bro15] E. H. Brooks, *Shimura curves and special values of p-adic L-functions*, Int. Math. Res. Not. IMRN 2015 `[unverified]`.
- [BS13a] M. Bhargava, A. Shankar, *The average number of elements in the 4-Selmer groups of elliptic curves is 7*, arXiv:1312.7333.
- [BS13b] M. Bhargava, A. Shankar, *The average size of the 5-Selmer group of elliptic curves is 6, and the average rank is less than 1*, arXiv:1312.7859.
- [BS15a] M. Bhargava, A. Shankar, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, Ann. of Math. 181 (2015) 191–242, DOI 10.4007/annals.2015.181.1.3.
- [BS15b] M. Bhargava, A. Shankar, *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0*, Ann. of Math. 181 (2015) 587–621, DOI 10.4007/annals.2015.181.2.4.
- [BSk14] M. Bhargava, C. Skinner, *A positive proportion of elliptic curves over Q have rank one*, arXiv:1401.0233 (J. Ramanujan Math. Soc. 29 (2014) `[journal data not verified]`).
- [BSTW24] A. Burungale, C. Skinner, Y. Tian, X. Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350 (v2, Sep 2024).
- [BSZ14] M. Bhargava, C. Skinner, W. Zhang, *A majority of elliptic curves over Q satisfy the Birch and Swinnerton-Dyer conjecture*, arXiv:1407.1826.
- [BT20] A. Burungale, Y. Tian, *p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, Invent. Math. 220 (2020) 211–253, DOI 10.1007/s00222-019-00929-7.
- [BT22] A. Burungale, Y. Tian, *The even parity Goldfeld conjecture: congruent number elliptic curves* (expository), J. Number Theory 230 (2022) 161–195, DOI 10.1016/j.jnt.2021.05.001; arXiv:2104.06732.
- [BT25] A. Burungale, Y. Tian, *A rank zero p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, arXiv:2506.03465 (v2, Oct 2025).
- [Cas18] F. Castella, *On the p-part of the Birch–Swinnerton-Dyer formula for multiplicative primes*, Camb. J. Math. 6 (2018) 1–23, DOI 10.4310/CJM.2018.v6.n1.a1; arXiv:1704.06608.
- [Cas23] F. Castella, *Nonvanishing of generalised Kato classes and Iwasawa main conjectures*, arXiv:2312.01481.
- [Cas24a] F. Castella, *Exceptional zeros for Heegner points and p-converse to the theorem of Gross–Zagier and Kolyvagin*, arXiv:2409.01360.
- [Cas24b] F. Castella, *Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*, arXiv:2407.11891 (v3, Sep 2025).
- [Cas25] F. Castella, *A formula of Perrin-Riou and characteristic power series of signed Selmer groups*, arXiv:2502.19618.
- [Cas26] F. Castella, *Generalised Kato classes on CM elliptic curves of rank 2*, arXiv:2204.09608 (v3, Feb 2026).
- [Cas62] J. W. S. Cassels, *Arithmetic on curves of genus 1. IV. Proof of the Hauptvermutung*, J. reine angew. Math. 211 (1962) 95–112 `[DOI not verified]`.
- [CCSS18] F. Castella, M. Çiperiani, C. Skinner, F. Sprung, *On the Iwasawa main conjectures for modular forms at non-ordinary primes*, arXiv:1804.10993.
- [Čes16] K. Česnavičius, *The p-parity conjecture for elliptic curves with a p-isogeny*, J. reine angew. Math. 719 (2016) 45–73, DOI 10.1515/crelle-2014-0040; arXiv:1207.0431.
- [CGLS22] F. Castella, G. Grossi, J. Lee, C. Skinner, *On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes*, Invent. Math. 227 (2022) 517–580, DOI 10.1007/s00222-021-01072-y; arXiv:2008.02571.
- [CGS25] F. Castella, G. Grossi, C. Skinner, *Mazur's main conjecture at Eisenstein primes*, Math. Ann. 393 (2025) 2451–2506, DOI 10.1007/s00208-025-03239-x; arXiv:2303.04373.
- [CH22] F. Castella, M.-L. Hsieh, *On the non-vanishing of generalized Kato classes for elliptic curves of rank 2*, arXiv:1809.09066 (Forum Math. Sigma 10 (2022) `[journal data not verified]`).
- [CLTZ15] J. Coates, Y. Li, Y. Tian, S. Zhai, *Quadratic twists of elliptic curves*, Proc. London Math. Soc. 110 (2015) 357–394, DOI 10.1112/plms/pdu059.
- [CLW26] F. Castella, Z. Liu, X. Wan, *Kato's main conjecture for nonordinary modular forms*, arXiv:2608.29470.
- [CM12] B. Creutz, R. L. Miller, *Second isogeny descents and the Birch and Swinnerton-Dyer conjectural formula*, J. Algebra 372 (2012) 673–701, DOI 10.1016/j.jalgebra.2012.09.029; arXiv:1105.4018.
- [CN23] A. Caraiani, J. Newton, *On the modularity of elliptic curves over imaginary quadratic fields*, arXiv:2301.10509 `[not fetched]`.
- [CS26] F. Castella, T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, arXiv:2601.14504.
- [CW23] F. Castella, X. Wan, *Perrin-Riou's main conjecture for elliptic curves at supersingular primes*, Math. Ann. 389 (2023) 2595–2636, DOI 10.1007/s00208-023-02711-w; arXiv:1607.02019.
- [CW77] J. Coates, A. Wiles, *On the conjecture of Birch and Swinnerton-Dyer*, Invent. Math. 39 (1977) 223–251, DOI 10.1007/BF01402975.
- [DD08] T. Dokchitser, V. Dokchitser, *Parity of ranks for elliptic curves with a cyclic isogeny*, J. Number Theory 128 (2008) 662–679, DOI 10.1016/j.jnt.2007.02.008; arXiv:math/0604149.
- [DD09] T. Dokchitser, V. Dokchitser, *Regulator constants and the parity conjecture*, Invent. Math. 178 (2009) 23–71, DOI 10.1007/s00222-009-0193-7; arXiv:0709.2852.
- [DD10] T. Dokchitser, V. Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, Ann. of Math. 172 (2010) 567–596, DOI 10.4007/annals.2010.172.567; arXiv:math/0610290.
- [DD11] T. Dokchitser, V. Dokchitser, *Root numbers and parity of ranks of elliptic curves*, J. reine angew. Math. 658 (2011) 39–64, DOI 10.1515/crelle.2011.060; arXiv:0906.1815.
- [DGKM25] V. Dokchitser, H. Green, A. Konstantinou, A. Morgan, *Parity of ranks of Jacobians of curves*, Proc. London Math. Soc. 131 (2025), DOI 10.1112/plms.70083; arXiv:2211.06357.
- [Dis17] D. Disegni, *The p-adic Gross–Zagier formula on Shimura curves*, Compos. Math. 153 (2017) 1987–2074.
- [Dis20] D. Disegni, *On the p-adic Birch and Swinnerton-Dyer conjecture for elliptic curves over number fields*, Kyoto J. Math. 60 (2020), DOI 10.1215/21562261-2018-0012.
- [Dis22] D. Disegni, *The universal p-adic Gross–Zagier formula*, Invent. Math. 230 (2022) 509–649, DOI 10.1007/s00222-022-01133-w (correction: Invent. Math. 243 (2025) 243–244).
- [DM23] V. Dokchitser, C. Maistret, *On the parity conjecture for abelian surfaces*, Proc. London Math. Soc. 127 (2023) 295–365, DOI 10.1112/plms.12545; arXiv:1911.04626.
- [DNS20] M. Derickx, F. Najman, S. Siksek, *Elliptic curves over totally real cubic fields are modular*, Algebra Number Theory 14 (2020) 1791–1800, DOI 10.2140/ant.2020.14.1791.
- [Dok24] V. Dokchitser, *A note on the parity conjecture and base change*, arXiv:2407.18260.
- [DR25] E. Da Ronche, *Kolyvagin's conjecture for modular forms at non-ordinary primes*, arXiv:2503.09955.
- [DZ26] D. Disegni, W. Zhang, *Gan–Gross–Prasad cycles and derivatives of p-adic L-functions*, arXiv:2410.08401 (v2, Mar 2026).
- [FLHS15] N. Freitas, B. Le Hung, S. Siksek, *Elliptic curves over real quadratic fields are modular*, Invent. Math. 201 (2015) 159–206, DOI 10.1007/s00222-014-0550-z.
- [GJM26] S. Gunri, S. Jha, D. Majumdar, *Explicit mock Heegner points and BSD formula on certain Mordell curves*, arXiv:2607.26774.
- [GJPST09] G. Grigorov, A. Jorza, S. Patrikis, W. Stein, C. Tarniţă, *Computational verification of the Birch and Swinnerton-Dyer conjecture for individual elliptic curves*, Math. Comp. 78 (2009) 2397–2425, DOI 10.1090/S0025-5718-09-02253-4.
- [GM22] H. Green, C. Maistret, *The 2-parity conjecture for elliptic curves with isomorphic 2-torsion*, Proc. R. Soc. A 478 (2022), DOI 10.1098/rspa.2022.0112; arXiv:2110.06718.
- [Gol79] D. Goldfeld, *Conjectures on elliptic curves over quadratic fields*, Number Theory Carbondale 1979, Lecture Notes in Math. 751, Springer (1979) 108–118 `[unverified]`.
- [GV00] R. Greenberg, V. Vatsal, *On the Iwasawa invariants of elliptic curves*, Invent. Math. 142 (2000) 17–63, DOI 10.1007/s002220000080.
- [GZ86] B. Gross, D. Zagier, *Heegner points and derivatives of L-series*, Invent. Math. 84 (1986) 225–320, DOI 10.1007/BF01388809.
- [How04] B. Howard, *The Heegner point Kolyvagin system*, Compos. Math. 140 (2004) 1439–1472, DOI 10.1112/S0010437X04000569.
- [IS24] R. Ito, F. Sprung, *On Iwasawa main conjectures for elliptic curves at supersingular primes: beyond the case $a_p=0$*, Adv. Math. 449 (2024) 109741, DOI 10.1016/j.aim.2024.109741.
- [JSW17] D. Jetchev, C. Skinner, X. Wan, *The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one*, Camb. J. Math. 5 (2017) 369–434, DOI 10.4310/CJM.2017.v5.n3.a2; arXiv:1512.06894.
- [Kat04] K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004) 117–290 (numdam AST_2004__295__117_0).
- [Kim07] B. D. Kim, *The parity conjecture for elliptic curves at supersingular reduction primes*, Compos. Math. 143 (2007) 47–72, DOI 10.1112/S0010437X06002569.
- [KL16] D. Kriz, C. Li, *Congruences between Heegner points and quadratic twists of elliptic curves*, arXiv:1606.03172.
- [KL19] D. Kriz, C. Li, *Goldfeld's conjecture and congruences between Heegner points*, Forum Math. Sigma 7 (2019) e15, DOI 10.1017/fms.2019.9; arXiv:1609.06687.
- [KL92] V. A. Kolyvagin, D. Yu. Logachëv, *Finiteness of Ш over totally real fields*, Math. USSR-Izv. 39 (1992) 829–853, DOI 10.1070/IM1992v039n01ABEH002228.
- [Kob03] S. Kobayashi, *Iwasawa theory for elliptic curves at supersingular primes*, Invent. Math. 152 (2003) 1–36, DOI 10.1007/s00222-002-0265-4.
- [Kob13] S. Kobayashi, *The p-adic Gross–Zagier formula for elliptic curves at supersingular primes*, Invent. Math. 191 (2013) 527–629, DOI 10.1007/s00222-012-0400-9.
- [Kol88] V. A. Kolyvagin, *Finiteness of E(Q) and Ш(E,Q) for a subclass of Weil curves*, Math. USSR-Izv. 32 (1989) 523–541, DOI 10.1070/IM1989v032n03ABEH000779 (Russian original Izv. 52 (1988)).
- [Kol89] V. A. Kolyvagin, *On the Mordell–Weil and Shafarevich–Tate groups for Weil elliptic curves*, Math. USSR-Izv. 33 (1989) 473–499, DOI 10.1070/IM1989v033n03ABEH000853.
- [Kol90] V. A. Kolyvagin, *Euler systems*, The Grothendieck Festschrift II, Progr. Math. 87, Birkhäuser (1990) 435–483 `[DOI not verified]`.
- [Kol91a] V. A. Kolyvagin, *On the structure of Selmer groups*, Math. Ann. 291 (1991) 253–259, DOI 10.1007/BF01445205.
- [Kol91b] V. A. Kolyvagin, *On the structure of Shafarevich–Tate groups*, Algebraic geometry (Chicago 1989), Lecture Notes in Math. 1479, Springer (1991) 94–121 `[unverified]`.
- [KiP25] C.-H. Kim, R. Pollack, *The refined Tamagawa number conjectures for GL2*, arXiv:2505.09121.
- [KoP24] P. Koymans, C. Pagano, *Hilbert's tenth problem via additive combinatorics*, arXiv:2412.01768 (v3, Nov 2025).
- [KoP25] P. Koymans, C. Pagano, *Elliptic curves of rank one over number fields*, arXiv:2505.16910.
- [KS22] T. Keller, M. Stoll, *Exact verification of the strong BSD conjecture for some absolutely simple abelian surfaces*, C. R. Math. Acad. Sci. Paris 360 (2022) 483–489, DOI 10.5802/crmath.313; arXiv:2107.00325.
- [KS24] P. Koymans, A. Smith, *Sums of rational cubes and the 3-Selmer group*, arXiv:2405.09311.
- [KS25] T. Keller, M. Stoll, *Complete verification of strong BSD for many modular abelian surfaces over Q*, Forum Math. Sigma 13 (2025), DOI 10.1017/fms.2024.133; arXiv:2312.07307.
- [KT03] K. Kato, F. Trihan, *On the conjectures of Birch and Swinnerton-Dyer in characteristic p>0*, Invent. Math. 153 (2003) 537–592, DOI 10.1007/s00222-003-0299-2.
- [KTTT24] W. Kim, K.-S. Tan, F. Trihan, K.-W. Tsoi, *On a BSD type conjecture for the Hasse–Weil–Artin L-functions in characteristic p>0*, arXiv:2411.12404.
- [KY24a] T. Keller, M. Yin, *On the anticyclotomic Iwasawa theory of newforms at Eisenstein primes of semistable reduction*, arXiv:2402.12781.
- [KY24b] T. Keller, M. Yin, *p-converse theorems for elliptic curves of potentially good ordinary reduction at Eisenstein primes*, arXiv:2410.23241.
- [Kri20] D. Kriz, *Supersingular main conjectures, Sylvester's conjecture and Goldfeld's conjecture*, arXiv:2002.04767 (v5, Oct 2022; unpublished).
- [Li26] H. Li, *A p-part Birch and Swinnerton-Dyer formula over totally imaginary quadratic extension of totally real fields*, arXiv:2608.11969.
- [LLT16] Y. Li, Y. Liu, Y. Tian, *On the Birch and Swinnerton-Dyer conjecture for CM elliptic curves over Q*, arXiv:1605.01481.
- [Lon06] M. Longo, *On the Birch and Swinnerton-Dyer conjecture for modular elliptic curves over totally real fields*, Ann. Inst. Fourier 56 (2006) 689–733, DOI 10.5802/aif.2197.
- [LPV24] M. Longo, M. R. Pati, S. Vigni, *Kolyvagin's conjecture for modular forms*, arXiv:2412.02303; *Anticyclotomic Iwasawa main conjectures for modular forms*, arXiv:2603.22483.
- [LSZ22] D. Loeffler, C. Skinner, S. L. Zerbes, *Euler systems for GSp(4)*, J. Eur. Math. Soc. 24 (2022) 669–733, DOI 10.4171/JEMS/1124; arXiv:1706.00201.
- [LTX24] Y. Liu, Y. Tian, L. Xiao, *Iwasawa's main conjecture for Rankin–Selberg motives in the anticyclotomic case*, arXiv:2406.00624.
- [LW16] T. Lawson, C. Wuthrich, *Vanishing of some Galois cohomology groups for elliptic curves*, in: Elliptic curves, modular forms and Iwasawa theory, Springer Proc. Math. Stat. 188 (2016) 373–399, DOI 10.1007/978-3-319-45032-2_11; arXiv:1505.02940.
- [LZ23] D. Loeffler, S. L. Zerbes, *On the Birch–Swinnerton-Dyer conjecture for modular abelian surfaces*, arXiv:2110.13102 (v3, Jul 2023).
- [LZ25a] D. Loeffler, S. L. Zerbes, *Iwasawa theory for quadratic Hilbert modular forms*, arXiv:2006.14491 (v2, Feb 2025).
- [LZ25b] D. Loeffler, S. L. Zerbes, *Ultra-Kolyvagin systems and non-ordinary Selmer groups*, arXiv:2511.08793.
- [LZ26a] D. Loeffler, S. L. Zerbes, *A universal Euler system for GSp(4)*, Forum Math., DOI 10.1515/forum-2025-0062; arXiv:2411.12576.
- [LZ26b] D. Loeffler, S. L. Zerbes, *On the Bloch–Kato conjecture for GSp(4)*, Camb. J. Math. 14 (2026) 603–784, DOI 10.4310/CJM.260722230404; arXiv:2003.05960.
- [Mil11] R. L. Miller, *Proving the Birch and Swinnerton-Dyer conjecture for specific elliptic curves of analytic rank zero and one*, LMS J. Comput. Math. 14 (2011) 327–350; arXiv:1010.2431.
- [Mil75] J. S. Milne, *On a conjecture of Artin and Tate*, Ann. of Math. 102 (1975) 517–533, DOI 10.2307/1971042.
- [MM91] M. R. Murty, V. K. Murty, *Mean values of derivatives of modular L-series*, Ann. of Math. 133 (1991) 447–475, DOI 10.2307/2944316.
- [MMZ26] L. Mastella, A. Matar, F. Zerman, *Vanishing of Sha(A/K)[P^∞] and its consequences for the anticyclotomic Iwasawa theory of GL2-abelian varieties*, arXiv:2608.29337.
- [MN19] A. Matar, J. Nekovář, *Kolyvagin's result on the vanishing of Ш(E/K)[p^∞] and its consequences for anticyclotomic Iwasawa theory*, J. Théor. Nombres Bordeaux 31 (2019) 455–501; arXiv:1808.09544.
- [Mon96] P. Monsky, *Generalizing the Birch–Stephens theorem I. Modular curves*, Math. Z. 221 (1996) 415–420, DOI 10.1007/PL00004518.
- [MS13] R. L. Miller, M. Stoll, *Explicit isogeny descent on elliptic curves*, Math. Comp. 82 (2013) 513–529, DOI 10.1090/S0025-5718-2012-02619-6; arXiv:1010.3334.
- [MTT86] B. Mazur, J. Tate, J. Teitelbaum, *On p-adic analogues of the conjectures of Birch and Swinnerton-Dyer*, Invent. Math. 84 (1986) 1–48, DOI 10.1007/BF01388731.
- [Nek06] J. Nekovář, *Selmer complexes*, Astérisque 310 (2006) `[unverified]`.
- [Nek07] J. Nekovář, *On the parity of ranks of Selmer groups III*, Doc. Math. 12 (2007) 243–274, DOI 10.4171/dm/225.
- [Nek07b] J. Nekovář, *The Euler system method for CM points on Shimura curves*, in: L-functions and Galois representations (Durham 2004), LMS Lecture Note Ser. 320, CUP (2007) 471–547, DOI 10.1017/CBO9780511721267.014.
- [Nek09] J. Nekovář, *On the parity of ranks of Selmer groups IV* (with an appendix by J.-P. Wintenberger), Compos. Math. 145 (2009) 1351–1359, DOI 10.1112/S0010437X09003959.
- [Nek12] J. Nekovář, *Level raising and anticyclotomic Selmer groups for Hilbert modular forms of weight two*, Canad. J. Math. 64 (2012) 588–668, DOI 10.4153/CJM-2011-077-6.
- [Pol03] R. Pollack, *On the p-adic L-function of a modular form at a supersingular prime*, Duke Math. J. 118 (2003) 523–558 `[unverified]`.
- [PR04] R. Pollack, K. Rubin, *The main conjecture for CM elliptic curves at supersingular primes*, Ann. of Math. 159 (2004) 447–464, DOI 10.4007/annals.2004.159.447.
- [PR87] B. Perrin-Riou, *Points de Heegner et dérivées de fonctions L p-adiques*, Invent. Math. 89 (1987) 455–510, DOI 10.1007/BF01388982.
- [PR93] B. Perrin-Riou, *Fonctions L p-adiques d'une courbe elliptique et points rationnels*, Ann. Inst. Fourier 43 (1993) 945–995, DOI 10.5802/aif.1362.
- [PT25] J. Pan, Y. Tian, *On the distribution of 2-Selmer ranks of quadratic twists of elliptic curves over Q*, arXiv:2503.21462.
- [Rub87] K. Rubin, *Tate–Shafarevich groups and L-functions of elliptic curves with complex multiplication*, Invent. Math. 89 (1987) 527–559, DOI 10.1007/BF01388984.
- [Rub91] K. Rubin, *The "main conjectures" of Iwasawa theory for imaginary quadratic fields*, Invent. Math. 103 (1991) 25–68, DOI 10.1007/BF01239508.
- [Rub92] K. Rubin, *p-adic L-functions and rational points on elliptic curves with complex multiplication*, Invent. Math. 107 (1992) 323–350, DOI 10.1007/BF01231893.
- [Rub99] K. Rubin, *Elliptic curves with complex multiplication and the conjecture of Birch and Swinnerton-Dyer*, in: Arithmetic theory of elliptic curves (Cetraro 1997), Lecture Notes in Math. 1716, Springer (1999) 167–234 `[journal data not re-verified; text fetched from swc-math.github.io]`.
- [Sch82] P. Schneider, *Zur Vermutung von Birch und Swinnerton-Dyer über globalen Funktionenkörpern*, Math. Ann. 260 (1982) 495–510, DOI 10.1007/BF01457028.
- [Ser72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972) 259–331 `[DOI not verified]`.
- [Ski16] C. Skinner, *Multiplicative reduction and the cyclotomic main conjecture for GL2*, Pacific J. Math. 283 (2016) 171–200, DOI 10.2140/pjm.2016.283.171.
- [Ski20] C. Skinner, *A converse to a theorem of Gross, Zagier, and Kolyvagin*, Ann. of Math. 191 (2020) 329–354, DOI 10.4007/annals.2020.191.2.1; arXiv:1405.7294.
- [Smi16] A. Smith, *The congruent numbers have positive natural density*, arXiv:1603.08479.
- [Smi17] A. Smith, *$2^\infty$-Selmer groups, $2^\infty$-class groups, and Goldfeld's conjecture*, arXiv:1702.02325 (unpublished; superseded).
- [Smi25a] A. Smith, *The distribution of $\ell^\infty$-Selmer groups in degree $\ell$ twist families I*, J. Amer. Math. Soc. 39 (2025) 1–72, DOI 10.1090/jams/1062; arXiv:2207.05674.
- [Smi25b] A. Smith, *… II*, J. Amer. Math. Soc. 39 (2025) 453–514, DOI 10.1090/jams/1063; arXiv:2207.05143.
- [Smi25c] A. Smith, *The Birch and Swinnerton-Dyer conjecture implies Goldfeld's conjecture*, arXiv:2503.17619.
- [Spr16] F. Sprung, *The Iwasawa main conjecture for elliptic curves at odd supersingular primes*, arXiv:1610.10017 (publication not confirmed).
- [SU14] C. Skinner, E. Urban, *The Iwasawa main conjectures for GL2*, Invent. Math. 195 (2014) 1–277, DOI 10.1007/s00222-013-0448-1.
- [SW13] W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013) 1757–1792, DOI 10.1090/S0025-5718-2012-02649-4.
- [Swe20] N. Sweeting, *Kolyvagin's conjecture and patched Euler systems in anticyclotomic Iwasawa theory*, arXiv:2012.11771 (v3, Nov 2022; publication not confirmed).
- [Swe25] N. Sweeting, *On the Bloch–Kato conjecture for some four-dimensional symplectic Galois representations*, arXiv:2503.19226.
- [SZ14] C. Skinner, W. Zhang, *Indivisibility of Heegner points in the multiplicative case*, arXiv:1407.1099.
- [Tan26] K.-S. Tan, *p-adic L-functions for elliptic curves over global function fields*, arXiv:2603.10576.
- [Tat66] J. Tate, *On the conjectures of Birch and Swinnerton-Dyer and a geometric analog*, Sém. Bourbaki 9 (1964–66), exp. 306, 415–440 (numdam).
- [Tia14] Y. Tian, *Congruent numbers and Heegner points*, Camb. J. Math. 2 (2014) 117–161, DOI 10.4310/CJM.2014.v2.n1.a4.
- [TTT26a] K.-S. Tan, F. Trihan, K.-W. Tsoi, *Iwasawa main conjecture for ordinary semistable elliptic curves over global function fields*, arXiv:2603.11615.
- [TTT26b] K.-S. Tan, F. Trihan, K.-W. Tsoi, *Specialisations of the Burungale–Castella–Skinner main conjecture to $\mathbb{Z}_p$-lines*, arXiv:2608.26791.
- [TW95] R. Taylor, A. Wiles, *Ring-theoretic properties of certain Hecke algebras*, Ann. of Math. 141 (1995) 553–572 `[DOI not verified]`.
- [TYZ17] Y. Tian, X. Yuan, S. Zhang, *Genus periods, genus points and congruent number problem*, Asian J. Math. 21 (2017) 721–774, DOI 10.4310/AJM.2017.v21.n4.a5.
- [Ulm02] D. Ulmer, *Elliptic curves with large rank over function fields*, Ann. of Math. 155 (2002) 295–315, DOI 10.2307/3062158.
- [Ven16] R. Venerucci, *On the p-converse of the Kolyvagin–Gross–Zagier theorem*, Comment. Math. Helv. 91 (2016) 397–444, DOI 10.4171/CMH/390.
- [Wal85] J.-L. Waldspurger, *Sur les valeurs de certaines fonctions L automorphes en leur centre de symétrie*, Compos. Math. 54 (1985) 173–242 `[unverified]`.
- [Wan14] X. Wan, *Iwasawa main conjecture for supersingular elliptic curves and BSD conjecture*, arXiv:1411.6352 (v9, Sep 2024; withdrawn from publication per [BSTW24, Rem. 1.4]).
- [Wan15] X. Wan, *The Iwasawa main conjecture for Hilbert modular forms*, Forum Math. Sigma 3 (2015) e18, DOI 10.1017/fms.2015.16.
- [Wan20] X. Wan, *Iwasawa main conjecture for Rankin–Selberg p-adic L-functions*, Algebra Number Theory 14 (2020) 383–483, DOI 10.2140/ant.2020.14.383.
- [Wil95] A. Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Ann. of Math. 141 (1995) 443–551 `[DOI not verified]`.
- [Wut14] C. Wuthrich, *On the integrality of modular symbols and Kato's Euler system for elliptic curves*, Doc. Math. 19 (2014) 381–402 `[unverified]`.
- [YZ17] Z. Yun, W. Zhang, *Shtukas and the Taylor expansion of L-functions*, Ann. of Math. 186 (2017), DOI 10.4007/annals.2017.186.3.2.
- [YZ19] Z. Yun, W. Zhang, *Shtukas and the Taylor expansion of L-functions (II)*, Ann. of Math. 189 (2019), DOI 10.4007/annals.2019.189.2.2.
- [YaZ26] X. Yan, X. Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes*, J. Algebra 693 (2026) 372–402, DOI 10.1016/j.jalgebra.2026.01.016; arXiv:2412.20078.
- [YZZ13] X. Yuan, S. Zhang, W. Zhang, *The Gross–Zagier formula on Shimura curves*, Ann. of Math. Studies 184, Princeton Univ. Press (2013), DOI 10.23943/princeton/9780691155913.001.0001.
- [Zan19] M. Zanarella, *A proof of Kolyvagin's conjecture via the BDP main conjecture*, arXiv:1909.07835.
- [Zha01a] S. Zhang, *Heights of Heegner points on Shimura curves*, Ann. of Math. 153 (2001) 27–147, DOI 10.2307/2661372.
- [Zha01b] S. Zhang, *Gross–Zagier formula for GL2*, Asian J. Math. 5 (2001) 183–290, DOI 10.4310/AJM.2001.v5.n2.a1.
- [Zha14] W. Zhang, *Selmer groups and the indivisibility of Heegner points*, Camb. J. Math. 2 (2014) 191–253, DOI 10.4310/CJM.2014.v2.n2.a2.
- [Zha25] S. Zhai, *The Birch–Swinnerton-Dyer exact formula for quadratic twists of elliptic curves*, Pure Appl. Math. Q. (2025), DOI 10.4310/PAMQ.250710201739.
