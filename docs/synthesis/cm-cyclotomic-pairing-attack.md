# A specified theta-unit pairing with the cyclotomic p-unit

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: bounded construction completed; all nine sections passed
[independent review](review-cm-cyclotomic-pairing.md).
The objective remains full BSD over Q. This note constructs
an actual polarized secondary operation, computes its boundary and
tower law, and tests its CM character against the exact derivative.
No Sha-finiteness or Selmer-corank-two hypothesis is used.

## 1. Both actual inputs and the choice of tower

Keep E:y²=x³+39x, K=Q(i), and the entire good split scope and
normalizations of the reviewed [CM-derived proof](cm-derived-unit-attack.md).
Thus p≥5, p≡1 mod4, p∉S_E, f=(f₀) with f₀=39(1+i)³, and
the rational auxiliary a is the same as in that proof. Set
$$F_r=K(\mathfrak f p^r),\quad L_r=K(E[p^r]),\quad
C_r=K(\mu_{p^r}),\quad D_r=[F_r:K],\quad
\varphi_r=p^{r-1}(p-1). \tag{1}$$
Choose ζ_{r+1}^p=ζ_r, with ζ_r primitive of order p^r. The two
inputs, before an ordinary norm discards any CM direction, are
$$U_r=\Theta_a\!\left(\frac{\Omega_\infty}{f_0p^r}\right)
\in\mathcal O_{F_r}^{\times},
\qquad v_r=1-\zeta_r\in\mathcal O_{C_r}[1/p]^\times. \tag{2}$$
The first is the exact rational theta function, including its
twelfth power:
$$\Theta_a(X)=a^{-12}\Delta_E^{a^2-1}
\prod_{0\ne T\in E[a]}(x(X)-x(T))^{-6},
\qquad \Delta_E=-64\cdot39^3.
\tag{3}$$
Its norm to L_r is the previous e_r(a). The raw ray-field unit
is used here so both norm laws can be stated at every r≥1.

The exact theta distribution and global-unit property in this
multi-prime conductor are the inputs from
[Schmitt, §§2.2–2.3 and Definition 3.12](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf),
Acta Arith.171 (2015),39–66, DOI10.4064/aa171-1-4,
already audited in the predecessor. The proof below retains v_r's
p-boundary; it is not a global unit merely because log_p p=0.

## 2. Exact degrees, norms and the p-boundary

**[NEW] Proposition 2.1.** For r≥1,
$$[F_{r+1}:F_r]=p^2,\qquad
N_{F_{r+1}/F_r}U_{r+1}=U_r,\qquad
N_{F_{r+1}/F_r}v_{r+1}=v_r^p. \tag{4}$$
For every finite place w of F_r, with integral valuation ord_w,
$$\operatorname{ord}_w(v_r)=
\begin{cases}
e(w/p)/\varphi_r,&w\mid p,\\
0,&w\nmid p.
\end{cases} \tag{5}$$
Moreover
$$N_{F_r/K}v_r=p^{D_r/\varphi_r},\qquad
N_{F_r/K}U_r\in\mu_4. \tag{6}$$

*Proof.* Since K has class number one, its ray group is the
appropriate residue-unit group modulo global units. The global
units inject modulo f. In the kernel of reduction from fp^{r+1}
to fp^r the two split-prime factors are each
(1+p^rZ_p)/(1+p^{r+1}Z_p), of order p, and there is no remaining
global-unit quotient in this kernel. This proves the first degree.

The two theta norm steps multiply the torsion argument by π and
barπ respectively; their product is p. The exact distribution
relation therefore gives the second equality of (4).

K and Q(μ_{p^r}) are linearly disjoint: their possible ramification
sets are respectively {2} and {p}. Thus [C_r:K]=φ_r. The
cyclotomic action of a ray class is the norm of its residue (with
the simultaneous inverse if inverse reciprocity is used). The
kernel from level r+1 to r maps onto the order-p cyclotomic kernel:
use residues 1+p^r in one split factor and 1 in the other.
Consequently the p² conjugates of v_{r+1} over F_r consist of
each cyclotomic conjugate repeated p times. The polynomial identity
$$\prod_{j=0}^{p-1}(1-\zeta_{r+1}\zeta_1^j)=1-\zeta_r$$
proves the last equality of (4).

Finally Φ_{p^r}(1)=p. Any two conjugates 1−ζ_r^b and 1−ζ_r
are associates: their ratio is a geometric sum, and the inverse
ratio is another such sum using b⁻¹ modulo p^r. Thus the product
formula for p gives φ_r·div(v_r)=div(p), proving (5).
Norm transitivity proves the first assertion of (6); the second
follows because U_r is a global unit and Z[i]×=μ₄. ∎

Here is a weight-correct way to center the p-unit if desired:
$$w_r=v_r^{\varphi_r}/p\in\mathcal O_{F_r}^{\times},
\qquad \bar v_r=[v_r]-\varphi_r^{-1}[p]
=\varphi_r^{-1}[w_r]\in F_r^\times\otimes\mathbb Q.
\tag{7}$$
Equation (5) proves the unit assertion, rather than suppressing a
valuation. Exact norms are
$$Nw_{r+1}=w_r^{p^2},\qquad
N\bar v_{r+1}=p\bar v_r. \tag{8}$$
Thus p^{1-r}[v_r], or p^{1-r}\bar v_r, is a rational
norm-compatible p-unit, or unit, system on this ray tower. The
denominators are unbounded in p; these are not new integral unit
systems. In particular division by φ_r is not permitted modulo
p^m when r>1.

## 3. A genuine polarized secondary operation

Use the actual geometric blends of the
[mixed-extension note](cm-mixed-extension-attack.md), whose chosen
local reference block is C_v. There is no assertion C_v=H_v/2.
Translate one corner by the actual Kummer extension K_R(U_r)
and the other by K_R(v_r), with coefficient-one matrices E₁₁ and
E₂₂. The p-unit translation exists over the number field, or its
arithmetic model with p inverted; (5) records its removed boundary.

**[NEW] Proposition 3.1.** The following four-term difference of
the four actual secondary determinants has exactly the value
ℓ_v(U_r)ℓ_v(v_r):
$$\begin{aligned}
&\det(C_v+\ell_v(U_r)E_{11}+\ell_v(v_r)E_{22})\\
&\quad-\det(C_v+\ell_v(U_r)E_{11})
-\det(C_v+\ell_v(v_r)E_{22})+\det C_v\\
&=\ell_v(U_r)\ell_v(v_r).
\end{aligned} \tag{9}$$
Here ℓ_∞=log|·| and ℓ_p=log_p with log_p p=0. In particular
this operation is additive in either multiplicative input and is
independent of the unknown reference C_v.

*Proof.* A coefficient-one Kummer translation changes the prescribed
local period by +ℓ_v of its argument. This exact sign, real 2π
factor and rational frame were verified in the mixed note. Expanding
the two-by-two determinant shows that its only term involving both
translations is the product of the two displayed logarithms. No
factor 2, 4, or hidden half-frame rescaling remains in (9). ∎

This is also a secondary period of the tensor of the two actual
Kummer motives. Their graded pieces are Q,Q(1), so the product
retains a Q(2) piece. At infinity the real logarithms are obtained
using conjugate periods as in the preceding note. It is not being
identified with the ordinary regulator of a degree-two cup merely
because the two period factors multiply.

The specified averaged operation is
$$P_{r,v}(U)=\frac1{D_r}
\sum_{\sigma:F_r\hookrightarrow\overline K_v}
\ell_v(\sigma U)\ell_v(\sigma v_r), \tag{10}$$
where embeddings extend one fixed embedding of K. At p this
includes all factors of the semilocal algebra F_r⊗_K K_v.
By (6), the mean theta logarithm is zero. Thus replacing v_r
by the explicit centered class in (7) leaves (10) unchanged.
At infinity the subtracted mean is log(p)/φ_r; at p it is zero.
The equality of these period operations does not delete the
integral Kummer boundary in (5).

There is an exact relation with the previous division-field units.
Since v_r∈L_r, grouping embeddings over L_r gives
$$\sum_{\sigma:F_r/K}\ell_v(\sigma U_r)\ell_v(\sigma v_r)
=\sum_{\tau:L_r/K}\ell_v(\tau e_r)\ell_v(\tau v_r). \tag{11}$$
For averaged rather than summed periods, the F_r expression is
therefore [F_r:L_r]⁻¹ times the L_r expression. For Kummer
corestriction, in contrast, there is no such averaging denominator.

## 4. The exact tower covariance and renormalization

**[NEW] Proposition 4.1.** For an embedding τ of F_r let the p²
embeddings σ of F_{r+1} over it have logarithms
X_σ=ℓ_v(σU_{r+1}), Y_σ=ℓ_v(σv_{r+1}). Put
$$\bar X_\tau=p^{-2}\sum_{\sigma|\tau}X_\sigma
=p^{-2}\ell_v(\tau U_r),\qquad
\bar Y_\tau=p^{-2}\sum_{\sigma|\tau}Y_\sigma
=p^{-1}\ell_v(\tau v_r).$$
Then
$$P_{r+1,v}=p^{-3}P_{r,v}+\operatorname{Cov}_{r,v}, \tag{12}$$
where the exact additional term is
$$\operatorname{Cov}_{r,v}=
\frac1{D_r}\sum_\tau\frac1{p^2}
\sum_{\sigma|\tau}(X_\sigma-\bar X_\tau)
(Y_\sigma-\bar Y_\tau). \tag{13}$$

*Proof.* The means follow from the two different norm laws (4).
In each fiber expand X_σY_σ around its two means. The two mixed
linear sums vanish. Their product contributes p⁻³ times the
lower-level product, and the remaining term is (13). ∎

For example, the degree-renormalized sequence
R_{r,v}=p^{3(r-1)}P_{r,v} satisfies the exact identity
$$R_{r+1,v}-R_{r,v}=p^{3r}\operatorname{Cov}_{r,v}. \tag{14}$$
No summability, p-adic boundedness or canonical limiting value of
these increments has been proved. Subtracting their finite sum
simply telescopes to P_{1,v}; this does not extract new higher-level
arithmetic information. Pairing with the rational norm-compatible
second input p^{1-r}[v_r] instead changes the coefficient in
(12) to p⁻⁴ and rescales the covariance accordingly. The
unbounded p-denominators in that replacement remain explicit.

## 5. The arithmetic cup, with its degree and boundary retained

Fix m and r≥m. Write δ_m for the Kummer map. Start with the
canonical INTEGRAL symbol {U_r,v_r} in H²_M(F_r,Z(2)).
Its rationalization lies in H²_M(F_r,Q(2)); reduction and the
étale cycle class of the integral symbol give
$$c_{r,m}=\delta_m(U_r)\cup\delta_m(v_r)
\in H^2(F_r,\mu_{p^m}^{\otimes2}). \tag{15}$$
It has cohomological degree two and Tate twist two. It is not an
H¹(F_r,V_pE) class. The relevant local invariant pairing pairs a
representation T with T∨(1), not with an arbitrarily equal Tate
twist; see
[Rubin, Euler Systems, I §4, Theorem 4.1](https://swc-math.github.io/aws/1999/99RubinES.pdf),
Annals of Math. Studies147 (2000).

For example, at a fixed finite p-adic field F,
H²(F,Q_p(2)) is zero by local duality, since its dual H⁰ group
is Q_p(−1)^G_F=0. This does not make the secondary period (9)
zero. Conversely, a finite cup (15) need not be discarded by
first tensoring with Q_p at that fixed level.

Equation (7) yields the integral identity
$$\varphi_r c_{r,m}
=\delta_m(U_r)\cup\delta_m(w_r)
+\delta_m(U_r)\cup\delta_m(p). \tag{16}$$
The last term is part of the exact Kummer expression. No division
by φ_r modulo p^m, and no omission of this term because
log_p p=0, is justified.

**[NEW] Proposition 5.1.** Let G=Gal(F_{r+1}/F_r), and abbreviate
the two Kummer classes at the upper level to a',b'. Then
$$\operatorname{Cor}(a'\cup b')
=p\,c_{r,m}
-\sum_{1\ne g\in G}\operatorname{Cor}(a'\cup g b'). \tag{17}$$
Thus simultaneous norm compatibility of the two inputs does not
remove the cross-conjugate terms in the cup.

*Proof.* The projection formula and the identity
res cor(b')=Σ_g g b' give
$$\sum_g\operatorname{Cor}(a'\cup g b')
=\operatorname{Cor}(a')\cup\operatorname{Cor}(b')
=\delta_m(U_r)\cup p\delta_m(v_r).$$
Remove the identity term. This proof also applies after localization
to the full semilocal algebra over either fixed prime of K above p,
using the sum of local corestrictions. It assumes no fixed splitting
pattern for individual primes in the ray tower. ∎

The restriction/corestriction and semilocal conventions here are
those of Rubin, I §§2–4 and Appendix B §5. Equation (17) is also
the precise arithmetic counterpart of retaining a covariance
instead of multiplying two ordinary norms.

## 6. A concrete CM involution tests the proposed comparison

The following involution is not complex conjugation: it fixes K.

**[NEW] Proposition 6.1.** There is a compatible order-two element
τ=(τ_r) of Gal(∪F_r/K) such that
$$\tau|_{C_\infty}=1,\qquad
\Psi(\tau)=\Psi^c(\tau)=\rho(\tau)=\rho'(\tau)=-1, \tag{18}$$
where ρ=(Ψ^c)⁻¹ and ρ'=Ψ⁻¹.

*Proof.* In the ray group modulo fp^r choose the class represented
by a_r≡1 modulo f and a_r≡−1 modulo p^r. CRT gives compatible
classes. Its square is the identity. It is nontrivial because a
global unit congruent to 1 modulo f must be 1, whereas −1≠1
modulo p^r. Its norm residue is (+1) modulo p^r, so it fixes C_r.

The CM reciprocity formula gives the Tate-module action on a
principal ideal (a_r) with a_r≡1 modulo the conductor by a_r
on the two p-adic components. Hence both actions are −1 modulo
p^r, proving (18) in the inverse limit. The primary formula is
Kato, Astérisque295 (2004), §15.8, pp.256–257, DOI10.24033/ast.639:
his cohomological action is the inverse Hecke character; dualizing
gives the Tate action. For the residue −1 this inverse has the
same sign. The full
[primary PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf)
was inspected, including its conductor and Artin-symbol convention. ∎

Put e⁺=(1+τ)/2 and e⁻=(1−τ)/2. These projectors are integral
in the completed unit group and its Kummer realizations because
p≥5. On rational unit classes e⁻U means one half of the actual
ratio U/τU; no algebraic square root of that ratio is being chosen.

**[NEW] Proposition 6.2.** The specified polarized operation (10)
sees only the τ-even part of its first input, whereas the exact
CM-twisted class and derived class see only its τ-odd part:
$$P_{r,v}(e^-U)=0,\qquad
\mathcal Z_{n,m}(e^+U)=0,\qquad
\mathcal Z_{n,m}(e^-U)=\mathcal Z_{n,m}(U). \tag{19}$$
The same last two identities hold for the reviewed d_m whenever
its augmentation vanishes, and for the resulting framed
realization where its inverse is defined.

*Proof.* Since v_r is fixed by τ, reindexing the embeddings in
(10) gives P(τU)=P(U). More strongly, (10) factors through the
ordinary cyclotomic norm:
$$\sum_{\sigma:F_r/K}\ell_v(\sigma U)\ell_v(\sigma v_r)
=\sum_{\eta:C_r/K}\ell_v(\eta N_{F_r/C_r}U)
\ell_v(\eta v_r). \tag{20}$$
This proves the first assertion.

For the twisted map before smoothing, with K_n=KQ_n⊂C_r,
the projection formula and inner-action invariance give
$$\begin{aligned}
\operatorname{Cor}_{F_r/K_n}
(\delta_m(\tau U)\otimes t_{\rho,m})
&=\rho(\tau)^{-1}
\operatorname{Cor}_{F_r/K_n}
\tau(\delta_m(U)\otimes t_{\rho,m})\\
&=-\operatorname{Cor}_{F_r/K_n}
(\delta_m(U)\otimes t_{\rho,m}).
\end{aligned} \tag{21}$$
The actual Kato smoothing operator commutes with τ in this
abelian tower. Shapiro, the fixed Betti map and the first-jet
projection are linear. Consequently (21) also holds for
the normalized class Z_{n,m}. The integral kernel extraction of
d_m is unique and linear, so it has the same sign. ∎

This is a test on the Galois module generated by the actual theta
units. In particular U/τU has zero polarized period at every
level, while its exact twisted derivative is twice that of U.
No nonvanishing of d_m is assumed. The precise consequence is:
if a linear natural recovery of d_m factored only through these
unweighted polarized periods, it would force d_m(U)=0. The result
does not prohibit a numerical coincidence at a single input, nor
does it prove a counterexample to BSD.

All scalar renormalizations and covariance corrections made solely
from (10) retain this even character. The two inputs are now
genuinely specified; using a non-torsion cyclotomic p-unit has
repaired the earlier zero logarithm, but has not repaired this CM
character mismatch.

## 7. The correctly dual CM Kummer pairing is also computed

To repair the coefficient type, set
$$A_m=T_{\mathfrak p}E/p^m,\qquad
B_m=T_{\bar{\mathfrak p}}E/p^m,\qquad
A_m\otimes B_m\simeq\mu_{p^m}.
$$
Choose the second finite CM coefficient t_ρ',m dual to the first
under the fixed polarization, so that their product corresponds
to the dual Tate basis. Over F_r, r≥m, both are invariant.
There are genuine finite classes
$$a_{r,m}(U)=\delta_m(U)\otimes t_{\rho,m}\in H^1(F_r,A_m),
\qquad
b_{r,m}=\delta_m(v_r)\otimes t_{\rho',m}\in H^1(F_r,B_m).
\tag{22}$$
Their cup followed by polarization has degree two and coefficient
μ_{p^m}; local invariant maps may therefore be applied with their
usual Tate-duality normalization.

**[NEW] Proposition 7.1.** Separately tracing the cyclotomic
companion to any K_n⊂C_r gives exactly zero:
$$\operatorname{Cor}_{F_r/K_n}b_{r,m}=0. \tag{23}$$
Forming the cup and then corestricting need not agree with pairing
the separately corestricted classes. The cup-then-corestriction
operation to C_r also annihilates the τ-odd theta component.
The untraced cup in H²(F_r,μ_{p^m}) is not asserted to be zero.

*Proof.* The unit v_r is τ-invariant while its coefficient
t_ρ',m has τ-action −1. Corestriction is unchanged by the inner
action of τ in the target group, so its value in (23) equals its
own negative. Since 2 is invertible modulo p^m it is zero.
This argument retains v_r itself with its valuation; centering or
multiplying its class by a scalar cannot restore a nonzero trace.

For the cup-then-corestriction operation, t_ρ,m⊗t_ρ',m is the finite
dual Tate vector, fixed over C_r. Applying the cup projection
formula first to F_r/C_r gives
$$\operatorname{Cor}_{F_r/C_r}
\bigl(a_{r,m}(U)\cup b_{r,m}\bigr)
=\bigl(\delta_m(N_{F_r/C_r}U)\cup\delta_m(v_r)\bigr)
\otimes t_{-1,m}. \tag{24}$$
For U replaced by U/τU its norm is one, proving the asserted
zero after corestriction to C_r. Further corestriction or
localization preserves that zero; this does not prove vanishing
of the untraced cup over F_r. ∎

There is no contradictory Tate-weight claim in (22)–(24).
Before insertion of the finite invariant vectors, the actual
motivic product of the two CM-twisted Kummer extensions is as
follows. Write A,B for the pure CM motives, k=Q(i) for the
coefficient field, R=A(−1)=B∨ and R'=B(−1)=A∨. The p-adic
character of R' is Ψ⁻¹. The product has type
$$\operatorname{Ext}^2(R\otimes R',A\otimes B)
=\operatorname{Ext}^2(k(-1),k(1)), \tag{25}$$
whose weight difference is two Tate twists. The coefficient
μ_{p^m} in (22) comes from the explicit finite-coefficient pullback
of the CHOSEN INTEGRAL realization/lattice of the source k(−1)
along t_{−1,m}. It is not reduction of a bare rational motive,
nor an invariant rational map k→k(−1). In every case the cup remains in degree two.
No degree-two symbol or local invariant is relabeled as d_m∈H¹.

## 8. The unchanged exact derivative and the first missing comparison

The input for the actual derivative continues to be the
coefficient-one integral theta Kummer difference. Grouping its
norm from F_r to L_r gives exactly δ_m(e_r)⊗t_ρ,m.
There is no averaging factor in this cohomological transfer.
Then retain, exactly,
$$12\bigl(a^2-\Psi^c((a))\overline\sigma_a\bigr),\qquad
\gamma_{\rm CM}=2\operatorname{pr}_\rho(\gamma_E^+),\qquad
g_p=\log_p(1+p).
\tag{26}$$
The first expression is the Kato smoothing divisor, with its
sign and twelfth power; the second is the fixed rational Betti
coefficient. For n≥m and r≥max(m,n+1), after the same
Shapiro and γ↦1+T maps, a cocycle f=A+TD with A(g)=gv−v
has the exact derivative
$$d_m(g)=D(g)+c_\gamma(g)gv,\qquad
c_\gamma(g)=g_p^{-1}\log_p\chi_{\rm cyc}(g).
\tag{27}$$
Propositions 6.2 and 7.1 compare the new operations with this
specific map, not an unspecified class of similar height.

Where Reg_p≠0 the previously proved framed output is
$$\mathcal B_p^{-1}\left(
\frac{p}{2\#E(\mathbb F_p)}\operatorname{pr}_W
((\varprojlim_m d_m)\otimes T)\right)
=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}\Xi,
\tag{28}$$
with e_p=(1−α⁻¹)², c_cmp,p=(156iΩ_p)⁻¹, and
M_p=∫log_p(χ_cyc)²dμ_ψ. If the point regulator is degenerate,
only the established undivided identity is used. Possible additional
Selmer directions are not assumed absent.

The positive polarized determinant operation (9) removes the
earlier quadratic-in-theta-input defect and is independent of C_v.
Its exact norm and covariance are now proved. However, its
unweighted polarized trace and the cup-then-corestriction operation
to C_r are both τ-even in the theta argument. No vanishing of
the untraced cup over F_r is asserted. The exact derivative is τ-odd.
The natural separately traced dual companion (22) is zero.
These are explicit failures of the tested comparison mechanisms,
not a broad claim that cyclotomic p-units cannot occur in a more
complicated arithmetic construction.

**[GAP CM-CycPair, remaining covariance and framed comparison].**
Construct a specified arithmetic secondary operation on the actual
theta-unit and cyclotomic-p-unit motives, their boundary (5), and
the fixed point frames, whose finite derived output agrees with
(27), including the τ-odd covariance (21), and whose framed
realizations give one element Z_alg over Q satisfying (28) at
every good split prime in the stated inverse-map scope, with the
compatible undivided identity elsewhere, and
$$R_\infty(Z_{\rm alg})=\frac{L''(E,1)/2}{2\Omega_E}.
\tag{29}$$
In particular a new operation must retain information lost by
(20), or introduce a justified CM-sensitive companion instead of
the zero trace (23); merely renormalizing (10) cannot do this.
The finite p-boundary and any division by p or φ_r must be part
of that construction. Writing Z_alg=qΞ would prove q=n_E∈Q;
rationality is not an input.

The candidates in (9), (15) and (22) were actually constructed and
their tower/character tests performed above. No operation meeting
this remaining comparison has been constructed. Full BSD, full
Sha finiteness and the complex leading-term formula are not claimed.

## 9. Primary-source and verification record

New source checks used Rubin's author text of Euler Systems,
I §4, II §4, VI §§2–3/5.3 and Appendix B §5; Schmitt's
ray-unit construction and distributions; and Kato2004 §15.8's
CM conductor/reciprocity convention in the previously downloaded
primary PDF. The ray-group, polynomial norm, valuation, covariance,
projector and cup formulas have full proofs above.
No previous numerical certificate was rerun, and no new agent was
created. The [independent PASS review](review-cm-cyclotomic-pairing.md)
checked all nine sections, including the integral-symbol and
chosen-lattice clarification. Subsequent status/link edits are editorial.
