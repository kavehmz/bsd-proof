# The theta series' elliptic projection and its metric adjoint

Date: 2026-09-12. Owner: coordinator. All eight sections passed
[independent adversarial review](review-theta-elliptic-projection.md)
after the compactification correction in §6. Restart:
[checkpoint](theta-elliptic-projection-checkpoint.md).
Full BSD over Q is still neither proved nor disproved.

This note computes the ACTUAL point projection of the whole untwisted
Du–Yang theta series and its curvature pairing with the original forcing.
The older eta-Hodge point projection was already known to vanish; that
older computation is not counted again as a new result here.

## 1. Fixed curve, map, and distinction between the two theta variables

Keep E=389a1, N=389, and the degree-40 parametrization
pi:X=X_0(N) -> E with pi(infinity)=O. Let w=w_N be Fricke and
alpha=pi^*omega=c_pi 2pi i f(z)dz. The previously reviewed facts are

$$f|_2w=-f,\quad \pi(0)=\pi(\infty)=O,\quad
\pi\circ w=[-1]\circ\pi.\tag{1.1}$$

They follow from the actual Fricke eigenvalue, the cuspidal torsion
relation and the certified torsion-free E(Q); see
[arithmetic Green, §6](arithmetic-green-comparison.md) and
[Mellin variation, §§5–6](mellin-variation-attack.md).
For example pi composed with w plus pi has zero differential by the
first equality, hence is constant; its value at infinity is pi(0)=O.
This verifies the last equality as a map of the actual curves.

Use the exact unit and forcing from the integrated construction:

$$v=N^{-6}\Delta(z)/\Delta(Nz),\quad l=\log|v|,\quad
g=(2\pi i)^{-1}d\log v/dz,\quad F=y^2f\bar g.$$

Let Y=X minus its cusps. All integrations below retain the effective
Du–Yang convention, with multiplicities 2/|Aut|. The universal elliptic
rank-two heat lattice of the original Mellin integral and the rank-three
orthogonal lattice of the Kudla–Millson lift are DISTINCT constructions.
The latter has an auxiliary upper-half-plane variable tau.

The actual spectral value remains

$$\mathcal M=\int_YFj_2\,d\mu
=-\frac{3N(N-1)}{2\pi^3}\ell L(E,2)\ne0,\qquad
\ell=L''(E,1)/2.\tag{1.2}$$

Here j_2 is the fixed second Laurent coefficient of
J_N=xi(2s)(N^(2s)-1)E_infinity. The lower pairings with 1,j_0,j_1
vanish, as proved in the existing full integral. The question is whether
an actual arithmetic theta operation supplies its period-height comparison.

## 2. Fricke symmetry of the actual Kudla–Millson kernel and CM cycles

Use EXACTLY the lattice, cosets and kernel of
[Du–Yang, arXiv:1702.07917v2](https://arxiv.org/pdf/1702.07917v2),
definitions(1.1)–(1.3),(2.3)–(2.7). Thus

$$L=\left\{\begin{pmatrix}b&-a/N\\c&-b\end{pmatrix}:a,b,c\in\mathbb Z\right\},
\quad Q(A)=N\det(A),\quad
\mu_r=\operatorname{diag}(r/(2N),-r/(2N)).$$

The discriminant group is indexed by r modulo2N. For n>0, the
point of the symmetric domain attached to A is the positive line R A,
so A and -A determine the same CM point. The cycles Z(n,mu) retain
all source orbit and stabilizer multiplicities.

**[NEW] Proposition 2.1.** Componentwise in the same discriminant basis,

$$w^*\Theta_L(\tau,z)=\Theta_L(\tau,z),\qquad
w^*Z(n,\mu)=Z(n,\mu)\quad(n>0).\tag{2.1}$$

*Proof.* Conjugation by the actual Fricke matrix is

$$\begin{pmatrix}0&-1\\N&0\end{pmatrix}
\begin{pmatrix}b&-a/N\\c&-b\end{pmatrix}
\begin{pmatrix}0&1/N\\-1&0\end{pmatrix}
=\begin{pmatrix}-b&-c/N\\a&b\end{pmatrix}.\tag{2.2}$$

It preserves L,Q, and sends mu_r to mu_-r. It normalizes Gamma_0(N).
The normalized real matrix w/sqrt(N) lies in SL_2(R) and acts on the
symmetric domain by z -> -1/(Nz). The Kudla–Millson form is equivariant
under this action. This also follows directly from its formula

$$\varphi^0(A,z)=\left((A,A(z))^2-\frac1{2\pi}\right)
                    e^{-2\pi R(A,z)}d\mu(z):$$

both the quadratic majorant and the squared pairing are invariant under
simultaneous conjugation. The form is EVEN in A, including its
exp(2pi i Q(A)tau) factor. Reindexing by (2.2) therefore sends its
mu component to the -mu component, which equals the mu component
by A -> -A. This proves the kernel equality, including the differential
form factor on the base.

The same reindexing sends CM point orbits to the -mu orbits, preserving
stabilizers. The map A -> -A identifies those orbits' point divisors
because they represent the same positive lines. This proves the second
equality as an equality of the actual weighted cycles. No restriction
on primitivity of their CM discriminants, or a split-prime-only
Gross–Zagier formula, is required. ∎

It follows for any smooth moderate-growth scalar h for which the lift
converges that

$$I_L(\tau,h)=I_L\left(\tau,\frac{h+h\circ w}{2}\right).
\tag{2.3}$$

This is proved by change of variables in the actual integral. In the
cases used here convergence follows from Du–Yang Proposition2.2's
Gaussian cusp decay and the earlier joint bounds. In particular this
kernel has no injective inverse on the whole scalar function space.
The statement is about this untwisted kernel, not every theta lift.

## 3. The whole arithmetic theta series has zero elliptic point projection

Let Xcal be the source's integral modular model. For an arithmetic
class Dhat=(D,G), use the same well-defined rational projection as in
the earlier arithmetic-Green note:

$$\mathfrak p_E(\widehat D)
 =\pi_*\left([D_{\mathbb Q}]-\deg(D_{\mathbb Q})[\infty]\right)
        \in E(\mathbb Q)\otimes\mathbb R.\tag{3.1}$$

For rational coefficients the target is E(Q) tensor Q; extend linearly
when the source includes real cusp coefficients. A principal arithmetic
divisor gives a principal generic divisor, and a vertical or pure Green
class has zero generic part. Thus the map is well-defined on the actual
arithmetic Chow group. It is NOT a projection of all metric information
to the point group.

By (1.1), for generic divisor classes and hence for this projection,

$$\mathfrak p_E(w^*\widehat D)=-\mathfrak p_E(\widehat D).
\tag{3.2}$$

The infinity-to-zero basepoint change gives no extra point because both
cusps map to O. We do not need to assert that every Green or vertical
term of the arithmetic theta series is Fricke invariant.

**[NEW] Theorem 3.1.** The entire ACTUAL Du–Yang arithmetic theta series
has zero projection to this elliptic point group, coefficient by coefficient:

$$\boxed{\ \mathfrak p_E(\widehat\phi_L(\tau))=0.\ }\tag{3.3}$$

*Proof.* For n>0 the generic divisor Z(n,mu) is Fricke invariant by
Proposition2.1. Its projection is its own negative by (3.2), so it is
zero in E(Q) tensor R. This uses the actual weighted divisor, not an
unspecified degree-zero representative or a numerical CM height.

For n<0 the source definitions give either zero finite part or a real
linear combination of cusp divisors. All degree-zero cusp divisors
project to zero by (1.1), so these coefficients also vanish.
At n=0, the source's corrected coefficient consists of its naive
cuspidal class, -2 times the Hodge class, vertical components and a
pure metric term. The vertical and metric parts project to zero by
definition. Generically the twelfth power of the Hodge bundle has the
nonzero rational section Delta, supported only at cusps. Its normalized
degree-zero elliptic projection is therefore zero after tensoring with
Q, hence over R. The cuspidal part is already zero. This proves (3.3).

These are all cases in Du–Yang's definitions(1.3)–(1.5). Their
Propositions8.2–8.3 and the displayed formula in the proof of Theorem8.4
identify the Mordell–Weil component by precisely the degree-zero generic
classes, with all degree, vertical and smooth-function terms separate.
Thus no Green contribution has silently been used to change a point
class in (3.3). ∎

The source's entire Jacobian-valued component need not be zero: this
is its projection to the PARTICULAR Fricke-negative elliptic quotient
E=389a1. No statement about all elliptic factors or all theta variants
is made. This is stronger than the previous eta-Hodge-only projection
calculation, which concerned only its own cuspidal divisor.

**[NEW] Corollary 3.2.** Every canonical E-height pairing of the projected
theta coefficients with the fixed P=(-1,1),Q=(0,-1) is zero. Any two
point classes obtained solely by linear combinations of these projections
have zero height determinant.

*Proof.* The projected point classes themselves are zero by Theorem3.1.
Apply the bilinear Neron–Tate height pairing. ∎

The certified full point regulator is positive. Thus this particular
point-valued projection cannot by itself construct its nonzero frame.
This corollary does not set arbitrary arithmetic metric intersections
to zero, and does not exclude a mixed or higher construction retaining
additional data.

## 4. The original forcing survives Fricke symmetrization

The following symmetry facts were partly used in the older Mellin note;
we spell them out to prevent an invalid inference from (3.3).
The modular discriminant transformation gives EXACTLY

$$v(wz)=v(z)^{-1},\quad l(wz)=-l(z),\quad
w^*\alpha=-\alpha,\quad g|_2w=-g,\quad F(wz)=F(z).
\tag{4.1}$$

Consequently the fixed transgression

$$\eta=-\frac{i}{4\pi^2c_\pi}l\alpha,
\qquad d\eta=F\,d\mu\tag{4.2}$$

is Fricke EVEN. Its nonzero second spectral pairing (1.2) is not
annihilated by (2.3). The two odd pieces in (4.1) occur together.
Removing either the unit logarithm or the elliptic differential changes
the actual input and its symmetry. In particular zero point projection
of the arithmetic theta coefficients does not imply zero of (1.2).

## 5. An actual Kummer source retains the logarithmic symmetry

There is an arithmetic object for the logarithm in (4.2), without
assigning a motive to the spectral parameter. Over the actual open
curve Y define the 1-motive

$$\mathcal K_v=[\mathbb Z_Y\longrightarrow\mathbb G_{m,Y}],
                     \qquad 1\longmapsto v.\tag{5.1}$$

Its homological Betti/Tate realization is an extension of Z(0) by
Z(1); the Tate subobject is not omitted. This is the elementary toric
case of Deligne's realizations in
[*Theorie de Hodge III*, §10.1.3 and10.1.5–10.1.10](https://www.numdam.org/item/10.1007/BF02685881.pdf),
Publ. Math. IHES44 (1974),5–77, DOI10.1007/BF02685881.
The torus and lattice map in (5.1) exist over Y even at points where
v=1; it is not replaced by an unlabelled relative pair whose two
sections would merge at such a point.

**[NEW] Proposition 5.1.** Inversion of the actual torus and the identity
on the lattice give a canonical equivariance

$$w^*\mathcal K_v\overset\sim\longrightarrow\mathcal K_v,
\qquad \text{graded actions }(+1,-1)\text{ on }\mathbb Z(0),\mathbb Z(1).
\tag{5.2}$$

It squares to the identity and respects its actual integral realizations.

*Proof.* The lattice maps of w^*K_v and K_v send1 to v^(-1) and v.
Inverting G_m carries the former to the latter and fixes the zero
section, while the lattice map is the identity. Composing twice is
literally the identity. On Tate/Kummer coefficients inversion is -1.
For example at coefficient n, the torsor of n-th roots of v maps to
the torsor of n-th roots of v^(-1) by x -> x^(-1), preserving every
transition in n and negating the mu_n subgroup.

Analytically the Betti fiber can be written

$$\{(r,z)\in\mathbb Z\times\mathbb C:\exp(z)=v^r\}.$$

The transformation (r,z) -> (r,-z) gives exactly (5.2), in either
inverse direction, with no additive logarithm constant chosen afterward.
On a simply connected chart the de Rham frame e0,e1 has

$$\nabla e_0=-d\log v\,e_1,\quad \nabla e_1=0,
\qquad \gamma_0=e_0+(\log v)e_1,\quad\gamma_1=2\pi i\,e_1.
\tag{5.3}$$

These comparison vectors are horizontal. Their equivariance is
e0 -> e0 and e1 -> -e1 over inversion, by (4.1). It preserves the
Tate comparison factor2pi i and the integral monodromy. Taking real
logarithms gives l -> -l, with no branch ambiguity. ∎

Together with the actual map pi and its [-1] action, (5.1) therefore
retains the two arithmetic symmetry factors that occur in l alpha.
It is a source for the LOGARITHM, not an identification of eta with a
closed rational cohomology class. In fact d eta=F dmu is generally
nonzero. Tensoring geometric realizations or writing this transgression
does not construct the missing second radial moment or its rational
point-height determinant comparison.

## 6. The exact cutoff metric-adjoint pairing of the original forcing

The forcing F is generally complex-valued. Write F_R=Re(F). Under
complex conjugation on the rational modular curve, c(z)=-bar z,
its real Fourier coefficients give F(cz)=bar F(z). Thus F_R is
real and conjugation invariant. It is smooth on the open orbifold,
but a distinction at its compactification is ESSENTIAL.

**Review correction.** Borel–Serre flatness does not imply smoothness
in the algebraic cusp coordinate q. In fact at infinity,

$$F_R=\frac{1-N}{4\pi^2}\operatorname{Re}(q)(\log|q|)^2
                   +O(|q|^2(1+|\log|q||)^2).\tag{6.1}$$

Along positive real q its first derivative is unbounded. Therefore
(0,2F_R) is NOT asserted to be a smooth Gillet–Soule class on the
compact curve, or a class in Du–Yang's particular smooth-remainder
log-log framework. The draft's former single-class assertion is
withdrawn. We use the following convergent family of ACTUAL smooth
classes instead; no stronger arithmetic-current theory is imported.

Choose conjugation-invariant smooth cutoffs chi_epsilon on the compact
coarse curve, zero in radius-epsilon coordinate disks at both cusps,
and one outside radius2epsilon. If needed cut off also at the finitely
many elliptic orbifold points; this ensures that every resulting function
is smooth even in coarse local coordinates, without needing to identify
orbifold smoothness with coarse smoothness. Use cutoffs invariant under
the finite conjugation orbits and let them increase pointwise to one
away from that finite set. Define

$$\widehat A_{F,\epsilon}=(0,2\chi_\epsilon F_R),\qquad
             \|1\|_\epsilon=\exp(-\chi_\epsilon F_R).\tag{6.2}$$

Each is a genuine smooth metrized trivial line allowed in the source's
arithmetic intersection theory. Its underlying algebraic line is trivial.
We do not insert the c-odd imaginary part into a real arithmetic Chow group.

**[NEW] Proposition 6.1.** With the source's curvature and intersection
normalization, the actual convergent limit is

$$\boxed{\ I_L(\tau,F)=I_L(\tau,F_R)
 =\lim_{\epsilon\to0}
   \langle\widehat\phi_L(\tau),\widehat A_{F,\epsilon}\rangle_{\rm GS}.\ }
\tag{6.3}$$

*Proof.* The scalar coefficients of Theta_L relative to dmu are real
and c-invariant before their exp(2pi i n tau) factors. Directly,
conjugation by diag(1,-1) preserves L and each mu_r. The symmetric-domain
involution c changes the relevant linear pairing by a sign, removed by
its square, and preserves the majorant. Reindex the full lattice as
in §2. Antiholomorphic pullback reverses the oriented (1,1)-form, while
the integration measure is invariant. Hence the integral of the c-odd
Im(F) against each scalar theta coefficient is zero. This proves the
first equality without conjugating the auxiliary variable tau.

Du–Yang's defining Green-current identity, equation(8.4), gives
c1(phi_hat_L)=Theta_L. Intersection with a pure metric class a(h)
is one-half its integral against this curvature, in their effective
convention. For each epsilon, the second expression in (6.3) is thus
I_L(tau,chi_epsilon F_R). The normalization agrees with
<phi,a(1)>=degree(phi)/2. Dominated convergence at the cusps follows
from their Gaussian kernel bound and F_R=O(r log²r). At elliptic
points use a finite uniformizing chart, where the kernel and original
F are smooth and integrable; removing shrinking disks changes no limit.
This proves (6.3), independent of the chosen cutoff profiles. ∎

The limit is a limit of pairings, not a claimed limit inside the
arithmetic Chow group. In particular it supplies no single rational
arithmetic class by an implicit completion of that group.

There is a further exact decomposition. Let Delta_hat_GS,
mu_GS=c1(Delta_hat_GS) and phi_SM(tau,z) be the ACTUAL objects of
Du–Yang§8, with their prescribed smoothing and mean-zero normalization.
The source proves

$$dd^c_z\phi_{\rm SM}
 =\Theta_L-\frac{\deg\widehat\phi_L}{\deg\widehat\Delta_{\rm GS}}\mu_{\rm GS}.
\tag{6.4}$$

Integrating against the cutoffs and then taking their limits gives

$$I_L(\tau,F)=
 \frac{\deg\widehat\phi_L}{\deg\widehat\Delta_{\rm GS}}
                         \int_XF_R\mu_{\rm GS}
                  +\int_X\phi_{\rm SM}\,dd^cF_R.\tag{6.5}$$

The last integral uses the locally integrable DISTRIBUTIONAL derivative
of F_R. It is not justified by falsely calling F_R smooth on X.
Here are the boundary checks. In a cusp disk r=|q|,

$$F_R=O(r(1+|\log r|)^2),\quad
 dF_R=O((1+|\log r|)^2)|dq|,\quad
 dd^cF_R=O((1+|\log r|)/r)\,dx_q\wedge dy_q.$$

There is no cusp atom: its boundary flux tends to zero. On the cutoff
annulus, first and second derivatives of chi_epsilon cost at most
C/epsilon and C/epsilon². The integrals of the derivative-of-cutoff
terms in dd^c(chi_epsilon F_R), paired with the smooth bounded
phi_SM, are O(epsilon(1+|log epsilon|)^2). They tend to zero;
the derivative without cutoff is locally integrable by the displayed
bound. This proves the Stokes limit at both cusps.

For completeness, at an elliptic point of order e, a uniformizing
coordinate t has coarse parameter t^e. Since f(z)dz and g(z)dz
are holomorphic invariant one-forms there, their coefficients vanish
to order at least e-1 in t. Thus F_R=O(|t|^(2e-2)), with the
corresponding differentiated estimates. Coarse-radius epsilon cutoffs
there give error O(epsilon^(2-2/e)), which also tends to zero.
All these estimates may be checked on a fixed torsion-free analytic
cover, retaining its finite effective degree. They require no new
arithmetic theorem about stack currents.

Thus (6.5) is a valid distributional Stokes identity with the source's
prescribed smooth orbifold lifts. Do NOT replace int F_R mu_GS by
zero merely because the older cancellation was for hyperbolic dmu;
these measures need not coincide. The formula exhibits the actual
degree and smooth-metric terms that contribute to the theta image.

This remains compatible with the zero elliptic point projection:
every A_(F,epsilon) has zero point projection, while arithmetic
metric/degree pairings need not vanish. The limit does not construct
a rational coefficient in the finite motivic point-height line.

## 7. What remains in the original weighted comparison

The original mass has a scalar spectral factor j2:
int F j2 dmu. The cutoff identity(6.3) computes the lift of F,
not that mass. Combining it formally with I_L(j2) does not authorize
multiplying theta lifts or canceling a Petersson norm. An actual
adjoint/doubling or regulator comparison with the correct kernels,
measures and coefficients is still needed.

The already computed I_L(j2) contains the third Eisenstein derivative;
its higher response is not in the tested Hodge/vertical span. The
entire untwisted point projection in Theorem3.1 is zero, so neither
that point projection nor a linear Neron–Tate pairing against its
coefficients can supply the nonzero fixed point determinant. The
logarithmic mixed source of §5 retains data that those projections
forget, but it has not yet been compared with the second radial jet.

**[GAP TPJ-389].** Construct an arithmetic comparison retaining that
logarithmic source, the actual original f-weighted pairing and the
higher spectral response, mapping to

$$D_{\rm pt}\otimes\mathbb Q\beta_2\otimes\mathbb Q(1)^{-2}$$

with real coefficient6N(N-1)n_E. The noncentral beta2 already has its
unique rational arithmetic lift and sufficient integral multiple;
that completed construction is not repeated here. The present
projection, equivariance and metric-adjoint formulas do not prove
rationality/integrality of n_E or the universal BSD statement.

## 8. Source and review scope

Root read Du–Yang1702.07917v2, the actual lattice/kernel definitions,
arithmetic coefficient cases, Propositions8.2–8.3 and equations8.4–8.5;
and the precise prior Fricke, cusp and eta normalization proofs.
The nonsmooth cusp term is treated by actual smooth cutoff classes and
a proved distributional limit, not a single smooth GS class. The
one-motive in(5.1) is written explicitly and its inversion and
realizations are checked directly. No claim about integral stack
stabilizer torsion is made; arithmetic projections use rational/real
coefficients as in the source. No numerical certificate was rerun.
Every new deduction requires independent review before promotion.
