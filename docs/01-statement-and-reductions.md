# 01 — Precise statements, equivalences and reductions

Owner: statement/reductions agent. Cross-references: `00-charter.md` (notation, tags), `approaches/A-iwasawa-padic.md` (full Iwasawa treatment), `approaches/G-motivic-bloch-kato.md` (full Bloch–Kato treatment), `approaches/D-function-field-analogy.md`, `approaches/H-sha-and-descent.md`, `compute/` (all numerics quoted here are to be re-derived there).

Every reference in §7 carries a DOI, arXiv identifier or stable URL; identifiers were checked on 2026-09-11 (Crossref, arXiv, Numdam, LMFDB). Standard books and a few classical papers whose identifiers could not be confirmed by fetching are marked "not fetched". Where a statement is quoted from a source whose full text could not be fetched, this is said explicitly.

---

## 0. Conventions

The conjecture is only a conjecture once every term is normalised. The following choices are used throughout the repository; every numerical statement in `compute/` must be read against them.

### 0.1 Minimal model and Néron differential

$E/\mathbb{Q}$ is given by a global minimal Weierstrass equation
$$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,\qquad a_i\in\mathbb{Z},$$
(unique up to the substitutions $x=u^2x'+r$, $y=u^3y'+su^2x'+t$ with $u=\pm1$; we normalise $a_1,a_3\in\{0,1\}$, $a_2\in\{-1,0,1\}$). $\Delta$ is its discriminant (the minimal discriminant), $N$ the conductor, and
$$\omega_E=\frac{dx}{2y+a_1x+a_3}$$
is the Néron differential: a $\mathbb{Z}$-basis of the invariant differentials of the Néron model, well defined up to sign.

### 0.2 Period lattice, real period, complex period

Let $\Lambda_E=\{\int_\gamma\omega_E:\gamma\in H_1(E(\mathbb{C}),\mathbb{Z})\}\subset\mathbb{C}$, so $E(\mathbb{C})\cong\mathbb{C}/\Lambda_E$. Complex conjugation acts on $\Lambda_E$ by $\lambda\mapsto\bar\lambda$ (the coefficients of $E$ are real), hence $\Lambda_E\cap\mathbb{R}=\mathbb{Z}\,\Omega_E^+$ and $\Lambda_E\cap i\mathbb{R}=\mathbb{Z}\,i\Omega_E^-$ with $\Omega_E^\pm>0$. Put
$$c_\infty:=\#\pi_0(E(\mathbb{R}))=\begin{cases}2,&\Delta>0,\\1,&\Delta<0,\end{cases}\qquad
\Omega_E:=\int_{E(\mathbb{R})}|\omega_E|=c_\infty\,\Omega_E^+ .$$

[THEOREM] (classical) If $\Delta>0$ then $\Lambda_E=\mathbb{Z}\Omega_E^+\oplus\mathbb{Z}\,i\Omega_E^-$ is rectangular and $E(\mathbb{R})$ is the union of the two circles $\mathbb{R}/\mathbb{Z}\Omega_E^+$ and $i\Omega_E^-/2+\mathbb{R}/\mathbb{Z}\Omega_E^+$; if $\Delta<0$ then $\Lambda_E=\mathbb{Z}\Omega_E^+\oplus\mathbb{Z}(\Omega_E^+/2+i\Omega_E^-/2)$ and $E(\mathbb{R})=\mathbb{R}/\mathbb{Z}\Omega_E^+$ is connected. In both cases
$$2\,\mathrm{covol}(\Lambda_E)=\Omega_E\cdot\Omega_E^-,\tag{0.2.1}$$
where $\mathrm{covol}$ is the Euclidean area of a fundamental parallelogram. (Proof: read off the two lattice shapes: for $\Delta>0$, $\mathrm{covol}=\Omega_E^+\Omega_E^-$ and $\Omega_E=2\Omega_E^+$; for $\Delta<0$, $\mathrm{covol}=\Omega_E^+\cdot\Omega_E^-/2$ and $\Omega_E=\Omega_E^+$.)

The quantity $\Omega_E$ (with the factor $c_\infty$) is what LMFDB, PARI/GP, Sage and Magma call the *real period* and what enters the BSD formula below. Example: for $E=389\mathrm{a}1$ ($\Delta=389>0$) LMFDB gives $\Omega_E=4.980425121710110\ldots=2\cdot 2.490212560855\ldots$ and $\mathrm{covol}(\Lambda_E)=4.910045991115\ldots$ [LMFDB-389a1].

### 0.3 Heights and regulator

For $P\in E(\mathbb{Q})$ with $x(P)=a/b$ in lowest terms put $h_x(P)=\log\max(|a|,|b|)$ (and $h_x(O)=0$). The canonical height is
$$\hat h(P)=\lim_{n\to\infty}\frac{h_x(nP)}{n^2},\qquad \langle P,Q\rangle=\tfrac12\bigl(\hat h(P+Q)-\hat h(P)-\hat h(Q)\bigr),$$
and $\mathrm{Reg}(E/\mathbb{Q})=\det(\langle P_i,P_j\rangle)_{i,j}$ for a $\mathbb{Z}$-basis $(P_i)$ of $E(\mathbb{Q})/E(\mathbb{Q})_{\mathrm{tors}}$; $\mathrm{Reg}=1$ if the rank is $0$. Note the absence of the factor $\tfrac12$ that appears in some textbooks (where $\hat h$ is normalised with respect to the divisor $(O)$ rather than $2(O)$); with the $\tfrac12$ the regulator of a rank-$r$ curve would be divided by $2^r$ and the BSD formula (1.2) would be false as written. Convention check: for $E=389\mathrm{a}1$ and $P=(0,0)$ one computes $2P=(3,5)$, $4P=(114/121,\ast)$, so $h_x(4P)/16=\log(121)/16=0.2997\ldots$, consistent with $\hat h(P)=0.32700077\ldots$ [LMFDB-389a1] and not with half of it. With these conventions LMFDB's data for $389\mathrm{a}1$ satisfy $\Omega_E\cdot\mathrm{Reg}(E/\mathbb{Q})=4.98042512\ldots\times0.15246017\ldots=0.75931650\ldots=L''(E,1)/2!$, which is the BSD formula (1.2) with $\#\mathrm{Sha}=1$.

Over a number field $K$: for $P\in E(K)$ put $h_{x,K}(P)=\sum_{v\in M_K}\log\max(1,|x(P)|_v)$ with the absolute values normalised so that $\prod_v|a|_v=1$ for $a\in K^\times$ (i.e. $|a|_v=|N_{K_v/\mathbb{Q}_p}a|_p$ at finite $v$, $|a|_v=|a|$ at real $v$, $|a|_v=|a|^2$ at complex $v$), and $\hat h_K(P)=\lim n^{-2}h_{x,K}(nP)$. Thus $\hat h_K=[K:\mathbb{Q}]\cdot\hat h_{\mathrm{abs}}$ where $\hat h_{\mathrm{abs}}$ is the absolute canonical height, and $\hat h_{\mathbb{Q}}=\hat h$. $\mathrm{Reg}_K(E)$ is the determinant of the pairing attached to $\hat h_K$ on $E(K)/E(K)_{\mathrm{tors}}$. This is the normalisation in Tate's and Milne's formulation (§1.5), where the logarithmic height on $\mathbb{P}^m(K)$ is $\log\prod_{v}\max_i|x_i|_v$ [Mil06, I §7].

### 0.4 Tamagawa numbers

For a finite place $v$ of $K$, $c_v(E/K):=[E(K_v):E_0(K_v)]$, where $E_0(K_v)$ is the subgroup of points reducing to the identity component of the Néron model; $c_v=1$ at good places. For $E/\mathbb{Q}$ we write $c_\ell$.

### 0.5 Selmer groups, Sha, coranks

$\mathrm{Sha}(E/K)=\ker\bigl(H^1(K,E)\to\prod_vH^1(K_v,E)\bigr)$, $\mathrm{Sel}_{p^\infty}(E/K)=\ker\bigl(H^1(K,E[p^\infty])\to\prod_vH^1(K_v,E)\bigr)$, with the exact sequence
$$0\to E(K)\otimes\mathbb{Q}_p/\mathbb{Z}_p\to\mathrm{Sel}_{p^\infty}(E/K)\to\mathrm{Sha}(E/K)[p^\infty]\to0.$$
$\mathrm{Sel}_{p^\infty}(E/K)$ is a cofinitely generated $\mathbb{Z}_p$-module; write $\delta_p(E/K):=\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sha}(E/K)[p^\infty]$. Then
$$\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/K)=\mathrm{rank}_{\mathbb{Z}}E(K)+\delta_p(E/K),$$
and $\mathrm{Sha}(E/K)[p^\infty]$ is finite if and only if $\delta_p(E/K)=0$ (a cofinitely generated $p$-primary group is finite iff its corank vanishes). Over $\mathbb{Q}$ we write $r_{\mathrm{alg}}=\mathrm{rank}\,E(\mathbb{Q})$ and $\delta_p=\delta_p(E/\mathbb{Q})$.

### 0.6 The $L$-function, root number, analytic rank

$L(E,s)=\prod_\ell L_\ell(E,s)$ with $L_\ell(E,s)^{-1}=\det\bigl(1-\mathrm{Frob}_\ell\,\ell^{-s}\mid (V_qE)^{I_\ell}\bigr)$ for any $q\ne\ell$; explicitly $L_\ell^{-1}=1-a_\ell\ell^{-s}+\ell^{1-2s}$ ($\ell\nmid N$), $1-a_\ell\ell^{-s}$ with $a_\ell=\pm1$ (split/nonsplit multiplicative), $1$ (additive). Same definition over $K$ with $\mathrm{Frob}_v$, $Nv^{-s}$, $(V_qE)^{I_v}$.

[THEOREM] (Wiles, Taylor–Wiles, [BCDT01]) $E$ is modular: $L(E,s)=L(f_E,s)$ for a newform $f_E\in S_2(\Gamma_0(N))$; hence $L(E,s)$ is entire and $\Lambda(E,s):=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)$ satisfies $\Lambda(E,s)=w(E)\Lambda(E,2-s)$ with $w(E)=\pm1$ the root number. Consequently $r_{\mathrm{an}}:=\mathrm{ord}_{s=1}L(E,s)$ is defined and
$$w(E)=(-1)^{r_{\mathrm{an}}}.\tag{0.6.1}$$
(Proof of (0.6.1): $\Lambda$ is even or odd about $s=1$ according to $w=\pm1$, and $N^{s/2}(2\pi)^{-s}\Gamma(s)$ is holomorphic and non-vanishing at $s=1$.) Over a number field $K$, $L(E/K,s)$ is only conjecturally entire in general (meromorphic continuation is known in many cases by potential modularity, e.g. for all totally real and all CM fields; this is not used here); the analytic rank $r_{\mathrm{an}}(E/K)$ presupposes analytic continuation to $s=1$.

### 0.7 The analytic order of Sha

For $E/\mathbb{Q}$ with $r:=r_{\mathrm{alg}}$ put
$$\mathcal{B}(E):=\frac{L^{(r)}(E,1)}{r!}\cdot\frac{\#E(\mathbb{Q})_{\mathrm{tors}}^2}{\Omega_E\cdot\mathrm{Reg}(E/\mathbb{Q})\cdot\prod_{\ell\mid N}c_\ell}\in\mathbb{R}.$$
When $r_{\mathrm{an}}=r_{\mathrm{alg}}$ this is the "analytic order of Sha" $\#\mathrm{Sha}_{\mathrm{an}}$; in general it is just a real number (equal to $0$ if $r_{\mathrm{an}}>r_{\mathrm{alg}}$).

---

## 1. The conjecture in all its forms

### 1.1 Rank

[CONJECTURE] (BSD, rank) $r_{\mathrm{an}}=r_{\mathrm{alg}}$. [BSD65], [Tat66].

### 1.2 Leading term

[CONJECTURE] (BSD, leading term) $\mathrm{Sha}(E/\mathbb{Q})$ is finite, $r_{\mathrm{an}}=r_{\mathrm{alg}}=:r$, and
$$\lim_{s\to1}\frac{L(E,s)}{(s-1)^r}=\frac{\Omega_E\cdot\mathrm{Reg}(E/\mathbb{Q})\cdot\prod_{\ell\mid N}c_\ell\cdot\#\mathrm{Sha}(E/\mathbb{Q})}{\#E(\mathbb{Q})_{\mathrm{tors}}^2},\tag{1.2}$$
with $\Omega_E=\int_{E(\mathbb{R})}|\omega_E|=c_\infty\Omega_E^+$ (§0.2), $\mathrm{Reg}$ as in §0.3, $c_\ell$ as in §0.4. Equivalently: $\mathrm{Sha}(E/\mathbb{Q})$ is finite, $r_{\mathrm{an}}=r_{\mathrm{alg}}$, and $\mathcal{B}(E)=\#\mathrm{Sha}(E/\mathbb{Q})$.

Remarks. (i) The right side is independent of the sign of $\omega_E$ and of the choice among minimal models ($u=\pm1$). (ii) The formula is invariant under $\mathbb{Q}$-isogeny (Theorem 2.1), so it may be tested on any curve in the isogeny class; the $L$-function and $r_{\mathrm{an}}$ depend only on the class. (iii) $\#\mathrm{Sha}(E/\mathbb{Q})$, if finite, is a square (Cassels; the Cassels–Tate pairing is alternating and non-degenerate on $\mathrm{Sha}$ modulo its divisible part [Cas62], see also [PS99]); hence the formula predicts that $\mathcal{B}(E)$ is a perfect square.

### 1.3 The $p$-part

Let $p$ be a prime. The following formulation makes precise what "the $p$-part of BSD" means when $\mathrm{Sha}$ is known to be finite only at $p$.

**Definition 1.3** ($\mathrm{BSD}_p(E)$). The conjunction of
(i) $r_{\mathrm{an}}=r_{\mathrm{alg}}$;
(ii) $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$ is finite;
(iii) $\mathcal{B}(E)\in\mathbb{Q}_{>0}$;
(iv) $\mathrm{ord}_p\,\mathcal{B}(E)=\mathrm{ord}_p\,\#\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$.

Equivalently, given (i)–(iii): the rational number $\dfrac{L^{(r)}(E,1)\,\#E(\mathbb{Q})_{\mathrm{tors}}^2}{r!\,\Omega_E\,\mathrm{Reg}(E/\mathbb{Q})\,\prod_\ell c_\ell\,\#\mathrm{Sha}[p^\infty]}$ is a $p$-adic unit.

Remarks. (a) Item (iii), the *rationality* of the leading term divided by period and regulator, is not a prime-by-prime statement; it is the Deligne–Beilinson-type rationality conjecture for $h^1(E)(1)$ and is part of every formulation of a $p$-part (Bloch–Kato's conjecture presupposes it, §2.4). (b) [THEOREM] For $r_{\mathrm{alg}}\le1$ and $r_{\mathrm{an}}=r_{\mathrm{alg}}$, (iii) is known: for $r=0$ by Manin's theorem (Theorem 5.1); for $r=1$ by Gross–Zagier together with Manin's theorem (Remark 5.4.1). In this range the literature's "$p$-part of the BSD formula" is (ii)+(iv), and the *$p$-part inequality* $\mathrm{ord}_p\#\mathrm{Sha}[p^\infty]\le\mathrm{ord}_p\mathcal{B}(E)$ is what Kolyvagin- and Kato-type upper bounds give. (c) [GAP 1.3] For no elliptic curve over $\mathbb{Q}$ with $r_{\mathrm{alg}}\ge2$ is it known that $\mathcal{B}(E)\in\mathbb{Q}$: there is no theorem relating the real numbers $L^{(r)}(E,1)$, $\Omega_E$, $\mathrm{Reg}(E/\mathbb{Q})$ when $r\ge2$. Stated as a problem: *for $E=389\mathrm{a}1$, prove $L''(E,1)/(2\,\Omega_E\,\mathrm{Reg}(E/\mathbb{Q}))\in\mathbb{Q}$* (numerically it is $1.000\ldots$). The same holds for $r\ge 2$ in any known approach: the conjectural mechanism is a rank-$r$ Gross–Zagier-type formula (approaches C, G).

**Proposition 1.4.** BSD (leading term) for $E$ is equivalent to the conjunction of (i), (iii), and $\bigl[(ii)\wedge(iv)\bigr]$ for every prime $p$.

*Proof.* BSD implies each item. Conversely, (iii) gives $\mathrm{ord}_p\mathcal{B}(E)=0$ for all but finitely many $p$, so by (iv) $\mathrm{Sha}[p^\infty]=0$ for almost all $p$, while (ii) gives finiteness at each $p$; hence $\mathrm{Sha}$ is finite, and $\#\mathrm{Sha}=\prod_pp^{\mathrm{ord}_p\#\mathrm{Sha}[p^\infty]}=\prod_pp^{\mathrm{ord}_p\mathcal{B}(E)}=\mathcal{B}(E)$ since $\mathcal{B}(E)\in\mathbb{Q}_{>0}$. $\square$

### 1.4 The two "half" statements

It is convenient to name the two implications of the rank conjecture and the two inequalities in the leading term:
- $\mathrm{(R\le)}$: $r_{\mathrm{alg}}\le r_{\mathrm{an}}$; $\mathrm{(R\ge)}$: $r_{\mathrm{alg}}\ge r_{\mathrm{an}}$.
- $\mathrm{(L\le)}_p$: $\mathrm{ord}_p\#\mathrm{Sha}[p^\infty]\le\mathrm{ord}_p\mathcal{B}(E)$ (upper bound on Sha); $\mathrm{(L\ge)}_p$: the reverse inequality (lower bound on Sha, or "the $L$-value is not too divisible").
Their status is catalogued in §2.5.

### 1.5 BSD over a number field; Tate's formulation for abelian varieties

Let $K$ be a number field, $A/K$ an abelian variety of dimension $g$ with dual $A^t$, $L(A/K,s)=\prod_vL_v(A/K,s)$ with $L_v^{-1}=\det(1-\mathrm{Frob}_v\,Nv^{-s}\mid(V_qA)^{I_v})$. Fix a nonzero global exterior form $\omega\in\Gamma(A,\Omega^g_{A/K})$. For each place $v$ let $\mu_v$ be the Haar measure on $K_v$ with $\mu_v(\mathcal{O}_v)=1$ ($v$ finite), the Lebesgue measure ($v$ real), and any fixed Haar measure at complex $v$ (the choice cancels below); $\omega$ and $\mu_v$ define a measure $|\omega|_v\mu_v^g$ on the $K_v$-analytic manifold $A(K_v)$ [Wei82], and we put $\mu_v(A,\omega):=\int_{A(K_v)}|\omega|_v\mu_v^g$. Let $\mu=\prod_v\mu_v$ on $\mathbb{A}_K$ and $|\mu|:=\mu(\mathbb{A}_K/K)$.

[CONJECTURE] (Tate [Tat66, §1], as stated in [Mil06, I §7]) Let $S$ be a finite set of places containing the archimedean ones, those where $A$ has bad reduction, and those where $\omega$ does not reduce to a nonzero form on the Néron model. Put $L_S^*(A,s):=L_S(A,s)\cdot|\mu|^g/\prod_{v\in S}\mu_v(A,\omega)$, where $L_S$ omits the Euler factors at $v\in S$. Then $L_S^*(A,s)$ has analytic continuation to $s=1$, $\mathrm{Sha}(A/K)$ is finite, $r:=\mathrm{rank}\,A(K)=\mathrm{rank}\,A^t(K)=\mathrm{ord}_{s=1}L_S^*(A,s)$, and
$$\lim_{s\to1}\frac{L_S^*(A,s)}{(s-1)^r}=\frac{\#\mathrm{Sha}(A/K)\cdot|\det\langle a'_i,a_j\rangle|}{[A^t(K):\sum\mathbb{Z}a'_i]\,[A(K):\sum\mathbb{Z}a_j]},\tag{1.5}$$
for any $\mathbb{Z}$-independent families $(a'_i)\subset A^t(K)$, $(a_j)\subset A(K)$ of size $r$, where $\langle\,,\rangle:A^t(K)\times A(K)\to\mathbb{R}$ is the canonical (Néron–Tate) height pairing normalised with the logarithmic height $h(x)=\log\prod_v\max_i|x_i|_v$ on $\mathbb{P}^m(K)$ (so relative to $K$, cf. §0.3). The statement is independent of $\omega$ (product formula) and of $S$ (for good $v\notin S$ one has $\mu_v(A,\omega)=\#A_v(k_v)\,Nv^{-g}=L_v(A,1)^{-1}$) [Mil06, I §7].

For an elliptic curve the terms can be made explicit. For a finite place $v$ let $\omega^{o}_v$ be a Néron differential at $v$ and write $\omega=\lambda_v\omega^o_v$ with $\lambda_v\in K_v^\times$; then $\mu_v(E,\omega)=|\lambda_v|_v\,c_v\,\#\tilde E^0_v(k_v)/Nv=|\lambda_v|_v\,c_v\,L_v(E,1)^{-1}$ (the last equality is checked case by case from the reduction type: good, split, nonsplit multiplicative, additive). At a real place $v$, $\mu_v(E,\omega)=\int_{E(K_v)}|\omega|=c_{v}\cdot\Omega^+_{v}(\omega)$ with $c_v\in\{1,2\}$ the number of components of $E(K_v)$ and $\Omega^+_v(\omega)$ the least positive real period of $\omega$ at $v$. At a complex place, with Lebesgue measure $dx\,dy$ on $\mathbb{C}$ one gets $\mu_v(E,\omega)=\mathrm{covol}(\Lambda_{\omega,v})$ (here $|\lambda|_v=|\lambda|^2$), and $|\mu|=\mathrm{vol}(K_\infty/\mathcal{O}_K)=2^{-r_2}|d_K|^{1/2}$ (Minkowski's covolume formula; $\mathbb{A}_K=K+(K_\infty\times\prod_v\mathcal{O}_v)$ with $K\cap(K_\infty\times\prod_v\mathcal{O}_v)=\mathcal{O}_K$); with the measure $2\,dx\,dy$ at complex places instead, $\mu_v(E,\omega)=2\,\mathrm{covol}$ and $|\mu|=|d_K|^{1/2}$ [Tat67] (check for $K=\mathbb{Q}(i)$: $\mathrm{vol}(\mathbb{C}/\mathbb{Z}[i])$ is $1$ for $dx\,dy$ and $2=|{-4}|^{1/2}$ for $2\,dx\,dy$). Either way the ratio is the same, and one obtains the explicit form:

[CONJECTURE] (BSD for $E/K$) $\mathrm{Sha}(E/K)$ is finite, $r:=\mathrm{rank}\,E(K)=\mathrm{ord}_{s=1}L(E/K,s)$, and
$$\lim_{s\to1}\frac{L(E/K,s)}{(s-1)^r}=\frac{\#\mathrm{Sha}(E/K)\cdot\mathrm{Reg}_K(E)\cdot\prod_{v\nmid\infty}c_v|\omega/\omega^o_v|_v\cdot\prod_{v\,\mathrm{real}}\int_{E(K_v)}|\omega|\cdot\prod_{v\,\mathrm{cplx}}2\,\mathrm{covol}(\Lambda_{\omega,v})}{\#E(K)_{\mathrm{tors}}^2\cdot|d_K|^{1/2}},\tag{1.6}$$
where $\Lambda_{\omega,v}$ is the period lattice of $\omega$ with respect to the embedding $v$. If $E$ has a global minimal model over $K$ and $\omega$ is its Néron differential, the factors $|\omega/\omega^o_v|_v$ are $1$.

Remarks on normalisation. (a) The complex-place contribution is $2\,\mathrm{covol}(\Lambda_{\omega,v})=\int_{E(\mathbb{C})}|\omega\wedge\bar\omega|$ where $|\omega\wedge\bar\omega|$ is the measure $|{-2i}|\,dx\,dy=2\,dx\,dy$ attached to the $2$-form $\omega\wedge\bar\omega=-2i\,dx\wedge dy$ ($\omega=dz$); this equals $\|\omega\|^2$ in the normalisation of Gross–Zagier, for which $\deg(\varphi)\|\omega_E\|^2=8\pi^2c_E^2\|f\|^2$ under a modular parametrisation $\varphi$ with Manin constant $c_E$ [GZ86, I §6]. For the base change of $E/\mathbb{Q}$ to $K$, at a complex place (0.2.1) gives $2\,\mathrm{covol}(\Lambda_E)=\Omega_E\,\Omega_E^-$: the product of the real period *with* its factor $c_\infty$ and of the *least* positive imaginary period. Formulas in the literature of the shape $\Omega_+^{r_1+r_2}|\Omega_-|^{r_2}$ are correct only with this reading of $\Omega_-$; if $\Omega_-$ is defined as $\int_{E(\mathbb{C})^-}\omega$ over the locus $\{\bar P=-P\}$, it is $2i\Omega_E^-$ when $\Delta>0$ (two circles) and $i\Omega_E^-$ when $\Delta<0$, and the formula acquires a spurious $2^{r_2}$ when $\Delta>0$. (b) The height is $\hat h_K=[K:\mathbb{Q}]\hat h_{\mathrm{abs}}$; using the absolute height would divide the right side by $[K:\mathbb{Q}]^r$. (c) The $|d_K|^{1/2}$ comes from $|\mu|$ and is not optional. Consistency of (1.6) with (1.2) under base change is a theorem (Theorem 2.5), not a definition.

For a principally polarised $A$ (e.g. a Jacobian), $\#\mathrm{Sha}(A/K)$ is a square or twice a square [PS99]; for an elliptic curve it is a square.

### 1.6 Modular abelian varieties $A_f$

Let $f\in S_2(\Gamma_0(N))$ be a newform with coefficient field $K_f$, $d=[K_f:\mathbb{Q}]$, and $A_f=J_0(N)/I_fJ_0(N)$ the Shimura quotient (an abelian variety over $\mathbb{Q}$ of dimension $d$ with $\mathcal{O}_f=\mathbb{T}/I_f\hookrightarrow\mathrm{End}_{\mathbb{Q}}(A_f)$).

[THEOREM] (Shimura [Shi71, Thm 7.14]) $L(A_f,s)=\prod_{\sigma:K_f\hookrightarrow\mathbb{C}}L(f^\sigma,s)$; each factor is entire with functional equation. Hence $A_f$ satisfies the hypotheses of Tate's conjecture 1.5, which is "BSD for $A_f$".

The Hecke action gives $A_f(\mathbb{Q})\otimes\mathbb{Q}$ the structure of a $K_f$-vector space, so $\mathrm{rank}\,A_f(\mathbb{Q})=d\cdot\dim_{K_f}(A_f(\mathbb{Q})\otimes\mathbb{Q})$. BSD (rank) for $A_f$ asserts $\sum_\sigma\mathrm{ord}_{s=1}L(f^\sigma,s)=d\cdot\dim_{K_f}(A_f(\mathbb{Q})\otimes\mathbb{Q})$; the finer statement

[CONJECTURE] (Hecke-refined rank conjecture) $\mathrm{ord}_{s=1}L(f^\sigma,s)=\dim_{K_f}(A_f(\mathbb{Q})\otimes\mathbb{Q})$ for every $\sigma$

is the rank part of the Bloch–Kato/ETNC conjecture for the motive of $f$ with coefficients in $K_f$ [BF01]; it is not formally implied by BSD for $A_f$ (which only controls the sum over $\sigma$).

[THEOREM] (Shimura [Shi77]; Manin [Man72]) With suitable period normalisations $\Omega^+_{f^\sigma}$, one has $L(f^\sigma,1)/\Omega^+_{f^\sigma}=\sigma\bigl(L(f,1)/\Omega^+_f\bigr)\in K_f$; in particular $L(f,1)=0\iff L(f^\sigma,1)=0$ for all $\sigma$.

[THEOREM] (Gross–Zagier, Kolyvagin, Kolyvagin–Logachev; formulation as in [Ski20, Introduction]) Let $r\in\{0,1\}$. Then $\mathrm{ord}_{s=1}L(f,s)=r\iff\mathrm{ord}_{s=1}L(A_f,s)=d\,r$, and in that case $\mathrm{rank}\,A_f(\mathbb{Q})=d\,r$ and $\mathrm{Sha}(A_f/\mathbb{Q})$ is finite. So the Hecke-refined rank conjecture holds for $A_f$ whenever $\mathrm{ord}_{s=1}L(f,s)\le1$.

The leading-term conjecture for $A_f$ is (1.5) with $g=d$; a Hecke-equivariant refinement (an equality of $\mathcal{O}_f\otimes\mathbb{Z}_p$-ideals for each $p$) is the ETNC for $h^1(A_f)(1)$ with coefficients in $K_f$ [BF01]; see `approaches/G-motivic-bloch-kato.md`.

---

## 2. Structural reductions and equivalences

### 2.1 Isogeny invariance

**Theorem 2.1** (Cassels [Cas65] for elliptic curves; Tate [Tat66]; Milne [Mil06, I.7.1–7.4]). Let $\varphi:A\to B$ be an isogeny of abelian varieties over a number field $K$. Then:

(a) [THEOREM] $L(A/K,s)=L(B/K,s)$ as Euler products (indeed $V_qA\cong V_qB$ as $G_K$-modules). In particular $\mathrm{ord}_{s=1}$ and all derivatives at $s=1$ agree.

(b) [THEOREM] $\mathrm{rank}\,A(K)=\mathrm{rank}\,B(K)$, and for each prime $p$, $\varphi$ induces a map $\mathrm{Sel}_{p^\infty}(A/K)\to\mathrm{Sel}_{p^\infty}(B/K)$ with finite kernel and cokernel (both are killed by $\deg\varphi$ and are cofinitely generated). Hence $\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(A/K)=\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(B/K)$, $\delta_p(A)=\delta_p(B)$, $\mathrm{Sha}(A/K)[p^\infty]$ is finite iff $\mathrm{Sha}(B/K)[p^\infty]$ is, and $\mathrm{Sha}(A/K)$ is finite iff $\mathrm{Sha}(B/K)$ is [Mil06, Lemma I.7.1].

(c) [THEOREM] (invariance of the right-hand side) If $\mathrm{Sha}(A/K)$ is finite, then the right-hand side of (1.5), computed with the same measure $\mu$ and with $\omega_A=\varphi^*\omega_B$, is the same for $A$ and for $B$. Consequently, BSD (rank, leading term) holds for $A$ iff it holds for $B$ [Mil06, Thm I.7.3]. The proof compares the two sides term by term via the Euler characteristic $z(\varphi)$ of the finite kernels/cokernels of $\varphi$ on $A(K)$, $A^t(K)$, $A(K_v)$ and $\mathrm{Sha}$, using the Poitou–Tate duality for the finite Galois module $\ker\varphi$.

(d) [THEOREM] ($p$-part) The argument in (c) applies prime by prime: if $\mathrm{Sha}(A/K)[p^\infty]$ is finite, then the right-hand side of (1.5) with $\#\mathrm{Sha}$ replaced by $\#\mathrm{Sha}[p^\infty]$ is, for $A$ and for $B$, a pair of positive real numbers whose ratio is a rational number of $p$-adic valuation $0$ [Mil06, Rem. I.7.4]; [DD10, Thm 2.3 and §4.1] (where the argument is rewritten so as to give an unconditional statement about Selmer groups, Thm 4.3 there). Hence $\mathrm{BSD}_p(A)\iff\mathrm{BSD}_p(B)$ in the sense of Definition 1.3.

What is *not* invariant: $\Omega$, $\mathrm{Reg}$, $c_v$, torsion and $\#\mathrm{Sha}$ individually all change under isogeny (by rational factors); only the combination in (1.5)–(1.6) is invariant. For elliptic curves over $\mathbb{Q}$, Cassels' original statement is exactly the invariance of $\Omega_E\mathrm{Reg}(E)\prod c_\ell\#\mathrm{Sha}/\#E(\mathbb{Q})_{\mathrm{tors}}^2$ under $\mathbb{Q}$-isogeny, assuming $\mathrm{Sha}$ finite [Cas65].

### 2.2 Quadratic twists and quadratic base change

Let $K=\mathbb{Q}(\sqrt d)$ be a quadratic field with character $\chi_K$ and discriminant $d_K$, and let $E^K$ be the quadratic twist of $E$ by $\chi_K$ (so $E^K\cong E$ over $K$ and $V_p(E^K)\cong V_p(E)\otimes\chi_K$ as $G_{\mathbb{Q}}$-representations).

**Theorem 2.2.** (a) [THEOREM] $L(E/K,s)=L(E,s)\,L(E^K,s)$ as Euler products, including all bad Euler factors. (Proof: $L(E/K,s)=L(\mathrm{Ind}_{G_K}^{G_{\mathbb{Q}}}V_pE|_{G_K},s)$ by inductivity of local $L$-factors [Tat79, §3–4], and $\mathrm{Ind}_{G_K}^{G_{\mathbb{Q}}}\mathrm{Res}\,V_pE=V_pE\otimes\mathrm{Ind}\mathbf{1}=V_pE\oplus V_pE\otimes\chi_K$.) In particular $L(E/K,s)$ is entire, $w(E/K)=w(E)w(E^K)$, and $r_{\mathrm{an}}(E/K)=r_{\mathrm{an}}(E)+r_{\mathrm{an}}(E^K)$.

(b) [THEOREM] $\mathrm{rank}\,E(K)=\mathrm{rank}\,E(\mathbb{Q})+\mathrm{rank}\,E^K(\mathbb{Q})$. (Proof: $E(K)\otimes\mathbb{Q}=(E(K)\otimes\mathbb{Q})^+\oplus(E(K)\otimes\mathbb{Q})^-$ under $\mathrm{Gal}(K/\mathbb{Q})$, with $(\cdot)^+=E(\mathbb{Q})\otimes\mathbb{Q}$ and $(\cdot)^-\cong E^K(\mathbb{Q})\otimes\mathbb{Q}$ via the $K$-isomorphism $E\cong E^K$, which identifies $E^K(\mathbb{Q})$ with $\{P\in E(K):\bar P=-P\}$.)

(c) [THEOREM] For every odd prime $p$: $\mathrm{Sel}_{p^\infty}(E/K)\cong\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\oplus\mathrm{Sel}_{p^\infty}(E^K/\mathbb{Q})$ and $\mathrm{Sha}(E/K)[p^\infty]\cong\mathrm{Sha}(E/\mathbb{Q})[p^\infty]\oplus\mathrm{Sha}(E^K/\mathbb{Q})[p^\infty]$; for $p=2$ the natural maps have finite kernel and cokernel. (Proof: decompose under $\mathrm{Gal}(K/\mathbb{Q})$; restriction $H^1(\mathbb{Q},E[p^\infty])\to H^1(K,E[p^\infty])^{\mathrm{Gal}(K/\mathbb{Q})}$ has kernel and cokernel killed by $2$ and compatible local conditions, and the $(-)$-part is the same computation for $E^K[p^\infty]=E[p^\infty]\otimes\chi_K$.) Hence $\mathrm{Sha}(E/K)$ is finite iff $\mathrm{Sha}(E/\mathbb{Q})$ and $\mathrm{Sha}(E^K/\mathbb{Q})$ are finite, and $\delta_p(E/K)=\delta_p(E)+\delta_p(E^K)$.

(d) [THEOREM] BSD (rank) for $E$ and for $E^K$ implies BSD (rank) for $E/K$ (immediate from (a),(b)).

(e) [GAP 2.3] The converse implication "BSD (rank) for $E/K$ $\Rightarrow$ BSD (rank) for $E$ and $E^K$" is not known in general: from $r_{\mathrm{an}}(E)+r_{\mathrm{an}}(E^K)=r_{\mathrm{alg}}(E)+r_{\mathrm{alg}}(E^K)$ one gets $r_{\mathrm{an}}(E)-r_{\mathrm{alg}}(E)=-(r_{\mathrm{an}}(E^K)-r_{\mathrm{alg}}(E^K))$, and no inequality between $r_{\mathrm{an}}$ and $r_{\mathrm{alg}}$ is known for either curve when both analytic ranks are $\ge2$ (§2.5). Precisely: *Let $E/\mathbb{Q}$ and $K$ quadratic with $r_{\mathrm{an}}(E)\ge2$ and $r_{\mathrm{an}}(E^K)\ge2$. Assume $r_{\mathrm{an}}(E/K)=r_{\mathrm{alg}}(E/K)$. Prove $r_{\mathrm{an}}(E)=r_{\mathrm{alg}}(E)$.* Even under finiteness of $\mathrm{Sha}$ (which gives $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod 2$ for each curve, §3) this is open.

**Proposition 2.4** [NEW] (elementary; recorded for the dependency graph). Let $K/\mathbb{Q}$ be quadratic and suppose $\min\bigl(r_{\mathrm{an}}(E),r_{\mathrm{an}}(E^K)\bigr)\le1$ — e.g. whenever $r_{\mathrm{an}}(E/K)\le3$. Then BSD (rank) for $E/K$ holds if and only if BSD (rank) holds for both $E$ and $E^K$.

*Proof.* "If" is (d). Conversely assume $r_{\mathrm{an}}(E/K)=r_{\mathrm{alg}}(E/K)$; the roles of $E$ and $E^K$ are symmetric ($(E^K)^K\cong E$), so assume $r_{\mathrm{an}}(E)\le1$. By the Gross–Zagier–Kolyvagin theorem (T1 in §2.5) $r_{\mathrm{alg}}(E)=r_{\mathrm{an}}(E)$. Subtracting from $r_{\mathrm{an}}(E/K)=r_{\mathrm{alg}}(E/K)$ using (a),(b) gives $r_{\mathrm{alg}}(E^K)=r_{\mathrm{an}}(E^K)$. If $r_{\mathrm{an}}(E/K)\le3$ then $\min(r_{\mathrm{an}}(E),r_{\mathrm{an}}(E^K))\le1$ automatically. $\square$

**Theorem 2.5** (leading term under quadratic base change). [THEOREM] Assume $\mathrm{Sha}(E/\mathbb{Q})$ and $\mathrm{Sha}(E^K/\mathbb{Q})$ are finite (equivalently, by (c), $\mathrm{Sha}(E/K)$ is finite). Let $\mathrm{RHS}(E/\mathbb{Q})$, $\mathrm{RHS}(E^K/\mathbb{Q})$ denote the right side of (1.2) and $\mathrm{RHS}(E/K)$ the right side of (1.6) (with the $|d_K|^{1/2}$). Then
$$\mathrm{RHS}(E/K)=\mathrm{RHS}(E/\mathbb{Q})\cdot\mathrm{RHS}(E^K/\mathbb{Q}).$$
Consequently BSD (leading term) for $E$ and for $E^K$ implies BSD (leading term) for $E/K$.

*Proof.* Let $W=\mathrm{Res}_{K/\mathbb{Q}}(E_K)$ be the Weil restriction, an abelian surface over $\mathbb{Q}$. By [Mil72, Thm 1] (as used in [DD10, proof of Thm 2.3]) the right side of (1.5) for $W/\mathbb{Q}$ equals that for $E/K$, term by term, given finiteness of $\mathrm{Sha}(E/K)\cong\mathrm{Sha}(W/\mathbb{Q})$; this is where $|d_K|^{1/2}$ arises (as $|\mu_K|/|\mu_{\mathbb{Q}}|^2$). There is a $\mathbb{Q}$-isogeny $E\times E^K\to W$ (of degree $4$, kernel the antidiagonal $E[2]$), so by Theorem 2.1(c) $\mathrm{RHS}(W)=\mathrm{RHS}(E\times E^K)$. Finally every term of (1.5) is multiplicative for products of abelian varieties: $L$-functions, Néron models (hence Tamagawa numbers), torsion, $\mathrm{Sha}$, periods (top form $\omega_1\wedge\omega_2$), and the height pairing (orthogonal sum), so $\mathrm{RHS}(E\times E^K)=\mathrm{RHS}(E)\mathrm{RHS}(E^K)$. $\square$

[GAP 2.6] The converse for leading terms: BSD (leading term) for $E/K$, together with BSD (rank) for $E$ and $E^K$ and finiteness of $\mathrm{Sha}$, gives only $\mathcal{Q}(E)\cdot\mathcal{Q}(E^K)=1$ for the BSD quotients $\mathcal{Q}:=L^{(r)}(\cdot,1)/(r!\,\mathrm{RHS})$; it does not separate the two factors. *Problem: give any argument, valid without knowing BSD for $E^K$, that $\mathcal{Q}(E)\mathcal{Q}(E^K)=1\Rightarrow\mathcal{Q}(E)=1$.* None is known; note that conjecturally $\mathcal{Q}(E)=\mathcal{Q}(E^K)=1$, so there is no counterexample to look for, but also no mechanism.

### 2.3 Artin formalism, Galois extensions, and Artin twists

Let $F/\mathbb{Q}$ be finite Galois with group $G$. For a complex representation $\rho$ of $G$ let $L(E,\rho,s)$ be the $L$-function of $V_pE\otimes\rho$ (Euler factors via inertia invariants).

[THEOREM] (Artin formalism) $L(E/F,s)=\prod_{\rho\in\mathrm{Irr}(G)}L(E,\rho,s)^{\dim\rho}$, and more generally for $K\subset F$, $L(E/K,s)=L(E,\mathrm{Ind}_{G_K}^{G_{\mathbb{Q}}}\mathbf{1},s)$; identities $\bigoplus_i\mathrm{Ind}_{L_i/\mathbb{Q}}\mathbf{1}\cong\bigoplus_j\mathrm{Ind}_{L'_j/\mathbb{Q}}\mathbf{1}$ (Brauer relations) give $\prod_iL(E/L_i,s)=\prod_jL(E/L'_j,s)$ [Tat79, §3].

[CONJECTURE] (Deligne–Gross; see [DEW21, Conj. 1] and references there; [Del79]) $\mathrm{ord}_{s=1}L(E,\rho,s)=\langle\rho,E(F)\otimes\mathbb{C}\rangle_G$, the multiplicity of $\rho$ in $E(F)\otimes\mathbb{C}$. This implies BSD (rank) for $E$ over every subfield of $F$, and is implied by BSD (rank) over all subfields of $F$ only for those $\rho$ that are rational linear combinations of permutation representations.

**Theorem 2.7** (compatibility of BSD with Brauer relations) [THEOREM] [DD10, Thm 2.3]. Let $A/K$ be an abelian variety and $L_i,L'_j$ finite extensions of $K$ with $\bigoplus_i\mathrm{Ind}_{L_i/K}\mathbf{1}\cong\bigoplus_j\mathrm{Ind}_{L'_j/K}\mathbf{1}$. Then (a) $\sum_i\mathrm{rank}\,A(L_i)=\sum_j\mathrm{rank}\,A(L'_j)$; (b) if all $\mathrm{Sha}(A/L_i)$, $\mathrm{Sha}(A/L'_j)$ are finite, then $\prod_i\mathrm{BSD}(A/L_i)=\prod_j\mathrm{BSD}(A/L'_j)$, where $\mathrm{BSD}(A/L)$ denotes the right side of (1.5)/(1.6) (with the same $\omega$ over $K$ throughout); (c) if only the $p^\infty$-parts of these $\mathrm{Sha}$ are finite, the same holds for the versions with $\#\mathrm{Sha}[p^\infty]$, up to a rational number of trivial $p$-adic valuation. (Proof: Weil restriction and Theorem 2.1, as in the proof of Theorem 2.5; the permutation modules are isogenous over $\mathbb{Z}$ by [Mil72, §2].) Theorem 2.5 is the case $L_1=K$, $L_2=K'$ (the quadratic twist realised as a Brauer relation via $\mathrm{Res}_{K/\mathbb{Q}}\sim E\times E^K$).

Refinements. (i) [CONJECTURE] The equivariant Tamagawa number conjecture (ETNC) of Burns–Flach for the pair $(h^1(E_F)(1),\mathbb{Z}[G])$ [BF01] refines BSD for $E$ over all intermediate fields simultaneously and is compatible with the functorialities in the coefficient ring; the non-equivariant projections recover the Tamagawa number conjecture for $E$ over each $K\subset F$ (§2.4). Burns–Macias Castillo [BMC19] formulate refined BSD-type conjectures for the Hasse–Weil–Artin $L$-series $L(E,\rho,s)$ and establish their precise relation to the ETNC. (ii) [THEOREM] (Dokchitser–Evans–Wiersema [DEW21, Example 3]) There is no BSD-type formula for the leading term of $L(E,\rho,s)$ in terms of the "usual" arithmetic invariants alone: the curves $307\mathrm{a}1$ and $307\mathrm{c}1$ have the same conductor, discriminant, trivial Mordell–Weil group, trivial $\mathrm{Sha}$ and trivial Tamagawa numbers over $\mathbb{Q}$ and over $\mathbb{Q}(\zeta_{11})^+$, but for a Dirichlet character $\chi$ of order $5$ and conductor $11$ the normalised $L$-values $\mathcal{L}(E,\chi)$ differ ($1$ versus $((1\pm\sqrt5)/2)^2$). Any refinement must therefore involve finer (Galois-module) invariants, as in [BMC19]. (iii) [THEOREM] For $\rho=\chi_K$ quadratic, the Artin-twisted statement is the twist statement of §2.2; for $\rho$ of dimension $1$ (Dirichlet characters), $L(E,\chi,s)=L(f_E\otimes\chi,s)$ is entire; for $\rho$ of dimension $2$ and odd, $L(E,\rho,s)$ is a Rankin–Selberg $L$-function of $f_E$ against a weight-one form (Khare–Wintenberger, Langlands–Tunnell) and is entire; for general $\rho$ analytic continuation is not known.

### 2.4 Relation to the Bloch–Kato Tamagawa number conjecture

Let $M=h^1(E)(1)$, so that $L(M,s)=L(E,s+1)$ and the point of interest is $s=0$. The Tamagawa number conjecture of Bloch–Kato [BK90, Conj. 5.15], in the general formulation of Fontaine–Perrin-Riou [FPR94] and Burns–Flach [BF01], asserts, for $M$ and each prime $p$: (rank) $\mathrm{ord}_{s=0}L(M,s)=\dim_{\mathbb{Q}_p}H^1_f(\mathbb{Q},V_pE)-\dim H^0(\mathbb{Q},V_pE)$; (rationality) the leading coefficient $L^*(M,0)$ lies in $\mathbb{Q}^\times$ times the period–regulator determinant; (integrality at $p$) the resulting rational number has the $p$-adic valuation dictated by the Tamagawa measures of the integral structures on the fundamental line. $H^1_f(\mathbb{Q},V_pE)$ is the Bloch–Kato Selmer group, and $\dim H^1_f(\mathbb{Q},V_pE)=\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})=r_{\mathrm{alg}}+\delta_p$ [BK90, §3], [Kat04, 14.1] (Kato: "the usual Selmer group of an abelian variety $A$ coincides with $\bigoplus_p\mathrm{Sel}(K,T_pA)$"). Hence the rank part of TNC$_p$ is $r_{\mathrm{an}}=r_{\mathrm{alg}}+\delta_p$; together with finiteness of $H^2_f$ it is equivalent to "$r_{\mathrm{an}}=r_{\mathrm{alg}}$ and $\mathrm{Sha}[p^\infty]$ finite".

**Theorem 2.9** [THEOREM] (Burns–Flach [BF96, (1.35)–(1.37)], following Bloch–Kato [BK90] (who introduced the conjecture as a generalisation of BSD) and Fontaine–Perrin-Riou [FPR94]; the explicit derivation of the classical formula from TNC$_p$ is written out in [Ven07, §3.1]). Let $A/\mathbb{Q}$ be an abelian variety with $\mathrm{Sha}(A/\mathbb{Q})$ finite, let $p$ be an odd prime, and let $T_p=T_p(A^t)$ be the natural lattice in $M_p$. Then TNC$_p$ for $h^1(A)(1)$ holds if and only if
$$\frac{L^*(A,1)}{\Omega_A\cdot\mathrm{Reg}(A/\mathbb{Q})}\in\mathbb{Q}^\times\quad\text{and}\quad \mathrm{ord}_p\!\left(\frac{L^*(A,1)}{\Omega_A\,\mathrm{Reg}(A/\mathbb{Q})}\right)=\mathrm{ord}_p\!\left(\frac{\#\mathrm{Sha}(A/\mathbb{Q})\prod_\ell c_\ell}{\#A(\mathbb{Q})_{\mathrm{tors}}\,\#A^t(\mathbb{Q})_{\mathrm{tors}}}\right),$$
where $L^*(A,1)$ is the leading coefficient at $s=1$ and $r_{\mathrm{an}}=r_{\mathrm{alg}}$ is part of the hypothesis "TNC$_p$". Under finiteness of $\mathrm{Sha}$, one has $H^1_f(\mathbb{Q},T_p)\cong A^t(\mathbb{Q})\otimes\mathbb{Z}_p$, $H^3_f\cong\mathrm{Hom}(A(\mathbb{Q})_{\mathrm{tors}},\mathbb{Q}_p/\mathbb{Z}_p)$, and an exact sequence $0\to\mathrm{Sha}(A/\mathbb{Q})[p^\infty]\to H^2_f(\mathbb{Q},T_p)\to\mathrm{Hom}(A(\mathbb{Q}),\mathbb{Z}_p)\to0$ [BF96, (1.35)–(1.37)]; the Bloch–Kato local Tamagawa numbers at $\ell\ne p$ are the $p$-parts of the $c_\ell$, and the archimedean and $p$-adic periods combine to $\Omega_A$ times a $p$-adic unit. In particular, for an elliptic curve with $\mathrm{Sha}$ finite and $p$ odd: TNC$_p(h^1(E)(1))\iff\mathrm{BSD}_p(E)$ in the sense of Definition 1.3, and TNC for all $p$ (with the $p=2$ case, for which the same argument is asserted to go through in [BF96] but was not re-derived here) is equivalent to BSD (leading term). The finiteness of $\mathrm{Sha}$ enters twice: it is needed to identify $H^2_f$ with the classical invariants, and the TNC's own finiteness assertion for $H^2_f(\mathbb{Q},T_p)_{\mathrm{tors}}$ is the finiteness of $\mathrm{Sha}[p^\infty]$. The full treatment (including the precise fundamental line, the $p=2$ case and the equivariant version) is in `approaches/G-motivic-bloch-kato.md`.

### 2.5 The two inequalities: what is known where

We catalogue the theorems that give $\mathrm{(R\le)}$, $\mathrm{(R\ge)}$, $\mathrm{(L\le)}_p$, $\mathrm{(L\ge)}_p$ in each regime, with exact hypotheses. Throughout $E/\mathbb{Q}$.

**T1.** [THEOREM] (Gross–Zagier [GZ86]; Kolyvagin [Kol88], [Kol89], [Kol90]; existence of the auxiliary quadratic field by Bump–Friedberg–Hoffstein [BFH90] and Murty–Murty [MM91]) If $r_{\mathrm{an}}\le1$ then $r_{\mathrm{alg}}=r_{\mathrm{an}}$ and $\mathrm{Sha}(E/\mathbb{Q})$ is finite. Moreover Kolyvagin gives an explicit upper bound for $\#\mathrm{Sha}[p^\infty]$ in terms of the index of the Heegner point, i.e. $\mathrm{(L\le)}_p$ up to controlled factors (Kolyvagin's bound is sharp only under further hypotheses). Both $\mathrm{(R\le)}$ and $\mathrm{(R\ge)}$ hold in this regime.

**T2.** [THEOREM] (Kato [Kat04, Thm 14.2(2)] with $k=2$, $K=\mathbb{Q}$, $\chi=1$) If $L(E,1)\ne0$ then $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ is finite for every $p$ and zero for all but finitely many $p$; hence $E(\mathbb{Q})$ and $\mathrm{Sha}(E/\mathbb{Q})$ are finite. This is $\mathrm{(R\ge)}$ (indeed $r_{\mathrm{alg}}=0$) for $r_{\mathrm{an}}=0$, by a method independent of Heegner points; with the integral divisibility of Theorem 4.8(a) it gives $\mathrm{(L\le)}_p$ for $p\ge5$ good with $\bar\rho_{E,p}$ surjective [SW13, Thm 8.1].

**T3.** [THEOREM] (Kato [Kat04, Thm 18.4]) For every prime $p$ at which $E$ has good or multiplicative reduction, and every root $\alpha$ of $X^2-a_pX+p$ (resp. $\alpha=a_p$ if $p\mid N$) with $\mathrm{ord}_p\alpha<1$:
$$\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\le\mathrm{ord}_{T=0}L_{p,\alpha}(E,T)\quad\text{if }\alpha\ne1,\qquad\le\mathrm{ord}_{T=0}L_{p,\alpha}(E,T)-1\quad\text{if }\alpha=1\ (E\text{ split multiplicative at }p).$$
In particular $r_{\mathrm{alg}}\le r_p$ for good ordinary $p$ (with $r_p$ as in §4). This is the $p$-adic analogue of $\mathrm{(R\le)}$; it says nothing about $r_{\mathrm{an}}$ unless $r_p$ is related to $r_{\mathrm{an}}$ ([GAP 4.9]).

**T4.** [CONDITIONAL] (converse in rank $0$: $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ finite $\Rightarrow L(E,1)\ne0$). Known under each of: (a) $p$ odd, good ordinary, $\bar\rho_{E,p}$ irreducible, and there is $q\ne p$ with $q\,\|\,N$ and $\bar\rho_{E,p}$ ramified at $q$ [SU14, Thm 1] (via the main conjecture, Theorem 4.8(b), and the interpolation formula (4.1.2)); (b) $E$ semistable, $p>2$ supersingular ($p=3$ with the extra condition (1.7) of loc. cit.) [BSTW24, Thm 1.6]; (c) $p>2$ of good ordinary reduction, $E$ with a rational $p$-isogeny with kernel character $\phi$ satisfying $\phi|_{G_p}\ne1,\omega$ [CGS25, Thm A] (main conjecture at Eisenstein primes; the deduction is as in (a)). Consequently, in these cases: $r_{\mathrm{alg}}=0$ and $\mathrm{Sha}[p^\infty]$ finite $\Rightarrow r_{\mathrm{an}}=0$.

**T5.** [CONDITIONAL] (converse in rank $1$: $\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})=1\Rightarrow r_{\mathrm{an}}=1$). Known under each of: (a) Skinner [Ski20, Thm A]: $E$ semistable with at least one odd prime of nonsplit multiplicative reduction or at least two odd primes of split multiplicative reduction, $\mathrm{rank}\,E(\mathbb{Q})=1$ and $\#\mathrm{Sha}(E)<\infty$; [Ski20, Thm C]: same reduction hypotheses, and a prime $p\ge5$ of good ordinary reduction with $E[p]$ irreducible, $\mathrm{Sel}_p(E)\cong\mathbb{Z}/p$ and the image of $\mathrm{Sel}_p(E)\to E(\mathbb{Q}_p)/pE(\mathbb{Q}_p)$ not contained in the image of $E(\mathbb{Q}_p)[p]$; (b) W. Zhang [Zha14]: $p\ge5$ good ordinary, $\bar\rho_{E,p}$ surjective, plus indivisibility conditions on Tamagawa numbers at primes $\ell\,\|\,N$ (see loc. cit. for the exact list); (c) Burungale–Skinner–Tian–Wan [BSTW24, Thm 1.10]: $p\nmid2N$ ordinary, $\bar\rho_{E,p}$ surjective, and some $\ell\,\|\,N$ with $\bar\rho_{E,p}$ ramified at $\ell$; (d) CM curves: Burungale–Tian [BT20] (hypotheses in loc. cit.); Eisenstein primes: Castella–Grossi–Lee–Skinner [CGLS22] (hypotheses in loc. cit.); dihedral residual image: Sweeting [Swe21]. Consequently, in these cases: $r_{\mathrm{alg}}=1$ and $\mathrm{Sha}[p^\infty]$ finite $\Rightarrow r_{\mathrm{an}}=1$.

**T6.** [THEOREM] (parity, §3) For every $p$, $(-1)^{\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})}=w(E)=(-1)^{r_{\mathrm{an}}}$ [DD10, Thm 1.4]. Hence if $\mathrm{Sha}[p^\infty]$ is finite for one $p$, then $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod 2$. This is the only known unconditional relation between $r_{\mathrm{alg}}$ and $r_{\mathrm{an}}$ valid for all curves.

**T7.** [GAP 2.10] If $r_{\mathrm{an}}\ge2$, neither $\mathrm{(R\le)}$ nor $\mathrm{(R\ge)}$ is known for any curve, except by direct computation for individual curves with $r_{\mathrm{an}}\le3$ (§5.1). In particular there is no curve with $r_{\mathrm{an}}\ge4$ for which BSD (rank) is known, and no curve with $r_{\mathrm{an}}\ge2$ for which $\mathrm{Sha}$ is known to be finite [SW13, §1.1].

**T8.** [THEOREM] (statistics; Bhargava–Skinner–Zhang [BSZ14]) When ordered by height, a proportion $>66\%$ of elliptic curves over $\mathbb{Q}$ satisfy BSD (rank); the proof combines T1, T4, T5 with Selmer averages (`approaches/E-arithmetic-statistics.md`).

**T9.** [CONDITIONAL] ($p$-part of the leading term, $r_{\mathrm{an}}\le1$) $\mathrm{(L\le)}_p\wedge\mathrm{(L\ge)}_p$ is known in rank $0$ under the hypotheses of T4(a) [SU14, Thm 2], of T4(b) [BSTW24, Thm 1.5], and (Eisenstein primes) [CGLS22]; in rank $1$ under $p\nmid2N$ ordinary, $\bar\rho_{E,p}$ absolutely irreducible and some $\ell\,\|\,N$ with $\bar\rho_{E,p}$ ramified at $\ell$ [JSW17], [BSTW24, Thm 1.9], and for $E$ semistable and $p>2$ supersingular [BSTW24, Thm 1.5]. For CM curves see Rubin [Rub91]. The prime $p=2$ and the primes of additive reduction are open in general; the full treatment is `02-state-of-the-art.md`.

### 2.6 The role of finiteness of Sha

**Theorem 2.12** (function fields). Let $K$ be the function field of a smooth projective curve over $\mathbb{F}_q$, $\mathrm{char}\,K=p$.

(a) [THEOREM] (Tate [Tat66], Milne [Mil75]; statement as in [Ulm11, Thm 12.1]) For an elliptic curve $E/K$: $\mathrm{rank}\,E(K)\le\mathrm{ord}_{s=1}L(E,s)$; and the following are equivalent: (i) $\mathrm{rank}\,E(K)=\mathrm{ord}_{s=1}L(E,s)$; (ii) $\mathrm{Sha}(E/K)$ is finite; (iii) $\mathrm{Sha}(E/K)[\ell^\infty]$ is finite for one prime $\ell$ ($\ell=p$ allowed). When they hold, the refined BSD formula (Tate's (1.5) in its function-field form) holds.

(b) [THEOREM] (Kato–Trihan [KT03], completing Schneider [Sch82b] ($\ell\ne p$), Bauer [Bau92] (good reduction), Milne [Mil75]) For an abelian variety $A/K$: if $\mathrm{Sha}(A/K)[\ell^\infty]$ is finite for one prime $\ell$ ($\ell=p$ allowed), then the full BSD conjecture (rank and leading term, in Tate's formulation) holds for $A/K$.

Mechanism (why finiteness at one $\ell$ suffices there). For non-constant $A$, $L(A,s)$ is a polynomial in $q^{-s}$: $\det(1-\mathrm{Frob}_q\,q^{-s}\mid H^1(\bar C,j_*V_\ell A))$ (Grothendieck), and $\mathrm{ord}_{s=1}L$ is the algebraic multiplicity of the eigenvalue $q$ of $\mathrm{Frob}_q$ on this weight-$2$ cohomology group. The $\ell$-adic Selmer group $H^1_f(K,V_\ell A)$ embeds into the corresponding eigenspace (Hochschild–Serre), which gives $\mathrm{rank}\,A(K)\le\mathrm{corank}\,\mathrm{Sel}_{\ell^\infty}\le(\text{geometric multiplicity})\le(\text{algebraic multiplicity})=\mathrm{ord}_{s=1}L$. Finiteness of $\mathrm{Sha}[\ell^\infty]$ makes the first inequality an equality; the non-degeneracy of the height pairing (equivalently of the intersection pairing on the Néron–Severi group of the associated surface, via Poincaré duality/Hodge index) then forces semisimplicity of Frobenius at the eigenvalue $1$ and equality throughout (Tate's argument [Tat66], made complete for surfaces in [Mil75] and for the $p$-part by [KT03]). Details in `approaches/D-function-field-analogy.md`.

**Proposition 2.13** (over $\mathbb{Q}$: what finiteness of $\mathrm{Sha}$ gives). [THEOREM] Let $E/\mathbb{Q}$ and suppose $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$ is finite for some prime $p$. Then:
(a) $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod 2$ (T6).
(b) $r_{\mathrm{alg}}=\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\le r_p$ if $p$ is good ordinary (T3); this is automatic and gives nothing about $r_{\mathrm{an}}$.
(c) If $r_{\mathrm{alg}}\le1$ and $(E,p)$ satisfies the hypotheses of T4 or T5, then $r_{\mathrm{an}}=r_{\mathrm{alg}}$.
(d) If $r_{\mathrm{an}}\le1$, then $r_{\mathrm{an}}=r_{\mathrm{alg}}$ regardless (T1).

**[GAP 2.14]** ("$\mathrm{Sha}$ finite $\Rightarrow$ rank BSD" over $\mathbb{Q}$) *Let $E/\mathbb{Q}$ with $r_{\mathrm{an}}\ge2$ (equivalently $w(E)=+1$ and $L(E,1)=0$, or $w(E)=-1$ and $L'(E,1)=0$). Assume $\mathrm{Sha}(E/\mathbb{Q})$ is finite. Prove $r_{\mathrm{alg}}=r_{\mathrm{an}}$.* This is not known for any such curve except those for which both sides have been computed (§5.3). Thus there is no known implication "$\mathrm{Sha}$ finite $\Rightarrow$ rank BSD" over $\mathbb{Q}$ beyond parity and the rank-$\le1$ converse theorems (c). What is missing, stated as two independent statements each of which is a theorem over function fields:

**[GAP 2.15]** (analytic rank bounded by Selmer corank) *For some prime $p$: $r_{\mathrm{an}}\le\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$.* Over function fields this is the step "algebraic multiplicity $=$ geometric multiplicity $=$ Selmer corank", which uses (i) a cohomological realisation of $L(E,s)$ as a characteristic polynomial on a finite-dimensional space containing the Selmer group and (ii) the non-degeneracy of a pairing on that space compatible with the height pairing. Over $\mathbb{Q}$ neither (i) nor (ii) has a known analogue for the complex $L$-function.

**[GAP 2.16]** (Selmer corank bounded by analytic rank) *For some prime $p$: $\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\le r_{\mathrm{an}}$.* Over function fields this is Tate's inequality. Over $\mathbb{Q}$ its $p$-adic shadow is Kato's theorem T3 ($\le r_p$); the statement with $r_{\mathrm{an}}$ would follow from T3 together with $r_p\le r_{\mathrm{an}}$ ([GAP 4.9]).

Given [GAP 2.15], [GAP 2.16] for the same $p$ and finiteness of $\mathrm{Sha}[p^\infty]$, one gets $r_{\mathrm{alg}}=\mathrm{corank}\,\mathrm{Sel}_{p^\infty}=r_{\mathrm{an}}$. The $p$-adic version of this programme is complete modulo two named conjectures:

**Proposition 2.17** ($p$-adic analogue of Tate–Milne). [THEOREM] (assembled from Kato [Kat04, Thm 17.4], Schneider [Sch85], Perrin-Riou [PR92]; formulation as in [SW13, Thm 6.1, Thm 7.3–7.4]) Let $p$ be an odd prime of good ordinary reduction for $E$, $X_\infty=\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$ with characteristic power series $f_E(T)$, and $L_p(E,T)$ as in §4. The following are equivalent:
(a) $r_p=r_{\mathrm{alg}}$;
(b) $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$ is finite, the canonical $p$-adic height pairing on $E(\mathbb{Q})$ is non-degenerate, and $(L_p/f_E)(0)\ne0$ (where $L_p/f_E\in\Lambda\otimes\mathbb{Q}_p$ by Kato).
Under the hypotheses of the main conjecture (Theorem 4.8(b)) the last condition in (b) is automatic.

*Proof.* By Kato (Theorem 5.8 below), $\mathrm{ord}_{T=0}f_E\le r_p$ with equality iff $(L_p/f_E)(0)\ne0$. By [SW13, Thm 6.1] (Schneider, Perrin-Riou), $\mathrm{ord}_{T=0}f_E\ge r_{\mathrm{alg}}$, with equality iff $\mathrm{Sha}[p^\infty]$ is finite and the $p$-adic height is non-degenerate. Combine. $\square$

So over $\mathbb{Q}$, "$\mathrm{Sha}[p^\infty]$ finite $\Rightarrow$ $p$-adic rank BSD ($r_p=r_{\mathrm{alg}}$)" holds exactly modulo Schneider's non-degeneracy conjecture ([GAP 4.10]) and the main conjecture; the remaining, entirely separate, obstacle is $r_p=r_{\mathrm{an}}$ ([GAP 4.9]).

---

## 3. The parity and $p$-parity conjectures

Let $E/K$ be an elliptic curve over a number field, $w(E/K)=\prod_vw_v(E/K_v)$ the global root number (a product of local root numbers, defined unconditionally), $\mathrm{rk}_p(E/K):=\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/K)=\mathrm{rank}\,E(K)+\delta_p(E/K)$.

[CONJECTURE] (Parity) $(-1)^{\mathrm{rank}\,E(K)}=w(E/K)$. [CONJECTURE] ($p$-parity) $(-1)^{\mathrm{rk}_p(E/K)}=w(E/K)$. Since $\delta_p\equiv0$ when $\mathrm{Sha}[p^\infty]$ is finite, $p$-parity for one $p$ together with finiteness of $\mathrm{Sha}(E/K)[p^\infty]$ implies parity; over $\mathbb{Q}$ parity is equivalent to $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod2$ by (0.6.1) [DD10, §1].

**Theorem 3.1** [THEOREM] (Dokchitser–Dokchitser [DD10, Thm 1.4 = Thm 4.19]; the case $p=2$ is due to Monsky [Mon96]) For every elliptic curve $E/\mathbb{Q}$ and every prime $p$, $\mathrm{rk}_p(E/\mathbb{Q})\equiv r_{\mathrm{an}}\pmod 2$. The proof for odd $p$ reduces, via a quadratic twist of analytic rank $\le1$ ([BFH90], [MM91], Waldspurger) and Kolyvagin (T1), to $E$ over an imaginary quadratic field $M_0$ in which all bad primes split, then to dihedral layers of the anticyclotomic $\mathbb{Z}_p$-extension, where a Brauer-relation formula for Selmer ranks [DD10, Prop 4.17] together with Cornut–Vatsal and Tian–Zhang/Yuan–Zhang–Zhang (or a result of Nekovář, cited as [29, Thm 3.2] in [DD10]) gives the parity. Earlier partial results, superseded over $\mathbb{Q}$ by this theorem: Nekovář ([Nek06, Ch. 12], [Nek07], [Nek09]; $p$ odd, under reduction-type hypotheses at $p$ stated in loc. cit.) and Kim [Kim07] (supersingular $p$, hypotheses as in loc. cit.).

**Corollary 3.2** [THEOREM] [DD10, Cor 4.20] For every $E/\mathbb{Q}$, either $r_{\mathrm{alg}}\equiv r_{\mathrm{an}}\pmod 2$ or $\mathrm{Sha}(E/\mathbb{Q})$ contains a copy of $\mathbb{Q}/\mathbb{Z}$ (indeed $(\mathbb{Q}_p/\mathbb{Z}_p)^{\delta_p}$ with $\delta_p$ odd for every $p$).

**Theorem 3.3** (number fields) (a) [CONDITIONAL] [DD11, Thm 1.2] Let $E/K$ be an elliptic curve over a number field and suppose $\mathrm{Sha}(E/K(E[2]))$ has finite $2$- and $3$-primary parts. Then $(-1)^{\mathrm{rank}\,E(K)}=w(E/K)$. (This is the precise form of "finiteness of $\mathrm{Sha}$ implies the parity conjecture over number fields"; the earlier [DD10, Thm 1.3] needed semistability at primes above $6$.) (b) [THEOREM] [DD11, Thm 1.8] If $E/K$ admits a $K$-rational isogeny of degree $p\in\{2,3\}$, then $p$-parity holds for $E/K$. (c) [THEOREM] (Česnavičius [Ces16]) If $E/K$ admits a $K$-rational $p$-isogeny with $p>3$, then $p$-parity holds for $E/K$; consequently $p$-parity holds for every $p$ for every CM elliptic curve $E/K$ (the CM being defined over $K$), and for such curves an infinite $\mathrm{Sha}(E/K)[p^\infty]$ must contain $(\mathbb{Q}_p/\mathbb{Z}_p)^2$. (d) [THEOREM] [DD11, Thm 1.7 and Nekovář as cited there] For $K$ totally real and $E/K$ with non-integral $j$-invariant, $p$-parity holds for all $p$ (Nekovář for odd $p$, [DD11, Thm 2.4] for $p=2$). (e) [THEOREM] [DD11, Cor 1.6] If $E$ is defined over a number field $K$, then for every quadratic extension $F/K$, $(-1)^{\mathrm{rk}_2(E/F)}=w(E/F)$ ($2$-parity over quadratic extensions of the field of definition; a consequence of the Kramer–Tunnell formula, [DD11, Thm 1.5]).

**[GAP 3.4]** *$p$-parity for a general elliptic curve over a general number field $K$ and a general prime $p$* (without isogeny, totally-real or finiteness hypotheses) is open; the parity conjecture itself is open without finiteness of $\mathrm{Sha}$. (Over $\mathbb{Q}$ everything is settled by Theorem 3.1.)

---

## 4. The Mazur–Tate–Teitelbaum $p$-adic conjecture

### 4.1 The $p$-adic $L$-function

Let $p$ be a prime of good or multiplicative reduction. Let $\alpha$ be a root of $X^2-a_pX+p$ with $\mathrm{ord}_p\alpha<1$ if $p\nmid N$ (unique if $p$ is ordinary, i.e. $p\nmid a_p$; two choices if supersingular), and $\alpha=a_p\in\{\pm1\}$ if $p\,\|\,N$. For $r\in\mathbb{Q}$ define the modular symbols
$$\lambda^+(r)=-\pi i\Bigl(\int_r^{i\infty}f_E(\tau)d\tau+\int_{-r}^{i\infty}f_E(\tau)d\tau\Bigr)\in\mathbb{R},\qquad [r]^+:=\lambda^+(r)/\Omega_E\in\mathbb{Q},$$
so that $[0]^+=L(E,1)/\Omega_E$ (rationality is Manin's theorem, Theorem 5.1; here $\Omega_E$ is the full real period of §0.2, with the factor $c_\infty$) [SW13, §3]. Following [MTT86, I §10] one defines a $\mathbb{Q}(\alpha)$-valued measure $\mu_\alpha$ on $\mathbb{Z}_p^\times$ by $\mu_\alpha(a+p^k\mathbb{Z}_p)=\alpha^{-k}[a/p^k]^+-\alpha^{-k-1}[a/p^{k-1}]^+$ (good reduction; drop the second term if $p\mid N$), and, for a topological generator $\gamma$ of $\Gamma=\mathrm{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$ with $\kappa(\gamma)\in1+p\mathbb{Z}_p$ (cyclotomic character; $p$ odd),
$$L_{p,\alpha}(E,T)=\int_{\mathbb{Z}_p^\times}(1+T)^{\log_p\langle x\rangle/\log_p\kappa(\gamma)}\,d\mu_\alpha(x)\in\mathbb{Q}_p(\alpha)[[T]],\qquad L_{p,\alpha}(E,s)=L_{p,\alpha}(E,\kappa(\gamma)^{s-1}-1).$$
For $p$ good ordinary we write $L_p(E,T)$ for the unique such series. Interpolation [MTT86, I §14], [SW13, §3.2]: with $\epsilon_p:=(1-\alpha^{-1})^2$ ($p\nmid N$), $\epsilon_p=1-\alpha^{-1}$ ($p\,\|\,N$; $=0$ split, $=2$ nonsplit),
$$L_{p,\alpha}(E,0)=\epsilon_p\cdot\frac{L(E,1)}{\Omega_E},\tag{4.1.2}$$
and for $\chi$ a character of $\Gamma$ of exact order $p^n$, $\zeta=\chi(\gamma)$: $L_{p,\alpha}(E,\zeta-1)=\alpha^{-n-1}\,\dfrac{p^{n+1}}{G(\chi^{-1})}\,\dfrac{L(E,\chi^{-1},1)}{\Omega_E}$. [THEOREM] (Rohrlich [Roh84]) $L_{p,\alpha}(E,T)\ne0$. [THEOREM] For $p>2$ good ordinary with $E[p]$ irreducible, $L_p(E,T)\in\mathbb{Z}_p[[T]]$ [SW13, Prop 3.7] (Greenberg–Vatsal).

Definition (charter): for $p$ good ordinary, $r_p:=\mathrm{ord}_{T=0}L_p(E,T)=\mathrm{ord}_{s=1}L_p(E,s)$, the $p$-adic analytic rank. By (4.1.2) and $\alpha\ne1$: $r_p=0\iff r_{\mathrm{an}}=0$.

### 4.2 The conjecture

Let $\hat h_p:E(\mathbb{Q})\to\mathbb{Q}_p$ be the canonical cyclotomic $p$-adic height (Schneider [Sch82a], Perrin-Riou, Mazur–Tate), normalised as in [SW13, (4.1)] (for $p$ good ordinary; the split multiplicative case uses the corrected height of [SW13, §4.2]), $\langle\,,\rangle_p$ the associated pairing, $\mathrm{Reg}_p(E/\mathbb{Q})$ its discriminant on $E(\mathbb{Q})/\mathrm{tors}$, and $\mathrm{Reg}_\gamma(E/\mathbb{Q}):=\mathrm{Reg}_p(E/\mathbb{Q})/(\log_p\kappa(\gamma))^{r_{\mathrm{alg}}}$ (this makes the leading term in $T$, rather than in $s$, the natural object). For $p$ split multiplicative let $q_E\in p\mathbb{Z}_p$ be the Tate period and $\mathcal{L}_p(E):=\log_p(q_E)/\mathrm{ord}_p(q_E)$ (nonzero by [BDGP96]).

[CONJECTURE] (Mazur–Tate–Teitelbaum [MTT86]; formulation with the above normalisations as in [SW13, Conj. 5.1]) Let $p$ be a prime of good ordinary or multiplicative reduction.
(rank) $\mathrm{ord}_{T=0}L_p(E,T)=r_{\mathrm{alg}}$ if $E$ is not split multiplicative at $p$, and $=r_{\mathrm{alg}}+1$ if it is (exceptional zero).
(leading term) With $L_p^*(E,0)$ the leading coefficient of $L_p(E,T)$ at $T=0$:
$$L_p^*(E,0)=\epsilon_p\cdot\frac{\prod_\ell c_\ell\cdot\#\mathrm{Sha}(E/\mathbb{Q})}{\#E(\mathbb{Q})_{\mathrm{tors}}^2}\cdot\mathrm{Reg}_\gamma(E/\mathbb{Q})\quad(\text{not split multiplicative}),\qquad L_p^*(E,0)=\frac{\mathcal{L}_p(E)}{\log_p\kappa(\gamma)}\cdot\frac{\prod_\ell c_\ell\cdot\#\mathrm{Sha}(E/\mathbb{Q})}{\#E(\mathbb{Q})_{\mathrm{tors}}^2}\cdot\mathrm{Reg}_\gamma(E/\mathbb{Q})\quad(\text{split multiplicative}).$$
The conjecture asserts exact equality (not just up to a $p$-adic unit); it presupposes $\mathrm{Sha}$ finite and the non-degeneracy of $\hat h_p$ ([GAP 4.10]). In [MTT86] the split multiplicative case is formulated with the "extended Mordell–Weil group" (adjoining the Tate period) and an extended regulator; the factorisation into $\mathcal{L}_p(E)\cdot\mathrm{Reg}$ displayed above is the form after the correction of the height normalisation in [Wer98], as explained in [SW13, §4.2]. (The full text of [MTT86] was not accessible for this document; its DOI and the restatement in [SW13], [Kat04, Conj. 18.2] were.) The supersingular analogue (Bernardi–Perrin-Riou, Pollack, Kobayashi) is [SW13, Conj. 5.2].

### 4.3 Status

**Theorem 4.3** [THEOREM] (Kato [Kat04, Thm 18.4]) The inequality $\le$ holds in the rank part: $\mathrm{rk}_p(E/\mathbb{Q})=r_{\mathrm{alg}}+\delta_p\le\mathrm{ord}_{T=0}L_{p,\alpha}(E,T)$ (resp. $\le\mathrm{ord}-1$ in the split multiplicative case), for all $p$ of good or multiplicative reduction and all admissible $\alpha$ (T3). In particular $r_{\mathrm{alg}}\le r_p$ for good ordinary $p$.

**Theorem 4.4** [THEOREM] (exceptional zero; Greenberg–Stevens [GS93] for $p\ge5$; Kobayashi [Kob06] for $p\ge3$ by a local method via Kato's Euler system; the case $p=2$ is asserted in [Dis20, §3.2] to follow from [Kob06] with modifications and is not independently verified here) If $E$ has split multiplicative reduction at $p$, then $\dfrac{d}{dT}L_p(E,T)\big|_{T=0}=\dfrac{\mathcal{L}_p(E)}{\log_p\kappa(\gamma)}\cdot\dfrac{L(E,1)}{\Omega_E}$. Hence MTT (rank and leading term) holds when $r_{\mathrm{an}}=0$ and $p$ is split multiplicative, in the *relative* form: the $p$-adic leading term equals $\mathcal{L}_p/\log_p\kappa(\gamma)$ times the complex leading term $L(E,1)/\Omega_E$ (which is $\#\mathrm{Sha}\prod c_\ell/\#\mathrm{tors}^2$ by BSD, known in this case only up to the $p$-part, T9).

**Theorem 4.5** [THEOREM] ($p$-adic Gross–Zagier; Perrin-Riou [PR87]; formulation [SW13, §9]) Let $p$ be an odd prime of good ordinary reduction and suppose $r_{\mathrm{an}}=1$, so $E(\mathbb{Q})$ has rank $1$ with generator $P$ (T1). If $\hat h_p(P)\ne0$ then
$$\frac{1}{\mathrm{Reg}(E/\mathbb{Q})}\cdot\frac{L'(E,1)}{\Omega_E}=\frac{1}{\mathrm{Reg}_p(E/\mathbb{Q})}\cdot\frac{\frac{d}{dT}L_p(E,T)|_{T=0}}{(1-\alpha^{-1})^2\log_p\kappa(\gamma)},$$
an equality of rational numbers. In particular $r_p=1$ iff $\hat h_p(P)\ne0$; in all cases $r_p\ge1$.

**Theorem 4.6** [CONDITIONAL] (Disegni [Dis20, Thm A]) Let $E/\mathbb{Q}$ have ordinary (good or multiplicative) reduction at $p$ and $r_{\mathrm{an}}\le1$; if $r_{\mathrm{an}}=1$ and $p$ is split multiplicative assume $p\ge5$ and that $E$ has another prime of multiplicative reduction. Then the $p$-adic BSD conjecture in its relative form (p-adic leading term versus complex leading term, in the formulation of loc. cit.) holds, including the exceptional-zero cases (Venerucci, Greenberg–Stevens, Perrin-Riou).

**Theorem 4.8** (main conjecture) Let $p$ be odd, good ordinary, $X_\infty=\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$.
(a) [THEOREM] (Kato [Kat04, Thm 17.4(1),(2)]) $X_\infty$ is $\Lambda$-torsion, and its characteristic power series $f_E$ divides $p^mL_p(E,T)$ in $\Lambda$ for some $m\ge0$ (no hypothesis on $\bar\rho_{E,p}$). [THEOREM] (Kato [Kat04, Thm 17.4(3)]) If moreover the image of $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}(\mu_{p^\infty}))\to\mathrm{Aut}(T_pE)$ contains $\mathrm{SL}_2(\mathbb{Z}_p)$ — e.g. $p\ge5$ and $\bar\rho_{E,p}$ surjective — then $f_E$ divides $L_p(E,T)$ in $\Lambda$ [SW13, Thm 7.3–7.4].
(b) [CONDITIONAL] (Skinner–Urban [SU14, Thm 1]) If $\bar\rho_{E,p}$ is irreducible and there exists $q\ne p$ with $q\,\|\,N$ and $\bar\rho_{E,p}$ ramified at $q$, then $(f_E)=(L_p(E,T))$ in $\Lambda$ (equality).
(c) [CONDITIONAL] (Castella–Grossi–Skinner [CGS25, Thm A]) If $p>2$ is a prime of good reduction and $E$ has a rational $p$-isogeny with kernel character $\phi$ satisfying $\phi|_{G_p}\ne1,\omega$, then $X_\infty$ is $\Lambda$-torsion and $(f_E)=(L_p(E,T))$ (a good Eisenstein prime is automatically ordinary, since $E[p]|_{G_{\mathbb{Q}_p}}$ is irreducible at supersingular $p$).
(d) [CONDITIONAL] (supersingular; Kobayashi's $\pm$ main conjecture) For $E$ semistable and $p>2$ supersingular ($p=3$ with condition (1.7) of loc. cit.), $(L^\pm_p(E))=\mathrm{char}(X^\pm(E))$ [BSTW24, Thm 1.3]; the earlier preprint [Wan14] is stated in [BSTW24, Rem. 1.4] to be superseded and no longer intended for publication.

**[GAP 4.9]** (no extra zeros) *For $p$ good ordinary: $r_p=r_{\mathrm{an}}$.* Known: $r_{\mathrm{an}}=0\iff r_p=0$; if $r_{\mathrm{an}}=1$ then $r_p\ge1$ with equality iff $\hat h_p(P)\ne0$ (Theorem 4.5). For $r_{\mathrm{an}}\ge2$ nothing is known in either direction beyond $r_p\ge r_{\mathrm{alg}}$ (T3). Note that $r_p=r_{\mathrm{an}}$ is a consequence of MTT (rank) together with BSD (rank), and conversely, given T3 and Proposition 2.17, is the only link between the $p$-adic and complex sides.

**[GAP 4.10]** (Schneider's conjecture [Sch82a]; [SW13, Conj. 4.1]) *For every good ordinary $p$, the canonical $p$-adic height pairing is non-degenerate on $E(\mathbb{Q})/\mathrm{tors}$, i.e. $\mathrm{Reg}_p(E/\mathbb{Q})\ne0$.* Known for rank $0$ (vacuous) and in scattered cases; for a given $(E,p)$ with $r_{\mathrm{alg}}$ known it is certifiable by a finite computation when true (§5.5), never refutable by computation.

Full Iwasawa-theoretic treatment: `approaches/A-iwasawa-padic.md`.

---

## 5. Certifiability for an individual curve with $r_{\mathrm{alg}}=2$

Reference curve: $E=389\mathrm{a}1$: $y^2+y=x^3+x^2-2x$, $N=\Delta=389$ (prime; multiplicative reduction, $c_{389}=1$), $E(\mathbb{Q})=\mathbb{Z}(0,0)\oplus\mathbb{Z}(1,0)$ (torsion-free, rank $2$), $w(E)=+1$, $\Omega_E=4.98042512171011\ldots$ ($c_\infty=2$), $\hat h((0,0))=0.32700077\ldots$, $\hat h((1,0))=0.47671165\ldots$, $\mathrm{Reg}(E/\mathbb{Q})=0.152460177943143\ldots$, $L''(E,1)/2=0.759316500288426\ldots$, $\mathcal{B}(E)=1.000\ldots$; optimal in its isogeny class, Manin constant $1$, modular degree $40$, non-CM, $\bar\rho_{E,p}$ surjective for every prime $p$ [LMFDB-389a1]. All numerics are to be reproduced in `compute/`.

### 5.1 Certifying the analytic rank

**Theorem 5.1** [THEOREM] (Manin [Man72]; Manin–Drinfeld [Man72], [Dri73]; Mazur [Maz77]) Let $\varphi:X_0(N)\to E$ be a modular parametrisation with $\varphi^*\omega_E=\pm c\,\omega_f$, $\omega_f=2\pi if_E(z)dz$, $c=c_E\in\mathbb{Z}_{\ge1}$ the Manin constant of $\varphi$. Let $n_E$ be the order of the divisor class $(0)-(\infty)$ in $J_0(N)(\mathbb{Q})$ (finite by Manin–Drinfeld; $n_E=\mathrm{num}\bigl(\tfrac{N-1}{12}\bigr)$ if $N$ is prime [Ogg74], [Maz77, Thm 1]). Then
$$c_\infty\,n_E\,c_E\cdot\frac{L(E,1)}{\Omega_E}=n_E\,c_E\cdot\frac{L(E,1)}{\Omega_E^+}\in\mathbb{Z}.$$
In particular $L(E,1)/\Omega_E\in\mathbb{Q}$, and $L(E,1)=0$ if and only if $|L(E,1)|<\Omega_E/(c_\infty n_Ec_E)$.

*Proof.* $L(f_E,1)=2\pi\int_0^\infty f_E(iy)\,dy=-\int_{\{0,\infty\}}\omega_f$ where $\{0,\infty\}$ is the path from $0$ to $i\infty$. The functional $\omega\mapsto\int_{\{0,\infty\}}\omega$ on $\Gamma(X_0(N),\Omega^1)$ represents the class of $(0)-(\infty)$ in $J_0(N)(\mathbb{C})=\Gamma(\Omega^1)^\vee/H_1(X_0(N),\mathbb{Z})$; since this class has order $n_E$, there is $\gamma_1\in H_1(X_0(N),\mathbb{Z})$ with $n_E\int_{\{0,\infty\}}\omega=\int_{\gamma_1}\omega$ for all $\omega$. Hence $n_EL(E,1)=\mp\int_{\gamma_1}\omega_f=\mp c^{-1}\int_{\gamma_1}\varphi^*\omega_E=\mp c^{-1}\int_{\varphi_*\gamma_1}\omega_E\in c^{-1}\Lambda_E$. As $L(E,1)\in\mathbb{R}$, $n_Ec\,L(E,1)\in\Lambda_E\cap\mathbb{R}=\mathbb{Z}\Omega_E^+$; finally $\Omega_E=c_\infty\Omega_E^+$. $\square$

[THEOREM] (Manin constant, optimal parametrisations) $c_E\in\mathbb{Z}$ (Edixhoven); if $p\mid c_E$ then $p^2\mid4N$ (Mazur), $p\mid N$ (Abbes–Ullmo), and $4\mid c_E\Rightarrow4\mid N$ (Raynaud) [ARS06, Thms 2.2–2.5] — so for odd $p$, $p\mid c_E$ forces additive reduction at $p$; $c_E=1$ for all optimal curves of conductor $\le130000$ (Cremona) [ARS06, Thm 2.6]; $c_E=\pm1$ for every semistable $E$ [Ces18]; in general $c_E$ is supported on the primes of additive reduction and $c_E\mid\deg\varphi$ under a mild condition at $2,3$ [CNS19, abstract]. For $389\mathrm{a}1$: $c_E=1$ (semistable, and verified), $n_E=97$, $c_\infty=2$, so $194\,L(E,1)/\Omega_E\in\mathbb{Z}$ and $L(E,1)=0$ follows from any rigorous bound $|L(E,1)|<\Omega_E/194=0.0256\ldots$; alternatively the exact modular symbol $[0]^+=L(E,1)/\Omega_E$ is computed by linear algebra over $\mathbb{Q}$ [Cre97, Ch. 2] and equals $0$.

**Proposition 5.2** [THEOREM] (rigorous numerics) For each $k\ge0$, $L^{(k)}(E,1)$ is computable to any prescribed accuracy with a proven error bound, from the $a_n$ ($n\le n_0$) and $N$, via the rapidly convergent series obtained from the functional equation (Buhler–Gross–Zagier [BGZ85, §2]; Cremona [Cre97, Prop. 2.13.1]; Dokchitser [Dok04]); the tails are bounded explicitly by incomplete-gamma-type integrals. Consequently a statement of the form $L^{(k)}(E,1)\ne0$, when true, is certifiable by a finite computation, and a statement $|L^{(k)}(E,1)|<\epsilon$ likewise; a statement $L^{(k)}(E,1)=0$ is not certifiable by numerics alone.

**Proposition 5.3** (even sign) [THEOREM] Let $w(E)=+1$. Then $r_{\mathrm{an}}\in\{0,2,4,\ldots\}$ by (0.6.1); $r_{\mathrm{an}}=0$ iff $[0]^+\ne0$ (Theorem 5.1, decidable exactly); if $L(E,1)=0$ then automatically $L'(E,1)=0$ (write $L=\Lambda\cdot\gamma^{-1}$ with $\gamma(s)=N^{s/2}(2\pi)^{-s}\Gamma(s)$; then $L'(1)=\Lambda'(1)/\gamma(1)$ when $\Lambda(1)=0$, and $\Lambda'(1)=0$ by evenness), and $r_{\mathrm{an}}=2$ iff $L''(E,1)\ne0$, which is certifiable when true (Proposition 5.2). Hence "$r_{\mathrm{an}}=2$" is a rigorously provable statement for any given curve for which it is true. For $389\mathrm{a}1$: $L(E,1)=0$ exactly (Theorem 5.1), $L'(E,1)=0$ (sign), and $L''(E,1)/2=0.7593\ldots\ne0$, so $r_{\mathrm{an}}(389\mathrm{a}1)=2$ modulo a certified evaluation of $L''(E,1)$ (to be recorded in `compute/RESULTS.md`; LMFDB's value is computed by Dokchitser's algorithm without a formal error certificate).

**Proposition 5.4** (odd sign) [THEOREM] (the method of Buhler–Gross–Zagier [BGZ85] for $5077\mathrm{a}1$, stated in general) Let $w(E)=-1$, so $L(E,1)=0$. Let $K$ be an imaginary quadratic field of discriminant $D$ with $(D,2N)=1$ in which every prime dividing $N$ splits, such that $L(E^K,1)\ne0$ (such $K$ exist by [BFH90], [MM91], and for a given $K$ the condition is decidable exactly by Theorem 5.1 applied to $E^K$). Let $y_K\in E(K)$ be the Heegner point. Then:
(a) [GZ86, Thm I.6.3; elliptic-curve form in Ch. V] $L'(E/K,1)=C_{E,K}\cdot\hat h_K(y_K)$ with $C_{E,K}>0$ an explicit constant (a positive rational multiple of $\|\omega_E\|^2/|D|^{1/2}$, the rational factor involving $u_K=\#\mathcal{O}_K^\times/2$ and $c_E$); and $L'(E/K,1)=L'(E,1)\,L(E^K,1)$ by Theorem 2.2(a) since $L(E,1)=0$. Hence $L'(E,1)=0\iff y_K\in E(K)_{\mathrm{tors}}$, and $L'(E,1)=0\Rightarrow L''(E,1)=0$ (with $\gamma$ as in Proposition 5.3 and $\Lambda(1)=\Lambda''(1)=0$ by oddness, $L''(1)=-2\Lambda'(1)\gamma'(1)/\gamma(1)^2$, which vanishes iff $\Lambda'(1)=0$ iff $L'(1)=0$), so then $r_{\mathrm{an}}\ge3$.
(b) $y_K\in E(K)_{\mathrm{tors}}$ is certifiable when true: let $\lambda>0$ be a proven lower bound for $\hat h_K$ on non-torsion points of $E(K)$ (computable: Thongjunthug [Tho10], using the height-difference bounds of Cremona–Prickett–Siksek [CPS06]); compute a rigorous bound $|L'(E,1)|\le\epsilon$ (Proposition 5.2) with $\epsilon\,|L(E^K,1)|/C_{E,K}<\lambda$; then $\hat h_K(y_K)<\lambda$ forces $y_K$ torsion. (Since $w(E)=-1$, $2y_K\in E(\mathbb{Q})+E(K)_{\mathrm{tors}}$ [Gro91], so one may instead use a height lower bound over $\mathbb{Q}$ [CS06].)
(c) If (b) succeeds and $L'''(E,1)\ne0$ is certified, then $r_{\mathrm{an}}=3$.
Thus "$r_{\mathrm{an}}=3$" is rigorously provable for any curve for which it is true; this was carried out for $5077\mathrm{a}1$ in [BGZ85].

**Remark 5.4.1** (rationality in rank one) [THEOREM] (Gross–Zagier + Manin; standard) Suppose $r_{\mathrm{an}}=1$, so $r_{\mathrm{alg}}=1$ (T1) with $E(\mathbb{Q})/\mathrm{tors}=\mathbb{Z}P$. Choose $K$ as in Proposition 5.4 with $L(E^K,1)\ne0$. Since $w(E)=-1$, $2y_K=mP+t$ with $m\in\mathbb{Z}\setminus\{0\}$, $t$ torsion [Gro91], so $\hat h_K(y_K)=\tfrac{m^2}{4}\hat h_K(P)=\tfrac{m^2}{2}\hat h(P)$. By (a), $L'(E,1)\,L(E^K,1)\in\mathbb{Q}^\times\cdot\dfrac{\|\omega_E\|^2}{|D|^{1/2}}\,\hat h(P)$, with $\|\omega_E\|^2=\Omega_E\Omega_E^-$ by (0.2.1). By Theorem 5.1, $L(E^K,1)\in\mathbb{Q}^\times\Omega_{E^K}$, and the period lattice of $E^K$ is $\Lambda_E/\sqrt D$ up to a rational factor (change of minimal model), so $\Omega_{E^K}\in\mathbb{Q}^\times\cdot\Omega_E^-/|D|^{1/2}$. Dividing, $L'(E,1)/(\Omega_E\,\hat h(P))\in\mathbb{Q}^\times$, i.e. $\mathcal{B}(E)\in\mathbb{Q}^\times$ in rank one. Together with Theorem 5.1 this is item (iii) of Definition 1.3 for $r_{\mathrm{alg}}\le1$.

**[GAP 5.5]** (no vanishing certificate beyond the first derivative) *Let $w(E)=+1$ and $L(E,1)=0$. Give a criterion, decidable by a finite exact computation, for $L''(E,1)=0$.* Manin's theorem does this for $L(E,1)$ (rationality with bounded denominator) and Gross–Zagier for $L'(E,1)$ (torsionness of an algebraic point); no analogue is known for $L''(E,1)$ (or for $L'''(E,1)$ when $w=-1$). Consequently $r_{\mathrm{an}}\ge4$ cannot be established for any curve by known methods, and BSD (rank) is not provable for any curve of rank $\ge4$ by known methods (the same remark is made in [LMFDB-5077a1]). A solution of [GAP 5.5] for all $E$ would be a "rank-two Gross–Zagier formula": $L''(E,1)$ as an algebraic quantity vanishing iff some canonical algebraic object (e.g. a class in $\bigwedge^2$ of a Selmer group, cf. the generalised Kato classes of Darmon–Rotger and [CH22]) vanishes; see `approaches/C-higher-rank-euler-systems-diagonal-cycles.md`.

### 5.2 Certifying the algebraic rank

[THEOREM] (descent; Cremona [Cre97], Schaefer–Stoll [SS04]) For each $m\ge2$ the $m$-Selmer group $\mathrm{Sel}_m(E/\mathbb{Q})$ is computable, giving $r_{\mathrm{alg}}\le\dim_{\mathbb{F}_p}\mathrm{Sel}_p(E/\mathbb{Q})-\dim_{\mathbb{F}_p}E(\mathbb{Q})[p]$ for each prime $p$; equality holds iff $\mathrm{Sha}(E/\mathbb{Q})[p]=0$. Lower bounds come from explicit points; linear independence of $P_1,\dots,P_r$ modulo torsion is certified by $\det(\langle P_i,P_j\rangle)\ne0$ computed with rigorous error bounds (canonical heights are computable to any accuracy with proven bounds), or by reduction modulo primes. Saturation (that the found points generate $E(\mathbb{Q})/\mathrm{tors}$) is certified by the standard sieving/saturation algorithms with an index bound from height-difference estimates [CPS06]. For $389\mathrm{a}1$: $\dim_{\mathbb{F}_2}\mathrm{Sel}_2=2$ and $E(\mathbb{Q})[2]=0$, so $r_{\mathrm{alg}}\le2$; the points $(0,0),(1,0)$ are independent ($\mathrm{Reg}\ne0$) and generate; hence $r_{\mathrm{alg}}=2$ and $\mathrm{Sha}(E/\mathbb{Q})[2]=0$, whence $\mathrm{Sha}(E/\mathbb{Q})[2^\infty]=0$ [LMFDB-389a1] (rank bounds $[2,2]$ from $2$-descent).

### 5.3 What is and is not provable for $389\mathrm{a}1$

**Proposition 5.6** [THEOREM, modulo the certified numerics of Proposition 5.3] BSD (rank) holds for $389\mathrm{a}1$: $r_{\mathrm{an}}=r_{\mathrm{alg}}=2$. The same holds for every curve with $r_{\mathrm{alg}}\in\{2,3\}$ for which the computations of §5.1–5.2 succeed; the computations succeed whenever BSD (rank) and $r_{\mathrm{an}}\le3$ are true.

For the leading term, the analytic order $\mathcal{B}(E)=1.000\ldots$ suggests $\mathrm{Sha}(E/\mathbb{Q})=0$. The following is the exact status.

(a) [GAP 1.3 for this curve] It is not known that $\mathcal{B}(E)\in\mathbb{Q}$; a fortiori not that $\mathcal{B}(E)=1$.
(b) [GAP 5.6a] It is not known that $\mathrm{Sha}(E/\mathbb{Q})$ is finite. The only general finiteness theorem (T1) requires $r_{\mathrm{an}}\le1$: Kolyvagin's Euler system of Heegner points is built from a point $y_K$ which is torsion when $r_{\mathrm{an}}(E/K)\ge2$, and Kato's Euler system controls $\mathrm{Sel}$ only when $L(E,\chi,1)\ne0$ for the relevant characters. Descent bounds $\mathrm{Sha}[p]$ for one prime $p$ at a time and is impractical beyond very small $p$; it cannot address all $p$.
(c) [THEOREM] What is known: $\mathrm{Sha}(E/\mathbb{Q})[2^\infty]=0$ (§5.2); $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]=0$ for every good ordinary prime $5\le p<1000$ [SW13, Thm 1.1] (this theorem covers exactly the pairs $(E,p)$ with $E$ non-CM of conductor $\le30000$, rank $\ge2$, $p\ge5$ good ordinary, $p<1000$, $\bar\rho_{E,p}$ surjective; $389\mathrm{a}1$ qualifies for all such $p$; the theorem is stated there as $\mathrm{Sha}[p]=0$, but the method bounds $\#\mathrm{Sha}[p^\infty]$, so the conclusion is $\mathrm{Sha}[p^\infty]=0$). The method is §5.4; for $p=3$ (good ordinary for $389\mathrm{a}1$, since $a_3=-2$) and for supersingular $p<1000$ the same method applies but no published certificate was located, and for $p\ge1000$ nothing is recorded.

### 5.4 What Iwasawa theory proves for individual $(E,p)$

**Lemma 5.7** [THEOREM] (structure of $\Lambda$-modules) Let $\Lambda=\mathbb{Z}_p[[T]]$ and $X$ a finitely generated torsion $\Lambda$-module with characteristic power series $f_X$ (defined up to $\Lambda^\times$). Then
$$\mathrm{rank}_{\mathbb{Z}_p}(X/TX)=\mathrm{rank}_{\mathbb{Z}_p}(X[T])\le\mathrm{ord}_{T=0}f_X,$$
with equality iff in a pseudo-isomorphism $X\sim\bigoplus_i\Lambda/(f_i)\oplus\bigoplus_j\Lambda/(p^{m_j})$ every $f_i$ with $f_i(0)=0$ has a simple zero at $T=0$.

*Proof.* (1) $\mathrm{rank}_{\mathbb{Z}_p}(M/TM)$ is invariant under pseudo-isomorphism $M\to N$ (finite kernel $C_0$, finite cokernel $C_1$): with $M'=M/C_0$, the sequences $C_0/TC_0\to M/TM\to M'/TM'\to0$ and $C_1[T]\to M'/TM'\to N/TN\to C_1/TC_1\to0$ (snake lemma for multiplication by $T$) are exact with finite end terms. (2) For $M=\Lambda/(g)$, $g\ne0$: $M/TM=\mathbb{Z}_p/(g(0))$ has rank $1$ if $g(0)=0$ and is finite otherwise; $M[T]=(g/T)\Lambda/(g)\cong\Lambda/(T)=\mathbb{Z}_p$ if $T\mid g$ and $M[T]=0$ otherwise ($\Lambda$ is a UFD); for $M=\Lambda/(p^m)$ both are finite. (3) Summing over the elementary summands, $\mathrm{rank}(X/TX)=\mathrm{rank}(X[T])=\#\{i:f_i(0)=0\}\le\sum_i\mathrm{ord}_{T=0}f_i=\mathrm{ord}_{T=0}f_X$, with equality iff each vanishing $f_i$ vanishes simply. $\square$

**Theorem 5.8** [THEOREM] (the chain, with exact hypotheses) Let $p$ be an odd prime of good ordinary reduction for $E/\mathbb{Q}$. Then
$$r_{\mathrm{alg}}\ \le\ r_{\mathrm{alg}}+\delta_p=\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\ \le\ \mathrm{ord}_{T=0}f_E\ \le\ r_p=\mathrm{ord}_{T=0}L_p(E,T)<\infty.$$
*Proof.* (i) Kato [Kat04, Thm 17.4(1)]: $X_\infty$ is $\Lambda$-torsion, so $f_E$ is defined; $L_p(E,T)\ne0$ by Rohrlich [Roh84], so $r_p<\infty$. (ii) Kato [Kat04, Thm 17.4(2)]: $f_E\mid p^mL_p(E,T)$ in $\Lambda$ for some $m$; write $p^mL_p=f_Eg$ with $g\in\Lambda$; since $\mathrm{ord}_{T=0}$ is additive on $\Lambda\setminus\{0\}$ and non-negative, $\mathrm{ord}_{T=0}f_E\le\mathrm{ord}_{T=0}L_p=r_p$. (iii) Mazur's control theorem [Maz72], [Gre99, Thm 1.2] ($p$ good ordinary): $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\to\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\Gamma$ has finite kernel and cokernel, so $\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})=\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\Gamma=\mathrm{rank}_{\mathbb{Z}_p}(X_\infty/TX_\infty)$ (Pontryagin duality: the dual of the $T$-kernel of a discrete module is the $T$-cokernel of its dual). (iv) Lemma 5.7. $\square$
No hypothesis on $\bar\rho_{E,p}$, on CM, or on $N$ is used. The resulting inequality $\mathrm{corank}\,\mathrm{Sel}_{p^\infty}\le r_p$ is stated directly, and more generally (supersingular and multiplicative $p$, no parity restriction on $p$), as Kato's Theorem 18.4 (T3), whose proof in the case $\alpha\ne1$ Kato attributes to Perrin-Riou.

**Proposition 5.9** (certificate for finiteness of $\mathrm{Sha}[p^\infty]$) [THEOREM] (Kato; Schneider–Perrin-Riou; this is the content of [SW13, Prop. 10.1, Alg. 11.1 step 3, Prop. 11.2] and the argument of [SW13, §7.1]) Let $p$ be an odd prime of good ordinary reduction, and let $r\ge0$ be such that $E(\mathbb{Q})$ contains $r$ points independent modulo torsion (so $r\le r_{\mathrm{alg}}$). Suppose the coefficient of $T^r$ in $L_p(E,T)$ is nonzero. Then:
(i) $r_{\mathrm{alg}}=r$ (an unconditional upper bound for the rank);
(ii) $\mathrm{corank}\,\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})=r$, i.e. $\delta_p=0$: $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$ is finite;
(iii) $r_p=r$ and $\mathrm{ord}_{T=0}f_E=r$;
(iv) the $p$-adic height pairing on $E(\mathbb{Q})$ is non-degenerate (Schneider's conjecture [GAP 4.10] holds for $(E,p)$), and $(L_p/f_E)(0)\ne0$;
(v) if in addition the image of $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}(\mu_{p^\infty}))$ in $\mathrm{Aut}(T_pE)$ contains $\mathrm{SL}_2(\mathbb{Z}_p)$ (e.g. $p\ge5$, $\bar\rho_{E,p}$ surjective), then
$$\mathrm{ord}_p\#\mathrm{Sha}(E/\mathbb{Q})[p^\infty]\le b_p:=\mathrm{ord}_p L_p^*(E,0)-\mathrm{ord}_p\epsilon_p-\sum_\ell\mathrm{ord}_pc_\ell-\mathrm{ord}_p\mathrm{Reg}_\gamma(E/\mathbb{Q})+2\,\mathrm{ord}_p\#E(\mathbb{Q})[p^\infty],$$
with equality if the main conjecture holds for $(E,p)$ (e.g. under Theorem 4.8(b)).
Certifiability: the coefficients of $L_p(E,T)$ are computable to any $p$-adic precision with proven error bounds by Riemann sums of modular symbols [SW13, Prop. 3.5–3.6]; the hypothesis "coefficient of $T^r$ nonzero" is verified by a finite computation exhibiting a nonzero residue modulo $p^n$; $\mathrm{Reg}_\gamma$ is computable with proven precision [MST06]. Conversely, if $\mathrm{Sha}[p^\infty]$ is finite, $\hat h_p$ non-degenerate and the main conjecture holds, the hypothesis is true and the computation terminates.

*Proof.* By Theorem 5.8, $r\le r_{\mathrm{alg}}\le r_{\mathrm{alg}}+\delta_p\le\mathrm{ord}_{T=0}f_E\le r_p$. The hypothesis gives $r_p\le r$. Hence all inequalities are equalities: (i), (ii), (iii). Then $(L_p/f_E)(0)\ne0$ (equality in step (ii) of Theorem 5.8), and equality $\mathrm{ord}_{T=0}f_E=r_{\mathrm{alg}}$ gives non-degeneracy of the $p$-adic height by [SW13, Thm 6.1] (Schneider [Sch85], Perrin-Riou [PR92]): (iv). For (v), [SW13, Thm 6.1] gives $\mathrm{ord}_pf_E^*(0)=\mathrm{ord}_p\bigl(\epsilon_p\prod c_\ell\#\mathrm{Sha}[p^\infty]\mathrm{Reg}_\gamma/\#E(\mathbb{Q})[p^\infty]^2\bigr)$, and Kato's integral divisibility (Theorem 4.8(a)) with $\mathrm{ord}_{T=0}f_E=\mathrm{ord}_{T=0}L_p$ gives $\mathrm{ord}_pf_E^*(0)\le\mathrm{ord}_pL_p^*(E,0)$, with equality iff $L_p/f_E\in\Lambda^\times$. $\square$

**Corollary 5.10** [THEOREM] For $E=389\mathrm{a}1$ and every good ordinary prime $5\le p<1000$: $r_p=2$, $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]=0$, the $p$-adic height pairing is non-degenerate, and the main conjecture $(f_E)=(L_p)$ holds [SW13, Thm 1.1 (stated as $\mathrm{Sha}[p]=0$; the algorithm bounds $\#\mathrm{Sha}[p^\infty]$) and the remark in §11.1 there]. (For $389\mathrm{a}1$ the Skinner–Urban hypotheses of Theorem 4.8(b) hold at every odd good ordinary $p$: $\bar\rho_{E,p}$ is surjective, and $\bar\rho_{E,p}$ is ramified at $q=389$ because $p\nmid\mathrm{ord}_{389}\Delta=1$ [SW13, remark after Thm 7.5]; so the main conjecture is known there independently of the computation, and $\#\mathrm{Sha}[p^\infty]=p^{b_p}$ exactly once $\mathrm{Reg}_\gamma$ and $L_p^*$ are computed.)

Remark (anticyclotomic alternative). Castella–Hsieh [CH22, Thm A–B] give, for $p>3$ good ordinary, $w(E)=+1$, $L(E,1)=0$, $\mathrm{rank}\,E(\mathbb{Q})>0$, and suitable auxiliary $(K,\chi)$ with $\bar\rho_{E,p}$ irreducible and ramified at the primes of $N$ inert in $K$: if the anticyclotomic $p$-adic $L$-function $\Theta_{f/K}$ vanishes to order exactly $2$ at the trivial character, then the generalised Kato class $\kappa\ne0$ and $\dim_{\mathbb{Q}_p}\mathrm{Sel}(\mathbb{Q},V_pE)=2$; for a rank-$2$ curve this again certifies $\delta_p=0$ from a $p$-adic computation. This is the rank-$2$ analogue of Kolyvagin's and Skinner's implications; details in `approaches/C-higher-rank-euler-systems-diagonal-cycles.md`.

### 5.5 What this does and does not give

Does: for each individual pair $(E,p)$ with $p$ odd good ordinary, a *finite* computation proves finiteness of $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]$, an unconditional upper bound for $r_{\mathrm{alg}}$, Schneider's conjecture for $(E,p)$, and (with surjective $\bar\rho_{E,p}$) an upper bound for $\#\mathrm{Sha}[p^\infty]$ that is sharp under the main conjecture — hence, for $389\mathrm{a}1$, the exact value $\#\mathrm{Sha}[p^\infty]=1$ for all good ordinary $5\le p<1000$. Combined with $2$-descent this gives $\mathrm{Sha}(389\mathrm{a}1)[p^\infty]=0$ for $p=2$ and all good ordinary $5\le p<1000$.

Does not: (a) finiteness of $\mathrm{Sha}(E/\mathbb{Q})$: this needs $\delta_p=0$ for *all* $p$, and the certificate is one computation per prime with no uniformity in $p$; the certificate's success at $p$ is equivalent (Proposition 2.17) to "$r_p=r_{\mathrm{alg}}$", a statement which is expected for all $p$ (MTT) but proven only one prime at a time. (b) Even "$\mathrm{Sha}[p^\infty]$ finite for all $p$" for $389\mathrm{a}1$ is unknown. (c) The bound $b_p$ is only an upper bound without the main conjecture; and for $p\ge5$ non-surjective or additive or $p=2$ the method is not available as stated. (d) Nothing about $r_{\mathrm{an}}$: the certificates live entirely on the $p$-adic side.

**[GAP 5.11]** (uniformity) *For $E=389\mathrm{a}1$ (or any curve with $r_{\mathrm{alg}}\ge2$), prove $\mathrm{Sha}(E/\mathbb{Q})[p^\infty]=0$ for all sufficiently large $p$*, equivalently (by Proposition 2.17 and Theorem 4.8(b)) $r_p=2$ for all large good ordinary $p$, i.e. the $T^2$-coefficient of $L_p(E,T)$ is nonzero for all large $p$. No approach to such a uniform statement is known; it would follow from BSD (leading term) since then $\mathrm{Sha}$ is finite.

---

## 6. What a proof must contain

### 6.1 Rank

For a given $E/\mathbb{Q}$, BSD (rank) is equivalent to the conjunction of the two independent statements
- **(R$\le$)** $r_{\mathrm{alg}}\le r_{\mathrm{an}}$. Status: [THEOREM] if $r_{\mathrm{an}}\le1$ (T1); [THEOREM by computation] for individual curves with $r_{\mathrm{an}}\le3$ once $r_{\mathrm{an}}$ is certified (§5.1) and $r_{\mathrm{alg}}$ is bounded above by descent (§5.2); otherwise [GAP 2.10].
- **(R$\ge$)** $r_{\mathrm{an}}\le r_{\mathrm{alg}}$. Status: [THEOREM] if $r_{\mathrm{an}}\le1$ (T1); [THEOREM by computation] for individual curves with $r_{\mathrm{an}}\le3$ (exhibit points); otherwise [GAP 2.10].

Alternatively, via the $p$-adic side: for a fixed odd good ordinary $p$, BSD (rank) is implied by the conjunction of the following three statements, and their conjunction is equivalent to [BSD (rank) $\wedge$ MTT (rank) at $p$]:
- **(R$'_1$)** $r_{\mathrm{alg}}\le r_p$: [THEOREM] (Kato, T3), unconditional.
- **(R$'_2$)** $r_p\le r_{\mathrm{alg}}$: equivalent (Proposition 2.17) to [$\mathrm{Sha}[p^\infty]$ finite] $\wedge$ [$\hat h_p$ non-degenerate, GAP 4.10] $\wedge$ [$(L_p/f_E)(0)\ne0$, a consequence of the main conjecture, Theorem 4.8(b)–(d)]. Status: [CONDITIONAL]; certifiable for individual $(E,p)$ (Proposition 5.9).
- **(R$'_3$)** $r_p=r_{\mathrm{an}}$: [GAP 4.9]. Known iff $r_{\mathrm{an}}\le1$ (with $\hat h_p(P)\ne0$ when $r_{\mathrm{an}}=1$).

The second list isolates the analytic–$p$-adic comparison (R$'_3$) as the single statement with no known approach; (R$'_1$) is done and (R$'_2$) is a conjunction of finiteness of $\mathrm{Sha}$, a non-degeneracy statement, and the main conjecture.

### 6.2 Leading term

For a given $E/\mathbb{Q}$, BSD (leading term) is equivalent (Proposition 1.4) to the conjunction of
- **(L$_0$)** BSD (rank), as above.
- **(L$_1$)** Rationality: $\mathcal{B}(E)\in\mathbb{Q}$. Status: [THEOREM] for $r_{\mathrm{alg}}\le1$ (Manin; Gross–Zagier + Manin); [GAP 1.3] for $r_{\mathrm{alg}}\ge2$, for every curve.
- **(L$_2$)$_p$** for every prime $p$: $\mathrm{Sha}[p^\infty]$ finite and $\mathrm{ord}_p\mathcal{B}(E)=\mathrm{ord}_p\#\mathrm{Sha}[p^\infty]$ (this is $\mathrm{BSD}_p$ given (L$_0$), (L$_1$); equivalent to TNC$_p$ for $h^1(E)(1)$ when $\mathrm{Sha}$ is finite and $p$ odd, Theorem 2.9). Status: [CONDITIONAL] for $r_{\mathrm{an}}\le1$ and $p$ satisfying the hypotheses in T9; open for $p=2$, for additive $p$ in general, and for all $p$ when $r_{\mathrm{an}}\ge2$ (where even finiteness of $\mathrm{Sha}[p^\infty]$ is known only for individual $(E,p)$, §5.4).

Finiteness of $\mathrm{Sha}$ is not a separate item: it follows from (L$_1$) and (L$_2$)$_p$ for all $p$ (Proposition 1.4). Conversely no item of the list is known to imply another in general.

### 6.3 Dependencies to be tracked in `synthesis/proof-architecture.md`

(1) All statements are isogeny-invariant (Theorem 2.1), so a proof may assume $E$ optimal with $c_E=1$ when $N$ is squarefree [Ces18]. (2) Quadratic base change reduces nothing in general ([GAP 2.3], [GAP 2.6]) but Proposition 2.4 and Theorem 2.5 record the exact directions that are free. (3) Parity is fully available over $\mathbb{Q}$ (Theorem 3.1) and reduces the rank problem for $r_{\mathrm{an}}\ge2$ to an even/odd gap of size $\ge2$ only when $\mathrm{Sha}[p^\infty]$ is finite for some $p$. (4) The function-field proof (Theorem 2.12) cannot be transported: its two inputs, [GAP 2.15] and [GAP 2.16], have $p$-adic shadows (Proposition 2.17, T3) but no complex-analytic analogue; the complex/$p$-adic link is [GAP 4.9]. (5) For any single curve of rank $2$ or $3$ the rank conjecture is a finite computation (§5.1–5.3), the finiteness of $\mathrm{Sha}[p^\infty]$ is a finite computation for each odd good ordinary $p$ (Proposition 5.9), and the rationality (L$_1$) is the first statement that no computation can reach.

---

## 7. References (all identifiers checked 2026-09-11)

- [ARS06] A. Agashe, K. Ribet, W. Stein, *The Manin constant*, Pure Appl. Math. Q. 2 (2006), 617–636. DOI 10.4310/PAMQ.2006.v2.n2.a11.
- [Bau92] W. Bauer, *On the conjecture of Birch and Swinnerton-Dyer for abelian varieties over function fields in characteristic $p>0$*, Invent. Math. 108 (1992), 263–287. DOI 10.1007/BF02100606.
- [BCDT01] C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises*, J. Amer. Math. Soc. 14 (2001), 843–939. DOI 10.1090/S0894-0347-01-00370-8.
- [BDGP96] K. Barré-Sirieix, G. Diaz, F. Gramain, G. Philibert, *Une preuve de la conjecture de Mahler–Manin*, Invent. Math. 124 (1996), 1–9 (cited via [SW13, §3.4]; not fetched).
- [BF96] D. Burns, M. Flach, *Motivic $L$-functions and Galois module structures*, Math. Ann. 305 (1996), 65–102. DOI 10.1007/BF01444212.
- [BF01] D. Burns, M. Flach, *Tamagawa numbers for motives with (non-commutative) coefficients*, Doc. Math. 6 (2001), 501–570. DOI 10.4171/dm/113.
- [BFH90] D. Bump, S. Friedberg, J. Hoffstein, *Eisenstein series on the metaplectic group and nonvanishing theorems for automorphic $L$-functions and their derivatives*, Ann. of Math. 131 (1990), 53–127. DOI 10.2307/1971508.
- [BGZ85] J. Buhler, B. Gross, D. Zagier, *On the conjecture of Birch and Swinnerton-Dyer for an elliptic curve of rank 3*, Math. Comp. 44 (1985), 473–481. DOI 10.1090/S0025-5718-1985-0777279-X.
- [BK90] S. Bloch, K. Kato, *L-functions and Tamagawa numbers of motives*, The Grothendieck Festschrift I, Progr. Math. 86, Birkhäuser 1990, 333–400. DOI 10.1007/978-0-8176-4574-8_9.
- [BMC19] D. Burns, D. Macias Castillo, *On refined conjectures of Birch and Swinnerton-Dyer type for Hasse–Weil–Artin $L$-series*, arXiv:1909.03959.
- [BSD65] B. Birch, H. P. F. Swinnerton-Dyer, *Notes on elliptic curves. II*, J. Reine Angew. Math. 218 (1965), 79–108 (standard reference; not fetched).
- [BSTW24] A. Burungale, C. Skinner, Y. Tian, X. Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350.
- [BSZ14] M. Bhargava, C. Skinner, W. Zhang, *A majority of elliptic curves over $\mathbb{Q}$ satisfy the Birch and Swinnerton-Dyer conjecture*, arXiv:1407.1826.
- [BT20] A. Burungale, Y. Tian, *p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, Invent. Math. 220 (2020), 211–253. DOI 10.1007/s00222-019-00929-7.
- [Cas62] J. W. S. Cassels, *Arithmetic on curves of genus 1. IV. Proof of the Hauptvermutung*, J. Reine Angew. Math. 211 (1962), 95–112 (standard; not fetched).
- [Cas65] J. W. S. Cassels, *Arithmetic on curves of genus 1. VIII. On conjectures of Birch and Swinnerton-Dyer*, J. Reine Angew. Math. 217 (1965), 180–199. DOI 10.1515/crll.1965.217.180.
- [Ces16] K. Česnavičius, *The $p$-parity conjecture for elliptic curves with a $p$-isogeny*, J. Reine Angew. Math. 719 (2016), 45–73; arXiv:1207.0431.
- [Ces18] K. Česnavičius, *The Manin constant in the semistable case*, Compos. Math. 154 (2018), 1889–1920. DOI 10.1112/S0010437X18007273; arXiv:1703.02951.
- [CGLS22] F. Castella, G. Grossi, J. Lee, C. Skinner, *On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes*, Invent. Math. 227 (2022), 517–580. DOI 10.1007/s00222-021-01072-y.
- [CGS25] F. Castella, G. Grossi, C. Skinner, *Mazur's main conjecture at Eisenstein primes*, Math. Ann. 393 (2025), 2451–2506; arXiv:2303.04373.
- [CH22] F. Castella, M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum Math. Sigma 10 (2022), e12. DOI 10.1017/fms.2021.85; arXiv:1809.09066.
- [CNS19] K. Česnavičius, M. Neururer, A. Saha, *The Manin constant and the modular degree*, arXiv:1911.09446.
- [CPS06] J. Cremona, M. Prickett, S. Siksek, *Height difference bounds for elliptic curves over number fields*, J. Number Theory 116 (2006), 42–68. DOI 10.1016/j.jnt.2005.03.001.
- [CS06] J. Cremona, S. Siksek, *Computing a lower bound for the canonical height on elliptic curves over $\mathbb{Q}$*, ANTS VII, Lecture Notes in Comput. Sci. 4076 (2006), 275–286. DOI 10.1007/11792086_20.
- [Cre97] J. Cremona, *Algorithms for modular elliptic curves*, 2nd ed., Cambridge Univ. Press, 1997 (standard; not fetched).
- [DD10] T. Dokchitser, V. Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, Ann. of Math. 172 (2010), 567–596. DOI 10.4007/annals.2010.172.567; arXiv:math/0610290.
- [DD11] T. Dokchitser, V. Dokchitser, *Root numbers and parity of ranks of elliptic curves*, J. Reine Angew. Math. 658 (2011), 39–64. DOI 10.1515/crelle.2011.060; arXiv:0906.1815.
- [Del79] P. Deligne, *Valeurs de fonctions $L$ et périodes d'intégrales*, Proc. Sympos. Pure Math. 33, part 2 (1979), 313–346. DOI 10.1090/pspum/033.2/546622.
- [DEW21] V. Dokchitser, R. Evans, H. Wiersema, *On a BSD-type formula for $L$-values of Artin twists of elliptic curves*, arXiv:1905.04282.
- [Dis20] D. Disegni, *On the $p$-adic Birch and Swinnerton-Dyer conjecture for elliptic curves over number fields*, Kyoto J. Math. 60 (2020). DOI 10.1215/21562261-2018-0012.
- [Dok04] T. Dokchitser, *Computing special values of motivic $L$-functions*, Experiment. Math. 13 (2004), 137–149. DOI 10.1080/10586458.2004.10504528.
- [Dri73] V. Drinfeld, *Two theorems on modular curves*, Funct. Anal. Appl. 7 (1973), 155–156. DOI 10.1007/BF01078890.
- [FPR94] J.-M. Fontaine, B. Perrin-Riou, *Autour des conjectures de Bloch et Kato: cohomologie galoisienne et valeurs de fonctions $L$*, Proc. Sympos. Pure Math. 55, part 1 (1994), 599–706. DOI 10.1090/pspum/055.1/1265546.
- [Gre99] R. Greenberg, *Iwasawa theory for elliptic curves*, Lecture Notes in Math. 1716 (1999), 51–144. DOI 10.1007/BFb0093453.
- [Gro91] B. Gross, *Kolyvagin's work on modular elliptic curves*, in: $L$-functions and arithmetic (Durham 1989), LMS Lecture Note Ser. 153 (1991), 235–256. DOI 10.1017/CBO9780511526053.009.
- [GS93] R. Greenberg, G. Stevens, *$p$-adic $L$-functions and $p$-adic periods of modular forms*, Invent. Math. 111 (1993), 407–447. DOI 10.1007/BF01231294.
- [GZ86] B. Gross, D. Zagier, *Heegner points and derivatives of $L$-series*, Invent. Math. 84 (1986), 225–320. DOI 10.1007/BF01388809.
- [JSW17] D. Jetchev, C. Skinner, X. Wan, *The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one*, Camb. J. Math. 5 (2017), 369–434. DOI 10.4310/CJM.2017.v5.n3.a2.
- [Kat93] K. Kato, *Iwasawa theory and $p$-adic Hodge theory*, Kodai Math. J. 16 (1993), 1–31. DOI 10.2996/kmj/1138039701.
- [Kat04] K. Kato, *$p$-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290. Numdam AST_2004__295__117_0 (full text fetched; Theorems 12.5, 14.2, 17.4, 18.4 and Conjecture 18.2 checked).
- [Kim07] B. D. Kim, *The parity conjecture for elliptic curves at supersingular reduction primes*, Compos. Math. 143 (2007), 47–72. DOI 10.1112/S0010437X06002569.
- [Kin03] G. Kings, *The Bloch–Kato conjecture on special values of $L$-functions. A survey of known results*, J. Théor. Nombres Bordeaux 15 (2003), 179–198. DOI 10.5802/jtnb.396. (Explicitly excludes the BSD point; cited for the general formulation.)
- [Kob03] S. Kobayashi, *Iwasawa theory for elliptic curves at supersingular primes*, Invent. Math. 152 (2003), 1–36. DOI 10.1007/s00222-002-0265-4.
- [Kob06] S. Kobayashi, *An elementary proof of the Mazur–Tate–Teitelbaum conjecture for elliptic curves*, Doc. Math. Extra Vol. (Kato) (2006), 567–575; arXiv:math/0610164.
- [Kol88] V. Kolyvagin, *Finiteness of $E(\mathbb{Q})$ and $\mathrm{Sha}(E,\mathbb{Q})$ for a subclass of Weil curves*, Math. USSR-Izv. 32 (1989), 523–541. DOI 10.1070/IM1989v032n03ABEH000779.
- [Kol89] V. Kolyvagin, *On the Mordell–Weil group and the Shafarevich–Tate group of Weil elliptic curves*, Math. USSR-Izv. 33 (1989), 473–499. DOI 10.1070/IM1989v033n03ABEH000853.
- [Kol90] V. Kolyvagin, *Euler systems*, The Grothendieck Festschrift II, Progr. Math. 87 (1990), 435–483. DOI 10.1007/978-0-8176-4575-5_11.
- [KT03] K. Kato, F. Trihan, *On the conjectures of Birch and Swinnerton-Dyer in characteristic $p>0$*, Invent. Math. 153 (2003), 537–592. DOI 10.1007/s00222-003-0299-2.
- [LMFDB-389a1] LMFDB, elliptic curve 389.a1, https://www.lmfdb.org/EllipticCurve/Q/389/a/1 and API tables `ec_curvedata`, `ec_mwbsd` (fetched 2026-09-11).
- [LMFDB-5077a1] LMFDB, elliptic curve 5077.a1, https://www.lmfdb.org/EllipticCurve/Q/5077/a/1 (fetched 2026-09-11).
- [Man72] Ju. Manin, *Parabolic points and zeta-functions of modular curves*, Math. USSR-Izv. 6 (1972), 19–64. DOI 10.1070/IM1972v006n01ABEH001867.
- [Maz72] B. Mazur, *Rational points of abelian varieties with values in towers of number fields*, Invent. Math. 18 (1972), 183–266. DOI 10.1007/BF01389815.
- [Maz77] B. Mazur, *Modular curves and the Eisenstein ideal*, Publ. Math. IHÉS 47 (1977), 33–186. DOI 10.1007/BF02684339.
- [Mil72] J. S. Milne, *On the arithmetic of abelian varieties*, Invent. Math. 17 (1972), 177–190. DOI 10.1007/BF01425446.
- [Mil75] J. S. Milne, *On a conjecture of Artin and Tate*, Ann. of Math. 102 (1975), 517–533. DOI 10.2307/1971042.
- [Mil06] J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., BookSurge 2006; https://www.jmilne.org/math/Books/ADTnot.pdf (Chapter I §7 fetched: Lemma 7.1, Theorem 7.3, Remarks 7.4–7.5).
- [MM91] M. R. Murty, V. K. Murty, *Mean values of derivatives of modular $L$-series*, Ann. of Math. 133 (1991), 447–475. DOI 10.2307/2944316.
- [Mon96] P. Monsky, *Generalizing the Birch–Stephens theorem I. Modular curves*, Math. Z. 221 (1996), 415–420. DOI 10.1007/PL00004518.
- [MST06] B. Mazur, W. Stein, J. Tate, *Computation of $p$-adic heights and log convergence*, Doc. Math. Extra Vol. (Coates) (2006), 577–614. DOI 10.4171/dms/4/17.
- [MTT86] B. Mazur, J. Tate, J. Teitelbaum, *On $p$-adic analogues of the conjectures of Birch and Swinnerton-Dyer*, Invent. Math. 84 (1986), 1–48. DOI 10.1007/BF01388731 (full text not accessible; statements taken from [SW13], [Kat04, Conj. 18.2], [Dis20]).
- [Nek06] J. Nekovář, *Selmer complexes*, Astérisque 310 (2006). DOI 10.24033/ast.717.
- [Nek07] J. Nekovář, *On the parity of ranks of Selmer groups III*, Doc. Math. 12 (2007), 243–274. DOI 10.4171/dm/225 (erratum Doc. Math. 14 (2009), 191–194).
- [Nek09] J. Nekovář, *On the parity of ranks of Selmer groups IV* (with an appendix by J.-P. Wintenberger), Compos. Math. 145 (2009), 1351–1359. DOI 10.1112/S0010437X09003959.
- [Nek13] J. Nekovář, *Some consequences of a formula of Mazur and Rubin for arithmetic local constants*, Algebra Number Theory 7 (2013), 1101–1120. DOI 10.2140/ant.2013.7.1101.
- [Ogg74] A. Ogg, *Hyperelliptic modular curves*, Bull. Soc. Math. France 102 (1974), 449–462. DOI 10.24033/bsmf.1789.
- [PR87] B. Perrin-Riou, *Points de Heegner et dérivées de fonctions $L$ $p$-adiques*, Invent. Math. 89 (1987), 455–510. DOI 10.1007/BF01388982.
- [PR92] B. Perrin-Riou, *Théorie d'Iwasawa et hauteurs $p$-adiques*, Invent. Math. 109 (1992), 137–185. DOI 10.1007/BF01232022.
- [PS99] B. Poonen, M. Stoll, *The Cassels–Tate pairing on polarized abelian varieties*, Ann. of Math. 150 (1999), 1109–1149. DOI 10.2307/121064.
- [Roh84] D. Rohrlich, *On $L$-functions of elliptic curves and cyclotomic towers*, Invent. Math. 75 (1984), 409–423. DOI 10.1007/BF01388636.
- [Rub91] K. Rubin, *The "main conjectures" of Iwasawa theory for imaginary quadratic fields*, Invent. Math. 103 (1991), 25–68. DOI 10.1007/BF01239508.
- [Sch82a] P. Schneider, *$p$-adic height pairings I*, Invent. Math. 69 (1982), 401–409. DOI 10.1007/BF01389362.
- [Sch82b] P. Schneider, *Zur Vermutung von Birch und Swinnerton-Dyer über globalen Funktionenkörpern*, Math. Ann. 260 (1982), 495–510. DOI 10.1007/BF01457028.
- [Sch85] P. Schneider, *$p$-adic height pairings II*, Invent. Math. 79 (1985), 329–374. DOI 10.1007/BF01388978.
- [Ser72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972), 259–331. DOI 10.1007/BF01405086.
- [Shi71] G. Shimura, *Introduction to the arithmetic theory of automorphic functions*, Iwanami Shoten and Princeton Univ. Press, 1971 (standard; not fetched).
- [Shi77] G. Shimura, *On the periods of modular forms*, Math. Ann. 229 (1977), 211–221. DOI 10.1007/BF01391466.
- [Ski20] C. Skinner, *A converse to a theorem of Gross, Zagier, and Kolyvagin*, Ann. of Math. 191 (2020), 329–354. DOI 10.4007/annals.2020.191.2.1; arXiv:1405.7294.
- [SS04] E. Schaefer, M. Stoll, *How to do a $p$-descent on an elliptic curve*, Trans. Amer. Math. Soc. 356 (2004), 1209–1231. DOI 10.1090/S0002-9947-03-03366-X.
- [SU14] C. Skinner, E. Urban, *The Iwasawa main conjectures for $\mathrm{GL}_2$*, Invent. Math. 195 (2014), 1–277. DOI 10.1007/s00222-013-0448-1 (hypotheses of Thm 1 as restated in [SW13, Thm 7.5] and [BSTW24, §1.1.2]; full text not fetched).
- [SW13] W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757–1792. DOI 10.1090/S0025-5718-2012-02649-4; no arXiv version exists — the preprint is at https://wstein.org/papers/shark/shark.pdf and the published version at https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf (both fetched; Theorems 1.1, 6.1, 7.3–7.5, 8.1, 9.1, Props 3.5–3.7, 10.1, 11.2, Conj. 5.1 checked).
- [Swe21] N. Sweeting, *Kolyvagin's conjecture and patched Euler systems in anticyclotomic Iwasawa theory*, arXiv:2012.11771.
- [Tat66] J. Tate, *On the conjectures of Birch and Swinnerton-Dyer and a geometric analog*, Séminaire Bourbaki 9 (1964–66), Exp. 306, 415–440. Numdam SB_1964-1966__9__415_0 (PDF fetched; text not machine-readable — statement taken from [Mil06, I §7]).
- [Tat67] J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions* (thesis, 1950), in: Algebraic Number Theory (Cassels–Fröhlich), 1967, 305–347 (standard; not fetched; used only for $\mathrm{vol}(\mathbb{A}_K/K)=|d_K|^{1/2}$ with the measure $2\,dx\,dy$ at complex places, which is also verified directly for $\mathbb{Q}(i)$ in §1.5).
- [Tat79] J. Tate, *Number theoretic background*, Proc. Sympos. Pure Math. 33, part 2 (1979), 3–26. DOI 10.1090/pspum/033.2/546607.
- [Tho10] T. Thongjunthug, *Computing a lower bound for the canonical height on elliptic curves over number fields*, Math. Comp. 79 (2010), 2431–2449. DOI 10.1090/S0025-5718-10-02352-5.
- [Ulm11] D. Ulmer, *Elliptic curves over function fields*, arXiv:1101.1939 (Park City lectures; Theorem 12.1 quoted).
- [Ven07] O. Venjakob, *From the Birch and Swinnerton-Dyer conjecture to non-commutative Iwasawa theory via the equivariant Tamagawa number conjecture — a survey*, LMS Lecture Note Ser. 320 (2007), 333–380; arXiv:math/0507275 (§3.1 checked).
- [Wan14] X. Wan, *Iwasawa main conjecture for supersingular elliptic curves and BSD conjecture*, arXiv:1411.6352 (superseded by [BSTW24], see [BSTW24, Rem. 1.4]).
- [Wei82] A. Weil, *Adeles and algebraic groups*, Progr. Math. 23, Birkhäuser 1982 (standard; not fetched; used for the definition of $|\omega|_v\mu_v^g$).
- [Wer98] A. Werner, *Local heights on Mumford curves*, Math. Ann. 310 (1998), 695–731 (cited via [SW13, §4.2]; not fetched).
- [Zha14] W. Zhang, *Selmer groups and the indivisibility of Heegner points*, Camb. J. Math. 2 (2014), 191–253. DOI 10.4310/CJM.2014.v2.n2.a2.

Searches performed with no result relevant to this chapter (recorded per charter): arXiv listing searches (2020–2026) for "analytic rank 2" + "Birch and Swinnerton-Dyer" (nothing beyond [CH22] and Zenodo/figshare preprints by D. Penchev, April–May 2026, claiming BSD in rank 2 and at all ranks, unrefereed and self-described as AI-assisted — not usable as evidence under the charter); for a rank-$\ge2$ finiteness theorem for $\mathrm{Sha}$ (none); for an unconditional $p$-parity theorem over general number fields (none beyond Theorem 3.3); for a proof of rationality of $L^{(r)}(E,1)/(\Omega_E\mathrm{Reg})$ with $r\ge2$ (none).
