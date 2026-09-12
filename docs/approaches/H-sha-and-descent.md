# H. Finiteness of \(\operatorname{Sha}\) and descent

Owner: coordinator (Wave 2 Sha agent did not run). Charter: `../00-charter.md`.
Cross-references: `../03-obstructions-rank-ge-2.md` §3, `A-iwasawa-padic.md`, `B-euler-systems-heegner-kolyvagin.md`, `../synthesis/proof-architecture.md`.

---

## 0. Outcome of this line

`[THEOREM]` \(\operatorname{Sha}(E/\mathbb{Q})\) is finite whenever \(r_{\mathrm{an}}\le 1\) (Kato; Gross–Zagier–Kolyvagin).

`[GAP H.1]` There is no \(E/\mathbb{Q}\) with \(r_{\mathrm{an}}\ge 2\) for which \(\operatorname{Sha}(E/\mathbb{Q})\) is known to be finite. This is still the 2013 status statement of Stein–Wuthrich [SW13, p. 1758]; Wave 1 found no contrary claim through 2026-09-11 (`03` §3.1).

The \(p\)-primary groups \(\operatorname{Sha}[p^\infty]\) **are** finite for many \((E,p)\) of rank \(\ge 2\), by a finite \(p\)-adic computation (Prop. 3.1 of `03`). The obstruction is “all \(p\) at once”: a \(p\)-independent bound on \(\#\operatorname{Sha}\).

---

## 1. Structure that is unconditional

`[THEOREM]` (Cassels). \(\operatorname{Sha}(E/K)\) carries a pairing \(\operatorname{Sha}\times\operatorname{Sha}\to\mathbb{Q}/\mathbb{Z}\) which is alternating and nondegenerate modulo the maximal divisible subgroup. Consequently \(\#\operatorname{Sha}/{\operatorname{Sha}}_{\mathrm{div}}\) is a square (when finite).

`[THEOREM]` (Cassels). The BSD leading-term formula is invariant under isogeny over \(K\): if it holds for \(E\) it holds for every \(E'\) isogenous to \(E\) over \(K\).

`[THEOREM]` (Tate). The Cassels–Tate pairing is compatible with the Poitou–Tate pairing on Selmer groups. Visibility (Mazur; Cremona–Mazur; Agashe–Stein) produces elements of \(\operatorname{Sha}(E)\) as images of rational points on isogenous abelian varieties; this **constructs** classes, it does not bound them.

`[THEOREM]` (Dokchitser–Dokchitser [DD10]). The \(p\)-parity conjecture holds over \(\mathbb{Q}\): \(\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\equiv r_{\mathrm{an}}\pmod 2\). This gives the even/odd dichotomy, not finiteness.

---

## 2. Why per-\(p\) finiteness does not give \(\operatorname{Sha}\) finite

`[NEW]` Proposition H.1 (bookkeeping). Let \(E/\mathbb{Q}\). The following are equivalent:

1. \(\operatorname{Sha}(E/\mathbb{Q})\) is finite.
2. \(\operatorname{Sha}[p^\infty]\) is finite for every \(p\), and \(\operatorname{Sha}[p]=0\) for all but finitely many \(p\).

*Proof.* \(\operatorname{Sha}=\bigoplus_p\operatorname{Sha}[p^\infty]\) (primary decomposition of a torsion abelian group). A direct sum of finite groups is finite iff all but finitely many summands are zero and the rest are finite. \(\square\)

In rank \(\le 1\) the second clause is supplied by a **single** \(p\)-independent integer (the Manin \(L(E,1)/\Omega_E\), or the Heegner index \([E(K):\mathbb{Z}P_K]\)). Kato / Kolyvagin bound \(\#\operatorname{Sha}[p^\infty]\) by the \(p\)-part of that integer, uniformly in \(p\).

In rank \(\ge 2\) every known Euler-system class that could play this role is either zero (Kato bottom class, Heegner point) or indexed by primes \(\ell\equiv 1\pmod p\) or by Kolyvagin primes for that \(p\) (derived classes). Lemma 3.2 of `03`: a fixed derived Heegner point of conductor \(\ell\) is a Kolyvagin class for only finitely many \(p\).

**[GAP H.2]** (same as GAP 7 / P3). Produce a \(p\)-independent rational \(c_E\in\mathbb{Q}^\times\) such that \(\#\operatorname{Sha}[p^\infty]\) divides the \(p\)-part of a fixed integer built from \(c_E\), \(\prod c_v\), and \(\#E_{\mathrm{tors}}\), for all but finitely many \(p\). Prop. 3.3 of `03` shows that \(\mathrm{U}(E)\) supplies this.

---

## 3. Descent algorithms: what they prove

`[THEOREM]` (standard 2-, 3-, 4-descent; Cremona, Fisher, Donnelly, Miller). For a fixed \(E/\mathbb{Q}\), descent computes \(\operatorname{Sel}_n(E/\mathbb{Q})\) for small \(n\) and hence an upper bound on \(r_{\mathrm{alg}}\) and on \(\#\operatorname{Sha}[n]\). Combined with exhibited points this often **certifies** \(r_{\mathrm{alg}}\) (PARI `ellrank` with \(r_1=r_2\); Sage `gens`).

This is a finite computation per curve. It does **not** prove \(\operatorname{Sha}[p]=0\) for large \(p\), and it does not prove \(\operatorname{Sha}\) finite.

For 389a1: \(r_{\mathrm{alg}}=2\) is certified; \(\operatorname{Sha}[p]=0\) is known for many ordinary \(p\) by [SW13] and the compute lab; \(\operatorname{Sha}\) as a group is not known to be finite.

---

## 4. Visibility does not close GAP H.1

Visibility realises a subgroup of \(\operatorname{Sha}(E)\) inside \(E'(K)/E'(K)_{\mathrm{div}}\) for an auxiliary abelian variety \(E'\). For rank-2 curves with analytic \(\#\operatorname{Sha}=1\), the predicted group is trivial, so visibility has nothing to find. For curves with analytic \(\#\operatorname{Sha}=4,9,\ldots\) (the LMFDB rank-2 examples in `compute/data/`), visibility can explain the known part; it does not bound the unknown part.

---

## 5. Residual gaps

**[GAP H.1]** \(\operatorname{Sha}(E/\mathbb{Q})\) finite for one \(E\) with \(r_{\mathrm{an}}\ge 2\).

**[GAP H.2]** A \(p\)-independent integer bounding \(\#\operatorname{Sha}[p^\infty]\) for almost all \(p\) (equivalent to P3 / \(\mathrm{U}(E)\)).

What would finish it: prove that \(L''(389a1,1)/(2\,\Omega\operatorname{Reg})\) is the rational number \(1\), or prove \(\mathrm{U}(389a1)\) by a Hida-family identity that the ratio \(L_p^{(2)}(0)/(\varepsilon_p\operatorname{Reg}_\gamma)\) is independent of \(p\).
