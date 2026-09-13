# Independent review of the weighted theta adjoint

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Reviewed [the proof](weighted-theta-adjoint-attack.md) and
[checkpoint](weighted-theta-adjoint-checkpoint.md).

**PASS.** All six sections check, after explicitly writing the original
modular-unit ratio as N^(-6)Delta(z)/Delta(Nz), avoiding ambiguity with
Du–Yang's different generalized Delta_N. No substantive formula repair
was needed. The raw Eisenstein factor TWO, simultaneous convergence,
isotropic multiplicities and second-derivative formula are verified.

Reviewed proof SHA256:
b15efe3c4ac397b857b35db03e6cc992f23f537a191828fe1b233ead39d80959.
Reviewed checkpoint SHA256:
d736aef403949798c0f29573a8d1f902f37d34391bb57c6268d9c4f7267ae9b0.
Subsequent PASS links and checkpoint completion are editorial.
The rational arithmetic realization remains unconstructed.

## 1. The actual kernel and the source's Eisenstein factor two

The primary source checked was
[Du–Yang1702.07917v2](https://arxiv.org/pdf/1702.07917v2),
(1.6), (2.2)–(2.7), the signed primitive-row calculation on
printed pp.11–12, and its degree normalization.
Combining its two exponentials gives exactly
\[
 (v p_A^2-1/(2\pi))e^{-\pi vq_z(A)}e^{2\pi iuQ(A)};
\]
indeed R(A,z)=p_A²/2−2Q(A), so R+Q=q_z(A)/2.
The zero-vector term is −e_0/(2π).

The central action can be checked without guessing a convention.
The source's Fourier formula gives ρ(S²)=i times reflection
μ↦−μ. The lift S²=(-I,i) contributes i^(-3)=i to the
weight-three-halves slash; multiplication by ρ(S²)^(-1)
leaves just reflection. Thus the combined action fixes e_0.
The kernel of the metaplectic cover likewise acts trivially
under the combined slash. The full stabilizer identifies
the two signed primitive rows, whereas the source's rewrite
keeps both. Its effective raw series is therefore twice
the full-stabilizer seed-one series.

I independently checked this factor by the displayed
one-dimensional Poisson identity. If theta(t)=Σe^(-πta²),
then −t theta'(t)/π−theta(t)/(2π), after differentiating
theta(t)=t^(-1/2)theta(1/t), is
\[
 -t^{-3/2}\sum_{n\ne0}n^2e^{-\pi n^2/t}.
\]
With t=v/(Ny²), its y-Mellin integral has leading seed
coefficient
\[
 -\frac{s}{2\pi}N^{(1-s)/2}\xi(s)v^{(s-1)/2}.
\]
Comparison with the source's coefficient −s/(4π)
therefore gives the same factor two. This resolves the
printed coset notation by its actual calculation, rather
than importing a generic stabilizer convention.

The independent s=1 arithmetic check also agrees:
the zero coefficient contributes −2deg(omega)=−(N+1)/6
in the effective degree convention. The degree identity
gives constant −(N²−1)/12 for the completed series.
Its normalizing factor a_N(1)=−(N²−1)/24 again leaves
raw leading coefficient two. None of these factors is
a missing stack-covering degree.

## 2. Rapidity after the mean-zero subtraction

The exact mean-zero condition cancels the zero-vector
term before any estimate. Since p_A²≤2q_z(A), the
polynomial factor is absorbed by a smaller Gaussian.
On a bounded-x cusp strip, the adjoint of the matrix
carrying i to z and its inverse have norm O(y), giving
q_z(A)≥c||A||²/y² in the fixed rank-three lattice.
On the compact core there is a fixed positive bound.

The full Gaussian sum is bounded by
C(1+y/sqrt(v))³. For y≤Y and v/Y² large, deleting A=0
gives the additional exp(−cv/Y²). Choosing Y=v^(1/3)
bounds that portion by exp(−cv^(1/3)); the h-tail is
bounded by a polynomial times exp(−cY). The hyperbolic
dy/y² factor is retained throughout. Thus the claimed
rapid v-decay follows. Fixed tau derivatives introduce
only polynomials in Q(A),q_z(A),v, which the same
Gaussian argument absorbs.

This proves rapidity for H=I_L(h), not for an
unsubtracted pointwise opposite theta integral.
It uses hyperbolic cusp decay, without restoring the
withdrawn algebraic-cusp smoothness assertion about F.

## 3. The isotropic orbit sum and absolute Mellin interchange

For odd prime N, integrality of −r²/(4N) forces
r=0 modulo2N, so only the zero discriminant coset is
isotropic. In the zeroth theta component, u-integration
over a period selects exactly Q(A)=0. This interchange
at fixed v is allowed by the Gaussian/lattice bound.

There are exactly two cusp orbits at prime level.
The vectors A_infinity and A_0 in the proof are primitive
in the actual lattice. Conjugation by Gamma preserves
primitivity. A cusp stabilizer fixes its displayed
nilpotent vector, not just its line: its diagonal
entries are ±1 and its conjugation scale is their
positive square. Hence it cannot identify that vector
with its negative. The two signs belong in the integer
multiple sum, producing 2zeta(s).

The pairing formula gives
\[
 |p_{A_\infty}(z)|^{-s}=N^{s/2}y^s,\qquad
 |p_{A_0}(z)|^{-s}=N^{s/2}\Im(w_Nz)^s.
\]
Inverting the orbit cosets gives the usual left-coset
Eisenstein sums. Thus the coefficient in (3.2), including
both cusp terms and width-one Fricke scaling, is correct.

For one isotropic vector the substitution x=πvp_A²
gives
\[
 \pi^{-s/2}|p_A|^{-s}
 \frac{\Gamma(s/2+1)-\Gamma(s/2)/2}{\pi}
 =\frac{s-1}{2\pi}\pi^{-s/2}\Gamma(s/2)|p_A|^{-s}.
\]
The absolute integral is bounded by the analogous
positive expression at Re(s). Summing those bounds
uses (3.2) with Re(s)>1 and integrating against |h|
is finite because of its exponential cusp decay.
Therefore the v-integral, isotropic sum and z-integral
may be exchanged precisely in the claimed initial region.

At s=1 one must NOT integrate each vector and then
sum its zero Mellin value: the absolute argument no
longer applies there. The continuation retains the
compensating zeta pole. The proof uses continuation,
so it does not make that invalid interchange.

## 4. Absolute Petersson unfolding and its scalar

The Weil representation is unitary in the stated basis.
Hence v^(3/4)||H(tau)|| is invariant and bounded on a
fundamental domain, by rapidity and compact-core
smoothness. On the bottom of the unfolded strip this
gives ||H||≤C v^(-3/4). The exponent v^(s/2−1) is
then integrable for Re(s)>3/2; the proof's stronger
starting hypothesis Re(s)>2 is sufficient. It also
lies in the absolute Poincaré-series region.

The bar on the parameter in the second Petersson
entry is essential and correct. After conjugation
the seed is v^((s−1)/2)e_0. Combining it with
v^(3/2)du dv/v² gives v^(s/2−1)du dv, with no
remaining phase or covering factor. Thus unfolding
gives exactly 2a_N(s) times the isotropic Mellin integral.

Multiplying the checked constants gives
\[
 2a_N(s)\frac{s-1}{\pi}N^{s/2}\xi(s)
       \int h(E_\infty+E_0)
 =
 -\frac{\sqrt N}{\pi^2}s(s-1)\xi(s)\int hJ_N^+(s).
\]
There are three distinct multiplicities here:
the signed isotropic integer multiples, the two cusp
terms, and the raw metaplectic factor two. The proof
keeps each. Fricke change of variables replaces
J_N^+ by J_N for the actual even F.

Both sides have the asserted meromorphic continuation.
The functional is defined on mean-zero rapid h.
The zero-vector contribution to the unregularized
opposite integral at a fixed z diverges at large v;
the proof cancels it before unfolding and never
interchanges that divergent pointwise integral.
The generalized adjoint-composition multiplier
r_N(s)xi(s) therefore has the stated tested scope,
not an inverse on every spectral component.

## 5. The original mass uses the second derivative

Because Res_(s=1)xi(s)=1,
r_N(1)=−sqrt(N)/pi². The known lower pairings make
the original scalar integral equal to M t²+O(t³).
Differentiating the convergent Petersson pairing
therefore gives
\[
 \langle I_L(F),\mathcal E_L''(1)\rangle
       =2r_N(1)\mathcal M.
\]
This proves (5.2), including its minus sign and
the factor one-half. Substitution of the known M
gives exactly
3N^(3/2)(N−1)ell L(E,2)/pi^5 in (5.3).
It is nonzero, so this actual theta lift I_L(F)
is nonzero.

The difference from the earlier forward third
derivative is correctly explained. In the forward
lift, xi(s) has a pole. In this weighted adjoint,
the isotropic Mellin factor s−1 cancels that pole.
The second derivative here is therefore consistent
with the earlier unpaired third-derivative formula.
The older Gamma completion changes no weighted
second coefficient because all lower pairings vanish.

## 6. Arithmetic scope and verification boundary

This proves the analytic weighted adjoint on the
required Eisenstein family. The arithmetic input
for I_L(F) remains the reviewed limit of smooth
cutoff metric pairings. It is not a single smooth
class a(2ReF), nor a rational motivic class obtained
by taking a limit inside an arithmetic Chow group.

The original f-weighted mass is recovered with its
full multiplier, but no rational arithmetic
second-derivative test or point-height determinant
map has been constructed. The beta2 line and its
arithmetic extension remain valid existing inputs.
The required coefficient6N(N−1)n_E is still a
conclusion to prove, not a scalar available for
defining the desired class.

No old numerical certificate was rerun for this
review, and no agent was spawned.

