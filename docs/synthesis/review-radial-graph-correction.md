# Independent review of the radial graph correction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file.

**PASS after the recorded normalization and relative-category precisions.**
All seven sections of the
[proof](radial-graph-correction-attack.md) and its
[checkpoint](radial-graph-correction-checkpoint.md) were read.
Reviewed proof SHA256:
e843569799237cf2022f0103527046e091390379055aef65ea1e13d597c8cf99.
Reviewed checkpoint SHA256:
fdfe600ef7646c647ee0bd4f52cc94caf211a9e776268d427d37ce2a3a722684.
Subsequent PASS links and completion statuses are editorial.

The real relative construction and its exact scalar are established.
The claimed rational scalar-Kummer source exists, but its entire
image has zero pairing. No rational spectral lift is claimed.

## 1. Rational relative source and the Green curvature

The formula L_D=d^*O_E(O) tensor p_E^*O_E(O)^{-1}
gives the displayed divisor Gamma_pi-Gamma_O.
On each cusp fiber the two maps agree, so cancellation
supplies the actual rational trivialization, not just
a degree-zero restriction.

I read
[Voevodsky, Proposition4.1.5](https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s5.pdf)
and the relative Picard description following
[MVW Definition7.10](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).
Both V and B are proper and Q admits resolution, so
the cone M(B) to M(V) is M^c(V^circ). The relative
Picard class therefore has the specified rational
motivic degree2 and twist1. Ordinary cohomology of
the punctured surface is not substituted.

The theta-product mean computation for g is correct:
the horizontal mean
-pi tau_2/3+2pi t-2pi t^2/tau_2 has vertical average0.
Its simple logarithmic zero gives delta_O, and the
quadratic term contributes -mu_E in the stated dd^c
normalization. Subtracting the two pullbacks gives
the full curvature(2.4), including its base term.
There is no purely vertical component.

Every term of dd^c a wedge Omega_D has too many base
degrees and is zero, also as a distribution.
For the fiber contraction, only -beta wedge dbar w
survives. Its integral with Omega_A dw is
Omega_A beta=alpha, since the fiber integral of
dbar w wedge dw is2i tau_2. This verifies the sign
and all comparison periods in(2.5).

## 2. Star sign and its normalization

Direct differentiation gives
$$
 \partial U_a+\bar\partial\overline{U_a}
           =a\,dd^cG-G\,dd^ca .
$$
The two cross-derivative terms cancel with the
conjugate expression. Consequently S_a equals
aOmega_D plus that explicit exact current, and
dd^c S_a=dd^ca wedge Omega_D=0. The minus sign
before Gdd^ca is correct.

The author supplied an important exact normalization
precision while this review was active. I checked
[Burgos–Goswami1712.10150v2, Proposition7.3 and equations7.2–7.3](https://arxiv.org/html/1712.10150v2):
the GS codimension-two Green current corresponds
to pi i times that current in the ordinary Deligne
form convention used here. The unit-normalized
regulator representative corresponds to2pi i S_a.
Thus the arithmetic product uses (0,2a) and has
GS representative2S_a, as the revised proof now
states. This converts the metric log-square and
the unit log consistently.

The two usual star representatives differ by the
explicit partial/barpartial homotopy above; the
arithmetic class is the same. No unconverted
Thom–Whitney product is used as an exact GS
coordinate. The displayed scalar formulas need
no further factor2.

## 3. Global cusp estimates and contraction

The gradient singularity of g is1/|w| and is
integrable on a two-dimensional fiber. Integrating
along a translation segment proves the L1
difference bound O(|P|).
For the gradient difference, disks of radius2|P|
give O(|P|), and the complement gives
O(|P|log(1/|P|)) from the Hessian1/|w|^2.
These are bounds for the actual Green function.

With P(q)=O(q^m), the horizontal coefficients
of U_a have fiberwise L1 bound
O(|q|^(m-1) times logarithmic powers).
The vertical difference has the stronger
O(|q|^m times logarithmic powers) bound.
The coefficients of aOmega_D are also locally
integrable. The cusp cutoff errors therefore
tend to zero, with the stated epsilon^m or
epsilon bounds. Unlike a1/q primitive, these
terms cannot leave a fiber delta in the
distributional limit.

The same derivative-difference estimate makes
the tangential vertical primitive tend to0
in fiberwise L1. At coarse elliptic points
the bounded invariant coefficient and its
integrable derivative powers give the
corresponding zero small-circle error.
No arbitrary singular-current pullback is used.

The global definition by(3.3) is thus legitimate,
without G times a cusp delta. It is a Deligne
current construction; the proof does not call
it convergence in an arithmetic Chow group.
The explicit Dirichlet-energy warning about
j_2 is correct and prevents an unsupported
scalar Sobolev theorem.

Finally p_*(U_a wedge omega_E)=0: its only
possible vertical term is a fiber derivative
of an integrable function, whose compact
integral against omega_E is zero.
The conjugate primitive has zero push by type.
Proper current differentiation then proves
p_*(S_a wedge omega_E)=a alpha globally,
with no new cusp contribution.

## 4. Original scalar and absolute boundary defect

The sign in(4.1) is correct:
d(lalpha)=barpartial l wedge alpha, so
i a alpha wedge barpartial l/(4pi^2 c_pi)
equals aF dmu. Its convergence follows from
the holomorphic cusp differential and the
logarithmic powers of a.

The distributional identity
partial barpartial l=-pi i sum m_c delta_c
gives
$$
 \int\partial b\wedge\bar\partial l
                =\pi i\sum_c m_c b(c).
$$
Thus the stated change is
-sum m_c b(c)/(4pi c_pi).
The proof gives an actual smooth primitive
with prescribed contraction b, so this is
an actual absolute representative ambiguity.
An unrestricted absolute Deligne class would
not determine the scalar.

The logarithmic test is closed on the open.
Its de Rham coefficient is explicitly named;
after complexification it is the indicated
degree2, twist1 Deligne test. Multiplication
and surface integration have the stated
total degrees and twists. No rational Betti
period is manufactured by this contraction.

## 5. The relative Cauchy construction

Both right sides in(5.1) are in every finite
Lp near a cusp. The conjugate Cauchy kernel
solves partial, and choosing p>2 gives
continuous W1p primitives. Subtracting u_1(0)
therefore makes sense.
Direct calculation of the two conjugate
terms in U^loc gives exactly aOmega_D:
the pure base coefficient is i a|h|^2/(2tau_2),
and the two mixed coefficients have
-i/(2tau_2), as required. The tangential
boundary primitive is zero.

The requested regularity precision is now
present in the proof. On a common smaller
disk, differences of two Cauchy solutions
satisfy the homogeneous partial equation.
They are antiholomorphic off the cusp and
continuous at it, hence extend smoothly.
The mixed coefficient has zero value, while
the base normal form restricts to zero.
The same intrinsic component equations
handle chart changes. Thus the difference
is an ordinary smooth relative Deligne
boundary, not merely a boundary in an
unverified Sobolev quotient.

Subtracting cutoff primitives kills the
representative near both B components.
The intermediate annuli are smooth, and
the analogous interior construction handles
coarse elliptic points. This constructs the
claimed smooth relative representative.
Its scalar is unchanged: u_1(0)=0,
the Holder estimate kills the boundary
circle, and Holder's inequality controls
its derivative against1/|q|.

For a general relative-exact change between
zero-boundary representatives, the boundary
primitive is Deligne-exact on each compact
E fiber. Its integral against the closed
elliptic differential is zero. Hence the
absolute defect from Section4 disappears.
This proves that the nonzero scalar detects
the particular relative class C_j2.

## 6. Actual compact motivic cup and its regulator

I read
[Déglise, Definition1.5 and Section1.6](https://deglise.perso.math.cnrs.fr/docs/2014/beijing.pdf)
for the six-functor cohomological compact-support
convention. The revised proof displays the
two composable morphisms
$$
 1_{\mathbb Q}\longrightarrow f_!1(1)[2]
                   \longrightarrow f_!1(2)[3].
$$
The first is c_D and the second is induced
by the actual unit on V^circ. This fixes the
cohomological versus homological convention
and constructs the claimed motivic product.
It does not assume the unit extends across B.

The real regulator product has normalized
form log|v| times2pi i Omega_D.
The canonical relative Chern class has zero
boundary metric. The explicit Green
homotopy and the limit log|v|G to0 fix
its boundary constants to the same zero
ones as the Cauchy construction.
With the factor2 conversion in Section2,
this proves precisely(6.2).
The product and regulator compatibilities
are those of
[Burgos–Feliu0907.5169v1](https://arxiv.org/html/0907.5169);
its source version was checked.

For the entire rational unit group, properness
of X gives div(v)=m(0-infinity).
Therefore v^(N-1)/u^m is a rational constant.
Its logarithm is a rational multiple of l
plus a constant. The constant term pairs
to0 by integral F=0, and the l term pairs
to0 by Fricke parity with absolute convergence
at both cusps. This proves the complete
scalar-Kummer image test, not just a test
of one selected unit.

## 7. Verdict and limitation

All seven sections pass after the recorded
precisions. The completed Gamma-pole term
is retained in the unpaired relative class;
only the previously proved lower scalar
pairings are zero. The weighted adjoint
is used as an independently reviewed
analytic input, without an arithmetic
converse.

The proof constructs a nonzero REAL relative
Deligne class on a rational pair. It does
not infer a rational motivic preimage from
that fact. The tested rational cup image
is too small for this scalar, and the
remaining gap RGC-389 is explicit.

Only this assigned review file was written.
No old numerical certificate was rerun.
