# 03 — Proof obligations in analytic rank $\ge 2$

Status: historical draft (2026-09-11), with selected logical corrections on 2026-09-12.
The [continuation audit](synthesis/continuation-2026-09-12.md) and
[corrected architecture](synthesis/proof-architecture.md) supersede conflicting synthesis claims.
The [odd-rank bridge](synthesis/odd-rank-selmer-bridge.md) now resolves the former ordinary-prime GAP 5 and the irreducible case of GAP 2.
Unreviewed legacy assertions are not promoted by this audit. Owner: obstruction analysis. Tags follow `00-charter.md`.
Cross-references: `01-statement-and-reductions.md`, `02-state-of-the-art.md`, `approaches/A-iwasawa-padic.md`,
`approaches/B-euler-systems-heegner-kolyvagin.md`, `approaches/C-higher-rank-euler-systems-diagonal-cycles.md`,
`approaches/D-function-field-analogy.md`, `approaches/E-arithmetic-statistics.md`, `approaches/H-sha-and-descent.md`.

---

## 0. Conventions, standing hypotheses, and the shape of the problem

Notation is that of the charter. In addition:

* $\varepsilon = w(E)\in\{\pm1\}$ is the global root number, so $r_{\mathrm{an}}\equiv \frac{1-\varepsilon}{2}\pmod 2$.
* $T=T_pE$, $V=V_pE$. $H^1_f(\mathbb{Q},V)$ is the Bloch–Kato Selmer group of $V$; $\dim_{\mathbb{Q}_p}H^1_f(\mathbb{Q},V)=\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = r_{\mathrm{alg}}+\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sha}[p^\infty]$ (standard).
* $H^1_{\mathrm{str}}(\mathbb{Q},V)=\ker\big(H^1_f(\mathbb{Q},V)\to H^1_f(\mathbb{Q}_p,V)\big)$, the *fine* (strict) Selmer group; $r_{\mathrm{str}}:=\dim H^1_{\mathrm{str}}(\mathbb{Q},V)$. Since $H^1_f(\mathbb{Q}_p,V)\cong E(\mathbb{Q}_p)\hat\otimes\mathbb{Q}_p$ is one-dimensional, $r_{\mathrm{str}}\in\{\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})-1,\ \operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\}$.
* $X_\infty=\operatorname{Hom}(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty),\mathbb{Q}_p/\mathbb{Z}_p)$, and when $X_\infty$ is $\Lambda$-torsion, $f_E(T)\in\Lambda$ denotes a generator of $\operatorname{char}_\Lambda(X_\infty)$.
* For an imaginary quadratic field $K$: (Heeg) every $\ell\mid N$ splits in $K$; (disc) $D_K$ odd, $D_K\ne -3$; $E^K$ is the quadratic twist; $P_K=y_K\in E(K)$ the Heegner point of conductor $1$; for $p$ odd, $\operatorname{Sel}_{p^\infty}(E/K)=\operatorname{Sel}_{p^\infty}(E/K)^+\oplus\operatorname{Sel}_{p^\infty}(E/K)^-$ with $\operatorname{Sel}^+=\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$, $\operatorname{Sel}^-=\operatorname{Sel}_{p^\infty}(E^K/\mathbb{Q})$; $r^\pm:=\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/K)^\pm$.
* Kolyvagin classes: $\mathcal{L}^{\mathrm{Heeg}}$ = primes $\ell\nmid NpD_K$ inert in $K$ with $p\mid \ell+1$ and $p\mid a_\ell$; $\mathcal{N}^{\mathrm{Heeg}}$ = squarefree products; $M(n)=\min_{\ell\mid n}\operatorname{ord}_p\gcd(\ell+1,a_\ell)$; $\kappa^{\mathrm{Heeg}}_n\in H^1(K,T/p^{M(n)}T)$ Kolyvagin's derived classes ($\kappa_1^{\mathrm{Heeg}}$ = Kummer image of $P_K$); $\nu(n)$ = number of prime factors of $n$; $\operatorname{ord}(\kappa^{\mathrm{Heeg}})=\min\{\nu(n):\kappa^{\mathrm{Heeg}}_n\neq 0\}$; $\mathscr{M}(n)$, $\mathscr{M}_r$, $\mathscr{M}_\infty$ the divisibility indices as in [BCGS, §0.1] (see §2.3 below).
* The charter's global notation $r_p=\operatorname{ord}_{T=0}L_p(E,T)$ is used for $p$ good ordinary. For $p$ of split multiplicative reduction the same symbol is used for the Mazur–Tate–Teitelbaum $p$-adic $L$-function, which then has an exceptional zero.

**The shape of the problem.** Every proof of a case of BSD (rank) has two halves:

$$
\text{(U)}\quad r_{\mathrm{alg}}\le \operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le r_{\mathrm{an}}
\qquad\qquad
\text{(L)}\quad r_{\mathrm{an}}\le r_{\mathrm{alg}}.
$$

(U) is an *upper bound on a Selmer group* (Euler systems, main conjectures); (L) is *the production of $r_{\mathrm{an}}$ independent rational points*, or, if the stronger equality $\operatorname{corank}\operatorname{Sel}_{p^\infty}=r_{\mathrm{an}}$ is known, the finiteness of $\operatorname{Sha}[p^\infty]$ at that $p$. In rank $\le 1$ the two halves are furnished by a *single object* — the rational number $L(E,1)/\Omega_E$ in rank $0$, the Heegner point $P_K$ in rank $1$ — whose non-vanishing is *equivalent* to the analytic hypothesis by an exact formula (the interpolation formula, resp. Gross–Zagier), and whose arithmetic controls both (U) and (L), at all $p$ simultaneously. For $r_{\mathrm{an}}\ge 2$ no object with these two properties is known; this document isolates, technique by technique, the exact step where this is used, and formulates what would replace it.

---

## 1. The four rank-$\le 1$ mechanisms and the exact step that needs $r_{\mathrm{an}}\le 1$

### 1.1 Kato's Euler system

**[THEOREM] (Kato's reciprocity law and the rank-0 theorem; Kato 2004 [Kat04, §§12–14]).** Let $E/\mathbb{Q}$, $p$ any prime. Kato constructs $\zeta^{\mathrm{Kato}}_E\in H^1(\mathbb{Q},V)$ (the bottom class of an Euler system $\{z_n\}$ for $T$ over the cyclotomic tower) with the properties:

1. (explicit reciprocity) the image of $\operatorname{res}_p\zeta^{\mathrm{Kato}}_E$ under the Bloch–Kato dual exponential $H^1(\mathbb{Q}_p,V)\to \operatorname{Fil}^0 D_{\mathrm{dR}}(V)$ is a *non-zero explicit multiple of* $L(E,1)$ (equivalently $L(E,1)/\Omega_E$). In particular
$$
L(E,1)=0\iff \operatorname{res}_p\zeta^{\mathrm{Kato}}_E\in H^1_f(\mathbb{Q}_p,V)\iff \zeta^{\mathrm{Kato}}_E\in H^1_f(\mathbb{Q},V).
$$
(Stated in this form in [BDV22, §1.1, eq. (1) and the sentence following]; the $\Lambda$-adic version is $\mathrm{Log}(\operatorname{res}_p z_\infty)=L_p(E,T)$ for good ordinary $p$, Kato's Theorem 16.6 [theorem number not re-verified].)
2. If $L(E,1)\ne 0$ then $E(\mathbb{Q})$ and $\operatorname{Sha}(E/\mathbb{Q})$ are finite (Kato, [Kat04, Thm. 14.2] — theorem number not re-verified; the statement is quoted in this form in [Ski20, Intro] and [SW13, §8]).

**[THEOREM] (Euler-system bound in the Selmer case).** Assume $p$ odd and $\bar\rho_{E,p}$ surjective. If $\zeta^{\mathrm{Kato}}_E\neq 0$ then $H^1_{\mathrm{str}}(\mathbb{Q},E[p^\infty])$ is finite, i.e. $r_{\mathrm{str}}(E/\mathbb{Q})=0$; consequently $\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le 1$.

*Source.* Rubin's Euler-system machine [Rub00, Thm. 2.2.2 — theorem number not re-verified] applied to Kato's Euler system, or, in the Kolyvagin-system formulation, [MR04, Thm. 5.2.12(v)]: for a non-zero Kolyvagin system $\kappa$ for $(T,\mathcal{F}_{\mathrm{can}})$, $\operatorname{ord}(\kappa)$ equals the corank of the dual Selmer group, which for Kato's system is $H^1_{\mathrm{str}}(\mathbb{Q},E[p^\infty])$ — this is exactly [BCGS, Cor. C] ($\operatorname{ord}(\kappa^{\mathrm{Kato}})=r_{\mathrm{str}}(E/\mathbb{Q})$), whose "$\kappa\ne 0\Rightarrow$" direction needs no main conjecture. Since $\kappa_1^{\mathrm{Kato}}=\zeta_E^{\mathrm{Kato}}$ (see [BCGS, §3.1.2]), $\zeta^{\mathrm{Kato}}_E\ne 0\Rightarrow\operatorname{ord}(\kappa^{\mathrm{Kato}})=0\Rightarrow r_{\mathrm{str}}=0$. The last inequality follows from $r_{\mathrm{str}}\ge \operatorname{corank}\operatorname{Sel}-1$.

**The exact step where $r_{\mathrm{an}}\le 1$ enters.** The Euler system machine converts *one* non-zero class into an upper bound; the class $\zeta^{\mathrm{Kato}}_E$ is non-zero if $r_{\mathrm{an}}=0$ (by (1)) and if $r_{\mathrm{an}}=1$ (Perrin-Riou's conjecture, now a theorem, §2.1). For $r_{\mathrm{an}}\ge 2$ the input is *identically zero*:

**[THEOREM] (Bertolini–Darmon–Venerucci [BDV22, Thm. A]).** Let $E/\mathbb{Q}$ have semistable reduction at an odd prime $p$ and suppose $L(E,1)=0$. Then there is $P\in E(\mathbb{Q})$ such that (1) $P$ has infinite order iff $L(E,s)$ has a simple zero at $s=1$; (2) $\log_{\omega_E}\big(\operatorname{res}_p\zeta^{\mathrm{Kato}}_E\big)=\log_{\omega_E}(P)^2$ in $\mathbb{Q}_p$, up to a non-zero rational number.

**[NEW] Proposition 1.1 (the Beilinson–Kato element vanishes globally in analytic rank $\ge 2$).** Let $E/\mathbb{Q}$, $p$ an odd prime at which $E$ has semistable (good or multiplicative) reduction and $\bar\rho_{E,p}$ is surjective. If $r_{\mathrm{an}}(E)\ge 2$, then $\zeta^{\mathrm{Kato}}_E=0$ in $H^1(\mathbb{Q},V_pE)$.

*Proof.* Since $L(E,1)=0$, [BDV22, Thm. A] applies: the point $P$ has finite order because the zero at $s=1$ is not simple; $\log_{\omega_E}$ is a group homomorphism $E(\mathbb{Q}_p)\to\mathbb{Q}_p$ to a torsion-free group, so $\log_{\omega_E}(P)=0$, hence $\log_{\omega_E}(\operatorname{res}_p\zeta^{\mathrm{Kato}}_E)=0$. By Kato's reciprocity law (1) above, $\operatorname{res}_p\zeta^{\mathrm{Kato}}_E\in H^1_f(\mathbb{Q}_p,V)\cong E(\mathbb{Q}_p)\hat\otimes\mathbb{Q}_p$, on which $\log_{\omega_E}$ is an isomorphism onto $\mathbb{Q}_p$. Hence $\operatorname{res}_p\zeta^{\mathrm{Kato}}_E=0$, i.e. $\zeta^{\mathrm{Kato}}_E\in H^1_{\mathrm{str}}(\mathbb{Q},V)$. Suppose $\zeta^{\mathrm{Kato}}_E\ne 0$. By the Euler-system bound above, $H^1_{\mathrm{str}}(\mathbb{Q},E[p^\infty])$ is finite; the $\mathbb{Z}_p$-rank of the strict Selmer group of $T$ equals the corank of the strict Selmer group of $E[p^\infty]$ (the standard comparison of Selmer groups of $T$, $V$, $T\otimes\mathbb{Q}_p/\mathbb{Z}_p$ for a fixed Selmer structure; see e.g. [MR04, Ch. 2]), so $H^1_{\mathrm{str}}(\mathbb{Q},V)=0$, contradicting $0\ne\zeta^{\mathrm{Kato}}_E\in H^1_{\mathrm{str}}(\mathbb{Q},V)$. $\square$

*Remark.* The local statement $\operatorname{res}_p\zeta^{\mathrm{Kato}}_E=0\iff r_{\mathrm{an}}\ge 2$ is [BDV22, Thm. A] itself; the passage to global vanishing is the small extra step above. Perrin-Riou's original conjecture [PR93] predicts the global statement; we have not located it stated as a theorem in print, so we flag it [NEW] with the caveat that it is probably known to experts. For $r_{\mathrm{an}}$ even $\ge 2$ one also gets $\zeta^{\mathrm{Kato}}_E=0$ from the rational main conjecture and parity: $L(E,1)=0\Rightarrow T\mid L_p(E,T)\Rightarrow T\mid f_E\Rightarrow\operatorname{corank}\operatorname{Sel}\ge 1$ (control), parity [DD10] forces $\operatorname{corank}\ge 2$, so $r_{\mathrm{str}}\ge 1$ and $\zeta^{\mathrm{Kato}}_E=0$ by [BCGS, Cor. C]. For $r_{\mathrm{an}}$ odd $\ge 3$ the BDV route is the only one available.

**Consequence for the method.** For $r_{\mathrm{an}}\ge 2$ all information in Kato's Euler system sits in the *derived* classes $\kappa^{\mathrm{Kato}}_n$, $\nu(n)\ge 1$ (§2.3). Their non-vanishing is now a theorem (given the rational main conjecture) — [BCGS, Thm. C]: for $E$ non-CM, $p$ odd good ordinary with $E(\mathbb{Q}_p)[p]=0$ and the rational cyclotomic main conjecture, some $\kappa^{\mathrm{Kato}}_n\neq 0$ — and $\operatorname{ord}(\kappa^{\mathrm{Kato}})=r_{\mathrm{str}}(E/\mathbb{Q})$ [BCGS, Cor. C]. But the *only* link between the $\kappa^{\mathrm{Kato}}_n$ and complex $L$-values is Kato's reciprocity law for the bottom class, which is now empty. What survives is the link to modular symbols mod $p$ (Kurihara numbers, §2.3), which is not a link to $\operatorname{ord}_{s=1}L(E,s)$.

### 1.2 Heegner points, Gross–Zagier, Kolyvagin

**[THEOREM] (Gross–Zagier [GZ86]; Yuan–Zhang–Zhang for the general Shimura-curve form).** For $K$ satisfying (Heeg), $L'(E/K,1)=c\cdot\langle P_K,P_K\rangle_{\mathrm{NT}}$ with an explicit $c\ne 0$. Hence $P_K$ is non-torsion iff $\operatorname{ord}_{s=1}L(E/K,s)=1$, i.e. iff $\{r_{\mathrm{an}}(E),r_{\mathrm{an}}(E^K)\}=\{0,1\}$.

**[THEOREM] (Kolyvagin [Kol90], [Gro91]).** Under (Heeg), if $P_K$ is non-torsion then $E(K)$ has rank $1$ and $\operatorname{Sha}(E/K)$ is finite; with [BFH90], [MM91] (existence of $K$ with $r_{\mathrm{an}}(E/K)=1$) this gives: $r_{\mathrm{an}}(E)\le 1\Rightarrow r_{\mathrm{alg}}(E)=r_{\mathrm{an}}(E)$ and $\operatorname{Sha}(E/\mathbb{Q})$ finite.

**The exact step where $r_{\mathrm{an}}\le 1$ enters.** Two places, and it is important to separate them.

(a) *Input.* Since $L(E/K,s)=L(E,s)L(E^K,s)$, if $r_{\mathrm{an}}(E)\ge 2$ then $\operatorname{ord}_{s=1}L(E/K,s)\ge 2$ for **every** $K$, so $P_K$ is torsion for every Heegner field. The construction yields the zero class $\kappa^{\mathrm{Heeg}}_1=0$ for all $K$.

(b) *Analytic identification.* Kolyvagin's argument in rank $1$ uses that the *single* class $\kappa^{\mathrm{Heeg}}_1$ is non-zero **and** that its index $[E(K):\mathbb{Z}P_K]$ is a fixed integer (giving all $p$ at once, §3.3). Gross–Zagier is what identifies "$\kappa^{\mathrm{Heeg}}_1\ne 0$" with an analytic statement. Nothing analogous is known for any $\kappa^{\mathrm{Heeg}}_n$ with $n>1$: there is no formula expressing $\kappa^{\mathrm{Heeg}}_\ell$ (or its order) in terms of $L(E/K,s)$ or its derivatives.

Kolyvagin's structure theorem itself (§2.3) is *rank-agnostic*: it computes $\operatorname{Sel}_{p^\infty}(E/K)$ from the whole system $\{\kappa^{\mathrm{Heeg}}_n\}$, in any rank, provided the system is non-zero (Kolyvagin's conjecture, now a theorem in wide generality: [Zha14, Thm. 1.1], [Swe], [BCGS, Thm. A]). What is missing in rank $\ge 2$ is *purely* the bridge from the system to analytic data.

### 1.3 Iwasawa main conjecture and control theorems

Fix $p$ odd, good ordinary. Recall:

**[THEOREM] (Kato [Kat04, Thm. 17.4]; Rohrlich [Roh84]).** $X_\infty$ is $\Lambda$-torsion and $f_E(T)$ divides $L_p(E,T)$ in $\Lambda\otimes\mathbb{Q}_p$; if $\bar\rho_{E,p}$ is surjective, in $\Lambda$. (Stated in this form in [SW13, Thms. 7.3, 7.4].)

**[THEOREM] (Mazur's control theorem [Maz72]; [Gre99, Thm. 1.2]).** The restriction map $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\to\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^{\Gamma}$ has finite kernel and cokernel. Dually, $\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{rank}_{\mathbb{Z}_p}X_\infty/TX_\infty$.

**[THEOREM] (Main conjecture: Skinner–Urban [SU14, Thm. 1]; Wan [Wan15]; Castella–Grossi–Skinner [CGS25]; as collected in [BCGS, Thm. 3.2.6]).** Let $p>2$ be good ordinary. (i) If $E[p]$ is irreducible, then $f_E(T)$ and $L_p(E,T)$ generate the same ideal of $\Lambda\otimes\mathbb{Q}_p$ (rational main conjecture) [BCGS, Thm. 3.2.6(ii), via Wan15]. (ii) If moreover $\rho_{E,p}$ is surjective and there is $q\,\|\,N$ with $\bar\rho_{E,p}$ ramified at $q$, they generate the same ideal of $\Lambda$ [SU14, Thm. 1], [SW13, Thm. 7.5]. (iii) Eisenstein cases: [CGS25].

**[THEOREM] (Schneider [Sch85], Perrin-Riou [PR92]; Jones for multiplicative $p$; as stated in [SW13, Thm. 6.1]).** $\operatorname{ord}_{T=0}f_E(T)\ge r_{\mathrm{alg}}$, with equality iff $\operatorname{Sha}[p^\infty]$ is finite and the cyclotomic $p$-adic height pairing on $E(\mathbb{Q})$ is non-degenerate. In that case $\operatorname{ord}_p$ of the leading coefficient of $f_E$ equals $\operatorname{ord}_p\big(\epsilon_p\cdot\prod_v c_v\cdot\#\operatorname{Sha}[p^\infty]\cdot\operatorname{Reg}_\gamma(E/\mathbb{Q})/\#E(\mathbb{Q})[p^\infty]^2\big)$, where $\epsilon_p$ is the $p$-adic multiplier of [SW13, Thm. 6.1, §8.1] (of the same valuation as $(1-\alpha_p^{-1})^2$, i.e. as $\#\tilde E(\mathbb{F}_p)[p^\infty]^2$, for good ordinary $p$; replaced by $\mathcal{L}_p/\log_p\kappa(\gamma)$ for split multiplicative $p$) and $\operatorname{Reg}_\gamma$ is the $p$-adic regulator in the normalisation of [SW13, §4].

**Proposition 1.2 (the basic chain; standard, proof included).** For $p$ odd good ordinary,
$$
r_{\mathrm{alg}}\ \le\ \operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ \le\ \operatorname{ord}_{T=0}f_E(T)\ \le\ r_p .
$$
*Proof.* First inequality: $E(\mathbb{Q})\otimes\mathbb{Q}_p/\mathbb{Z}_p\hookrightarrow\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$. Third: Kato's divisibility in $\Lambda\otimes\mathbb{Q}_p$ (a $p$-power factor does not change $\operatorname{ord}_{T=0}$). Second: by the structure theory of torsion $\Lambda$-modules there is a pseudo-isomorphism $X_\infty\to\bigoplus_i\Lambda/(f_i)$ with $f_E=\prod f_i$ (finite kernel and cokernel). Then $\operatorname{rank}_{\mathbb{Z}_p}X_\infty/TX_\infty=\#\{i:f_i(0)=0\}\le\sum_i\operatorname{ord}_{T=0}f_i=\operatorname{ord}_{T=0}f_E$, since $\Lambda/(f_i,T)=\mathbb{Z}_p/(f_i(0))$ has rank $1$ if $f_i(0)=0$ and is finite otherwise, and finite modules contribute nothing to ranks. Conclude with Mazur's control theorem. $\square$

**The exact step where $r_{\mathrm{an}}\le 1$ enters.** The main conjecture is rank-agnostic. The chain above is *all inequalities*, and two of them must be equalities to conclude:

* (E1) $r_p=r_{\mathrm{an}}$ — Bridge (i), §2.1. Known for $r_{\mathrm{an}}=0$ (interpolation formula: $L_p(E,0)=(1-\alpha^{-1})^2L(E,1)/\Omega_E$ with $\alpha\ne 1$ by Hasse), and for $r_{\mathrm{an}}=1$ *only up to the non-vanishing of a $p$-adic height* ($p$-adic Gross–Zagier).
* (E2) $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{ord}_{T=0}f_E$ — semisimplicity of $X_\infty\otimes\mathbb{Q}_p$ at $T=0$, equivalent (Schneider–Perrin-Riou) to non-degeneracy of the $p$-adic height. **In rank $\le 1$ this equality is free**:

**Lemma 1.3 (standard; proof included).** Assume $p$ odd good ordinary, the rational main conjecture at $p$, and $r_p\le 1$. Then $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{ord}_{T=0}f_E=r_p$.
*Proof.* Prop. 1.2 gives $\operatorname{corank}\operatorname{Sel}\le r_p\le 1$. By $p$-parity [DD10] (for good ordinary $p$ already [Nek01]), $\operatorname{corank}\operatorname{Sel}\equiv r_{\mathrm{an}}\pmod 2$; by the functional equation of $L_p(E,T)$ under $T\mapsto(1+T)^{-1}-1$, whose sign is $w(E)$ for good ordinary $p$ ([MTT86, §I.17 — section number not re-verified]; the sign is $-w(E)$ in the split multiplicative case [GS93, Intro]), $r_p\equiv r_{\mathrm{an}}\pmod 2$. Two integers $\le 1$ of the same parity with $\operatorname{corank}\le r_p$ are equal. The rational main conjecture gives $\operatorname{ord}_{T=0}f_E=r_p$. $\square$

For $r_p\ge 2$ parity no longer forces equality, and (E2) becomes a genuine hypothesis. This is the precise sense in which the Iwasawa-theoretic route is stuck at $2$: it needs (E1) and (E2), both open, and both equivalent to non-degeneracy statements for $p$-adic heights (§2.1, §5).

### 1.4 Converse theorems

**[THEOREM] (Skinner [Ski20, Thms. A, A$'$, B]).** Let $E/\mathbb{Q}$ be semistable with non-split multiplicative reduction at an odd prime or split multiplicative reduction at two odd primes. Then $\operatorname{rank}E(\mathbb{Q})=1$ and $\#\operatorname{Sha}(E)<\infty\Rightarrow\operatorname{ord}_{s=1}L(E,s)=1$. The engine is Theorem B: for $p\ge 5$ good ordinary, $K$ with (b)–(d) of loc. cit. and (e) $\dim H^1_f(K,V)=1$ with $H^1_f(K,V)\to\prod_{w\mid p}H^1(K_w,V)$ injective, one has $\operatorname{ord}_{s=1}L(E/K,s)=1$.
**[THEOREM] (Zhang [Zha14, Thm. 1.3]; BCGS [BCGS, Cor. A and Remark]).** Under Kolyvagin's conjecture for $(E,p,K)$: $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/K)=1\Rightarrow P_K$ non-torsion $\Rightarrow\operatorname{ord}_{s=1}L(E/K,s)=1$.

**The exact step where rank $1$ enters (Skinner's argument, [Ski20, Intro and Remark 2.9.1(ix),(x)]).** Let $H^1_{\bar{\mathfrak p}}(K,V)\subset H^1(K,V)$ be the classes vanishing at every place $w\ne\bar{\mathfrak p}$. Because $H^1_f(K_w,V)=E(K_w)\hat\otimes\mathbb{Q}_p=0$ for $w\nmid p$, every Selmer class is trivial at all $w\nmid p$, so
$$
H^1_{\bar{\mathfrak p}}(K,V)\ \supseteq\ \ker\big(H^1_f(K,V)\xrightarrow{\ \operatorname{loc}_{\mathfrak p}\ }H^1_f(K_{\mathfrak p},V)\big),\qquad \dim H^1_f(K_{\mathfrak p},V)=1 .
$$
The proof runs: (Wan's divisibility in the main conjecture for the BDP $p$-adic $L$-function) $L^{\mathrm{BDP}}_p(f/K)(\mathbf 1)=0\Rightarrow H^1_{\bar{\mathfrak p}}(K,V)\ne 0$; hypothesis (e) forces $H^1_{\bar{\mathfrak p}}(K,V)=0$ [Ski20, Lemma 2.3.2]; hence $L_p^{\mathrm{BDP}}(f/K)(\mathbf 1)\ne 0$; by [BDP13, Thm. 5.13] $L^{\mathrm{BDP}}_p(f/K)(\mathbf 1)\doteq\log_\omega(P_K)^2$, so $P_K$ is non-torsion; Gross–Zagier finishes. **If $\dim H^1_f(K,V)\ge 2$, then $\dim\ker(\operatorname{loc}_{\mathfrak p})\ge 1$, so $H^1_{\bar{\mathfrak p}}(K,V)\ne 0$ automatically**, the implication is vacuous, and indeed $L^{\mathrm{BDP}}_p(f/K)(\mathbf 1)=\log_\omega(P_K)^2=0$. The rank-$2$ analogue would have to use the *leading coefficient* of $L^{\mathrm{BDP}}_p(f/K)$ (or of the Bertolini–Darmon theta element $\Theta_{f/K}$) at the trivial character; Castella–Hsieh [CH22] prove a formula for it (§2.2(d)) in terms of *derived $p$-adic heights* and a *$p$-adic regulator* — quantities with no known complex counterpart. There is no formula relating that leading coefficient to $L''(E,1)$; this is exactly Bridge (ii) in anticyclotomic clothing.

---

## 2. The three bridges

### 2.1 Bridge (i): the $p$-adic/complex transfer

**[CONJECTURE] $\mathrm{T}(E,p)$.** For $p$ good ordinary: $r_p=r_{\mathrm{an}}$. For $p$ split multiplicative: $r_p=r_{\mathrm{an}}+1$. (Equivalently: MTT's $p$-adic BSD order-of-vanishing conjecture [MTT86] with $r_{\mathrm{alg}}$ replaced by $r_{\mathrm{an}}$; so $\mathrm{T}(E,p)\iff$ [MTT order part] $\wedge$ [BSD rank].)

**What is known: $r_{\mathrm{an}}=0$.** [THEOREM] Good ordinary: $r_p=0$ by interpolation. Split multiplicative: $r_p=1$ by Greenberg–Stevens [GS93] ($L_p'(E,0)=\mathcal{L}_p(E)\cdot L(E,1)/\Omega_E$, $\mathcal{L}_p(E)=\log_p q_E/\operatorname{ord}_pq_E$) together with $\mathcal{L}_p(E)\ne 0$, which follows from the transcendence of the Tate period [BSDGP96].

**What is known: $r_{\mathrm{an}}=1$, good ordinary $p$.** Let $P$ generate $E(\mathbb{Q})\otimes\mathbb{Q}$ and $\langle\ ,\ \rangle_p$ the cyclotomic $p$-adic height.

**[THEOREM] ($p$-adic Gross–Zagier: Perrin-Riou [PR87] under (Heeg) and $p$ split in $K$; Disegni [Dis17], [Dis20, Thm. 3.2.1(1)] in general).** If $r_{\mathrm{an}}=1$ and $E$ has good ordinary reduction at $p$ then
$$
L_p'(E,0)=e_p\cdot\frac{L'(E,1)}{\Omega_E\,\langle P,P\rangle_{\mathrm{NT}}}\cdot\langle P,P\rangle_p,
$$
where $e_p\ne0$ is an explicit product of Euler-type factors at $p$ (involving $(1-\alpha_p^{-1})$) and of normalisation constants for the height and for the variable $T$; see [Dis20, Thm. 3.2.1 and §2.2] for the exact expression. (Disegni's "$(\mathrm{BSD}_p)$" is an identity between the $\tilde r$-th Taylor coefficient and the regulator, which is *not* an order-of-vanishing statement when the regulator is $0$; [Dis20, footnote (3)].) Hence
$$
\boxed{\ r_{\mathrm{an}}=1\ \Longrightarrow\ \big(\,r_p=1\iff\langle P,P\rangle_p\ne 0\,\big).}
$$

**[GAP 1] (Schneider's non-degeneracy conjecture in rank one).** *Let $E/\mathbb{Q}$ have $r_{\mathrm{an}}=1$ (so $E(\mathbb{Q})\otimes\mathbb{Q}=\mathbb{Q}P$), and let $p$ be a good ordinary prime. Show $\langle P,P\rangle_p\ne 0$.* Known: CM curves (Bertrand [Ber82], via $p$-adic transcendence; this is what makes $\mathrm{T}(E,p)$ a theorem for CM curves of rank $1$, cf. [Ski20, Intro], [BDV22, §1.3]). Not known for a single non-CM curve at infinitely many $p$ (we found no such result; [unverified] that none exists).

**Perrin-Riou's conjecture and its proofs.** [CONJECTURE → THEOREM] Perrin-Riou [PR93] conjectured that for $L(E,1)=0$ the local point $\operatorname{res}_p\zeta^{\mathrm{Kato}}_E\in E(\mathbb{Q}_p)\otimes\mathbb{Q}_p$ is the image of a global point with $\log$ equal to $\log(P)^2$ up to $\mathbb{Q}^\times$; proved by [BDV22, Thm. A] ($p$ odd, $E$ semistable at $p$; via Beilinson–Flach elements and [BDP13]), by Büyükboduk–Pollack–Sasaki [BPS] ($p$ odd good ordinary, $K$ with $p$ split and (Heeg), via a critical-slope $p$-adic Gross–Zagier formula), and independently by Burungale–Skinner–Tian (cited as [BST] in [Kim-soft, Thm. 2.3]; reference not independently located). In the supersingular case it is equivalent to Kobayashi's $p$-adic Gross–Zagier formula [Kob13] ([BDV22, §1.3]); in the CM case it follows from [PR87], [PR93], [Rub92], [Ber82]; in the split multiplicative case it was proved earlier by Venerucci [Ven16] using Bertolini–Darmon's Hida-family formula [BD07].

*What Perrin-Riou's conjecture does and does not give for $\mathrm{T}(E,p)$.* It shows $\zeta^{\mathrm{Kato}}_E\ne 0$ when $r_{\mathrm{an}}=1$, hence (§1.1) $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le 1$ — a Kato-only proof of the rank-one Selmer bound. It does **not** give $r_p=1$: by the $\Lambda$-adic reciprocity law and Perrin-Riou's derivative formalism ([PR93], [Nek06, §11.5.10] in the form of a "Rubin-style formula", cf. [BDV22, §1.3]), $L_p'(E,0)$ is expressed through the $p$-adic *height* of $\zeta^{\mathrm{Kato}}_E$ against $P$, and the non-degeneracy of that height is exactly [GAP 1]. The anticyclotomic route (BDP formula $L_p^{\mathrm{BDP}}(\mathbf 1)\doteq\log_\omega(P_K)^2$, [JSW17]) avoids heights, because $\log_\omega$ — unlike $\langle\ ,\ \rangle_p$ — is *automatically* injective on non-torsion points. This is why the $p$-part of BSD in rank one is a theorem while $\mathrm{T}(E,p)$ for $r_{\mathrm{an}}=1$ is not.

**Exceptional zero case, $r_{\mathrm{an}}=1$.** [CONDITIONAL] For split multiplicative $p\ge 5$: $r_p\ge 2$ (trivial zero and parity, sign $-w(E)$ [GS93]); Büyükboduk [Buy, Thm. B, Cor. C] and Venerucci [Ven16] prove $r_p=2$ and a second-derivative formula *assuming the relevant (Nekovář) $p$-adic height pairing is non-degenerate*; Disegni [Dis20, Thm. 3.2.1(2)] gives the exact leading-term identity in Taylor-coefficient form. So the exceptional case has the same status as the good ordinary one: reduced to a height non-degeneracy.

**What is known for $r_{\mathrm{an}}\ge 2$.** [THEOREM] (i) For $r_{\mathrm{an}}$ even $\ge 2$ and good ordinary $p$: $r_p\ge 2$ ($L_p(E,0)=0$ and $r_p\equiv r_{\mathrm{an}}$). (ii) For any $E$ and good ordinary odd $p$: $r_p\ge r_{\mathrm{alg}}$ (Prop. 1.2). (iii) Nothing else: for $r_{\mathrm{an}}=3$ it is not known that $r_p\ge 3$ unless $r_{\mathrm{alg}}\ge 3$ is known for the specific curve.

**[THEOREM / remaining cases of former GAP 2].** If $E/\mathbb Q$ is
non-CM, $p\ge5$ is good ordinary with irreducible $E[p]$, and the analytic
rank is odd and at least three, then $s_p(E)\ge3$ by the
[odd-rank bridge](synthesis/odd-rank-selmer-bridge.md). Proposition 1.2 gives
$r_p\ge3$. The previous blanket statement that this was a gap is withdrawn
in this range. Other residual-image and reduction cases require their
own converse theorem; no claim about them is added here.

**[GAP 3] ($\mathrm{T}(E,p)$ in rank $\ge 2$; upper bound half).** *Let $E/\mathbb{Q}$ with $r_{\mathrm{an}}=r\ge 2$, $p$ good ordinary with $E[p]$ irreducible. Show $r_p\le r$.* Under the rational main conjecture this is $\operatorname{ord}_{T=0}f_E\le r$, which by Schneider–Perrin-Riou is equivalent to: $\operatorname{Sha}[p^\infty]$ finite, $r_{\mathrm{alg}}=r$, and the $p$-adic height on $E(\mathbb{Q})$ non-degenerate. So [GAP 3] $\iff$ [BSD rank at $E$] $\wedge$ [$\operatorname{Sha}[p^\infty]$ finite] $\wedge$ [Schneider at $p$]. It is *strictly stronger* than BSD (rank) for $E$.

### 2.2 Bridge (ii): an arithmetic interpretation of $L^{(r)}(E,1)$, $r\ge 2$

**(a) What BSD itself says, and why it is a determinant.** [CONJECTURE] BSD (leading term) predicts $L^{(r)}(E,1)/r!=\Omega_E\prod c_p\,\#\operatorname{Sha}\,\det(\langle P_i,P_j\rangle_{\mathrm{NT}})/[E(\mathbb{Q}):\sum\mathbb{Z}P_i]^2\#E(\mathbb{Q})_{\mathrm{tors}}^2$. For the motive $h^1(E)$ the Beilinson–Bloch conjecture ([Blo84], [Bei87]) is BSD: the only cycles are points, and the height pairing is Néron–Tate. In rank $1$ the *determinant is a single height*, and Gross–Zagier realises it as the height of a *canonical* point $P_K$ by passing to $L(E/K,s)$. For $r\ge 2$ the determinant of an $r\times r$ Gram matrix is not the height of any single canonical point on $E$; a "higher Gross–Zagier formula" over $\mathbb{Q}$ would have to produce a canonical *object* whose height/period is a determinant. No such object is known on $E$, on $E^r$, or on modular curves.

**(b) Triple products do not help.** Let $V=V_pE$ (or the motive $h^1(E)$). Since $\dim V=2$,
$$
V^{\otimes 3}\ \cong\ \operatorname{Sym}^3V\ \oplus\ (V\otimes\det V)^{\oplus 2}\ =\ \operatorname{Sym}^3V\oplus V(-1)^{\oplus 2},
$$
hence $L(E\otimes E\otimes E,s)=L(\operatorname{Sym}^3E,s)\cdot L(E,s-1)^2$ (standard). The centre of $L(E^{\otimes 3},s)$ is $s=2$, and $L(E,s-1)$ at $s=2$ is $L(E,1)$.

**Proposition 2.1 (standard; proof included).** $\operatorname{ord}_{s=2}L(E\otimes E\otimes E,s)=\operatorname{ord}_{s=2}L(\operatorname{Sym}^3E,s)+2\,r_{\mathrm{an}}(E)\ \ge\ 2\,r_{\mathrm{an}}(E)$. In particular, if $r_{\mathrm{an}}(E)\ge 1$ then $L'(E^{\otimes3},2)=0$, and if $r_{\mathrm{an}}(E)\ge 2$ then $L^{(k)}(E^{\otimes 3},2)=0$ for $k\le 3$.
*Proof.* $L(\operatorname{Sym}^3E,s)$ is entire ([KS02] for non-CM $E$; for CM $E$ it is a product of Hecke $L$-functions of non-trivial characters) and $L(E,s-1)^2$ has a zero of order exactly $2r_{\mathrm{an}}$ at $s=2$; orders of zeros add. $\square$

The Gross–Kudla conjecture [GK92] (Gross–Schoen cycle [GS95]), proved by Yuan–Zhang–Zhang [YZZ] under ramification hypotheses, is $L'(F,2)=\Omega(F)\,\langle\Delta(F),\Delta(F)\rangle_{\mathrm{BB}}$ for $F=f\times g\times h$ with global sign $-1$ — a formula for the **first** derivative. By Prop. 2.1, for $f=g=h=f_E$ with $r_{\mathrm{an}}(E)\ge 1$ the first derivative vanishes, so (granting the Beilinson–Bloch non-degeneracy conjecture) $\Delta(f_E^{\otimes 3})$ is *torsion in the Chow group* — the exact analogue of "$P_K$ is torsion". Moreover, even an ideal "higher Gross–Kudla formula" for $L^{(k)}(E^{\otimes 3},2)$ with $k=\operatorname{ord}_{s=2}L(\operatorname{Sym}^3E,s)+2r_{\mathrm{an}}$ would express (leading term of $\operatorname{Sym}^3$) $\times\big(L^{(r_{\mathrm{an}})}(E,1)\big)^2$: the square of the BSD leading term multiplied by an unrelated $\operatorname{Sym}^3$ value. On the cycle side, the $V(-1)^{\oplus 2}$-part of $H^3(E^3)$ is $H^1(E)\otimes(\text{Tate classes in }H^2(E^2))$, and the corresponding homologically trivial cycles are of the form $(P-O)\times\Gamma$ with $P\in E(\mathbb{Q})$, $\Gamma\in\mathrm{NS}(E^2)$ — i.e. **they are the points of $E(\mathbb{Q})$ again**, not new cycles. The triple product therefore neither produces new points nor isolates $L^{(r)}(E,1)$.

**(c) The only place a higher-derivative formula exists: function fields.** [THEOREM] (Yun–Zhang [YZ17, Thm. 1.2]; [YZ19]). Let $F=k(X)$, $k=\mathbb{F}_q$ of odd characteristic, $F'/F$ a quadratic extension, $\pi$ an everywhere unramified cuspidal automorphic representation of $\mathrm{PGL}_2(\mathbb{A}_F)$, $r\ge 0$ even. Then
$$
\tfrac12(\log q)^r|\omega_X|\ \mathscr L^{(r)}(\pi_{F'},\tfrac12)=\big([\mathrm{Sht}^\mu_T]_\pi,[\mathrm{Sht}^\mu_T]_\pi\big)_{\mathrm{Sht}^r_G},
$$
the self-intersection of the $\pi$-isotypic Heegner–Drinfeld cycle on the moduli of $\mathrm{PGL}_2$-Shtukas with $r$ legs ($\dim\mathrm{Sht}^r_G=2r$). [YZ19] allows squarefree level and odd $r$ (products $L^{(a)}(\pi,\tfrac12)L^{(r-a)}(\pi\otimes\eta,\tfrac12)$).

*Why it does not transfer.* (1) The right-hand side is a self-intersection of a *single canonical cycle* on a space of dimension $2r$ that exists only because one can take $r$ independent Frobenius-twisted modifications; over $\mathbb{Z}$ there is no moduli of Shtukas with $r\ge 2$ legs (the case $r=1$ over $\mathbb{Q}$ is the modular curve over $\operatorname{Spec}\mathbb{Z}$; [YZ17, Intro]). (2) Even over function fields the formula is *not* a statement about $\operatorname{rank}E(F)$: no relation between $[\mathrm{Sht}^\mu_T]_\pi$ and Mordell–Weil groups is known for $r\ge 2$. The function-field BSD for elliptic curves is proved by entirely different means (Tate/Milne/Kato–Trihan: finiteness of $\operatorname{Sha}$ $\iff$ BSD, via the Tate conjecture for the surface) — see `approaches/D`.

**(d) The one available rank-2 formula over $\mathbb{Q}$ is $p$-adic and anticyclotomic.** [CONJECTURE] (Darmon–Rotger [DR16, Conj. 3.2 and §4.5]; rank-2 specialisation as [CH22, Conj. 1.2]). Let $E/\mathbb{Q}$, $K$ imaginary quadratic with $p=\mathfrak p\bar{\mathfrak p}$ split, $\chi$ a ring class character with $\chi(\mathfrak p)\ne\pm1$, $g,h$ the weight-one theta series of $\chi,\chi^{-1}$; then $L(f\otimes g\otimes h,s)=L(E,s)L(E^K,s)L(E/K,\chi^2,s)$, and the generalised Kato classes $\kappa_{\alpha,\alpha^{-1}},\dots\in H^1(\mathbb{Q},V_pE)$ ($p$-adic limits of étale Abel–Jacobi images of Gross–Kudla–Schoen cycles along Hida families) satisfy: if $L(E^K,1)L(E/K,\chi^2,1)\ne 0$ then TFAE: (1) the classes span a non-trivial subspace of $H^1_f(\mathbb{Q},V)$; (2) $\dim H^1_f(\mathbb{Q},V)=2$; (3) $r_{\mathrm{alg}}=2$; (4) $r_{\mathrm{an}}=2$.

[THEOREM] (Castella–Hsieh [CH22, Thm. A, Cors. B, C]). Assume moreover $\bar\rho_{E,p}$ irreducible, $N^-$ squarefree and $\bar\rho_{E,p}$ ramified at every $q\mid N^-$. Then $\kappa_{\alpha,\beta^{-1}}=\kappa_{\beta,\alpha^{-1}}=0$ and: $\kappa_{\alpha,\alpha^{-1}}\ne 0$ in $H^1_f(\mathbb{Q},V)$ $\iff$ $r_{\mathrm{str}}(E/\mathbb{Q})=1$. In particular $\kappa_{\alpha,\alpha^{-1}}\neq0\Rightarrow\dim H^1_f(\mathbb{Q},V)=2$; and if $r_{\mathrm{alg}}=2$ and $\operatorname{Sha}[p^\infty]$ is finite then $\kappa_{\alpha,\alpha^{-1}},\kappa_{\beta,\beta^{-1}}$ are non-zero and span $H^1_{\mathrm{str}}(\mathbb{Q},V)$. The proof gives the formula
$$
\kappa_{E,K}=\frac{\bar\theta_{f/K}}{h^{(\rho)}(P,Q)}\cdot\big(P\otimes\log_pQ-Q\otimes\log_pP\big)\cdot(\text{explicit non-zero rational}),
$$
where $(P,Q)$ is a basis of $H^1_f(\mathbb{Q},V)$, $\rho=\operatorname{ord}_{T=0}\Theta_{f/K}(T)$, $\bar\theta_{f/K}$ is the leading coefficient of the Bertolini–Darmon theta element at the trivial character, and $h^{(\rho)}$ is the $\rho$-th *derived* anticyclotomic $p$-adic height [BD95], [How04-derived].

*Assessment.* This is a genuine rank-2 "Gross–Zagier": a canonical class equals a canonical *$p$-adic regulator vector* ($P\otimes\log Q-Q\otimes\log P\ne 0$ whenever $P,Q$ are independent — the $p$-adic logarithm has no degeneracy problem). But its analytic partner is $\bar\theta_{f/K}$, the leading term of an *anticyclotomic* $p$-adic $L$-function at a point *outside* the range of interpolation; no formula relates $\bar\theta_{f/K}$ to $L''(E,1)$. The recent formulation of a $p$-adic BSD conjecture for $L^{\mathrm{BDP}}_{\mathfrak p}$ [CHKLL25] makes the same point: its order-of-vanishing part reduces to a *maximal non-degeneracy* of an anticyclotomic height — the anticyclotomic avatar of [GAP 1]/[GAP 3].

**[GAP 4] (higher Gross–Zagier over $\mathbb{Q}$).** *Let $E/\mathbb{Q}$ with $r_{\mathrm{an}}=2$ and let $K$ satisfy (Heeg) with $L(E^K,1)\ne 0$ (so $\operatorname{ord}_{s=1}L(E/K,s)=2$). Construct a canonical element $\mathcal{Z}(E,K)$ of an arithmetic group (Chow group, Selmer group, or $E(\mathbb{Q})\otimes E(\mathbb{Q})$) together with a canonical real-valued invariant $\mathrm{ht}(\mathcal{Z})$ such that $L''(E/K,1)/2=c\cdot\mathrm{ht}(\mathcal{Z}(E,K))$ with $c\ne 0$ explicit, and such that $\mathrm{ht}(\mathcal{Z})\ne 0\Rightarrow\operatorname{rank}E(\mathbb{Q})\ge 2$.* Serious attempt and its outcome: §6.

### 2.3 Bridge (iii): Kolyvagin's vanishing index and analytic data

**Kolyvagin's structure theorem.** [THEOREM] (Kolyvagin [Kol91, Thm. 4], in the formulation of [Zha14, Thm. 1.2] and [BCGS, Cor. A]). Let $(E,p,K)$ satisfy (Heeg), (disc), $E(K)[p]=0$, $p$ odd, and suppose $\kappa^{\mathrm{Heeg}}\neq 0$ (Kolyvagin's conjecture; a theorem under the hypotheses of [Zha14, Thm. 1.1] — $p\ge 5$ good ordinary, $\bar\rho_{E,p}$ surjective, $N^-$ squarefree with an even number of prime factors, Hypothesis $\spadesuit$ — or of [BCGS, Thm. A] — $p$ odd good ordinary split in $K$, and the rational anticyclotomic main conjecture, known for $p>3$ with $E[p]$ irreducible [BCS25] and in Eisenstein cases [CGS25]). Put $\nu_\infty:=\operatorname{ord}(\kappa^{\mathrm{Heeg}})$ and $\varepsilon_{\nu_\infty}:=\varepsilon\cdot(-1)^{\nu_\infty+1}$ with $\varepsilon=w(E)$. Then
$$
\nu_\infty=\max\{r^+,r^-\}-1,\qquad r^{\varepsilon_{\nu_\infty}}=\nu_\infty+1,\qquad 0\le\nu_\infty-r^{-\varepsilon_{\nu_\infty}}\equiv 0\pmod 2 .
$$

**[NEW] Proposition 2.2 (the rank-2 bridge, exact form).** Let $E/\mathbb{Q}$ with $r_{\mathrm{an}}(E)=2$ (so $\varepsilon=+1$). Let $K$ satisfy (Heeg), (disc) with $r_{\mathrm{an}}(E^K)=1$ (such $K$ exist: under (Heeg) one has $w(E^K)=-w(E)=-1$, and [BFH90], [MM91] give infinitely many quadratic twists in prescribed residue classes with non-vanishing first derivative), and let $p$ be odd with $E(K)[p]=0$ such that Kolyvagin's conjecture and the structure theorem above hold for $(E,p,K)$ (e.g. under the hypotheses of [Zha14, Thm. 1.1] or of [BCGS, Thm. A]). Then:

1. $r^-=\operatorname{corank}\operatorname{Sel}_{p^\infty}(E^K/\mathbb{Q})=1$;
2. $\nu_\infty=\operatorname{ord}(\kappa^{\mathrm{Heeg}})$ is **odd** (in particular $\ge 1$), and
$$
\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\nu_\infty+1\ \ge 2 ;
$$
3. consequently
$$
\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)=2
\iff\nu_\infty=1
\iff\exists\ell\in\mathcal L^{\mathrm{Heeg}}:\kappa^{\mathrm{Heeg}}_\ell\ne0.
$$
If two independent rational points are additionally exhibited, these conditions
imply $\operatorname{rank}E(\mathbb Q)=2$ and $\operatorname{Sha}[p^\infty]$ finite.
Alternatively $\mathrm{Fin}(p)$ plus any of the equivalent conditions gives the same conclusion.
The converse from rank two **and** primary finiteness is valid without an extra point hypothesis.

First nonvanishing does not imply $\mathscr M_1=\mathscr M_\infty$.
That stronger divisibility condition must be kept separate. Under compatible
index conventions, the additional corank-difference-one hypotheses in
[Kim24, Theorem 2.3] give the finite-part formula
$\operatorname{length}\operatorname{Sel}(E/K)_{/\mathrm{div}}
=2(\mathscr M_1-\mathscr M_\infty)$ when $\nu_\infty=1$.
Thus stabilization also forces a trivial finite Selmer quotient; it is not
just a statement about the first nonzero class.

*Proof.* The analytic-rank-one twist has Mordell–Weil rank one and finite Sha,
so $r^-=1$. Gross–Zagier makes $P_K$ torsion since the analytic rank over $K$
is three. As $E(K)[p]=0$, its Kummer class is zero, and $\nu_\infty\ge1$.
If $\nu_\infty$ were even, the structure theorem would give
$r^-=\nu_\infty+1\ge3$, a contradiction. Hence $\nu_\infty$ is odd and
$r^+=\nu_\infty+1$. This proves the displayed equivalences. Finally
$r^+=r_{\mathrm{alg}}+\operatorname{corank}\operatorname{Sha}[p^\infty]$;
the extra rank lower bound, or primary finiteness, supplies exactly the
missing condition for rank two. $\square$

*Remark.* Part (2) says that under Kolyvagin's conjecture, $r_{\mathrm{an}}=2$ forces $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ge 2$ — the Selmer lower bound in even rank (also obtainable from the rational main conjecture + parity, §1.1). Nothing forces $\nu_\infty\ne 3,5,\dots$: BSD predicts $\nu_\infty=1$, and Prop. 2.2 makes "$\nu_\infty=1$" the exact statement to prove. This is the complete statement of Bridge (iii) on the Heegner side; the full Kolyvagin analysis is in `approaches/B`.

**The cyclotomic side of Bridge (iii): Kurihara numbers.** Here the analytic data are *explicit modular symbols*, and the structure theorem is complete.

Let $[a/b]^{\pm}\in\mathbb{Q}$ be defined by $2\pi\int_0^\infty f_E(a/b+iy)\,dy=[a/b]^+\Omega^+_E+[a/b]^-\,i\,\Omega^-_E$. For $k\ge1$ let $\mathcal{P}^{\mathrm{cyc}}_k=\{\ell\nmid Np:\ \ell\equiv 1,\ a_\ell\equiv\ell+1\pmod{p^k}\}$, $I_\ell=(\ell-1,a_\ell-\ell-1)\mathbb{Z}_p$, $\mathcal{N}^{\mathrm{cyc}}_1$ the squarefree products, $I_n=\sum_{\ell\mid n}I_\ell$. Fix generators $\eta_\ell$ of $(\mathbb{Z}/\ell)^\times$ and $\log_{\eta_\ell}:(\mathbb{Z}/\ell)^\times\to\mathbb{Z}/(\ell-1)$. The **Kurihara number** is
$$
\tilde\delta_n=\sum_{a\in(\mathbb{Z}/n)^\times}\overline{[a/n]^+}\prod_{\ell\mid n}\overline{\log_{\eta_\ell}(a)}\ \in\ \mathbb{Z}_p/I_n,\qquad \tilde\delta_1=[0]^+=L(E,1)/\Omega^+_E,
$$
well defined up to $(\mathbb{Z}_p/I_n)^\times$ ([Kur14, (1.2)], [Kim24, §3.1.1]); $\operatorname{ord}(\tilde{\boldsymbol\delta}):=\min\{\nu(n):\tilde\delta_n\ne 0\}$ and $\partial^{(i)},\partial^{(\infty)}$ the divisibility indices as in [Kim24, §2.2].

**[THEOREM] (Kurihara [Kur14, Thm. 1.1.1] under main conjecture + non-degenerate height; Kim [Kim25], stated as [Kim24, Thm. 3.1], unconditionally).** Let $E/\mathbb{Q}$ be non-CM, $p\ge 5$ with (a) $\bar\rho_{E,p}$ surjective and (b) the Manin constant prime to $p$ (automatic if $E$ is semistable at $p$). If $\operatorname{ord}(\tilde{\boldsymbol\delta})<\infty$, then
$$
\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{ord}(\tilde{\boldsymbol\delta}),
$$
and the finite part $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})_{/\mathrm{div}}$ is determined by the $\partial^{(i)}(\tilde{\boldsymbol\delta})$ [Kim24, Thm. 3.1(2),(3)]. Moreover $\operatorname{ord}(\tilde{\boldsymbol\delta})<\infty$ holds if $E$ is semistable with good ordinary reduction at $p\ge 5$ and $\bar\rho_{E,p}$ surjective [Kim24, Cor. 2.2]; in general it is equivalent to the main conjecture localised at the augmentation ideal [Kim24, Thm. 2.1 (IMC)].

**[THEOREM] (Kim's "higher Gross–Zagier formula" [Kim24, Thm. 2.3]).** Under the working hypotheses of [Kim24, §2.1] with $\nu(N^-)$ even, if $\kappa^{\mathrm{Heeg}}\ne 0$ and $\tilde{\boldsymbol\delta}(E),\tilde{\boldsymbol\delta}(E^K)\ne 0$, then $\operatorname{ord}(\kappa^{\mathrm{Heeg}})+1=\max\{\operatorname{ord}\tilde{\boldsymbol\delta}(E),\operatorname{ord}\tilde{\boldsymbol\delta}(E^K)\}$ (and the corresponding minimum formula for $\operatorname{ord}(\kappa^{\mathrm{Heeg}})$ holds only if the two Selmer coranks differ by one), together with an exact formula for $\operatorname{length}\operatorname{Sel}_{p^\infty}(E/K)_{/\mathrm{div}}$.

So the two Kolyvagin systems (Heegner, Kato) are both *complete* descriptions of $\operatorname{Sel}_{p^\infty}$, and both are now known to be non-zero. The bridge to $r_{\mathrm{an}}$ is missing on both. On the cyclotomic side the missing bridge can be stated with unusual precision, because $\tilde\delta_n$ *is* built from $L$-values:

**[NEW] Proposition 2.3 (Kurihara numbers of prime conductor are $(\zeta_p-1)$-derivatives of twisted $L$-values).** Let $E/\mathbb{Q}$, $p$ odd, and suppose $[a/b]^+\in\mathbb{Z}_{(p)}$ for all $a/b$ (true under (a),(b) above). Let $\ell\nmid Np$ be a prime with $\ell\equiv 1$ and $a_\ell\equiv\ell+1\pmod p$; let $\chi:(\mathbb{Z}/\ell)^\times\to\mu_{p^j}$ be a character of exact order $p^j$, $1\le j\le\operatorname{ord}_p(\ell-1)$, normalised by $\chi(\eta_\ell)=\zeta$ (a primitive $p^j$-th root of unity), and put
$$
L^{\mathrm{alg}}(E,\bar\chi,1):=\frac{\tau(\chi)\,L(E,\bar\chi,1)}{\Omega^+_E},\qquad \tau(\chi)=\sum_{a}\chi(a)e^{2\pi ia/\ell}.
$$
Then $L^{\mathrm{alg}}(E,\bar\chi,1)\in\mathbb{Z}_{(p)}[\zeta]$ (although $\tau(\chi)\notin\mathbb{Q}(\zeta)$ in general), and in $\mathbb{Z}_p[\zeta]$:
$$
L^{\mathrm{alg}}(E,\bar\chi,1)\ \equiv\ (\zeta-1)\cdot\tilde\delta_\ell\ \pmod{(\zeta-1)^2},
$$
where $\tilde\delta_\ell$ is read modulo $p$ via $\mathbb{Z}_p[\zeta]/(\zeta-1)\cong\mathbb{F}_p$. In particular $\tilde\delta_\ell\not\equiv 0\pmod p$ iff $\operatorname{ord}_{(\zeta-1)}L^{\mathrm{alg}}(E,\bar\chi,1)=1$, and this does not depend on the choice of $\chi$ (of any $p$-power order dividing $\ell-1$).

*Proof.* (i) *Birch's lemma.* For a primitive character $\chi$ mod $\ell$ and all $n\ge1$, $\chi(n)=\tau(\bar\chi)^{-1}\sum_{a}\bar\chi(a)e^{2\pi ian/\ell}$ (both sides vanish for $\ell\mid n$). Hence, using $\int_0^\infty e^{2\pi in(a/\ell+iy)}dy=e^{2\pi ina/\ell}/2\pi n$ and absolute convergence for $\Re s>3/2$ followed by analytic continuation of both sides (the right side is a finite sum of Mellin transforms),
$$
L(E,\chi,1)=\tau(\bar\chi)^{-1}\sum_{a}\bar\chi(a)\,2\pi\!\int_0^\infty f_E(a/\ell+iy)\,dy=\tau(\bar\chi)^{-1}\sum_a\bar\chi(a)\big([a/\ell]^+\Omega^+_E+i[a/\ell]^-\Omega^-_E\big).
$$
Since $z\mapsto-\bar z$ acts on $[a/\ell]^\pm$ by $\pm1$ (i.e. $[-a/\ell]^\pm=\pm[a/\ell]^\pm$) and $\chi$ of odd order is even, the $[\ ]^-$ terms cancel. Replacing $\chi$ by $\bar\chi$: $\sum_a\chi(a)[a/\ell]^+=\tau(\chi)L(E,\bar\chi,1)/\Omega^+_E=L^{\mathrm{alg}}(E,\bar\chi,1)$, which lies in $\mathbb{Z}_{(p)}[\zeta]$ because the $[a/\ell]^+$ do.
(ii) *Expansion.* Write $\chi(a)=\zeta^{\log_{\eta_\ell}(a)}$. For $k\in\mathbb{Z}$, $\zeta^k-1=(\zeta-1)(1+\zeta+\dots+\zeta^{k-1})\equiv k(\zeta-1)\pmod{(\zeta-1)^2}$ (each $\zeta^i\equiv 1$); this is compatible with reading $k$ modulo $p^j$, in particular modulo $\ell-1$. Therefore
$$
L^{\mathrm{alg}}(E,\bar\chi,1)=\sum_a[a/\ell]^+\ +\ (\zeta-1)\sum_a[a/\ell]^+\log_{\eta_\ell}(a)\ +\ O\big((\zeta-1)^2\big).
$$
(iii) *The constant term.* The Hecke relation $T_\ell\{0\}=\{0\}+\sum_{a=0}^{\ell-1}\{a/\ell\}$ for the modular symbol $\{x\}=\int_x^{i\infty}f_E$ (with $\ell\nmid N$) gives $\sum_{a\in(\mathbb{Z}/\ell)^\times}[a/\ell]^+=(a_\ell-2)[0]^+$. Since $a_\ell\equiv\ell+1\equiv 2\pmod p$ and $[0]^+\in\mathbb{Z}_{(p)}$, this lies in $p\mathbb{Z}_p\subset(\zeta-1)^{\varphi(p^j)}\subset(\zeta-1)^2$ ($p$ odd). The middle term is $(\zeta-1)\tilde\delta_\ell$ by definition. $\square$

**[NEW] Corollary 2.4 (an analytic congruence attached to the Selmer lower bound).** Let $E/\mathbb{Q}$ be non-CM and $p\ge 5$ a good ordinary prime such that: $\bar\rho_{E,p}$ is surjective (hence $\rho_{E,p}$ is, [SW13, Prop. 7.2]); the Manin constant is prime to $p$; and Kurihara's standing hypotheses [Kur14, §1.1 (iii),(iv)] hold: the algebraic $\mu$-invariant vanishes, $p\nmid\prod_v c_v$, and $p\nmid\#E(\mathbb{F}_p)$. Let $\mathcal{P}_1^{(1)}=\{\ell\nmid Np:\ \ell\equiv1\pmod p,\ E(\mathbb{F}_\ell)[p]\cong\mathbb{Z}/p\}$ (so $a_\ell\equiv\ell+1\pmod p$). Then:

1. If for some $\ell\in\mathcal{P}_1^{(1)}$ and some (equivalently every) character $\chi$ mod $\ell$ of order $p$ one has $\operatorname{ord}_{(\zeta_p-1)}L^{\mathrm{alg}}(E,\bar\chi,1)=1$, then $\dim_{\mathbb{F}_p}\operatorname{Sel}(E/\mathbb{Q},E[p])\le 1$; hence $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le1$, and $w(E)=-1$ if in addition $L(E,1)=0$.
2. Consequently, if $r_{\mathrm{an}}(E)$ is even and $\ge 2$ and the rational main conjecture holds at $p$, then
$$
(\zeta_p-1)^2\ \big|\ L^{\mathrm{alg}}(E,\bar\chi,1)\quad\text{for every }\ell\in\mathcal{P}_1^{(1)}\text{ and every }\chi\text{ mod }\ell\text{ of order }p .
$$
3. Assume $\operatorname{ord}(\tilde{\boldsymbol\delta})<\infty$ (automatic if $E$ is semistable, [Kim24, Cor. 2.2]). Then $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ge2$ iff $L(E,1)=0$ and $\tilde\delta_\ell=0$ in $\mathbb{Z}_p/I_\ell$ for every $\ell\in\mathcal{P}^{\mathrm{cyc}}_1$; this implies the congruence in (2) for all $(\ell,\chi)$, and for those $\ell$ with $I_\ell=p\mathbb{Z}_p$ the vanishing of $\tilde\delta_\ell$ *is* the congruence. In particular, for $r_{\mathrm{an}}(E)\ge3$ odd, BSD predicts the congruence in (2) for all $(\ell,\chi)$. The congruence alone does not establish a Selmer lower bound: its converse has not been proved here.

*Proof.* (1) By Prop. 2.3, $\tilde\delta_\ell$ is a unit mod $p$; Kurihara's theorem [Kur14, Thm. 1.2.3(1)] (with $N=1$, $m=\ell$) says the localisation map $\operatorname{Sel}(E/\mathbb{Q},E[p])\to E(\mathbb{Q}_\ell)\otimes\mathbb{Z}/p\cong\mathbb{Z}/p$ is injective. As $E(\mathbb{Q})[p]=0$, $\operatorname{Sel}(E/\mathbb{Q},E[p])=\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})[p]$, whose $\mathbb{F}_p$-dimension bounds the corank. Parity [DD10] gives the sign. (2) Under the rational main conjecture, $L(E,1)=0\Rightarrow\operatorname{corank}\operatorname{Sel}\ge1$ (§1.1), and parity gives $\ge2$; so by (1) no $\tilde\delta_\ell$ is a unit mod $p$, and Prop. 2.3 converts this into the congruence. (3) By [Kim24, Thm. 3.1(1)], $\operatorname{corank}\operatorname{Sel}\ge 2\iff\operatorname{ord}(\tilde{\boldsymbol\delta})\ge2\iff\tilde\delta_1=0$ and $\tilde\delta_\ell=0$ in $\mathbb{Z}_p/I_\ell$ for all $\ell\in\mathcal{P}^{\mathrm{cyc}}_1$; $\tilde\delta_1=L(E,1)/\Omega^+_E$. Vanishing in $\mathbb{Z}_p/I_\ell$ implies vanishing mod $p$ (as $I_\ell\subset p\mathbb{Z}_p$), which is the congruence by Prop. 2.3; if $I_\ell=p\mathbb{Z}_p$ the two are the same. No converse from the mod-$p$ congruences alone is asserted. $\square$

*Remark (what is and is not captured mod $p$).* First reduce coefficients modulo $I_\ell$. The augmentation of $\theta_\ell=\sum_a[a/\ell]^+\sigma_a$ then vanishes, and its linear augmentation term yields $\tilde\delta_\ell$. Over $\mathbb Z_p$ itself, the augmentation $(a_\ell-2)[0]^+$ need not be zero, so a class in $I/I^2$ cannot be asserted without this qualification; its reduction mod $p$ is detected by *individual* twisted $L$-values modulo $(\zeta-1)^2$ (Prop. 2.3), but its class modulo $p^k$ for $k\ge2$ is a $p$-adic linear combination of all the $[a/\ell]^+$ with coefficients $\log_{\eta_\ell}(a)$ that is not a value of $\theta_\ell$ at a single character. So the exact Selmer statement lives in $\mathbb{Z}_p/I_\ell$, while its mod-$p$ shadow is an honest statement about twisted $L$-values.

*Why this is the right formulation of the missing bridge.* The cyclotomic $p$-adic $L$-function sees twists by characters of $p$-power **conductor** ("vertical" direction; this is where $\operatorname{ord}_{s=1}L(E,s)$ lives). The Kurihara numbers see twists of order $p$ and prime conductor $\ell\equiv 1\pmod p$ ("horizontal" direction; this is where the Mazur–Tate elements $\theta_\ell=\sum_a[a/\ell]^+\sigma_a\in\mathbb{Z}_{(p)}[(\mathbb{Z}/\ell)^\times]$ live, and Prop. 2.3 identifies $\tilde\delta_\ell$ with the image of $\theta_\ell$ in $I/I^2$ of the augmentation ideal, i.e. with the *Mazur–Tate refined conjecture* [MT87] at the level of first derivatives). The Mazur–Tate refined conjecture predicts $\theta_n\in I_n^{\,r_{\mathrm{alg}}}$; combined with BSD this is "$\tilde\delta_n=0$ for $\nu(n)<r_{\mathrm{an}}$". **There is no known mechanism relating vertical vanishing ($\operatorname{ord}_{s=1}$) to horizontal vanishing ($\theta_\ell\in I^2$).** Everything proved in rank $\le 1$ (and in even rank $\ge 2$, Cor. 2.4(2)) about horizontal vanishing goes *through the Selmer group*, never directly through analysis.

**[THEOREM: former GAP 5 resolved in its standing hypotheses].**
For non-CM $E$, $p\ge5$ good ordinary with irreducible $E[p]$, odd analytic
rank at least three implies $s_p(E)\ge3$. Under residual surjectivity and
the Manin-constant hypothesis, Kim's theorem then forces
$\tilde\delta_n=0$ in the full quotient $\mathbb Z_p/I_n$ for every
$\nu(n)<3$. No independent nonvanishing hypothesis for the family is needed
for this implication. The proof and the semistable supersingular extension
are in [odd-rank-selmer-bridge.md](synthesis/odd-rank-selmer-bridge.md).
The next odd lower-bound target is O5 there, concerning two-prime Heegner
classes when the analytic rank is at least five.

**[GAP 6] (the Kolyvagin bridge for rank-2 curves).** *Let $E/\mathbb{Q}$ with $r_{\mathrm{an}}=2$, $K$ with $r_{\mathrm{an}}(E^K)=1$, $(E,p,K)$ as in Prop. 2.2 with $\bar\rho_{E,p}$ surjective and $p>3$. Prove $\operatorname{ord}(\kappa^{\mathrm{Heeg}})=1$, i.e. exhibit one Kolyvagin prime $\ell$ with $\kappa^{\mathrm{Heeg}}_\ell\ne0$. Do not replace this by equality of the first and limiting divisibility indices.* The known analytic handle on $\kappa_\ell^{\mathrm{Heeg}}$ is *mod $p$ and for a different form*: by the first explicit reciprocity law of Bertolini–Darmon [BD05] in Zhang's formulation [Zha14, §§5–7] (bipartite Euler systems, cf. [Kim24, §2.4]), the localisation $\operatorname{loc}_\ell(\kappa^{\mathrm{Heeg}}_{\ell})$ is (up to units) the algebraic part mod $p$ of $L(g_\ell/K,1)$ for a newform $g_\ell$ of level $N\ell$ congruent to $f_E$ mod $p$ (level raising). Thus $\kappa^{\mathrm{Heeg}}_\ell\ne0$ follows from $p\nmid L^{\mathrm{alg}}(g_\ell/K,1)$ for *some* level-raised $g_\ell$ — a statement about a congruent form, not about $L(E,s)$. Details and the attempt: `approaches/B` and §6 below.

---

## 3. Finiteness of $\operatorname{Sha}$ in rank $\ge 2$

### 3.1 The precise claim

**Status claim (with source [SW13, p. 1758]).** "The group $\operatorname{Sha}(E/\mathbb{Q})$ is not known to be finite for even a single elliptic curve with $r_{\mathrm{an}}\ge 2$." We searched (arXiv listings, 2020–2026, keywords "finiteness of Tate–Shafarevich group rank 2", "Sha finite rank two elliptic curve", the BCGS/Kim/Castella–Hsieh introductions of 2022–2026) and found no claim to the contrary as of 2026-09-11; Castella–Hsieh [CH22, Remark 1.3] and Kim [Kim24, §1] still treat finiteness of $\operatorname{Sha}[p^\infty]$ for rank-2 curves as a hypothesis. The claim is therefore stated as: *no $E/\mathbb{Q}$ with $r_{\mathrm{an}}\ge2$ (equivalently, by GZK, with $r_{\mathrm{alg}}\ge 2$) has $\operatorname{Sha}(E/\mathbb{Q})$ known to be finite.* [unverified beyond the literature search described]

Three distinct statements must be separated:

* (S1) $\operatorname{Sha}(E/\mathbb{Q})$ finite $\iff$ $\operatorname{Sha}[p^\infty]$ finite for every $p$ **and** $\operatorname{Sha}[p]=0$ for all but finitely many $p$.
* (S2) $\operatorname{Sha}[p^\infty]$ finite for a *specified* $p$.
* (S3) $\operatorname{Sha}[p]=0$ for a specified $p$ (hence $\operatorname{Sha}[p^\infty]=0$).

For rank $\ge 2$ curves, (S2) and (S3) are known for many $(E,p)$; (S1) for none.

### 3.2 The chain giving $p$-primary finiteness, with exact hypotheses

**Proposition 3.1 ($p$-primary finiteness from a $p$-adic computation; [SW13, §7.1, Prop. 10.1, Alg. 11.1]; proof included).** Let $p$ be an odd prime of good ordinary reduction. Suppose $r_{\mathrm{alg}}\ge r_p$ (e.g. $r_p=2$ is verified numerically — a finite computation, since it is an *upper bound* on $\operatorname{ord}_{T=0}$ of a power series computed to finite precision — and two independent points are exhibited). Then
$$
r_{\mathrm{alg}}=\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{ord}_{T=0}f_E=r_p,\qquad\operatorname{Sha}(E/\mathbb{Q})[p^\infty]\ \text{is finite},
$$
the $p$-adic height pairing on $E(\mathbb{Q})$ is non-degenerate. If Kato's divisibility holds integrally (in particular under the surjectivity hypothesis stated in §1.3), then
$$
\operatorname{ord}_p\#\operatorname{Sha}[p^\infty]\ \le\ \operatorname{ord}_p\Big(\frac{L_p^{(r)}(E,0)}{r!}\Big)-\operatorname{ord}_p\Big(\frac{\epsilon_p\prod_vc_v\cdot\operatorname{Reg}_\gamma(E/\mathbb{Q})}{\#E(\mathbb{Q})[p^\infty]^2}\Big),
$$
with equality if $\bar\rho_{E,p}$ is surjective and the integral main conjecture holds at $p$ ($\epsilon_p$, $\operatorname{Reg}_\gamma$ as in §1.3).
*Proof.* Prop. 1.2 squeezes the chain to equalities. Finiteness of $\operatorname{Sha}[p^\infty]$ and non-degeneracy follow from [SW13, Thm. 6.1] (Schneider–Perrin-Riou), which also gives the valuation of the leading term of $f_E$; Kato's divisibility $f_E\mid L_p$ (in $\Lambda$ when $\bar\rho_{E,p}$ is surjective, [SW13, Thm. 7.3]) compares leading terms; the main conjecture makes it an equality. $\square$

**Numerical status (evidence, not proof; charter rule 6).**
* [SW13, Thm. 1.1]: for all $1{,}534{,}422$ pairs $(E,p)$ with $E$ non-CM, $\operatorname{rank}E(\mathbb{Q})\ge 2$, $N\le 30{,}000$, $5\le p<1000$ good ordinary, $\bar\rho_{E,p}$ surjective: $\operatorname{Sha}(E/\mathbb{Q})[p]=0$ (via $r=\operatorname{ord}_TL_p(E,T)$ and the $p$-adic BSD leading term $\equiv 1\bmod p$).
* [SW13, Thm. 12.3]: for $E=389a1$ ($r_{\mathrm{alg}}=r_{\mathrm{an}}=2$), $\operatorname{Sha}[p]=0$ for $p=2$ and all $5{,}005$ good ordinary $p<48{,}859$ except $p=16{,}231$ (where $\operatorname{ord}_p\operatorname{Reg}_p=3>2$ and the computation was too expensive — the regulator is *unusually divisible*, not zero).
* [LMFDB, 389.a1, accessed 2026-09-11]: $r_{\mathrm{an}}=2$, $r=2$, $\Omega\approx4.9804$, $\operatorname{Reg}\approx0.15246$, $L^{(2)}(E,1)/2!\approx0.759317$, analytic $\#\operatorname{Sha}\approx 1$; $E$ semistable, $\rho_{E,\ell}$ surjective for all $\ell$; Iwasawa invariants $(\lambda,\mu)=(2,0)$ for every good ordinary $p\in\{3,5,\dots,47\}$ and $\lambda=3$ at the split multiplicative prime $389$. Since $r_p\le\lambda_p$ and $r_p\ge r_{\mathrm{alg}}=2$ (Prop. 1.2), this gives $r_p=2$ and hence (Prop. 3.1) $\operatorname{Sha}[p^\infty]$ finite for each of these $p$; $\mu=0$, $\lambda=2$ mean $L_p(E,T)=T^2\cdot(\text{unit})$, so the leading coefficient is a $p$-unit, and since the integral main conjecture holds for these $p$ ([SU14]: $\bar\rho_{E,p}$ surjective, $389\,\|\,N$ with $\bar\rho_{E,p}$ ramified at $389$ as $p\nmid\operatorname{ord}_{389}\Delta=1$), $\operatorname{ord}_p\big(\epsilon_p\cdot\#\operatorname{Sha}[p^\infty]\cdot\operatorname{Reg}_\gamma\big)=0$ (Tamagawa product and torsion are trivial). Note $p=3$ is anomalous for this curve ($a_3=-2$, $\#\tilde E(\mathbb{F}_3)=6$), so $\epsilon_3$ is not a unit and the identity constrains $\operatorname{Reg}_\gamma$ as well as $\operatorname{Sha}[3^\infty]$; [SW13, Thm. 12.3] independently gives $\operatorname{Sha}[p]=0$ for all these $p$.

### 3.3 Why "all $p$ at once" is the crux

**The single objects in rank $0$ and $1$.**
* Rank $0$: the object is the rational number $L(E,1)/\Omega_E\in\mathbb{Q}^\times$ (Manin). Kato's bound gives $\#\operatorname{Sha}[p^\infty]\le p$-part of $L(E,1)/\Omega_E\cdot(\text{Tamagawa, torsion})$ for all $p$ with $\bar\rho_{E,p}$ surjective, hence $\operatorname{Sha}[p^\infty]=0$ for all but finitely many $p$, and finite for the rest. One object, all $p$.
* Rank $1$: the object is $P_K\in E(K)$ with the fixed integer $[E(K):\mathbb{Z}P_K+\text{tors}]$; Kolyvagin bounds $\#\operatorname{Sha}(E/K)[p^\infty]$ by a power of this index (times fixed fudge), uniformly in $p$. Gross–Zagier identifies the index with $L'(E/K,1)/(\Omega\cdot\langle P_K,P_K\rangle)$ up to a fixed rational. The **cyclotomic** route in rank $1$ would instead need, at each $p$, $L_p'(E,0)/\langle P,P\rangle_p=e_p\cdot L'(E,1)/(\Omega\langle P,P\rangle_{\mathrm{NT}})$ ($p$-adic Gross–Zagier, §2.1) — again a *fixed* rational number times a local factor — but it also needs [GAP 1] at every $p$, which is why the anticyclotomic/Heegner route is the one that works.

**Candidates in rank $2$, and why each fails to be $p$-independent.**

(a) *Kato's element.* $\zeta^{\mathrm{Kato}}_E=0$ (Prop. 1.1). The derived classes $\kappa^{\mathrm{Kato}}_n$ are defined for $n$ built from primes $\ell\equiv 1\pmod p$: their index set depends on $p$.

(b) *Heegner points.* $P_K$ is torsion for every $K$ (§1.2(a)).

(c) *Derived Heegner points.* The points $D_\ell y_\ell\in E(K[\ell])$ (Kolyvagin's derivative operator applied to the Heegner point of conductor $\ell$) are honest, $p$-independent points over ring class fields, but:

**Lemma 3.2 (elementary).** For a fixed prime $\ell\nmid ND_K$ inert in $K$, the set of primes $p$ for which $\ell$ is a Kolyvagin prime (i.e. $p\mid\gcd(\ell+1,a_\ell)$) is finite, of cardinality $\le\omega(\ell+1)$.
*Proof.* $\ell+1\neq0$, so $\gcd(\ell+1,a_\ell)$ is a positive integer dividing $\ell+1$ (it equals $\ell+1$ if $a_\ell=0$). $\square$

Thus a fixed finite set of conductors can be used as Kolyvagin indices
for only finitely many $p$ through the stated divisibility conditions.
A varying-conductor construction is not ruled out. Nonzero derived classes,
unit derived classes, and a trivial finite Selmer quotient are distinct
conditions; the exact implications require the rank and divisibility
hypotheses discussed in corrected Proposition 2.2.

(d) *The BSD leading term.* Rationality of
$c_E=L^{(r)}(E,1)/(r!\Omega_E\operatorname{Reg}_{\mathrm{NT}})$ is only a
rationality assertion. It does not identify $c_E$ with an arithmetic order
or with $p$-adic leading terms. The following proposition uses a separate
comparison hypothesis and concludes only within its stated ordinary-prime set.

**[NEW] Proposition 3.3 (uniformity $\Rightarrow$ almost-all-$p$ triviality of $\operatorname{Sha}$; conditional on the main conjecture).** Let $E/\mathbb{Q}$ be non-CM with $r:=r_{\mathrm{alg}}$, and assume $E$ has at least one prime $q$ of multiplicative reduction. Let $\mathcal{P}$ be the set of good ordinary primes $p>3$ with $\bar\rho_{E,p}$ surjective and $p\nmid\operatorname{ord}_q\Delta_E$; $\mathcal{P}$ contains all but finitely many good ordinary primes ([Ser72]; $\bar\rho_{E,p}$ is ramified at $q$ if $p\nmid\operatorname{ord}_q\Delta_E$, [SW13, after Thm. 7.5]), and the integral main conjecture $L_p(E,T)=f_E(T)\cdot u(T)$, $u\in\Lambda^\times$, holds at every $p\in\mathcal{P}$ [SU14, Thm. 1], [SW13, Thm. 7.5]. Write the $p$-adic BSD conjecture of [MTT86] in the normalisation of [SW13, Conj. 5.1 and Thm. 6.1] as
$$
\frac{L_p^{(r)}(E,0)}{r!}\ \overset{?}{=}\ \epsilon_p\cdot\frac{\prod_vc_v\cdot\#\operatorname{Sha}(E/\mathbb{Q})\cdot\operatorname{Reg}_\gamma(E/\mathbb{Q})}{\#E(\mathbb{Q})_{\mathrm{tors}}^2},
$$
with $\epsilon_p$ the explicit $p$-adic multiplier of loc. cit. (a $p$-adic unit for non-anomalous $p$) and $\operatorname{Reg}_\gamma$ the $p$-adic regulator normalised as there. Consider the **uniformity statement**
$$
\mathrm{U}(E):\qquad \exists\,c_E\in\mathbb{Q}^\times\ \text{ such that for all but finitely many }p\in\mathcal{P}:\quad \operatorname{Reg}_\gamma(E/\mathbb{Q})\ne0\ \text{ and }\ \frac{L_p^{(r)}(E,0)/r!}{\epsilon_p\operatorname{Reg}_\gamma(E/\mathbb{Q})}=c_E .
$$
Then $\mathrm{U}(E)$ implies: for all but finitely many $p\in\mathcal{P}$, $r_p=r$, $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]$ is finite, the $p$-adic height is non-degenerate, and $\operatorname{Sha}(E/\mathbb{Q})[p^\infty]=0$ (the exceptions being the finitely many $p$ excluded in $\mathrm{U}(E)$ together with the divisors of the numerator and denominator of $c_E$, of $\prod_vc_v$ and of $\#E(\mathbb{Q})_{\mathrm{tors}}$). Conversely, BSD (leading term) for $E$, the $p$-adic BSD formulas for all $p\in\mathcal{P}$, and nonzero $p$-adic regulators for all but finitely many $p\in\mathcal P$ imply $\mathrm{U}(E)$ with $c_E=L^{(r)}(E,1)/(r!\,\Omega_E\operatorname{Reg}_{\mathrm{NT}}(E/\mathbb{Q}))$.

*Proof.* Fix $p\in\mathcal{P}$ as in $\mathrm{U}(E)$, not dividing the numerator or denominator of $c_E$, nor $\prod c_v$, nor $\#E(\mathbb{Q})_{\mathrm{tors}}$. Since $c_E\ne0$ and $\operatorname{Reg}_\gamma\ne0$, $L_p^{(r)}(E,0)\ne0$, so $r_p\le r$; Prop. 1.2 gives $r_p\ge r$. Hence $r_p=r=r_{\mathrm{alg}}$ and Prop. 3.1 applies: $\operatorname{Sha}[p^\infty]$ is finite, the height is non-degenerate, and by [SW13, Thm. 6.1] $\operatorname{ord}_p f_E^{*}(0)=\operatorname{ord}_p\big(\epsilon_p\prod c_v\#\operatorname{Sha}[p^\infty]\operatorname{Reg}_\gamma/\#E(\mathbb{Q})[p^\infty]^2\big)$, where $f_E^*(0)$ is the leading coefficient of $f_E$ at $T=0$. The integral main conjecture gives $\operatorname{ord}_p(L_p^{(r)}(E,0)/r!)=\operatorname{ord}_pf_E^*(0)$ (same order of vanishing, unit ratio). Substituting $\mathrm{U}(E)$: $\operatorname{ord}_p(c_E)+\operatorname{ord}_p(\epsilon_p\operatorname{Reg}_\gamma)=\operatorname{ord}_p(\epsilon_p\operatorname{Reg}_\gamma)+\operatorname{ord}_p\#\operatorname{Sha}[p^\infty]+\operatorname{ord}_p\prod c_v-2\operatorname{ord}_p\#E(\mathbb{Q})_{\mathrm{tors}}$, i.e. $\operatorname{ord}_p\#\operatorname{Sha}[p^\infty]=0$. Under the added regulator hypothesis the converse is obtained by dividing the two conjectural formulas ($p$-adic BSD as displayed; BSD: $L^{(r)}(E,1)/r!=\Omega_E\prod c_v\#\operatorname{Sha}\operatorname{Reg}_{\mathrm{NT}}/\#E_{\mathrm{tors}}^2$). $\square$

*Caveat on normalisations.* Whether $\epsilon_p$ and the $\log_p\kappa(\gamma)$-factors are placed in $\operatorname{Reg}_\gamma$ or displayed separately varies between [MTT86], [SW13, §4–6] and [PR03]; the proof uses only that [SW13, Thm. 6.1] and the $p$-adic BSD conjecture are written in *the same* normalisation, which is how [SW13] states them. A reader testing $\mathrm{U}(E)$ numerically must fix conventions as in [SW13, Lemma 4.2].

**[GAP 7] (uniformity of $p$-adic leading terms in rank $\ge 2$).** *Prove $\mathrm{U}(E)$ for one $E/\mathbb{Q}$ with $r_{\mathrm{alg}}=r_{\mathrm{an}}=2$ (e.g. $389a1$).* In rank $\le 1$, $\mathrm{U}(E)$ is a theorem: rank $0$ by interpolation; rank $1$ by $p$-adic Gross–Zagier + Gross–Zagier, *modulo* $\operatorname{Reg}_p\ne0$ at each $p$ [GAP 1]. In rank $2$ it is an open statement about infinitely many *unrelated* $p$-adic numbers, with no complex number known to tie them together. This is the exact content of "all $p$ at once".

**Further uniformity work.** Lemma 3.2 limits which primes a *fixed*
derived conductor can serve. It does not exclude a varying-conductor family
or a different global construction. In particular the
[continuation](synthesis/continuation-2026-09-12.md) gives a sufficient
unit-Kurihara-witness target covering both ordinary and supersingular primes
under Kim's hypotheses. No implication from complex rationality alone is used.

---

## 4. Heuristics, and exactly what they do and do not say about BSD

**[HEURISTIC] Poonen–Rains [PR12].** Model $\operatorname{Sel}_p(E)$ as the intersection of two random maximal isotropic subspaces of a $2n$-dimensional quadratic space over $\mathbb{F}_p$, $n\to\infty$. Predictions: $\operatorname{Prob}(\dim_{\mathbb{F}_p}\operatorname{Sel}_p=d)=\prod_{j\ge0}(1+p^{-j})^{-1}\prod_{j=1}^d\frac{p}{p^j-1}$; average $\#\operatorname{Sel}_p=p+1$ (proved for $p\le5$ by Bhargava–Shankar); $\dim\operatorname{Sel}_p$ even/odd each with probability $1/2$.

**[HEURISTIC] Bhargava–Kane–Lenstra–Poonen–Rains [BKLPR15].** A model for $\operatorname{Sel}_{p^\infty}$, $\operatorname{rank}$ and $\operatorname{Sha}[p^\infty]$ jointly (cokernel of a random alternating matrix): rank $0$ and $1$ each with probability $1/2$, rank $\ge2$ with probability $0$; conditional on the rank, $\operatorname{Sha}[p^\infty]$ distributed as in Delaunay's heuristics.

**[HEURISTIC] Park–Poonen–Voight–Wood [PPVW19, Thm. 1.1.1].** Modelling $E$ of height $H$ by a random alternating integer matrix of size $\approx H^{1/12}$ with entries bounded by $H^{1/12}$: with probability $1$, all but finitely many $E$ have $\operatorname{rank}\le 21$, and $\#\{E:\operatorname{ht}E\le H,\ \operatorname{rank}\ge r\}=H^{(21-r)/24+o(1)}$ for $1\le r\le 20$. (They note the model may fail on special families.) The current record is a curve of rank $\ge 29$ (Elkies–Klagsbrun, announced Aug. 2024; rank exactly $29$ under GRH; [unverified primary source: NMBRTHRY listserv; secondary: MathOverflow 477849, Dujella's tables]).

**[THEOREM/CONDITIONAL] Analytic-rank bounds.** Mestre [Mes86]: for a newform of weight $k$ and level $N$, the order $r$ of $L$ at the centre satisfies $r\ll\log(k^2N)$ unconditionally (explicit formula + functional equation), and $r=O(\log N/\log\log N)$ under GRH; applied to $E/\mathbb{Q}$ (modularity), $r_{\mathrm{an}}(E)\ll\log N$ and, under GRH, $r_{\mathrm{an}}(E)=O(\log N/\log\log N)$. Averages under GRH: Brumer [Bru92] $\le 2.3$; Heath-Brown [HB04] $\le 2$ (and the proportion with $r_{\mathrm{an}}\ge R$ decays faster than exponentially in $R$); Young [Young06] $\le 25/14$. Unconditional algebraic averages: Bhargava–Shankar, average rank $<1$ via $5$-Selmer; Bhargava–Skinner–Zhang [BSZ14]: $\ge 66.48\%$ of $E/\mathbb{Q}$ (by height) satisfy BSD (rank), all of them with rank $\le1$; and *if* the average size of $\operatorname{Sel}_p$ is $p+1$ for all $p$, BSD (rank) holds for $100\%$. (We could not verify a separate Oesterlé rank bound; "Mestre–Oesterlé" in the brief presumably refers to the explicit-formula method of [Mes86]. [unverified])

**What they say about BSD.**
1. All three heuristic models are models of the *arithmetic* side only ($\operatorname{Sel}$, $\operatorname{rank}$, $\operatorname{Sha}$); $L$-functions do not enter. They cannot bear on BSD (rank) except through *consistency*: the analytic "minimalist" prediction ($r_{\mathrm{an}}\in\{0,1\}$ for $100\%$; Goldfeld [Gol79] for twist families, Katz–Sarnak [KS99] for orthogonal symmetry; Heath-Brown's decay) matches the algebraic prediction. Consistency between two heuristics is not evidence for an identity between the two quantities on the exceptional set.
2. They predict that curves with $r\ge2$ have **density zero** (and $r\ge r_0$ has density $H^{-(r_0-1)/24}$). Consequently *every statistical theorem about BSD, present or future, is silent on rank $\ge2$*: [BSZ14]'s $66.48\%$, and even a proof of BSD (rank) for $100\%$ of curves, would not include a single rank-$2$ curve.
3. The GRH bounds concern $r_{\mathrm{an}}$; through BSD they would bound $r_{\mathrm{alg}}$ by $O(\log N/\log\log N)$, and conversely a curve with $r_{\mathrm{alg}}>C\log N/\log\log N$ would refute BSD or GRH. Known high-rank curves are consistent (Mestre's tables; the rank-29 curve has $r_{\mathrm{an}}\le29$ under GRH, hence $=29$ under GRH+BSD). This is a *consistency test with no known failure*, not evidence of the equality $r_{\mathrm{alg}}=r_{\mathrm{an}}$.
4. PPVW's boundedness prediction, if true, would make BSD (rank) a statement about finitely many "rank levels", but says nothing about how to prove it at any level $\ge 2$; the BKLPR/Delaunay predictions for $\operatorname{Sha}$ in rank $r$ do give the expected *size* of the object whose finiteness is the problem of §3, and predict that $\operatorname{Sha}[p]=0$ for a positive proportion of $(E,p)$ in each rank, consistent with [SW13, Thm. 1.1].

Detailed treatment: `approaches/E`, `approaches/F`.

---

## 5. What would suffice: a layered list, with proofs of the implications

Each layer is a statement about all $E/\mathbb{Q}$ (or a specified class) which implies BSD (rank) for that class, with the proof of the implication from known theorems. Layers decrease in strength.

**Layer 0.** BSD (leading term) for $E$ $\Rightarrow$ BSD (rank) for $E$. *Trivial.*

**Layer 1 (Selmer-rank BSD at one prime, plus $p$-primary finiteness).** For each $E$ there is a prime $p$ with
$$
\operatorname{corank}_{\mathbb{Z}_p}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r_{\mathrm{an}}\quad\text{and}\quad\operatorname{Sha}(E/\mathbb{Q})[p^\infty]\text{ finite}.
$$
*Proof of $\Rightarrow$ BSD (rank).* $\operatorname{corank}\operatorname{Sel}=r_{\mathrm{alg}}+\operatorname{corank}\operatorname{Sha}[p^\infty]=r_{\mathrm{alg}}$. $\square$ Conversely BSD (rank) for $E$ plus finiteness of $\operatorname{Sha}[p^\infty]$ gives Layer 1 at $p$. **Without** the finiteness clause, "$\operatorname{corank}\operatorname{Sel}_{p^\infty}=r_{\mathrm{an}}$ at one $p$" gives only $r_{\mathrm{alg}}\le r_{\mathrm{an}}$.

**Layer 2 (one $p$-adic transfer).** For each $E$ there is a good ordinary odd prime $p$ with $r_p=r_{\mathrm{an}}$ [$\mathrm{T}(E,p)$].
*What it gives.* By Prop. 1.2: $r_{\mathrm{alg}}\le\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\le r_p=r_{\mathrm{an}}$ — **one inequality**, (U).
*What is needed for the other.* Either (i) $r_{\mathrm{alg}}\ge r_{\mathrm{an}}$ directly (point construction, no method known for $r_{\mathrm{an}}\ge2$), or (ii) $\operatorname{corank}\operatorname{Sel}=r_{\mathrm{an}}$ **and** $\operatorname{Sha}[p^\infty]$ finite. For (ii):

**[NEW] Proposition 5.1 (what Layer 2 needs, exactly).** Let $p>2$ be good ordinary with $E[p]$ irreducible (so the rational main conjecture holds, [BCGS, Thm. 3.2.6(ii)]), and assume $r_p=r_{\mathrm{an}}$. Then:
1. $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r_{\mathrm{an}}$ $\iff$ $X_\infty\otimes\mathbb{Q}_p$ is semisimple at $T=0$ (no elementary divisor divisible by $T^2$) $\iff$ (Perrin-Riou [PR92]) the cyclotomic $p$-adic height pairing on $H^1_f(\mathbb{Q},V)$ is non-degenerate.
2. If moreover $\operatorname{Sha}[p^\infty]$ is finite: $r_{\mathrm{alg}}=r_{\mathrm{an}}$ $\iff$ the $p$-adic height pairing on $E(\mathbb{Q})$ is non-degenerate (Schneider's conjecture at $p$).
3. If $r_{\mathrm{alg}}\ge r_{\mathrm{an}}$ is known (e.g. by exhibiting points), then $r_{\mathrm{alg}}=r_{\mathrm{an}}$, $\operatorname{Sha}[p^\infty]$ is finite, and the height is non-degenerate.

*Proof.* Rational main conjecture: $\operatorname{ord}_{T=0}f_E=r_p=r_{\mathrm{an}}$. (1) By the proof of Prop. 1.2, $\operatorname{corank}\operatorname{Sel}=\#\{i:T\mid f_i\}$ and $\operatorname{ord}_{T=0}f_E=\sum_i\operatorname{ord}_T f_i$; equality iff each $f_i$ with $T\mid f_i$ has $\operatorname{ord}_T f_i=1$, i.e. semisimplicity. The equivalence with non-degeneracy of the height on $H^1_f(\mathbb{Q},V)$ is Perrin-Riou's theorem [PR92] (in [SW13, Thm. 6.1] the statement is given for $E(\mathbb{Q})$ under finiteness of $\operatorname{Sha}[p^\infty]$; the exact form of [PR92]'s general statement was not re-verified from the source; the derived-height refinement of Bertolini–Darmon [BD95] expresses $\operatorname{ord}_{T=0}f_E$ through the dimensions of the graded pieces of the derived-height filtration, so that equality with $\dim H^1_f(\mathbb{Q},V)$ holds iff the first height is already non-degenerate). (2) With $\operatorname{Sha}[p^\infty]$ finite, $H^1_f(\mathbb{Q},V)=E(\mathbb{Q})\otimes\mathbb{Q}_p$ and $\operatorname{corank}\operatorname{Sel}=r_{\mathrm{alg}}$; apply (1), or directly [SW13, Thm. 6.1]. (3) Prop. 1.2 with $r_{\mathrm{alg}}\ge r_{\mathrm{an}}=r_p$ forces equalities throughout; conclude by [SW13, Thm. 6.1]. $\square$

Thus **Layer 2 alone yields (U); the missing half (L) is again either a point construction or [finiteness of $\operatorname{Sha}[p^\infty]$ + Schneider at $p$]**. Note that Schneider's conjecture is *implied* by Layer 2 + BSD (rank) + finiteness (by (2)), so it is not an extra assumption beyond BSD; but no route to it is known that does not pass through BSD.

**Layer 3 (Selmer lower bound).** For each $E$ there is a good ordinary odd prime $p$ with $E[p]$ irreducible and $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\ge r_{\mathrm{an}}$.
*What it gives.* Combined with Layer 2 at the same $p$: $\operatorname{corank}\operatorname{Sel}=r_{\mathrm{an}}$, hence Layer 1 up to finiteness of $\operatorname{Sha}[p^\infty]$. Known: $r_{\mathrm{an}}\le1$ (Lemma 1.3), $r_{\mathrm{an}}$ even (rational main conjecture + parity: $L(E,1)=0\Rightarrow\operatorname{corank}\ge1\Rightarrow\ge2$ — but *not* $\ge r_{\mathrm{an}}$ for $r_{\mathrm{an}}\ge4$). The case $r_{\mathrm{an}}=3$ is now proved for non-CM curves at good ordinary $p\ge5$ with irreducible residual representation; see the odd-rank bridge. For higher odd analytic rank it proves only the lower bound three. O5 is the next odd-rank obligation.

**Layer 4 (the Kolyvagin layer for $r_{\mathrm{an}}=2$).** For each $E$ with $r_{\mathrm{an}}=2$ and $K$ with $r_{\mathrm{an}}(E^K)=1$ there is $p$ as in Prop. 2.2 with $\operatorname{ord}(\kappa^{\mathrm{Heeg}})=1$.
*What it gives.* $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=2$ (Prop. 2.2), i.e. Layer 1 up to finiteness of $\operatorname{Sha}[p^\infty]$; for a curve with two known independent points, BSD (rank) and finiteness of $\operatorname{Sha}[p^\infty]$.

**Layer 5 (the Kurihara–Mazur–Tate layer).** For each non-CM $E$ there is $p\ge5$ good ordinary with $\bar\rho_{E,p}$ surjective, Manin constant prime to $p$, and
$$
\tilde\delta_n=0\ \text{ in }\mathbb{Z}_p/I_n\ \text{ for all }n\in\mathcal{N}^{\mathrm{cyc}}_1\text{ with }\nu(n)<r_{\mathrm{an}},\qquad\tilde\delta_n\ne0\ \text{ for some }n\text{ with }\nu(n)=r_{\mathrm{an}}.
$$
*What it gives.* $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r_{\mathrm{an}}$ by [Kim24, Thm. 3.1(1)]; again Layer 1 up to finiteness of $\operatorname{Sha}[p^\infty]$. This layer is a statement *purely about modular symbols and $\operatorname{ord}_{s=1}L(E,s)$*; its first half for $\nu(n)=1$ is the congruence of Cor. 2.4. It is the most "analytic" reformulation of Selmer-rank BSD available, and it is exactly the Mazur–Tate refined conjecture [MT87] (order-of-vanishing part, with $r_{\mathrm{alg}}$ replaced by $r_{\mathrm{an}}$) together with its non-degeneracy part at level $\nu(n)=r_{\mathrm{an}}$.

**Layer 6 (finiteness of $\operatorname{Sha}[p^\infty]$ at one $p$ for curves with known points).** For each $E$ with $r_{\mathrm{an}}\ge2$ and $r_{\mathrm{alg}}\ge r_{\mathrm{an}}$ known, there is a good ordinary $p$ with $\operatorname{Sha}[p^\infty]$ finite and $\operatorname{corank}\operatorname{Sel}_{p^\infty}\le r_{\mathrm{an}}$. *What it gives.* $r_{\mathrm{alg}}=\operatorname{corank}\operatorname{Sel}\le r_{\mathrm{an}}\le r_{\mathrm{alg}}$. This is the form in which BSD (rank) is *verified* for individual curves such as $389a1$ (Prop. 3.1 with $p=5$, say), and it shows that for individual curves the *rank* statement is not the obstruction — finiteness of $\operatorname{Sha}$ at *all* $p$ is.

**Summary of the logical structure.** Writing $\mathrm{Sel}(p)$ for "$\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=r_{\mathrm{an}}$" and $\mathrm{Fin}(p)$ for "$\operatorname{Sha}[p^\infty]$ finite":
$$
\big[\forall p:\ \mathrm{Sel}(p)\wedge\mathrm{Fin}(p)\big]\Rightarrow\big[\exists p:\ \mathrm{Sel}(p)\wedge\mathrm{Fin}(p)\big]\Rightarrow\text{BSD(rank) for }E;
$$
Neither reverse implication is established by rank equality alone. Under the rational main conjecture, $[\text{Layer 2 at }p]\wedge[\text{Perrin-Riou non-degeneracy at }p]\Rightarrow\mathrm{Sel}(p)$, and given $\mathrm{Sel}(p)$, Layer 2 at $p$ holds iff Perrin-Riou non-degeneracy holds at $p$ (Prop. 5.1(1)); $\mathrm{Sel}(p)\iff$ [Layer 4 at $p$] (for $r_{\mathrm{an}}=2$, Prop. 2.2) $\iff$ [Layer 5 at $p$] ([Kim24, Thm. 3.1]); and $\mathrm{Fin}(p)$ has **no** known reformulation in terms of $L$-values other than through $\mathrm{Sel}(p)\wedge(r_{\mathrm{alg}}\ge r_{\mathrm{an}})$.

---

## 6. The gaps, and what an attempt on each achieved

**[GAP 1] Schneider non-degeneracy, rank 1.** *Attempt.* (a) Reformulations established: $\langle P,P\rangle_p\ne0\iff r_p=1\iff$ the zero of $f_E$ at $T=0$ is simple (under the rational main conjecture) $\iff L_p'(E,0)\ne0$; and, granting the Rubin-style formula of Perrin-Riou/Nekovář in the form described in [BDV22, §1.3] (exact statement not re-verified here), $\iff\langle\zeta^{\mathrm{Kato}}_E,P\rangle_p\ne0$. (b) Observed that for the purposes of BSD in rank $1$ the gap is *avoidable* (anticyclotomic route; $\log_\omega$ is injective on non-torsion points), whereas for $\mathrm{T}(E,p)$ it is *essential*; and that in rank $2$ its analogue is the non-degeneracy of the *derived* anticyclotomic height $h^{(\rho)}(P,Q)$ in [CH22] — which Castella–Hsieh prove is non-zero in their setting, so that in rank $2$ the anticyclotomic side *does* avoid the degeneracy; what is missing there is the complex partner of $\bar\theta_{f/K}$, not a non-degeneracy. (c) No progress on the statement itself; no non-CM case at infinitely many $p$ located in the literature.

**[THEOREM: resolution of former GAP 2 / GAP 5 in the ordinary irreducible range].**
The [new deduction](synthesis/odd-rank-selmer-bridge.md) combines an auxiliary
analytic-rank-zero twist, BCGS nonvanishing and its corank formula, and
$p$-parity. It proves $s_p\ge3$, hence $r_p\ge3$, in odd analytic rank at
least three. Kim then supplies full-modulus low-index Kurihara vanishing.
The previous attempt recorded here overlooked the rank-one converse route.
The deduction does not produce rational points or an upper bound on $s_p$.

**[GAP 3] $\mathrm{T}(E,p)$, upper half.** *Attempt.* Shown equivalent to [BSD rank] $\wedge$ [$\operatorname{Sha}[p^\infty]$ finite] $\wedge$ [Schneider at $p$] under the rational main conjecture (Prop. 5.1). Hence strictly stronger than BSD (rank) for $E$; no independent approach.

**[GAP 4] Higher Gross–Zagier over $\mathbb{Q}$.** *Attempt.* (a) Triple products: Prop. 2.1 shows $\operatorname{ord}_{s=2}L(E^{\otimes3},s)\ge2r_{\mathrm{an}}$, so the Gross–Kudla–Schoen cycle is (conjecturally) torsion exactly when $E$ has rank, and even a higher-derivative formula would only give $(L^{(r)}(E,1))^2\times(\operatorname{Sym}^3\text{-value})$; the relevant Chow classes are $E(\mathbb{Q})\otimes\mathrm{NS}(E^2)$, i.e. the points themselves. (b) Rankin–Selberg $L(E\otimes g,s)$ with $g$ of weight $1$ (Darmon–Rotger): produces the only known canonical rank-$2$ object $\kappa_{\alpha,\alpha^{-1}}$, but its analytic partner is $p$-adic anticyclotomic [CH22]; identifying $\bar\theta_{f/K}$ with $L''(E,1)$ would be a $p$-adic-to-complex transfer of Bridge (i) type in the anticyclotomic direction, for which no formula (even conjectural, beyond [CHKLL25]'s $p$-adic BSD for $L^{\mathrm{BDP}}$) exists. (c) Function fields: Yun–Zhang's cycle lives on $\mathrm{Sht}^r_G$, which has no number-field analogue for $r\ge2$. Outcome: the three natural candidates are excluded for identifiable structural reasons; the problem is genuinely one of *finding a new canonical object*.

**[GAP 6] $\operatorname{ord}(\kappa^{\mathrm{Heeg}})=1$ for rank-2 curves.** *Attempt.* Prop. 2.2 reduces it exactly to $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=2$ and shows $\nu_\infty$ is odd, so the first *possible* failure is $\nu_\infty=3$, i.e. $\operatorname{corank}\operatorname{Sel}=4$. The level-raising reformulation ($\operatorname{loc}_\ell\kappa^{\mathrm{Heeg}}_\ell\leftrightarrow L^{\mathrm{alg}}(g_\ell/K,1)\bmod p$ for $g_\ell\equiv f_E$ of level $N\ell$; [BD05], [Zha14]) turns "$\nu_\infty=1$" into: *some* mod-$p$ level-raising of $f_E$ at a Kolyvagin prime has $p$-indivisible central $L$-value over $K$. Zhang's proof of Kolyvagin's conjecture proceeds by induction on the (mod $p$) Selmer rank, lowering it by level raising until the rank-$0$ case, which is handled by the integral main conjecture ([Zha14, §1], [BCGS, §0.2]); *the method proves $\nu_\infty<\infty$ without producing the value of $\nu_\infty$* — controlling it would amount to knowing the Selmer rank at the outset, i.e. Layer 3. Outcome: reduction to Layer 3, no independent progress. Full analysis in `approaches/B`.

**[GAP 7] Uniformity $\mathrm{U}(E)$.** *Attempt.* Prop. 3.3 shows $\mathrm{U}(E)$ (with a rational constant) implies $\operatorname{Sha}[p^\infty]=0$ for almost all $p$ under the integral main conjecture, and that $\mathrm{U}(E)$ is a consequence of BSD + $p$-adic BSD. Searched for any $p$-independent object: none (Lemma 3.2 and §3.3). Outcome: "all $p$ at once" is precisely $\mathrm{U}(E)$; the Iwasawa-theoretic route cannot produce a rational constant, and the Heegner route produces one only when $\kappa_1^{\mathrm{Heeg}}\ne0$.

---

## 7. Developments 2020–2026 the team must know (verified sources)

1. **Kolyvagin's conjecture is a theorem in wide generality**: Zhang [Zha14] ($p\ge5$, $\bar\rho$ surjective, ramification hypotheses), Sweeting [Swe] (relaxed hypotheses, patched bipartite Euler systems, $p=3$ and dihedral images), Burungale–Castella–Grossi–Skinner [BCGS, Thm. A] ($p$ odd good ordinary split in $K$, given the rational anticyclotomic main conjecture — known for $p>3$ with $E[p]$ irreducible [BCS25] and in Eisenstein cases [CGS25]); refined version $\mathscr{M}_\infty=\sum_{\ell\mid N}\operatorname{ord}_pc_\ell$ [BCGS, Thm. B]; the *Kato* Kolyvagin system is also non-zero [BCGS, Thm. C], with $\operatorname{ord}(\kappa^{\mathrm{Kato}})=r_{\mathrm{str}}$ [BCGS, Cor. C]. Consequence for us: **Bridge (iii) is now a clean equality $\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})=\operatorname{ord}(\kappa^{\mathrm{Heeg}})+1$ in rank 2 (Prop. 2.2)**, with no remaining non-vanishing hypothesis.
2. **Cyclotomic main conjecture without the Skinner–Urban ramification hypothesis**: rational version for $p>2$ good ordinary with $E[p]$ irreducible ([Wan15]; collected in [BCGS, Thm. 3.2.6]); Eisenstein primes [CGS25]; base-change methods [BCS25].
3. **Structure of Selmer groups from modular symbols in arbitrary rank**: Kim [Kim25], [Kim24, Thm. 3.1] ($\operatorname{corank}\operatorname{Sel}=\operatorname{ord}\tilde{\boldsymbol\delta}$) and the higher Gross–Zagier formula [Kim24, Thm. 2.3]; Kurihara–Sakamoto [KS25] (rank-$0$ Euler/Kolyvagin systems; cited in [BCGS], not independently located).
4. **Perrin-Riou's conjecture is a theorem** [BDV22], [BPS] (and Burungale–Skinner–Tian, independently); consequence Prop. 1.1.
5. **Rank-2 generalised Kato classes**: [DR16] conjecture; [CH22] first cases and the formula $\kappa=\bar\theta/h^{(\rho)}\cdot(P\otimes\log Q-Q\otimes\log P)$; [CHKLL25] $p$-adic BSD for $L^{\mathrm{BDP}}$ with derived heights.
6. **No change** in the status of: finiteness of $\operatorname{Sha}$ for any rank-$\ge2$ curve; $\mathrm{T}(E,p)$ for $r_{\mathrm{an}}\ge1$ non-CM (still reduced to height non-degeneracy); any higher-derivative formula over number fields.

---

## 8. Verification log (what was searched and fetched)

* arXiv export API (`export.arxiv.org/api/query`) by id and title for: 1407.1099 (turned out to be Skinner–Zhang, *not* Zhang's CJM paper — corrected via CJM/MathSciNet pages), 1405.7294, 1811.08216, 1009.0287, 1304.3971, 1602.01431, 1512.02683, 1712.08026, 2012.11771, 1407.1913, 2203.12161, 2203.12159, 1407.2465, 1510.02114, 1907.13040, 1908.09512, math/0610290, 1408.4043, 2405.00270, 2303.04373, 2008.02571, 1512.06894, 2001.03878, 2506.03465, 2312.09301, 1809.09066, 1405.2643, 1609.02528, 1407.1826, 2003.00077.
* Full texts read (HTML/PDF-to-text): [BCGS] v2 (Jan 2026), [SW13] (author PDF), [BDV22] (author PDF), [Zha14] (author PDF), [Kur14] (ar5iv), [Kim24] (arXiv HTML), [CH22] (arXiv text), [Ski20] (Annals PDF), [Mes86] (Numdam), [PPVW19] (author PDF), [GS93] (author PDF), [Dis20] (journal text), [Buy] (arXiv text), Bertolini–Darmon survey (McGill PDF), [YZ17] (Annals PDF).
* Journal/DOI pages fetched: CJM (Zhang 2014), Annals (Skinner 2020; Yun–Zhang 2017, 2019; Bertolini–Darmon 2005; Dokchitser–Dokchitser 2010), Adv. Math. (BDV), Forum Math. Sigma (Castella–Hsieh), JEMS/MathSciNet (PPVW), Compositio/Numdam (Gross–Kudla; Mestre), Ann. Inst. Fourier (Gross–Schoen), Duke (Mazur–Tate), Inventiones/EuDML (Perrin-Riou 1987, 1992; Brumer; Kobayashi; BFH; Nekovář 2001 via CRAS), Bull. AMS (Katz–Sarnak; Goldfeld reference), LMFDB 389.a1.
* Not independently verified (marked in text): theorem numbers in [Kat04] (14.2, 16.6) and [Rub00] (2.2.2); §I.17 of [MTT86]; journal data of [BCGS] (reported: Camb. J. Math. 14 (2026)); [BST]; [KS25]; a separate "Oesterlé" rank bound; the NMBRTHRY primary source for the rank-29 curve; page ranges of [HB04], [Young06].

---

## References (verified unless marked)

* [BCGS] A. Burungale, F. Castella, G. Grossi, C. Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory*, arXiv:2312.09301 (v2, 2026); reported Camb. J. Math. 14 (2026) [journal data unverified].
* [BCS25] A. Burungale, F. Castella, C. Skinner, *Base change and Iwasawa main conjectures for $\mathrm{GL}_2$*, Int. Math. Res. Not. IMRN 2025, no. 8, rnaf082; arXiv:2405.00270.
* [BCK21] A. Burungale, F. Castella, C.-H. Kim, *A proof of Perrin-Riou's Heegner point main conjecture*, Algebra Number Theory 15 (2021) 1627–1653; arXiv:1908.09512.
* [BD90] M. Bertolini, H. Darmon, *Kolyvagin's descent and Mordell–Weil groups over ring class fields*, J. reine angew. Math. 412 (1990) 63–74.
* [BD95] M. Bertolini, H. Darmon, *Derived $p$-adic heights*, Amer. J. Math. 117 (1995) 1517–1554.
* [BD07] M. Bertolini, H. Darmon, *Hida families and rational points on elliptic curves*, Invent. Math. 168 (2007) [pages unverified; cited via BDV22 as the key input to Ven16].
* [BD05] M. Bertolini, H. Darmon, *Iwasawa's main conjecture for elliptic curves over anticyclotomic $\mathbb{Z}_p$-extensions*, Ann. of Math. (2) 162 (2005), no. 1.
* [BDP13] M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles and $p$-adic Rankin $L$-series*, Duke Math. J. 162 (2013) 1033–1148.
* [BDV22] M. Bertolini, H. Darmon, R. Venerucci, *Heegner points and Beilinson–Kato elements: a conjecture of Perrin-Riou*, Adv. Math. 398 (2022) 108172, DOI 10.1016/j.aim.2021.108172.
* [Bei87] A. Beilinson, *Height pairing between algebraic cycles*, in K-theory, Arithmetic and Geometry (Moscow 1984–86), LNM 1289 (1987) 1–25.
* [Ber82] D. Bertrand, *Valeurs de fonctions thêta et hauteurs $p$-adiques*, Sém. Théorie des Nombres Paris 1980–81, Progr. Math. 22, Birkhäuser (1982) 1–11.
* [BFH90] D. Bump, S. Friedberg, J. Hoffstein, *Nonvanishing theorems for $L$-functions of modular forms and their derivatives*, Invent. Math. 102 (1990) 543–618.
* [BKLPR15] M. Bhargava, D. Kane, H. Lenstra, B. Poonen, E. Rains, *Modeling the distribution of ranks, Selmer groups, and Shafarevich–Tate groups of elliptic curves*, Camb. J. Math. 3 (2015) 275–321; arXiv:1304.3971.
* [Blo84] S. Bloch, *Height pairings for algebraic cycles*, J. Pure Appl. Algebra 34 (1984) 119–145.
* [BPS] K. Büyükboduk, R. Pollack, S. Sasaki, *$p$-adic Gross–Zagier formula at critical slope and a conjecture of Perrin-Riou*, arXiv:1811.08216.
* [Bru92] A. Brumer, *The average rank of elliptic curves I*, Invent. Math. 109 (1992) 445–472.
* [BSDGP96] K. Barré-Sirieix, G. Diaz, F. Gramain, G. Philibert, *Une preuve de la conjecture de Mahler–Manin*, Invent. Math. 124 (1996) 1–9.
* [BSZ14] M. Bhargava, C. Skinner, W. Zhang, *A majority of elliptic curves over $\mathbb{Q}$ satisfy the Birch and Swinnerton-Dyer conjecture*, arXiv:1407.1826.
* [Buy] K. Büyükboduk, *On Nekovář's heights, exceptional zeros and a conjecture of Mazur–Tate–Teitelbaum*, arXiv:1405.2643.
* [CGLS22] F. Castella, G. Grossi, J. Lee, C. Skinner, *On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes*, Invent. Math. 227 (2022) 517–580; arXiv:2008.02571.
* [CGS25] F. Castella, G. Grossi, C. Skinner, *Mazur's main conjecture at Eisenstein primes*, Math. Ann. 393 (2025) 2451–2506; arXiv:2303.04373.
* [CH22] F. Castella, M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum Math. Sigma 10 (2022) e12, DOI 10.1017/fms.2021.85; arXiv:1809.09066.
* [CHKLL25] F. Castella, C.-Y. Hsu, D. Kundu, Y. Lee, Z. Liu, *Derived $p$-adic heights and the leading coefficient of the Bertolini–Darmon–Prasanna $p$-adic $L$-function*, Trans. Amer. Math. Soc. Ser. B (2025) [details from abstract page only].
* [DD10] T. Dokchitser, V. Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, Ann. of Math. (2) 172 (2010) 567–596; arXiv:math/0610290.
* [Dis17] D. Disegni, *The $p$-adic Gross–Zagier formula on Shimura curves*, Compos. Math. 153 (2017) 1987–2074; arXiv:1510.02114.
* [Dis20] D. Disegni, *On the $p$-adic Birch and Swinnerton-Dyer conjecture for elliptic curves over number fields*, Kyoto J. Math. (2020), DOI 10.1215/21562261-2018-0012; arXiv:1609.02528.
* [DR16] H. Darmon, V. Rotger, *Elliptic curves of rank two and generalised Kato classes*, Res. Math. Sci. 3 (2016), 27, DOI 10.1186/s40687-016-0074-9.
* [GJPST09] G. Grigorov, A. Jorza, S. Patrikis, C. Tarniţă, W. Stein, *Computational verification of the Birch and Swinnerton-Dyer conjecture for individual elliptic curves*, Math. Comp. 78 (2009) 2397–2425.
* [GK92] B. Gross, S. Kudla, *Heights and the central critical values of triple product $L$-functions*, Compos. Math. 81 (1992) 143–209.
* [Gol79] D. Goldfeld, *Conjectures on elliptic curves over quadratic fields*, LNM 751 (1979) 108–118.
* [Gre99] R. Greenberg, *Iwasawa theory for elliptic curves*, LNM 1716 (1999) 51–144.
* [Gro91] B. Gross, *Kolyvagin's work on modular elliptic curves*, in L-functions and Arithmetic (Durham 1989), LMS LNS 153 (1991) 235–256.
* [GS93] R. Greenberg, G. Stevens, *$p$-adic $L$-functions and $p$-adic periods of modular forms*, Invent. Math. 111 (1993) 407–447.
* [GS95] B. Gross, C. Schoen, *The modified diagonal cycle on the triple product of a pointed curve*, Ann. Inst. Fourier 45 (1995) 649–679.
* [GZ86] B. Gross, D. Zagier, *Heegner points and derivatives of $L$-series*, Invent. Math. 84 (1986) 225–320.
* [HB04] D. R. Heath-Brown, *The average analytic rank of elliptic curves*, Duke Math. J. 122 (2004); arXiv:math/0305114.
* [How04] B. Howard, *The Heegner point Kolyvagin system*, Compos. Math. 140 (2004) 1439–1472.
* [How04-derived] B. Howard, *Derived $p$-adic heights and $p$-adic $L$-functions*, Amer. J. Math. 126 (2004) [pages unverified].
* [JSW17] D. Jetchev, C. Skinner, X. Wan, *The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one*, Camb. J. Math. 5 (2017) 369–434.
* [Kat04] K. Kato, *$p$-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004) 117–290.
* [Kim24] C.-H. Kim, *A higher Gross–Zagier formula and the structure of Selmer groups*, Trans. Amer. Math. Soc. 377 (2024) 3691–3725; arXiv:2203.12161.
* [Kim25] C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, arXiv:2203.12159.
* [Kim-soft] C.-H. Kim, *On the soft $p$-converse to a theorem of Gross–Zagier and Kolyvagin*, arXiv:2109.12344.
* [Kob13] S. Kobayashi, *The $p$-adic Gross–Zagier formula for elliptic curves at supersingular primes*, Invent. Math. 191 (2013) 527–629.
* [Kol90] V. Kolyvagin, *Euler systems*, The Grothendieck Festschrift II, Progr. Math. 87 (1990) 435–483.
* [Kol91] V. Kolyvagin, *On the structure of Selmer groups*, Math. Ann. 291 (1991) 253–259.
* [KS99] N. Katz, P. Sarnak, *Zeroes of zeta functions and symmetry*, Bull. Amer. Math. Soc. 36 (1999) 1–26.
* [KS02] H. Kim, F. Shahidi, *Functorial products for $\mathrm{GL}_2\times\mathrm{GL}_3$ and the symmetric cube for $\mathrm{GL}_2$*, Ann. of Math. (2) 155 (2002) [pages unverified].
* [KS25] M. Kurihara, R. Sakamoto, *Euler and Kolyvagin systems of rank 0 and the structure of Selmer groups*, preprint 2025 [cited in BCGS; not located].
* [Kur14] M. Kurihara, *The structure of Selmer groups of elliptic curves and modular symbols*, in Iwasawa Theory 2012, Contrib. Math. Comput. Sci. 7, Springer (2014) 317–356; arXiv:1407.2465.
* [LMFDB] The LMFDB Collaboration, elliptic curve 389.a1, https://www.lmfdb.org/EllipticCurve/Q/389/a/1 (accessed 2026-09-11).
* [Maz72] B. Mazur, *Rational points of abelian varieties with values in towers of number fields*, Invent. Math. 18 (1972) 183–266.
* [Mes86] J.-F. Mestre, *Formules explicites et minorations de conducteurs de variétés algébriques*, Compos. Math. 58 (1986) 209–232.
* [MM91] M. R. Murty, V. K. Murty, *Mean values of derivatives of modular $L$-series*, Ann. of Math. 133 (1991) 447–475.
* [MR04] B. Mazur, K. Rubin, *Kolyvagin systems*, Mem. Amer. Math. Soc. 168 (2004), no. 799.
* [MT87] B. Mazur, J. Tate, *Refined conjectures of the "Birch and Swinnerton-Dyer type"*, Duke Math. J. 54 (1987) 711–750.
* [MTT86] B. Mazur, J. Tate, J. Teitelbaum, *On $p$-adic analogues of the conjectures of Birch and Swinnerton-Dyer*, Invent. Math. 84 (1986) 1–48.
* [Nek01] J. Nekovář, *On the parity of ranks of Selmer groups II*, C. R. Acad. Sci. Paris Sér. I 332 (2001) 99–104.
* [Nek06] J. Nekovář, *Selmer complexes*, Astérisque 310 (2006) [cited via BDV22].
* [PPVW19] J. Park, B. Poonen, J. Voight, M. M. Wood, *A heuristic for boundedness of ranks of elliptic curves*, J. Eur. Math. Soc. 21 (2019) 2859–2903; arXiv:1602.01431.
* [PR87] B. Perrin-Riou, *Points de Heegner et dérivées de fonctions $L$ $p$-adiques*, Invent. Math. 89 (1987) 455–510.
* [PR92] B. Perrin-Riou, *Théorie d'Iwasawa et hauteurs $p$-adiques*, Invent. Math. 109 (1992) 137–185.
* [PR93] B. Perrin-Riou, *Fonctions $L$ $p$-adiques d'une courbe elliptique et points rationnels*, Ann. Inst. Fourier 43 (1993) 945–995.
* [PR03] B. Perrin-Riou, *Arithmétique des courbes elliptiques à réduction supersingulière en $p$*, Experiment. Math. 12 (2003) 155–186.
* [PR12] B. Poonen, E. Rains, *Random maximal isotropic subspaces and Selmer groups*, J. Amer. Math. Soc. 25 (2012) 245–269; arXiv:1009.0287.
* [Roh84] D. Rohrlich, *On $L$-functions of elliptic curves and cyclotomic towers*, Invent. Math. 75 (1984) 409–423.
* [Rub00] K. Rubin, *Euler Systems*, Ann. of Math. Studies 147, Princeton Univ. Press (2000).
* [Rub92] K. Rubin, *$p$-adic $L$-functions and rational points on elliptic curves with complex multiplication*, Invent. Math. 107 (1992) [pages unverified; cited via BDV22].
* [Sch82] P. Schneider, *$p$-adic height pairings I*, Invent. Math. 69 (1982) 401–409.
* [Sch85] P. Schneider, *$p$-adic height pairings II*, Invent. Math. 79 (1985) 329–374.
* [Ser72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972) 259–331.
* [Ski20] C. Skinner, *A converse to a theorem of Gross, Zagier, and Kolyvagin*, Ann. of Math. (2) 191 (2020) 329–354; arXiv:1405.7294.
* [SU14] C. Skinner, E. Urban, *The Iwasawa main conjectures for $\mathrm{GL}_2$*, Invent. Math. 195 (2014) 1–277.
* [SW13] W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013) 1757–1792, DOI 10.1090/S0025-5718-2012-02649-4.
* [Swe] N. Sweeting, *Kolyvagin's conjecture and patched Euler systems in anticyclotomic Iwasawa theory*, arXiv:2012.11771.
* [Ven16] R. Venerucci, *Exceptional zero formulae and a conjecture of Perrin-Riou*, Invent. Math. 203 (2016) 923–972; arXiv:1407.1913.
* [Wan15] X. Wan, *The Iwasawa main conjecture for Hilbert modular forms*, Forum Math. Sigma 3 (2015) e18.
* [Wan21] X. Wan, *Heegner point Kolyvagin system and Iwasawa main conjecture*, arXiv:1408.4043.
* [Young06] M. Young, *Low-lying zeros of families of elliptic curves*, J. Amer. Math. Soc. 19 (2006) [pages unverified].
* [YZ17] Z. Yun, W. Zhang, *Shtukas and the Taylor expansion of $L$-functions*, Ann. of Math. (2) 186 (2017) 767–911; arXiv:1512.02683.
* [YZ19] Z. Yun, W. Zhang, *Shtukas and the Taylor expansion of $L$-functions (II)*, Ann. of Math. (2) 189 (2019) 393–526; arXiv:1712.08026.
* [YZZ] X. Yuan, S.-W. Zhang, W. Zhang, *Triple product $L$-series and Gross–Kudla–Schoen cycles*, preprint (author websites, versions 2012 and 2023).
* [Zha14] W. Zhang, *Selmer groups and the indivisibility of Heegner points*, Camb. J. Math. 2 (2014) 191–253, DOI 10.4310/CJM.2014.v2.n2.a2.
