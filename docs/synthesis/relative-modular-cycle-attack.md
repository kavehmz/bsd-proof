# Noncuspidal relative cycles for 389a1 and the modular-path comparison

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Model: GPT-6 Astra, xhigh reasoning. The `[NEW]` constructions and
deductions below passed [independent review](review-relative-modular-cycle.md).
The objective is full BSD
over Q. No leading-term rationality, integrality, or full BSD is proved.

## 1. Concrete outcome

This note constructs a genuine rank-six relative 1-motive from the full
noncuspidal basis of 389a1. Two explicit rational functions modify its
marked divisors so that **every finite local intersection contribution
to its two-by-two height matrix is zero**. The remaining real
biextension-period matrix is exactly the full BSD height matrix.
Its determinant, multiplied by the full real period, therefore gives
the required integral period–regulator line without defining a
conjectural analytic element in that line.

The missing comparison is then tested on the actual modular cusp path.
Its image in the elliptic quotient has a closed real logarithm lift.
A specified small imaginary translate contracts in a strip avoiding
the noncuspidal punctures. Thus this natural projected-path construction
has identity holonomy at every iterated length. An additional test
shows that ordinary 1-motive transport, even after squaring the cusp
1-motive, cannot reach the top determinant of the point extension.
These are statements about the particular transport constructions,
not about all possible secondary motives or about BSD itself.

The certified analytic target remains

$$
\ell_E=\frac{L''(E,1)}2=4\pi(J''(0)-\mathcal C_E),\qquad
110<\mathcal C_E<111,
$$

with the definitions in [the eta note](higher-period-integrality-attack.md)
and [its certificate](eta-correction-certificate.md).

## 2. Actual divisors and their disjoint representatives

Use

$$
E:y^2+y=x^3+x^2-2x,\quad
\omega=\frac{dx}{2y+1},\quad
P=(-1,1),\quad Q=(0,-1),\quad O=[0:1:0].
$$

The [reviewed arithmetic model](weil-etale-lattice-attack.md) is the
regular projective cubic over Z. Every fiber is irreducible of
multiplicity one. P,Q are the certified full basis, and E(Q) has
no torsion.

Put

$$
R=P+Q=(4,8),\quad
S=R+P=(-51/25,-68/125),\quad
T=R+Q=(1/16,-9/64).
\tag{2.1}
$$

Let

$$
D_1=(P)-(O),\quad D_2=(Q)-(O),\quad
B_1=(S)-(R),\quad B_2=(T)-(R).
$$

Each D_i has support disjoint from each B_j, and [B_1]=P,
[B_2]=Q in Pic^0(E). These are actual rational divisors, not abstract
height coordinates.

**[NEW] Lemma 2.1 (explicit moving functions).** The functions

$$
f_P=\frac{x+51/25}{y-7x/5-12/5},\qquad
f_Q=\frac{x-1/16}{y-9x/4+1}
$$

satisfy div(f_P)=B_1-D_1 and div(f_Q)=B_2-D_2.

*Proof.* The denominator of f_P is the line through P and R;
its divisor is P+R+(-S)-3O. The numerator has divisor S+(-S)-2O.
Their difference is S-R-P+O. The calculation for Q,R,T is identical.
The addition formulas give the coordinates in (2.1). \(\square\)

## 3. All finite contributions can be cancelled explicitly

For rational sections A,B of the projective model, let j_p(A,B)
be their local intersection multiplicity at p. Their primitive
projective coordinates are

$$
\begin{array}{c|c}
O&(0,1,0)\\
P&(-1,1,1)\\
Q&(0,-1,1)\\
R&(4,8,1)\\
S&(-255,-68,125)\\
T&(4,-9,64).
\end{array}
$$

**[NEW] Lemma 3.1 (finite intersection matrix).** If
\(I_{ij}=\sum_p i_p(\overline D_i,\overline B_j)\log p\), then

$$
I=\begin{pmatrix}
-\log5&-\log4\\
\log3-\log5&-\log4
\end{pmatrix}.
\tag{3.1}
$$

No vertical Néron-symbol correction is required on this model.

*Proof.* For two primitive integer coordinate vectors a,b, the
intersection of their sections in projective space is defined locally
on Spec Z by their two-by-two minors. At a prime choose a coordinate
which is a unit; the minors are the coordinate differences in that
affine chart. Thus the local length is the p-valuation of the gcd
of the minors. Fiber products in the model and in projective space
agree because the model is a closed subscheme containing both sections.

The gcds are

$$
\begin{array}{c|ccc}
 &S&T&R\\\hline
P&1&1&1\\
Q&3&1&1\\
O&5&4&1.
\end{array}
$$

Expanding (P_i-O).(R+P_j-R) gives (3.1). This table also records
each prime contribution individually. Any vertical divisor is a
combination of full fibers. A degree-zero horizontal divisor has
intersection zero with each full fiber, so the vertical correction
can be chosen zero at every prime. \(\square\)

Now define

$$
h_1=1-\frac{332}{27(x-4)}+
                    \frac{1040y}{27(x-4)^2},\qquad
h_2=1-\frac{41}{3(x-4)}+
                    \frac{20y}{3(x-4)^2},
\tag{3.2}
$$
$$Z_1=B_1+\operatorname{div}_E(h_1),\qquad
Z_2=B_2+\operatorname{div}_E(h_2). \tag{3.3}$$

**[NEW] Proposition 3.2 (actual cycles with zero finite symbols).**
The divisors Z_1,Z_2 are defined over Q, have degree zero, avoid
\(A=\{O,P,Q\}\), and represent P,Q respectively. Moreover

$$i_p(\overline D_i,\overline Z_j)=0
\quad\text{for every prime p and every i,j}. \tag{3.4}$$

*Proof.* The functions are regular and nonzero at A. Their exact
values are

$$
\begin{array}{c|ccc}
 &O&P&Q\\\hline
h_1&1&5&5/3\\
h_2&1&4&4.
\end{array} \tag{3.5}
$$

At O both nonconstant terms in (3.2) tend to zero, as their orders
there are positive. The other values follow by substitution.
The possible poles x=4 lie at R and -R, neither in A. This proves
the support assertion; principality proves degree and Picard class.

For any rational function h regular and nonzero on the generic
support of D_i,

$$
i_p(\overline D_i,\operatorname{div}_{\mathcal E}h)
=v_p(h(P_i)/h(O)).
$$

The closure of div_E(h) may differ from div_model(h) by a vertical
divisor, including primes in the denominators of (3.2). Such a divisor
is a combination of full fibers and has zero intersection with D_i.
Hence the same formula applies to the closure of the generic divisor.

The valuations of (3.5) are exactly the negatives of the local
entries in Lemma 3.1: 5 cancels -log5, 4 cancels -log4, and 5/3
cancels log3-log5. This cancellation is prime by prime, proving
(3.4). \(\square\)

The functions h_j were constructed from finite section intersections
alone. No canonical height or L-value was used to choose their
coefficients, so this is not a normalization that assumes BSD.

## 4. The relative 1-motive and its integral realizations

Let \(G=J(E,A)\) be the generalized Jacobian for the reduced modulus
A. It is the semiabelian extension

$$0\longrightarrow(\mathbb G_m^A/\mathbb G_m)
\longrightarrow G\longrightarrow E\longrightarrow0,$$

with torus character lattice
\(X=\operatorname{Div}^0(A)=\mathbb Z D_1\oplus\mathbb Z D_2\).
Define the actual 1-motive over Q

$$
M=[L\longrightarrow G],\qquad
L=\mathbb Z e_1\oplus\mathbb Z e_2,
\quad e_j\longmapsto\operatorname{AJ}_A(Z_j).
\tag{4.1}
$$

The marking is defined by the explicit rational cycles (3.3). Its
abelian projection sends e_1 to P and e_2 to Q. Thus both X, via
Pic^0(E), and L map to the full integral Mordell–Weil lattice.
Here the 1-motive is defined over Q and has an integral marking and
Betti lattice; no smooth semiabelian extension over every prime of
Spec Z is being asserted. The finite-place contributions were instead
handled on the explicit regular model in §3.

**[THEOREM, realization used]** The generalized-Jacobian construction
of a punctured marked curve and its Betti/de Rham realization are
spelled out in Sertöz–Ouaknine–Worrell,
[arXiv:2505.20397v1](https://arxiv.org/html/2505.20397v1),
Definition 6.1.10, §4.1, and Proposition 6.5.43; they are the usual
Deligne 1-motive realizations. The finite sets and the marking in
(4.1) are Galois stable over Q, so the algebraic construction descends
to Q. No use of that paper's transcendence algorithm is made here.

More explicitly, let B* be the geometric support of Z_1 and Z_2.
It is finite and disjoint from A. The Betti lattice is the pullback

$$
H_{\mathbb Z}=\{(\gamma,n_1,n_2):
 \gamma\in H_1(E(\mathbb C)\setminus A,B^*;\mathbb Z),
\ \partial\gamma=n_1Z_1+n_2Z_2\}.
\tag{4.2}
$$

**[NEW] Lemma 4.1 (ranks and weights).** H_Z is free of rank six,
with weight-graded ranks two, two, two in weights -2,-1,0:

$$
\operatorname{gr}_{-2}^W H=X^\vee\otimes\mathbb Z(1),\quad
\operatorname{gr}_{-1}^W H=H_1(E,\mathbb Z),\quad
\operatorname{gr}_0^W H=L.
\tag{4.3}
$$

*Proof.* A torus punctured at three points has first homology free
of rank 2+3-1=4. Its kernel on mapping to H_1(E) is generated by
two puncture loops, the third being minus their sum. Relative
homology adds the prescribed two-dimensional boundary lattice L.
Every degree-zero integral divisor is the boundary of an integral
chain on the connected punctured curve; hence this is an extension
of L by that rank-four homology. Both groups are free. The usual
weight filtration gives weight -2 to puncture loops, -1 to compact
homology, and zero to relative endpoints, yielding (4.3). \(\square\)

Before the rational principal modifications, the same construction
uses A={O,P,Q}, B={R,S,T}, and the rank-six group H_1(E\A,B;Z).
The modifications in (3.3) are genuine torus/Kummer changes of the
marking. In torus coordinates dual to D_1,D_2 their values are
\((5,5/3)\) and \((4,4)\), as computed in (3.5).

## 5. An exact period formula for the full height matrix

Use standard counterclockwise residues. The algebraic third-kind
differentials are particularly simple:

$$
\rho_1=\frac{y+2}{x+1}\omega,\qquad
\rho_2=\frac yx\omega. \tag{5.1}
$$

**[NEW] Lemma 5.1.** rho_i has residue +1 at P_i, residue -1 at O,
and no other poles, where P_1=P,P_2=Q.

*Proof.* Put Y=2y+1. For a point (a,b), the differential
\((Y+(2b+1))dx/(2(x-a)Y)\) has residue +1 at that point; its apparent
pole at its inverse cancels. At O, using x=t^(-2)+O(t^(-1)) and
Y=-2t^(-3)+O(t^(-2)), its leading term is -dt/t. Substituting P
and Q gives (5.1). \(\square\)

Choose a symplectic basis a,b of H_1(E,Z) with periods
\(\omega_1=\int_a\omega>0\), \(\omega_2=\int_b\omega\), and
\(\tau=\omega_2/\omega_1\). Because E has two real components, the
basis may be chosen rectangular, so \(\tau=i t_0\), t_0>0.
Set \(\omega_0=\omega/\omega_1\). Lift a,b off A and define

$$
A_i=\int_a\rho_i,\quad B_i=\int_b\rho_i,\quad
c_i=\operatorname{Re}A_i-i\frac{\operatorname{Re}B_i}{t_0},
\qquad \eta_i=\rho_i-c_i\omega_0.
\tag{5.2}
$$

The real parts in (5.2) do not depend on moving the cycles around
punctures, since such moves add integral multiples of 2 pi i.

**[NEW] Proposition 5.2 (the regulator has been realized).** Let
\(\gamma_j\) be any integral chain in E\A with boundary Z_j. Then

$$
H_{ij}:=h_{\rm BSD}(P_i,P_j)
=\operatorname{Re}\int_{\gamma_j}\eta_i.
\tag{5.3}
$$

Equivalently, writing
\(v_j=\int_{\gamma_j}\omega_0\),
\(C_{ij}=\int_{\gamma_j}\rho_i\),

$$H_{ij}=\operatorname{Re}(C_{ij}-c_i v_j),\qquad
\operatorname{Reg}_{\rm BSD}(E)=\det H. \tag{5.4}$$

*Proof.* Equation (5.2) makes both a- and b-periods of eta_i purely
imaginary: their real parts are respectively Re A_i-Re c_i=0
and Re B_i-Re(c_i i t_0)=0. The small-loop periods are 2 pi i
times its integral residues, so all periods are purely imaginary.
Uniqueness follows because a holomorphic differential with both
periods purely imaginary is zero when Im tau is nonzero.

Thus \(g_i(z)=-\operatorname{Re}\int^z\eta_i\), up to an irrelevant
constant, is the degree-zero Néron Green function at the real place.
It has local singularity -log|t| and satisfies
\(g_i(\operatorname{div}h)=-\log|h(D_i)|\); this fixes the sign and
the single-log normalization. Its value on Z_j is
\(-\operatorname{Re}\int_{\gamma_j}\eta_i\), independent of the
chosen chain.

Faltings–Hriljac gives the negative global Néron symbol as the
canonical height pairing. Every finite symbol is zero by Proposition
3.2. Hence the negative real symbol is precisely (5.3).

For the exact height convention, use Müller,
[arXiv:1105.1719v3](https://arxiv.org/html/1105.1719),
Definitions 2.3, 2.6 and 3.1, Proposition 2.8, and Theorem 3.2. In genus one his
canonical height is \(\lim4^{-n}h_x(2^nP)\), with polarization divided
by two, exactly the BSD convention used in our certificate. In
Gillet–Soulé squared-norm notation the Green current is 2g_i and
the archimedean intersection has its factor one-half; this gives
the same symbol, not another factor of two. \(\square\)

Without the principal modifications, put
\(S_{ij}=\operatorname{Re}\int_{R}^{R+P_j}\eta_i\). Then the same
proof yields H=S-I. Equation (3.5) adds exactly -I to the period
matrix. The finite corrections have therefore been represented by
actual rational Kummer data, not suppressed as an unspecified unit.

**[THEOREM, biextension interpretation]** The framed rank-one
subquotients selected by D_i and Z_j are the relative-curve
biextensions, with weights -2,-1,0. Their invariant Poincaré metric
and their real-normalized period formula are related by Hain's
theorem as presented in Amini–Bloch–Burgos Gil–Fresán,
[arXiv:1512.04862v2](https://arxiv.org/abs/1512.04862v2),
[author PDF §§4.1–4.4](https://www.math.ens.psl.eu/~amini/Publications/Feynman.pdf),
Theorems 4.10–4.11 and Proposition 4.12. That source uses a boundary
orientation for residues; our sign is instead fixed explicitly by
the Green/principal-divisor normalization in the proof above.
Taking the appropriate dual Deligne-pairing line gives degree H_ij.
No signed source convention is transferred without this check.

## 6. The integral determinant line and its weight

Let \(\gamma_{\mathbb R}\) be the sum of the two real components
oriented by omega; it is 2a in the rectangular basis. Thus
\(\int_{\gamma_{\mathbb R}}\omega=\Omega_E=2\omega_1\), the full
real period. Define the rank-one integral module

$$
\mathscr D_{\mathbb Z}
=\det X\otimes\det L\otimes\mathbb Z\gamma_{\mathbb R}
                         \otimes\mathbb Z\omega.
\tag{6.1}
$$

The factor \(\mathbb Z\gamma_{\mathbb R}=\mathbb Z(2a)\) has index
two in \(H_1(E,\mathbb Z)^+\). It is the specified full-period
lattice, not a primitive Betti lattice; only the two point lattices
are claimed saturated below.

**[NEW] Proposition 6.1.** The period–regulator map defined by the
actual pairings (5.3) sends

$$e=(D_1\wedge D_2)\otimes(e_1\wedge e_2)
           \otimes\gamma_{\mathbb R}\otimes\omega$$

to \(\Omega_E\operatorname{Reg}_{\rm BSD}(E)\). This image is
strictly positive and the point lattices in (6.1) are saturated.

*Proof.* The determinant of the bilinear period pairing on X and L
is det H, by Proposition 5.2. Multiply by the displayed period.
The two point maps identify their bases with the already certified
full Mordell–Weil basis, and the real Néron–Tate pairing is positive
definite. The real-component factor two has been retained in (6.1).
\(\square\)

The degree of this operation should not be confused with one
biextension height. M has weights -2,-1,0. Its exterior square has
weights from -4 through zero, with top determinant det L and bottom
\(\det(X^\vee)\otimes\mathbb Z(2)\). The determinant in (5.4) is
quadratic in the real height matrix, a weight-drop-four operation.
It is not the linear height of an ordinary single rank-one
biextension. Nor is it obtained by multiplying ordinary K_0 classes
and discarding extension/metric data.

One may equally retain the four actual dual metrized Deligne-pairing
lines of D_i,Z_j and form the alternating tensor of their degrees.
Their integral line modules do not force the resulting real scalar,
or its ratio to another period, to be rational. Equation (6.1)
specifies the target lattice; it does not place the analytic leading
coefficient in it by definition.

## 7. Carrying the construction back to the modular curve

Let \(\pi:X_0(389)\to E\) be the rational modular parametrization
of degree d=40, with pi(infinity)=O, and retain its differential
factor \(\pi^*\omega=c_\pi\,2\pi i f(z)dz\),
\(c_\pi\in\mathbb Q^\times\). Its precise value is not needed
for the following zero and degree assertions; it is not replaced
by a guessed unit in a leading-term formula.

The divisors pi^*D_i and pi^*Z_j are actual rational divisors on
X_0(389) with disjoint supports between the two sets. Choose a chain
\(\widetilde\gamma_j\) in \(X_0(389)\setminus\pi^{-1}(A)\) with
boundary pi^*Z_j. Such chains exist because that boundary has degree
zero and avoids the removed points. Then

$$
\operatorname{Re}\int_{\widetilde\gamma_j}\pi^*\eta_i
=40H_{ij}. \tag{7.1}
$$

**[NEW] Proof of (7.1).** The boundary of its pushforward is
pi_* pi^*Z_j=40Z_j, including ramification multiplicities. Subtract
40gamma_j. The difference is a closed chain in E\A, whose eta_i
period is purely imaginary. Taking real parts and applying (5.3)
proves the formula. \(\square\)

This realizes the nonzero height matrix using genuine modular
noncuspidal divisors and pulled-back algebraic forms. Its determinant
has the expected factor 40^2. Dividing by 40 in an integral argument
would introduce primes two and five; (7.1) by itself gives no
permission to ignore those indices.

## 8. Testing the actual relative cusp path, including iterated holonomy

Let gamma_mod be the imaginary-axis path from the cusp infinity to
the cusp zero. In the elliptic uniformization its logarithm lift is

$$
F(y)=c_\pi\int_{i\infty}^{iy}2\pi i f(z)dz\in\mathbb R.
\tag{8.1}
$$

Cusp decay makes it continuous at y=0 and y=infinity. The exact
vanishing L(E,1)=0 gives

$$F(0)=F(\infty)=0.$$

Both P,Q lie in the nonidentity real component (use the three real
roots in the certificate). With a rectangular lattice
\(\Gamma=\omega_1\mathbb Z+i b\mathbb Z\), b>0, their lifts have
imaginary part b/2 modulo b; lifts of O have imaginary part zero
modulo b.

**[NEW] Proposition 8.1 (the specified projected loop has trivial
holonomy at every length).** For any 0<epsilon<b/2 define the closed
loop in E\A by

$$\gamma_\epsilon(y)=F(y)+i\epsilon\pmod\Gamma.$$

It is nullhomotopic in E\A. Consequently every flat connection on
E\A has identity holonomy on it. In particular all positive-length
word coefficients of the universal unipotent connection formed from
holomorphic one-forms on E\A are zero.

*Proof.* The strip 0<Im z<b/2 contains no lattice translate of A.
The explicit based contraction

$$H(s,y)=(1-s)F(y)+i\epsilon\pmod\Gamma,
\qquad0\le s\le1,$$

stays in that strip and fixes both endpoints at i epsilon. This is
a contraction of the loop in the punctured curve. Flat holonomy is
homotopy invariant. For holomorphic one-forms on a complex curve,
their exterior derivatives and pairwise wedges are zero, so the
universal finite unipotent connections are flat. Their independent
word coefficients are the corresponding Chen integrals, proving
the final assertion as well. \(\square\)

If a base point R is desired, conjugate by any connector from R to
i epsilon; the conjugated loop is still nullhomotopic. The limit
of this family specifies one regularization at O. Other indentation
or tangential choices must be specified separately and may append
local monodromy; no assertion about every possible regularization
is being made.

This tests more than the degree-one cusp projection. For example the
algebraic connection with strictly upper-triangular entries rho_1,
rho_2 is flat on E\A because these holomorphic one-forms are closed
and their wedge is zero. Its second iterated coefficient, and every
coefficient in the universal finite unipotent truncations, vanishes
on gamma_epsilon. Thus replacing the Mellin logarithms by these
noncuspidal period letters on the projected path gives zero, whereas
the certified second central coefficient is positive.

The statement concerns connections descended to this punctured
elliptic curve and this specified path. A construction on X_0(389)
retaining additional modular, boundary, or higher-extension data is
not covered by this contraction argument.

## 9. A further test: ordinary 1-motive transport and its square

The preceding failed path comparison might be replaced by an
algebraic morphism of relative motives. This proposal can also be
tested precisely.

Let

$$M_c=[\mathbb Z\longrightarrow J_0(389)],\qquad
1\longmapsto[0-\infty].$$

The cuspidal class is torsion: the rational modular unit
Delta(z)/Delta(389z) has divisor 388(0-infinity). Let
\(M_0=[L\to E]\) be the quotient of (4.1) by its torus.

**[NEW] Lemma 9.1.** Any morphism of 1-motives from M_c to M_0
has zero lattice map. The same is true for a map to M followed by
the torus quotient.

*Proof.* If 1 maps to (m,n), compatibility with the abelian map
requires the image of the torsion cuspidal class to equal mP+nQ.
Independence of P,Q implies m=n=0. The argument also applies
after tensoring with Q. \(\square\)

**[NEW] Proposition 9.2 (squaring the ordinary cusp motive is still
insufficient).** No morphism of rational mixed Hodge structures

$$H(M_c)^{\otimes2}\longrightarrow\bigwedge^2H(M)$$

is nonzero on the weight-zero determinant line of the target.

*Proof.* Since the point defining M_c is torsion, its rational
Hodge structure splits as \(H_1(J_0(389),\mathbb Q)\oplus\mathbb Q(0)\).
Its tensor square therefore has a weight-zero direct summand Q(0),
and all remaining summands have strictly negative weights.

Consider the weight-at-least-minus-one quotient of the target. It
is an extension of \(\det L_{\mathbb Q}=\mathbb Q(0)\) by
\(H_1(E,\mathbb Q)\otimes L_{\mathbb Q}\). Its extension class is

$$[P]\otimes e_2-[Q]\otimes e_1. \tag{9.1}$$

To verify this, choose lifts v_1,v_2 of the two lattice generators.
Changing their splittings by the two point-extension cocycles
h_1,h_2 changes v_1 wedge v_2 modulo weight at most -2 by
h_1 tensor e_2-h_2 tensor e_1. This is exactly (9.1). The torus
and the principal modifications in §3 affect only lower weights,
so they do not alter this class.

The point extension of a nontorsion elliptic point is nonzero over
Q: its Hodge class is its elliptic logarithm modulo rational periods;
vanishing would mean a rational combination of periods, and clearing
denominators would make the point torsion. Thus (9.1) is nonzero;
its two components in the displayed L-basis cannot cancel.

A morphism nonzero on weight zero would restrict to the Q(0)
direct summand in the source and split this nonzero extension,
after dividing by its nonzero rational scalar on the one-dimensional
top quotient. That is impossible. \(\square\)

This tests the natural quadratic repair to Lemma 9.1. It does not
exclude a genuinely higher Mellin-decorated source extension, whose
top piece need not split as it does for M_c. In particular no
claimed nonexistence of a BSD motive is inferred.

## 10. Exact remaining comparison

The construction has supplied the integral outer lattices, actual
relative cycles, explicit algebraic differentials, exact finite
corrections, and a regulator map with value Omega_E Reg_BSD. It has
not supplied an analytic class in that lattice.

**[GAP RM-389]** Construct from the fixed modular form and its
relative cusp path a higher/secondary relative object and an exact
comparison to the determinant line (6.1), producing an integral
element z with

$$\theta_M(z)=4\pi(J''(0)-\mathcal C_E).$$

The construction must retain enough extra data to avoid the explicit
contraction and weight-zero splitting tests in §§8–9. It must identify
the full real period cycle and the two saturated point lattices of
(6.1), rather than defining z by applying the inverse real regulator
map to the desired value. Such a definition over R would simply
assume the rationality/integrality statement being sought.

The natural attempts made here were actual projected-path holonomy,
ordinary relative 1-motive transport, and its tensor square. Each has
been pushed through a precise comparison and fails as described.
The nonzero target point construction remains available for a more
substantial higher comparison. Solving this test-curve comparison
would still not prove full BSD for all elliptic curves over Q.

## 11. Verification and handoff

The exact rational group law, section-minor gcds and evaluations in
(3.5) are elementary finite computations. Their reproduction is:

```sh
python3 - <<'PY'
from fractions import Fraction as F
from math import gcd
from functools import reduce
pts={'O':(0,1,0),'P':(-1,1,1),'Q':(0,-1,1),
     'R':(4,8,1),'S':(-255,-68,125),'T':(4,-9,64)}
for a in ('P','Q','O'):
    for b in ('S','T','R'):
        v,w=pts[a],pts[b]
        print(a,b,reduce(gcd,(abs(v[i]*w[j]-v[j]*w[i])
                              for i,j in ((0,1),(0,2),(1,2)))))
for x,y in ((F(-1),F(1)),(F(0),F(-1))):
    print(1-F(332,27)/(x-4)+F(1040,27)*y/(x-4)**2,
          1-F(41,3)/(x-4)+F(20,3)*y/(x-4)**2)
PY
```

No old certificate was rerun. No numerical equality to an L-value was
used. The independent review checked the real-place height sign
and factor, prime-by-prime principal-divisor cancellation, the integral
relative lattice, the precise path regularization, and the nonzero
extension class in Proposition 9.2. It retained the index-two Betti
sublattice and puncture-avoidance clarifications. Only this file and
[its checkpoint](relative-modular-cycle-checkpoint.md) were edited.
