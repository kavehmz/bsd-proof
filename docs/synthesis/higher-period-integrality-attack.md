# Higher complex periods and the integrality of the BSD quotient

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Model: GPT-6 Astra, xhigh reasoning. The `[NEW]` deductions below passed the
[independent review](review-higher-period-integrality.md). No claim of historical novelty is intended.

## 1. Task, result, and exact normalization

The objective remains **full BSD for elliptic curves over Q**. This note tests
a narrower possible input: an explicit rational or integral interpretation of
the higher complex leading coefficient. It obtains exact analytic identities
and identifies failures of two proposed arithmetic shortcuts. It proves
neither rationality nor integrality of the BSD quotient, even for 389a1.

Let E/Q have equal proved analytic and algebraic rank r, let f be its normalized
weight-two newform, and put

$$
\ell_E=\frac{L^{(r)}(E,1)}{r!},\quad
t_E=\#E(\mathbb Q)_{\rm tors},\quad C_E=\prod_{p\mid N}c_p,\quad
n_E=\frac{\ell_Et_E^2}{\Omega_E\operatorname{Reg}_E C_E}.
$$

Here Omega is the full real Néron period and Reg uses the saturated
Mordell–Weil lattice with the BSD height convention of the
[archimedean certificate](bsd-archimedean-bound.md). That certificate proves
0.9931 < n_389 < 1.0077, with t=C=1. Only an arithmetic discreteness theorem
can turn this real interval into equality.

The concrete conclusions of this attempt are:

- The leading Mellin moment is exactly a difference of two convergent Chen
  integrals with letters alpha = 2 pi i f(z) dz and beta = dz/z (§2).
- Beta and every positive logarithmic Mellin jet have infinite translation
  orbit. They do not directly enter a finite-rank flat coefficient system
  in its horizontal trivialization (§3).
- Corrected cocycles encoding higher derivatives **do exist** in the
  Goldfeld–Diamantis approach. The polynomial-valued higher cocycles in
  Diamantis–Rolen have zero class in ordinary rational group cohomology in
  degrees at least two. The missing rational period line cannot be supplied
  by taking their ordinary higher cohomology class (§4).
- The analytic eta-weight deformation has an extra even logarithmic moment
  in its second jet. Vanishing of L(1) and L'(1) does not formally eliminate
  it (§5).
- The real period–height determinant line itself is elementary to construct;
  identifying any of these higher periods with its rational or integral
  lattice is still missing (§7).

These statements do not rule out a different motivic, Green-function,
relative-cohomological, or arithmetic theta construction.

## 2. The exact iterated-integral candidate

For this section only, r denotes the exact analytic order at one; rank
equality is not needed. On the upper half-plane H put

$$
\alpha=2\pi i f(z)\,dz,\qquad \beta=\frac{dz}{z},\qquad a=iy_0\quad(y_0>0).
$$

The differential alpha descends to the modular curve: in q-coordinates it is
f(q) dq/q. Beta is holomorphic on H. For an oriented path from a to b, our
Chen convention is

$$
I_a^b(\beta^r\alpha)=
\int_{a<t_1<\cdots<t_r<z<b}
\beta(t_1)\cdots\beta(t_r)\alpha(z).
$$

The inequalities refer to path order, also when the path goes down the
imaginary axis. For r=0 this means the ordinary integral of alpha.

**[NEW] Proposition 2.1 (anchored higher Mellin identity).** With the paths
on the imaginary axis and improper limits at the cusps, both integrals
below converge and

$$
\boxed{\ell_E=I_a^0(\beta^r\alpha)-I_a^{i\infty}(\beta^r\alpha).} \tag{2.1}
$$

The right side is independent of y_0 because all lower Mellin moments
vanish.

*Proof.* Let

$$
M(s)=\int_0^\infty f(iy)y^{s-1}\,dy.
$$

The Fourier expansion at infinity bounds f(iy) by O(exp(-c y)). The cusp
expansion at zero gives O(y^{-2} exp(-c'/y)). Consequently the integral
converges locally uniformly for all complex s, even after any finite number
of derivatives in s. Mellin integration of the Fourier series in its
half-plane of absolute convergence, followed by analytic continuation, gives

$$
L(E,s)=\frac{(2\pi)^s}{\Gamma(s)}M(s).
$$

The factor is nonzero at one. Thus M has exact order r there and

$$
\ell_E=\frac{2\pi}{r!}\int_0^\infty f(iy)(\log y)^r\,dy. \tag{2.2}
$$

For each k<r the corresponding k-th moment vanishes. Expanding
(log y - log y_0)^r therefore leaves (2.2) unchanged.

The iterated integral of r identical beta letters from a to z equals
(Log(z/a))^r/r!: differentiate this expression inductively along the path,
starting with the constant one in length zero. Along z=iy it equals
(log(y/y_0))^r/r!. Since alpha restricts to -2 pi f(iy) dy,

$$
I_a^{i\infty}(\beta^r\alpha)-I_a^0(\beta^r\alpha)
=-\frac{2\pi}{r!}\int_0^\infty f(iy)(\log(y/y_0))^r\,dy.
$$

This proves (2.1), including its signs and factorial. The same cusp bounds
prove convergence of the two improper integrals. No separate integral of
beta at a cusp is being asserted to converge. $\square$

**[NEW] Lemma 2.2 (repeating the elliptic differential alone).** If the
ordinary cusp integral of alpha from 0 to i infinity is zero, then

$$
I_0^{i\infty}(\alpha^m)=0\qquad(m\ge1).
$$

*Proof.* On any truncated path, the identical-letter simplex identity gives
I(alpha^m) = (integral alpha)^m/m!. Pass to the cusp limits, using the absolute
convergence of alpha. $\square$

Thus merely increasing the length while keeping only the f-letter cannot
recover the missing central derivative. Other differentials or other
arithmetic data are essential.

## 3. Why this exact Chen integral is not already an algebraic period proof

**[THEOREM, verified source scope]** Manin,
[arXiv:math/0502576v1](https://arxiv.org/abs/math/0502576v1),
§2.1.2, equations (2.3)–(2.4), allows arbitrary complex Mellin arguments
analytically. For weight k, the usual finite invariant span consists of
f(z) z^{s-1} dz for integers 1 <= s <= k-1. In weight two this leaves s=1.
His §2.5 explicitly discusses descent at that argument. Brown,
[arXiv:1407.5167v4](https://arxiv.org/abs/1407.5167v4),
§2.1.2–§2.1.3, uses the finite polynomial representations V_n and
f(tau)(X-tau Y)^{k-2} d tau. Neither construction identifies arbitrary Mellin
derivatives with the elliptic height determinant merely by differentiation.

**[NEW] Proposition 3.1 (infinite translation orbit).** Let T(z)=z+1.

1. The forms (T^n)^* beta = dz/(z+n), n>=0, are linearly independent over C.
2. If f is a nonzero holomorphic one-periodic function and r>=1, the forms
   f(z)(Log(z+n)-c)^r dz, n>=0, are linearly independent over C for every
   fixed c in C. Use the logarithm on the upper half-plane.
3. None of these positive logarithmic jets, nor beta, is a component of a
   finite-dimensional equivariant vector of scalar differential forms with
   constant T-action.

*Proof.* A finite linear relation in part 1 is a rational-function identity.
The residue at the distinct pole z=-n gives the corresponding coefficient
zero.

For part 2, divide a proposed relation by f on the nonempty open set where
f is nonzero. The holomorphic identity theorem gives a relation among the
logarithm powers on all of H. Fix an index n in this finite relation and let
z=-n+i epsilon with epsilon tending to zero positively. All terms with a
different index have a finite limit: their logarithms approach logarithms
of nonzero real numbers from above. The n-th term has magnitude tending to
infinity if its coefficient is nonzero, because
Log(i epsilon)-c = log epsilon + pi i/2-c. It cannot be cancelled by the
bounded remaining terms. Its coefficient is zero. Repeat for each index.

For part 3, components of an equivariant vector omega=(omega_1,...,omega_d)
with T^*omega=A omega, A a constant matrix, span a finite-dimensional
T-stable space. This contradicts part 1 or 2. $\square$

**[NEW, precise interpretation].** A differential form with values in a
finite-rank local system, pulled back to H and written in a horizontal
basis, transforms by constant monodromy matrices. Proposition 3.1 rules
out the proposed literal components in that trivialization. It does **not**
rule out non-horizontal algebraic gauges, corrected integrands, period
relations after integration, or higher cochains with several group
arguments. The obstruction belongs to this proposed representation, not
to all possible motives with the same numerical period.

The local coordinate also makes the problem visible:

$$
\beta=\frac{dq}{q\log q},\qquad q=e^{2\pi i z}.
$$

The branch of log q records the lift to H. This is not a single-valued
meromorphic differential on a punctured q-disc.

**[NEW] Lemma 3.2 (finite modular-unit logarithms do not replace log y
pointwise).** For a finite list of functions u_j meromorphic at a cusp of
width h, with u_j nonzero on a sufficiently small punctured cusp disc, any
finite real linear combination of log|u_j(iy)| has the form

$$
A y+B+O(e^{-2\pi y/h}). \tag{3.1}
$$

It cannot equal log y for every sufficiently large y.

*Proof.* Write u_j=q^{m_j}(a_j+O(q)), a_j nonzero. Taking the logarithm of
the absolute value gives -2 pi m_j y/h+log|a_j|+O(exp(-2 pi y/h)). Sum. If
A is nonzero the difference from log y has linear growth; if A=0 the
expression tends to B while log y is unbounded. $\square$

This does not apply to Petersson norms, which contain an explicit power
of y. They are treated in §5.

## 4. Corrected higher cocycles: an actual construction, and what it lacks

**[THEOREM, restricted to the verified statement]** Diamantis–Rolen,
[arXiv:1704.02667v1](https://arxiv.org/abs/1704.02667v1), §3.3, Lemma 3.6
and Proposition 3.7, construct polynomial-valued higher cocycles for
modular forms on SL_2(Z). The published account is
[Research in the Mathematical Sciences 5 (2018), article 9](https://doi.org/10.1007/s40687-018-0126-4),
§3.3, Lemma 3.6 and Proposition 3.7. For a cusp form of even weight k,
their distinguished (m+1)-cocycle sigma has

$$
(-1)^m\sigma(S,\ldots,S)(z)
=\sum_{n=0}^{k-2}\binom{k-2}{n}i^{1-n}
\Lambda_f^{(m)}(n+1)z^{k-2-n}. \tag{4.1}
$$

Here Lambda_f(s)=(2 pi)^(-s) Gamma(s)L_f(s), S is the usual inversion,
and there are m+1 arguments. Their construction starts with the eta
automorphy cocycle, takes cup powers, integrates, and takes a cochain
differential. Thus failure of the raw logarithmic form to descend does
not prevent such corrected **cocycles** from existing.

Formula (4.1) is a level-one statement. There is no nonzero weight-two
level-one cusp form, so this particular displayed theorem is not being
silently applied to 389a1. Its cohomological mechanism is the candidate
being tested.

**[NEW] Proposition 4.1 (ordinary higher cohomology has no nonzero period
line here).** Let Gamma be any subgroup of SL_2(Z), K a field of
characteristic zero, and V any K[Gamma]-module. Then

$$
H^j(\Gamma,V)=0\qquad(j\ge2). \tag{4.2}
$$

In particular a polynomial-valued (m+1)-cocycle with m>=1 has zero class
in ordinary group cohomology, even if its distinguished representative
has nonzero values.

*Proof.* The presentation PSL_2(Z)=C_2*C_3 gives its coset tree: vertices
are G/C_2 and G/C_3, and edges are G, the edge g joining gC_2 to gC_3.
Reduced-word uniqueness shows this graph is connected and contains no
cycle. The presentation and reduced-word proof are explicitly available in
Keith Conrad, [SL_2(Z), Appendix C, Theorem C.1](https://kconrad.math.uconn.edu/blurbs/grouptheory/SL%282%2CZ%29.pdf).

Let Gamma act on this tree through its projection to PSL_2(Z). Stabilizers
of vertices and edges in Gamma are finite: in SL_2(Z) their orders divide
4, 6, and 2, respectively. The action preserves the two vertex types, so
there is no edge inversion. The augmented cellular chain sequence is
therefore exact:

$$
0\longrightarrow K[\text{edges}]
\longrightarrow K[\text{vertices}]
\longrightarrow K\longrightarrow0. \tag{4.3}
$$

Each permutation module is a direct sum over Gamma-orbits of induced
modules K[Gamma] tensor_{K[F]} K with F a finite stabilizer. The trivial
K[F]-module K is projective: its projection from K[F] is split by
1 maps to |F|^(-1) sum_{g in F}g. Induction preserves projectives because
K[Gamma] is free as a right K[F]-module. Direct sums of projectives are
projective. Thus (4.3) is a projective resolution of the trivial module of
length one. Applying Hom_{K[Gamma]}(-,V) computes group cohomology and
proves (4.2). $\square$

Consequently the following argument fails: “sigma is a higher cocycle with
polynomial coefficients, so its Hecke eigenspace in ordinary higher
cohomology is a rational line whose period is L^(m).” The proposed
cohomology group is zero. A nonzero secondary invariant could retain the
choice of primitive, an automorphy defect, relative boundary conditions, or
an extension. Its rational structure and its comparison to the
Mordell–Weil height determinant require additional statements.

This observation does not contradict Diamantis–Rolen: equation (4.1)
concerns a selected cocycle representative, not a nonzero ordinary higher
cohomology class. Nor does it apply automatically to restricted or relative
cohomology groups with extra structures.

**[THEOREM, source scope]** Bruggeman–Choie–Diamantis,
[arXiv:1404.6718](https://arxiv.org/abs/1404.6718), Memoirs AMS 253 (2018),
no. 1212, §9.4, instead places a derivative in a family of degree-one
cocycles with holomorphic-function/boundary-germ coefficients. The
[authors' corrected PDF](https://webspace.science.uu.nl/~brugg103/notes/caf-with-corr.pdf),
dated 28 November 2018, §9.4, uses f(z)(eta(z)eta(Nz))^s. Its introduction
describes the further arithmetic understanding as a hoped-for application.
It does not provide an identified rational height-determinant lattice.

The exact printed scalar in that PDF's equation (9.6) is not used here:
normalizations must be checked directly against Goldfeld's original
[Special values of derivatives of L-functions](https://www.math.columbia.edu/~goldfeld/DerivativesL-Functions.pdf),
CMS Conference Proceedings 15 (1995), 159–173, §4. The next section derives
the needed eta identities from scratch with the standard Mellin convention.

## 5. Testing the eta deformation at analytic rank two

Now assume the functional-equation sign is +1 and L(E,1)=0. It follows
that L'(E,1)=0 as well: the completed function is even about one, and its
value at one vanishes. This includes 389a1.

For y>0 set

$$
x=\log(\sqrt N y),\quad y=e^x/\sqrt N,\quad
\rho(x)=y f(iy),
$$
$$
u(y)=\log(\eta(iy)\eta(iNy)),\qquad
U(x)=u(e^x/\sqrt N)+\frac{x}{2}.
$$

The eta factors on this axis are positive real, so these logarithms have
no branch ambiguity. Define a holomorphic germ at s=0 by

$$
J(s)=\int_0^\infty f(iy)e^{s u(y)}\,dy. \tag{5.1}
$$

**[NEW] Proposition 5.1 (the second eta jet includes another moment).**
With the preceding assumptions,

$$
\rho(-x)=\rho(x),\qquad U(-x)=U(x), \tag{5.2}
$$
$$
J''(0)=\int_{-\infty}^{\infty}\rho(x)U(x)^2\,dx
+\frac14\int_{-\infty}^{\infty}\rho(x)x^2\,dx, \tag{5.3}
$$
and

$$
\boxed{\frac{L''(E,1)}{2}
=4\pi\left(J''(0)-\int_{-\infty}^{\infty}\rho(x)U(x)^2\,dx\right).} \tag{5.4}
$$

*Proof.* Write w_N for the weight-two Fricke eigenvalue, so that
f(-1/(Nz))=w_N N z^2 f(z); the functional-equation sign is -w_N. Here
w_N=-1. At z=iy this gives

$$
\frac{f(i/(Ny))}{Ny^2}=f(iy).
$$

Multiplication by y and the change x to -x prove the first part of (5.2).
The eta inversion formula on the positive imaginary axis is
eta(i/y)=sqrt(y) eta(iy); it also follows immediately from the published
Diamantis–Rolen equation (3.1) with u=2 log eta and c_S=-pi i/2.
Apply it to the two factors to obtain

$$
u(1/(Ny))=u(y)+\log(\sqrt N y)=u(y)+x.
$$

Therefore U is even, proving the second part.

The q-product gives u(y)=-pi(N+1)y/12+O(exp(-2 pi y)) at infinity.
Inversion gives its corresponding O(1/y+|log y|) behavior at zero. For
|s| sufficiently small the exponential decay of f at both cusps dominates
exp(su), also after two s-derivatives. Thus differentiation in (5.1) is
justified and

$$
J''(0)=\int\rho(x)(U(x)-x/2)^2\,dx.
$$

The cross term rho(x) U(x)x is odd and absolutely integrable; its
integral is zero. This proves (5.3).

Since L(1)=L'(1)=0, the Mellin calculation in §2 gives
L''(1)/2=pi integral f(iy)(log y)^2 dy. Replacing log y by
x=log y+(log N)/2 does not change this expression because the zeroth and
first moments vanish. Substitute (5.3) to obtain (5.4). $\square$

The even correction integral in (5.4) is **not claimed nonzero for 389a1**.
The point is that it survives the symmetry calculation; omitting it is an
unproved additional identity. Both rho and U are even, so there is no
parity cancellation. Rank-two vanishing supplies integral rho=0 and
integral rho x=0, not integral rho U^2=0.

For comparison, with sign -1 the same calculation gives rho odd and U
even, hence J'(0)=-(1/2) integral rho x. If L(1)=0 this recovers
L'(1)=-4 pi J'(0) in our Mellin/eta normalization. The special first-jet
relation does not extend by dropping the new term in the second jet.

**[NEW, interpretation of the correction].** On H the function

$$
\mathcal U(z)=\log|\eta(z)\eta(Nz)|+\tfrac12\log\operatorname{Im}z
+\tfrac14\log N
$$

is Gamma_0(N)-invariant: the product has weight one and a multiplier of
absolute value one. On z=iy it restricts to U(x). Thus the missing term
uses the square of a Petersson logarithm, not a logarithm of a meromorphic
modular unit. An arithmetic Green-function construction is a possible
next route, but no proved arithmetic intersection identity identifies
this particular weighted geodesic integral with the required regulator.

## 6. What the regulator, harmonic-Maass, and theta sources actually supply

These are source-scope checks, not assertions that no stronger theorem can
exist. They were checked on 2026-09-12.

**[THEOREM, source scope]** Schappacher–Scholl, *Beilinson's theorem on
modular curves*, in *Beilinson's conjectures on special values of
L-functions*, Perspectives in Mathematics 4 (1988), pp. 273–304:
[author location](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/RSS.pdf),
[readable scan of the authors' chapter](https://ncatlab.org/nlab/files/SchappacherScholl.pdf).
Theorem 1.1.2 constructs regulator rational structures from modular-unit
K_2 symbols; §2.1, equation (2.1.0), relates its derivative at zero to
the value at s=2. This is a different special point from the central
higher derivative. In Remark 1.1.3(i), the regulator of symbols using only
the two cusps of X_0(p) is zero; passing to higher levels is part of their
construction. Thus even this genuine modular-unit regulator theorem is
not a ready-made central rank-two period identity for prime conductor 389.
No integrality conclusion for n_E is inferred from its “integrality” part.

**[THEOREM, exact restricted instance]** Bruinier–Ono,
[Annals of Mathematics 172 (2010), 2135–2181](https://annals.math.princeton.edu/2010/172-3/p15),
Theorem 1.1(2): let p be prime, G a weight-two newform on Gamma_0(p) with
sign -1, and f_g the weight-one-half harmonic weak Maass form normalized
as in their introduction, with algebraic principal part and prescribed
shadow. For a positive fundamental discriminant D with (D/p)=1,
L'(G,chi_D,1)=0 iff c_g^+(D) is algebraic. This detects vanishing of a
**first** derivative. It is not a formula for a second derivative or its
regulator-normalized rationality. The printed PDF drops minus signs in
text extraction; [arXiv:0710.0283v2](https://arxiv.org/html/0710.0283v2)
explicitly confirms the sign -1 in Theorem 1.1.

**[THEOREM, statement inspected; proof not independently audited]**
Du–Peng, [arXiv:2603.15795v1](https://arxiv.org/html/2603.15795v1),
Theorem 0.6, expresses a global height of higher Heegner cycles in terms
of L'(Sh(xi f),kappa), under the stated coprimality condition
(D_0,2ND(f))=1. The source's “higher” refers to weight/cycle codimension;
the derivative in equation (0.7) is first order. We use no assertion of
this preprint beyond this checked scope distinction.

Brown's [arXiv:1904.00190v2](https://arxiv.org/abs/1904.00190v2) studies
multiple-variable L-values and relates certain integer values to periods.
It supplies no identification used here between the Mellin derivative of
a fixed weight-two newform and its Mordell–Weil regulator. No implication
from “is a period” to “is this rational multiple of Omega Reg” is valid
without a further comparison: rational ratios of two arbitrary periods
are not a property of periods in general.

## 7. The actual determinant line and the first missing comparison

The target rational line is available without invoking a conjectural
zeta element. Let

$$
W=E(\mathbb Q)\otimes\mathbb Q,\quad
B=H_1(E(\mathbb C),\mathbb Q)^+,\quad
D=H^0(E,\Omega^1_{E/\mathbb Q}),
$$
$$
\mathscr D_E=(\det W)^{\otimes2}\otimes B\otimes D. \tag{7.1}
$$

**[NEW, explicit linear-algebra construction]** The height and integration
pairings define a real isomorphism theta_E: D_E tensor R to R by

$$
\theta_E\big((P_1\wedge\cdots\wedge P_r)
\otimes(Q_1\wedge\cdots\wedge Q_r)\otimes\gamma\otimes\omega\big)
=\det(h(P_i,Q_j))\int_\gamma\omega. \tag{7.2}
$$

*Proof.* The determinant of a bilinear pairing is alternating multilinear
in each list, so it factors through the two determinant lines. Integration
is bilinear in the last two factors. Nondegeneracy of the real Néron–Tate
height and nonzero real period show that this map between real lines is
nonzero, hence an isomorphism. $\square$

Let gamma_R be the sum of the real connected components, oriented so that
the fixed minimal differential omega integrates positively on each.
It is an integral Betti class and its integral is the full real period.
For a saturated Mordell–Weil basis P_i define

$$
e_E=(P_1\wedge\cdots\wedge P_r)^{\otimes2}\otimes\gamma_R\otimes\omega.
$$

The squared determinant makes this independent of integral basis change.
Changing the sign of omega reverses gamma_R and leaves their tensor fixed.
In particular

$$
\theta_E(e_E)=\Omega_E\operatorname{Reg}_E,
\qquad
\theta_E\big(\mathbb Z(C_E/t_E^2)e_E\big)
=\mathbb Z\,\Omega_E\operatorname{Reg}_E C_E/t_E^2. \tag{7.3}
$$

The displayed lattice retains the real-component factor at two. It is a
specific arithmetic normalization; no identification with a full integral
motivic cohomology complex is asserted in this paragraph.

Defining theta_E^(-1)(ell_E) over R is automatic and supplies no arithmetic
information. Its membership in D_E is exactly the rationality problem;
its membership in Z(C_E/t_E^2)e_E is exactly the integrality problem.
The constructions in §§2–5 have not produced either membership.

**[GAP HP-389, explicit first period comparison for the test curve].**
Let f be the normalized newform of 389a1, alpha=2 pi i f(z)dz,
beta=dz/z, and P=(-1,1), Q=(0,-1), the certified full basis. Prove that

$$
I_i^0(\beta^2\alpha)-I_i^{i\infty}(\beta^2\alpha)
\ \in\
\mathbb Z\,\Omega_E\big(h(P,P)h(Q,Q)-h(P,Q)^2\big). \tag{7.4}
$$

Replacing Z by Q asks only rationality. An acceptable arithmetic-period
approach to (7.4) must construct a rational/integral secondary period
object and its regulator comparison independently of the left-hand real
number. In particular, the value of a distinguished higher cocycle is not
by itself an element of the right-hand lattice. Neither Proposition 3.1
nor Proposition 4.1 rules out a secondary object that retains the extra
data lost by ordinary cohomology.

**[GAP HP-eta, concrete remaining comparison in the corrected approach].**
For the same f define J, rho, and U exactly as in §5. Construct and prove
an arithmetic regulator identity, with rational coefficients, for

$$
4\pi\left(J''(0)-\int_{-\infty}^{\infty}\rho(x)U(x)^2\,dx\right)
$$

whose target is the explicitly normalized line and lattice in (7.3).
The analytic equality with ell_E is already proved in (5.4). The first
unproved step is the arithmetic meaning of this **difference**, including
its Petersson-log-square correction; dropping the correction would be a
different unproved identity.

These gap formulations are recorded as unmet proof obligations, not
renamed successes. The attempted construction of their source was the
Chen model, then corrected higher cocycles and the eta family. The first
fails literal finite-rank descent; the ordinary higher cohomology class
of the second is zero; and the eta family's second jet leaves the explicit
extra term. No zeta element was fabricated by declaring its period equal
to ell_E.

## 8. Review and restart information

The proofs requiring independent review are Propositions 2.1, 3.1, 4.1,
5.1 and the determinant normalization in §7. The first three obstruction
statements must retain their limited scope. In particular, no claim has
been made that higher derivatives are not periods or that BSD is false.

No numerical certificate was rerun: this task added analytic derivations
and source checks, not numerical claims. Only this note and
[the owned checkpoint](higher-period-integrality-checkpoint.md) were edited.
The parent should update its ledger and research-state after review.

The next meaningful investigation would retain the secondary data of the
eta automorphy/cup construction or identify the correction in (5.4) by an
arithmetic Green-function identity. Merely repeating critical-value
algebraicity, increasing iterated-integral length, or taking the ordinary
higher cohomology class does not supply that identity.
