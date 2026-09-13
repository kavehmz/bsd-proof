# Arithmetic theta pairings, their actual domain, and the second spectral test

Date: 2026-09-12. Owner: root/coordinator. Completed bounded construction.
All eight sections passed [independent review](review-theta-doubling-arithmetic.md),
including the additional Poisson construction after its sign correction.
Restart: [checkpoint](theta-doubling-arithmetic-checkpoint.md).
Full BSD remains the objective and is neither proved nor disproved.

## 1. Completed input and the arithmetic product being tested

Keep N=389, X=X0(N), Y=X minus its two cusps, and the exact input
F=y²f conjugate(g), g=(2pi i)^(-1)dlog(N^(-6)Delta(z)/Delta(Nz))/dz.
Write F_R=ReF and H=I_L(F). The [reviewed weighted adjoint](weighted-theta-adjoint-attack.md)
proves

    <H,Ecal_L(bar s)> = -sqrtN/pi²*s(s-1)xi(s) int F J_N(s),
    M=-pi²/(2sqrtN)<H,Ecal_L''(1)> !=0.

The task here is an arithmetic realization of this SAME pairing.
The actual arithmetic height kernel <phi_hat(tau),phi_hat(w)> is
well-defined coefficientwise in the source arithmetic Chow theory.
A genus-two arithmetic degree series is also available by SSY.
Equality of its diagonal restriction with that height kernel is NOT
assumed. The source's superconnection Green functions, singular
Fourier coefficients, arithmetic degree and stabilizer conventions
must be compared before such an identification can be used.

Primary sources inspected in this task:

- Du–Yang1702.07917v2 (52pages), the existing kernel, curvature and
  arithmetic decomposition formulas.
- [Du2412.00688v1](https://arxiv.org/pdf/2412.00688v1),75pages,
  Theorems0.10–0.11 and3.2, Propositions3.4,3.9. These arithmetic
  lifts and the inner-product theorem use HOLOMORPHIC cusp forms.
- [Alfes1209.5197v2](https://arxiv.org/pdf/1209.5197v2), Theorem5.1,
  especially its k=0 proof on printed pp.24–25.
- [SSY, the45-page revision](https://home.cc.umanitoba.ca/~sankaras/ArithSW-rev1.pdf),
  §§2.3–2.5. It constructs an actual intersection product and genus-two
  cycles; its nondegenerate indefinite Green form is a superconnection
  integral, not a claimed uncorrected product of two genus-one Greens.

The older Kudla division-Shimura-curve result gives a partial diagonal
identity at t1*t2 nonsquare and a unary-theta ambiguity. Its stated
scope is not silently substituted for this full modular-curve problem.

## 2. The actual nonzero input has zero holomorphic cusp projection

**[THEOREM, primary kernel statement]** The k=0 proof of Alfes5.1
establishes, for a holomorphic cusp form b of weight3/2 in the same
Weil representation,

    <Theta_KM(tau,z),b(tau)>_Pet=0

for each fixed z. Although the theorem's headline concerns a class
of weakly holomorphic lifts, this fixed-z identity is proved INSIDE
its proof: the opposite kernel lift is annihilated by the weight-zero
Laplacian, tends tozero at each cusp, and hence iszero. Du3.4 uses
precisely that kernel identity. There is no assumption that our F
is a harmonic Maass form.

**[NEW] Proposition2.1.** For every such holomorphic cusp b,

    <H,b>_Pet=0.

Consequently the holomorphic cuspidal projection of H is zero, while
H itself is nonzero by the completed weighted adjoint.

*Proof.* In a bounded-x source cusp strip of height y, the positive
majorant bound from the reviewed adjoint gives, for v bounded below,

    sum_A |(v p_A²-1/(2pi)) exp(-pi v q_z(A))|
        <= C(1+y/sqrt(v))³.

It includes A=0 here. All norms are on the same fixed rank-three
lattice, with constant depending on N. The coefficients of b decay
exponentially at the only cusp of the metaplectic fundamental domain.
F decays exponentially in y at both source cusps. The displayed
polynomial bound therefore makes the DOUBLE absolute integral,
with both hyperbolic measures and v^(3/2), finite. On the two compact
cores smoothness gives the remaining bound. Fubini now gives

    <I_L(F),b> = int_Y F(z)<Theta_KM(tau,z),b>_Pet =0.

This proves the claim without replacing F by a different modular
form. The known nonzero pairing with Ecal_L'' shows H is notzero. ∎

Thus applying a cusp-only arithmetic inner-product theorem to a
holomorphic projection of H would lose the original nonzero value.
This rules out that SPECIFIC substitution. It does not rule out
an arithmetic operation on its nonholomorphic spectral component.

## 3. An actual Sobolev arithmetic class for the fixed forcing

The earlier claim of a single SMOOTH Gillet–Soulé class a(2F_R)
was correctly withdrawn. At a cusp it has leading term

    F_R=(1-N)Re(q)log²|q|/(4pi²)+O(|q|²log²|q|),

so it is not even C1 there. Nevertheless it has finite Dirichlet
energy. This permits a different actual arithmetic category.

**[THEOREM, exact category]** [Bost1999](https://www.numdam.org/article/ASENS_1999_4_32_2_241_0.pdf),
§§5.1–5.3, defines an arithmetic Chow group and intersection pairing
on any integral normal projective arithmetic SURFACE using Green
functions which, after their algebraic logarithms, lie in W^(1,2).
The star-integral extension is defined by(5.4); the pointwise product
of two arbitrary distributional Green currents need not exist.
Section5.5 has a version with real divisor coefficients, distinguished
from simply tensoring the earlier group withR. No stack extension
is assumed here.

Choose the actual fine modular curve C=X1(5N) overQ, and the
forgetful map h:C→X0(N) taking a point of order5N to its cyclic
N-subgroup. Its generic degree is

    d=12(N-1)=4656.

Indeed each generic cyclic N-subgroup has N-1 generators, each lifts
to24 points with nonzero5-part, and the target's automorphism -1
identifies opposite choices. Equivalently this is the effective
congruence-subgroup index. C has no elliptic stabilizers in its
complex uniformization. Take an integral normal projective arithmetic
model of C (a projective closure followed by normalization suffices).
Bost's scheme theorem applies on that model. This step does not
assert smoothness of all its bad fibers or an arithmetic stack theorem.

**[NEW] Proposition3.1.** The actual metrized trivial line

    A_F=(0,2h^*F_R)

defines a Bost arithmetic class. For each chosen actual theta divisor
coefficient, pull back its generic divisor and Green function to C
and extend the divisor by its closure on the model. It defines a
Bost class Z_C; vertical choices do not affect A_F·Z_C. The normalized
coefficientwise pairing is the old cutoff limit, and their scalar
series is exactly H=I_L(F).

*Proof.* At a source cusp |dF_R|=O((1+|log r|)²)|dq|, r=|q|.
Hence its squared gradient has integral bounded by a constant times
int_0^epsilon r(1+|log r|)^4 dr, which is finite and tends tozero.
The function itself is continuous and square-integrable. On an
elliptic uniformizing chart it is smooth. Pullback to C removes those
orbifold charts and preserves finite conformal Dirichlet energy;
the change-of-variable identity multiplies that energy by d.
Finite cusp ramification does not change finiteness. Thus h^*F_R
is a real conjugation-invariant W^(1,2) function on the compact C.

The source Green coefficients have their prescribed point and cusp
logarithms. After those are subtracted, their only additional cusp
singularity is loglog; its squared gradient has integral bounded
by int_0^epsilon dr/(r log²r), which is finite. On C the other
remainders are smooth. Their generic divisors and pulled-back
Green singularities match, so closure gives the asserted Bost classes.
Changing a vertical divisor contributes no intersection against the
pure metric A_F. We do not assert a canonical vertical extension or
convergence of a whole formal theta series inside the Chow group.

The earlier smooth cutoffs pull back to functions converging to
h^*F_R in W^(1,2). The derivative-of-cutoff term at a cusp has
squared norm O(epsilon²(1+|log epsilon|)^4); the ordinary removed
gradient and L2 norms also tend tozero. Elliptic-point cutoffs, if
retained, have the positive-power bounds already proved in the
projection note. Bost(5.4) makes intersection with each fixed Green
coefficient continuous in this norm. For each smooth cutoff the
metric intersection equals one-half its integral against curvature.
The explicit2 cancels the one-half. Dividing by d and passing to
the established pairing limit gives the desired source integral.
The generic cover degree is retained; no extra central-stabilizer
factor is inserted. Equality with the analytic scalar series H is
coefficientwise through the source curvature identity and the already
proved convergence of I_L(F). ∎

In this category the fixed forcing therefore has an ACTUAL arithmetic
class, rather than only a sequence of smooth classes. The earlier
smooth-class withdrawal remains correct: these are different groups.
The metric is fixed by F, not chosen from M. This still does not
make it a rational motivic regulator or a point determinant.

Its normalized self-intersection is

    d^(-1) A_F² = -1/(2pi) int_X |grad(F_R)|² dxdy <0,

where the Dirichlet integral is conformally invariant. This follows
from the pure metric star formula and Sobolev integration by parts.
F_R is nonconstant by its cusp expansion. Thus the class is nonzero;
its point projection is neverthelesszero, since its finite divisor iszero.

## 4. The scalar second spectral jet does not belong to this category

**[NEW] Proposition4.1.** Neither j1 nor j2 is a Bost Green function
for any finite divisor on the compact modular curve, even after adding
any fixed linear combination of cusp logarithms. The same holds for
the fully Gamma-completed second coefficient.

*Proof.* In the width-one infinity cusp, the leading y^s term of
J_N(z,s)=b_N(s)E_infinity(z,s) gives

    j1=b_N(1)y log y+O(y)+O((log y)²),
    j2=b_N(1)y(log y)²/2+O(y log y)+O((log y)³),
    b_N(1)=pi(N²-1)/6 !=0.

The Fourier remainder and its fixed derivatives are exponentially
smaller; these expansions follow by differentiating the explicit
constant term. A Green function's algebraic cusp logarithm can only
subtract a constant multiple of y. The remaining y-derivative of
j1 grows as a nonzero multiple of log y, and that of j2 as a nonzero
multiple of(log y)². Their Dirichlet energies contain respectively
int^infinity(log y)²dy and int^infinity(log y)^4dy, both divergent.
Adding lower Gamma coefficients cannot cancel the leading y(log y)²
term. Away from the cusp these functions are smooth, so a divisor
supported elsewhere cannot remove this local failure. ∎

The original pairing with F still converges because F is exponentially
small. It is therefore incorrect to infer a Bost class a(j2), or an
arithmetic intersection of two such classes, merely from that scalar
convergence. A hyperbolic Green inverse and its meromorphic spectral
pole require a separate regularization and arithmetic source. The
relative mixed-form construction being developed in the separate
radial-graph note has a different degree and domain; Proposition4.1
does not exclude it.

## 5. A stronger theta bound and an extended adjoint

The next argument uses an ACTUAL Poisson potential of F rather than
assuming a full genus-two product identity. We first need a bound
stronger than the pointwise estimates in the preceding adjoint note.
Write volY=pi(N+1)/3 and theta for the scalar density of the kernel.

**[NEW] Lemma5.1.** Uniformly for tau=u+iv in the standard fundamental
domain with v>=1,

    int_Y ||theta(tau,z)+e0/(2pi)|| dmu_z <= C v^(-1/2).

*Proof.* On a compact source core, the nonzero-vector Gaussian sum
is exponentially small in v. In each bounded-x cusp strip, for
y<=sqrt(v), the positive majorant gives the bound
C exp(-cv/y²). Its integral with dy/y² is O(v^(-1/2)).

For y>=sqrt(v), apply Poisson summation in the a-coordinate of the
ACTUAL lattice. Here is a direct absolute-value check. Put
b'=b-cx and a'=a-2Nbx+Ncx². Then

    q_z(A)=a'²/(Ny²)+Nc²y²+2Nb'²,
    Q(A)=ca'-Nb'²,
    p_A²=(a'+Ncy²)²/(Ny²).

The Fourier transform of the a'-Gaussian polynomial has factor
-(Ny²/v)^(3/2)(m-cu+icv)². Its exponential, together with the
remaining c-Gaussian, has modulus
exp(-piNy²|m-c tau|²/v). The b'-Gaussian sum is uniformly bounded
for v>=1. The term m=c=0 is zero. Since the lattice Z+tau Z has
uniform separation for v>=1, its remaining polynomial-Gaussian
sum is bounded by C exp(-cy²/v) in this region. Thus

    ||theta(tau,z)|| <= C(y/sqrt(v))³ exp(-cy²/v).

Its tail integral is O(v^(-1/2)), as is the tail integral of the
added constant. The second cusp follows by the actual Fricke
lattice symmetry. These bounds prove the assertion. ∎

**[NEW] Corollary5.2.** Suppose h is bounded, smooth on Y and has
zero hyperbolic integral. Then I_L(h)=O(v^(-1/2)). Its ordinary
Petersson pairing with Ecal_L(bar s) converges in the strip
0<Re(s)<1, away from poles of the Eisenstein family, and satisfies

    <I_L(h),Ecal_L(bar s)> = r_N(s) int_Y h J_N^+(s)dmu,
    r_N(s)=-sqrtN/pi²*s(s-1)xi(s).                         (5.1)

*Proof.* Exact mean zero removes the constant lattice vector, so
Lemma5.1 gives the asserted bound. The two constant-term powers
of the weight3/2 Eisenstein series are v^((s-1)/2) and v^(-s/2).
Together with v^(3/2)dmu_tau and the new bound, both are integrable
at infinity exactly in the indicated strip. Nonconstant terms
are exponentially smaller; on compact tau-sets there is no problem.

Approximate h by compactly supported smooth h_R of exact mean zero:
cut it off at both cusps and subtract a multiple of one fixed compact
bump of nonzero integral. The multiples tend tozero and the h_R are
uniformly bounded. Their theta pairings obey the SAME v^(-1/2)
bound, and converge pointwise to I_L(h). The previously reviewed
adjoint applies to each h_R. Dominated convergence in the strip,
and integrability of J_N(s) in hyperbolic measure there, pass that
identity to h. This proves (5.1) without unfolding a nonconvergent
Poincare series in that strip. ∎

## 6. The canonical Poisson potential and its vanishing cusp constants

Define q_F to be the real solution

    dd^c q_F = F_R dmu,      int_Y q_F dmu=0.              (6.1)

This normalization uses the intrinsic hyperbolic measure. It is not
chosen from the desired Mellin value.

**[NEW] Proposition6.1.** The solution exists, is unique, belongs to
W^(1,2) on the compact curve, and is smooth on Y. It is Fricke even
and conjugation invariant. At both cusps it has a common constant
value q_c and an error O(y exp(-cy)), with the same type of bound
for fixed hyperbolic-coordinate derivatives. In fact q_c=0.

*Proof of existence and preliminary regularity.* Let
alpha_0=f(z)dz and beta_0=g(z)dz. Then
F_R dmu=Re((i/2)alpha_0 wedge conjugate(beta_0)). At a cusp,
write alpha_0=a(q)dq and beta_0=(b_-1/q+b_hol(q))dq, with both
holomorphic coefficients regular there. Let A'=a, B'=b_hol and
A(0)=B(0)=0. The explicit single-valued real local potential is

    pi Re( conjugate(b_-1) A(q) log|q|²
                                + A(q) conjugate(B(q)) ). (6.2)

Applying dd^c=i/(2pi)partial bar-partial gives exactly the above
real two-form. Its possible Dirac term vanishes because A(0)=0.
It is O(|q|log|q|) with finite Dirichlet energy. Subtract dd^c of
cutoff versions of these local potentials from F_R dmu. The remainder
is a SMOOTH real two-form on the compact curve and has integralzero.
The usual compact Green operator supplies a smooth potential for that
remainder. Adding back (6.2), then fixing the mean in (6.1), proves
existence and the stated local expansion. Its hyperbolic mean exists
because it is bounded. A distributionally harmonic difference on the
compact curve is constant, so normalization gives uniqueness.

The equations and normalization are invariant under Fricke and real
conjugation; uniqueness gives those invariances. In particular the
values at the two cusps agree. Subtracting their common value leaves
an exponentially decreasing function in the hyperbolic cusp coordinates.

*Proof that q_c=0.* Put M_F(s)=int F_R J_N(s)dmu. The earlier
conjugation and Mellin identities give the SAME scalar as int FJ_N,
and

    M_F(1+t)=M t²+O(t³).                                  (6.3)

For 0<Re(s)<1, integration by parts gives

    int q_F J_N(s)dmu = +4pi/[s(s-1)] M_F(s).              (6.4)

Indeed dd^c J_N=+s(s-1)J_N dmu/(4pi). All boundary terms vanish:
the constant terms of J_N have powers y^s and y^(1-s), whose
normal derivatives tend tozero in that strip, whereas the derivatives
of q_F are exponentially small. The two integrals converge absolutely.
Combining Corollary5.2 with (6.4) gives the meromorphic continuation

    P_F(s):=<I_L(q_F),Ecal_L(bar s)>
                =-4sqrtN/pi * xi(s) M_F(s).               (6.5)

By (6.3) it is regular at s=1 and vanishes there.

There is an independent explicit test for its possible pole. The
arithmetic degree formula and the zero coefficient of the ACTUAL
theta series give

    I_L(1) = -volY/(2pi)e0 +sqrtN/(pi sqrt(v))e0
                                        +O(v^B exp(-cv)). (6.6)

Both cusps contribute sqrtN/(2pi sqrt(v)); the Hodge part gives
the constant. This is also the zero coefficient of the reviewed
identity I_L(1)=2Ecal_L(1)/(N-1). Now q_F-q_c is rapid, of mean
-q_c volY. The nonzero-vector bound from the earlier adjoint proof
therefore gives

    I_L(q_F)=q_c sqrtN/(pi sqrt(v))e0
                                      +O(v^B exp(-c v^(1/3))). (6.7)

The source Eisenstein has leading term2a_N(s)v^((s-1)/2)e0,
where a_N(s)=-s b_N(s)N^((1-s)/2)/(4pi),
b_N(s)=xi(2s)(N^(2s)-1), and a_N(1)=-(N²-1)/24 is nonzero.
Pairing its tail with (6.7)
shows that P_F has residue at1 equal to

    -4a_N(1) q_c sqrtN/pi.

The other constant-term power is integrable near s=1, and the
rapid remainder is holomorphic there. Since (6.5) has no pole,
q_c must bezero. This completes the proof. ∎

Thus q_F is itself an ACTUAL rapid scalar input to the completed
weighted-adjoint theorem. No conjectural second arithmetic derivative
or genus-two product formula has entered its construction.

## 7. An exact first-derivative arithmetic Hodge-height representation

Let H_F^G=I_L(q_F). It is rapidly decreasing by Proposition6.1.
Differentiating (6.5) at1, using the already fixed residue of xi,
gives

    <H_F^G,Ecal_L(1)>=0,
    M=-pi/(4sqrtN) <H_F^G,Ecal_L'(1)>.                    (7.1)

There is no factorial missing: xi(s) times the quadratic zero in
M_F gives a LINEAR leading coefficient. The new test is a first
derivative because the Green equation supplied the factor1/[s(s-1)].
The earlier direct test of I_L(F) still uses the second derivative.

The source arithmetic Siegel–Weil formula gives the ACTUAL series

    R_omega(tau)=<phi_hat(tau),omega_hat_N>_GS
       =1/(N-1)(Ecal_L'(1)-N logN/(N-1)Ecal_L(1)).         (7.2)

Consequently

    M=-pi(N-1)/(4sqrtN) <H_F^G,R_omega>_Pet.               (7.3)

This is a convergent Petersson pairing against the known arithmetic
Hodge-height series, with its vertical normalization inherited from
the primary formula. Its lower correction vanishes only because of
the first equality in (7.1).

There is also an actual arithmetic class for the new input. On the
same scheme cover as in§3 set A_q=(0,2h^*q_F). Its local form (6.2)
has finite energy, so Bost's theorem applies. The same cutoff and
pure-metric argument as in Proposition3.1 proves, coefficientwise,

    d^(-1)<Z_C,A_q>_Bost = I_L(q_F)'s corresponding coefficient.

Thus both scalar series in (7.3) have specified arithmetic-intersection
constructions. We do NOT identify arbitrary vertical extensions of
both factors with a pullback of the entire arithmetic height pairing.
The Hodge-height series in (7.2) remains the original source series;
the pure-metric pairing on C is independent of its vertical choices.

For comparison, the ordinary intersection of A_q with any extension
of the pulled-back Petersson Hodge line is ZERO:

    d^(-1)<A_q,omega_hat_C>=1/(4pi) int q_F dmu=0.

So (7.3) is not the ordinary height of those two classes and does not
identify the theta pairing operator with the identity. Its normalization
and Green operator are substantive. The class A_q has zero finite
part, and no rational point determinant is inferred from this new
arithmetic representation of the scalar.

## 8. Exact remaining arithmetic comparison

The proposed uncorrected SSY genus-two diagonal/height-kernel equality
was not used. The verified cusp-only inner-product theorem cannot
be applied by replacing our input with its zero holomorphic cusp
projection. The alternative actual Poisson construction above gives
an arithmetic Hodge-height SERIES test with all scalar factors, instead
of assuming that unproved diagonal identification.

The source of A_q is a canonically determined real Sobolev metric.
Its existence and arithmetic intersections do not show that the
Petersson functional in (7.3) factors through a rational motivic
regulator or through the determinant of the known point heights.
The point/K2/Tate target remains
D_pt tensor Q beta2 tensor Q(1)^(-2), with coefficient6N(N-1)n_E
as a conclusion. Constructing that rational operation and its lattice
comparison is the remaining gap. The separate relative graph-star
construction has a different degree/domain and may provide further
arithmetic input; it is not excluded by the scalar finite-energy test.

Sections1–4 and the additional §§5–8 passed separate bounded audits
in the linked review. The reviewer reconstructed Lemma5.1, the global
potential, the zero cusp constants and the first-derivative formula.
The repaired Poisson multiplier is POSITIVE 4pi/[s(s-1)]; combining
it with the negative weighted adjoint gives the NEGATIVE constants
in (6.5), (7.1) and (7.3). The earlier direct second-derivative formula
is unchanged. No rational BSD comparison is claimed by this completion.
