# Coordinator log — Wave 2 launch

2026-09-11. Parent agent. Six Fable 5.1 thinking-max agents running on disjoint files.

## What is already a theorem (do not reopen)

For every \(E/\mathbb{Q}\):

- \(L(E,s)\) is entire (modularity).
- \(r_{\mathrm{alg}}\le\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\) at every \(p\).
- If \(r_{\mathrm{an}}\le 1\), then \(r_{\mathrm{alg}}=r_{\mathrm{an}}\) and \(\operatorname{Sha}(E/\mathbb{Q})\) is finite (Gross–Zagier–Kolyvagin + nonvanishing of twists + Kato; converses of Skinner, Zhang, BCGS).
- A positive-density set of curves, all of rank \(\le 1\), satisfy BSD (rank) (Bhargava–Skinner–Zhang). This set contains **no** rank-\(\ge 2\) curve.

For \(r_{\mathrm{an}}=2\), after Wave 1, the rank statement plus \(p\)-primary finiteness is **equivalent** to a single nonvanishing:

\[
\nu_\infty(E,K,p)=1
\qquad\text{i.e.}\qquad
\kappa_\ell^{\mathrm{Heeg}}\ne 0\text{ for some Kolyvagin prime }\ell.
\]

That is the shortest open sentence that finishes BSD (rank) and \(\operatorname{Sha}[p^\infty]<\infty\) for a given rank-2 curve at a given \(p\). Finiteness of the whole \(\operatorname{Sha}\) is the uniformity statement \(\mathrm{U}(E)\) (a rational constant tying \(p\)-adic leading terms), or equivalently the rationality of \(L''(E,1)/(2\,\Omega_E\operatorname{Reg})\).

## Minimal sufficient package (coordinator form)

The following three open statements, conjoined with theorems of 2014–2026, imply **full BSD over \(\mathbb{Q}\)**.

**P1 (Kolyvagin index).** For every \(E/\mathbb{Q}\) with \(r_{\mathrm{an}}=2\) and every auxiliary \(K\) with \(r_{\mathrm{an}}(E^K)=1\) satisfying (Heeg), there exists a prime \(p\) as in Zhang / BCGS with \(\nu_\infty(E,K,p)=1\).

**P2 (Kurihara / Mazur–Tate).** For every \(E/\mathbb{Q}\) and some good ordinary \(p\ge 5\) with \(\bar\rho_{E,p}\) surjective,
\(\tilde\delta_n=0\) for \(\nu(n)<r_{\mathrm{an}}\) and \(\tilde\delta_n\ne 0\) for some \(n\) with \(\nu(n)=r_{\mathrm{an}}\).

**P3 (uniformity).** For every \(E/\mathbb{Q}\) with \(r_{\mathrm{alg}}=r_{\mathrm{an}}\), the constant
\(c_E=L^{(r)}(E,1)/(r!\,\Omega_E\operatorname{Reg}_{\mathrm{NT}})\) is rational and nonzero, or equivalently \(\mathrm{U}(E)\) holds.

Remarks:

- P1 ⇒ BSD (rank) + \(\operatorname{Sha}[p^\infty]<\infty\) in rank 2, once two independent points are known (true for every tabulated curve) or once P2 supplies the Selmer lower bound without exhibiting points.
- P2 ⇒ \(\operatorname{corank}\operatorname{Sel}_{p^\infty}=r_{\mathrm{an}}\) in every rank (Kim). With P3 or Schneider + exhibited points, this is full BSD (rank) + \(p\)-part of the leading term.
- P2 for \(r_{\mathrm{an}}=2\) is equivalent to P1 via Kim’s higher Gross–Zagier (\(\operatorname{ord}(\kappa^{\mathrm{Heeg}})+1=\max\{\operatorname{ord}\tilde\delta(E),\operatorname{ord}\tilde\delta(E^K)\}\) and \(\operatorname{ord}\tilde\delta(E^K)=1\)).
- P3 is the leading-term conjecture once the rank is known. It is the only known route to \(\operatorname{Sha}\) finite at **all** \(p\) in rank \(\ge 2\).

So the program has two independent doors into rank 2 (Heegner \(\kappa_\ell\), or Kurihara \(\tilde\delta_{n}\)), and one door into the leading term (a \(p\)-independent rational period). Wave 2 hits all three.

## Numerical anchor (already in `compute/`)

On 389a1, the smallest rank-2 curve:

- \(r_{\mathrm{alg}}=r_{\mathrm{an}}=2\), certified.
- Analytic \(\#\operatorname{Sha}=1\) to \(>20\) digits: \(L''(E,1)/2 = \Omega_E\operatorname{Reg}\).
- \(r_p=2\) and \(L_p^{(2)}/(\varepsilon_p\operatorname{Reg}_\gamma)\equiv 1\) at every good ordinary \(p\le 97\) computed (PARI and Sage agree). Stein–Wuthrich 2013 extend this to thousands of \(p\).

This is the curve on which P1 and P3 must be proved first.

## Agents — all six failed on launch

Other Models quota exhausted. None wrote a file.

1. [Kolyvagin index](5ccc8ad9-5d8a-4295-8fec-51cb6d066eda)
2. [Mazur–Tate horizontal](6650a6ac-b6c4-42e1-955a-35dd06d397c7)
3. [Uniformity and Sha](5a9fd712-660c-4a7b-af9d-3385c5ec8851)
4. [Literature 2025–26](eda1d101-d68c-4612-8168-9ac79256c4f8)
5. [Sha + architecture](9a26e937-789a-49d8-881d-df361ce59f1e)
6. [Canonical object](a00056ff-98aa-4340-a911-2195a8ea6fdb)

Coordinator finished `proof-architecture.md`, `H-sha-and-descent.md`, and `final-report.md`. No further agents.
