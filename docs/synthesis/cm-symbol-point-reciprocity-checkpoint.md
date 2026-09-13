# CM symbol–point reciprocity: completed checkpoint

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only cm-symbol-point-reciprocity-attack.md and this checkpoint.
Status: all nine sections completed with a
[full independent PASS review](review-cm-symbol-point-reciprocity.md),
also inspected by the coordinator. Only completion links/status have
changed since the reviewed mathematical revision.
Full BSD over Q remains the objective. No additional agents, old
certificate reruns, shared synthesis edits or completed-proof edits.

## Assignment and preserved scope

Read next-research-plan §3 and the completed uniform-carry proof/review.
Construct a concrete arithmetic reciprocity/norm map on the ACTUAL
modular-symbol/elliptic-unit and rational-point/sigma families, retaining
the smoothing, determinant u(0), local iota, generator and full basis.
Seek a uniform nonvanishing/index or common rational-frame theorem.
If a natural map fails, prove its exact failure on these objects and
continue with a justified alternative. No abstract-series model or
prime scan may substitute for the arithmetic construction.

The current plan and completed uniform-carry proof/review have been read.
The new bounded deductions passed independent review. The construction
is an ACTUAL translated theta system on the Kummer division torsors of
P,Q, rather than postulated height series or fixed-multiplier evaluation.

## Completed arithmetic construction

Let tau_m=Omega_infinity/(f_0 p^m), choose compatible p^m-division
points P_m,Q_m, and put F_m=K(f p^m), M_m=F_m(P_m,Q_m).
Use the original rational Theta_a (twelfth power included), and the
three values Theta_a(tau_m+P_m), Theta_a(tau_m+Q_m),
Theta_a(tau_m+P_m+Q_m). The exact theta isogeny distribution gives
the norm computations on the finite étale fibers. Its exact primary
Kato/Schmitt normalization has been checked.

There is a concrete elementary route to the actual Kummer Galois group:
CM reciprocity and CRT give the full split Cartan on E[p^m]. Its
central homothety minus1 kills H¹ of the ray group on E[p^m] (Sah).
The full O_K⊗Z_p point basis P,Q and Kummer injectivity then show
that Gal(M_m/F_m)=E[p^m]^2: a missing residual component would
give a nonzero O_K/p-linear relation between P,Q modulo p; Nakayama
lifts this to every m. The full proof and its review include the
finite tame extension and exact coefficient action.

Using that proved group and the primary theta distribution, the ACTUAL
field norm to F_m of each translated theta value is
Theta_a(tau_0+R)^(p^(2m)), R=P,Q,P+Q. The unused Kummer direction
gives this multiplicity. Thus transferring first through the complete
two-point Kummer field kills its finite p^k Kummer class once2m>=k;
it cannot give the old nonzero derived class at5. This is a proved
failure on the actual objects, not a claim their raw classes vanish.

The tested alternative uses separate finite étale Kummer
fibers (or single-point Kummer fields), whose norm has no unused
direction multiplicity. Their exact norm is Theta_a(tau_0+R).
The further CM twist/tame projection of this fixed-base value is
also killed by a homothety fixing K(f); the complete transfer with
T_pi coefficients is therefore zero.

For a uniform source, outside a finite fixed set of places where
[a](tau_0+R) reduces toO, the theta values on these division fibers
are S-units, as proved from the actual divisor of Theta_a.
The exceptional set is finite because tau_0+R is non-torsion.
No numerical scan is needed or authorized for this statement.

The theta distribution, Kummer-image/norm proof, single-fiber test and
cubical comparison to the actual point-sigma units are completed,
with smoothing, u(0), iota, period and generator factors preserved.
Uniform/all-prime control and rational real comparison remain unproved.

## Completed source verification and relative refinement

Kato2004 Proposition1.3(1)(ii),(4) and proof1.10 have now been read
in /tmp/cm-derived-kato2004.txt, printedpp121–125. They give EXACT
Norm_[n](Theta_a)=Theta_a for(n,a)=1, including constant1; the source
function's twelfth power is the already reviewed rational Theta_a.
No new-prime Euler factor is inserted in this full finite-étale-fiber
norm. The primitive ray-orbit norm remains a different operation.
Schmitt's primary general-conductor source was also reopened.

The actual joint-field norm root is canonical when k<=2m:
Norm(u_R,m)=w_R^(p^(2m)), with w_R=Theta_a(tau_0+R), so choose
r_R,m,k=w_R^(p^(2m-k)). Choosing p^k-th roots of all conjugate units
whose product is this specified r defines a canonical class in
H¹(F_m,ker(Norm:Res_mu[p^k]→mu[p^k])). This retains the norm
nullhomotopy without choosing an arbitrary Galois primitive.

The actual first point-translation augmentation of this relative class
is proved zero: roots can be chosen constant in the unused Q
direction for R=P, with p^(2m) repetitions; their total product is
exactly r. The first weighted sum is then killed modulo p^k.
For R=P+Q roots depend only on the sum of the two translations and
the same cancellation holds. The full cochain proof and correct
Tate/CM-twist target passed review. The raw relative class is not
asserted zero.

A further positive alternative is an ACTUAL cubical norm on the full
torsion fiber [p^m]^-1(tau_0): the ratio of four translated Theta_a
values norms to
C_a(tau_0;P,Q)=Theta_a(tau_0+P+Q)Theta_a(tau_0)/
 (Theta_a(tau_0+P)Theta_a(tau_0+Q)). It is independent of division
choices, and its rational function in tau is nonconstant because
the four E[a]-cosets differ by the independent non-torsion P,Q.
Its exact regularized leading coefficient at tau=O is
(psi_a(P)psi_a(Q)/(a psi_a(P+Q)))^12. This was evaluated by
exact rational division-polynomial recurrences (a5 and7 only),
without a prime scan or an old certificate rerun. The sigma division
identity identifies it with an isogeny-smoothing defect of the
Poincare section, which canonical quadratic heights annihilate
AFTER their finite corrections; its raw logarithm is not asserted zero.
The desired unsmoothed point determinant/rational frame has not followed.

## Authoritative reviewed proof and next action

Complete proof: cm-symbol-point-reciprocity-attack.md.
Reviewed mathematical SHA256:
6f08e8f4e1d3142436fb3bbcf1f631d4023448b9070bb36f6e1ed0924b63e22f.

Established with independent PASS review:

- Full split Cartan over the fixed tame base, including minus1;
  full O_K⊗Z_p point lattice and Gal(M_m/F_m)=E[p^m]^2.
- Exact unused-direction norm w_R^(p^(2m)), distinct tower norm
  u_R,m^(p^4), and a uniform finite S-unit boundary for this source.
- Complete joint transfer zero at finite p^k; the single-point
  alternative also has zero CM-twisted complete transfer, by the
  homothety fixing F0. This does not set the raw units to zero.
- The actual norm-torus torsor(14), using the specified root
  w_R^(p^(2m−k)); its first point-translation augmentation is zero
  by an explicit cochain calculation. Its full relative class is
  not asserted zero and retains its toric/CM coefficient type.
- A genuine full-fiber cubical norm(17) and nonconstant rational
  function on E with actual P,Q; regularized Néron leading value
  L_a=(psi_a(P)psi_a(Q)/(a psi_a(P+Q)))^12.
- New exact Fraction evaluations at a5 and7 only, using the displayed
  division-polynomial recurrences. Both reduced signed ratios have
  numerator and denominator of absolute value greater than1, so
  log_p L_a≠0 for EVERY odd p. This is an auxiliary nonvanishing
  theorem, not a theorem for c2,p. No prime scan or old run occurred.
- The exact sigma/Poincare and denominator identities(21)–(24)
  identify the cube as an isogeny-smoothing defect. Its corrected
  canonical height component is zero, despite its raw nonzero log.

The first remaining comparison is CM-Symbol-Point in§9: an operation
on the ORIGINAL ray branch and retained relative point data giving
uniform actual coefficient/index control and one rational framed
element before separate completions. Its coefficient must map to
c2/(2e_p detB_p) and have real realization ell/(2Omega_E), with
rationality a conclusion. No value of epsilon_p, u(0), iota or any
basis factor has been assigned. Bad/nonsplit and universal BSD scope
remain open as well.

Next action: wait for the coordinator's next bounded assignment.
No new mathematical task is dispatched. Do not expand this completed
proof or edit shared synthesis. No process or numerical script is running.

The independent reviewer has reconstructed all nine sections and
independently reproduced the new rational psi values/fractions.
Its sole type precision is now saved in§5: restrict scalars from
F_(m+1) to F_m before the norm map on the relative torsors, whose
target is the p^4-power torsor, not the unmodified level-m torsor.
This sentence was inspected and the final verdict is PASS. Every norm,
coefficient and regulator formula is unchanged. The coordinator also
read the full proof/review and independently reproduced the new exact
psi values and both rational leading coefficients.
