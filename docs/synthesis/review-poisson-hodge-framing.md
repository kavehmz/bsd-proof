# Independent review of the Poisson Hodge framing

Date:2026-09-13. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. **PASS for all seven sections.**
No mathematical or normalization correction is required.

Reviewing poisson-hodge-framing-attack.md, mathematical SHA256
8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210,
its checkpoint and the completed predecessor proof/review. The
checkpoint's candidate/review-queue wording is a historical draft
status; the complete proof is the mathematical object audited here.
Reviewed checkpoint SHA256:
1cca1b98cde8e991c0e5ae42c5229aaa2b92ac312c3131c0b5f6aaff3d9de22d.
Ownership: this review only, plus a review-status addition to the
reviewer's existing marked-rational-boundary-lift checkpoint.
Root's proof and shared synthesis remain unchanged.

Audit targets: the actual ordered path quotient and exact sequences,
the corrected F1 logarithmic bar representative, canonical I^(1,2)
including the weight-zero constant, the I00 test, the real-split
weight-one lift, and the exact Deligne/Tate/sign identity h=-U/(4pi).
No numerical certificate or old computation was rerun.
Full BSD and the rational arithmetic comparison remain unresolved.

## 1. Primary versions and conventions

I directly read the following primary sources:

- [Looijenga2403.03748v2](https://arxiv.org/pdf/2403.03748v2),
  arXiv stamp23June2024,13pages: Theorem1.1, Corollary3.1,
  Example4.5, and the concluding mixed-Hodge compatibility statement.
- [Hain math/0109204v2](https://arxiv.org/html/math/0109204v2),
  arXiv stamp26October2001: §2, the reduced bar discussion, the
  logarithmic comparison, and Theorems13.2,13.6,13.7 with the proof
  of13.7. The PDF fetch had a cache miss; the complete primary
  HTML supplied the precise filtered statements.
- [Burgos Gil–Goswami–Pearlstein2410.17167v3](https://arxiv.org/html/2410.17167v3),
  §2.1, especially(2.2),(2.5)–(2.7), and the Deligne projection
  conventions. I checked the overbars in the full mathematical HTML,
  rather than inferring them from the lossy PDF text extraction.
  The arXiv stamp is8July2026; generated front-page dates are not
  treated as new versions.

The source's earliest-first convention is independently fixed by its
oriented sampling simplex. No word-order sign is imported from a paper
using right-to-left categorical composition. The only BGG-P input here
is the Deligne bigrading/splitting formalism. The functional called h
is the displayed elliptic-period functional on its weight-minus-three
component, not an automatic application of a standard scalar height
theorem with Tate bottom.

## 2. The complex loop character and intrinsic principal parts

For two based loops h,k, the concatenation defects in G_b are

    bar(a_h)b_k + bar(a_h)bar(b_k).

They cancel because b_k is a period of dlog u and belongs to2pi i Z.
Thus G_b is an actual additive COMPLEX character, not only a real one.
It factors through H1(Y,Z).

I checked the transported cusp-loop formula including the possible
pole of the primitive of rho. For a path tau from b to a point x
near the cusp, the chronological concatenation formula for
tau gamma tau^-1 has the additional term Atilde(x) int_gamma theta.
The local iterated integral is

    2pi i Res(Atilde theta)−Atilde(x)int_gamma theta,

so those terms cancel exactly. The zero residue of rho is what
removes the other possible first-period cross term. For alpha the
primitive is A_c+a_c(q), with a_c(0)=0, and the residue is m_c A_c.
Scalar conjugation negates2pi i, giving

    G_b(gamma_c)=−2pi i Res_c[(bar A_c−Atilde)theta].

The two positive cusp loops sum to zero in H1(Y). Their G_b values
therefore sum to zero and prove the residue compatibility of s_c
without assuming the already constructed Poisson solution. The
finite differential Mittag-Leffler/Riemann-Roch problem is consequently
solvable in the stated cuspidal pole space.

Adding the xi_b periods kills the cusp values of G_b, so Lambda_b
is a well-defined compact cohomology class. Its Hodge decomposition
has unique holomorphic and antiholomorphic representatives. The real
period equation for the predecessor's correction is exactly

    Re eta_b = 2log2 Re alpha−Re Lambda_b

on compact cycles. Hence eta_b=2log2 alpha−Lambda10−bar Lambda01,
as in(2.2). The real compact-period isomorphism gives uniqueness.
All genus directions are present.

## 3. The actual rational path quotient and its ordered central map

The maps pi and u are algebraic, so their homological maps are
rational MHS morphisms. The positive cusp generator maps to
388·1(1)_B under u_*. Dividing that generator by388 gives the
claimed rational splitting of H1(Y); the kernel of u_* maps
isomorphically to H1(X). The compact map pi_* kills the cusp loop.
There is no assertion that this splitting is integral or primitive.

For b distinct from z, Looijenga's theorem identifies the FULL
truncated path module with the relative H2 of the displayed pair.
When b=z, its kernel is precisely the constant-path line. Adding
that line back gives the augmented group algebra used in the proof.
This exception is retained in both the statement and the calculation.

The affine curve has free fundamental group. Its degree-two
augmentation quotient is consequently H tensorH, with no compact
cup-product relation imposed. Multiplication is an MHS morphism
by the geometric compatibility in Looijenga's Example4.5 and
concluding paragraph; truncation is one by Corollary3.1.
Thus(3.2) is an exact sequence of rational MHS, not just an equality
of dimensions. The kernel identification is independent of the
chosen path: changing a reference path only changes the degree-two
identification in augmentation degree at least three.

On the simplex(gamma(s),gamma(t)), ds wedge dt with s<=t, evaluation
of alpha from the first factor and theta from the second gives
I_(alpha,theta) itself. On a product of two augmentation differences
it gives a_alpha(h)b_theta(k), with positive coefficient one.
This checks the chronological ordering and excludes an extra factor2.

The map lambda(a tensorb)=pi_*a tensoru_*b is therefore the declared
ordered map. It is surjective over Q: u_* is nonzero onto its Tate
line, and pi_* is onto elliptic H1 over Q (the pullback/trace
composite has the nonzero modular degree). The pushout in(3.4)
exists in the abelian category of rational MHS and is exact.
No division by the modular degree is inserted into lambda.

The graded pieces and types are exactly those listed: topQ0,
compact H_X of weight-1, Tate Q1 of weight-2, and
K=H1(E,Q)(1) of weight-3 with types(-2,-1),(-1,-2).
The central alpha-theta covector evaluates on h tensor1(1)_B as
2pi i int_h omega_E. This retains both the actual pi-map and the
Tate comparison; it is not the functional ell_omega by itself.

## 4. The logarithmic F1 repair and the canonical central covectors

The two-holomorphic-form word f_alpha belongs to the F2 bar
subcomplex. The lower P1 dual has no F2, while the central dual
has a single(2,1) line. Therefore f_alpha is the unique canonical
I^(2,1) lift of its central covector.

For the second-kind form, the uncorrected word is not simply
declared logarithmic. Set v=bar A−Atilde, with dv=bar alpha−rho
and v(b)=0. Integration by parts gives

    I_(rho,theta)+int xi_b
      =I_(bar alpha,theta)+int(xi_b−v theta).

The correction nu=xi_b−v theta has type(1,0). Since rho wedge theta
is zero on the complex curve,

    d nu=−bar alpha wedge theta.

This is precisely the closed-bar equation in the chronological
convention. Locally, the full meromorphic principal part cancels
against xi_b, leaving a holomorphic regular term minus
bar(a_c(q))theta. Its coefficient is smooth at the cusp and the
remaining singular differential is of logarithmic type.
Smooth coefficients multiplying dq/q are permitted in this
logarithmic Dolbeault model.

Hain's proof of13.7 explicitly identifies that smooth logarithmic
filtered complex with the filtered algebraic logarithmic model.
The word bar alpha then theta has total Hodge filtration at least
one, and so does the correction nu. This proves the needed F1
membership. It does not rely on a general claim that every
meromorphic second-kind word is already in the logarithmic F1 model.

The sum f_rho1+bar f_alpha vanishes on K. On a prefix-loop
difference representing h, its value is

    Lambda_b(h)+bar(a_h)(B+bar B)
      =Lambda_b(h)+2l'bar(a_h).

Its Tate component is zero because the cusp periods vanish.
Subtracting the holomorphic Lambda10 leaves a compact(0,1)
class on the lower H part. In P1 dual this belongs to
bar F1 W1 plus a POSSIBLE W0 constant. The proof correctly
keeps that constant.

I substituted p=1,q=2 into BGG-P(2.2). The expression is exactly

    F1 intersect W3 intersect
      (bar F2 W3 + bar F1 W1 + bar F0 W0).

It includes the weight-zero term; omitting it would not be justified.
This proves the asserted canonical I^(1,2) lift. Its prescribed
central image fixes it uniquely by the Deligne bigrading. The
holomorphic ambiguity in xi_b cancels with the same change of
Lambda10, and a change of rho within its fixed cohomology class
leaves the same canonical lift.

On K_R the exact covector relation is

    f_rhoD = −bar f_alpha.

Both original restrictions contain2pi i; scalar Betti conjugation
negates that factor. This is not the geometric real involution of
the algebraic curve or its endpoints.

## 5. The real split compact lift

By the displayed Hodge types, delta can only map the top to
weights-2,-3 and compact weight-1 to weight-3. It kills the last
two weights, so delta squared is zero. There is no component
strictly lower in BOTH indices from the Tate(-1,-1) line to K.
Consequently its Deligne lift tD is real.

The map from H_X,R to all compact holomorphic periods is a real
isomorphism. It therefore gives the unique r_H with the specified
ALL-form periods, including alpha(r_H)=A and theta(r_H)=0.
Using only the elliptic periods would not prove the later
Lambda01 evaluation; the proof retains the full compact curve.

The real split lift hat s_H=exp(-i delta_-)s_H^D is canonical.
Let y_r=delta_-hat s_H(r_H), a real vector in K. Since the two
central Deligne covectors vanish on the Deligne H lift, their
values on hat s_H are respectively-i f_alpha(y_r) and
-i f_rhoD(y_r). The Tate-conjugation relation then gives

    f_rhoD(hat s_H(r_H))=bar(f_alpha(hat s_H(r_H))).

Also f_alpha+bar f_rhoD annihilates K_R. Any chosen real prefix-loop
lift R_r differs from hat s_H(r_H) by exactly such a vector after
its Tate component has been removed. The loop evaluation from
the preceding section proves

    2f_alpha(hat s_H(r_H))
       =2l'A+bar Lambda01(r_H)
       =2l'A+int_b^z bar Lambda01.

This verifies(5.1) with its sign and its full-genus contribution.
No free real correction is tuned to match a desired scalar.

## 6. I00, conjugation and every scalar factor

Subtracting hat s_H(r_H) and (B/(2pi i))tD from the Betti path
vector removes respectively all compact first-order F1 covectors
and the logarithmic covector. The two canonical central covectors
form a basis on K_C and therefore specify a unique vK. Subtracting
it kills the remainder of F1(V dual). Thus eD is in F0(V), has
top value one, and its conjugation difference has no weight-minus-one
component because the compact lift was real.

For p=q=0, BGG-P(2.2) allows the lower terms
bar F^(-1)W_-2 and bar F^(-2)W_-3. The first contains the Tate
piece, and the second contains all of K. Together they are the
entire W_-2 in this precise type range. Hence the condition
bar eD−eD in W_-2 is sufficient here to identify the canonical
I00 lift. This does not assert that it is sufficient in arbitrary
mixed Hodge structures.

The convention exp(-i delta) gives the real splitting, so
bar eD=eD−2i delta eD. I independently conjugated(6.1)–(6.2):

    bar eD−eD =
      (B+bar B)/(2pi i)·tD + vK−bar vK.

Since ReB=l', division by-2i yields exactly

    delta eD = l'/(2pi)·tD + (bar vK−vK)/(2i).

The Deligne projection kills the declared tD and keeps the second
term. It is real in K. If vK=x+i w with x,w real, this component
is-w, not+w.

Finally, on a real K vector, f_alpha is2pi i ell_omega and
f_rhoD is2pi i bar ell_omega. Their sum on x is purely imaginary.
Their sum on i w has real part-4pi Re ell_omega(w). Therefore

    Re ell_omega(pi_-3 delta eD)
      =1/(4pi) Re(f_alpha(vK)+f_rhoD(vK)).

Substitution of(5.1) and eta_b=2log2 alpha−Lambda10−bar Lambda01
gives the last real part equal to-U_b(z). This proves the claimed

    h_(omega,b)(z)=−U_b(z)/(4pi),
    q_F(z)=−(h_(omega,b)(z)−h_(omega,b)(infinity))/c_pi.

Both minus signs, the2pi i comparison, and the final4pi are thus
fixed by the actual frames. No regulator or unknown BSD coefficient
has been used to rescale the construction.

## 7. Endpoint, averaging and arithmetic scope

At b=z the constant path line is retained; all displayed integrals
for that path are zero, consistently with the top unit and its
Deligne invariant. The cusp value in the theorem is the existing
finite LIMIT after principal-part cancellation. The proof does not
declare it a rational tangential-basepoint fiber.

For algebraic b,z the underlying object is the actual rational MHS
pushout, with compatible geometric Betti/de Rham source. The full
reduced fiber u=2 and all its conjugates are retained under
basepoint averaging, with its rational denominator. The normalized
Poisson formula is independent of the basepoint by the completed
uniqueness theorem.

The Deligne splitting, projections and the explicitly compared
elliptic period define a canonical REAL operation. Neither they
nor the averaging of its values are thereby rational motivic
morphisms. The result does not settle the marked motivic
obstruction, identify the Petersson pairing with an arithmetic
intersection, or prove a BSD determinant or integral lattice.

**PASS.** All seven sections have been checked in their stated
scope. No root proof, shared synthesis file or numerical certificate
was edited. The completed predecessor's normalization and the
universal BSD objective are unchanged.
