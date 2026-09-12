# B. Attack via Euler systems: Kato, Heegner points, Kolyvagin systems

Owner: agent B. Charter: `../00-charter.md`. Cross-references: `../01-statement-and-reductions.md`,
`../03-obstructions-rank-ge-2.md`, `A-iwasawa-padic.md`, `C-higher-rank-euler-systems-diagonal-cycles.md`,
`F-analytic-side.md`, `H-sha-and-descent.md`. All citations below were checked against the source
(arXiv abstract page, Numdam, Crossref/zbMATH record, or the published text) on 2026-09-11; the
search log is in §9.

## 0. Summary of the outcome of this line

The Euler-system method proves BSD (rank statement and finiteness of $\mathrm{Sha}$) exactly when
$r_{\mathrm{an}}\le 1$, and it does so through a *bottom class* whose non-vanishing is equivalent to an
$L$-value or $L$-derivative being non-zero (Kato's zeta element $\leftrightarrow L(E,1)$; the Heegner point
$\leftrightarrow L'(E/K,1)$). For $r_{\mathrm{an}}\ge 2$ **both bottom classes vanish identically**
(§1.4, §4.3), and all information is carried by *derived* classes $\kappa_n$, $\nu(n)\ge 1$.

Since 2014–2026 the following has become a theorem for a large set of primes $p$
(Zhang, Sweeting, Burungale–Castella–Grossi–Skinner; Kolyvagin's structure theorem):

$$
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})
=\nu_\infty(E,K,p)+1
\qquad(\text{§4, Theorem B.4.5}),
$$

for any $E/\mathbb Q$ with $w(E)=+1$ and $\operatorname{rank}E(\mathbb Q)\ge 2$, where $K$ is an auxiliary
imaginary quadratic field with $r_{\mathrm{an}}(E^K)=1$ and $\nu_\infty(E,K,p)$ is the *order of
vanishing* of Kolyvagin's Heegner-point Kolyvagin system (the "$M(E,K,p)$" of the brief). Consequently, for
$E=389a1$ and every such $p$:

$$
\operatorname{Sha}(E/\mathbb Q)[p^\infty]\ \text{finite}
\iff \nu_\infty(E,K,p)=1
\iff \exists\ \text{Kolyvagin prime }\ell:\ \kappa_\ell\neq 0 .
$$

So the Euler-system attack on rank $2$ reduces, *exactly and unconditionally for these $p$*, to the
non-vanishing of a single first-derived Heegner class $\kappa_\ell\in H^1(K,E[p^{M}])$ (§4.5). The analytic
input that would force this non-vanishing is missing: the only formulae available for $\kappa_n$ are integral
congruence formulae (Kim's "higher Gross–Zagier formula" in terms of Kurihara numbers, §4.5.4), and no
formula links $\kappa_\ell$ (or the second Kurihara derivative on the Kato side) to $L''(E,1)$. This is
isolated as [GAP B.3] and [GAP B.1]; the structural reason (non-semisimplicity of $\mathbb Z_p[G_n]$ when
$p^M\mid |G_n|$, so that $\chi$-decompositions of Heegner points lose exactly the information Kolyvagin's
derivatives extract) is worked out in §4.5.5.

Everything of substance carries a tag. `[NEW]` items are elementary corollaries whose proofs are complete on
the page; none of them claims more than a specialisation or a bookkeeping identity, and each says what it
specialises.

## 0.1 Notation and sign conventions (used throughout)

- $E/\mathbb Q$, conductor $N$, newform $f=\sum a_nq^n\in S_2(\Gamma_0(N))$, root number $w=w(E/\mathbb Q)=\pm1$,
  so $\Lambda(E,s)=w\,\Lambda(E,2-s)$ and $r_{\mathrm{an}}\equiv \frac{1-w}{2}\pmod 2$.
- $p$ an odd prime; $T=T_pE$; $\bar\rho=\bar\rho_{E,p}:G_\mathbb Q\to \mathrm{Aut}(E[p])\cong GL_2(\mathbb F_p)$.
  (sur): $\bar\rho$ surjective. (irr): $E[p]$ irreducible.
- $K$ imaginary quadratic, discriminant $D_K<0$, $\chi_K$ its character, $u_K=\tfrac12|\mathcal O_K^\times|$, $h_K$ class
  number. **Heegner hypothesis** (Heeg): every prime $\ell\mid N$ splits in $K$ (so $(D_K,N)=1$). Generalised
  Heegner hypothesis: $N=N^+N^-$, $N^-$ squarefree with an even number of prime factors inert in $K$, primes of
  $N^+$ split. (disc): $D_K$ odd and $D_K\neq -3$.
- $K[n]$: ring class field of conductor $n$; $\mathcal G_n=\operatorname{Gal}(K[n]/K)$, $G_n=\operatorname{Gal}(K[n]/K[1])
  \cong\prod_{\ell\mid n}G_\ell$, and for $\ell$ inert in $K$, $\ell\nmid D_K$, $D_K\notin\{-3,-4\}$: $G_\ell$ cyclic of
  order $\ell+1$. $\tau\in\operatorname{Gal}(K/\mathbb Q)$ complex conjugation; $E^K$ the quadratic twist.
- Eigenspaces: for a $\mathbb Z_p[\operatorname{Gal}(K/\mathbb Q)]$-module $A$ with $p$ odd, $A=A^+\oplus A^-$
  ($\tau=\pm1$). **Kolyvagin (1991) uses a different labelling** (his $A^\nu$, $\nu\in\{0,1\}$, is the
  $\varepsilon(-1)^{\nu-1}$-eigenspace with $\varepsilon=(-1)^{g-1}=-w$); we translate everything into $\pm$.
- Kolyvagin primes for $(E,K,p)$: primes $\ell\nmid NpD_K$, inert in $K$, with
  $M(\ell):=\min\{\operatorname{ord}_p(\ell+1),\operatorname{ord}_p(a_\ell)\}\ge 1$. $\Lambda$ (or $\mathcal N_{\mathrm{Heeg}}$)
  = squarefree products $n$ of Kolyvagin primes; $\nu(n)=\#\{\ell\mid n\}$; $M(n)=\min_{\ell\mid n}M(\ell)$, $M(1)=\infty$.
- $\kappa_n=c_M(n)\in H^1(K,E[p^M])$, $M\le M(n)$: Kolyvagin's derived classes (§2.2); $\kappa^\infty=\{c_M(n)\}$.
- $\nu_\infty=\nu_\infty(E,K,p):=\min\{\nu(n): c_M(n)\ne0 \text{ for some } M\le M(n)\}\in\mathbb Z_{\ge0}\cup\{\infty\}$,
  the **order of vanishing** of $\kappa^\infty$ (this is the quantity the brief calls $M(E,K,p)$; we keep $\mathcal M$
  for divisibility indices, as Kolyvagin and Zhang do).
- $\mathcal M(n)=\max\{m: c_M(n)\in p^mH^1(K,E[p^M])\ \forall M\le M(n)\}$ ($=\infty$ if $c_M(n)=0$ for all $M$),
  $\mathcal M_r=\min_{\nu(n)=r}\mathcal M(n)$, $\mathcal M_\infty=\lim_r\mathcal M_r$ (Zhang 2014, §3.8; Kolyvagin's $m_r$, $m$).
- $r_p^\pm(E/K)=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/K)^\pm$; $r_p(E/\mathbb Q)=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$;
  $s_p(E):=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sha}(E/\mathbb Q)[p^\infty]$, so $r_p(E/\mathbb Q)=r_{\mathrm{alg}}+s_p(E)$.

---

## 1. Kato's Euler system

### 1.1 Construction (outline)

[THEOREM] (Kato 2004 = [Ka04], Chapters I–II; expositions Scholl 1998 [Sc98], Rubin 1998 [Ru98], Colmez 2004 [Co04].)
For $M,N\ge 3$ let $Y(M,N)$ be the modular curve of full level structure, and let $g_{a/M,b/N}\in\mathcal O(Y(M,N))^\times$
be the **Siegel units** (Kubert–Lang), modified by an auxiliary integer $c$ (Kato's ${}_cg_{a,b}$) to make them integral units.
Kato's **Beilinson elements** are the Steinberg symbols
$$
{}_{c,d}z_{M,N}=\{{}_cg_{1/M,0},\ {}_dg_{0,1/N}\}\in K_2(Y(M,N)),
$$
whose images under the étale Chern class $K_2\to H^2_{\mathrm{et}}(Y(M,N)\otimes\mathbb Z[1/MNp],\mathbb Z_p(2))$,
followed by the Hochschild–Serre projection to $H^1(\mathbb Z[\zeta_m,1/mp],\,H^1_{\mathrm{et}}(\bar Y,\mathbb Z_p(1)))$ and by the
Hecke projection to the $f$-isotypic quotient $T=T_pE$ (via a modular parametrisation), produce classes
$$
{}_{c,d}z_m\in H^1(\mathbb Z[\zeta_m,1/mp],\,T)\qquad(m\ge1,\ (cd,6mNp)=1).
$$
They satisfy the Euler-system norm relations of Rubin's book [Ru00, Def. 2.1.1]: for a prime $\ell\nmid mNp$,
$\operatorname{cor}_{\mathbb Q(\zeta_{m\ell})/\mathbb Q(\zeta_m)}({}_{c,d}z_{m\ell})=P_\ell(\operatorname{Fr}_\ell^{-1})\,{}_{c,d}z_m$
with $P_\ell(X)=\det(1-\operatorname{Fr}_\ell^{-1}X\mid T^*(1))=1-a_\ell\ell^{-1}X+\ell^{-1}X^2$ (Kato's normalisation of the
Euler factor differs by Tate twists; see [Ka04, §8] and [Ru00, §3.5]). Kato's Theorem 12.6 shows that the
$\Lambda$-module generated by these elements has finite index in the module $Z(f,T)$ of "zeta elements" (§1.2).
The construction is *uniform in the base*: the system lives over all abelian extensions $\mathbb Q(\zeta_m)$ of $\mathbb Q$;
this is the cyclotomic Euler system for $T$ in the sense of Rubin/Perrin-Riou.

### 1.2 The explicit reciprocity law

[THEOREM] (Kato [Ka04, Thm. 12.5(1)]; for weight $2$ see [Ru98, Thm. 7.1], [Sc98, Thm. 5.1.1].) Write
$D_{\mathrm{dR}}(V_pE)\supset D^0_{\mathrm{dR}}=\operatorname{Fil}^0=\mathbb Q_p\,\omega_E$ (cotangent space at $0$, $\omega_E$ a Néron
differential), and let
$$
\exp^*:H^1(\mathbb Q_p,V_pE)\longrightarrow D^0_{\mathrm{dR}}(V_pE)=\mathbb Q_p\,\omega_E
$$
be the Bloch–Kato dual exponential, whose kernel is $H^1_f(\mathbb Q_p,V_pE)=E(\mathbb Q_p)\hat\otimes\mathbb Q_p$.
There are "zeta elements" $\mathbf z_n=z_\gamma^{(p)}\in H^1(\mathbb Z[\zeta_{p^n},1/p],V_pE)$, norm-compatible in $n$
(depending linearly on a choice $\gamma\in V_{\mathbb Q}(f)$; for $E$ one normalises $\gamma$ so that
$\operatorname{per}(\gamma)^{\pm}=\Omega_E^{\pm}$), such that for every $n\ge0$ and every character $\chi$ of
$G_n=\operatorname{Gal}(\mathbb Q(\zeta_{p^n})/\mathbb Q)$,
$$
\sum_{\sigma\in G_n}\chi(\sigma)\,\exp^*\!\big(\operatorname{loc}_p(\sigma\,\mathbf z_n)\big)
=\frac{L_{\{p\}}(E,\chi^{\pm1},1)}{\Omega_E^{\chi(-1)}}\cdot\omega_E ,
$$
where $L_{\{p\}}$ is the $L$-function with the Euler factor at $p$ removed and the exponent $\pm1$ of $\chi$ is a
convention (Kato writes the character sum with $\chi(\sigma)\sigma$ and the value $L_{\{p\}}(f,\chi,r)$). For $\chi=1$, $n=0$:
$$
\exp^*(\operatorname{loc}_p\mathbf z)=\Big(1-\frac{a_p}{p}+\frac1p\Big)\frac{L(E,1)}{\Omega_E^+}\,\omega_E ,\qquad \mathbf z:=\mathbf z_0 .
$$
(Kato's statement is for general weight $k$, $1\le r\le k-1$, with the factor $(2\pi i)^{k-r-1}$ and sign
$(-1)^{k-r-1}\chi(-1)$; the elliptic-curve normalisation above is the one in [Ru98, Thm. 7.1] and [BKS19, (2.1.5)];
the analogue for tame characters — twists by Dirichlet characters of conductor prime to $p$ — is obtained by applying
Kato's theorem to the twisted forms.) Rationality of $\mathbf z$ (it lies in $H^1(\mathbb Z[1/p],T)\otimes\mathbb Q$) and integrality
under the big-image hypothesis (12.5.2) below are [Ka04, Thm. 12.5(4)].

**Consequence.** $\operatorname{loc}_p\mathbf z\notin H^1_f(\mathbb Q_p,V_pE)$ iff $L(E,1)\neq0$ (note
$1-a_p/p+1/p>0$ by Hasse). In particular $\mathbf z\neq 0$ when $L(E,1)\ne 0$. When $L(E,1)=0$, $\mathbf z$ lies in the
Bloch–Kato Selmer group $H^1_f(\mathbb Q,V_pE)$, a $\mathbb Q_p$-vector space of dimension $r_p(E/\mathbb Q)$ containing
$E(\mathbb Q)\otimes\mathbb Q_p$, and its non-vanishing is a *different* question (§1.4–1.5).

### 1.3 Consequences: finiteness when $L(E,1)\ne0$; $\Lambda$-torsion

[THEOREM] (Kato [Ka04, Thm. 14.2, Cor. 14.3]; Rubin [Ru98, Thm. 8.1].) Let $E/\mathbb Q$ be an elliptic curve
(modular by [BCDT]). If $L(E,1)\neq0$ then $E(\mathbb Q)$ and $\operatorname{Sha}(E/\mathbb Q)$ are finite. More generally, for $K/\mathbb Q$
finite abelian and $\chi$ a character of $\operatorname{Gal}(K/\mathbb Q)$ with $L(E,\chi,1)\neq0$, the $\chi$-parts of
$\operatorname{Sel}(K,E[p^\infty])$ and of $E(K)\otimes\mathbb C$ are finite (for every $p$). No hypothesis on $p$ or on $\bar\rho$ is needed
for finiteness. Kato's Thm. 14.2(1) also gives finiteness of the Selmer groups of the twists $V_pE(r)$, $r\neq1$.

[THEOREM] (Kato [Ka04, Thm. 14.5]; one inequality of the Tamagawa number conjecture at $p$.) Under the hypothesis
(12.5.2) — *there is a $\mathbb Z_p$-basis of $T$ for which the image of $\operatorname{Gal}(\bar{\mathbb Q}/\mathbb Q(\zeta_{p^\infty}))\to GL_2(\mathbb Z_p)$
contains $SL_2(\mathbb Z_p)$* — and $p\ne2$, if $L(E,1)\ne0$ then $H^2(\mathbb Z[1/p],T)$ is finite, $H^1(\mathbb Z[1/p],T)$ has rank one,
and $\#\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$ is bounded above in terms of $\operatorname{ord}_p(L(E,1)/\Omega_E^+)$ and explicit local terms
(we do not use the exact form; see loc. cit.). For $p\ge5$ non-CM, (12.5.2) is equivalent to (sur) (Serre's lemma
[Se68, IV-3.4, Lemma 3]). The reverse inequality — the full $p$-part of BSD in rank $0$ — is Skinner–Urban [SU14, Thm. 2]
(and [BCS25] without ramification hypotheses).

[THEOREM] (Kato [Ka04, Thm. 14.4], deduced from Cor. 14.3 and Rohrlich [Ro84].) $E(\mathbb Q(\zeta_{m^\infty}))$ is
finitely generated for every $m\ge1$; in particular $E(\mathbb Q_\infty)$ is finitely generated over the cyclotomic
$\mathbb Z_p$-extension. The analytic input is Rohrlich's theorem [Ro84]: $L(E,\chi,1)\neq0$ for all but finitely many
characters $\chi$ of $p$-power conductor.

[THEOREM] (Kato [Ka04, Thm. 12.4, Thm. 17.4].) Let $\mathbb H^i(T)=H^i_{\mathrm{Iw}}(\mathbb Q(\zeta_{p^\infty}),T)$ (Iwasawa
cohomology, $\Lambda=\mathbb Z_p[[\operatorname{Gal}(\mathbb Q(\zeta_{p^\infty})/\mathbb Q)]]$).
(1) $\mathbb H^2(T)$ is $\Lambda$-torsion; $\mathbb H^1(T)$ is torsion-free of $\Lambda\otimes\mathbb Q$-rank $1$, free of rank $1$
if $p\neq2$ and $E[p]$ is irreducible (Thm. 12.4).
(2) If $p$ is a prime of **good ordinary** reduction, $X:=\operatorname{Sel}_{p^\infty}(E/\mathbb Q(\zeta_{p^\infty}))^\vee$ is
$\Lambda$-torsion, and for every height-one prime $\mathfrak p\not\ni p$,
$\operatorname{length}_{\Lambda_\mathfrak p}(X_\mathfrak p)\le\operatorname{ord}_\mathfrak p(L_p(E))$ where $L_p(E)\in\Lambda\otimes\mathbb Q$ is
the Mazur–Swinnerton-Dyer $p$-adic $L$-function (Thm. 17.4(1),(2)); if moreover $p\neq 2$ and (12.5.2) holds, then
$L_p(E)\in\Lambda$ and the inequality holds for all height-one primes, i.e. $\operatorname{char}_\Lambda(X)\mid (L_p(E))$
in $\Lambda$ (Thm. 17.4(3)). Equality is the Iwasawa main conjecture, proved by Skinner–Urban [SU14, Thm. 1] for
$p\ge3$ good ordinary with $E[p]$ irreducible and $\bar\rho$ ramified at some $q\,\|\,N$, and by
Burungale–Castella–Skinner [BCS25] for $p\ge3$ good ordinary with $E[p]$ irreducible and no ramification hypothesis
(see `A-iwasawa-padic.md`).
(3) [Ka04, Thm. 18.4] ($p$-adic BSD inequality): for $p$ of good ordinary or multiplicative reduction,
$\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)\le \operatorname{ord}_{s=1}L_p(E,s)$ if $E$ is not a Tate curve at $p$
(i.e. not split multiplicative), and $\le\operatorname{ord}_{s=1}L_p(E,s)-1$ if it is (Kato's displayed statement is
"$\operatorname{corank}_{O_\lambda}\operatorname{Sel}(T)\le\operatorname{ord}_{s=k/2}L_{p\text{-adic},\alpha}(f)$", with the "$-1$" in the exceptional case
$\alpha=p^{(k-2)/2}$; he also states the rank consequence). For supersingular $p$ the analogous statements are due to
Kobayashi [Ko03] ($\pm$ Selmer groups) and, for the main conjecture, to Burungale–Skinner–Tian–Wan [BSTW24]
(semistable $E$, $a_p=0$).

Exact hypotheses summary for §1.3: finiteness results (Thm. 14.2/Cor. 14.3) need only $L(E,\chi,1)\neq0$; the
integral divisibility needs $p\ne2$ and (12.5.2), equivalent to (sur) for $p\ge5$; Thm. 17.4 needs good ordinary reduction.

### 1.4 Kato's Kolyvagin system and its order of vanishing

[THEOREM] (Mazur–Rubin [MR04, Thm. 3.2.4, Thm. 5.2.12]; Burungale–Castella–Grossi–Skinner [BCGS26, Thm. C, Cor. C].)
Let $\mathcal L_{\mathrm{Kato}}$ be the set of primes $\ell\nmid Np$ with $I_\ell:=(\ell-1,\,a_\ell-\ell-1)\subset p\mathbb Z_p$,
$\mathcal N_{\mathrm{Kato}}$ the squarefree products, $I_n=\sum_{\ell\mid n}I_\ell$. Kolyvagin's derivative
construction applied to $\{{}_{c,d}z_m\}$ yields a **Kolyvagin system**
$\kappa^{\mathrm{Kato}}=\{\kappa_n^{\mathrm{Kato}}\in H^1(\mathbb Q,T/I_nT)\}_{n\in\mathcal N_{\mathrm{Kato}}}$ for the canonical
Selmer structure $\mathcal F_{\mathrm{can}}$ (unramified away from $p$, no condition at $p$) [MR04, Thm. 3.2.4],
with $\kappa_1^{\mathrm{Kato}}=\mathbf z$. For $(T,\mathcal F_{\mathrm{can}})$ over $\mathbb Q$ the **core rank** is $1$
[MR04, §6.2, Prop. 6.2.2]. Mazur–Rubin's structure theorem [MR04, Thm. 5.2.12] gives, for any nonzero
$\kappa\in\mathbf{KS}(T,\mathcal F_{\mathrm{can}})$ and under the running hypotheses of [MR04, §3.5] (for $T=T_pE$ these
hold when $p\ge5$ and (sur) holds; [MR04, §6.2]):
$$
\operatorname{ord}(\kappa):=\min\{\nu(n):\kappa_n\neq0\}=\operatorname{corank}_{\mathbb Z_p}H^1_{\mathcal F_{\mathrm{can}}^*}(\mathbb Q,E[p^\infty])
=:r_{\mathrm{str}}(E/\mathbb Q),
$$
the corank of the **fine (strict) Selmer group** (local condition $0$ at $p$), and the elementary divisors of
$H^1_{\mathcal F^*_{\mathrm{can}}}(\mathbb Q,E[p^\infty])_{/\mathrm{div}}$ are $\partial^{(i)}(\kappa)-\partial^{(i+1)}(\kappa)$,
$i\ge\operatorname{ord}(\kappa)$, with $\partial^{(i)}=\min_{\nu(n)=i}\operatorname{ord}_p(\kappa_n)$.
The non-vanishing $\kappa^{\mathrm{Kato}}\ne0$ is [BCGS26, Thm. C]: it holds for $E$ non-CM, $p$ odd of good
ordinary reduction with $E(\mathbb Q_p)[p]=0$, provided the rational cyclotomic main conjecture holds — unconditionally
if $p>3$ and $E[p]$ is irreducible, or if $E$ has a rational $p$-isogeny with kernel $\mathbb F_p(\phi)$,
$\phi|_{G_p}\ne\mathbb 1,\omega$. Hence [BCGS26, Cor. C]: **$\operatorname{ord}(\kappa^{\mathrm{Kato}})=r_{\mathrm{str}}(E/\mathbb Q)$**
under these hypotheses. (Independently, Kim [Kim26, Thm. 1.4, Cor. 1.5] proves $\kappa^{\mathrm{Kato}}\ne0$ from the
main conjecture *localised at the augmentation ideal*, for $p\ge5$, (sur), Manin constant prime to $p$.)

**Consequence (bottom class in rank $\ge2$).** [THEOREM] (immediate from the above.) Let $E,p$ be as in
[BCGS26, Thm. C] with $\kappa^{\mathrm{Kato}}\neq0$. If $\operatorname{rank}E(\mathbb Q)\ge1$ then $r_{\mathrm{str}}(E/\mathbb Q)=r_p(E/\mathbb Q)-1$
(a non-torsion rational point has infinite order in $E(\mathbb Q_p)\cong\mathbb Z_p\times(\text{finite})$, so the localisation
$\operatorname{Sel}_{p^\infty}(E/\mathbb Q)\to E(\mathbb Q_p)\otimes\mathbb Q_p/\mathbb Z_p$ has corank-one image). Hence
$$
\operatorname{rank}E(\mathbb Q)\ge2\ \Longrightarrow\ \mathbf z=\kappa_1^{\mathrm{Kato}}=0\ \text{ and }\ \kappa_\ell^{\mathrm{Kato}}=0\ \forall\ell,
\qquad \operatorname{ord}(\kappa^{\mathrm{Kato}})=r_p(E/\mathbb Q)-1\ \ge 1 .
$$
(Here $H^1(\mathbb Q,T)$ is torsion-free since $E(\mathbb Q)[p]=0$, so "$=0$" is literal.) In particular for a curve of rank
$2$: $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite $\iff\operatorname{ord}(\kappa^{\mathrm{Kato}})=1\iff\kappa^{\mathrm{Kato}}_{\ell}\neq0$
for some $\ell\in\mathcal L_{\mathrm{Kato}}$.

### 1.5 Perrin-Riou's conjecture and its generalisation; where the Kato line stops

[CONJECTURE]/[THEOREM] (Perrin-Riou 1993 [PR93, §3.3]; proved by Bertolini–Darmon–Venerucci [BDV22] for good
reduction, Büyükboduk–Pollack–Sasaki [BPS18] (good ordinary, via a critical-slope $p$-adic Gross–Zagier formula),
Venerucci [Ve16] (split multiplicative), Burungale–Skinner–Tian–Wan [BSTW24, §7].) If $r_{\mathrm{an}}(E)=1$
then $\mathbf z\in E(\mathbb Q)\otimes\mathbb Q_p$ and
$\log_{\omega}(\mathbf z)=\dfrac{L'_S(E,1)}{\Omega^+\,\langle x,x\rangle_\infty}\log_\omega(x)^2$
for $x$ a generator of $E(\mathbb Q)/\mathrm{tors}$ (formulation of [BKS19, Thm. 1.4]); in particular $\mathbf z\neq0$ and
$\mathbf z$ is a nonzero multiple of a Heegner point.

[CONJECTURE] (Burns–Kurihara–Sano, "Generalized Perrin-Riou Conjecture" [BKS19, Conj. 1.1, Conj. 1.5].) Let
$r=\operatorname{rank}E(\mathbb Q)>0$, $E(\mathbb Q)[p]=0$, $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ finite, $F/\mathbb Q$ real abelian with group $G$,
$I\subset\mathbb Z_p[G]$ the augmentation ideal. Then (i) the "Darmon-type" element
$N_{F/\mathbb Q}(z_F)=\sum_\sigma\sigma(z_F)\otimes\sigma^{-1}$ lies in $H^1(\mathcal O_{F,S},T)\otimes I^{r-1}$; (ii) the
Birch–Swinnerton-Dyer element $\eta^{\mathrm{BSD}}$ (defined from the leading term of $L(E,s)$) lies in
$\bigwedge^r H^1(\mathbb Z_S,T)$; (iii) the image of $N_{F/\mathbb Q}(z_F)$ in $H^1\otimes I^{r-1}/I^r$ equals
$\mathrm{Boc}_F(\eta^{\mathrm{BSD}})$ for a canonical Bockstein regulator map
$\mathrm{Boc}_F:\bigwedge^r H^1(\mathbb Z_S,T)\to H^1(\mathbb Z_S,T)\otimes I^{r-1}/I^r$. Along the cyclotomic tower this
reads $\kappa_\infty=\dfrac{L^{(r)}_S(E,1)}{\Omega^+R_\infty}\cdot R^{\mathrm{Boc}}_\omega$ [BKS19, Conj. 1.5]. Part (i) is a
theorem under $p>3$, finiteness of $\operatorname{Sha}(E/F)[p^\infty]$ and $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$, image of $\rho_{E,p}\supseteq SL_2(\mathbb Z_p)$,
and $E(\mathbb Q_\ell)[p]=0$ for $\ell\in S$ [BKS19, Thm. 1.3]; (iii) is open for $r\ge2$.

**Where the line stops.** For $r_{\mathrm{an}}\ge2$: $L(E,1)=0$ forces (by §1.2) $\operatorname{loc}_p\mathbf z\in H^1_f$; and if
$\operatorname{rank}E(\mathbb Q)\ge2$ then $\mathbf z=0$ outright (§1.4). Every Euler-system bound on $\operatorname{Sel}$ is an
upper bound *by the index of the bottom class*; with $\kappa_1=\kappa_\ell=0$ the first informative class is
$\kappa^{\mathrm{Kato}}_{\ell_1\ell_2}$, and its non-vanishing is (Mazur–Rubin) *equivalent* to $r_{\mathrm{str}}\le 1$, i.e.
to finiteness of $\operatorname{Sha}[p^\infty]$ when $\operatorname{rank}=2$. No formula expresses $\kappa^{\mathrm{Kato}}_{\ell_1\ell_2}$, or
the Kurihara number $\tilde\delta_{\ell_1\ell_2}$ that is its image under the (refined) dual exponential (§3.4), in
terms of $L''(E,1)$. This is [GAP B.1] (§7).

---

## 2. Heegner points, Gross–Zagier, Kolyvagin

### 2.1 Heegner points and the Gross–Zagier formula

Assume (Heeg). Fix $\mathfrak N\subset\mathcal O_K$ with $\mathcal O_K/\mathfrak N\cong\mathbb Z/N$; for $n\ge1$ prime to $N$ let
$\mathcal O_n=\mathbb Z+n\mathcal O_K$, $x_n\in X_0(N)(K[n])$ the point representing $\mathbb C/\mathcal O_n\to\mathbb C/(\mathfrak N\cap\mathcal O_n)^{-1}$, and
$y_n=\pi(x_n)\in E(K[n])$ for a fixed modular parametrisation $\pi:X_0(N)\to E$ (Manin constant $c_\pi$, degree $\deg\pi$).
Put $P_K=\operatorname{Tr}_{K[1]/K}(y_1)\in E(K)$.

[THEOREM] (Gross–Zagier [GZ86, Thm. I.6.3, (6.4)] for $D_K$ odd; the parity restriction was removed by
S. Zhang [Zh01] and Yuan–Zhang–Zhang [YZZ13]; explicit constants in Cai–Shu–Tian [CST14, Thm. 1.1].)
For $\chi$ a character of $\operatorname{Gal}(K[1]/K)$ and $c_\chi=\sum_\sigma\chi^{-1}(\sigma)\,[x_1-\infty]^\sigma\in J_0(N)(K[1])\otimes\mathbb C$,
with $c_{\chi,f}$ its $f$-isotypic component,
$$
L'(f,\chi,1)=\frac{8\pi^2(f,f)}{h_K\,u_K^2\,|D_K|^{1/2}}\ \hat h_{K[1]}(c_{\chi,f}),
\qquad (f,f)=\iint_{\Gamma_0(N)\backslash\mathfrak H}|f|^2\,dx\,dy,
$$
where $\hat h_{K[1]}$ is the Néron–Tate height on $J_0(N)$ over $K[1]$, and heights over $K[1],K,\mathbb Q$ are related by
$\langle\,,\rangle_{K[1]}=h_K\langle\,,\rangle_K=2h_K\langle\,,\rangle_\mathbb Q$ [GZ86, (6.4)]. Here $L(f,\chi,s)$ is the
Rankin–Selberg $L$-function of $f$ against the theta series of $\chi$, so $L(f,\mathbb 1,s)=L(E/K,s)=L(E,s)L(E^K,s)$.
Passing to $E$ through $\pi$ (using $\hat h_E(\pi_*y)=\deg\pi\cdot\hat h_J(y_f)$ on the $f$-part and
$\|\omega_E\|^2:=\int_{E(\mathbb C)}|\omega_E\wedge\bar\omega_E|=c_\pi^2\,8\pi^2(f,f)/\deg\pi$) gives the form quoted in
[GZ86, §V.2] and in the literature:
$$
\boxed{\ L'(E/K,1)=\frac{\|\omega_E\|^2}{c_\pi^2\,u_K^2\,|D_K|^{1/2}}\ \hat h_K(P_K)\ }\qquad(\hat h_K=\text{Néron–Tate height over }K).
$$
Since $\hat h_K$ is positive definite on $E(K)\otimes\mathbb R$: **$L'(E/K,1)\neq0\iff P_K$ is non-torsion.**
For ring class characters: [CST14, Thm. 1.1]: if $\chi$ is a primitive character of $\operatorname{Pic}(\mathcal O_c)$ with $(c,N)=1$,
no prime of $N$ inert in $K$, primes with $\ell^2\mid N$ split, and $\chi([\mathfrak p])=a_p$ for $p\mid(N,D_K)$, then
$$
L'(1,E,\chi)=2^{-\mu(N,D_K)}\frac{8\pi^2(f,f)}{u_c^2\,|D_Kc^2|^{1/2}}\cdot\frac{\hat h_K\big(P^0_\chi\big)}{\deg\pi},
\qquad P^0_\chi=\sum_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O_c)}\pi(x_{\mathfrak a})\otimes\chi([\mathfrak a])\in E(K[c])\otimes\mathbb C,
$$
$u_c=[\mathcal O_c^\times:\mathbb Z^\times]$, $\mu(N,D_K)=\#\{\ell\mid(N,D_K)\}$, $\hat h_K$ extended Hermitian-ly. Under (Heeg),
$\mu=0$. Hence **$L'(E/K,\chi,1)\neq0\iff e_{\chi^{\pm1}}(y_c)\neq0$ in $E(K[c])\otimes\mathbb C$**, where
$e_\chi=\frac1{|\mathcal G_c|}\sum_\sigma\chi^{-1}(\sigma)\sigma$ (the sign ambiguity is harmless: $L(E/K,\chi,s)=L(E/K,\chi^{-1},s)$
because $\chi^{-1}=\chi\circ\tau$ for ring class characters and $f$ has real coefficients).

Root numbers under (Heeg): $w(E^K)=w(E)\chi_K(-N)=-w(E)$ (since $\chi_K(\ell)=1$ for $\ell\mid N$ and $\chi_K(-1)=-1$),
hence $w(E/K)=w(E)w(E^K)=-1$ and $\operatorname{ord}_{s=1}L(E/K,s)$ is odd [GZ86, Introduction].

### 2.2 Kolyvagin's derived classes

[THEOREM/DEFINITION] (Kolyvagin [Ko90], [Ko91, §1]; Gross [Gr91, §§3–5]; Zhang [Zh14, §3.7].) Let $p$ be odd
with (sur) and $p\nmid ND_K$; then $E(K[n])[p]=0$ for all $n\in\Lambda$ [Gr91, Lemma 4.3]. Fix generators $\sigma_\ell$ of
$G_\ell$ and put
$$
D_\ell=\sum_{i=1}^{\ell}i\,\sigma_\ell^i\in\mathbb Z[G_\ell],\qquad D_n=\prod_{\ell\mid n}D_\ell,\qquad
(\sigma_\ell-1)D_\ell=(\ell+1)-\operatorname{Tr}_{G_\ell}.
$$
Fix representatives $\mathcal S\subset\mathcal G_n$ of $\mathcal G_n/G_n\cong\operatorname{Gal}(K[1]/K)$ and set
$P_n=P_n^{\mathcal S}:=\sum_{\sigma\in\mathcal S}\sigma D_ny_n\in E(K[n])$. Using the norm relations
$\operatorname{Tr}_{K[n\ell]/K[n]}y_{n\ell}=a_\ell\,y_n$ and the congruence $\operatorname{Frob}_\lambda\equiv\tau$ on $E[p^M]$ at the
prime $\lambda\mid\ell$ of $K$ [Gr91, Prop. 3.7], one checks that for $M\le M(n)$ the image of $P_n$ in
$E(K[n])/p^M$ is $\mathcal G_n$-invariant and independent of $\mathcal S$; since $E[p^M]^{G_{K[n]}}=0$, restriction
$H^1(K,E[p^M])\to H^1(K[n],E[p^M])^{\mathcal G_n}$ is an isomorphism, and
$$
c_M(n)\in H^1(K,E[p^M])\quad\text{is the unique class with}\quad \operatorname{res}_{K[n]}c_M(n)=\delta(P_n)\in E(K[n])/p^M\hookrightarrow H^1(K[n],E[p^M]).
$$
$c_M(1)$ is the Kummer image of $P_K$. Sign: [Gr91, Prop. 5.4], [BD96, Prop. 2.6], [Zh14, (3.24)]:
$$
c_M(n)\in H^1(K,E[p^M])^{\epsilon_{\nu(n)}},\qquad \epsilon_\nu:=w(E)\cdot(-1)^{\nu+1}.
$$
(So $\tau P_K\equiv -w(E)P_K$ mod torsion, and each Kolyvagin prime flips the eigenspace.) Local properties
[Gr91, §6]: $c_M(n)$ satisfies the Selmer local condition at every place $v\nmid n$, and at $\lambda\mid\ell\mid n$ its singular
part is determined by the finite part of $c_M(n/\ell)$ at $\lambda$ ("finite–singular relation"). Howard [Ho04, §1] recast
this as: **$\{c_M(n)\}$ is a Kolyvagin system for $(T,\mathcal F_{\mathrm{cl}},\Lambda)$ over $K$** in a modified
Mazur–Rubin sense (transverse conditions at $\lambda\mid n$, self-dual structure, complex-conjugation action). Kolyvagin
[Ko91] proves $\mathcal M_r\ge\mathcal M_{r+1}\ge0$; thus $\mathcal M_r=\infty$ exactly for $r<\nu_\infty$.

### 2.3 Kolyvagin's theorem (rank one)

[THEOREM] (Kolyvagin [Ko88], [Ko90]; Gross–Zagier [GZ86]; auxiliary nonvanishing: Bump–Friedberg–Hoffstein
[BFH90], Murty–Murty [MM91], Waldspurger.) Let $E/\mathbb Q$, $K$ with (Heeg), $D_K\notin\{-3,-4\}$. If $P_K$ is
non-torsion (equivalently $L'(E/K,1)\ne0$), then $\operatorname{rank}E(K)=1$ and $\operatorname{Sha}(E/K)$ is finite; moreover for
$p$ odd with $\rho_{E,p}$ surjective onto $GL_2(\mathbb Z_p)$ and $p\nmid ND_K$,
$\#\operatorname{Sha}(E/K)[p^\infty]\le p^{2\mathcal M_0}$ where $p^{\mathcal M_0}=[E(K)\otimes\mathbb Z_p:\mathbb Z_pP_K]$
(Kolyvagin; the structure of $\operatorname{Sha}(E/K)[p^\infty]$ is in [Ko91b] and §2.4). Howard's Kolyvagin-system
proof [Ho04, Thm. A]: for $p$ odd, $p,D_K,N$ pairwise coprime and $G_K\to\operatorname{Aut}_{\mathbb Z_p}(T)$ surjective, if
$\kappa_1\neq0$ then $S_p(E/K)$ (the compact Selmer group) is free of rank one over $\mathbb Z_p$ and there is a finite
$\mathbb Z_p$-module $M$ with $\operatorname{Sel}_{p^\infty}(E/K)\cong\mathbb Q_p/\mathbb Z_p\oplus M\oplus M$ and
$\operatorname{length}_{\mathbb Z_p}M\le\operatorname{length}_{\mathbb Z_p}(S_p(E/K)/\mathbb Z_p\kappa_1)$ (statement checked against the published text).
Over $\mathbb Q$: if $r_{\mathrm{an}}(E)=1$ choose $K$ with (Heeg) and $L(E^K,1)\neq0$ ([BFH90], [MM91]; then
$L'(E/K,1)=L'(E,1)L(E^K,1)\neq0$), get $\operatorname{rank}E(K)=1$, $\operatorname{Sha}(E/K)$ finite, and $E^K(\mathbb Q)$ finite (Kolyvagin or
Kato), so $\operatorname{rank}E(\mathbb Q)=1$, $\operatorname{Sha}(E/\mathbb Q)$ finite. If $r_{\mathrm{an}}(E)=0$ use Kato (§1.3) or choose $K$ with
$L'(E^K,1)\ne0$ ([BFH90], [MM91], [Iw90]).

### 2.4 Kolyvagin's structure theorem

We state Kolyvagin's theorem from "On the structure of Selmer groups" [Ko91] (Thms. 1 and 4 there; in the
transcription at wstein.org they are Thm. 1.2 and Thm. 2.3), in the $\pm$ convention, using the restatements
[Zh14, Thm. 1.2, Thm. 11.2, Remark 18] which we checked against Kolyvagin's text. Kolyvagin works with primes
$\ell\in B(E)$: odd, $\ell\nmid\operatorname{disc}\operatorname{End}(E)$, and $\rho_{E,\ell}:G_\mathbb Q\to\operatorname{Aut}_{\mathcal O}T_\ell E$ surjective
(for non-CM $E$ and $\ell\ge5$ this is (sur), by Serre's lemma); he assumes $0>D_K\equiv\square\bmod 4N$, $D_K\ne-3,-4$.

[THEOREM, conditional on Conjecture A] (Kolyvagin 1991.) Let $p$ be odd with $\rho_{E,p}$ surjective onto $GL_2(\mathbb Z_p)$,
$p\nmid ND_K$, $K$ with (Heeg), $D_K\ne-3,-4$. Assume **Kolyvagin's Conjecture A** for $(E,K,p)$: $\kappa^\infty\ne0$ (equivalently
$\mathcal M_\infty<\infty$, equivalently $\nu_\infty<\infty$) — a theorem for the $p$ listed in §2.5. Put $\nu=\nu_\infty$ and
$\epsilon_\nu=w(E)(-1)^{\nu+1}$. Then:

1. $\mathcal M_0\ge\mathcal M_1\ge\cdots\ge\mathcal M_\infty\ge0$, and $\mathcal M_r<\infty\iff r\ge\nu$.
2. (Ranks) $r_p^{\epsilon_\nu}(E/K)=\nu+1$, and $0\le\nu-r_p^{-\epsilon_\nu}(E/K)\equiv0\pmod 2$. In particular
   $\nu=\max\{r_p^+,r_p^-\}-1$ and $r_p^++r_p^-$ is odd (so $p$-parity for $E/K$ follows; [Zh14, Remark 1]).
3. (Structure, dominant eigenspace) $\operatorname{Sel}_{p^\infty}(E/K)^{\epsilon_\nu}_{/\mathrm{div}}\cong\bigoplus_{i\ge1}
   \big(\mathbb Z/p^{\mathcal M_{\nu+2i-1}-\mathcal M_{\nu+2i}}\big)^{2}$.
4. (Structure, other eigenspace) $\operatorname{Sel}_{p^\infty}(E/K)^{-\epsilon_\nu}_{/\mathrm{div}}\cong
   \bigoplus_{i=1}^{\nu-r_p^{-\epsilon_\nu}}\mathbb Z/p^{a_i}\ \oplus\ \bigoplus_{i\ge1}\big(\mathbb Z/p^{\mathcal M_{\nu+2i-2}-\mathcal M_{\nu+2i-1}}\big)^2$,
   where the first $\nu-r_p^{-\epsilon_\nu}$ (an even number of) invariants $a_i$ are determined by Kolyvagin in terms of
   his local characters (Thm. 2.1 of the transcription) but not by the $\mathcal M_r$ alone.
5. Hence $\#\operatorname{Sel}_{p^\infty}(E/K)_{/\mathrm{div}}\ge p^{2(\mathcal M_\nu-\mathcal M_\infty)}$ with equality iff
   $\nu=r_p^{-\epsilon_\nu}$ [Zh14, Remark 18].
6. (Generation) $\operatorname{Sel}_{p^\infty}(E/K)^{\epsilon_\nu}$ is contained in the subgroup of $H^1(K,E[p^\infty])$ generated by
   all $c_M(n)$ [Zh14, Thm. 11.2(ii)], and Kolyvagin's Thm. 2 (transcription Thm. 2.2) exhibits $\nu+1$ classes
   $c_{M}(n_i)$, $\nu(n_i)=\nu$, spanning $(\mathbb Z/p^M)^{\nu+1}\subset\operatorname{Sel}_{p^M}(E/K)^{\epsilon_\nu}$.

When $\nu=0$ this is the rank-one theorem of §2.3 together with $\#\operatorname{Sha}(E/K)[p^\infty]=p^{2(\mathcal M_0-\mathcal M_\infty)}$
[Zh14, proof of Thm. 10.2], which is the $p$-part of BSD for $E/K$ once $\mathcal M_\infty=0$ (Zhang) or, in general,
once $\mathcal M_\infty=\sum_{\ell\mid N}\operatorname{ord}_p c_\ell$ (BCGS, §2.5).

### 2.5 Kolyvagin's conjectures and their status (through 2026)

Kolyvagin's own conjectures [Ko91] (numbering of the transcription; "$T$" is his set of classes, $\ell$ his prime):

- **Conjecture 1.1 (= Conjecture A).** $T\neq\{0\}$, i.e. $\kappa^\infty\ne0$ ($\mathcal M_\infty<\infty$), for every
  $\ell\in B(E)$ and every Heegner $K$.
- **Conjecture 2.5.** For all $\ell$ (not only $\ell\in B(E)$), $\{\tau_{\lambda,n}\}$ is a "strong nonzero system".
- **Conjecture 2.6.** $\mathcal M_\infty\ne0$ for only finitely many $\ell\in B(E)$.
- **Conjecture 2.7.** There exist $\nu\in\{0,1\}$ and a subgroup $V\subset(E(K)/E(K)_{\mathrm{tor}})^{\nu}$ (his eigenspace
  labelling) with $1\le\operatorname{rank}V\equiv\nu\pmod 2$ such that for all sufficiently large $k$ and all $n$, the classes
  $\tau_{\lambda,n}$ with $\lambda\in\Lambda^{a}$, $a=\operatorname{rank}V-1$, generate exactly $V\bmod \ell^n$ inside $E(K)/\ell^n$.
  Kolyvagin proves: Conjecture 2.7 $\iff$ [$\{\tau\}$ is a strong nonzero system **and** $\operatorname{Sha}(\mathbb Q,E^{(f+1)})_{\ell^\infty}$
  is finite], and that it implies $\operatorname{rank}E^\nu(\mathbb Q)=\operatorname{rank}V$, $V\otimes\mathbb Z_\ell=\ell^{m_f}(E^\nu(\mathbb Q)\otimes\mathbb Z_\ell)$,
  $\#\operatorname{Sha}(\mathbb Q,E^\nu)_{\ell^\infty}\mid\ell^{2m_f}$.
- **Conjecture 2.8.** Conjecture 2.7 holds for all $\ell$ with a **universal $V$ independent of $\ell$**. Kolyvagin proves:
  Conjecture 2.8 $\iff$ [Conjectures 2.5 and 2.6, **$f+1$ is independent of $\ell$**, $\operatorname{Sha}(\mathbb Q,E^{(f+1)})$ is finite,
  and $\operatorname{inv}_{f+1-r^{1-\nu}}\operatorname{Sha}^{1-\nu}\ne0$ for only finitely many $\ell\in B(E)$].

Kolyvagin then discusses (last paragraph of [Ko91]) exactly the scenario of §4: "$g>1$ … $P_1$ has finite order by the
formula of Gross and Zagier … $\operatorname{rank}E(\mathbb Q)=\operatorname{rank}V$ and $\operatorname{Sha}(\mathbb Q,E)_{\ell^\infty}$ is finite" under his
Conjecture 2.7. We will not claim novelty for anything contained in that paragraph. (The text of the Grothendieck
Festschrift article [Ko90] was not accessible to us online; Zhang [Zh14, Conj. 3.2] and [BCGS26] attribute Conjecture A to
[Ko91], and [Ko91, §1] states that the theory of [Ko90] "is valid under a more general assumption which is, hypothetically,
always true" — namely Conjecture A.)

Status of Conjecture A:

- [THEOREM] (W. Zhang [Zh14, Thm. 1.1, Thm. 9.3].) $E/\mathbb Q$ of conductor $N$, $p\ge5$ **good ordinary**, $p\nmid D_KN$,
  $(D_K,N)=1$, $N^-$ squarefree with an even number of prime factors, (sur), and **Hypothesis ♠**: (1) $\bar\rho$ is ramified at
  every $\ell\,\|\,N^+$ and at every $\ell\mid N^-$ with $\ell\equiv\pm1\pmod p$; (2) if $N$ is not squarefree then
  $\#\operatorname{Ram}(\bar\rho)\ge1$ and either $\operatorname{Ram}(\bar\rho)$ contains a prime $\ell\,\|\,N^-$ or there are at least two primes
  $\ell\,\|\,N^+$. Then $c_1(n)\neq0$ for some $n$; i.e. **$\mathcal M_\infty=0$** (indivisibility). Multiplicative $p\ge5$:
  Skinner–Zhang [SZ14].
- [THEOREM] (Sweeting [Sw20, Thm. A = Cor. 8.3.7].) $f$ weight-2 newform, $\wp\mid p$, $K$ with the generalised Heegner
  hypothesis ($\nu(N^-)$ even), (unr): $p\nmid 2N\operatorname{disc}K$, (sclr): the image of $G_K$ on $T_f$ contains a nonzero
  scalar, and **Condition ♦**: $\bar T_f$ absolutely irreducible (and, if $p=3$, not induced from $G_{\mathbb Q(\sqrt{-3})}$); if
  $p$ is inert in $K$ or $a_p$ is not a $\wp$-unit, some prime $\ell\,\|\,N$ exists; if $a_p$ is not a $\wp$-unit, either such
  an $\ell$ can be chosen with $A_f$ of non-split toric reduction at $\ell$, or the image of Galois on $T_f$ contains a
  conjugate of $SL_2(\mathbb Z_p)$. Then some $c(m)\in H^1(K,T_f/I_m)$ is nonzero (Conjecture A; **not** the mod-$\wp$
  indivisibility, which fails in general). Allows $p=3$, supersingular $p$, $p$ inert in $K$; no ramification hypothesis on
  $\bar\rho$. Also [Sw20, Cor. B]: $\max\{r^+,r^-\}=\nu+1$, $r^++r^-$ odd, larger eigenspace of sign $(-1)^{\nu+1}\epsilon_f$;
  [Sw20, Thm. D]: definite analogue ($\nu(N^-)$ odd) with elements $\lambda(m)\in\mathcal O/I_m$ and
  $\min\{\nu(m):\lambda(m)\ne0\}=r^++r^-$. (arXiv:2012.11771v3; not located in a journal as of 2026-09-11.)
- [THEOREM] (Burungale–Castella–Grossi–Skinner [BCGS26, Thm. A].) $p$ odd of good ordinary reduction, **$p$ split in $K$**,
  (Heeg), (disc), (tor): $E(K)[p]=0$; if the rational anticyclotomic main conjecture (their Conj. 1.2.10) holds then
  $\kappa^{\mathrm{Heeg}}\ne0$. Unconditionally in both cases: (a) $E$ has a rational $p$-isogeny with kernel $\mathbb F_p(\phi)$,
  $\phi|_{G_p}\ne\mathbb 1,\omega$ (Eisenstein primes; via [CGS25]); (b) **$p>3$ and $E[p]$ irreducible** (via [BCS25]). No
  ramification hypothesis; Cor. A: $\operatorname{ord}(\kappa^{\mathrm{Heeg}})=\max\{r(E/K)^+,r(E/K)^-\}-1$ in this generality.
- [THEOREM] (Refined conjecture; W. Zhang's conjecture [Zh14b, Conj. 4.5], proved in [BCGS26, Thm. B].) With $(E,p,K)$
  as in Thm. A, $p>3$, (sur), the integral anticyclotomic main conjecture (known for $p>3$ with (sur), [BCGS26, Thm. 1.2.13]),
  and $\pi$ $p$-optimal: $\ \mathcal M_\infty=\sum_{\ell\mid N}\operatorname{ord}_p(c_\ell)$. Lower bounds $\mathcal M_\infty\ge\operatorname{ord}_p c_\ell$
  were Jetchev's [Je08]. So Kolyvagin's Conjecture 2.6 holds along good ordinary primes split in $K$ (and along all
  good ordinary $p\ge5$ satisfying ♠, by Zhang); it is open along supersingular primes, where only $\mathcal M_\infty<\infty$
  is known (Sweeting).
- [THEOREM] (Kim [Kim24, Thm. 2.1 (HPMC), Cor. 2.2].) For $p\ge5$, (sur), good ordinary, $\kappa^{\mathrm{Heeg}}\neq0$ iff the
  Heegner-point main conjecture of Perrin-Riou holds *localised at the augmentation ideal*.
- Higher weight analogues: Longo–Pati–Vigni [LPV24] (ordinary, $p>k+1$), Da Ronche [DR25] (non-ordinary, assuming a
  Selmer rank one hypothesis); a conditional route via Kato's main conjecture for non-ordinary forms is announced in
  [CLW26]. These do not bear on rank $\ge2$.

---

## 3. Mazur–Rubin Kolyvagin systems, core rank, and the rank-2 question

### 3.1 Selmer structures and core rank

[THEOREM] (Mazur–Rubin [MR04, Ch. 2–5]; [MR16, Def. 3.4, Thm. 5.4, Prop. 5.9].) For $T$ free of finite rank over a
principal Artinian local ring or a DVR $R$ with $G_K$-action, a Selmer structure $\mathcal F$ is a choice of local
conditions $H^1_{\mathcal F}(K_v,T)\subset H^1(K_v,T)$ for $v$ in a finite set, unramified elsewhere; $\mathcal F^*$ is the
orthogonal complement structure on $T^*=\operatorname{Hom}(T,\mu_{p^\infty})$. The **core rank** $\chi(T,\mathcal F)$ is the
common rank of the free parts of the "core" Selmer modules $H^1_{\mathcal F(n)}(K,T)$ obtained by modifying $\mathcal F$ at
Kolyvagin primes. For an abelian variety $A/K$ of dimension $d$ and the usual Selmer structure on $T_pA$ with the
local conditions above $p$ relaxed,
$$
\chi(T_pA,\mathcal F)=d\,[K:\mathbb Q]
$$
[MR16, Prop. 5.9]. Thus **$(T_pE,\mathcal F_{\mathrm{can}})$ has core rank $1$ over $\mathbb Q$ and core rank $2$ over an
imaginary quadratic $K$** (for $K=\mathbb Q$ one can also read this off Wiles' Euler characteristic formula for the canonical
structure: $\dim\bar T-\dim\bar T^{\tau=1}+\operatorname{corank}H^0(\mathbb Q_p,T^*)=2-1+0=1$; cf. [MR04, Prop. 6.2.2]).

### 3.2 Core rank one: Kolyvagin systems control Selmer groups

[THEOREM] ([MR04, Thm. 4.4.1, Thm. 5.2.12].) Assume the running hypotheses of [MR04, §3.5] and $\chi(T,\mathcal F)=1$.
Then the $\mathbb Z_p$-module $\mathbf{KS}(T,\mathcal F,\mathcal P)$ of Kolyvagin systems is free of rank one, generated by a
*primitive* system; for a nonzero $\kappa$: $\operatorname{ord}(\kappa)=\operatorname{corank}H^1_{\mathcal F^*}(K,T^*)$, the elementary divisors
of $H^1_{\mathcal F^*}(K,T^*)_{/\mathrm{div}}$ are $\partial^{(i)}(\kappa)-\partial^{(i+1)}(\kappa)$ ($i\ge\operatorname{ord}\kappa$), and
$\kappa$ is primitive iff $\partial^{(\infty)}(\kappa)=0$. If $\kappa_1\neq0$ then $H^1_{\mathcal F}(K,T)$ is free of rank one
and $\operatorname{length}H^1_{\mathcal F^*}(K,T^*)\le\operatorname{length}(H^1_{\mathcal F}(K,T)/R\kappa_1)$, with equality iff $\kappa$ is primitive.
The bridge to $L$-values is [MR04, Thm. 3.2.4]: an Euler system yields a Kolyvagin system with $\kappa_1$ = bottom class.

For Heegner points the relevant structure on $T$ over $K$ is *self-dual with complex conjugation*, and the theory is
Howard's [Ho04] (the two eigenspaces play the roles of $T$ and $T^*$; the core rank is $1$ in the anticyclotomic
direction: $H^1_{\mathcal F_\Lambda}(K,\mathbf T)$ is torsion-free of $\Lambda^{\mathrm{ac}}$-rank one [Ho04, Thm. B]).

### 3.3 Higher core rank

[THEOREM] (Mazur–Rubin [MR16] (JTNB 28 (2016), arXiv:1312.4052); Büyükboduk [Bu10]; Burns–Sano [BS21]; Burns–Sakamoto–Sano
[BSS19]; Sakamoto.) For core rank $r\ge2$ Mazur–Rubin define Kolyvagin systems of rank $r$ (classes in $\bigwedge^r$ of
the modified Selmer groups) and **Stark systems**; under (H.1)–(H.6) both modules are free of rank one, a Stark system
controls the elementary divisors of $H^1_{\mathcal F^*}(K,T^*)$ [MR16, Thm. 8.9, Thm. 13.4], and Stark systems correspond
to the *stub* Kolyvagin systems [MR16, Thm. 12.4]; for $r=1$ every Kolyvagin system is stub [MR04, Thm. 4.4.1], for
$r\ge2$ not necessarily, which is why exterior powers had to be replaced by **exterior biduals**
$\bigcap^r X=\big(\bigwedge^r X^*\big)^*$ [BS21, §2] to obtain a theory in which higher rank Euler systems give higher rank
Kolyvagin systems that do control Selmer modules; the canonical "higher Kolyvagin derivative" homomorphism
$\mathrm{ES}_r\to\mathbf{KS}_r$ conjectured by Mazur–Rubin is constructed in [BSS19] (for representations free over a
Gorenstein order). Büyükboduk [Bu10] passes from rank-$r$ Euler systems to rank-one Kolyvagin systems via Rubin's
choice of $r-1$ homomorphisms and shows the resulting bounds are sharp under suitable hypotheses. Mazur–Rubin write
[MR16, Introduction]: "We expect that when $r>1$ there is still a connection between Euler systems … and Stark and
Kolyvagin systems, but this connection is still mysterious"; the only motivic examples of higher rank Euler systems
are Rubin–Stark elements (conjectural) and the "vertical determinantal systems" of [BS21, Thm. 2.17].

### 3.4 What a "rank-2 Euler system for $T_pE$ over $\mathbb Q$" would have to be

We work this out precisely, because it is the point where the method's rank-limitation becomes a definite statement.

**(a) Core rank is $1$, so "rank 2" is not a Mazur–Rubin/Burns–Sano rank.** Over $\mathbb Q$, along the cyclotomic
tower, $H^1(\mathbb Z[\zeta_m,1/p],T)$ is generically of $\mathbb Z_p[G_m]$-rank one (Kato's Thm. 12.4(2) for the
$p$-power tower; Euler characteristic in general), so $\bigwedge^2_{\mathbb Z_p[G_m]}H^1(\mathbb Q(\zeta_m),T)$ is a torsion module
for generic $m$. **A norm-compatible system of classes in second exterior powers over the cyclotomic tower is
identically torsion** and cannot interpolate anything. Rank $2$ occurs only *at the bottom*, where the rank of
$H^1_f(\mathbb Q,V)$ jumps from the generic value $1$ to $r_{\mathrm{alg}}=2$.

**(b) The honest rank-1 formulation.** What the theory of §3.2 needs in rank $2$ is *not* a new system but the first
*informative* derived classes of the existing one: on the Kato side $\kappa^{\mathrm{Kato}}_{\ell_1\ell_2}$ over $\mathbb Q$
(for $\operatorname{rank}E(\mathbb Q)=2$ one has $\kappa_1^{\mathrm{Kato}}=\kappa_\ell^{\mathrm{Kato}}=0$ and $r_{\mathrm{str}}=r_p-1$, §1.4, so
$\operatorname{ord}\kappa^{\mathrm{Kato}}\ge2$ with equality iff $r_p=2$); on the Heegner side $\kappa_\ell^{\mathrm{Heeg}}$ over $K$ (§4, where
$\kappa_1^{\mathrm{Heeg}}=0$ and $\nu_\infty\ge1$ with equality iff $r_p=2$). Their non-vanishing is *equivalent* (Mazur–Rubin,
Kolyvagin) to the conclusion one wants, $r_p(E/\mathbb Q)=2$. So an "analytic" rank-2 theorem must supply an **explicit
reciprocity law for a derived class**: a formula
$$
\Phi(\kappa_n)\ \doteq\ (\text{analytic quantity})\qquad\text{with }\ \Phi(\kappa_n)\ne0\iff\kappa_n\ne0,
\qquad \nu(n)=2\ (\text{Kato})\ \text{or}\ \nu(n)=1\ (\text{Heegner}),
$$
for a suitable linear functional $\Phi$ (localisation at a prime of $n$ or at $p$ composed with $\exp^*$/$\log$), and the
analytic quantity must be shown $\ne0$ from $L''(E,1)\ne0$ (or from $L'(E^K,1)L''(E,1)\ne0$ over $K$).

**(c) What the analytic object actually is — Kurihara numbers.** For Kato's system the functional exists and its
value is known: Kurihara [Ku14], Kim [Kim26, §1.4]: for $n\in\mathcal N_{\mathrm{Kato}}$ with all $\ell\mid n$ satisfying
$\ell\equiv1$, $a_\ell\equiv\ell+1\pmod{p^k}$, the **Kurihara number**
$$
\tilde\delta_n=\sum_{a\in(\mathbb Z/n)^\times}\Big[\frac an\Big]^+\prod_{\ell\mid n}\log_{\eta_\ell}(a)\ \in\ \mathbb Z_p/I_n ,
\qquad \Big[\frac ab\Big]^+\Omega_E^+ +\Big[\frac ab\Big]^-\sqrt{-1}\,\Omega_E^-=2\pi\!\int_0^\infty f\Big(\frac ab+iy\Big)dy,
$$
($\log_{\eta_\ell}$ a discrete logarithm mod $\ell$) is the image of $\kappa_n^{\mathrm{Kato}}$ under a refinement of the dual
exponential map, and $\tilde\delta_1=L(E,1)/\Omega_E^+$. $\tilde\delta_n$ is the $\nu(n)$-th **Kolyvagin derivative of the
Mazur–Tate element** $\theta_n=\sum_a[a/n]^+\sigma_a\in\mathbb Q[(\mathbb Z/n)^\times]$, i.e. its leading coefficient in the
augmentation filtration $I^{\nu(n)}/I^{\nu(n)+1}$ [MT87]. [THEOREM] (Kim [Kim26, Thm. 1.8]; Kurihara [Ku14] under extra
hypotheses.) For $p\ge5$, (sur), Manin constant prime to $p$: if the collection $\tilde{\boldsymbol\delta}$ does not vanish
identically (which follows from the main conjecture localised at the augmentation ideal, and holds unconditionally if
$E$ has good ordinary reduction at $p$, or $r_{\mathrm{an}}(E)=0$, or $r_{\mathrm{an}}(E)=1$ and $E$ is semistable at $p$
[Kim26, Cor. 1.6]), then
$$
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)=\operatorname{ord}(\tilde{\boldsymbol\delta}):=\min\{\nu(n):\tilde\delta_n\ne0\},
$$
and $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)\cong(\mathbb Q_p/\mathbb Z_p)^{\operatorname{ord}\tilde\delta}\oplus\bigoplus_{i\ge1}
\big(\mathbb Z/p^{(\partial^{(\operatorname{ord}+2i-2)}(\tilde\delta)-\partial^{(\operatorname{ord}+2i)}(\tilde\delta))/2}\big)^2$. **Thus, for a rank-2 curve
and such $p$: $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite iff $\tilde\delta_{\ell_1\ell_2}\ne0$ for some pair of Kurihara primes.**
The quantities $\tilde\delta_n$ are finite sums of modular symbols — algebraic combinations of the central values
$L(E,\chi,1)$, $\chi$ Dirichlet characters mod $n$, reduced mod $I_n$. Kim conjectures [Kim26, Conj. 1.9]
$\partial^{(\infty)}(\tilde\delta)=\sum_{\ell\mid N}\operatorname{ord}_pc_\ell$ (proved in cases by [BCGS26, Rmk. 3.3.4] and
Kurihara–Sakamoto [KS25]).

**(d) The gap, precisely.** What is missing is any relation between the mod-$I_n$ quantities $\tilde\delta_{\ell_1\ell_2}$
(equivalently $\kappa^{\mathrm{Kato}}_{\ell_1\ell_2}$) and the archimedean number $L''(E,1)$. The Mazur–Tate philosophy relates the
leading term of $\theta_n$ in $I^{r}/I^{r+1}$ to a *regulator* (discriminant of a height pairing valued in $I/I^2$) times
$\#\operatorname{Sha}$ — an algebraic statement whose only contact with $L^{(r)}(E,1)$ is through the BSD formula itself.
The best available conjectural bridge is [BKS19, Conj. 1.5]: the cyclotomic Darmon-derivative $\kappa_\infty$ of Kato's zeta
elements equals $\frac{L^{(r)}_S(E,1)}{\Omega^+R_\infty}R^{\mathrm{Boc}}_\omega$; even granting it, one would need
$R^{\mathrm{Boc}}_\omega\neq0$, a $p$-adic-height non-degeneracy statement (Schneider's conjecture) — see `A-iwasawa-padic.md`.
This is [GAP B.1]/[GAP B.2] in §7.

**(e) Over $K$ (core rank 2) the natural rank-2 element is trivial in the relevant case.** Over an imaginary quadratic $K$,
$H^1(K,V_pE)=H^1(\mathbb Q,V_pE)\oplus H^1(\mathbb Q,V_pE^K)$ and the canonical rank-2 Euler system is $\mathbf z(E)\wedge\mathbf z(E^K)$,
whose bottom class is nonzero iff $L(E,1)L(E^K,1)\ne0$: it only encodes rank $0$ for both twists. In the situation of §4
($\operatorname{rank}E=2$, $\operatorname{rank}E^K=1$) one has $\mathbf z(E)=0$ (§1.4), $\mathbf z(E^K)\neq0$ (Perrin-Riou), $P_K=0$ (torsion): the two
available Euler systems over $K$ see only the $E^K$-line in the three-dimensional $E(K)\otimes\mathbb Q_p$.

---

## 4. The key structural analysis: $r_{\mathrm{alg}}(E)=2$, $w(E)=+1$, auxiliary $K$ with $r_{\mathrm{an}}(E^K)=1$

### 4.0 Hypotheses; the running example

Throughout §4: $E/\mathbb Q$ with $\operatorname{rank}E(\mathbb Q)=2$ and $w(E)=+1$. (If $\operatorname{Sha}(E/\mathbb Q)[p_0^\infty]$ is finite for one
prime $p_0$, then $w(E)=+1$ follows from $p_0$-parity [DD10, Thm. 1.4]; otherwise it is an assumption, true for the example.)

**Example $E=389a1$** (LMFDB 389.a1, checked 2026-09-11): $y^2+y=x^3+x^2-2x$, $N=389$ prime, $\Delta=389$, split
multiplicative at $389$ with $c_{389}=1$ and $\operatorname{ord}_{389}\Delta=1$ (so $\bar\rho_{E,p}$ is ramified at $389$ for every
$p$), $E(\mathbb Q)\cong\mathbb Z^2$ (generators $(0,0),(1,0)$), torsion trivial, no rational isogenies, Manin constant $1$,
$\deg\pi=40$, and **the $\ell$-adic Galois representation has maximal image for every prime $\ell$** (so (sur) holds for all
$p$). $r_{\mathrm{an}}=2$: $L(E,1)=0$ because $\operatorname{rank}>0$ (contrapositive of Kolyvagin/Kato), $L'(E,1)=0$ because $w=+1$,
and $L''(E,1)/2\approx0.7593165$ [LMFDB; numerical, rigorous once computed with error bounds — `compute/`].
$\Omega_E\approx4.98043$, $\operatorname{Reg}\approx0.152460$, analytic $\#\operatorname{Sha}=1$. LMFDB lists the (analytic) Iwasawa invariants
$\lambda=2$, $\mu=0$ for all good ordinary $3\le p\le 47$; since $\operatorname{ord}_{T=0}L_p(E,T)\le\lambda$, Kato's Thm. 18.4
(§1.3(3)) gives $r_p(E/\mathbb Q)\le2$, i.e. $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ finite for those $p$ [numerical input for $\lambda$;
see `A-iwasawa-padic.md`, Stein–Wuthrich [StW13]].

### 4.1 (i) Root numbers and parity constraints

**Proposition B.4.1.** [THEOREM] Let $K$ satisfy (Heeg). Then $w(E^K)=-w(E)=-1$ and $w(E/K)=-1$. Hence
$r_{\mathrm{an}}(E^K)$ is odd, $r_{\mathrm{an}}(E)$ is even, and $\operatorname{ord}_{s=1}L(E/K,s)=r_{\mathrm{an}}(E)+r_{\mathrm{an}}(E^K)$ is odd.

*Proof.* For $(D_K,N)=1$, $w(E\otimes\chi_K)=w(E)\chi_K(-N)$ (standard; the local root numbers at $\ell\mid N$ are multiplied
by $\chi_K(\ell)$ and the archimedean one by $\chi_K(-1)$). Under (Heeg) $\chi_K(\ell)=1$ for all $\ell\mid N$, so
$\chi_K(N)=1$, while $\chi_K(-1)=-1$ since $K$ is imaginary. Multiply. $\square$

By $p$-parity [DD10, Thm. 1.4] (all $E/\mathbb Q$, all $p$): $r_p(E/\mathbb Q)\equiv r_{\mathrm{an}}(E)\equiv0$ and
$r_p(E^K/\mathbb Q)\equiv1\pmod2$ for every $p$.

### 4.2 (ii) Choosing $K$ with $r_{\mathrm{an}}(E^K)=1$

**Theorem B.4.2.** [THEOREM] (Bump–Friedberg–Hoffstein [BFH90, main theorem]; Murty–Murty [MM91, main theorem];
Iwaniec [Iw90].) Let $f$ be a newform of weight $2$ on $\Gamma_0(N)$ with root number $\varepsilon$, and let $S$ be any
finite set of primes containing the primes dividing $N$. Then there exists a fundamental discriminant $D$ such that
$\varepsilon\chi_D(-1)<0$, every prime of $S$ splits in $\mathbb Q(\sqrt D)$, and $L(s,f,\chi_D)$ has a **simple zero** at $s=1$
[BFH90]. If $\varepsilon=+1$ there are infinitely many $D<0$ with $D\equiv1\pmod{4N}$ (so $D$ odd and all primes of $N$
split) and $L'(f\otimes\chi_D,1)\neq0$; indeed $\sum_{0<-D\le Y,\ D\equiv1(4N)}L'(f\otimes\chi_D,1)\sim cY\log Y$ with
$c\ne0$ [MM91], and at least $Y^{2/3-\epsilon}$ such $D\le Y$ [Iw90].

Apply this with $\varepsilon=w(E)=+1$ and $S\supseteq\{\ell\mid N\}\cup\{2,p\}$: $\chi_D(-1)=-1$ forces $D<0$, so
**there exist (infinitely many) imaginary quadratic $K$ with (Heeg), (disc) ($2$ split $\Rightarrow D_K$ odd), $p$ split in
$K$, $p\nmid D_K$, and $r_{\mathrm{an}}(E^K)=1$.** For $E=389a1$ this means $D_K<0$ odd, $D_K$ a nonzero square mod $389$, $p$ split.

**Corollary B.4.3.** [THEOREM] (Gross–Zagier–Kolyvagin, §2.3, applied to $E^K$.) For such $K$: $\operatorname{rank}E^K(\mathbb Q)=1$,
$\operatorname{Sha}(E^K/\mathbb Q)$ is finite, and hence $r_p(E^K/\mathbb Q)=1$ for every $p$. Moreover the $p$-part of BSD for $E^K$ holds
for $p\ge5$ good ordinary for $E^K$ with (sur) and Hypothesis ♠-type conditions [Zh14, Thm. 1.6], [JSW17], and for further $p$
by [BCGS26], [BSTW24].

### 4.3 (iii) Rank three over $K$; the Heegner point is torsion

**Proposition B.4.4.** [THEOREM] For $E,K$ as in §4.2: $\operatorname{rank}E(K)=3$; $\operatorname{ord}_{s=1}L(E/K,s)=r_{\mathrm{an}}(E)+1\ge3$,
with equality $3$ when $r_{\mathrm{an}}(E)=2$ (e.g. $389a1$); and $P_K\in E(K)$ is torsion, so $\kappa_1=c_M(1)=0$ for all $M$
and $\nu_\infty(E,K,p)\ge1$ for every $p$.

*Proof.* $E(K)\otimes\mathbb Q=E(\mathbb Q)\otimes\mathbb Q\oplus E^K(\mathbb Q)\otimes\mathbb Q$ (eigenspaces of $\tau$; $2$ is invertible), giving rank
$2+1$. $L(E/K,s)=L(E,s)L(E^K,s)$, $r_{\mathrm{an}}(E)\ge2$ (§4.0), $r_{\mathrm{an}}(E^K)=1$. Thus $L'(E/K,1)=0$, and by Gross–Zagier
(§2.1) $\hat h_K(P_K)=0$, so $P_K$ is torsion; then $c_M(1)=\delta(P_K)=0$ because $E(K)[p^\infty]=0$ under (sur). $\square$

### 4.4 (iv) Kolyvagin's structure theorem in this situation

**Lemma B.4.4′ (eigenspace decomposition).** [THEOREM] (standard; [Ko91, §2], [Gr91, §5].) For $p$ odd,
restriction identifies $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)\xrightarrow{\ \sim\ }\operatorname{Sel}_{p^\infty}(E/K)^+$ and
$\operatorname{Sel}_{p^\infty}(E^K/\mathbb Q)\xrightarrow{\ \sim\ }\operatorname{Sel}_{p^\infty}(E/K)^-$ (using $E^K[p^\infty]\cong E[p^\infty]$ as
$G_K$-modules with $\tau$ acting through $-1$ relative to $E$, and $[K:\mathbb Q]=2\in\mathbb Z_p^\times$ for the compatibility of local
conditions). Hence $r_p^+(E/K)=r_p(E/\mathbb Q)$ and $r_p^-(E/K)=r_p(E^K/\mathbb Q)$.

**Theorem B.4.5.** [THEOREM] (specialisation of Kolyvagin [Ko91, Thm. 4] with Conjecture A supplied by Zhang/Sweeting/BCGS;
the rank consequence is stated by Kolyvagin in his final paragraph under his Conj. 2.7 and by Zhang as
[Zh14, Thm. 1.4(ii)] in the form "$r_p(E/\mathbb Q)\ge2$".) Let $E$ be as in §4.0 and $K$ as in §4.2. Let $p$ be an odd prime
with (sur) and $p\nmid ND_K$ such that Kolyvagin's Conjecture A holds for $(E,K,p)$; by §2.5 this is the case if any of

- **[Z]** $p\ge5$ good ordinary and Hypothesis ♠ (for $N^-=1$: $\bar\rho$ ramified at every $\ell\,\|\,N$; extra condition if $N$
  not squarefree) — for $389a1$: every good ordinary $p\ge5$, $p\nmid D_K$;
- **[S]** $p$ odd, $p\nmid 2ND_K$, Condition ♦ — for $389a1$: every $p\ge5$, $p\nmid D_K$, **including supersingular $p$ and
  $p$ inert in $K$** (for supersingular $p$ use that the image of $\rho_{E,p}$ contains $SL_2(\mathbb Z_p)$, which follows from
  (sur) for $p\ge5$; (sclr) also follows);
- **[B]** $p>3$ good ordinary, $p$ split in $K$, (disc) — no ramification hypothesis.

Then, with $\nu_\infty=\nu_\infty(E,K,p)$:

1. $\nu_\infty$ is finite and **odd**, $\nu_\infty\ge1$;
2. the dominant eigenspace is the $+$ one, i.e. $\epsilon_{\nu_\infty}=w(E)(-1)^{\nu_\infty+1}=+1$, and
$$
\boxed{\ \operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)=\nu_\infty(E,K,p)+1,\qquad
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sha}(E/\mathbb Q)[p^\infty]=\nu_\infty(E,K,p)-1\ };
$$
3. $r_p^-(E/K)=r_p(E^K/\mathbb Q)=1\le\nu_\infty$, consistent with $\nu_\infty-1\equiv0\pmod2$;
4. $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)_{/\mathrm{div}}\cong\bigoplus_{i\ge1}\big(\mathbb Z/p^{\mathcal M_{\nu_\infty+2i-1}-\mathcal M_{\nu_\infty+2i}}\big)^2$;
5. $\operatorname{Sha}(E^K/\mathbb Q)[p^\infty]=\operatorname{Sel}_{p^\infty}(E^K/\mathbb Q)_{/\mathrm{div}}\cong\bigoplus_{i=1}^{\nu_\infty-1}\mathbb Z/p^{a_i}\oplus
   \bigoplus_{i\ge1}\big(\mathbb Z/p^{\mathcal M_{\nu_\infty+2i-2}-\mathcal M_{\nu_\infty+2i-1}}\big)^2$.

*Proof.* Conjecture A holds by [Z]/[S]/[B]. By Lemma B.4.4′ and Cor. B.4.3, $r_p^-(E/K)=1$ and
$r_p^+(E/K)=r_p(E/\mathbb Q)\ge\operatorname{rank}E(\mathbb Q)=2$. Kolyvagin's Thm. 4 (§2.4(2)) says one eigenspace has corank $\nu_\infty+1$ and
the other has corank $\le\nu_\infty$; since $r_p^+\ge2>1=r_p^-$, the eigenspace of corank $\nu_\infty+1$ must be $+$
(if it were $-$ we would get $1=\nu_\infty+1$ and $r_p^+\le\nu_\infty=0$, absurd). Thus $\epsilon_{\nu_\infty}=+1$, and as
$w(E)=+1$ this reads $(-1)^{\nu_\infty+1}=1$: $\nu_\infty$ is odd. Then $r_p(E/\mathbb Q)=\nu_\infty+1$ and
$\operatorname{corank}\operatorname{Sha}[p^\infty]=r_p-2=\nu_\infty-1$. Items 4–5 are §2.4(3),(4) read in the $\pm$ labelling
($\epsilon_{\nu_\infty}=+$, $-\epsilon_{\nu_\infty}=-$, $r_p^{-}=1$). $\square$

*Consistency checks.* $p$-parity: $r_p(E/\mathbb Q)=\nu_\infty+1$ is even ✓ (§4.1). Zhang's Thm. 1.4(ii) gives exactly "$\ge2$",
recovered here as $\nu_\infty\ge1$ ✓. For $389a1$ and $5\le p\le47$ good ordinary with LMFDB $\lambda=2$ (and $p\nmid D_K$):
$\nu_\infty(E,K,p)=1$, i.e. some first derived Heegner class $c_M(\ell)$ is nonzero — a statement about explicit points in
$E(K[\ell])$ that could in principle be tested in `compute/`.

**Corollary B.4.6.** [NEW] (elementary specialisation; the individual ingredients are Kolyvagin's Thms. 1 and 4 and the
equality case of [Zh14, Remark 18]; we have not found the statement in this form in the literature — cf. Kolyvagin's
final paragraph, [Zh14, Thm. 1.4(ii)], [Kim24, Thm. 2.3]. Requires adversarial review per charter.) In the setting of
Theorem B.4.5 the following are equivalent:

(a) $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite (equivalently $r_p(E/\mathbb Q)=2$);
(b) $\nu_\infty(E,K,p)=1$;
(c) there is a Kolyvagin prime $\ell$ for $(E,K,p)$ and $M\le M(\ell)$ with $c_M(\ell)\ne0$ in $H^1(K,E[p^M])^{+}$;
(d) $\mathcal M_1<\infty$.

When they hold:
$$
\operatorname{Sha}(E/\mathbb Q)[p^\infty]\cong\bigoplus_{i\ge1}\big(\mathbb Z/p^{\mathcal M_{2i}-\mathcal M_{2i+1}}\big)^2,\qquad
\operatorname{Sha}(E^K/\mathbb Q)[p^\infty]\cong\bigoplus_{i\ge1}\big(\mathbb Z/p^{\mathcal M_{2i-1}-\mathcal M_{2i}}\big)^2,
$$
$$
\operatorname{ord}_p\#\operatorname{Sha}(E/K)[p^\infty]=2\,(\mathcal M_1-\mathcal M_\infty),\qquad
\operatorname{ord}_p\#\operatorname{Sha}(E/\mathbb Q)[p^\infty]=2\sum_{i\ge1}(\mathcal M_{2i}-\mathcal M_{2i+1}),
$$
and, under the hypotheses of [BCGS26, Thm. B] ($p>3$, $p$ split in $K$, (sur), $\pi$ $p$-optimal), $\mathcal M_\infty=\sum_{\ell\mid N}\operatorname{ord}_pc_\ell$,
so $\mathcal M_1=\operatorname{ord}_p\big(\prod_{\ell\mid N}c_\ell\big)+\tfrac12\operatorname{ord}_p\#\operatorname{Sha}(E/K)[p^\infty]$.

*Proof.* (a)$\iff$(b) is Theorem B.4.5(2). (b)$\iff$(c): $\nu_\infty=1$ means $c_M(1)=0$ for all $M$ (true, Prop. B.4.4) and
$c_M(\ell)\ne0$ for some $\ell,M$; the eigenspace is $\epsilon_1=w(E)(-1)^2=+1$. (b)$\iff$(d): $\mathcal M_r<\infty\iff r\ge\nu_\infty$
(§2.4(1)) and $\mathcal M_0=\infty$. The structure statements are Theorem B.4.5(4),(5) with $\nu_\infty=1$ (then
$\nu_\infty-r_p^-=0$, so no undetermined invariants $a_i$). Summing the two exponent series telescopes:
$\sum_{i\ge1}(\mathcal M_{2i}-\mathcal M_{2i+1})+\sum_{i\ge1}(\mathcal M_{2i-1}-\mathcal M_{2i})=\mathcal M_1-\lim_r\mathcal M_r=\mathcal M_1-\mathcal M_\infty$
(the sequence is non-increasing and eventually constant since $\mathcal M_\infty<\infty$). $\operatorname{Sel}_{p^\infty}(E/K)_{/\mathrm{div}}
=\operatorname{Sha}(E/K)[p^\infty]$ when the latter is finite, and it is finite here. The last sentence is [BCGS26, Thm. B]. $\square$

### 4.5 (v) Conclusions, the $\mathbb Z$-version question, and the relation to $L$-values

**4.5.1 Which statement about $\nu_\infty$ is equivalent to finiteness of $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$.** Exactly
$\nu_\infty(E,K,p)=1$ (Cor. B.4.6), for every $p$ as in Theorem B.4.5. Note that this is *unconditional* for those $p$: no
conjecture is assumed. In particular **for $E=389a1$, all $p\ge5$ with $p\nmid D_K$: $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite iff
some first derived Heegner class $c_M(\ell)\in H^1(K,E[p^M])$ is nonzero.**

**4.5.2 Which statement would give $r_{\mathrm{alg}}\le r_{\mathrm{an}}$.** In the scenario $r_{\mathrm{alg}}=2\le r_{\mathrm{an}}$ is known
(§4.0), so the content is the Selmer statement $r_p(E/\mathbb Q)\le r_{\mathrm{an}}(E)$, i.e. $\nu_\infty(E,K,p)\le r_{\mathrm{an}}(E)-1$.
Since $\operatorname{ord}_{s=1}L(E/K,s)=r_{\mathrm{an}}(E)+1$, the BSD-compatible prediction is
$$
[\mathrm{CONJECTURE}]\qquad \nu_\infty(E,K,p)=r_{\mathrm{an}}(E)-1=\operatorname{ord}_{s=1}L(E/K,s)-2\qquad\text{for all }p\text{ as in Thm. B.4.5},
$$
which is *equivalent* (given Thm. B.4.5) to "$r_p(E/\mathbb Q)=r_{\mathrm{an}}(E)$", i.e. to BSD-rank for $E$ together with
finiteness of $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$. More generally, for arbitrary $(E,K)$ with (Heeg), Kolyvagin's Thm. 4 plus BSD
predicts $\nu_\infty(E,K,p)=\max\{r_{\mathrm{an}}(E),r_{\mathrm{an}}(E^K)\}-1$. (The upper bound $\nu_\infty\le r_{\mathrm{an}}(E)-1$ alone would
already give $r_p\le r_{\mathrm{an}}$, i.e. "$r_{\mathrm{alg}}\le r_{\mathrm{an}}$ and $\operatorname{Sha}[p^\infty]$ finite".) There is no known
way to bound $\nu_\infty$ from above by analytic data: see [GAP B.3].

**4.5.3 Independence of $p$; a $\mathbb Z$-version.**

**Proposition B.4.7.** [NEW] (elementary.) Let $E,K$ be as in §4.2 and let $\mathcal P$ be the set of odd primes $p$ satisfying the
hypotheses of Theorem B.4.5. Define the **$\mathbb Z$-version** $\nu_\infty(E,K):=\max\{\operatorname{rank}E(\mathbb Q),\operatorname{rank}E^K(\mathbb Q)\}-1=1$.
Then for $p\in\mathcal P$:
$$
\nu_\infty(E,K,p)=\nu_\infty(E,K)+s_p(E),\qquad s_p(E)=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sha}(E/\mathbb Q)[p^\infty]\ (\text{even}).
$$
Consequently: (i) $\nu_\infty(E,K,p)=\nu_\infty(E,K)$ for all $p\in\mathcal P$ with $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ finite;
(ii) $\nu_\infty(E,K,p)$ is independent of $p\in\mathcal P$, $p\gg0$, iff $s_p(E)$ is eventually constant on $\mathcal P$, and it is
eventually equal to $\nu_\infty(E,K)=1$ iff $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite for all $p\in\mathcal P$, $p\gg0$;
(iii) if $\operatorname{Sha}(E/\mathbb Q)$ is finite then $\nu_\infty(E,K,p)=1$ for all $p\in\mathcal P$.

*Proof.* Theorem B.4.5(2): $\nu_\infty(E,K,p)=r_p(E/\mathbb Q)-1=(\operatorname{rank}E(\mathbb Q)+s_p(E))-1=1+s_p(E)$; $s_p$ is even because
$\nu_\infty$ is odd. (i)–(iii) follow. $\square$

Remarks. (1) The divisibility indices $\mathcal M_r(p)$ have no literal $\mathbb Z$-version, since the Kolyvagin primes and the
levels $M(\ell)$ depend on $p$; Kolyvagin's **Conjecture 2.8** is precisely the assertion that a universal lattice
$V\subset E(K)/\mathrm{tors}$ (here $V\subset E(\mathbb Q)$ of rank $2$, with $V\otimes\mathbb Z_p=p^{\mathcal M_1(p)}E(\mathbb Q)\otimes\mathbb Z_p$
for $p\in\mathcal P$) is generated by the first derived Heegner classes for every $p$, and he proves that Conjecture 2.8 is
equivalent to Conjectures 2.5, 2.6, finiteness of $\operatorname{Sha}(E/\mathbb Q)$, $p$-independence of $\nu_\infty$, and a finiteness
condition on the $\operatorname{Sha}$-invariants of $E^K$. (2) By [BCGS26, Thm. B], **$\mathcal M_\infty(p)=\operatorname{ord}_p\prod_{\ell\mid N}c_\ell$
for all $p>3$ good ordinary, split in $K$, with (sur)**: so $\mathcal M_\infty$ *does* have a $\mathbb Z$-version, the Tamagawa product,
and Kolyvagin's Conjecture 2.6 holds along such $p$. By Cor. B.4.6, when $\operatorname{Sha}(E/\mathbb Q)$ is finite,
$p^{\mathcal M_1(p)}=\big|\prod_{\ell\mid N}c_\ell\cdot\sqrt{\#\operatorname{Sha}(E/\mathbb Q)\,\#\operatorname{Sha}(E^K/\mathbb Q)}\big|_p^{-1}$ for such $p$ — a
$\mathbb Z$-version of $\mathcal M_1$ as well (all three factors are integers; $\#\operatorname{Sha}$'s are squares by Cassels–Tate).
(3) Whether $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite for all $p\gg0$ is not known for any elliptic curve of rank $\ge2$
(see `../03-obstructions-rank-ge-2.md`, `H-sha-and-descent.md`); for $389a1$ it is known for the finitely many good ordinary
$p\le47$ via Iwasawa theory (§4.0). This is [GAP B.4].

**4.5.4 What is known or conjectured relating $\nu_\infty$, $\mathcal M_r$ to $L$-values.**

(a) Kolyvagin's own conjectures are the ones listed in §2.5; none of them mentions $L$-values except through the
Gross–Zagier formula for $\kappa_1$ and through the equivalences with finiteness of $\operatorname{Sha}$ (which is an $L$-value
statement only via BSD).

(b) [CONJECTURE ⇐ BSD] (bookkeeping from Cor. B.4.6 and the BSD formula.) If $\operatorname{Sha}(E/\mathbb Q)$ is finite and BSD holds for $E$
and $E^K$, then for every $p\in\mathcal P$:
$$
2\sum_{i\ge1}\big(\mathcal M_{2i}(p)-\mathcal M_{2i+1}(p)\big)=\operatorname{ord}_p\Big(\frac{L''(E,1)\,\#E(\mathbb Q)_{\mathrm{tor}}^2}{2\,\Omega_E\operatorname{Reg}(E/\mathbb Q)\prod_{\ell\mid N}c_\ell}\Big),
\qquad
2\sum_{i\ge1}\big(\mathcal M_{2i-1}(p)-\mathcal M_{2i}(p)\big)=\operatorname{ord}_p\Big(\frac{L'(E^K,1)\,\#E^K(\mathbb Q)_{\mathrm{tor}}^2}{\Omega_{E^K}\operatorname{Reg}(E^K/\mathbb Q)\prod_{\ell}c_\ell(E^K)}\Big).
$$
The second identity is a theorem for the $p$ covered by the $p$-part of BSD in rank one ([Zh14, Thm. 1.6], [JSW17], [BCGS26]);
the first is BSD for $E$ in rank $2$, i.e. it is the conjecture. For $389a1$ ($c_{389}=1$, torsion trivial, analytic
$\#\operatorname{Sha}=1$) the prediction is $\mathcal M_{2i}(p)=\mathcal M_{2i+1}(p)$ for all $i\ge1$ and all $p\in\mathcal P$; if moreover
$p\nmid\#\operatorname{Sha}(E^K/\mathbb Q)$ (a computable condition, $E^K$ having rank one) then also $\mathcal M_{2i-1}(p)=\mathcal M_{2i}(p)$, so
$\mathcal M_1(p)=\mathcal M_2(p)=\cdots=\mathcal M_\infty(p)$, which equals $0$ for $p>3$ split in $K$ by [BCGS26, Thm. B]:
**for such $p$ some first derived Heegner class $c_M(\ell)$ should already be $p$-indivisible.**

(c) [THEOREM] (Kim's "higher Gross–Zagier formula" [Kim24, Thm. 2.3]; hypotheses of [Kim24, §2.1]: $E$ non-CM, $p\ge5$,
(sur), Manin constant prime to $p$, $(D_K,Np)=1$, $D_K$ odd $\ne-3$, $N^-$ squarefree with $\nu(N^-)$ even.) If
$\kappa^{\mathrm{Heeg}}\ne0$ and the Kurihara collections $\tilde{\boldsymbol\delta}(E)$, $\tilde{\boldsymbol\delta}(E^K)$ are both nonzero, then
$$
\nu_\infty(E,K,p)+1=\max\{\operatorname{ord}\tilde{\boldsymbol\delta}(E),\operatorname{ord}\tilde{\boldsymbol\delta}(E^K)\}
=\max\{r_p(E/\mathbb Q),r_p(E^K/\mathbb Q)\},
$$
and if the two coranks differ by one (in our scenario: iff $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite) then
$\nu_\infty=\min\{\operatorname{ord}\tilde\delta(E),\operatorname{ord}\tilde\delta(E^K)\}$ and
$$
2\big(\partial^{(\nu_\infty)}(\kappa^{\mathrm{Heeg}})-\partial^{(\infty)}(\kappa^{\mathrm{Heeg}})\big)
=\big[\partial^{(\operatorname{ord}\tilde\delta(E))}(\tilde\delta(E))-\partial^{(\infty)}(\tilde\delta(E))\big]
+\big[\partial^{(\operatorname{ord}\tilde\delta(E^K))}(\tilde\delta(E^K))-\partial^{(\infty)}(\tilde\delta(E^K))\big]
=\operatorname{length}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/K)_{/\mathrm{div}} .
$$
In our scenario the left side is $2(\mathcal M_1-\mathcal M_\infty)$, recovering Cor. B.4.6. **This is the only known formula
expressing $\nu_\infty(E,K,p)$ and the $\mathcal M_r$ in terms of $L$-values**: the Kurihara numbers of $E$ and $E^K$, i.e.
integral (mod $I_n$) combinations of the central values $L(E,\chi,1)$, $L(E^K,\chi,1)$ for *Dirichlet* characters $\chi$
— not of $L^{(r)}(E,1)$, and not of the *anticyclotomic* values $L'(E/K,\chi,1)$. Kim's proof compares two structure
theorems (Kolyvagin's and Kurihara–Kim's); it is not an analytic identity.

(d) [THEOREM] (Mazur's conjecture: Cornut [Co02], Vatsal [Va02], Cornut–Vatsal [CV07].) Fix a prime $q\nmid 2ND_K$.
Along the anticyclotomic tower of $q$-power conductor: for $n\gg0$, $L'(E/K,\chi,1)\ne0$ for **all** ring class characters
$\chi$ of exact conductor $q^n$ (indefinite case, i.e. (Heeg)); equivalently the Heegner points $y_{q^n}$ are non-torsion with
non-torsion $\chi$-components for all such $\chi$. With $q=p$ this gives the non-vanishing of Howard's $\Lambda^{\mathrm{ac}}$-adic
class $\kappa_1^{\mathrm{Heeg}}$ [Ho04, Thm. B], but it says nothing about characters of conductor $\ell$ for a *fixed*
Kolyvagin prime $\ell$ (conductor exactly $\ell$, not $\ell^n$ with $n\gg0$).

**4.5.5 Derived classes $\kappa_n$ versus $L'(E/K,\chi,1)$ for $\chi$ of conductor dividing $n$.**

**Lemma B.4.8 (character decomposition of derived Heegner points).** [NEW] (elementary; the computation is standard —
cf. Darmon [Da92], Bertolini–Darmon [BD96, §2] — but we did not find this statement.) Assume (Heeg), $D_K\notin\{-3,-4\}$,
$p$ odd with (sur), $p\nmid ND_K$, and let $n\in\Lambda$, $\mathcal S$ a set of representatives of $\mathcal G_n/G_n$. For a character
$\chi$ of $\mathcal G_n$ let $c(\chi)\mid n$ be the conductor of $\chi$ as a ring class character (the product of the $\ell\mid n$
with $\chi|_{G_\ell}\ne1$), and $e_\chi=|\mathcal G_n|^{-1}\sum_{\sigma}\chi^{-1}(\sigma)\sigma$ acting on $E(K[n])\otimes\mathbb C$. Then
$$
e_\chi\big(P_n^{\mathcal S}\big)=\Big(\sum_{\sigma\in\mathcal S}\chi(\sigma)\Big)\cdot\prod_{\ell\mid c(\chi)}\frac{\ell+1}{\chi(\sigma_\ell)-1}
\cdot\prod_{\ell\mid n/c(\chi)}\frac{\ell\,a_\ell}{2}\cdot e_\chi\big(y_{c(\chi)}\big),
$$
where $y_{c(\chi)}$ is regarded in $E(K[n])$ via $K[c(\chi)]\subset K[n]$. In particular:

(i) if $\chi$ is trivial on $G_n$ (a character of $\operatorname{Gal}(K[1]/K)$) then $e_\chi(P_n^{\mathcal S})=h_K\,\mathbb 1[\chi=1]\prod_{\ell\mid n}\frac{\ell a_\ell}{2}\,e_1(y_1)$,
and $e_1(y_1)=h_K^{-1}P_K$;
(ii) for every $\chi$, $e_\chi(P_n^{\mathcal S})\ne0$ implies $e_\chi(y_{c(\chi)})\ne0$, hence (by [CST14, Thm. 1.1]) $L'(E/K,\chi,1)\ne0$
and $a_\ell\neq0$ for all $\ell\mid n/c(\chi)$.

*Proof.* $e_\chi$ is the projector onto the $\chi$-isotypic component, on which every $\sigma\in\mathcal G_n$ acts as $\chi(\sigma)$;
hence $e_\chi(\sigma x)=\chi(\sigma)e_\chi(x)$ and
$e_\chi(P_n^{\mathcal S})=\sum_{\sigma\in\mathcal S}\chi(\sigma)\prod_{\ell\mid n}\Big(\sum_{i=1}^{\ell}i\,\chi(\sigma_\ell)^i\Big)e_\chi(y_n)$.
If $\zeta=\chi(\sigma_\ell)\ne1$ is an $(\ell+1)$-th root of unity, $\sum_{i=1}^{\ell}i\zeta^i=\sum_{i=0}^{\ell}i\zeta^i=\frac{\ell+1}{\zeta-1}$
(differentiate $\sum_{i=0}^{m-1}X^i=(X^m-1)/(X-1)$ at $X=\zeta$, $m=\ell+1$); if $\zeta=1$ the sum is $\ell(\ell+1)/2$.
For $\ell\mid n/c(\chi)$ (so $\chi|_{G_\ell}=1$), $e_\chi$ factors through $\operatorname{Tr}_{G_\ell}/(\ell+1)$ and the norm relation
$\operatorname{Tr}_{K[m\ell]/K[m]}y_{m\ell}=a_\ell y_m$ [Gr91, Prop. 3.7] gives $e_\chi(y_{m\ell})=\frac{a_\ell}{\ell+1}e_\chi(y_m)$; iterate
down to $c(\chi)$ and combine with $\frac{\ell(\ell+1)}2\cdot\frac{a_\ell}{\ell+1}=\frac{\ell a_\ell}{2}$. (i): if $\chi|_{G_n}=1$
then $\sum_{\sigma\in\mathcal S}\chi(\sigma)$ is the full character sum over $\operatorname{Gal}(K[1]/K)$. (ii): all scalar factors other than
possibly $\sum_{\mathcal S}\chi(\sigma)$ and $a_\ell$ are nonzero; $e_\chi(y_{c})\ne0$ iff $P^0_{\chi^{\pm1}}\ne0$ in $E(K[c])\otimes\mathbb C$
iff $\hat h_K(P^0_{\chi^{\pm1}})\ne0$ (positive definiteness of the Hermitian Néron–Tate form) iff $L'(E/K,\chi,1)\ne0$ by
[CST14, Thm. 1.1], whose Heegner conditions hold: $(c,N)=1$ as $c\mid n$ and $n$ is prime to $N$, all $\ell\mid N$ split, and
condition (2) is vacuous since $(N,D_K)=1$. $\square$

**Proposition B.4.9.** [NEW] (elementary consequence.) In the setting of Theorem B.4.5 (so $P_K$ is torsion), for every
$n\in\Lambda$ and $M\le M(n)$:
$$
c_M(n)\neq0\ \Longrightarrow\ \exists\,\chi\in\widehat{\mathcal G_n}\ \text{with}\ c(\chi)>1,\ c(\chi)\mid n,\ \ a_\ell\ne0\ \forall\ell\mid n/c(\chi),\ \text{and}\ L'(E/K,\chi,1)\neq0 .
$$
In particular, if $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite then there is a Kolyvagin prime $\ell$ and a ring class character $\chi$
of conductor exactly $\ell$ with $L'(E/K,\chi,1)\ne0$; and if $h_K=1$ the converse holds *rationally*: $P_\ell$ is non-torsion
iff $L'(E/K,\chi,1)\ne0$ for some $\chi$ of conductor $\ell$.

*Proof.* If $c_M(n)\ne0$ then $P_n^{\mathcal S}\notin p^ME(K[n])$ (restriction to $K[n]$ and the Kummer map are injective).
If $P_n^{\mathcal S}$ were torsion it would lie in the finite group $E(K[n])_{\mathrm{tor}}$, which has order prime to $p$
[Gr91, Lemma 4.3], hence in $p^ME(K[n])_{\mathrm{tor}}\subset p^ME(K[n])$; so $P_n^{\mathcal S}$ is non-torsion and
$e_\chi(P_n^{\mathcal S})\ne0$ for some $\chi$. By Lemma B.4.8(i) the characters with $c(\chi)=1$
contribute $0$ (for $\chi\ne1$ the character sum vanishes; for $\chi=1$, $e_1(y_1)=h_K^{-1}P_K$ is torsion), so $c(\chi)>1$, and
(ii) gives the rest. For the last assertion: if $\operatorname{Sha}[p^\infty]$ is finite then $c_M(\ell)\ne0$ for some $\ell$ (Cor. B.4.6(c)),
and $c(\chi)\mid\ell$, $c(\chi)>1$ forces $c(\chi)=\ell$. If $h_K=1$, $\mathcal S=\{1\}$ and every scalar factor in Lemma B.4.8 is
nonzero for $\chi$ of conductor $\ell$, so $P_\ell\otimes1\ne0$ iff some $e_\chi(y_\ell)\ne0$, $c(\chi)=\ell$. $\square$

**Why the converse (from $L'(E/K,\chi,1)\neq0$ to $c_M(\ell)\neq0$) fails, precisely.** Suppose $h_K=1$ and
$L'(E/K,\chi,1)\ne0$ for some $\chi$ of conductor $\ell$, so $P_\ell$ is non-torsion. Then $c_M(\ell)\ne0$ iff
$m(\ell):=\max\{m:P_\ell\in p^mE(K[\ell])\}<M(\ell)$. The point $P_\ell=D_\ell y_\ell$ is a fixed element of the finitely generated
group $E(K[\ell])$, so $m(\ell)<\infty$, but $M(\ell)=\min(\operatorname{ord}_p(\ell+1),\operatorname{ord}_p a_\ell)$ is also a fixed finite number and
nothing forces $m(\ell)<M(\ell)$. The $\chi$-decomposition cannot decide this: $E(K[\ell])\otimes\mathbb Z_p$ is a module over
$\mathbb Z_p[G_\ell]$ with $p^{M(\ell)}\mid|G_\ell|=\ell+1$, which is **not semisimple**; the idempotents $e_\chi$ have denominators
$|G_\ell|$, and the scalar $\frac{\ell+1}{\chi(\sigma_\ell)-1}$ has $p$-adic valuation $\ge\operatorname{ord}_p(\ell+1)-\frac{1}{\varphi(p^j)}\ge M(\ell)-\frac1{p-1}$
if $\chi|_{G_\ell}$ has order $p^j$, and exactly $\operatorname{ord}_p(\ell+1)\ge M(\ell)$ if that order is prime to $p$: *every* $\chi$-component of
$D_\ell y_\ell$ is divisible by (essentially) $p^{M(\ell)}$ in $E(K[\ell])\otimes\mathbb Z_p[\chi]$. Whether $D_\ell y_\ell$ itself is divisible by
$p^{M(\ell)}$ in the *integral* module $E(K[\ell])\otimes\mathbb Z_p$ is a question about the non-semisimple $\mathbb Z_p[G_\ell]$-structure of
$E(K[\ell])\otimes\mathbb Z_p$, invisible to $E(K[\ell])\otimes\mathbb C$ and hence to the complex $L$-values $L'(E/K,\chi,1)$. Conjecturally
(equivariant BSD for $E/K[\ell]$) $m(\ell)$ is governed by $\operatorname{ord}_p$ of $\#\operatorname{Sha}(E/K[\ell])^{\chi}$-type quantities and by the
$p$-divisibility of the "Euler factors" $\frac{\ell+1}{\chi(\sigma_\ell)-1}$, $\frac{\ell a_\ell}{2}$ — i.e. by $p$-parts of
*algebraic* parts of $L'(E/K,\chi,1)$ (mod $p^{M}$ congruences between them), not by their non-vanishing. This is exactly the
regime handled by "Jochnowitz congruences" and level-raising in the proofs of Zhang and Sweeting (which never use $L'(E/K,\chi,1)$
for $\chi$ of conductor $n$), and by Kim's comparison with Kurihara numbers. We record it as **[GAP B.3]** (§7).

### 4.6 Summary of §4

| statement | status for $(E,K,p)$ as in Thm. B.4.5 |
|---|---|
| $w(E^K)=-1$, $w(E/K)=-1$ | [THEOREM] Prop. B.4.1 |
| $K$ with (Heeg), $D_K$ odd, $p$ split, $r_{\mathrm{an}}(E^K)=1$ exists | [THEOREM] BFH/MM/Iwaniec, Thm. B.4.2 |
| $\operatorname{rank}E(K)=3$, $\operatorname{ord}L(E/K,s)=r_{\mathrm{an}}(E)+1$, $P_K$ torsion, $\kappa_1=0$ | [THEOREM] Prop. B.4.4 |
| $\kappa^\infty\ne0$ | [THEOREM] Zhang / Sweeting / BCGS (hyp. [Z]/[S]/[B]) |
| dominant eigenspace $=+$, $\nu_\infty$ odd, $r_p(E/\mathbb Q)=\nu_\infty+1$ | [THEOREM] Thm. B.4.5 (Kolyvagin) |
| $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ finite $\iff\nu_\infty=1\iff$ some $c_M(\ell)\ne0$ | [NEW, elementary] Cor. B.4.6 |
| $\#\operatorname{Sha}(E/K)[p^\infty]=p^{2(\mathcal M_1-\mathcal M_\infty)}$ when $\nu_\infty=1$ | [THEOREM] Kolyvagin/Zhang Rmk. 18; Cor. B.4.6 |
| $\mathcal M_\infty=\operatorname{ord}_p\prod c_\ell$ | [THEOREM] BCGS Thm. B ($p>3$ split, (sur)) |
| $\nu_\infty(E,K,p)=1$ for $p\gg0$ | [GAP B.4] $\iff\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ finite for $p\gg0$ |
| $\nu_\infty=r_{\mathrm{an}}(E)-1$ | [CONJECTURE] $\iff$ BSD-rank $+$ Sha finiteness at $p$ |
| $c_M(n)\ne0\Rightarrow L'(E/K,\chi,1)\ne0$ for some $\chi$ of conductor $\mid n$, $>1$ | [NEW, elementary] Prop. B.4.9 |
| converse | fails structurally; [GAP B.3] |

---

## 5. Converse theorems (rank $\le1$) and why they are inherently rank $\le1$

Exact statements (hypotheses verbatim from the sources):

- [THEOREM] (Skinner [Sk20, Thm. A].) $f$ weight-$2$ newform of squarefree level $N$, $A_f$ the associated abelian
  variety. If there is at least one odd prime $\ell$ with $\pi_\ell$ the twist of the special representation by the unramified
  quadratic character (for $E$: non-split multiplicative at $\ell$), or at least two odd primes with $\pi_\ell$ special (split
  multiplicative), then $\operatorname{rank}_\mathbb ZA_f(\mathbb Q)=[M_f:\mathbb Q]$ and $\#\operatorname{Sha}(A_f)<\infty\Rightarrow\operatorname{ord}_{s=1}L(f,s)=1$. The
  $p$-adic criterion [Sk20, Thm. B]: $N$ squarefree, $p\ge5$, $K$ imaginary quadratic of odd discriminant $D$ with (a) $p\nmid N$,
  $f$ ordinary at $\lambda\mid p$; (b) $\bar\rho_{f,\lambda}$ irreducible and ramified at an odd prime inert or ramified in $K$;
  (c) $2$ and $p$ split in $K$; (d) if $(D,N)\ne1$ then $\pi_\ell$ is the unramified-quadratic twist of special for $\ell\mid(D,N)$ and
  the other primes of $N$ split; (e) $\dim_LH^1_f(K,V)=1$ and $H^1_f(K,V)\to\prod_{\mathfrak l\mid p}H^1(K_{\mathfrak l},V)$ is injective.
  Then $\operatorname{ord}_{s=1}L(f,K,s)=1$, $\operatorname{rank}A_f(K)=[M_f:\mathbb Q]$, $\operatorname{Sha}(A_f/K)$ finite. Method: Iwasawa theory (Wan's
  divisibility for the Rankin–Selberg main conjecture) shows the Bertolini–Darmon–Prasanna $p$-adic $L$-value is nonzero, which
  by the BDP formula $L^S_{\mathfrak p}(f,\mathbb 1)\doteq(\log_\omega P_K(f))^2$ gives $P_K(f)\ne0$, then Gross–Zagier.
- [THEOREM] (W. Zhang [Zh14, Thm. 1.4(i), Thm. 1.5].) $p\ge5$ good ordinary, (sur), $\bar\rho$ ramified at every $\ell\,\|\,N$
  with $\ell\equiv\pm1\pmod p$, and if $N$ is not squarefree, $\#\operatorname{Ram}(\bar\rho)\ge1$ and (if $\#\operatorname{Ram}=1$) an even
  number of $\ell\,\|\,N$: $r_p(E/\mathbb Q)=1\Rightarrow r_{\mathrm{an}}=r_{\mathrm{alg}}=1$, $\operatorname{Sha}$ finite. Thm. 1.5: if $N$ is squarefree
  (or has $\ge2$ primes $\ell\,\|\,N$), then $[\operatorname{rank}=1$ and $\#\operatorname{Sha}<\infty]\iff r_{\mathrm{an}}=1$. Method: Cor. B.4.6-type argument
  in rank one — choose $K$ with $L(E^K,1)\ne0$, get $r_p(E/K)=1$, so $\nu_\infty=0$ by Kolyvagin's Thm. 4, so $P_K$ non-torsion.
- [THEOREM] (Sweeting [Sw20, Cor. C].) Under (Heeg), (unr), ♦, $\nu(N^-)$ even: $L'(f/K,1)\ne0\iff\operatorname{rk}_{\mathcal O}\operatorname{Sel}(K,T_f)=1
  \iff\operatorname{rk}_\mathbb ZA_f(K)=[\mathcal O_f:\mathbb Z]$; new when $\bar\rho$ has dihedral image or $p=3$.
- [THEOREM] (Burungale–Castella–Grossi–Skinner [BCGS26, Cor. A].) For $(E,p,K)$ as in their Thm. A (incl. Eisenstein $p$):
  $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/K)=1\Rightarrow\operatorname{ord}_{s=1}L(E/K,s)=1$.
- [THEOREM] (Castella–Grossi–Lee–Skinner [CGLS22, Thm. E].) $p>2$ Eisenstein for $E$, $E[p]^{ss}=\mathbb F_p(\phi)\oplus\mathbb F_p(\psi)$
  with $\phi|_{G_p}\ne\mathbb 1,\omega$, $r\in\{0,1\}$: $r_p(E/\mathbb Q)=r\Rightarrow\operatorname{ord}_{s=1}L(E,s)=r$.
- [THEOREM] (Castella–Wan [CW23].) $E$ semistable, $p>3$ good **supersingular**: $r_p(E/\mathbb Q)=1\Rightarrow\operatorname{ord}_{s=1}L(E,s)=1$
  (via a Heegner-point main conjecture in Perrin-Riou's style). Castella [Ca24]: $p>3$ multiplicative, via an exceptional-zero
  formula for Heegner points (earlier: Skinner–Zhang [SZ14], Venerucci).
- [THEOREM] (Burungale–Tian [BT20]; [BT26].) $E/\mathbb Q$ with CM: $r_p(E/\mathbb Q)=1\Rightarrow\operatorname{ord}_{s=1}L(E,s)=1$ for primes
  $p$ of good ordinary reduction (split in the CM field; exact small-prime restrictions as in [BT20, Invent. Math. 220], not
  re-verified here); and **rank zero for every prime $p$**:
  $\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)=0\Rightarrow\operatorname{ord}_{s=1}L(E,s)=0$ [BT26, Ann. of Math. 203 (2026)], which with
  Smith's work gives the first instance of the even-parity Goldfeld conjecture ($50\%$ of $ny^2=x^3-x$ have analytic rank $0$).
- [THEOREM] (Burungale–Skinner–Tian–Wan [BSTW24].) New cases of the $p$-converse via a two-variable zeta element, Kobayashi's
  main conjecture for semistable $E$ at supersingular $p$, and Perrin-Riou's conjecture.
- Rank zero: Skinner–Urban [SU14, Thm. 2] ($p\ge3$ good ordinary, $E[p]$ irreducible, $\bar\rho$ ramified at some $q\,\|\,N$):
  $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$ finite $\Rightarrow L(E,1)\ne0$; Kim [Kim26, Cor. 1.11] ($p\ge5$, (sur), $\operatorname{ord}\tilde\delta<\infty$):
  $\operatorname{Sel}$ finite $\iff L(E,1)\ne0$ without the full main conjecture.

**Why these are inherently rank $\le1$.** [THEOREM-level analysis.] Every converse theorem above has the shape

$$
\text{(Selmer corank }r\in\{0,1\})\ \xrightarrow{\ \text{Iwasawa main conjecture / Kolyvagin structure theorem}\ }\ \text{(bottom class }\ne0)\ \xrightarrow{\ \text{explicit reciprocity}\ }\ L^{(r)}(E,1)\ne0 .
$$

In rank $0$ the reciprocity law is Kato's (§1.2) or the interpolation formula $L_p(E,0)=(1-\alpha^{-1})^2L(E,1)/\Omega^+$; in rank $1$
it is Gross–Zagier ($P_K\leftrightarrow L'(E/K,1)$) or BDP ($\log P_K\leftrightarrow L_p^{\mathrm{BDP}}(f,\mathbb 1)$). Both are
statements about the *bottom* class $\kappa_1$ of a rank-one Kolyvagin system, and Mazur–Rubin/Kolyvagin show $\kappa_1\ne0$ iff the
relevant Selmer corank is $\le$ the core rank $1$. For $r_p(E/\mathbb Q)=2$ the argument produces instead $\nu_\infty=1$ (Thm. B.4.5),
i.e. **$\kappa_\ell\neq0$ for some $\ell$, and there is no reciprocity law converting $\kappa_\ell\ne0$ into $L''(E,1)\ne0$** (§3.4(b),(d)).
The Iwasawa-theoretic route gives, from $r_p=2$ and the main conjecture, only $\operatorname{ord}_{T=0}L_p(E,T)\ge2$ (and equality iff the
$p$-adic height is non-degenerate — Schneider's conjecture, `A-iwasawa-padic.md`), and $\operatorname{ord}_{T=0}L_p=2$ is not known to imply
$L''(E,1)\ne0$: the $p$-adic Gross–Zagier formula (Perrin-Riou, Kobayashi) compares $L_p'(E,0)$ with $L'(E,1)$ only in rank $1$; no
rank-2 $p$-adic Gross–Zagier formula exists. So a rank-2 converse would need **either** an explicit reciprocity law for a derived class
**or** a comparison of $L_p''(E,0)$ with $L''(E,1)$; both are open. This is [GAP B.2].

---

## 6. Darmon (Stark–Heegner) points: a conjectural rank-one mechanism over real quadratic fields

[CONJECTURE] (Darmon [Da01, Conj. 5.9 (rationality and reciprocity), Conj. 5.15 (Gross–Zagier type)]; numbering as quoted
in [BD09].) Let $E/\mathbb Q$ have conductor $N=pM$, $p\nmid M$, $K$ real quadratic with $p$ inert and all $\ell\mid M$ split
(later generalised to $\chi_K(M)=1$ [Gr09], [DR22, (1.2)], and to arbitrary signature [GMS15]). For $\tau\in\mathcal H_p\cap K$
Darmon defines, by a $p$-adic "double integral" on $\mathcal H_p\times\mathcal H$ of the Tate-uniformised curve, a local point
$P_\tau\in E(K_p)$, and conjectures: (i) an integral multiple of $P_\tau$ is a global point, defined over the ring class field of
$K$ attached to the order of $\tau$; (ii) a Shimura-type reciprocity law describing the action of $G_K$ on these points;
(iii) the linear combinations $P_\psi=\sum_\sigma\psi^{-1}(\sigma)P_{\sigma\tau}$ lie in the $\psi$-part of the Mordell–Weil group and
are non-trivial when $L'(E/K,\psi,1)\ne0$ ("Stark–Heegner Gross–Zagier"). Evidence and partial results:

- [THEOREM] (Bertolini–Darmon [BD09, Thm. 1].) For genus characters $\psi$ of $K$, the combinations $P_\psi$ are global points on
  $E$ over the predicted quadratic extension of $K$, and their non-vanishing is governed by the corresponding twisted $L$-values
  (via the factorisation $L(E/K,\psi,s)=L(E^{D_1},s)L(E^{D_2},s)$ and $p$-adic $L$-functions). Hypotheses removed by Mok [Mo20];
  non-maximal orders: Longo–Martin–Hu [LMH20]; quaternionic version: Longo–Vigni [LV14]; totally real base: Mok [Mo11].
- [THEOREM] (Darmon–Rotger [DR22].) Under hypotheses on the pro-$p$ Selmer group, the $\psi$-combinations of Stark–Heegner points
  arise from global classes in the $\psi$-part of the Selmer group, non-trivial when the first derivative of a weight-variable
  $p$-adic $L$-function $L_p(f/K,\psi)$ does not vanish at the point attached to $(E/K,\psi)$ — a $p$-adic (not archimedean)
  substitute for (iii), via diagonal classes (see `C-higher-rank-euler-systems-diagonal-cycles.md`).
- [THEOREM] (Darmon–Vonk [DV21]; Darmon–Pozzi–Vonk [DPV21], [DPV24].) Rigid meromorphic cocycles give a uniform framework for
  Gross–Stark units and Stark–Heegner points and real-quadratic "singular moduli"; algebraicity of RM values is conjectural in
  general, proved for the Dedekind–Rademacher cocycle [DPV24].
- Computations: Darmon–Pollack, Guitart–Masdeu–Şengün [GMS15] (arbitrary signature), and the modular algorithms of
  Damm-Johnsen [DJ23] based on [DPV21], all consistent with rationality to high precision; no counterexample.

**Status (2026-09-11).** Rationality of individual Stark–Heegner points over ring class fields of real quadratic fields remains
open; even granted, the mechanism produces one point per ring class character, i.e. it is a **rank-one** device (its analogue of
Gross–Zagier is (iii), a *first* derivative). It has no bearing on $r_{\mathrm{an}}\ge2$ over $\mathbb Q$ beyond what Heegner points already
give, and it is outside the scope of the proof architecture for BSD over $\mathbb Q$ except as a source of rank-one auxiliary results.

---

## 7. Gap register (each with the attempt made and what it achieved)

**[GAP B.1] (Kato line, rank two).** *Statement.* Let $E/\mathbb Q$ be non-CM with $\operatorname{rank}E(\mathbb Q)=2$, $w(E)=+1$, $L''(E,1)\ne0$;
let $p>3$ be a prime of good ordinary reduction with $E[p]$ irreducible and $E(\mathbb Q_p)[p]=0$. Prove that
$\kappa^{\mathrm{Kato}}_{\ell_1\ell_2}\ne0$ for some $\ell_1\ell_2\in\mathcal N_{\mathrm{Kato}}$; equivalently (Kim [Kim26, Thm. 1.8], (sur))
that some Kurihara number $\tilde\delta_{\ell_1\ell_2}\in\mathbb Z_p/I_{\ell_1\ell_2}$ is nonzero. By §1.4 and [Kim26, Thm. 1.8] this is
*equivalent* to finiteness of $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$. *Attempt.* We reduced the problem to the explicit finite quantities
$\tilde\delta_n$ (modular symbols weighted by discrete logarithms) and identified the only conjectural bridge to $L''(E,1)$: the
Generalized Perrin-Riou Conjecture [BKS19, Conj. 1.5] for $r=2$, which expresses the cyclotomic Darmon derivative of the zeta element as
$\frac{L''_S(E,1)/2}{\Omega^+R_\infty}R^{\mathrm{Boc}}_\omega$; even assuming it, the non-vanishing of the Bockstein regulator $R^{\mathrm{Boc}}_\omega$
(a $p$-adic height non-degeneracy) is needed, and the *tame* derived classes $\kappa_{\ell_1\ell_2}$ are not the cyclotomic derivative.
*Achieved:* precise reformulation; identification of the two independent missing inputs (reciprocity law for a derived class; $p$-adic
non-degeneracy). Not proved.

**[GAP B.2] (No rank-two reciprocity law).** *Statement.* Give a linear functional $\Phi$ on $H^1(\mathbb Q,T/I_nT)$ (resp. $H^1(K,E[p^M])$)
and an analytic quantity $\mathcal A(E,n)$ (resp. $\mathcal A(E,K,\ell)$) such that $\Phi(\kappa_n)\doteq\mathcal A$ with $\mathcal A\ne0$ provable
from $L''(E,1)\neq0$ (resp. $L''(E,1)L'(E^K,1)\ne0$), for some $n$ with $\nu(n)=2$ (resp. $\nu(n)=1$). *Attempt.* §3.4 shows that (a) no
norm-compatible $\wedge^2$-system exists over the cyclotomic tower (generic rank one); (b) the candidates for $\Phi(\kappa_n)$ are the
Kurihara numbers (Kato side) and, on the Heegner side, Kim's Kurihara-number comparison [Kim24, Thm. 2.3] — both integral congruence
quantities with no known archimedean interpretation; (c) over $K$ the natural rank-2 element $\mathbf z(E)\wedge\mathbf z(E^K)$ is zero in
the relevant case. *Achieved:* the analytic object is identified (Kurihara numbers / BKS leading term); the impossibility of a
tower-interpolated $\wedge^2$ system is proved. Not resolved.

**[GAP B.3] (Integral Gross–Zagier for derived Heegner points).** *Statement.* In the setting of Theorem B.4.5 with $h_K=1$: given a
Kolyvagin prime $\ell$ and a ring class character $\chi$ of conductor $\ell$ with $L'(E/K,\chi,1)\neq0$, prove
$D_\ell y_\ell\notin p^{M(\ell)}E(K[\ell])$ — or find the correct $p$-adic/integral refinement of [CST14, Thm. 1.1] modulo $p^{M(\ell)}$ that
decides it. *Attempt.* Lemma B.4.8/Prop. B.4.9 prove the implication in one direction and show the converse is a statement about the
non-semisimple $\mathbb Z_p[G_\ell]$-module $E(K[\ell])\otimes\mathbb Z_p$, invisible to complex $L$-values; every $\chi$-component of $D_\ell y_\ell$ is
divisible by essentially $p^{M(\ell)}$, so the indivisibility of $D_\ell y_\ell$ is an integral phenomenon (equivariant BSD for $E/K[\ell]$
modulo $p^{M(\ell)}$). The only proven substitutes are congruence methods (Zhang, Sweeting) and Kim's structural comparison, none of which
starts from $L'(E/K,\chi,1)$. *Achieved:* exact identification of the obstruction; one-directional implication proved. Not resolved.

**[GAP B.4] ($p$-independence / $\mathbb Z$-version of $\nu_\infty$).** *Statement.* For $E=389a1$ (or any rank-2 curve) and a Heegner $K$ as in
§4.2, prove $\nu_\infty(E,K,p)=1$ for all $p\in\mathcal P$, $p\gg0$. By Prop. B.4.7 this is equivalent to finiteness of $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$
for all $p\gg0$, which is not known for any curve of rank $\ge2$. *Attempt.* Reduction to Sha (Prop. B.4.7); observation that $\mathcal M_\infty$
and (conditionally) $\mathcal M_1$ do have $\mathbb Z$-versions ($\prod c_\ell$; $\prod c_\ell\sqrt{\#\operatorname{Sha}(E/K)}$). For $389a1$ and $5\le p\le47$
good ordinary, $p\nmid D_K$, the statement holds via Iwasawa theory ($\lambda=2$, §4.0). *Achieved:* equivalence proved; the gap is transferred to `H-sha-and-descent.md`
and `A-iwasawa-padic.md`.

**[GAP B.5] (Kolyvagin's Conjecture A at supersingular primes, indivisibility).** *Statement.* For $p$ supersingular for $E$, prove
$\mathcal M_\infty(p)=\sum_{\ell\mid N}\operatorname{ord}_pc_\ell$ (Zhang's refined conjecture). Known: $\mathcal M_\infty<\infty$ (Sweeting, under ♦). Not needed
for Theorem B.4.5 (which uses only $\kappa^\infty\ne0$), but needed for the $\mathbb Z$-version of $\mathcal M_1$ along supersingular $p$. Not attempted
beyond recording the status.

---

## 8. References (verified)

- [BCDT] C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over $\mathbb Q$: wild 3-adic exercises*, J. Amer. Math. Soc. 14 (2001), 843–939.
- [BCGS26] A. Burungale, F. Castella, G. Grossi, C. Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory*, Camb. J. Math. 14 (2026), no. 2, 285–348, DOI 10.4310/CJM.260514224852; arXiv:2312.09301 (v2, Jan 2026).
- [BCS25] A. Burungale, F. Castella, C. Skinner, *Base change and Iwasawa main conjectures for GL$_2$*, IMRN 2025, no. 8, rnaf082, DOI 10.1093/imrn/rnaf082.
- [BD96] M. Bertolini, H. Darmon, *Heegner points on Mumford–Tate curves*, Invent. Math. 126 (1996), 413–456, DOI 10.1007/s002220050105.
- [BD05] M. Bertolini, H. Darmon, *Iwasawa's main conjecture for elliptic curves over anticyclotomic $\mathbb Z_p$-extensions*, Ann. of Math. 162 (2005), 1–64, DOI 10.4007/annals.2005.162.1.
- [BD09] M. Bertolini, H. Darmon, *The rationality of Stark–Heegner points over genus fields of real quadratic fields*, Ann. of Math. 170 (2009), 343–369, DOI 10.4007/annals.2009.170.343.
- [BDV22] M. Bertolini, H. Darmon, R. Venerucci, *Heegner points and Beilinson–Kato elements: a conjecture of Perrin-Riou*, Adv. Math. 398 (2022), 108172, DOI 10.1016/j.aim.2021.108172.
- [BFH90] D. Bump, S. Friedberg, J. Hoffstein, *Nonvanishing theorems for L-functions of modular forms and their derivatives*, Invent. Math. 102 (1990), 543–618, DOI 10.1007/BF01233440 (statement checked against zbMATH 0721.11023).
- [BKS19] D. Burns, M. Kurihara, T. Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404; sequel *…and the Mazur–Tate conjecture*, IMRN 2025, no. 4, rnaf012.
- [BPS18] K. Büyükboduk, R. Pollack, S. Sasaki, *$p$-adic Gross–Zagier formula at critical slope and a conjecture of Perrin-Riou*, arXiv:1811.08216.
- [BS21] D. Burns, T. Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems*, IMRN 2021, no. 13, 10118–10206, DOI 10.1093/imrn/rnz103; arXiv:1612.06187.
- [BSS19] D. Burns, R. Sakamoto, T. Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, arXiv:1805.08448.
- [BSTW24] A. Burungale, C. Skinner, Y. Tian, X. Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350.
- [BT20] A. Burungale, Y. Tian, *$p$-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, Invent. Math. 220 (2020), 211–253, DOI 10.1007/s00222-019-00929-7.
- [BT26] A. Burungale, Y. Tian, *A rank zero $p$-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, Ann. of Math. 203 (2026), no. 1, DOI 10.4007/annals.2026.203.1.1; arXiv:2506.03465.
- [Bu10] K. Büyükboduk, *On Euler systems of rank $r$ and their Kolyvagin systems*, Indiana Univ. Math. J. 59 (2010), 1277–1332, DOI 10.1512/iumj.2010.59.4237.
- [Ca24] F. Castella, *Exceptional zeros for Heegner points and $p$-converse to the theorem of Gross–Zagier and Kolyvagin*, arXiv:2409.01360.
- [CGLS22] F. Castella, G. Grossi, J. Lee, C. Skinner, *On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes*, Invent. Math. 227 (2022), 517–580, DOI 10.1007/s00222-021-01072-y.
- [CGS25] F. Castella, G. Grossi, C. Skinner, *Mazur's main conjecture at Eisenstein primes*, Math. Ann. 393 (2025), 2451–2506.
- [CLW26] F. Castella, Z. Liu, X. Wan, *Kato's main conjecture for nonordinary modular forms*, arXiv:2608.29470 (Aug 2026).
- [Co02] C. Cornut, *Mazur's conjecture on higher Heegner points*, Invent. Math. 148 (2002), 495–523, DOI 10.1007/s002220100199.
- [Co04] P. Colmez, *La conjecture de Birch et Swinnerton-Dyer $p$-adique*, Sém. Bourbaki 2002/03, exp. 919, Astérisque 294 (2004), 251–319 (Numdam SB_2002-2003__45__251_0).
- [CST14] L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra Number Theory 8 (2014), 2523–2572, DOI 10.2140/ant.2014.8.2523.
- [CV07] C. Cornut, V. Vatsal, *Nontriviality of Rankin–Selberg L-functions and CM points*, in L-functions and Galois representations (Durham 2004), LMS LNS 320 (2007), 121–186, DOI 10.1017/CBO9780511721267.005.
- [CW23] F. Castella, X. Wan, *Perrin-Riou's main conjecture for elliptic curves at supersingular primes*, Math. Ann. 389 (2024), 2595–2636 (online 2023), DOI 10.1007/s00208-023-02711-w. (Also: *The Iwasawa main conjectures for GL$_2$ and derivatives of $p$-adic L-functions*, Adv. Math. 400 (2022), 108266, DOI 10.1016/j.aim.2022.108266 — Hida-family main conjecture and Greenberg's conjecture on central derivatives; its converse-type result [Thm. B] is again rank one: $\mathcal I$-rank one Selmer implies $\frac{d}{ds}L_p^{\mathrm{MTT}}(f_k,s)|_{s=k/2}\ne0$ for almost all $k$.)
- [Da92] H. Darmon, *A refined conjecture of Mazur–Tate type for Heegner points*, Invent. Math. 110 (1992), 123–146, DOI 10.1007/BF01231327.
- [Da01] H. Darmon, *Integration on $\mathcal H_p\times\mathcal H$ and arithmetic applications*, Ann. of Math. 154 (2001), 589–639, DOI 10.2307/3062142.
- [DD10] T. Dokchitser, V. Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, Ann. of Math. 172 (2010), 567–596, DOI 10.4007/annals.2010.172.567 (Thm. 1.4: $p$-parity for all $E/\mathbb Q$, all $p$).
- [DPV21] H. Darmon, A. Pozzi, J. Vonk, *Diagonal restrictions of $p$-adic Eisenstein families*, Math. Ann. 379 (2021), 503–548, DOI 10.1007/s00208-020-02086-2.
- [DPV24] H. Darmon, A. Pozzi, J. Vonk, *The values of the Dedekind–Rademacher cocycle at real multiplication points*, J. Eur. Math. Soc. 26 (2024), 3987–4032, DOI 10.4171/jems/1344.
- [DR22] H. Darmon, V. Rotger, *Stark–Heegner points and diagonal classes*, arXiv:2207.01310 (Astérisque volume on diagonal classes).
- [DR25] E. Da Ronche, *Kolyvagin's conjecture for modular forms at non-ordinary primes*, arXiv:2503.09955.
- [DV21] H. Darmon, J. Vonk, *Singular moduli for real quadratic fields: a rigid analytic approach*, Duke Math. J. 170 (2021), DOI 10.1215/00127094-2020-0035.
- [DJ23] H. Damm-Johnsen, *Modular algorithms for Gross–Stark units and Stark–Heegner points*, arXiv:2301.08977.
- [GMS15] X. Guitart, M. Masdeu, M. H. Şengün, *Darmon points on elliptic curves over number fields of arbitrary signature*, Proc. LMS 111 (2015), 484–518, DOI 10.1112/plms/pdv033.
- [Gr91] B. Gross, *Kolyvagin's work on modular elliptic curves*, in L-functions and arithmetic (Durham 1989), LMS LNS 153 (1991), 235–256, DOI 10.1017/CBO9780511526053.009.
- [Gr09] M. Greenberg, *Stark–Heegner points and the cohomology of quaternionic Shimura varieties*, Duke Math. J. 147 (2009), DOI 10.1215/00127094-2009-017.
- [GZ86] B. Gross, D. Zagier, *Heegner points and derivatives of L-series*, Invent. Math. 84 (1986), 225–320, DOI 10.1007/BF01388809.
- [Ho04] B. Howard, *The Heegner point Kolyvagin system*, Compos. Math. 140 (2004), 1439–1472, DOI 10.1112/S0010437X04000569.
- [Iw90] H. Iwaniec, *On the order of vanishing of modular L-functions at the critical point*, Sém. Théor. Nombres Bordeaux 2 (1990), 365–376, DOI 10.5802/jtnb.33.
- [Je08] D. Jetchev, *Global divisibility of Heegner points and Tamagawa numbers*, Compos. Math. 144 (2008), 811–826, DOI 10.1112/S0010437X08003497.
- [JSW17] D. Jetchev, C. Skinner, X. Wan, *The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one*, Camb. J. Math. 5 (2017), 369–434, DOI 10.4310/CJM.2017.v5.n3.a2.
- [Ka04] K. Kato, *$p$-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290 (Numdam AST_2004__295__117_0; theorem numbers checked there).
- [Kim24] C.-H. Kim, *A higher Gross–Zagier formula and the structure of Selmer groups*, Trans. AMS 377 (2024), 3691–3725, DOI 10.1090/tran/9125; arXiv:2203.12161.
- [Kim26] C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Amer. J. Math. 148 (2026), no. 1, 79–129, DOI 10.1353/ajm.2026.a980769; arXiv:2203.12159.
- [Ko88] V. A. Kolyvagin, *Finiteness of $E(\mathbb Q)$ and Ш$(E,\mathbb Q)$ for a subclass of Weil curves*, Izv. Akad. Nauk SSSR 52 (1988); Math. USSR-Izv. 32 (1989), 523–541, DOI 10.1070/IM1989v032n03ABEH000779.
- [Ko90] V. A. Kolyvagin, *Euler systems*, The Grothendieck Festschrift II, Progr. Math. 87, Birkhäuser (1990), 435–483.
- [Ko91] V. A. Kolyvagin, *On the structure of Selmer groups*, Math. Ann. 291 (1991), 253–259, DOI 10.1007/BF01445205 (text checked via the transcription at wstein.org).
- [Ko91b] V. A. Kolyvagin, *On the structure of Shafarevich–Tate groups*, Algebraic geometry (Chicago 1989), LNM 1479 (1991), 94–121, DOI 10.1007/BFb0086267.
- [Ko03] S. Kobayashi, *Iwasawa theory for elliptic curves at supersingular primes*, Invent. Math. 152 (2003), 1–36, DOI 10.1007/s00222-002-0265-4.
- [KS25] M. Kurihara, R. Sakamoto, *Euler and Kolyvagin systems of rank 0 and the structure of Selmer groups*, preprint 2025 (as cited in [BCGS26]).
- [Ku14] M. Kurihara, *The structure of Selmer groups of elliptic curves and modular symbols*, in Iwasawa Theory 2012, Contrib. Math. Comput. Sci. 7, Springer (2014), 317–356; arXiv:1407.2465.
- [LMH20] M. Longo, K. Martin, Y. Hu, *Rationality of Darmon points over genus fields of non-maximal orders*, Ann. Math. Québec 44 (2020), 173–195, DOI 10.1007/s40316-019-00116-3.
- [LPV24] M. Longo, M. R. Pati, S. Vigni, *Kolyvagin's conjecture for modular forms*, arXiv:2412.02303.
- [LV14] M. Longo, S. Vigni, *The rationality of quaternionic Darmon points over genus fields of real quadratic fields*, IMRN 2014, DOI 10.1093/imrn/rnt048.
- [MM91] M. R. Murty, V. K. Murty, *Mean values of derivatives of modular L-series*, Ann. of Math. 133 (1991), 447–475, DOI 10.2307/2944316 (statement checked against zbMATH).
- [Mo11] C. P. Mok, *Heegner points and $p$-adic L-functions for elliptic curves over certain totally real fields*, Comment. Math. Helv. 86 (2011), 867–945, DOI 10.4171/CMH/243.
- [Mo20] C. P. Mok, *On a theorem of Bertolini–Darmon on the rationality of Stark–Heegner points over genus fields of real quadratic fields*, Trans. AMS 374 (2021), 1391–1419, DOI 10.1090/tran/8254.
- [MR04] B. Mazur, K. Rubin, *Kolyvagin systems*, Mem. AMS 168 (2004), no. 799, DOI 10.1090/memo/0799.
- [MR16] B. Mazur, K. Rubin, *Controlling Selmer groups in the higher core rank case*, J. Théor. Nombres Bordeaux 28 (2016), 145–183, DOI 10.5802/jtnb.933; arXiv:1312.4052.
- [MT87] B. Mazur, J. Tate, *Refined conjectures of the "Birch and Swinnerton-Dyer type"*, Duke Math. J. 54 (1987), 711–750, DOI 10.1215/S0012-7094-87-05431-7.
- [PR93] B. Perrin-Riou, *Fonctions L $p$-adiques d'une courbe elliptique et points rationnels*, Ann. Inst. Fourier 43 (1993), 945–995.
- [Ro84] D. Rohrlich, *On L-functions of elliptic curves and cyclotomic towers*, Invent. Math. 75 (1984), 409–423, DOI 10.1007/BF01388636.
- [Ru98] K. Rubin, *Euler systems and modular elliptic curves*, in Galois representations in arithmetic algebraic geometry (Durham 1996), LMS LNS 254 (1998), 351–367, DOI 10.1017/CBO9780511662010.009.
- [Ru00] K. Rubin, *Euler Systems*, Ann. of Math. Studies 147, Princeton (2000), DOI 10.1515/9781400865208.
- [Sc98] A. Scholl, *An introduction to Kato's Euler systems*, ibid., 379–460, DOI 10.1017/CBO9780511662010.011.
- [Se68] J.-P. Serre, *Abelian $\ell$-adic representations and elliptic curves*, W. A. Benjamin (1968), Ch. IV §3.4 Lemma 3 (the "$SL_2(\mathbb Z_p)$ lemma", $p\ge5$).
- [Se72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972), 259–331, DOI 10.1007/BF01405086 (surjectivity of $\bar\rho_{E,p}$ for $p\gg0$, non-CM $E$).
- [Sk20] C. Skinner, *A converse to a theorem of Gross, Zagier, and Kolyvagin*, Ann. of Math. 191 (2020), 329–354, DOI 10.4007/annals.2020.191.2.1; arXiv:1405.7294.
- [StW13] W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757–1792, DOI 10.1090/S0025-5718-2012-02649-4.
- [SU14] C. Skinner, E. Urban, *The Iwasawa main conjectures for GL$_2$*, Invent. Math. 195 (2014), 1–277, DOI 10.1007/s00222-013-0448-1.
- [Sw20] N. Sweeting, *Kolyvagin's conjecture, bipartite Euler systems, and higher congruences of modular forms* (arXiv title: *Kolyvagin's conjecture and patched Euler systems in anticyclotomic Iwasawa theory*), arXiv:2012.11771 (v3, Nov 2022).
- [SZ14] C. Skinner, W. Zhang, *Indivisibility of Heegner points in the multiplicative case*, arXiv:1407.1099.
- [Va02] V. Vatsal, *Uniform distribution of Heegner points*, Invent. Math. 148 (2002), 1–46, DOI 10.1007/s002220100183.
- [Ve16] R. Venerucci, *Exceptional zero formulae and a conjecture of Perrin-Riou*, Invent. Math. 203 (2016), 923–972, DOI 10.1007/s00222-015-0606-8.
- [YZZ13] X. Yuan, S. Zhang, W. Zhang, *The Gross–Zagier formula on Shimura curves*, Ann. of Math. Studies 184, Princeton (2013).
- [Zh01] S. Zhang, *Gross–Zagier formula for GL$_2$*, Asian J. Math. 5 (2001), 183–290; *Heights of Heegner points on Shimura curves*, Ann. of Math. 153 (2001), 27–147.
- [Zh14] W. Zhang, *Selmer groups and the indivisibility of Heegner points*, Camb. J. Math. 2 (2014), no. 2, 191–253, DOI 10.4310/CJM.2014.v2.n2.a2 (full text checked; not on arXiv).
- [Zh14b] W. Zhang, *The Birch–Swinnerton-Dyer conjecture and Heegner points: a survey*, Current Developments in Mathematics 2013, Int. Press (2014), 169–203 (Conj. 4.5 cited via [BCGS26]; not independently checked).
- LMFDB, *Elliptic curve 389.a1*, https://www.lmfdb.org/EllipticCurve/Q/389/a/1 (accessed 2026-09-11).

## 9. Search log (2026-09-11)

Fetched/verified: arXiv abstract pages 1407.1099 (Skinner–Zhang), 2012.11771 (Sweeting; v3 PDF text extracted), 2312.09301v2 (BCGS;
full text via arXiv), 1405.7294 (Skinner; Annals text), 1312.4052 (Mazur–Rubin), 1612.06187 & 1805.08448 (Burns–Sano(–Sakamoto)),
2203.12161 (Kim TAMS; full text), 2203.12159 (Kim AJM; full text), 1910.07404 (BKS), 2409.01350 (BSTW), 2409.01360 (Castella),
2506.03465 (Burungale–Tian 2026), 2503.09955, 2412.02303, 2608.29470, 2207.01310, 2301.08977, 1408.1733 (CST, full text), math/0610290
(Dokchitser²); Kolyvagin 1991 full text (wstein.org transcription) and DOI; Zhang CJM 2014 full text (author's page) and DOI; Kato
Astérisque 295 via Numdam (theorem numbers 12.4, 12.5, 14.2–14.5, 17.4, 18.4 read from the Numdam text); Colmez Bourbaki exp. 919 via
Numdam; Gross–Zagier 1986 full text (Zagier's page: (6.3), (6.4), "$D$ odd"); Howard 2004 (Cambridge Core abstract and Thms. A, B);
zbMATH reviews of BFH 1990, Murty–Murty 1991, Iwaniec 1990; Crossref records for ≈60 items (DOIs above); LMFDB 389.a1.
Searches: "Kolyvagin's conjecture 2024 2025 arXiv", "Non-vanishing of Kolyvagin systems and Iwasawa theory", "Kurihara numbers structure of
Selmer groups", "higher Gross–Zagier formula Kim", "Stark–Heegner points rationality 2024 2025 rigid meromorphic cocycles",
"Cornut Vatsal nontriviality Rankin–Selberg CM points", "Sweeting Kolyvagin bipartite Euler systems published" (no journal version found),
"Burungale Tian rank zero p-converse Annals 2026", "Castella Wan Iwasawa main conjectures GL2 derivatives converse".
Not independently verified (flagged in text): the exact numbering "Conj. 4.5" in [Zh14b] (cited via [BCGS26] and [Kim26]);
the text of [Ko90]; the journal status of [Sw20], [DR22].
