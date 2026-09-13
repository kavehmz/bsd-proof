# Hecke–Brauer annihilator restart checkpoint

Date: 2026-09-12. Agent `/root/uniform_witness`, GPT-6 Astra/xhigh.
Current status: completed, [coordinator review PASS](review-hecke-brauer.md).
Initial targets and the draft-progress section below are historical;
resume from the completed handoff and HB-cycle. Revalidate live handles.
Own ONLY `hecke-brauer-annihilator-attack.md` and this checkpoint in
`docs/synthesis/`.

Parent objective remains full BSD over Q for all elliptic curves. This task
seeks an actual construction of a Hecke annihilator on arithmetic Brauer/Sha
classes, not another restatement of Sha finiteness. No such construction has
yet been obtained in this new task.

Read on resume: AGENTS.md, research-state.md, research-ledger.md,
final-report.md, modular-visibility-attack.md, and this checkpoint. Tools
confirm root plus three research agents live. The subagent goal tool is null;
the coordinator owns the active full-BSD goal. The worktree is uncommitted
research and must be preserved.

Previous result review is complete: coordinator passed the visibility note's
Props2.2/3.1, all-local-condition prime-to-degree splitting, the visible Sha
zero result for389, and Hecke-annihilator equivalence. Coordinator independently
verified AS2002 §4.2/Prop4.2, Cremona–Mazur printedp15, and ARS Thm2.2.
The separate `review-modular-visibility.md` preserves that source/computation
scope. Latest ownership restricts this task to the two new files above.

Historical starting mathematical targets (completed in the proof):

1. For smooth proper X=X0(N)/Q with rational cusp c, compute exactly
   Br(X)/Br(Q), its normalization at c, and local-triviality kernel, using
   Hochschild–Serre and Pic(Xbar)=J(Xbar) direct-sum Z via c.
2. Transfer the Hecke action correctly (pull/push correspondences versus
   the induced action on J), preserving the Br(Q) term and cusp correction.
3. Test whether proper regular models outside N, purity, or norm/restriction
   makes a fixed integer annihilator available. Do not assume finite Br of
   an arithmetic surface or confuse geometric Br(Xbar)=0 with arithmetic Br(X).
4. For389 identify Theta=40e_E=i*pi on the normalized locally trivial Brauer
   component and test a relation from the modular parametrization or cuspidal
   divisors. Save the exact first unproved arithmetic comparison.

No computations have been rerun and no subagents have been spawned.

## Historical draft-progress snapshot — superseded by completed review

1. For smooth proper geometrically connected curve X/Q with rational c,
   the section splits Br(Q)->Br(X), and Pic(Xbar)=J(Qbar) direct-sum Z[c].
   Tsen plus Hochschild–Serre gives Br_c(X)=ker(c*) ≅ H1(Q,J), compatibly
   at every completion. Thus Br_loc(X)=ker(Br(X)->product_v Br(X_Qv))
   is canonically Sha(J); the constants have zero local kernel by BHN.
2. Finite coefficient calculation: H2(Xbar,mu_n)=Z/n and
   H1(Xbar,mu_n)=J[n]. A rational cusp supplies both base-field retraction
   and a degree-one cycle class. The simultaneous kernel of geometric
   restriction and c* in H2(X,mu_n) identifies with H1(Q,J[n]); quotient
   by Pic^0(X)/n=J(Q)/n yields Br_c(X)[n]. With local Kummer conditions,
   the omitted cokernel is exactly Sha(J)[n]. Need finish the full proof,
   especially explain the d2 differential vanishes because the section
   injects the base H3 term (so no hidden odd-n assumption).
3. For f:X->E taking c to O, Br pullback/norm induce Pic pullback/norm,
   hence i and pi on H1(J). Normalize f_* at O before working on Br_c.
   f_*^0 f*=d; f*f_*^0 is the normalized Theta=i*pi. On locally trivial
   classes normalization correction already vanishes by BHN. This is a
   multiplication relation, not an annihilation.
4. Any strict-local Brauer class evaluates to0 at every closed point:
   for its residue number field L, all evaluations at L_w vanish, then
   Brauer–Hasse–Noether gives zero in Br(L). Thus rational-cusp or even
   arbitrary zero-cycle evaluations miss this subgroup entirely.
5. IMPORTANT VERIFIED MODEL INPUT: González-Avilés, J. Math. Sci. Univ.
   Tokyo10(2003)391–419, Lemma2.2(b), gives unconditionally
   0->Br(𝒳)->Br(X)->direct_sum_{v in U} Br(X_Qv), for regular connected
   2-dimensional 𝒳 proper over U, smooth geometrically connected generic
   curve. Take U=SpecZ, then impose zero at real places to get
   Br(𝒳)' ≅ Br_loc(X) ≅ Sha(J) in the rational-cusp case.
   Do NOT invoke that paper's main order theorem: it assumes no nonzero
   infinitely divisible Sha. The elementary Lemma2.2(b) does not.

Sources actually fetched:

- González-Avilés published paper https://www.ms.u-tokyo.ac.jp/journal/pdf/jms100207.pdf
  §0 hypotheses; equations(5),(6), Lemma2.2 on pp401–402; citation to
  Milne1981 Lemma2.6. arXiv:math/0104214, published2003.
- McCallum, Brauer Points on Fermat Curves, author PDF
  https://math.arizona.edu/~wmc/Research/BrauerFermat.pdf §2 p4:
  Br(X)/Br0(X) ≅ H1(K,J) for number/local fields, local evaluation pairing.
- Česnavičius, Purity for the Brauer group, arXiv:1711.06456,
  authorPDF https://www.imo.universite-paris-saclay.fr/~kestutis.cesnavicius/brauer-purity.pdf
  Theorem1.1/6.1. Not needed for the model transfer because the verified
  González-Avilés lemma avoids a risky mixed-characteristic residue shortcut.
  An initial mistyped arXiv1711.08726 was unrelated and is NOT a source.

Next: prove Pic(𝒳) finite generation from closure of generic divisors and
vertical component relations; show the fppf Kummer quotient still contains
the full Sha. Test specialization/Eichler–Shimura and cuspidal correspondence
relations with the actual arithmetic kernel retained. Seek a cycle-lifting
or norm-annihilation construction; do not claim Br(𝒳) finite from properness.

## Completed and reviewed bounded attack

The proof file `hecke-brauer-annihilator-attack.md` is now written with all
source assumptions and proofs. Root requested that its separate arithmetic
surface/zeta/Picard calculations not be duplicated; accordingly this note
states the exact fppf Kummer sequence but leaves those calculations to root.

Additional proved deductions:

- Propositions1.1/2.1 and Cor2.2 rigorously identify the arithmetic middle
  term at every n, including even n. The section kills the possible HS d2
  by splitting the base H3 edge map; no false H3(F,mu_2^k)=0 assertion.
- Proposition3.1 gives normalized Brauer pullback/norm and the exact degree
  relation. Propositions4.1/5.1 show all closed-point evaluations vanish on
  strict-local Brauer, while t0=T2-T3+1 kills constants and geometric degree
  but acts as1 on the389 elliptic arithmetic component.
- Lemma6.1 explicitly tests the Frobenius homotopy attempt:
  g z(g^-1 sigma g)=z(sigma)+(sigma-1)z(g); coefficient multiplication
  g z(sigma) has cocycle defect(g sigma-sigma g)z(tau). The ES coefficient
  relation therefore cannot be replaced by inner-conjugation identities.
- Cor7.1 transfers all target classes to one fixed regular arithmetic
  surface, retaining the real-place kernel and all divisible parts.
- At root's request, Proposition8.1 proves Br(𝓔)=Br(𝓔)'=Sha(389a1):
  O and Q=(0,-1) cover both real components and evaluate classes toBr(Z)=0;
  local Tate duality and normimage E(R)^0 force the real restriction0.
  Full proof communicated to root; no finite-Sha hypothesis.
- Equation9.1 identifies imageTheta on Br(𝒳)' exactly with f*Br(𝓔),
  isomorphic to Br(𝓔), using existing Sha2/Sha5 vanishing and d40.

Exact residual construction HB-cycle (9.2): for every n and every arithmetic
finite-coefficient Selmer class z on X0(389), construct a global degree-zero
line bundle L_z such that Theta_c z=c1(L_z). A fixed nonzero scalar multiple
uniform in n would suffice for finiteness. Local line bundles already exist
by definition and do not constitute this construction. No such global lift
or annihilator is proved. The universal full-BSD goal remains unresolved.

Extra primary source: Ribet–Wake, PNAS119(2022)e2210032119,
DOI10.1073/pnas.2210032119, https://pmc.ncbi.nlm.nih.gov/articles/PMC9565053/,
§2.2 Picard Hecke conventions and §2.5 Lemma2.4. Its rational-torsion
specialization injection does not apply to Brauer/Sha classes.
