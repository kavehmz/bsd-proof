# Local CM point comparison — initial checkpoint

Date:2026-09-13. Owner: root. Full BSD remains active and unresolved.
CURRENT STATUS: all six sections and the sharper P-or-Q consequence
have passed independent review. Core review f2242d2b... covers repaired
8fad3936...; numerical review c64bb530dd9201b58bd2611a660ab190c1ccb14829fd37a1d150d2449bd63392
covers the six-section2b221093... revision and proves the additional
P-or-Q refinement separately in its§8. Root read both full reviews.
Historical candidate/pending language below is superseded by this status.
The capacity error was resolved on the SAME Astra/xhigh handle, with
no new arithmetic run. Both independent programs and outputs are durable.

The preceding goal turn made progress: two independently reviewed
constructions were saved and integrated. Its partial manifest verified
234 artifacts,892 links,nine certificate JSONs and six dependency hashes.
Those are snapshots while agents continue; no old numerical run is needed.

Current companion state: odd completed cm-asymmetric-ray-attack.md at
39b60a777aa5447ff2cd14348b39bbd3b9b806d330a39f1f335b1b2846bb0a64,
sent it to uniform, and is moving to the cofactor review. Higher is now
constructing the actual Poisson source motive in new owned
poisson-path-motive-attack.md / poisson-path-motive-checkpoint.md.
Root has read the entire CM draft. Its claims remain subject to uniform's
separate review; root must inspect that review before promotion.

## Root bounded target

Use the ACTUAL semilocal norm-compatible units in CM draft§8:
U_(a,m)(R)=Theta_a(beta_m+[barpi]^-m R)/Theta_a(beta_m),
for R in the pi-adic formal group, beta_m=Omega/(f0 barpi^m).
All norms are on the full unramified semilocal ray algebra; rho is the
original inverse conjugate CM character. Its normalized finite Kummer
transfer defines U_pi(R) in H1(Qp,T_pi), asserted finite in the draft.

Goal of this substep: compute the PARTICULAR local point map, testing
whether it is additive/linear and giving an explicit comparison with
the actual pi-Kummer map in the original frames. Do not assert linearity
merely from the rank-one target. No adjustment of the arithmetic boundary
parameter c in CM draft(24) is allowed to fit a desired BSD value.
The normalized proper point line is an ACTUAL A_k line with generator
the pi projection of the universal[p^k] Kummer torsor; its compatible
boundary selection has a Zp ambiguity. A canonical local comparison
would constrain this parameter, but global gluing/other local conditions
and full BSD are additional requirements.

Potential approach to test, NOT proved: express the twisted local Kummer
map through Bloch-Kato logarithms and normalized Coleman theta functions,
then use connected pi-isogeny norm and opposite-ray Frobenius to control
the formal Taylor coefficients. A norm-compatible local family alone
does not imply additivity, nonzero selected-rho class, or a global ray
section. The draft explicitly proves deep global-ray nondescent, while
its selected-rho local class may still be zero.

Preserve q_(a,0,k)=12(a²-u_a), u_a=Psi^c((a))=±a;
Theta_a=Delta_E^(a²-1)psi_a^-12; a5 except atp5 a7;
gamma_CM=2pr_rho gamma_E^+; all pi/barpi embeddings, primitive-ray
Euler factors and actual Kummer([pi^k] versus[p^k]) unit factors.
No old certificate/prime scan, extra agent or shared predecessor edit.
Write complete deductions in cm-local-point-comparison-attack.md if any;
separate source facts, proved identities and unresolved analytic claims.

## Five-section candidate now saved for separate review

Full draft cm-local-point-comparison-attack.md has been written. It uses
a matched formal isomorphism eta_j with period Omega_j, calibrated to
the ORIGINAL coefficient t_rho. Any ratio to the independently chosen
Katz Omega_p is a declared frame unit and is not silently1.
For D_omega and L_(a,d)=D^(d-1)(DTheta/Theta), the actual weighted sums
C_(m,d)=Omega_j/q_a·barpi^(-md)sum_g rho_m(g)L_(a,d)(g beta_m)
have integral limits C_d inZp, with coefficientwise errorp^m uniformlyd.
The degree-p norm gives sum_h L_d(gh beta_(m+1))=barpi^d L_d(g beta_m).
The Frobenius period relation cancels the original rho weights.

Candidate exact local comparison:
Log_omega U_pi(R)=F_a(log_E R), F_a(z)=sum_(d>=1)C_d z^d/d!.
Finite approximations have uniform errorp^(m+1) onpZp. The proof uses
the actual finite-flat connected Kummer isomorphism by Cartier duality,
not target dimension; its descent/modulus argument needs close review.
The full semilocal trace and the coefficient vector action are retained.

Linearity is equivalent to all C_d for d>=2 vanishing. For the three
fixed multiplied rational points, a common scalar is equivalent to the
two explicit defects in§4 vanishing, with scalar integral by the bound
F(z)-C1z in p^(2v_pz). No coefficient/defect/nonvanishing is proved.
This draft is NOT promoted before a separate review and completion of
the companion asymmetric audit. Next root action: inspect those reviews,
then route this draft to an available existing Astra/xhigh handle.

## Review repair: finite flat descent

Uniform reconstructed the period sign and coefficient limits, and required
an explicit injectivity proof at the integral cohomology descent step.
The root proof now uses Witt invariants to descend Omega_j log(v) modulo
p^(k+1), chooses P_L with that logarithm, and checks that its difference
from the W-point is p^k times a formal point. The actual finite flat
isomorphism identifies H1(O_L,G_pi,k)->H1(W,G_pi,k) with the INJECTION
pO_L/p^(k+1)->pW/p^(k+1), via unit Kummer, Teichmuller divisibility and
Picard-zero of the two integer rings. This proves equality of the torsors
after their comparison over W. Faithful flatness alone was insufficient
justification and is no longer used for H1 injectivity. The full review
is still running. The companion asymmetric proof has now passed review.

## Further coefficient lead: retain its unresolved denominators

Primary BKT0711.1701v2 HTML was inspected at Remark2.12 and Lemma4.18.
Its ordinary unsmoothed torsion value F_(z0,1)(0) at order prime to the
chosen IDEAL pi satisfies(1-sigma/barpi)F=F1^(p)(z0). A finite-orbit
formula has denominator1-barpi^-n. This need not be uniformly a unit as
the opposite ray level grows. BK0610163v4 Cor2.16–17 gives integrality
for order prime to the rational p, which does NOT directly include beta_m.
Therefore a tempting smoothing/reindexing cancellation of C1 cannot be
promoted to C1=0 by assuming these unsmoothed values uniformly integral.
No C1 vanishing claim has been made. For derivatives of order>=2 the
unsmoothed derivatives reduce to rational wp derivatives, suggesting
better bounds, but no additional theorem is yet written or reviewed.

The same primary BK§2.4 explicitly warns that torsion translation and
formal logarithm evaluation cannot be interchanged: a nonzero connected
torsion point has logarithmzero but the formal multiplicative isomorphism
still has nontrivial torsion value. No translation-invariance/linearity
argument based on the invalid interchange is used in the root proof.

## New targeted finite-field test being prepared

NEW script compute/scripts/cm_local_taylor_mod5.py tests the local Taylor
sums atp5,m1,a7, not the original cyclotomicc2 certificate. It constructs
the actual CM image from Frobenius endomorphisms at good split primes,
checks its order4608 and trivial intersection with Gaussian units,
then evaluates the four derivative sums on an exact primitive
f0 barpi-torsion orbit inE(F_(5^24)). A primitive point need not match
the analytic embedding to test ZERO/NONZERO: all choices differ by the
CM image and a Gaussian unit, which multiply each sum by a nonzero
character/weight scalar. Exact values in the old period frame are NOT
asserted from that freedom. Every required point-annihilator, orbit and
Frobenius-eigenvalue check is included; the mathematical source and the
calculation will still need separate review before promotion.

If the QUADRATIC local Taylor coefficient is a unit, the full three-point
additivity defect has leading C2*x*y and cannot vanish for nonzero x,y
in5Z5; all higher terms have strictly larger valuation. This would test
the particular local scalar comparison, not disprove BSD. No result is
asserted before the run and independent inspection.

The NEW Sage calculation was launched with
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python
compute/scripts/cm_local_taylor_mod5.py. Its authoritative exec session
is52006. Poll this SAME handle before any restart; no output had arrived
at the initial1-second yield. All earlier certificates remain untouched.

## New finite calculation completed; extra audit required

Session52006 completed exit0: CM image and orbit both4608; local Taylor
sum zero/nonzero pattern[false,true,true,false] for d1..4. The script was
then strengthened by the direct primitive-point Frobenius assertion and
relaunched as session16250; POLL that same handle before any further run.
Root's separate exact rational group-law check(session99511, completed)
gave v5(t(64P)),v5(t(64Q)),v5(t(64(P+Q)))=1,1,2.

The full additional §6 now records the actual CM-image calculation,
primitive torsion/finite-field model, rational differential recurrence,
Gaussian-unit independence of zero/nonzero and the candidate inference
C2 is a5-unit. Its exact additivity defect has valuationv5(x)+v5(y);
thus at the original multiplied P,Q its log valuation is2 and local
lattice valuation1. No single proper-line scalar matches all three,
and at least one selected local class is nonzero. This is NOT the
old cyclotomicc2 coefficient, not a global Selmer statement, and notBSD.
It needs a separate independent arithmetic/source audit. The corefive
sections remain under uniform's audit at repaired revision8fad3936...
before this additional mathematical section.

## Current completion and review snapshot

Session16250 completed exit0 with the same[false,true,true,false] pattern,
including the new direct[pi]B Frobenius check. No root numerical session
remains live. The script/data hashes are respectively
0fffae4120bc9a2632bc174444832fea0bb3f91450bdc984e594d2ee0e336586 and
900a9060c40de02e5d541276d358938a7929b6538f4fef23db31f6954462c307.
The six-section proof is2b2210930ef8ee5419055ec5b83965551b09d72f0c0a485ffdcf1de7f4e14f25.
Uniform's complete corefive-section PASS is saved in
review-cm-local-point-comparison.md, hash
f2242d2b6b8655c6eb67180719163a47bd77836b810882f23befb029f7ca69e0,
at repaired8fad3936...; root read the full review. Higher is independently
reviewing/reproducing §6 in review-cm-local-taylor-certificate.md.
No §6 promotion yet. Odd's cofactor audit is still running.

Root read and independently reconstructed all seven sections of higher's
actual Poisson source-motive draft d1b1a3f3fe290c8754d63c526973f1405a9398f3353f870d81ba5bdefbeaa1c3.
review-poisson-path-motive.md now records PASS, including labelled
coincident endpoints, chronological tensor-shift sign, exact zero
augmentation nullhomotopy and finite-base averaging. This source
construction is complete in its scope; rationality of delta remains open.

## Independent NEW arithmetic reproduction preserved

Higher reports that its independent run passed with point i·B outside the
original H orbit, a different O/(mu) normal form, direct Legendre counts,
deterministic Frobenius witnesses and Hasse/Taylor-flow derivatives.
Root read the full verifier/output and preserved them BYTE-FOR-BYTE as
compute/scripts/verify_cm_local_taylor_mod5.py, hash
72c397c20fcb27e250b282d950305fc36493a4ef1b8231be276adec0eb788027,
and compute/data/cm_local_taylor_mod5_independent.json, hash
a9c2cc60c05adeee2f06d17c33a16435c0b6c5f5b9ab8bdbf7621e050e7c31ae.
The original execution paths were /tmp/cm_local_taylor_independent.py/json.
The preserved verifier intentionally retains its original workspace ROOT
and /tmp output destination so its exact audited bytes/hash stay unchanged;
its two input artifacts and full output are now durable in the repository.
It independently verifies field irreducibility, Frobenius order24, all12
CM generators, group/orbit4608 and exact Gaussian-unit scaling of the sums.
Fraction doubling reproduces valuations1,1,2 and normalized residues4,1,4.
The detailed audit file is still being finalized. No original output changed.

## Temporary reviewer capacity failure and same-model recovery

The higher_period_integrality turn returned a terminal model-capacity error
AFTER reporting and saving the independent arithmetic reproduction but
BEFORE expanding the24-line review-cm-local-taylor-certificate.md skeleton.
Root inspected the actual files: the source-motive editorial PASS links
were also not yet applied. No calculation or source artifact was lost.
Root re-dispatched the SAME Astra/xhigh handle to finish only that audit
record and its owned editorial completion. No model was changed and no
numerical process was restarted. Revalidate the actual handle on resumption;
this is not a three-goal-turn external blocker and the goal remains active.

## Latest coordinator recovery action

Root revalidated the same higher handle as RUNNING after retry. Two
bounded30-second waits yielded no update; neither is treated as terminal.
The detailed numerical review remains a24-line initial skeleton. Both
actual arithmetic programs completed earlier and their outputs are durable;
do not rerun them merely to wait for the review record.
Odd's final cofactor PASS was received/read; its sole index-source repair
uses Kim's same modified-Selmer indices. The author applied editorial
completion, final cofactor proof55393737... / checkpoint49a13d4c....
No next new mathematical task is dispatched. Next-research-plan.md is
updated around the actual remaining targets and distinguishes the pending
numerical verdict. Core six construction results are integrated; the
additional §6 numerical implication waits for its saved review.

## Final completed round24 handoff

The numerical review is NOW complete and read in full: c64bb530... PASS,
including the separate P-or-Q proof. Root added that already reviewed
refinement and completion links to the proof; its final hash is
79d4ec292b1b2094e7fc388c4c40efff825a34bd8da7243bc2eeab5b8ed9ade6.
No script or certificate changed. Higher also finished its source-motive
editorial links: final proofa6470b0f45c1d33fef2b8581f0d4af810410594abda4573134982548e322127f,
checkpoint0df1a07c68236667021942ecb6736c18e4f22ddc9ff2f980f8c71cdb5b97459b.
All three handles reported completion; revalidate tools before next use.
No process is live and no new mathematical assignment is dispatched.
The six constructions/seven review records, new local unit and nonlinear
comparison test are integrated in ledger24/report. Next-research-plan.md
has the concrete remaining tasks. Full BSD remains active and unresolved.

## Unreviewed next-step leads retained for the next round

The exact polarized local defect admits a prospective quadratic extraction:
D_r(P,Q)=U_pi([p^r](P+Q))-U_pi([p^r]P)-U_pi([p^r]Q).
The reviewed series bounds appear to prove actual integral divisibility
by p^(2r), followed by a limit whose logarithm is C2 logP logQ.
This needs a separate written proof/review before promotion. Its purely
local bilinear matrix would have rank at most1, so it cannot by itself
be substituted for the full rank-two global height determinant. Retain
finite-place corrections and do not infer a global source from local
normalization. The next plan also suggests a global division-coefficient
object that retains the local selector in growing order.

For the other remaining motivic component, a prospective degree rewrite
may help choose the right higher-symbol theorem: if A=M1(E) denotes the
homological elliptic h1 motive, curve duality gives h1_coho=A(-1)[-2].
Then the h1×h1 part of Hom(1,RΓ(E²)(3)[4]) rewrites as
Hom(1,A tensor A(1))=Hom(1,A tensor A tensor Gm[-1]).
The geometric MINUS projector must still be carried through the shifts.
This is NOT the ordinary degree-zero Somekawa group. Do not assume a
homotopy-module tensor is flat, that a negative derived tensor group
vanishes, or that regulator zero is faithful. Check this exact rewrite
and any theorem's degree before using it for the actual point×K2 classes.


### Final round24 continuity verification

The final snapshot verifies 246 artifact hashes, 956 local artifact links,
11 certificate JSONs and all 10 certificate/source dependency hashes.
The legacy certify_ran.json contains two valid JSONL records. All three
Astra/xhigh handles reported completion; no process or next mathematical
assignment is live. No old certificate suite was rerun. The goal remains
active, with full universal BSD unresolved and the next actual targets saved.
