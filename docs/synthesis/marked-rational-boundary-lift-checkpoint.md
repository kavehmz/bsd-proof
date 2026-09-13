# Marked rational boundary lift — initial checkpoint

Date:2026-09-13. Owner /root/higher_period_integrality,
GPT-6 Astra/xhigh. Own only this checkpoint and
marked-rational-boundary-lift-attack.md.

Full BSD over Q remains the objective. This bounded task computes the
ACTUAL motivic connecting class of the known rational j_B(beta2),
restricted to mathcal S, in H_M4(K_F,mot(2)). The coefficient motive,
its top map, and existence of a real coefficient lift are completed
inputs; do not reconstruct them as new results.

Use the positive relative boundary, full divisor marking, fixed point
one-motive and rational h_j corrections. Seek an explicit motivic
cycle/cochain nullhomotopy or rational lift. Never infer motivic zero
from zero real regulator, divide by the unknown BSD scalar, or assign
zero trivializations to the actual nonzero added Poincare fibers.
Retain trace degree b, exterior projector2, all native Tate frames and
the actual Sigma boundary tuple.

Initial checkpoint saved before research. Next: read next-research-plan
§1 and the completed marked coefficient proof/review, then express the
boundary composite by the coefficient extension and the actual cusp
fiber object. No agents, shared/completed-proof edits or old reruns.
New deductions require separate independent review before promotion.

## First exact motivic formula saved

Working proof now contains Proposition1.1:
 O_W^M(j_B(beta2)|S) = -j^+_(B,F)(epsilon0 tensor beta2,0).
The minus is checked directly fromD(a,b)=(da,r a−db) and the
POSITIVE boundary(0,+beta2); it is not a guessed commuting-square sign.
The two cusp coefficient objects are canonically the fixedW0/F0
becausepi(c)=O andall actualKummerfunctions a_ij(O)=1.
The classchi=epsilon0 tensorbeta2 is an actual rational morphism
1→F0 tensorRΓ(E_t,Q2)[3]. Full vanishing is equivalent to the pair
(chi,0) lying in the image of globalF-coefficient restriction.
The diagonal(chi,chi) is already a global restriction; that fact
alone does not kill one component. Vanishing ofchi itself would
be a sufficient, not necessary, fiberwise lift criterion.

Next candidate to PROVE: the first derived-exterior graded component
iseta1 tensor e2−eta2 tensor e1, whereeta_j is the full corrected
semiabelian point extension. Its abelian quotient should identify
with(P−O)×beta2 and(Q−O)×beta2 inCH3(E×E,2)_Q, with the curve
Poincare-duality orientation fixed by positive cycle classes.
Do not omit the toric h_j/Kummer components or declare these productszero.

An important open-boundary distinction is now explicit: the proper
Chow relationdivu=388(c0−c_infinity) does NOT automatically identify
maps into the open motiveM(S), nor restrictions for nonconstantF.
The valuesu|Sigma remain in the generalized-Jacobian/relative boundary.
No assertion of injection of the old properj_B after restriction toS
has been made. Need compute the actual localization/coefficient term.

Root has been informed of this formula and boundary distinction.
All three other handles are live; this scoped goal remainsnull as
expected. No old arithmetic run or shared/completed-proof edit occurred.

## Concrete localization and unit-trace calculation to finish

For the CONSTANT first abelian coefficientD=H1(E)_hom tensorL,
proper-relative j_(B,D):H_M3(E_t,D2)→H_M4(C×E_t,B;D2) is injective
by the original proper Chow correspondence argument (tensor withD).
Restriction toS can have a kernel. Purity on the addedSigma gives
that kernel as the image of
 H_M2(Sigma×E_t,D(1)) → H_M4(properrelative,D(2)).
Thus no injection of j_B AFTER opening is assumed.

The ALREADY constructed right-cup/compact-traceT_u extends to
constantD coefficients. Its whole-group identity isT_u j_(B,D)=388id.
For a closed added point s and ζ_s inH_M2(E_k(s),D1), its projection
formula should give
 T_u i_(s,*)ζ_s = Tr_(k(s)/Q)(ζ_s RIGHT-CUP u(s)).
No new Tate scalar: Gysin(+1)[2] and smoothtrace(-1)[-2] cancel;
right cup has twist+1/degree+1, giving H_M3(E,D2) as required.
Therefore j_B(χ)=iSigma_*ζ implies
 388χ = sum_s Tr(ζ_s cup u(s)).
This would be an exact NECESSARY boundary-unit-span condition on the
point×beta2 first exterior products, with actual higherChowζ_s of
type projectedCH2(E×E,1). Full motivic lift is stronger.

A natural attempted correction can be tested: take ζ_s=e_s Res ξ_x
from a common downstairs removed pointx inSigma_E. SinceS is the
FULL inverseimage ofS_E, the entire fiber is present. Norm_pi(u)=±1
implies product_s Norm(u(s))^e_s=±1. Projection formula then makes
the sum of these particular trace/cup termszero rationally. This does
not prove χnonzero, nor rule out corrections not of that pulled-back
form. Root informed; full proof and source/formalism audit still needed.

Primary exterior-filtration lead found: Guletskii math/0306297v1,
§3.4Proposition19 gives the filtration in a rational monoidal model
category. Need directly open arXiv/author primary, not cite secondary
search text. For m=2 its first boundary is derived directly as
eta1 tensor e2−eta2 tensor e1, with fullG and native alternating frames.
Kahn–Yamazaki1108.2764 is a possible further symbol test; no vanishing
or Somekawa identification has been imported yet.

## SIGN REFINEMENT before final theorem (supersedes previous candidate sign)

The actual RIGHT-cup operator has the degree-dependent boundary rule
 T_u(j_B chi)=(-1)^r·388chi forchi inH_M^r(E_t,D(2)).
Indeedj_Bchi=e0 externalchi; movingchi past the rightmost unitu
has sign(-1)^r. The prior wholeK2 identity hadr=2, while herechi
hasr=3 and the sign isMINUS. Since the proper projected coefficient
obstruction isO=−j_Bchi, its trace is+388chi.
Thus O=iSigma_*ζ implies EXACTLY
 388chi=sum_s Tr(ζ_s RIGHT-CUPu(s)).
Hereζ representsO, not+j_Bchi. T_u iSigma_*ζ has no extra sign:
ζhasdegree2 and the projection formula retains rightcup order.
Root has been informed of this correction before final writing.

Primary Guletskii math/0306297v1 opened directly,36pages. Banner says
19Jun2003; retrievedPDFfrontdateis21Nov2018, so retain exactversion
rather than silently citing the published numbering. §3.4Prop19
(pp27–28) is inspected: actual model-category exterior filtration
withgradedpieces exterior^(m-i)quotient tensor exterior^i kernel.
Kahn–Yamazaki author40pagePDF Theorems1.5/11.14/12.3 inspected.
Its ordinary Somekawa identification appliesCH_(−r)(X,r), hence
onE² withr=1 givesCH3(E²,1), not ourCH3(E²,2). No vanishing
theorem for the needed product is supplied by changing that degree.

## Full eight-section draft now saved for independent review

Proof SHA256:
43fe51db76af4fdc7340507526878d27086539d6073f36a06870cc560ebde492.
No rational lift or motivic obstruction vanishing is claimed.
The full exact obstruction formula and its first point/K2 component
are now proved in the saved draft, with Guletskii's actual model
filtration, the rational point cycle chains and all signs retained.

New completed positive correction within the bounded attempt:
 sigma_ij={u,a_ij∘pi} initially onY'=S minusoldcusps extends UNIQUELY
rationally toH_M2(S,Q2), since both old-cusp residuesare1 and the
localization kernelH_M0(B0,Q1)=0. Ataddeds itsRostresidueis
u(s)^(−ord_s a_ij); atpointsabove−R it is−e_s[[4,3],[3,4]]κu(s).
Finite transfer toS_E is{Norm_pi u,a_ij}=0 rationally. This is an
actual rational K2 correction, not a chosen current or an assertion
that the fixed point×beta2 products vanish.

The full rational extensionF→W→1 projects via the derived exterior
filtration to the constantD=H1(E)_hom tensorL. Its point component
isκ(P)tensor e2−κ(Q)tensor e1. The CH3(E×E,2) representatives are
(P−O)×z_beta incolumn e2 and−(Q−O)×z_beta incolumn e1.
The literal rationalchain(h_j/m_(R,P_j))×z_beta identifies the
correctedZ_j presentation withthatproperpointcycle. It is NOT a
relative nullhomotopy onE minusA becauseP_j andO are punctures.

Purity gives the exact added-boundary kernel. The RIGHT-cuptrace
has(-1)^r boundarysign; atourr3 it gives−388 onj_B, hence+388 on
the actualobstruction−j_B. The finiteunitspan condition(5.4) is
NECESSARY, withzeta representingthe properprojectedobstruction.
Pulled-backzeta_s=e_s Res xi_x has zeroimage by the actualfiber
normNorm_pi u=±1. Noχnonvanishingorallboundarycorrectionvanishing
is inferred. The fullF-lift is strongerthanthefirstprojectiontest.

MVW27Jan2004/221pageprimary§4,Theorem7.16 and§19 inspected;
Theorem7.16 is the explicit relativePic/Suslin condition and its
proof requiresf|boundary=1. Kahn–Yamazaki40pageauthorPDF ordinary
Somekawacycle formula hasCH_(−r)(X,r), notourCH3(surface,2).
No vanishing theorem was imported bychanging that degree.
All coretrace/norm/CDpurity inputs are the already reviewed exact
maps; no old numerical/certificate test wasrerun.

Next: request independentreviewofthisfullstableproof. Address any
actualtype/sign/sourceconcern, then finishboundedstatus. Remaining
GAPMRBL-389 is anactualrationalnullcochain/globalrestriction lift
for(1.2), includingthefixedpoint×K2 andfullboundaryterms. Root's
Poisson framing task and sharedsynthesis are notedited.

## Additional actual Tate-component vanishing saved as§9

Current mathematical proof SHA256:
0da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2.

The actual point×beta2 cycles lie in cohomologicalh1 tensorh1.
Bothbeta2's h0/h2 components vanish byK2(Q)_Q=0 andH_M0(Q,Q1)=0.
The point divisor hasdegreezero. For an ellipticcurve the categorical
Sym²(h1_coho)=Q(-1)[-2]; its geometricPLUS projected group here is
H_M2(Q,Q2)=0. Thereforet^* z_P=−z_P andt^*z_Q=−z_Q rationally.
The remaininggeometricMINUS motive realizes ordinaryrank3Sym²H1;
no vanishing of that remaining product is proved.

Primary inputs directly read: Ancona–Enright-Ward–Huber1312.4171v2,
51pages,Theorem3.1.4/4.2.3/Prop4.3.5; its homological convention is
dualized explicitly. WeibelKbookIII73pagePDF5.2.2/6.5.1 gives the
exactDIRECTSUM tame quotient andK2Z=Z/2. Ancona–Huber–PepinLehalleur
1409.3401v2Theorems3.3/3.7 was also inspected, but the saved theorem
uses the former field-level primary source. No changed degree or
realization-faithfulness inference is used. This is the final bounded
additional component test before independent review, not a full lift.

## Bounded construction handoff

All nine sections are saved with full proofs and exact primary references.
The stable proof hash remains0da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2.
No mathematical change followed that revision. Root has the stable revision
and has been asked to route the independent audit on an existing handle.
There is no PASS verdict yet and no mathematical process running.

The completed bounded output is the exact obstruction and component tests,
not its vanishing or a full rational lift. On resumption read this proof,
then the actual independent review if one has been created. Do not repeat
old certificates, rebuild the completed coefficient motive/real lift, or
spawn a new agent. Resume the same Astra/xhigh handle for reviewer concerns
or the coordinator's next concrete assignment.

## New reciprocal review active

Root assigned review-poisson-hodge-framing.md for its new Hodge-framing
proof8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210.
This agent remains Astra/xhigh and owns only that review plus this status
addition while auditing it. Root separately audits the marked-boundary
construction. No parent proof/shared file or old certificate is to be edited.

## AUTHORITATIVE COMPLETION — independent reviews finished

Date:2026-09-13. All nine marked-boundary proof sections passed the
independent coordinator audit in review-marked-rational-boundary-lift.md,
review SHA256322af5b8356ea08a755804040b00095a31db177dc15740d5f6b18d0c7a353368.
The reviewed mathematical revision remains0da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2.
Final proof after editorial PASS/header/conclusion links only:
ddfdd2d3de3708b1f0bba359e79d87de7154fc2e0e5e6cc34bac98c3da3f47dc.
No numerical or mathematical formula changed after review. Earlier
working/candidate/pending-review snapshots in this checkpoint are historical.

The reciprocal Poisson Hodge-framing review is also COMPLETE PASS:
review-poisson-hodge-framing.md, SHA256
b88f4ecf7056253deac4c278a26aa23fdaa7522c4b922c707420238abc5caea9,
against root mathematical8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210
and checkpoint1cca1b98cde8e991c0e5ae42c5229aaa2b92ac312c3131c0b5f6aaff3d9de22d.
All ordered-path, logarithmic F1, Deligne constant/I00, real lift and
exact h=−U/(4pi) calculations pass without correction. Root proof and
shared synthesis were not edited.

Remaining MRBL-389 is the actual full rational obstruction/nullcochain,
including its non-Tate point×beta2 component and actual added-boundary
selection. No rational spectral input, BSD scalar or integral lattice
comparison has been proved. Full universal BSD remains active at root.
No process is running. Report final hashes, then await a new bounded
assignment on this same Astra/xhigh handle; no old computations or agents
need restarting.
