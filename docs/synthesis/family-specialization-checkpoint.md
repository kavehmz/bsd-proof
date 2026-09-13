# Checkpoint: family specialization attack

Date: 2026-09-12. Research explicitly resumed after the continuity audit.
Agent configuration: GPT-6 Astra, extra-high (`xhigh`).

## Current status after first material source finding

The resume checks in `AGENTS.md` have been completed: continuity notes,
worktree status, and live-agent inventory read. The subagent's scoped
`get_goal` returned null; root was informed, and no goal was created or
closed. The coordinator owns the persistent BSD goal.

Disegni's 86-page author PDF has now been read at Theorems C and D,
§§1.2–1.4, §7.3, and Appendix B. These readings supersede the older
“search abstracts only” descriptions below for this source.

* Theorem D is an exact equality of normalized functionals with values in
  the cyclotomic conormal space: a universal height of two Heegner classes
  equals the **first normal derivative** of the family $p$-adic $L$-function
  times a specified product of toric local pairings. It is not an identity
  directly computing all higher normal derivatives.
* Appendix B corrects its scope to Hida-star families: at nonsplit
  $p$-adic places the quadratic extension must be inert and the Hecke
  character unramified; no $p$-adic place may ramify in that extension.
  Working over Q with $p$ split in the auxiliary imaginary quadratic
  field makes these additional conditions vacuous.
* Theorem C constructs/interpolates the universal Heegner class, but does
  not identify its leading term at rank jumps. Conjecture Pf, §7.3.2,
  separately predicts order at least floor(dim extended Selmer/2) and a
  Pfaffian-regulator leading term, initially only modulo the coefficient
  field's multiplicative group. Remark 7.3.3 explicitly discusses the
  additional integral normalization needed to improve this ambiguity.
* The exact family height identity has no explicit Sha-finiteness
  hypothesis. Identifying special Selmer groups with Mordell–Weil spaces
  would need it; BKS's corresponding standing hypothesis must be retained.

The full proof file `docs/synthesis/family-specialization-attack.md` now
exists. It contains the following `[NEW]` deductions, all with proofs and
pending independent review:

1. Lemma 1: exact identities of meromorphic sections of an invertible
   determinant line on a reduced irreducible affinoid extend from a dense
   set and give equal jets at any regular special point. Perfect-complex
   determinant base change does not require cohomological flatness.
2. Lemma 2: for a two-term complex over L[[U]], Smith exponents describe
   every rank jump and the exact sequence
   `0 -> H1(C)/U -> H1(C derived tensor L) -> H2(C)[U] -> 0`.
   New special directions from the torsion need not lift to family classes.
3. Lemma 3: first cyclotomic conormal differentiation has kernel (T²);
   with odd symmetry, its remaining kernel is T³ B[[T²]]. Knowing the
   exact family height at every weight therefore does not recover the
   pure cubic cyclotomic coefficient.
4. Proposition 4: a compatible perfect-complex model
   `D_c=[[cT,U,0],[-U,T,0],[0,0,T]]`, with determinant `U²T+cT³`,
   has identical generic rank-one height, identical universal class Ue3,
   and identical exact tangent Pfaffian leading formula for every c.
   Its pure cubic coefficient is c, detected only by the extra special
   normal-height directions. It satisfies `D_c^t=-D_c(U,-T)`.
   This is a formal model, not an elliptic-curve example or BSD disproof.

The paper's corrected Theorem D and these proofs establish exactly which
continuation operations are valid. §6 fixes the BKS period Ω_ξ (rather
than silently replacing it by a full real period), the imprimitive complex
Taylor coefficient, the full MW regulator, and the explicit Sha-finiteness
hypothesis. The remaining identity FS is that the fixed-motive
archimedean period-regulator map of a compatible specialized arithmetic
determinant section gives the BSD element. Under nonzero Bockstein
regulator and the assumed Kato specialization this is equivalent to the
generalized Perrin–Riou comparison, not a weaker consequence of density.

The primary determinant-family source check is now completed. Fouquet,
JEP4(2017), DOI10.5802/jep.38, Theorem1.1/Corollary1.2 establishes
p-adic fundamental-line/base specialization under its hypotheses.
Its §2.1.1 strict-criticality definition and §2.2.2 period construction
were read. New Proposition5 of the attack proves the higher-rank BKS
elliptic point fails strict criticality: its global dual exponential is
zero and H2 has dimension r−1>0. Thus the explicit strict-critical
period formula cannot be applied there. The related1604.06411 preprint
was read at §2.3.2: its displayed interpolation equations concern
critical values; they do not establish the fixed-motive higher
derivative/NT-regulator comparison. This is not a challenge to those
arithmetic specialization results.

Current result: the bounded research task has reached its precise
missing identity FS in §6, and §7 records both attempts to derive it
(dense determinant sections and motivic line specialization) and the
exact points where they stop. No actual arithmetic proof of FS, no new
Sha finiteness result, and no proof/disproof of BSD have been obtained.

Independent review is now PASS in `review-family-specialization.md`.
Two precision fixes were made before that PASS: Lemma1 now uses
one global denominator and a global projective-module embedding on
the affinoid; §6 explicitly assumes the exact Bockstein descent
identity (8b), retaining Hyp2.2 and integralIMC7.1 if invoking BKS
(7.3.2). The auxiliary rank-one twist is now conditional on its
being chosen with the stated local conditions. The substantive
rank-jump model and normal-jet calculations were independently checked.

Next action: a further research round would need a construction of the
fixed-motive period-regulator compatibility, not another use of
density or of arithmetic line base change alone.

The historical pause record follows; the final pause sentence there is
superseded by this explicit resumption status.

## Assigned task

Investigate whether exact Gross–Zagier or $p$-adic Gross–Zagier identities
on dense classical points of a Hida/Coleman family can prove the
generalized Perrin–Riou/Burns–Kurihara–Sano comparison at a weight-two
elliptic curve of rank at least two. The eventual owned research artifact
is `docs/synthesis/family-specialization-attack.md`; it has **not yet been
created**. This checkpoint is the only file created for the new task.

The task requires a precise candidate with variables, a determinant line,
period normalizations, rank-jump behavior, and all finiteness assumptions;
then a proof attempt pushed to its first precisely stated missing identity.
Do not repeat the earlier bounded-series valuation counterexamples, and do
not convert equality of ideals into an exact complex leading-term formula.

## Material already read

Read the relevant supplied text from:

* `docs/synthesis/derived-comparison-attack.md`, especially the determinant
  and cofactor descent lemmas, the exact-interpolation-versus-valuation
  distinction, and the failure of an automatic archimedean limiting step.
* `docs/approaches/G-motivic-bloch-kato.md`, especially §§2.3–2.4 on the
  generalized Perrin–Riou comparison and the distinction between an
  arithmetic determinant element and the complex BSD element.

The source-version corrections in `derived-comparison-attack.md` take
precedence over conflicting legacy BKS theorem/conjecture numbers in G.
In particular, its audit records that BKS Hypothesis 2.2 includes
$\Sha[p^\infty]$ finiteness. No such hypothesis is to be silently removed.

One web search was performed. The following were **located through search
results/abstracts only**; their full theorem statements and hypotheses have
**not** yet been read in this task:

1. Daniel Disegni, *The universal $p$-adic Gross–Zagier formula*,
   [arXiv:2001.00045](https://arxiv.org/abs/2001.00045),
   [author PDF](https://disegni-daniel.perso.math.cnrs.fr/univ.pdf).
   The abstract describes a universal Heegner class on a Hida family,
   an exact family $p$-adic height formula for a cyclotomic derivative,
   and a proposed Bertolini–Darmon conjecture for the class's leading term
   at classical points. This is the most promising next primary source.
2. Bertolini–Darmon, *Hida families and rational points on elliptic curves*,
   Invent. Math. **168** (2007), 371–431, DOI
   [10.1007/s00222-007-0035-4](https://doi.org/10.1007/s00222-007-0035-4),
   [available PDF](https://virtualmath1.stanford.edu/~conrad/DarmonCM/2011Refs/BDHidaFamilies.pdf).
   The located abstract concerns a split multiplicative elliptic curve
   with another multiplicative prime and a second derivative along a
   central critical line. It must not be mistaken for a general
   analytic-rank-two complex formula.
3. Howard, *Variation of Heegner points in Hida families*,
   [arXiv:1202.6358](https://arxiv.org/abs/1202.6358), and
   *The Iwasawa-theoretic Gross–Zagier theorem*,
   [arXiv:1202.6349](https://arxiv.org/abs/1202.6349).
4. Castella, *$p$-adic heights of Heegner points and Beilinson–Flach
   elements*, [arXiv:1509.02761](https://arxiv.org/abs/1509.02761),
   published under a closely related title in J. Lond. Math. Soc. **96**
   (2017), 156–180, DOI
   [10.1112/jlms.12058](https://doi.org/10.1112/jlms.12058).

## Candidate under examination, not a verified theorem statement

Work near a weight-two point $x_E$ on an ordinary Hida branch, with local
weight parameter $U$ vanishing at $x_E$, and a separate cyclotomic
parameter $T$. A possible starting identity has the schematic form
$$
\partial_T\mathscr L_p(U,0)
=\mathscr E(U)\,h_{p,U}(\mathscr P(U),\mathscr P(U)),
$$
where $\mathscr P$ is a big Heegner class and $\mathscr E$ denotes the
explicit factors after fixing compatible period and automorphic
normalizations. The actual source may express this as an identity of
functionals rather than the displayed scalar equation. That distinction
must be checked before using it.

The contemplated strongest continuation step is: exact identities at
$p$-adically dense classical weights should identify sections in a common
determinant line, and hence identify their leading specializations at a
point where Selmer rank jumps. Even if that algebraic specialization
works, a separate question remains: does its distinguished leading
specialization equal the complex normalized leading coefficient for the
**fixed** motive of $E$, as required by BKS?

No precise arithmetic determinant complex, specialization map, period
trivialization, or general family identity has yet been constructed or
verified. No new lemma or arithmetic result has been proved in this task.

## Issues still to resolve

* Classical weights can accumulate $p$-adically while going to infinity
  as complex weights. A $p$-adic identity theorem is not a complex
  continuation argument in weight.
* The classical fibers have varying motives and varying cycle/height
  realizations. Their first central derivatives must not be identified
  with higher central derivatives of the fixed weight-two $L$-function.
* A Selmer cohomology sheaf may fail to be locally free at a rank jump;
  a determinant line can still admit base change, but its cohomological
  trivializations and orders of vanishing need to be tracked.
* Independently chosen complex or $p$-adic periods at each classical
  point do not automatically give a coherent normalized analytic section.
* Determine exactly where any family theorem assumes rank one,
  nondegenerate height, or finiteness of a primary Sha group.
* A Heegner argument passes through a quadratic extension. Its rank
  and auxiliary twist factor must be specified before comparing with the
  rational-curve BKS statement.

These are questions to investigate, not established no-go theorems.

## Next action after explicit resumption

Read Disegni's author PDF, identify the exact universal height theorem,
its hypotheses and normalization, and the proposed leading-Heegner-class
conjecture mentioned in the abstract. Then formulate the strongest valid
specialization lemma in a precise local ring and determinant line. Test
whether that lemma supplies the fixed-motive complex comparison or instead
stops at a specifically quantified additional identity. Only after this
should the full `family-specialization-attack.md` be written.

Research stops at this checkpoint until the coordinator explicitly resumes
the task. No additional source reading or proof work followed the pause.
