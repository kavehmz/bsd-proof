# Independent review of the level-Nv toric construction

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. **Verdict: PASS for the stated bounded deductions.**

Reviewed [proof](heegner-toric-vanishing-attack.md), SHA256
`56a1027562e985a6da108d03a3eb510bcf757f93f9c8f2960fb5945036721fc1`,
and its [checkpoint](heegner-toric-vanishing-checkpoint.md).
The proof does not establish its remaining TV-TP5 vanishing or full BSD.
No formula correction is required. Editorial PASS links and removal of
historical initial-checkpoint instructions do not change this verdict.

## 1. Actual CM lift and the cusp correction

I checked the source/target degeneracy interpretation and identities
directly in Bertolini–Darmon, *Euler systems and Jochnowitz congruences*,
§2, printed source pp.7–8, and the conductor-one norm statement in
Proposition 5.1 ([primary author PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/21.Jochnowitz/paper.pdf)).
The extension to conductor m in the reviewed note is proved by its own
CM-isogeny orbit calculation, not silently supplied by the
conductor-one statement. The unit quotient is one in the stated
discriminant range, so the fiber/orbit has v+1 elements.

The two points over the old infinity cusp have indices 1 and v.
Thus, before quotienting by torsion,
$$\alpha^*[\infty]=[\infty]+v[c_N],\qquad
\operatorname{Tr}z-\alpha^*Z=v\operatorname{aug}(A_m)C_v.$$
The positive sign and the augmentation
$h_K\ell(\ell+1)q(q+1)/4$ are correct. Both degeneracy maps send
$c_N$ to the old infinity cusp. The use of this cusp class only in
rational formula (9) is consequently legitimate; it has not been
discarded inside an integral point equality.

## 2. Projector, other-old term and actual integral division

The four degeneracy compositions give exactly
$q_vj=d_\pi\Delta_v$. Since $v+1>|a_v|$, its determinant is nonzero.
The stated rational projector is idempotent and is the identity on the
image of j. Its two eigendirections have denominators
$2d_\pi(v+1\pm a_v)$, with both factors retained.

For the trace, applying the inverse matrix to $(M_vP,a_vP)$ gives
$(P,0)$. This independently recovers the other-old contribution
$\alpha^*(1-iq_E/d_\pi)Z$ in (9). The complement is correctly not
called entirely v-new.

Let $A=\operatorname{adj}(\Delta_v)$. The identity
$p^k(B_1,B_2)=A(P,Y)$ proves
$$q_v\bigl(d_\pi d_vz-p^kj(B_1,B_2)\bigr)=0$$
as an exact point equality. The inequality $v_p(d_v)\ge2k$ makes
the declared $W^{(1)}$ integral and gives its reduction (12).
No p^k-division of an unspecified rational point is used. The trace
calculations give exactly $(d_v/p^k)P$ and zero for $B_1,B_2$.

## 3. Reduction, Frobenius and the full coefficient

The ring-class extension is totally ramified at the new inert prime,
while its lower completion is the unramified quadratic local field.
Specialization of the chosen degree-v CM isogeny has Frobenius kernel
on its supersingular source. Hence $\overline Y=\mathsf F\overline P$
with the same weights. The two polynomial identities in Proposition
4.1 follow directly from $\mathsf F^2-a\mathsf F+v=0$.

Choose $p^kQ=\overline P$. Substituting this in the INTEGER
coefficients defining $B_i$ gives
$$\overline B_1=-(\mathsf F^2-1)Q=-x,\qquad
\overline B_2=(a-\mathsf F)x=-\mathsf Fx.$$
Thus the divisions cannot introduce a hidden sign or a lower
coefficient modulus. The raw two-prime plus sign gives $\mathsf Fx=x$.

I checked this against Howard, §1.7, especially the explicit cocycle in
Lemma 1.7.2 and the reduction calculation in Proposition 1.7.4
([primary version](https://arxiv.org/html/1202.6340#S1.SS7)).
Equation $(\sigma_v-1)D_vY=p^kB_2$ supplies the specified correction
term, so the raw three-prime transverse value is
$-\overline B_2=\mathsf Fx$. The separate actions $\mathsf F$ and
$v^{-1}\mathsf F=-\mathsf F$ and the already reviewed scalars
$u_2=u_3=-1$ are preserved. No Q-to-K factor two belongs in this
K-local equality. Detection retains its stated full-image hypothesis.

## 4. The nonvanishing proposal and its actual height term

The character calculation is exact. On characters trivial at $G_v$,
$e_\chi Y=(a/M_v)e_\chi P$, whence $e_\chi B_2=0$. On every
other character $e_\chi P=0$ and
$e_\chi B_2=(M_v/p^k)e_\chi Y$. Expanding the derivative operator
gives precisely the two cases in (18).

The primitive-conductor trace contributes one $a_r$ for each omitted
fresh inert conductor prime, and its height contributes $a_r^2$.
The factor $M_v^2/h_{mv}^2=1/h_m^2$ explains all the cancellation
in (19). I read the elliptic-quotient statement of Cai–Shu–Tian,
Theorem 1.1 directly ([1408.1733v2](https://arxiv.org/html/1408.1733#S1.Thmthm1)).
Its $d_\pi$, $c_\chi\sqrt{|D|}$ and $8\pi^2(f,f)$ give exactly
the stated prefactor. The common-discriminant and unit corrections
are one under this note's hypotheses. Heights stay in the source's
fixed K convention.

Thus only characters with v in their primitive conductor survive.
No theorem relates their first derivatives to the untwisted third
derivative vanishing used in the proposed repair. The torsion criterion
is sufficient: $E(L)[p]=0$, and a prime-to-p torsion point cannot reduce
to a nonzero p-primary point. The note correctly does not make this
criterion necessary for vanishing of the reduction.

## 5. Local Euler factor and final scope

Squaring the two good Frobenius eigenvalues gives
$Q_v(s)=1-(a_v^2-2v)v^{-2s}+v^{2-4s}$ and
$Q_v(1)=d_v/v^2$. The product rule proves (22) with exactly the
lower derivative hypotheses stated. Its characteristic-zero nonzero
factor is not an integral unit at p. The separate Steinberg
base-change factor belongs to a different level-raised eigenform;
the note does not substitute it for E's good local factor.

The final remaining statement concerns the actual reduction of $B_2$,
not its automatically vanishing trace, the cleared projector, or a
height on an unspecified cohomology class. All geometric and finite
identifications checked here leave that vanishing open. No old
certificate or numerical computation was rerun for this review.
