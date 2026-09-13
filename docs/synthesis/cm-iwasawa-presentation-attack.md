# The actual CM Iwasawa presentation and its normalized determinant element

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: bounded construction completed; all nine sections passed the
[independent coordinator review](review-cm-iwasawa-presentation.md).
Reviewed mathematical revision:
407f2915bf07aa46a3e1608c0d4ddab264b9580e9dca5fe891457f5cda826708.
Subsequent completion and review links are editorial.
Full BSD over Q remains the objective. No Sha-finiteness, corank-two,
nonzero first derivative or rational BSD quotient is assumed.

## 1. Fixed arithmetic complex and primary inputs

Keep E:y²=x³+39x, K=Q(i), f=(39(1+i)³), and the good split
scope p≥5, p≡1 mod4, p∤2·3·13 of the reviewed
[two-variable construction](cm-two-variable-jet-attack.md). Put
\[
 R=\mathbb Z_p[[X,Y]],\ I=(X,Y),\
 \mathbb T=T_\pi\widehat\otimes R^\iota,\quad
 C=R\Gamma(G_{K,S},\mathbb T),\quad M=H^1(C),\ N=H^2(C).       \tag{1}
\]
S contains the places above 2,3,13,p and infinity. The action is
g(t⊗1)=gt⊗(1+X)^(-c_pi(g))(1+Y)^(-c_barpi(g)).
The generators have Tate-character pairs (1+p,1),(1,1+p);
g_p=log_p(1+p). The cyclotomic QUOTIENT sends X,Y to T.

The class throughout is the ACTUAL normalized unit
\[
 z=q_a(X,Y)^{-1}z^{(a)}_{2,\infty},\quad
 q_a=12\left(a^2-u_a(1+X)^{\lambda_a}(1+Y)^{\lambda_a}\right),
 \quad u_a=\Psi^c((a))=\pm a,\quad\lambda_a=\log_p(a)/g_p.       \tag{2}
\]
Here a=5, except a=7 at p=5. Its finite theta units, coefficient
twist ρ=(Ψ^c)^(-1), and corestrictions are exactly those of the
predecessor. Θ_a retains its twelfth power. Before twisting the
branch is e_(ρ^(-1)); afterward it is the trivial Δ branch.
The tame norm is UNNORMALIZED: Res Cor=|Δ|e_1 with
|Δ|=1152(p−1)². Its vector is γ_CM=2pr_ρ(γ_E^+).
Finite ray exponents remain at least m+1 modulo p^m.

Primary perfectness input:
[Nekovář, Selmer complexes, Astérisque310 (2006)](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
3.4.2–3.4.4, 4.2.1–4.2.9 and 5.1.1–5.1.2, read directly.
Finite global/local p-cohomology and cd_p=2 meet his hypotheses;
Proposition4.2.9 gives perfect amplitude [0,2] for our free
continuous coefficient. This is initially ORDINARY cohomology.

Primary arithmetic inputs:
[Kato, Astérisque295 (2004)](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
Theorem12.4 with its CM proof, Theorem15.2 and
(15.6.1)–(15.6.4). These give cyclotomic rank-one H¹ and
torsion H², and equality of all height-one elliptic-unit/class
lengths when p splits and is prime to the finite ray torsion
degree and to the roots of unity in the Hilbert class field.
Here class number one, roots order four and |Δ| verify those
hypotheses. We construct exact elements separately below.

## 2. Actual two-term presentation and free rank-one H¹

**[NEW] Proposition 2.1.** There are finite free R-modules P,Q with
\[
 C\simeq[P\xrightarrow{D}Q]\quad\text{in degrees }1,2,\qquad
 \operatorname{rank}P=b+1,\quad\operatorname{rank}Q=b.           \tag{3}
\]
N is torsion and M is free of rank one.

*Proof.* R is complete Noetherian with finite residue field,
the coefficient is free, and G_(K,S) satisfies Nekovář's
finiteness condition and cd_p=2. Thus C has a finite free
model in degrees0,1,2.

At the COEFFICIENT level use finite free resolutions of the
quotients below. Continuous cochains preserve short exact
coefficient sequences and commute with finite free tensor
complexes by Nekovář3.4.2–3.4.4. Thus
\[
 C\otimes_R^{\mathbf L}B
 \simeq R\Gamma(G_{K,S},\mathbb T\otimes_R B)                   \tag{4}
\]
for B=R/I, R/(X−Y), R/(p,X,Y), and finite jet quotients.
R is regular, so these resolutions are finite. No H¹-flatness
is used. A lift of τ acts by −1 on the residual coefficient
and trivially on the ray quotient, so residual H⁰=0.
Cancel unit differential entries to make the free model
minimal. Its differential is zero modulo the maximal ideal;
its degree-zero term is therefore zero.

Write S_c=R/(X−Y)=Z_p[[T]]. Base change and the fixed Shapiro
identification give the actual cyclotomic T_pE complex over Q.
Kato12.4 gives its rank-one H¹ and torsion H². In particular
N/(X−Y)N is S_c-torsion. Localizing at the height-one prime
(X−Y) and applying Nakayama gives N_(X−Y)=0, hence rank_R N=0.
The Euler characteristic of the same free model on the
cyclotomic line is −1. This proves the ranks in (3).

The rank-one kernel is free by the following direct argument.
R is a regular factorial domain; see the standard algebraic theorem
[Stacks, Tag0AG0](https://stacks.math.columbia.edu/tag/0AG0).
Choose a fraction-field kernel
vector, clear denominators and divide the gcd of its coordinates,
obtaining h∈P with Dh=0. If t h∈P, t∈Frac R, then at each
height-one prime at least one coordinate of h is a unit.
Thus t lies in each height-one DVR, whose intersection is R.
Every integral kernel vector is therefore an R-multiple of h:
\[
 M=Rh.                                                       \tag{5}
\]
This also proves reflexivity. Coordinate gcd one does NOT mean
that the coordinates generate the unit ideal; they may all lie
in I. ∎

This is an actual presentation, not a postulated free cohomology
module. Its existence is proved; no numerical matrix of Galois
relations is computed here.

## 3. Cofactors and the integral determinant basis from the actual unit

Choose ordered bases in (3), and define
\[
 \Delta_j=(-1)^{j+1}\det D_{\widehat j},\quad
 \Delta=(\Delta_j)_j=c h,\quad z=f h.                          \tag{6}
\]
The empty minor is one if b=0. Both c,f∈R are nonzero:
D has full row rank generically and z has nonzero cyclotomic
image. Let 𝒟=det_R^(-1)C=det_RP⊗(det_RQ)^(-1).
The cofactor contraction j_D:𝒟→M sends its ordered frame ε
to Δ, with exactly (6)'s sign. This is the determinant convention
that sends (h wedge lifts of an ordered Q-basis)/(that Q-basis)
to h. It is compatible with changes of bases and adjoining an
acyclic summand. Expansion using a LAST localization row has
the additional sign (−1)^b retained in (15).

**[NEW] Proposition 3.1.** The exact element
\[
 \eta_z=j_D^{-1}(z)=u\epsilon,\qquad u=f/c                     \tag{7}
\]
is an INTEGRAL R-BASIS of 𝒟. The defined scalar u∈R^× is
not replaced by one.

*Proof.* At any height-one prime q, Smith normal form for D
over the corresponding DVR gives
\[
 v_q(c)=\operatorname{length}_{R_q}N_q,\qquad
 v_q(f)=\operatorname{length}_{R_q}(M/Rz)_q.                   \tag{8}
\]
The first equality uses the gcd of the maximal minors and a
unit coordinate of h there. Higher-codimension parts of N are
not declared zero by this computation.

Apply Kato15.2(b,c) and15.6 to K(p^infty f). Its diagonal
levels are cofinal in our tower. Kato15.6.2 compares the class
module with H² up to modules finite over Z_p, hence invisible
at height one of the three-dimensional algebra. Formula15.6.4
identifies the height-one elliptic-unit module with the
normalized theta element. Neither statement asserts equality
of the full class and H² modules.

Twisting by ρ is the integral ring automorphism
σ↦ρ(σ)^(-1)σ. Projecting the p-prime finite branch transports
the length equality to R, on exactly the pre-twist branch
e_(ρ^(-1)). The actual norm contributes |Δ|, a p-unit whose
value remains in z.

Here is the ramification-set check. Away from p the pro-p
ray extension is unramified. At each prime dividing f the CM
inertia character is nontrivial in μ_4, since f is its actual
conductor; it remains nontrivial modulo p≥5. The local
residual coefficient and its Tate dual have no invariants.
Local duality and the non-p Euler characteristic make all
local cohomology zero. Perfectness and residual base change
then make the R-local complex acyclic. Its unramified complex
is zero as well. Thus extending across these primes in
Kato's convention or removing them in G_(K,S) contributes no
term on this branch.

Finally the exact theta and Betti identification is the reviewed
[derived-unit construction, §3](cm-derived-unit-attack.md):
Θ_a is Kato theta to the twelfth power, and (2) divides by
12 times his N(a)−σ_a factor. The Betti coefficient is primitive
over Z_p in the present range. Explicitly in the lattice
b^vee,(ib)^vee, γ_E^+=(b^vee−(ib)^vee)/2; either CM projection
has coefficient (1±i)/4 in its eigenbasis. Multiplying by two
gives (1±i)/2, a p-unit. The exact coefficient, smoothing,
and norm remain in z, even though their p-unit property
suffices for this length comparison.

Rubin's hypotheses hold at EVERY height-one prime, including
(p): p splits, p∤4, and p∤1152(p−1)². Hence v_q(f)=v_q(c)
for every q. Factoriality implies u=f/c∈R^×, proving (7).
No correcting unit was chosen after the comparison. ∎

Thus the arithmetic unit constructs an exact determinant
basis, with integrality proved by a characteristic-divisor
theorem. Neither u(0) nor its real rationality has been
identified. Replacing the norm by its average would change
η_z by |Δ|^(-1); the present construction retains the norm.

## 4. Augmentation, first jets and all remaining Tor terms

Put D_0=D(0,0), h_0=h(0,0), f_0=f(0,0). Then
\[
 H^1(G_{K,S},T_\pi)=\ker(D_0:P/IP\to Q/IQ).                   \tag{9}
\]
There are no degree-zero boundaries in this model. The known
zero cohomological augmentation of z therefore means that its
VECTOR has zero constant coefficient. Write
\[
 z=Xv_\pi+Yv_{\bar\pi}+X^2v_{20}+XYv_{11}+Y^2v_{02}
                  \pmod{I^3P}.                             \tag{10}
\]
D_0v_pi=D_0v_barpi=0; their classes in (9) are precisely
d_pi,d_barpi. Indeed transport the coefficient first-jet
sequence through (4) and use its unique extraction.
In continuous cochains that transport is the reviewed
B+c_pi gv, D+c_barpi gv correction. Cancellation of the
degree-zero term explains why no correction remains in (10).

The exact resolution 0→R→P→Q→N→0, whose first arrow is h,
computes
\[
 \operatorname{Tor}_2^R(N,\mathbb Z_p)=\ker(h_0:\mathbb Z_p\to P/IP),
 \quad \operatorname{Tor}_1^R(N,\mathbb Z_p)=\ker D_0/\mathbb Z_ph_0,
 \quad N/IN=\operatorname{coker}D_0.                          \tag{11}
\]
This is the previous augmentation edge sequence with explicit
maps. Tor₂ is zero if h_0≠0 and is Z_p mapping onto M/IM
if h_0=0. Tor₁ can have torsion; h_0 need not be saturated.

Expanding f,h gives exactly
\[
 f_0h_0=0,\quad d_\pi=f_\pi h_0+f_0h_\pi,\quad
 d_{\bar\pi}=f_{\bar\pi}h_0+f_0h_{\bar\pi}.                    \tag{12}
\]
If h_0≠0, then f_0=0, so z∈IM and the derivatives are
dependent. If h_0=0, no such divisibility follows.
If both h_0,f_0 vanish, both derivatives vanish.
Independent derivatives would require the nonzero Tor₂
case and f_0≠0. Freeness has not removed this obstruction.

On S_c the actual kernel is likewise free rank one; choose its
primitive coordinate generator e_c. Since h has coordinate
gcd one, h(T,T) cannot be zero. Write
\[
 h(T,T)=s(T)e_c,\quad
 N[X-Y]\simeq S_c/(s),\quad
 z_{\rm cyc}=f(T,T)s(T)e_c=T w_\infty.                         \tag{13}
\]
These are exactly the one-element base-change sequence.
They do not set N[X−Y] to zero. The actual quotient is
w_infty=(f(T,T)s(T)/T)e_c. At the base,
Sh(d_pi+d_barpi)=w_0 with no factor two. Divisibility by T
may come from s, rather than from f.

**[NEW] Corollary 4.1.** If either actual integral ray derivative
is nonzero, Sel_(p^infty)(E/Q) has corank two and Sha[p^infty]
is finite. No such nonvanishing is proved here.

*Proof.* Let r=dim_(Q_p)H¹(G_(K,S),V_pi). By the reviewed
local theorem and Shapiro this is rational Selmer over Q.
The known point basis gives r≥2. Over Q_p the constant
matrix D_0 has rank b+1−r. In Q_p[[X,Y]], isolate this
invertible constant block by row and column operations.
Each maximal minor then contains at least r−1 entries in I.
Thus Δ, and z=uΔ, have coordinate I-order at least r−1.
Since P/I^jP is Z_p-free, this also holds integrally.
If r≥3 both first coefficients vanish. Nonvanishing forces
r=2. The p-primary Selmer group is cofinitely generated;
its quotient by the known rank-two point group is Sha[p^infty],
which is finite when its corank is zero. ∎


## 5. Actual local trivializations and a square Selmer matrix

At the unramified split place barpi put L=H¹(K_barpi,𝕋).
**[NEW] Proposition 5.1.** The local complex is L[-1], with
L free rank one over R. The ordinary Selmer complex of this
CM component has the actual square presentation
\[
 C_f=\operatorname{Cone}(C\to R\Gamma(K_{\bar\pi},\mathbb T))[-1]
 \simeq[P\xrightarrow{A=(D,\lambda)^t}Q\oplus L]
                   \quad\text{in degrees }1,2.              \tag{14}
\]

*Proof.* At barpi the residual representation is unramified
with arithmetic Frobenius α. The reviewed nonanomalous argument
for this curve gives α≠1 modulo p. Its Tate dual has nontrivial
cyclotomic inertia. Thus local residual H⁰,H² vanish, and the
local Euler characteristic gives H¹ dimension one. Perfectness
and residual minimality as in §2 leave a single free term.

The ordinary plus coefficient is all of T_pi at pi, and zero
at barpi. The bad non-p local complexes and their unramified
terms are acyclic by §3. Thus the ordinary local-condition
cone is (14). Its row λ:P→L represents actual localization.
Changing a representative by a homotopy changes λ by tD
for t:Q→L. This does not change λ(z) or the determinant below. ∎

At augmentation the [reviewed local theorem](cm-ray-local-conditions-attack.md)
gives zero localization on ALL H¹(G_(K,S),T_pi). Therefore
H¹(C_f⊗^LZ_p) is exactly (9). Both derivatives have unique
lifts to this Selmer H¹. Concretely their actual local cocycles
at barpi are coboundaries with unique nullhomotopies, because
local H⁰=0. The same holds at every finite coefficient level.
At pi the quotient local complex is zero. These are actual
local trivializations; no afterward chosen point correction
or global H/2 local normalization enters.

Choose a basis e_L of L. Let λ(h)=l e_L and λ(z)=F e_L.
Expansion of det A along its last row, with the sign (6), gives
\[
 \det A=(-1)^b c\,l,\qquad F=f\,l=(-1)^b u\det A.             \tag{15}
\]
F and det A are nonzero. To verify this arithmetically,
specialize to the cyclotomic line. Kato12.5 and13.5–13.7
give nonzero dual exponentials of the selected zeta class
at sufficiently ramified finite characters. The formal
ordinary component has zero dual exponential. Thus its
ordinary quotient localization is nonzero, proving F≠0.
The selected plus Betti coefficient generates that branch
by the reviewed conjugation relation. Hence C_f is
generically acyclic.

F is a coordinate of the ACTUAL localized unit in L. An
arbitrary choice e_L does not turn it into a canonically
normalized Katz L-function. Changing e_L rescales F and
det A together; (15) is invariant in the corresponding lines.

The unit and BOTH actual first derivatives have zero
barpi localization. The local complex L[-1] has exact base
change, so
\[
                         F\in I^2.                          \tag{16}
\]
This is a two-variable assertion, stronger than divisibility
of F(T,T) by T².

## 6. Linearized differential and genuine Selmer second-jet identities

Expand D=D_0+XD_pi+YD_barpi+… and A=A_0+XA_pi+YA_barpi+….
The NATURAL connecting maps of the first coefficient jet are
\[
 \partial_j^g:\ker D_0\to\operatorname{coker}D_0,\quad
             x\mapsto[D_jx],\qquad
 \partial_j^f:H^1(C_{f,0})\to H^2(C_{f,0}),\quad
             x\mapsto[A_jx].                                \tag{17}
\]
Changing a lift adds a D_0 or A_0 boundary. On continuous
global cochains the inverse coefficient action gives
∂_j^g=−c_j cup: its deformed differential on a constant
cochain has first term −X(c_pi cup a)−Y(c_barpi cup a).

The height convention in [BKS §5.1.1](https://arxiv.org/pdf/1910.07404)
uses MINUS the natural connecting map before duality.
Its height Bockstein is therefore −∂^f. Keep this sign
distinct from the natural maps in the next identities.

Write
\[
 F=F_{20}X^2+F_{11}XY+F_{02}Y^2\pmod{I^3},\qquad
 j^+(e_{L,0})=[(0,e_{L,0})]\in H^2(C_{f,0}).                 \tag{18}
\]
Here j^+ is DEFINED by the positive coordinate inclusion
in the fiber differential (Da,λa−db). It is not silently
identified with a differently signed triangle boundary.

**[NEW] Proposition 6.1.** The actual Selmer H² satisfies
\[
 \begin{aligned}
 \partial_\pi^f(d_\pi)&=F_{20}j^+(e_{L,0}),\\
 \partial_\pi^f(d_{\bar\pi})+
 \partial_{\bar\pi}^f(d_\pi)&=F_{11}j^+(e_{L,0}),\\
 \partial_{\bar\pi}^f(d_{\bar\pi})&=F_{02}j^+(e_{L,0}).
 \end{aligned}                                               \tag{19}
\]
Replacing ∂ by the height Bockstein negates the right sides.

*Proof.* The actual unit vector satisfies A z=(0,F e_L).
Insert (10). The X²,XY,Y² coefficients on the left are
A_0v_20+A_pi v_pi,
A_0v_11+A_pi v_barpi+A_barpi v_pi, and
A_0v_02+A_barpi v_barpi. Passing to coker A_0 gives (19).
These are identities in the SELMER cone, retaining its local
terms. Projection to coker D_0 recovers the older ordinary
global cup identities. ∎

The equations determine the two diagonal responses and the
polarized sum. They do not determine the two mixed terms
separately, or individual cyclotomic height projections.

To compare with the fixed numerical normalization, calculate
directly on the ACTUAL global derivative w_infty. No bounded
Coleman factorization on an arbitrary generator of L is assumed.
Local Shapiro identifies L on the cyclotomic line with the
ordinary quotient at Q_p. Put iota_p=O_p(e_(L,0)), where
the exact quotient functional is
O_p(ξ)=[exp*ξ,δ_0]=(expδ_0,ξ)_p, with
\[
 \delta_0=k_\alpha^{-1}\nu,\quad
 k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1}),\quad
 \varphi\nu=\beta^{-1}\nu,\quad[\omega,\nu]=1,\quad\beta=p/\alpha .
\]
The scalar iota_p is nonzero and is not assumed a p-unit.
It is the value of the fixed local integral basis, not a
normalization prescribed after the fact.

Indeed z_cyc=T w_infty and the local module is free, so
\[
 \operatorname{loc}^{-}(w_\infty)=\frac{F(T,T)}T e_L|_{\rm cyc}.
\]
By (16), F(T,T) is divisible by T². Set
F_Sigma=F_20+F_11+F_02. The local first-jet class is therefore
F_Sigma e_(L,0)⊗T. This is EXACTLY Rubin's derivative:
\[
 D(w_\infty)=F_\Sigma e_{L,0}\otimes T.
\]
The definition immediately after BKS(6.4.1) identifies D(y)
by loc^-(y)=i(D(y)), where i is the positive coefficient
inclusion. Its uniqueness uses H⁰(Q_p,F^-V)=0. Thus no
minus sign enters this extraction; the separately stated
minus in the height Bockstein remains unchanged.

The base of this actual w_infty is already proved Selmer,
without a Sha assumption. Apply the proof of BKS Lemma6.14
to this global class, obtaining its augmentation congruence
\[
 \operatorname{Col}(w_\infty)
 \equiv(\exp(\delta_0),D(w_\infty))_p
 =\iota_pF_\Sigma T\pmod{T^2}.
\]
The exact global reciprocity for the normalized z_cyc, with
z_cyc=T w_infty, identifies its second coefficient as in
the calculation following that lemma. Hence
\[
                  c_2=\iota_p(F_{20}+F_{11}+F_{02}).          \tag{20}
\]
Only this congruence for the actual global derivative is
used. No power-series germ for Col(e_L|cyc), or division
by T in an unrestricted inverse limit of finite group
algebras, is asserted. These are coefficient identities,
so no factorial is missing.

Summing (19) along X,Y↦T recovers the old derived-height
identity with its independently reviewed duality convention:
\[
 h_\Gamma(x,w_0\otimes T)=k_\alpha\log_\omega(x)c_2T^2.
\]
The numerical conversion retains exactly
\[
 c_2=\frac{c_{\rm cmp,p}M_p}{2g_p^2},\quad
 c_{\rm cmp,p}=(156i\Omega_p)^{-1},\quad e_p=(1-\alpha^{-1})^2,
 \quad k_\alpha e_p=\#E(\mathbb F_p)/p.                        \tag{21}
\]
Thus the final frame factor is still p/(2#E(F_p)).
No inverse of iota_p, a logarithm or an Euler factor is
taken in an integral or finite coefficient ring.

## 7. Exact determinant specialization through the rank jump

The integral basis η_z DOES specialize under perfect base change:
\[
 \eta_{z,0}\in
 \det_{\mathbb Z_p}^{-1}R\Gamma(G_{K,S},T_\pi).
\]
This is a precise p-local determinant object from actual
units. Its target retains H² and possible extra Selmer
directions; it is not yet the rational point determinant.

Let r=dim_(Q_p)H¹(C_(f,0))≥2. The square A_0 has nullity r.
Over Q_p, isolate its invertible constant block of size
b+1−r. The remaining Schur complement has zero constant
term and linear part X B_pi+Y B_barpi, where B_j is (17)
on the kernel/cokernel. Every term in its determinant
has I-degree at least r. Its degree-r part is exactly
det(X B_pi+Y B_barpi), multiplied by the determinant of
the isolated constant block in the induced frames.
A higher Schur term contributes only in degree at least r+1.
This is a direct determinant calculation on the actual
complex; no nondegeneracy of the B_j is assumed.

Equation (15) multiplies that leading determinant by (−1)^b u(0),
a p-unit whose value is retained. IF r=2 this gives the
quadratic Bockstein/height determinant. That equality of
ranks would also identify rational Selmer with the known
point space and imply p-primary Sha finiteness. If r>2,
both first unit jets are zero by Corollary4.1, and the
determinant comparison has higher degree. No step here
decides which case occurs or discards those extra directions.

In particular the existence of a nonzero integral determinant
basis does not imply a nonzero first derivative. The cofactor
map can vanish to higher order even while its source basis
remains primitive.

## 8. Exact result and the first remaining rational comparison

The actual complex has a proved two-term free presentation,
and H¹ is proved free rank one. The actual normalized elliptic
unit gives the integral determinant BASIS (7). Its localization
satisfies the exact square Selmer identity F=(−1)^b u det A, and its
two Selmer first derivatives, with unique local trivializations,
satisfy (19). This construction retains all Tor terms in
(11),(13); no I-divisibility is inferred from freeness.

The augmentation differential, its Bockstein maps, u(0) and
local coordinate have not been numerically computed.
Neither derivative is proved nonzero or independent.

**[GAP CM-Presentation-BSD].** Construct, before separate p-adic
completion, an arithmetic operation on the normalized unit
determinants and fixed point motives producing ONE rational
framed Z_alg∈𝓛_(P,Q) such that its localizations give
\[
 \mathcal B_p^{-1}\left(
 \frac{p}{2\#E(\mathbb F_p)}\operatorname{pr}_{W_p}
 \bigl(\operatorname{Sh}(d_\pi+d_{\bar\pi})\otimes T\bigr)\right)
 =\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}\Xi,         \tag{22}
\]
where the inverse is only on its specified line when Reg_p≠0,
with the established undivided identities otherwise, and
\[
 R_\infty(Z_{\rm alg})=\frac{L''(E,1)/2}{2\Omega_E}.             \tag{23}
\]
Then its rational coefficient would equal n_E as a CONCLUSION.
The integral R-basis η_z does not supply this rational descent:
its augmentation is still a separate p-adic cohomological
determinant with the rank and point-space issues of §7.
The actual local reference C_v remains distinct from the
normalized GLOBAL height block H/2.

## 9. Source and verification record

Nekovář's primary PDF is cached at
/tmp/cm-presentation-nekovar.pdf, SHA256
61c84e5ad3252a2e520747215ac57a282addc2b58c824a3637bcd77bbe02153f.
Printed pp.83–84,96–100,113–114 were inspected for the exact
cochain, perfectness, finiteness and local-duality statements.
The [author errata](https://webusers.imj-prg.fr/~jan.nekovar/pu/selerr.pdf)
do not alter these sections.

The Kato cache is /tmp/cm-derived-kato2004.pdf and
/tmp/cm-derived-kato2004.txt. The all-height-one CM comparison,
including actual elliptic-unit generator and smoothing ideal,
was checked at printed pp.250–255. The cyclotomic nonvanishing
was checked in13.5–13.7. The exact theta/Betti and Coleman
conventions are the separately reviewed predecessor ones;
(20) was rederived here.

No old numerical certificate was rerun, and no agent was created.
The [independent PASS review](review-cm-iwasawa-presentation.md)
checks all nine sections, including the direct Rubin-derivative
repair of (20). Nonvanishing of the first derivatives and the
rational global comparison remain unproved. Full BSD remains unresolved.
