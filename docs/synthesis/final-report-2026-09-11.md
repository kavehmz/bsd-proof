# Final report — BSD research program

Date: 2026-09-11. Historical snapshot; superseded by [the current report](final-report.md)
and [the 2026-09-12 audit](continuation-2026-09-12.md). Some implications below were withdrawn.

---

## 1. What was asked, and what was delivered

The brief was to prove the Birch and Swinnerton-Dyer conjecture for elliptic curves over \(\mathbb{Q}\). The program did **not** produce a proof of BSD in rank \(\ge 2\). It produced a complete reduction of BSD to three open statements (P1, P2, P3), with every implication written and cited, plus a computational laboratory that checks the predictions on the smallest rank-2 and rank-3 curves.

Charter: `../00-charter.md`. Architecture: `proof-architecture.md`. Obstructions: `../03-obstructions-rank-ge-2.md`.

Wave 2 launched six Fable 5.1 agents on P1–P3, Sha, literature, and a higher Gross–Zagier object. All six died immediately on the Other Models quota and wrote no files. The architecture, Sha file, and this report were finished by the coordinator.

---

## 2. Theorems the program uses, not claims

For every \(E/\mathbb{Q}\):

- \(L(E,s)\) is entire (Wiles, Taylor–Wiles, Breuil–Conrad–Diamond).
- If \(r_{\mathrm{an}}\le 1\), then \(r_{\mathrm{alg}}=r_{\mathrm{an}}\) and \(\operatorname{Sha}\) is finite (Gross–Zagier, Kolyvagin, Kato, Bump–Friedberg–Hoffstein, Murty–Murty).
- Converses in rank 1: Skinner; Zhang; Burungale–Castella–Grossi–Skinner.
- \(\ge 66.48\%\) of curves by height satisfy BSD(rank), all of rank \(\le 1\) (Bhargava–Skinner–Zhang).
- In arbitrary rank, Selmer groups are *described* by Kolyvagin systems (Zhang, Sweeting, BCGS) and by Kurihara numbers (Kurihara, Kim). The description is not yet linked to \(r_{\mathrm{an}}\) when \(r_{\mathrm{an}}\ge 2\).
- No elliptic curve over \(\mathbb{Q}\) of rank \(\ge 2\) has \(\operatorname{Sha}\) known to be finite (Stein–Wuthrich 2013; still current).

---

## 3. The residual conjecture, in three sentences

**P1.** For \(r_{\mathrm{an}}=2\), one first derived Heegner class is nonzero.

**P2.** The Mazur–Tate / Kurihara elements vanish to order exactly \(r_{\mathrm{an}}\) (horizontal vanishing from vertical vanishing of \(L(E,s)\)).

**P3.** The number \(L^{(r)}(E,1)/(r!\,\Omega_E\operatorname{Reg})\) is a nonzero rational (equivalently, the \(p\)-adic leading terms are a single rational times local factors).

P1 \(\iff\) P2 in rank 2 (Kim). Either one plus exhibited points (or \(\mathrm{Fin}(p)\)) is BSD(rank) in rank 2. P2 is the uniform statement in every rank. P3 is BSD(lead) and is the only known route to \(\operatorname{Sha}\) finite at all \(p\).

Proofs of the equivalences: Props. 2.2, 2.3, 3.3, 5.1 of `../03-obstructions-rank-ge-2.md`.

---

## 4. Numerics (evidence, not proof)

Reproducible from `compute/README.md`.

| Curve | \(r_{\mathrm{alg}}\) | \(r_{\mathrm{an}}\) | analytic \(\#\operatorname{Sha}\) | \(r_p\) at computed ordinary \(p\) |
|-------|----------------------|---------------------|-----------------------------------|-------------------------------------|
| 389a1 | 2, certified | 2 | \(1\) to \(>20\) digits | \(=2\) for all good ordinary \(p\le 97\) (PARI/Sage); [SW13] to \(p<48859\) with one expensive exception |
| 433a1 | 2 | 2 | \(1\) | \(=2\) on the computed range |
| 5077a1 | 3 | 3 | \(1\) | computed for small \(p\) |

On 389a1 the predicted rational in P3 is \(1\). The \(p\)-adic ratios \(L_p^{(2)}/(\varepsilon_p\operatorname{Reg}_\gamma)\) are \(1+O(p^k)\) at every computed \(p\). That is \(\mathrm{U}(389a1)\) to finite precision, not a proof.

---

## 5. `[NEW]` claims that need review

All live in `../03-obstructions-rank-ge-2.md` unless noted.

| Claim | Content | Risk |
|-------|---------|------|
| Prop. 1.1 | Kato class vanishes globally if \(r_{\mathrm{an}}\ge 2\) | Short deduction from [BDV22]; probably known to experts |
| Prop. 2.2 | Rank-2 Kolyvagin bridge, \(\nu_\infty\) odd, \(\nu_\infty=1\iff\mathrm{Sel}(p)=2\) | Bookkeeping on [Kol91]/[BCGS]; should survive review |
| Prop. 2.3 | Kurihara number \(\tilde\delta_\ell\) is the \((\zeta-1)\)-derivative of a twisted \(L\)-value | Elementary from Birch’s lemma; check the constant-term congruence |
| Cor. 2.4 | Horizontal congruence forced by even rank \(\ge 2\) | Depends on Prop. 2.3 + Kim/Kurihara |
| Prop. 3.3 | \(\mathrm{U}(E)\Rightarrow\operatorname{Sha}[p^\infty]=0\) for almost all \(p\) | Formal from IMC + Schneider–Perrin-Riou; watch normalisations |
| Prop. 5.1 | Layer 2 needs height semisimplicity | Standard Iwasawa; [PR92] citation flagged |
| Prop. H.1 | Finite Sha \(\iff\) almost-all-\(p\) vanishing | Trivial |

None of these is a proof of BSD. They are reductions.

---

## 6. Why Wave 2 did not close P1–P3

The three statements are the same three that have blocked the field since Kolyvagin (1990) and Mazur–Tate (1987):

- No formula relates \(\kappa_\ell^{\mathrm{Heeg}}\) or \(\tilde\delta_\ell\) to \(L''(E,1)\).
- No \(p\)-independent Euler-system class survives in rank \(\ge 2\).
- No number-field analogue of Yun–Zhang’s \(r\)-legged shtuka cycle is known.

A honest program stops at that sentence rather than inventing a comparison isomorphism.

---

## 7. What to do with the remaining day / quota

Do **not** relaunch Fable agents. The Other Models quota is gone.

If any quota remains on this model, the only high-leverage tasks are:

1. Adversarial check of Props. 2.2–2.3 and 3.3 against the primary sources (Kolyvagin 1991, Kim 2024, Stein–Wuthrich 2013).
2. One computation: for 389a1 and one Heegner \(K\), find a Kolyvagin prime \(\ell\) and evaluate whether \(\kappa_\ell\ne 0\) (Jetchev–Lauter–Stein algorithm). That is a proof of P1 for **one curve, one \(p\)** — BSD(rank)+\(\mathrm{Fin}(p)\) for 389a1 at that \(p\), which [SW13] already gives by another route.
3. Leave P3 (full Sha) and the uniform statements alone until a new comparison formula exists.

---

## 8. Verdict

BSD over \(\mathbb{Q}\) is a theorem in analytic rank \(\le 1\) and a pair of comparison problems in rank \(\ge 2\): a horizontal/vertical \(L\)-value comparison (P1/P2) and a period-rationality comparison (P3). This repository records those problems at the level of self-contained lemmas, with the 2024–2026 Euler-system and Iwasawa theorems filled in, and with numerics that match the lemmas on the smallest examples.

That is the state of the problem, not a solution of it.
