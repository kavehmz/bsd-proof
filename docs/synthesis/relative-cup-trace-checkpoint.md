# Relative compact cup and trace checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Own [relative-cup-trace-attack.md](relative-cup-trace-attack.md)
and this checkpoint only. The initial checkpoint was saved before research.
The completed radial/beta2 proofs and shared synthesis were not edited.
Universal full BSD remains active and unresolved.

## Completed construction and review

All six sections passed the coordinator's independent
[review-relative-cup-trace.md](review-relative-cup-trace.md),
SHA25645b07441f668cbdc8b3eedc296612b139b4f28ee4f9e1dbab08f22fb5c5e2794.
Reviewed mathematical proof:
754373e0d23a81096abca7d1617ab142d6901f1988672a1e1643e1240306c059.
The full review was inspected. Later proof-header/checkpoint changes
are editorial; no mathematical correction was needed.

## Actual rational morphism

Y=X0(389) minus the two cusps; V°=Y times E.
The exact unit is u(z)=N^-6 Delta(z)/Delta(Nz),
divu=(N-1)(0-infinity), N=389.
The map uses RIGHT cup c cup{u}; cohomological degrees3 and1
make this minus the opposite left order.

With f:V°→E and q:E→SpecQ proper, the trace is the actual counit
f_!f^!1_E(2)[2]→1_E(2)[2], using f^!1_E=1(1)[2].
Equivalently factor through j_!1→1 on X times E AFTER the cup,
then the proper projection trace. No ordinary push from the open.

Thus T_u:H_M,c³(V°,Q2)→H_M²(E,Q2) is an actual rational map,
with degree/twist(3,2)+(1,1)-(2,1)=(2,2).
The compact trace is normalized by degree1 on a rational point.

## Full boundary composite

Let e0=partial^+(1,0) in H_M,c¹(Y,Q0), where
D(c,b)=(dc,i*c-db) and partial^+(b)=(0,+b)=-partial_can(b).
The entire boundary injection is j_B(beta)=e0 external beta.
Moving beta of degree2 past the unit of degree1 has no sign.
Projection formula reduces T_u j_B to lambda·id, with
lambda=Tr_Y(e0 cupu) in End(1_Q)=Q.

The ACTUAL Betti fiber representative for e0 is -d rho,
rho=1 near0 and0 nearinfinity. Kummer is du/u and curve
trace is(2pi i)^(-1)integration. The clockwise puncture boundary
gives lambda=N-1. Injectivity only of Q→C on the UNIT endomorphism
is used; there is no faithfulness assertion on general K2.

Therefore T_u j_B=(N-1)id on ALL H_M²(E,Q2).
R_u=T_u/(N-1) is a rational retraction and Pi_B=j_B R_u is idempotent.
The denominator388, including its primes2 and97, remains.
No primitive integral splitting is proved.

## Full native Deligne realization

A normalized relative real(1,1) representative S has native form
c=2pi i S. Its RIGHT Deligne product with l=log|u|, followed by
the curve trace, is the closed native imaginary one-form
Theta_u(S)=∫Y[S wedge(partial l-barpartial l)
                    -l(partial S-barpartial S)].
The second term is essential in the general formula.
It follows from the actual total/concise product and its real projection,
not from naive multiplication. Smooth representatives vanish near both
cusps, so extension by zero and proper push are legitimate.

Integration by parts gives
Theta_u(S)=2∫Y S wedge(partial l-barpartial l)
              -(partial_E-barpartial_E)∫Y lS.
For the translation-invariant radial representatives the last function
is constant, but the general operator does not omit it.

Its full scalar relation is
∫E omega_E wedge Theta_u(S)=8pi² i c_pi P(S).
For Theta=i eta in the arithmetic real part,
R_E^D(T_u^D[S])=8pi² c_pi P(S)/omega1.
A separate substitution of the boundary cutoff gives i(N-1)eta,
agreeing with the WHOLE motivic composite and the old beta2 scalar.

## Arithmetic real eigenspace and projected spectral class

The concise curve complex gives
H_D²(E(C),R2)=i H¹(E(C),R).
Combined coefficient/geometric conjugation fixes
i H¹(E,R)^minus, dimension1 because c(a)=a,c(b)=-b.
Its b-period is an isomorphism on this REAL space.

Hence the actual spectral image is determined as a FULL real class:
T_u^D(C_j2)=-12N(N-1)c_pi ell_E/omega1 · r_D(beta2),
R_u^D(C_j2)=-12N c_pi ell_E/omega1 · r_D(beta2).
The full Omega_E is2omega1. This does not prove that K2(E)_Q
has rank one or that C_j2 has a rational motivic lift.
Even a rational relative lift only gives some rational K2 class,
not automatically one in Q beta2.

The Gamma-completed input keeps gamma1 j1+gamma2 j0+gamma3 R_N.
Only AFTER projection, their previously zero scalar values and the
one-dimensional arithmetic real target imply zero projected classes.
Thus T_u^D(C_tildej2)=T_u^D(C_j2), with no deletion of terms
from the unpaired relative source.

## Primary inputs checked

- Déglise, Definition1.5/§1.6, cohomological compact supports and products.
- Voevodsky Proposition4.1.5, proper-pair/compact localization.
- Déglise–Fasel–Jin–Khan, JEP8(2021), TheoremA(I),(II),(V),
  canonical PLUS rational orientation, smooth purity and motivic comparison.
- Burgos–Goswami1712.10150v2 §§4.1/4.3–4.5 and Proposition5.5,
  native forms, product, trace normalization and proper regulator compatibility.
- All radial/beta2 period, finite-data and full-real-cycle conventions are
  the unchanged previously reviewed inputs.

## Assigned reciprocal review and remaining target

The independent review of root's six-section point-determinant proof
is complete:
[review-point-determinant-single-valued.md](review-point-determinant-single-valued.md),
PASS SHA25664439ef8ff11ad3c42a295217906b155a4b27fbb0bf8ca10b58e5391726cb9d5.
Reviewed root proof88ef905fb2dbcfbf8381166dfd78b80ea2a0d2f8d8593ab51b7a2d844be8f843,
checkpointc78daf70....
The level/exterior-object notation precision was inspected.
The review verifies direct delta=H/(2pi), full B* geometry,
geometric PLUS interchange and integral2, both scalar-height zeros,
no two-step framed collapse, and the actual rational K2 extension/tensor.

RCT-389 remains: construct the rational framed spectral source and
its arithmetic comparison with the actual point-height determinant,
including all finite corrections and integral denominators.
The coefficient above lacks Reg_E and is not known rational.
This is one attempted route, not a necessary condition for all BSD.

This bounded construction and its reciprocal review are complete.
Root handles shared integration. No old numerical/certificate rerun,
shared synthesis edit, completed-proof edit or additional agent occurred.
