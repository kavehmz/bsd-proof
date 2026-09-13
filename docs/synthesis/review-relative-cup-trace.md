# Independent review of the relative compact cup and trace

Date: 2026-09-12. Reviewer root/coordinator.
**PASS for all six sections and their stated scope.**
Reviewed [proof](relative-cup-trace-attack.md), mathematical SHA256
754373e0d23a81096abca7d1617ab142d6901f1988672a1e1643e1240306c059.
Reviewed [checkpoint](relative-cup-trace-checkpoint.md), SHA256
83771006082b3cee4b63c55dce024a3bb841f7a9c81ba4eb94b012fb5b3e1fe3.
Subsequent completion and review-link edits are editorial.

I read the full proof and checkpoint, reconstructed the motivic degree
and sign and every native-form scalar, and checked the cited primary
purity, compact-support and regulator inputs. The result is an actual
rational retraction and a full real Deligne image. It does not prove a
rational lift of the spectral class, a rank-one rational K2 group, or BSD.

## 1. The rational morphism is typed and uses compact support

The displayed cohomological compact-support convention agrees with
[Déglise, Definition1.5 and §1.6](https://deglise.perso.math.cnrs.fr/docs/2014/beijing.pdf).
For f:Y×E→E, the unit acts on f_!1; this is not a push of an
ordinary open-cohomology class. I checked
[Déglise–Fasel–Jin–Khan, TheoremA(I),(II),(V)](https://www.numdam.org/item/JEP_2021__8__533_0.pdf),
printed p534: its PLUS rational motivic category is canonically
oriented, has the stated purity isomorphism, and identifies with
rational motivic modules. The paper's full rational homotopy category
has a weaker orientation; the proof correctly uses TheoremA.

Here f is smooth of relative dimension1 between regular schemes,
so f^!1=1(1)[2]. The counit therefore sends f_!1(3)[4] to1(2)[2].
Composing with the actual degree1/twist1 unit gives degree2/twist2
on E as asserted. The factorization through j_!j^! followed by
the PROPER projection p:X×E→E is the counit's composition law.
The relative/compact identification is the same proper-pair
localization already checked for the preceding two constructions.

## 2. The entire K2 composite, including its sign

The relative positive boundary has e0=(0,1,0) in the actual fiber
cone and is opposite the canonical boundary under the declared
ordinary projection. Since beta has degree2, moving it past the
degree1 unit introduces no sign. Thus projection formula really
reduces the full composite to lambda times the identity, where
lambda lies in End(1_Q)=Q before realization.

Subtracting the differential of rho gives the compact Betti
representative -d rho. On the punctured compact curve,
the inner boundary around0 is clockwise. With rho=1 there,
integral d(rho du/u)=-2pi i(N-1). Multiplying by the minus sign
and the trace normalization(2pi i)^(-1) gives lambda=N-1.
The nonzero local holomorphic unit factor contributes no residue.

This uses injectivity only for the scalar Q→C on the unit object.
It does not infer faithfulness of Betti realization on K2 or
equality of general motive morphisms from equal periods.
Therefore T_u j_B=(N-1)id holds on the WHOLE motivic K2 group,
and R_u=T_u/(N-1) is an actual rational retraction.
The denominator388 is retained, including its primes2 and97.

## 3. The actual native Deligne product and trace

I checked the total/concise maps and products in
[Burgos–Goswami1712.10150v2, §§4.3–4.5](https://arxiv.org/html/1712.10150v2),
together with §4.1's current convention and Proposition5.5's
proper regulator compatibility. Its proper-projective hypotheses
apply AFTER the proof's extension by zero to X×E.

For c=2pi i S and l=log|u|, a right-product total representative
has third component 2c∧partial l-l partial c+l barpartial c.
Projection to the real degree-four/twist-three form, using bar c=-c,
gives
$$
 c\wedge(\partial l-\bar\partial l)
             -l(\partial c-\bar\partial c).
$$
The homotopic symmetric total product gives the same projected
expression here. The curve trace divides by2pi i, yielding
exactly the proof's Theta_u(S), with its derivative term retained.

For closedness, da_l=-2partial barpartial l=0 on Y and
d(partial S-barpartial S)=-2partial barpartial S=0.
The remaining terms cancel: after deleting the impossible
(3,1) and(1,3) terms on a surface, both dS∧a_l and
dl∧(partial S-barpartial S) equal
-partial S∧barpartial l+barpartial S∧partial l.
The output is therefore a closed imaginary one-form.
Relative boundaries map to Deligne boundaries by the actual
product and trace. The smooth representatives vanish near both
cusps, so no singular current restriction or unproved boundary
limit is hidden here.

The integration-by-parts rewrite with
A(S)=integral_Y lS retains the E-derivative of A(S).
For the translation-invariant radial representatives it is
constant, but the general operator is not defined by dropping it.

## 4. Independent evaluation of the coefficient

Let I=integral_V S∧omega_E∧barpartial l.
In integral_E omega_E∧Theta_u(S), the first surviving term is-I.
Compact Stokes on barpartial(l omega_E∧S) gives the second-I;
the other two terms vanish by type. Therefore the result is-2I.
Since P(S)=iI/(4pi²c_pi), this equals8pi² i c_pi P(S).

For Theta=i eta in the arithmetic real eigenspace,
Riemann bilinearity gives integral_E omega_E∧eta
=omega1 integral_b eta. Thus
$$
 \mathscr R_E^{\mathcal D}(T_u^{\mathcal D}[S])
                   ={8\pi^2c_\pi\over\omega_1}\mathscr P(S).
$$
On the boundary cutoff S=(d rho∧eta)^(1,1)/(2pi),
both cusp integrals are pi i(N-1); direct substitution yields
the full native form i(N-1)eta. This independently checks both
the motivic composite and the old beta2 period normalization.
The named omega1 is retained; Omega_E=2omega1 is not replaced
by the primitive period.

## 5. Full real image and the remaining arithmetic distinction

In the concise complex for a projective curve and twist2,
degrees1,2,3 are imaginary functions, one-forms and two-forms,
with the first two differentials-d. Hence H_D²=i H¹(E,R).
Geometric conjugation combined with coefficient conjugation fixes
i H¹(E,R)^minus. Since c(a)=a and c(b)=-b, this real space is
one-dimensional and its b-period is an isomorphism.

The input radial class and the rational cup/trace have this real
structure. Substitution of the already proved Mellin value thus
determines their FULL real Deligne image:
$$
 R_u^{\mathcal D}(\mathcal C_{j_2})
       =-12Nc_\pi{\ell_E\over\omega_1}\,r_{\mathcal D}(\beta_2).
$$
The same one-dimensional argument justifies the stronger projected
Gamma-completed class equality from the established lower scalar
vanishings. Those lower terms are not discarded from the unprojected
relative source.

The coefficient still lacks Reg_E. Even a hypothetical rational
relative input would give some rational K2 class, without proving
that it belongs to Q beta2. The proof preserves that distinction
and makes no rational-rank or regulator-injectivity assertion.
The remaining RCT-389 comparison is correctly open.
No old certificate or numerical calculation was rerun for this review.
