# Program Charter: The Birch and Swinnerton-Dyer Conjecture

## Objective

Produce a complete, rigorous proof of the Birch and Swinnerton-Dyer conjecture for elliptic
curves over $\mathbb{Q}$, or — at every point where the proof is not yet complete — isolate the
*exact* missing statement as a precisely formulated lemma, prove as much of it as possible, and
document what remains with full precision.

The program is organised as a team of research agents working in parallel on different attack
lines, followed by adversarial review and synthesis. The standard of writing is that of a research
monograph: every statement is either proved on the page, cited to a verifiable source, or tagged
as open.

## The conjecture

Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $L(E,s)=\sum a_n n^{-s}$ its Hasse–Weil
$L$-function (entire by modularity), $r=\operatorname{rank}_\mathbb{Z} E(\mathbb{Q})$.

**BSD (rank).** $\operatorname{ord}_{s=1} L(E,s) = r$.

**BSD (leading term).** $\operatorname{Sha}(E/\mathbb{Q})$ is finite and
$$
\lim_{s\to 1}\frac{L(E,s)}{(s-1)^r}
= \frac{\Omega_E\cdot \operatorname{Reg}(E/\mathbb{Q})\cdot \prod_{p\mid N} c_p\cdot |\operatorname{Sha}(E/\mathbb{Q})|}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}.
$$

Variants in scope: the $p$-part of the leading term for each prime $p$; BSD over number fields;
the parity conjecture; the $p$-adic BSD conjecture of Mazur–Tate–Teitelbaum; the function-field
analogue.

## Epistemic tags (mandatory)

Every mathematical assertion of substance in this repository carries one of these tags:

- `[THEOREM]` — proved in the literature; cite precisely (author, year, arXiv ID or DOI/journal).
- `[CONDITIONAL]` — proved in the literature under stated hypotheses; list the hypotheses.
- `[CONJECTURE]` — a standard named conjecture; name it and cite where it is formulated.
- `[HEURISTIC]` — probabilistic or analogical reasoning; not evidence of truth.
- `[NEW]` — a claim first made in this repository, with a full proof on the page. Must be
  reviewed by an adversarial reviewer before it can be relied on elsewhere.
- `[GAP]` — a precisely stated assertion that is needed and not known. Every `[GAP]` must be
  stated as a self-contained mathematical statement (hypotheses, conclusion) so that it could be
  handed to a mathematician as a problem.

## Rules of engagement

1. **No fabrication.** Never invent a theorem, a reference, or a numerical result. If you are not
   certain a result exists, search for it (arXiv, MathSciNet-indexed journals, LMFDB). If you
   cannot verify it, write `[unverified]` next to it.
2. **Verify citations.** Each reference must carry an arXiv identifier, a DOI, or a full journal
   citation you have confirmed by fetching the source. Prefer the arXiv abstract page.
3. **Exact hypotheses.** When stating a known theorem, state its hypotheses exactly (e.g. "$p\ge 5$
   good ordinary, $\bar\rho_{E,p}$ irreducible, ..."). Loose statements are worse than none.
4. **Push to the gap.** For each approach, the deliverable is not a survey; it is a proof attempt
   pushed until the *first* statement that cannot be proved, which is then written down as a
   `[GAP]` with complete precision, followed by a serious attempt on that gap.
5. **Prove what you can.** If, in the course of the attack, a genuinely new lemma can be proved
   (even a small one, e.g. a new equivalence or a new conditional implication), write the full
   proof and tag it `[NEW]`.
6. **Numerics are evidence, not proof.** Computations live in `compute/` and are reproducible from
   scripts. Report them with the exact command that generated them.
7. **Write for a reader.** Markdown with LaTeX (`$...$`, `$$...$$`). Define notation once, in the
   document where it is introduced, and reuse it.
8. **Keep to your file(s).** Each agent owns the files named in its brief. Cross-reference other
   documents by relative path rather than duplicating them.

## Repository layout

```
docs/
  00-charter.md                       this file
  01-statement-and-reductions.md      precise statements, equivalences, reductions
  02-state-of-the-art.md              what is proved, with exact hypotheses, through 2026
  03-obstructions-rank-ge-2.md        why analytic rank >= 2 is out of reach, exactly
  approaches/
    A-iwasawa-padic.md                Iwasawa theory, p-adic L-functions, p-adic BSD
    B-euler-systems-heegner-kolyvagin.md
    C-higher-rank-euler-systems-diagonal-cycles.md
    D-function-field-analogy.md       Tate/Milne/Kato–Trihan, Ulmer, Yun–Zhang
    E-arithmetic-statistics.md        Bhargava–Shankar, Smith, converse theorems
    F-analytic-side.md                nonvanishing, rank bounds, random matrix theory
    G-motivic-bloch-kato.md           Bloch–Kato / Tamagawa number conjecture framing
    H-sha-and-descent.md              finiteness of Sha, Cassels–Tate, descent
  synthesis/
    proof-architecture.md             dependency graph: statements whose conjunction is BSD
    review-*.md                       adversarial reviews of [NEW] claims
    final-report.md                   what was achieved, what remains
compute/
  README.md                           how to reproduce
  scripts/                            Sage / PARI / Python scripts
  data/                               outputs
  RESULTS.md                          numerical results with exact commands
```

## Notation (global)

- $E/\mathbb{Q}$ elliptic curve, conductor $N$, minimal discriminant $\Delta$.
- $a_p = p+1-\#E(\mathbb{F}_p)$; $L(E,s)=\prod_{p\nmid N}(1-a_pp^{-s}+p^{1-2s})^{-1}\prod_{p\mid N}(1-a_pp^{-s})^{-1}$.
- $r_{\mathrm{alg}} = \operatorname{rank} E(\mathbb{Q})$; $r_{\mathrm{an}} = \operatorname{ord}_{s=1}L(E,s)$.
- $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$, $\operatorname{Sha}(E/\mathbb{Q})$ with the usual meanings; $\operatorname{Sha}[p^\infty]$ its $p$-primary part.
- $T_pE$, $V_pE = T_pE\otimes\mathbb{Q}_p$, $\bar\rho_{E,p}: G_\mathbb{Q}\to \mathrm{GL}_2(\mathbb{F}_p)$.
- $\mathbb{Q}_\infty$ the cyclotomic $\mathbb{Z}_p$-extension, $\Lambda=\mathbb{Z}_p[[\Gamma]]$, $L_p(E,T)\in\Lambda\otimes\mathbb{Q}_p$ the Mazur–Swinnerton-Dyer $p$-adic $L$-function (good ordinary $p$).
- $r_p := \operatorname{ord}_{T=0} L_p(E,T)$, the $p$-adic analytic rank.
