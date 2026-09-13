# Global Heegner tame nullhomotopy checkpoint

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own this file and heegner-tame-nullhomotopy-attack.md only.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-tame-nullhomotopy.md](review-heegner-tame-nullhomotopy.md).
Reviewed mathematical revision:
90b0925736532683e8ee1ab03b6b5fc155b3b2ddb9f9844c14a47a14e0e3b713.
All eight sections passed; no mathematical repair remains.
The reciprocal [secondary Kummer review](review-secondary-kummer-theta.md)
is also complete PASS.

The separate independent audit of CM integral local duality and
the Smith/Sha bound is also complete PASS in
[review-cm-derivative-integral-bound.md](review-cm-derivative-integral-bound.md).
It takes the reviewed presentation and the coordinator's c2
certificate as inputs; no numerical certificate was rerun.
No further mathematical task is assigned to this agent this round.
TN-TP5 and the universal BSD objective remain open.

## Historical initial checkpoint and progress snapshots

The entries below preserve the original assignment and intermediate
review handoff. Any references to pending review below are historical;
the completed verdict and current assignment are recorded above.
The initial checkpoint was saved before sources.

Universal objective: full BSD for every elliptic curve over Q.
Bounded task: solve, if possible, the actual first finite-coefficient
tame cup equations for the cofactor-corrected BF/Kato class, then
compute the mixed obstruction and its Heegner comparison. Keep all
local conditions, finite H2 terms, twist zeta/Euler/Tamagawa scalars,
full p^k and the ambiguity of nullhomotopies. No nonunit division.

Read next-research-plan.md section2 and the completed Heegner–Kato
proof/checkpoint. The extra p∤h_K hypothesis is retained only for
the independent two tame coordinates. The twist base Kato class
is p-relaxed; rank-zero twist does not mean finite Selmer is zero.

Next: form the actual finite Poitou–Tate obstruction pairing and
inspect primary annihilator inputs. Old local cup isomorphisms and
the nonzero full strict group are completed work, not new targets.

No shared synthesis edits, agents or old numerical reruns.
Every new deduction requires separate review.

## Full bounded proof saved, pending review

heegner-tame-nullhomotopy-attack.md §§1–8 is saved.
New results are not yet independently reviewed.

Actual first global equations:
- For t=v_p Tam(E^D), s=v_p#Sha(E^D)[p∞], multiplication
  by p^t makes a_i cup x locallyzero at every actual S.
  Old conditions are strict; goodp nonanomalous andD
  havezeroH²; badN uses normsurjectivity onE0 over
  unramifiedextensions. A full proof ofthat normfact isgiven.
- FinitePoitou–Tate pairs theglobalH²kernel with the
  S-strict twist H¹ subgroup of Sel_(p^k)(E^D).
  That subgroup hasorder≤p^s. Hencep^(t+s)killstheactualcups.
- In the EXTRA surjective/Manin range, CS2601.14504v1
  TheoremB plusits explicitrankzeroformula gives
  v_p d0=t+s. NonanomalousEuler andfull/cycleperiodfactor2
  areunits. Thusglobalnullcochains existforthe ACTUAL
  input z=d0 P_AB(w_k), with no nonunitdivision.
  Their construction isfinite cochainlinearalgebra after
  refinementtoa finitequotient; no canonicalchoice claimed.

Precise native-local distinction:
- At ramified oldi, regularpointShapiroimage inN_i isZERO:
  normpolynomial p^e+p^e(p^e−1)Y/2 maps to0inR[Y]/Y².
- Howeverker(H¹(M_D)→H¹(N_i)) is TRANSVERSE, fromthe
  boundaryH⁰(M)→H¹(M_D). It is NOT zero orfinite.
  This corrects a preliminary message beforeproof drafting.
- DefineJ_i,v exactlyaspreimageofnativepointimage.
  Under extra p∤TamE it isclassicalfiniteawayfromi,
  transverseati. Ordinarynonanomalousfiltrationchecks p;
  componentdefectsatbadprimesareotherwise retained viaJ.
- The actual compact obstruction c_i=(-a_i cupz,tau_i,v)
  modulo∂⁺J is dualtothe groupwithJ-perp localconditions.
  Its signedvalueis sum inv(tau_i,v cupb_v−u_v),
  du=(-a_i cupz)cupb. GlobalH²zero doesNOT killthisclass.
- If additionallySha_D[p∞]=0, theactualtransversetwist
  Selmergroupati isR. FinitePTgivesthe relaxedgroupR,
  andlocalisotropyforcesitsgraphtobethetransverseline.
  Thisdoesnotassert thecompactobstructionisnonzero.

Mixedequationandactualcomparison:
Omega=-a_l cup t_q−a_q cup t_l−a_lq cupz isclosed.
Changingfirstsolutionsbyh_i changesitsclassby
−a_l cuph_q−a_q cuph_l. Nativechoicesrequireloc h_i∈J_i,v.
Actualz_D0 adjustmentsproduce thoseexplicitcupterms,
butretain both p-relaxed defect andoldi finitevalue constraint.
Ifamixedlift exists, addingthe ACTUAL Heegner Shapiroclass
changesitstopcoefficientbyκ_rawwithoutchanginglowerones.
Nativepointimagesarepreservedbythataddition.
No complexrank-five coefficientidentity isproved.

Primary sources read:
CS2601.14504v1 sections1.1.1–1.1.4; MilneADT2 I.4.10
andI.5.1 finitekernelsequence; Demarche–Harari1804.03941v3
Theorem1.1/Proposition2.1. Predecessorraw/standard, Q/K2,
BFnormalization andKatojets remain fixed.

Next: independentreview ofallnewdeductions, especially
the d0 globalannihilator, nativezero/transverse distinction,
andthecompactobstruction'sduallocalconditions.
Root assigned a reciprocalreview ofhigher's
secondary-kummer-theta-attack.md inreview-secondary-kummer-theta.md
onceits full draftisstable. No oldscript orsharedfileedited.

Final review precisions requested and applied:
the R-splitting in the unramified coefficient quotient is
inertia-equivariant because inertia acts trivially on the
auxiliary factors (it may still act on M); formula(18)
explicitly uses e(compact coefficient, ordinary coefficient).
No formula or sign changed. Await the reviewer's final verdict.
The reciprocal secondary-Kummer review is complete PASS in
review-secondary-kummer-theta.md, with exact Rost/KLM
orientation and the canonical/admissible current restriction
repair recorded there.
