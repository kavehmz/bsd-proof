# Integral lifts of the fixed Kato cofactor and a quadratic Heegner test

Date: 2026-09-13. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
**PASS: all nine sections independently reviewed after the §3 source repair.**
See [the complete review](review-heegner-cofactor-lift.md), against
mathematical revision
1069acaa79900311139625292de131d1e4d380f768f6d9464cd43d42c995150d.
Subsequent completion-status and review-link edits are editorial.
Restart: [checkpoint](heegner-cofactor-lift-checkpoint.md).
Full BSD over Q remains the universal objective.

We prove a point-local integral lifting criterion for the FIXED
cofactor, and bound its finite lifting defect using the order of
the actual two-prime Heegner class. In the primitive case no scaling
is needed. A thicker actual Heegner quotient is then tested against
the native conditions, retaining its other-old-prime residue.
No finite Sha assumption or rational-point premise for Kato is used.

## 1. Fixed input and three different lifting questions

Use the [reviewed Prym proof](heegner-prym-norm-attack.md) and
[its review](review-heegner-prym-norm.md).
Keep n=p^k, R=Z/n, T=T_pE, M=E[n], M_D=M tensor epsilon_K,
the O5 ordinary nonanomalous/surjective/Manin range, the specified
quadratic twist K with rank-zero L(E^D,1), and p not dividing h_K
for the two independent tame coordinates. All earlier local
conditions and the actual complement U of NpD ell q remain.

Let kappa=kappa_(ell q,Q)^raw be the ACTUAL raw Heegner class,
strict at both old primes. The FIXED cofactor classes A,B
and the actual integral Kato derivative w0 give
$$
 \begin{split}
 D&=[A,B]_m,\qquad a=[w_k,B]_m,\qquad b=[A,w_k]_m,\\
 z&=d_0(Dw_k-aA-bB).
 \end{split}
 \tag{1}
$$
No A or B is adjusted to choose a desired value. d0 and all
cofactor coordinates are exactly the existing ones.

The questions remain distinct:
an integral point-local Selmer lift in T;
an integral cohomological norm lift in T_pC_i^+;
and a native first lift in N_i with all point-image conditions.
The first does not imply the second or third.
The original compact-FIRST pairing and contragredient point
transport are unchanged.

## 2. The intrinsic point-local integral lifting defect

Write
$$
 \Sigma=\operatorname{Sel}_{p^\infty}(E/\mathbb Q),\quad
 \Sigma_{\rm div}\subset\Sigma,\quad
 F_E=\Sigma/\Sigma_{\rm div},\quad
 {\cal S}_T=\varprojlim_r\operatorname{Sel}_{p^r}(E/\mathbb Q).
 \tag{2}
$$
The transition maps in the last expression are multiplication p
on the torsion coefficients. F_E is finite because Sigma is
cofinitely generated over Z_p. Its definition does NOT assert
that Sha(E)[p^infinity] is finite.

Since E(Q)[p^infinity]=0, the finite point-Kummer Selmer group
identifies canonically with Sigma[p^r] for every r.
For instance the finite and infinite global Kummer sequences,
and divisibility of E(Q) tensor Q_p/Z_p, give this identification
by their exact kernels and cokernels. It retains the full local
point conditions, including torsion at finite places.

**[NEW] Proposition2.1.** There is an exact sequence
$$
 0\to{\cal S}_T/n{\cal S}_T
     \longrightarrow\operatorname{Sel}_n(E/\mathbb Q)
     \xrightarrow{\delta_n}F_E[n]\to0 .
 \tag{3}
$$
In particular delta_n is the exact obstruction to an integral
POINT-LOCAL Selmer lift, not merely to an ordinary global
Galois cohomology lift.

*Proof.* Abstractly Sigma is a direct sum of a divisible
p-primary group and a finite group. Its maximal divisible
subgroup is canonical. The p-adic Tate module of a finite
p-group is zero; that of the divisible part is free Z_p
of rank s_p. The inverse limit in(2) is therefore the latter
Tate module, with image Sigma_div[n] at level n.
The map Sigma[n]→F_E[n] is onto: for a lift of an n-torsion
element, its n-multiple lies in Sigma_div and can be removed
using divisibility. Its kernel is Sigma_div[n].
This proves(3) canonically, without choosing a splitting.

The compatible global Kummer classes in the inverse limit
give actual integral T-cohomology classes; their localizations
lie in the inverse limits of the point-Kummer groups.
Thus the image is the specified integral point-local Selmer
lattice. Square.

The actual w_k lies in the kernel of delta_n. Consequently
$$
 \boxed{\delta_n(z)=-d_0\{a\,\delta_n(A)+b\,\delta_n(B)\}.}
 \tag{4}
$$
This is a necessary and sufficient criterion for an unscaled
integral Selmer lift of the actual z.
The ordinary global Bockstein beta_E factors through(3),
but its vanishing alone need not imply delta_n(z)=0.
No such converse is used.

For clarity, even a change which preserves the old localization
coordinates is not harmless. If A'=A+u, B'=B+v with both
old localizations of u,v zero, then D,a,b are unchanged and
$$
 z'-z=-d_0(au+bv).
 \tag{5}
$$
Thus this change preserves the actual finite target exactly
when d0(au+bv)=0 in the FULL Selmer group.
No change of this kind is made below; choosing an integral
lift of a fixed finite class does not change that class.

## 3. A bound from the order of the actual Heegner class

Suppose for this section that kappa is nonzero and has
exact order p^s in coefficient n=p^k. Put c=k-s.
The previously proved lower bound gives s_p(E)>=3.
BCGS's order-of-vanishing theorem and the rank-zero twist
then give
$$
 \nu(\boldsymbol\kappa^{\rm Heeg})=2,\qquad s_p(E)=3.
 \tag{6}
$$
This does not identify s_p(E) with the rational point rank.

Here is the additional primary structure input: its
LARGER-corank plus branch, together with one nonnegativity
inequality from its second displayed line.
[Kim2203.12161v7, §2.1, §2.3 and Theorem3.3](https://arxiv.org/html/2203.12161v7),
arXiv stamp12January2024, describes
$$
 \Sigma_{K,/\rm div}^{+}
       \simeq\bigoplus_{j\ge1}
                 (\mathbb Z/p^{a_j^+})^{\oplus2},\qquad
 a_j^+=M_{2j+1}-M_{2j+2}.
 \tag{7}
$$
Here M_r is EXACTLY Kim's partial^(r) from §2.3, with
divisibility measured in the conductor-modified Selmer
group, not an index defined in the ambient H1.
The working hypotheses are surjectivity and p-unit Manin
constant; in our Heegner case N^-=1, so the additional
quaternionic ramification conditions are empty.
Nontriviality is supplied either by the present nonzero
kappa or the already verified BCGS theorem.
Since W(E)=-1 and nu=2, equation(7) is the plus branch.
For the SAME Selmer-defined indices, the second displayed
line of Theorem3.3, with i=1 and |r^+-r^-|=3, gives
$$
                         M_2-M_3=a_3^-\ge0 .
 \tag{7a}
$$
This uses only nonnegativity of that elementary-divisor
exponent. No value of an initial opposite-sign error term
or total reduced Selmer order is used. In particular we
do not identify Kim's Selmer divisibility filtration with
BCGS's ambient-H1 filtration or import monotonicity between them.

Also M2<=c: if the actual class at conductor ell q in
Kim's coefficient T/I_(ell q)T is p^j-divisible in its
modified Selmer group, its reduction to coefficient p^k
is p^j-divisible in H1 and has order at most p^(k-j).
The latter order is p^s, so j<=k-s=c. Taking the minimum
over two-prime conductors gives the claim. The standard
factor u2=-1 does not change order or divisibility, and
restriction Q→K preserves order by its p-unit degree2.
Nonnegativity of M4, equation(7a), and the decreasing
ordering of the elementary-divisor exponents in(7) now give
$$
 a_j^+\le a_1^+=M_3-M_4\le M_2\le c .
$$
Quadratic descent identifies F_E with this plus quotient.
Thus:

**[NEW] Theorem3.1.**
$$
                         p^c F_E=0 .
 \tag{8}
$$
No absolute Sha finiteness or refined M_infinity/Tamagawa
formula is needed for(8).

Set v_R(0)=k and use the ordinary truncated p-valuation
on R otherwise. If t0=v_p(d0), define
$$
 r=\max\{c-t_0-\min(v_R(a),v_R(b)),\,0\}.
 \tag{9}
$$
Then(4) and(8) give
$$
                         \delta_n(p^r z)=0 .
 \tag{10}
$$
This is a proved annihilator of the PARTICULAR integral
Selmer lifting defect. It is not yet an annihilator of
the native Cassels–Tate value.

The lift is constructive as an inverse-limit Selmer class.
Choose integral point-local lifts A_c,B_c of the fixed
classes p^c A,p^c B, which exist by(3),(8).
Choose scalar lifts tilde D,tilde a,tilde b in Z_p with
the given residues and valuations at least their truncated
valuations. The coefficients
$$
 u_A=p^r d_0\widetilde a/p^c,\qquad
 u_B=p^r d_0\widetilde b/p^c
$$
are integral by(9). Hence
$$
 w_{z,r}=p^r d_0\widetilde D\,w_0-u_A A_c-u_B B_c
                 \in{\cal S}_T
 \tag{11}
$$
reduces to exactly p^r z.
Only divisibility proved in Z_p justifies the displayed
coefficient quotients. No nonunit is canceled in a
finite cohomology group.
When r>0, the theorem does not recover an unscaled lift.

## 4. The primitive case removes the fixed A,B defects entirely

If kappa has order n, then c=0 and(8) gives F_E=0.
There is also an independent elementary verification from
the completed higher-residue argument:
Sel_n(E/Q)=R³ while s_p(E)>=3.
The finitely generated dual of Sigma must have rank3
and no finite summand, since any nonzero finite summand
would contribute additional p-torsion at level n.
Thus
$$
 \Sigma\simeq(\mathbb Q_p/\mathbb Z_p)^3,\qquad
 {\cal S}_T\simeq\mathbb Z_p^3,\qquad
 {\cal S}_T/n\simeq\operatorname{Sel}_n(E/\mathbb Q).
 \tag{12}
$$
Every FIXED A,B therefore has an integral point-local lift.
In particular beta_E(A)=beta_E(B)=0 and the actual unscaled
z has an integral Selmer lift w_z.
Possible divisible Sha directions remain in(12).
It neither constructs three rational points nor assumes
that the integral lattice is the Mordell–Weil lattice.

Let epsilon_(C_i) be the exact-order-n class of the
reviewed Prym norm lattice. For every lift in(11),
the particular global norm obstruction becomes
$$
 {\cal B}_{i,n}(p^r z)
                      =[\epsilon_{C_i}\cup w_{z,r}].
 \tag{13}
$$
This class is independent of all integral lift and scalar
representative choices. Indeed any two lifts of the same
finite Selmer class differ by n times an integral Selmer
class, by(3). Their cup difference vanishes because
n[epsilon_(C_i)]=0. No coefficient-map lift excluded
by the predecessor is being constructed.

For r=0 this is a canonical PARTICULAR cup for the
unchanged target z, with the fixed A,B defects now proved
absent. Its value is not thereby proved zero.
An ordinary global norm preimage and a point-local native
norm preimage remain separate requirements.

## 5. A genuine thicker Heegner quotient

For §§5–8 work in the clean native range, including
p-unit Tamagawa and Sel_n(E^D)=0.
These hypotheses are used for local point conditions and the
specified b_i, not for the integral-lift theorem of§3.
Use the actual Heegner points and compatible transversals from
the reviewed two-prime construction. Trace the prime-to-p
ring-class part by its actual norm, without dividing its degree.

For an ordered pair (i,j)=(ell,q) or(q,ell), set
$$
 {\cal C}_{i,j}=R[X_i,X_j]/(X_i^3,X_j^2).
 \tag{14}
$$
Here X_i=log(1+Y_i)=Y_i-Y_i²/2 and X_j=Y_j.
The actual group-ring quotient sends
sigma_i to exp(X_i)=1+X_i+X_i²/2 and sigma_j to1+X_j.
It is well-defined: both group orders are divisible by n,
and2 is invertible. The inverse Artin character is
exp(a_i X_i+a_j X_j). Reflection acts by X_i→-X_i,
X_j→-X_j, exactly in these coordinates.

Let mathfrak H_(ij) be the actual Shapiro class of y_(ij)
in this coefficient module, with the same reflection-plus
projection as in the completed construction.
Over H_(ij) its coefficients are the Kummer classes of
the corresponding finite weighted point sums.
All coefficients with X_j-degree0 vanish modulo n:
the j-norm of y_(ij) is a_j(E)y_i, and a_j(E) is zero
modulo n. The coefficient of X_j with X_i-degree0
vanishes similarly using the i-norm. Therefore
$$
 \mathfrak H_{ij}\in
 \operatorname{im}\!\left[
 H^1\bigl(\mathbb Q,M\otimes J_{i,j}\bigr)
           \to H^1\bigl(\mathbb Q,M\otimes{\cal C}_{i,j}\bigr)
 \right],
 \qquad J_{i,j}=X_iX_j{\cal C}_{i,j}.
 \tag{15}
$$
This is a statement about the actual class, not formal
divisibility in a free cohomology module.

To justify descent and uniqueness, E(H_(ij))[p]=0 by the
previously reviewed irreducibility/ordinary-inertia argument.
Every coefficient quotient here is free over R and becomes
trivial apart from M over H_(ij). Inflation–restriction
therefore detects the asserted zero quotient class, and H0
of that quotient is zero. The preimage in(15) is UNIQUE.

The basis u=X_iX_j, v=X_i²X_j identifies M tensor J_(i,j)
with the actual N_i: the action is u→u+a_i v, v→v,
and reflection has signs+,-. Its bottom coefficient is the
existing raw two-prime kappa because X_iX_j and Y_iY_j
have the same mixed quadratic coefficient.
Thus(15) constructs a specified global first lift
$$
                         H_i\in H^1(\mathbb Q,N_i),
                     \qquad \pi(H_i)=\kappa .
 \tag{16}
$$
No p-power is divided in(15), and no coefficient-map lift
excluded by the preceding Prym theorem is used.

The single-prime class in R[X_i]/X_i³ also has zero constant
and linear coefficients: the first is its norm, and the
second is the already vanishing one-prime Kolyvagin class.
It has a unique preimage in X_i²M, giving a specified
reflection-plus class
$$
                           \eta_i\in H^1(\mathbb Q,M).
 \tag{17}
$$
Before the stated plus projection its restriction to H_i
is the Kummer class of the actual quadratic moment
$$
 Q_i^{[2]}=\frac12\sum_{g\in\operatorname{Gal}(H_i/K)}
                              j_i(g)^2\,g y_i
                 \quad\text{in }E(H_i)\otimes\mathbb Z_{(p)} .
 \tag{18}
$$
The additive Artin representatives j_i(g) include the fixed
unnormalized prime-to-p traces. Changing their integer lifts
changes(18) by an n-multiple and not its finite class.
The reflection-plus projector is retained explicitly; it is
not replaced by a claim that the raw moment point is rational.

The primary point norm and CM reduction congruence used here
are [Howard1202.6340v1, §1.7, equation13](https://arxiv.org/html/1202.6340v1),
the28February2012 archive of the published2004 construction.
Its Lemma1.7.2 supplies the raw division-cofactor cocycle.
We use its point identities and that cocycle, not the
unqualified global coefficient automorphisms of1.7.5.
All raw/standard signs remain the previously repaired ones.

## 6. Exact native local conditions of the thicker lift

The following local computation retains the H0 terms which
can be lost by looking only at restrictions to H_(ij).
At each old prime use the fixed Frobenius gauge in which
the local additive Artin coordinate has value0 on Frobenius.
The other coordinate is locally trivial over K because
an inert rational prime is principal in the opposite
ring-class group. In log coordinates reflection negates
both variables. Write e_+,e_- for the elliptic Frobenius
eigenvectors, with e_+ the vector fixed by the native
beta normalization.

The local native point image in M tensor C_(i,j) is zero
at either old prime. The relevant inertia norm element has
coefficients, through degree2,
$$
 d,\quad d(d-1)/2,\quad d(d-1)(2d-1)/12,
 \tag{19}
$$
where n divides d. They all vanish in R since p>=5.
This is the same regular point-image calculation as before,
now with the actual next coefficient retained.

At the prime i, C_(i,j)/J_(i,j) has basis
1,X_i,X_i²,X_j. Its inertia invariants are spanned by
X_i² and X_j. After Frobenius invariance, H0 is spanned
by X_i²e_+ and X_j e_-.
The first lifts to an invariant of the full C module.
The boundary of the second has nonzero bottom inertia
value -e_- in N_i, hence maps injectively to the
singular bottom M line.
Since loc_i(kappa)=0, the preimage H_i in(16) must
therefore have
$$
                         \operatorname{loc}_i H_i=0.
 \tag{20}
$$
It is genuinely native at its OWN old prime.

At the prime j, inertia invariants of the same quotient
are X_i,X_i²,X_j, with invariant vectors
X_i e_-, X_i²e_+, X_j e_-.
The last already lifts to an invariant of C.
The boundaries of the first two have inertia values
-u e_- and -v e_+, respectively.
The bottom strictness loc_j(kappa)=0 removes the first.
The remaining class is a transverse TOP M_D class.
Thus for one well-defined coefficient t_(i;j) in R,
$$
             \operatorname{loc}_j H_i=t_{i;j}\,\beta_j
                   \quad\text{in the top }M_D\text{ summand}.
 \tag{21}
$$
This term is not native at j unless it is zero.

Away from the old primes, H_i has the native finite condition.
At non-p unramified places the coefficient inclusion/quotient
is split as an inertia module, so the preimage of an unramified
class is unramified. The p-unit Tamagawa hypothesis makes
this the point condition in the p-part of the ring-class fields.
At p, the nonanomalous ordinary quotient has no residual
invariants; the same exact-sequence argument on ordinary
coefficients proves the point condition.
At D, order-two inertia is exact at odd p. The earlier
unnormalized prime-to-p trace preserves these point images.
No new bad-place condition is silently removed.

For the single-prime eta_i, the corresponding computation
with R[X_i]/X_i³ and ideal X_i² gives a transverse E
class at i and finite point conditions elsewhere.
In the additional primitive-kappa case, the old finite
localization Sel_n(E/Q)→R at i is surjective by the
completed higher-residue theorem. Poitou–Tate then makes
the i-relaxed global Selmer group equal to the ordinary
one: its potential singular quotient is dual to that
surjective localization. Finite and transverse lines
intersect trivially. Hence in that case
$$
 \eta_i\in\operatorname{Sel}_n(E/\mathbb Q),\qquad
                         \operatorname{loc}_i\eta_i=0.
 \tag{22}
$$
Neither this conclusion nor(17) makes eta_i a rational point.

## 7. Computing the other-old-prime residue on actual points

The coefficient t_(i;j) is not inferred just from local
restriction to H_(ij), which has a nonzero kernel.
There is an actual global comparison over H_i that fixes it.

Before taking the final reflection projector, restrict(15)
to G_(H_i). The i-coordinate is then trivial, so extraction
of the X_i² coefficient is G_(H_i)-equivariant.
It sends the thick Shapiro class to the j-Shapiro class
of the ACTUAL quadratic i-moment companion Y_(i;j),
obtained by applying the operator in(18), with compatible
lifts, to y_(ij). Its norm is
$$
 N_jY_{i;j}=a_j(E)Q_i^{[2]} .
 \tag{23}
$$
The exact sequence for R[X_j]/X_j² and ideal X_jM has
H0(H_i,M)=0, because E(H_i)[p]=0.
Thus the global preimage of this j-Shapiro class is unique.
It is MINUS the usual raw j-derivative class of Y_(i;j),
since the inverse-Artin linear coefficient is -D_j.
This uniqueness over H_i fixes the local transverse term;
no arbitrary local H0 section is selected.

For clarity its raw cofactor is the actual point
$$
 B_{i^{[2]},j}
      =\frac{j+1}{n}Y_{i;j}
           -\frac{a_j(E)}{n}Q_i^{[2]}
             \quad\text{in }E(H_{ij})\otimes\mathbb Z_{(p)} .
 \tag{24}
$$
Its j-norm is zero by(23). The coefficients in(24) are
integers, with only the already retained factor1/2 in
the quadratic moment. No division by a possibly
nondivisible point has been made.

The inert prime j splits completely in H_i/K.
Write F_j for rational arithmetic Frobenius on the
good special fiber. Before the final reflection projector,
let x be the finite F_j² evaluation of the unprojected
quadratic-moment class. The CM reduction congruence applies
to the companion and its weighted prefix; together with
Howard's raw division cocycle it gives
$$
 \overline B_{i^{[2]},j}=(a_j(E)-F_j)x=-F_jx .
 \tag{25}
$$
One can check the polynomial sign directly:
(a_j(E)-F_j)(F_j²-1)=(j+1)F_j-a_j(E).
The raw j-derivative has inertia value -bar B.
Our extracted top coefficient has its additional minus
from -D_j, so its inertia value is bar B.

Apply the fixed reflection-plus projector to the cofactor and x
in this calculation. Now write x=eta_(i,K)(F_j²) for their
projected value.
Finite evaluation has conjugation action F_j, whereas
transverse evaluation has action -F_j; the top coefficient
has the additional odd-degree sign. Thus the result is
compatible with that projector. In particular the x for
the class eta_i in(17) belongs to the plus Frobenius line.
Define its exact coordinate by
$$
 x=a_j^+(\eta_i)\,t_j^+,
 \qquad \beta_j(\sigma_j)=t_j^+ .
$$
Equations(21),(25) give the full-coefficient identity
$$
                         t_{i;j}=-a_j^+(\eta_i).
 \tag{26}
$$
This uses K-Frobenius F_j². In Q finite coordinates the
value has the explicit factor2 from unramified quadratic
restriction; inertia has no such factor.
No unrecorded change of t_j^+ or of the dual point frame
is allowed in(26).

## 8. An explicit factorization of the native scalar

Keep the already constructed global transverse twist tests
b_i,b_j and their actual cross-local coefficient
$$
 G_{ij}=B_i(\operatorname{loc}_i b_j,\beta_i)\in R,
                         \qquad G_{ij}=-G_{ji}.
 \tag{27}
$$
All their point-dual transports, including the p-coordinate
normalization, are exactly the completed ones.

Correct the actual first lift H_i by -t_(i;j)b_j in its
top M_D term. This removes its transverse class at j.
At all other non-i places it preserves the finite point
conditions. At i the former class was zero by(20);
the correction has finite coordinate -t_(i;j)G_ij.
The native local difference is its negative, by the
compact-FIRST convention. Hence
$$
 \boxed{{\cal R}_i(\kappa)
       =t_{i;j}G_{ij}
       =-a_j^+(\eta_i)G_{ij}.}
 \tag{28}
$$
The p-local condition remains finite during this correction.
It is not the discarded p-relaxed Kato correction from
the previous failed normalization.

If kappa has order n, the completed strict Selmer theorem
gives S=R kappa. The unchanged actual z in(1) therefore
has a UNIQUE coefficient alpha_z with z=alpha_z kappa.
It is computable from any actual full-order detecting
finite value of kappa, exactly as in the reviewed cofactor
formula; its denominator is a proved unit.
In particular alpha_z retains d0, D,a,b and the FIXED A,B.
Linearity of the native connecting pairing then gives
$$
 \boxed{{\cal R}_i(z)
       =-\alpha_z\,a_j^+(\eta_i)G_{ij}\quad(i\ne j).}
 \tag{29}
$$
No factor in this identity is asserted to be a unit or
canceled as a nonunit. Switching to the standard Heegner
class changes kappa by u2=-1 and changes alpha_z by
the inverse sign, leaving the actual expression invariant.
Its classical torsor interpretation still has CT=-R_i/n.

In the nonprimitive case(28) still evaluates this particular
Heegner class, but the strict group is not declared R kappa.
Formula(29) is not applied to an arbitrary cofactor z.
Instead the scaled integral-lift result(9)–(13) retains
the exact finite lifting defects and coefficient loss.
Without the clean native hypotheses retain the actual
extra local image groups; this simple two-old-place
factorization is not asserted for those groups.

## 9. The remaining arithmetic relation

The nonprimitive Heegner order supplies a concrete bound
on the fixed cofactor's point-local integral lifting defect.
The primitive case removes that defect entirely without
a finite-Sha or rational-point premise.
The thicker ACTUAL point construction then gives a
specified first lift and computes its other-old-prime
defect as a localization of a quadratic single-prime
Heegner moment. In the primitive clean case the native
value is exactly the product(29).

The extra untwisted L'''(E,1)=0 has not been proved to
annihilate alpha_z, a_j^+(eta_i), G_ij, or their particular
product. The moment eta_i is constructed from genuine
points of conductor i; it is not declared a complex
third derivative or a p-adic scalar chosen to fit one.
Likewise integral Selmer lifts may include divisible
Sha directions, and are not selected rational points.

**[OPEN, Cofactor-TP5].** Supply an arithmetic comparison
using the extra complex zero which kills the particular
product(29), with the nonprimitive and nonclean cases
retained, or constructs the required point-local norm
preimage of the actual input. The canonical cup in(13)
must be controlled on its actual class, not inferred
zero from the order of epsilon_C alone.
Even first-pairing vanishing leaves the previously
recorded mixed/top Heegner selection problem.

All nine sections passed [independent review](review-heegner-cofactor-lift.md),
including the plus-branch structure formula and the precise
second-line nonnegativity use in Kim's Theorem3.3,
the fixed-class integral lifts, the thick-quotient H0
calculations and the global-over-H_i determination of
the other-old-prime residue. Cofactor-TP5 above remains open.
No old numerical computation, shared-file edit,
completed-proof edit or additional agent was used.
