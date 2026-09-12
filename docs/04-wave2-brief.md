# Wave 2 brief — close the gaps

Date: 2026-09-11. Coordinator: parent agent. Model for all Wave-2 agents: Claude Fable 5.1 thinking-max.

Wave 1 produced a complete map. The remaining work is **not** another survey. Each agent owns one gap and must either prove it or replace it by a strictly smaller, self-contained lemma with a full proof of the reduction.

Charter (`00-charter.md`) is in force: no fabrication, verify citations, tag every claim, push to the first unproved statement, prove what you can.

Do **not** write that the problem is impossible. Do **not** stop at “this is the known obstruction.” Assume the statement is true and find the argument.

## What Wave 1 already settled (do not redo)

Read, then cite; do not recopy:

- `01-statement-and-reductions.md`, `02-state-of-the-art.md`, `03-obstructions-rank-ge-2.md`
- Approaches A–G. Approach H is missing and is assigned below.
- Compute lab: `compute/README.md`, `compute/data/padic_ranks_report.md`. For 389a1, \(r_p=2\) and \(L_p^{(2)}/R_p \equiv 1\) at every good ordinary \(p\le 97\) that was computed.

Settled equivalences (use them):

- Rank \(\le 1\): BSD (rank) and finiteness of \(\mathrm{Sha}\) are theorems (Gross–Zagier–Kolyvagin, Kato, Skinner converse, …).
- For \(r_{\mathrm{an}}=2\), \(K\) with \(r_{\mathrm{an}}(E^K)=1\), and \(p\) as in Prop. 2.2 of `03`:  
  \(\operatorname{corank}\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})=2 \iff \nu_\infty=1 \iff \exists\,\ell:\ \kappa_\ell^{\mathrm{Heeg}}\ne 0\).
- Kim: \(\operatorname{corank}\mathrm{Sel}_{p^\infty}=\operatorname{ord}(\tilde{\boldsymbol\delta})\) (Kurihara numbers).
- Kato bottom class vanishes for \(r_{\mathrm{an}}\ge 2\) (Prop. 1.1 of `03`).
- No \(E/\mathbb{Q}\) of rank \(\ge 2\) has \(\mathrm{Sha}\) known finite at **all** \(p\).

## The seven gaps (from `03`, §6)

| Gap | Statement | Owner file |
|-----|-----------|------------|
| 1 | Schneider: \(\langle P,P\rangle_p\ne 0\) in rank 1 (avoidable for BSD via Heegner) | not Wave-2 priority |
| 2 / 5 | Selmer lower bound in odd rank \(\ge 3\); Kurihara \(\tilde\delta_\ell=0\) | `approaches/I-mazur-tate-horizontal.md` |
| 3 | \(r_p\le r_{\mathrm{an}}\) in rank \(\ge 2\) | equivalent to BSD + Sha + Schneider; do not attack directly |
| 4 | Higher Gross–Zagier over \(\mathbb{Q}\) | `approaches/C-wave2-canonical-object.md` |
| 6 | \(\nu_\infty=1\) for \(r_{\mathrm{an}}=2\) | `approaches/B-wave2-kolyvagin-index.md` |
| 7 | Uniformity \(\mathrm{U}(E)\) for one rank-2 curve | `approaches/A-wave2-uniformity.md` |

## File ownership (do not edit another agent’s file)

1. `docs/approaches/B-wave2-kolyvagin-index.md`
2. `docs/approaches/I-mazur-tate-horizontal.md`
3. `docs/approaches/A-wave2-uniformity.md`
4. `docs/04-literature-2025-2026.md`
5. `docs/approaches/H-sha-and-descent.md`
6. `docs/approaches/C-wave2-canonical-object.md`
7. `docs/synthesis/proof-architecture.md` — coordinator + architecture agent
8. `docs/synthesis/review-new-claims.md` — reviewer, after the others land

## Writing standard

Markdown + LaTeX. Every substance claim tagged. Every `[NEW]` has a complete proof. Every `[GAP]` is a self-contained problem. Search arXiv (`export.arxiv.org/api/query` and `https://arxiv.org/abs/...`) before asserting a result is unknown.
