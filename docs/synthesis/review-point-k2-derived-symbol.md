# Independent review of the actual point–K2 derived symbols

Date:2026-09-13. Reviewer: root/coordinator.
**PASS for all eight sections after the explicit cancellation-source
precision.** Reviewed [proof](point-k2-derived-symbol-attack.md), mathematical
SHA256 `3cf1c40dada9ed02f7e724c3db9a3f36c04449e61bb979857a94be38f1bbed36`,
and [checkpoint](point-k2-derived-symbol-checkpoint.md), snapshot
`750f505ea2fcc4a86d7ec581b447225a27e1d450cbff3869537982013e102a07`.
The initial mathematical revision was42ff4d66...; no formula changed.
The first-difference vanishing and full rational lift remain open.

I read the full proof, reconstructed its degree shifts, coniveau sequence,
Miller divisors and every tame boundary, and opened the actual primary
sheaf-tensor, cancellation, evaluation and coniveau sources. No numerical
certificate or old calculation was rerun.

## 1. The derived degree and the effective category

With A the homological M1(E), curve duality gives h1_coho=A(-1)[-2].
Two such substitutions in twist3/degree4 leave A tensorA(1), which
is A tensorA tensorGm[-1]. The two shifts being even, they preserve the
geometric MINUS projector. This is not the degreezero Somekawa group.

I required the stable-to-effective step to be stated explicitly. The
added paragraph now uses [Voevodsky math/0202012v1,
Corollary4.10](https://arxiv.org/pdf/math/0202012): Tate twist is fully
faithful over the perfect field Q. The stabilization colimit therefore
does not change these Hom groups. The unit, A and Gm are effective
geometric objects, and the assertion respects their shifts and rational
summands. This supplies the actual justification rather than silently
using an effective formula in the stable category.

## 2. The sheaf tensor is exact before A1 localization

I checked [Sugiyama, published AppendixA PropositionA.1 and
CorollaryA.3](https://ems.press/content/serial-article-files/26252?nt=1),
the24-page Documenta Mathematica19(2014) version. Its exact tensor is the
rational Nisnevich SHEAF tensor with transfers. This justifies the
pre-localization derived tensor of the degreezero sheaves. It is not
the naive pointwise tensor of point groups and not a theorem that
motivic localization is t-exact.

[Kahn–Yamazaki, Lemma3.3 and equation3.2](https://webusers.imj-prg.fr/~bruno.kahn/preprints/Somekawa-Voevodsky31.pdf)
identify the motivic tensor with C_*(derived sheaf tensor) and morphisms
from the unit with evaluation of the corresponding cohomology at the
field. Nisnevich evaluation there is exact. Thus the [-1] shift gives
H_1 of the actual simplicial transfer-sheaf complex, as asserted.

The same calculation for beta gives Hom(1,A(1)), also in Suslin degree1.
Its previously computed nonzero regulator proves that this actual
degree1 class is nonzero. This is a concrete reason that discarding
degree1 cannot solve the desired product problem. The rational point
section acts on that actual complex; no unproved tensor flatness after
A1 localization has been inserted.

## 3. The Gersten complex computes the full group

The exact indexing in [Déglise1106.0905v1, equation2.1.c and
Proposition2.7](https://arxiv.org/pdf/1106.0905v1) gives
E1^(p,q)=sum_x H_M^(q-p)(k(x),Q(3-p)). On this smooth surface in
total degree4, (0,4) vanishes because field motivic degree4 exceeds
weight3, and(2,2) is H_M0(field,Q1)=0. Only(1,3) can remain.
Its row is K3^M of the generic field, K2^M of divisors and K1 of
closed points. No higher differential can enter or leave(1,3) in
dimension2. Therefore its H1 is the WHOLE CH³(X,2)_Q, not merely
one graded part whose extension to the target is unknown.

The residue differential retains divisor normalizations and finite
transfers. The Kummer-first positive-uniformizer convention gives
partial{pi,a,b}={a,b}. For unramified beta it yields ord(f) times
its specialization in partial{f,beta}. The unramified hypothesis
holds for the actual generic beta from its curve class. At the only
horizontal divisors of M_R with nonzero order, the specialized point
is rational O or-R, and K2(Q)_Q=0. No arbitrary function-field K2
vanishing is assumed. WeibelIII5.2.2 is now correctly called Example.

## 4. Full Miller divisor on the actual generalized Weierstrass model

The inverse points are-P=(-1,-2) and-Q=(0,0). The displayed slopes
and x-coordinate addition formula give exactly the two rational
functions(4.2), including a2=1 and a3=1 of this model.
Generically in s their horizontal divisor is
Delta-Gamma_-R+H_-R-H_O.

The possible vertical contributions require separate calculation.
At s=R the slope has a simple pole because2y_R+1 is3 or-1. The
numerator has pole order1, the denominator pole order2, so their
ratio has a simple zero. At s=-R the slope has its regular tangent
limit and the function is generically nonzero. At O the slope has
a simple pole but x(s-R) approaches x_R; the ratio has a simple
pole. Away from these possible slope singularities the monic-y
numerator and variable x_t denominator cannot vanish identically
along a vertical fiber. This proves the complete extra V_R-V_O.

Thus the full divisor in(4.3) has every component with the asserted
multiplicity. Omitting its vertical terms would indeed discard
the exact class being investigated.

## 5. First-difference cochain and its residual terms

At V_R and V_O, d{M_R,p_t*beta} gives beta and-beta. At Delta it
gives+Delta_*beta. At Gamma_-R it gives-beta in the t coordinate.
Parameterizing that graph by t identifies it with -(tau_R×1)_*D_beta.
This does not replace the coefficient by a translated beta on the
test factor. The horizontal O,-R specializations vanish rationally;
all other residues arezero by the actual unramified product rule.
Norm/projection compatibility retains the fixed norm-symbol presentation.

I therefore obtain exactly dTheta_R=z_R+D_beta-T_R D_beta.
In the proved Gersten model this gives z_R=(T_R-1)D_beta. The
diagonal cycle is geometrically invariant, and the already proved
Tate/PLUS vanishing of z_R gives e_-T_R D_beta=z_R. Translation
on one factor does not commute with the interchange, so this is
not a zero of that remaining geometric MINUS component.

These are literal rational K3 cochains in the exact Gersten complex.
The proof does not claim that an unmodified symbol graph is already
a globally admissible Bloch chain without any localization/moving
comparison; the proved Gersten identification is the bridge used here.

## 6. Filled second difference and its exact signs

On the actual point divisor,
(T_S-1)z_R=z_(R+S)-z_R-z_S. The Miller divisor gives
d{m_RS(s),beta(t)}=z_R+z_S-z_(R+S). Hence the negative of this
cochain has boundary(T_S-1)z_R. Translating the first boundary
identity and subtracting it gives
dXi_(R,S)=(T_S-1)(T_R-1)D_beta, with precisely the signs in(6.2).
Pushforward of a function by tau_S is its expression at s-S;
this verifies the single-symbol quotient in the second line.

For P,Q the slope is-2 and m_PQ=(y+2x+1)/(x-4), as displayed.
Their sum(4,8) is the inherited rational point, so no exceptional
chord case is used. The actual second difference is thus filled,
and the same divisor relation makes R->z_R additive. Neither
statement produces a filling of its first difference.

## 7. Verdict limits and full marked interface

The derived model, exact Gersten computation and both explicit
cochain identities pass. The proof keeps the full h_j marked
corrections and does not trivialize their toric restrictions or
added Poincare fibers. The global coefficient obstruction is still
-j_B(epsilon0 tensorbeta,0), and the degree3 RIGHT-cup trace on
+j_B is-388. Its leading minus therefore leaves+388 in the actual
necessary Sigma-unit relation. The earlier pulled-back-pattern
vanishing is not extended to all boundary corrections.

The remaining task is a first-difference K3/Suslin filling, or the
actual full coefficient restriction preimage, followed by the
remaining toric/exterior and rational spectral comparisons. No
BSD rationality, integrality or counterexample is inferred.
