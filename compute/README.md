# `compute/` — computational laboratory for BSD (rank ≥ 2)

Everything here is reproducible from the scripts in `compute/scripts/`; every number quoted in
`compute/RESULTS.md` carries the command that produced it and the precision used (charter rule 6).
Raw outputs live in `compute/data/`. Software is installed *only* under `.tools/` (git-ignored); nothing is
installed system-wide.

## Fresh-machine recovery

Start with [the migration guide](../docs/synthesis/migration-guide.md).
`python3 compute/scripts/verify_handoff.py` verifies the saved checkpoint
without Sage. The portable archive includes working files, raw logs and
cached data; installed native environments must be rebuilt for the new
machine. [The package inventory](environment/installed-package-inventory.json)
records actual installed versions and the same-platform explicit specs.
The 2026-09-13 metadata shows cypari2 **2.2.2** in both environments;
the earlier installation-log version 2.2.4 below is historical.

The original independent CM verifier contains an audited absolute path.
Preserve its bytes and use
`python3 compute/scripts/run_cm_local_verifier_portable.py --check`
to inspect the portable adaptation. When a rerun is needed, use
`sage -python compute/scripts/run_cm_local_verifier_portable.py`.
It saves a separate result and explicit adaptation provenance; the original
script and certificate remain intact. Full execution of this adapter was
not part of the migration audit. Other historical reproduction commands
below assume the project root as the current directory.

## Exact local CM Taylor test (2026-09-13)

This NEW test concerns the local norm-family Taylor coefficients, not the
original cyclotomic coefficient c2,p. It evaluates the original rho-weighted
derivatives on the exact4608-point CM orbit in F_(5^24). The observed
nonzero pattern for degrees1–4 is false,true,true,false. Its analytic
interpretation and precise review status are in
[the local point-map proof](../docs/synthesis/cm-local-point-comparison-attack.md)
and [the independent arithmetic review](../docs/synthesis/review-cm-local-taylor-certificate.md).

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/cm_local_taylor_mod5.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/verify_cm_local_taylor_mod5.py
```

The first writes [the original exact output](data/cm_local_taylor_mod5.json).
The second preserves the independent reviewer's exact audited code: it
uses the recorded workspace root /Users/kaveh/bsd-conjecture, checks the
two original input hashes, and writes /tmp/cm_local_taylor_independent.json.
Its completed output is also preserved permanently as
[the independent output](data/cm_local_taylor_mod5_independent.json).
It uses a different Gaussian-unit orbit, direct Legendre counts,
deterministic Frobenius witnesses and Hasse/Taylor-flow derivatives.
It also independently checks the rational formal-point valuations1,1,2.
The two original files should not be edited to make its hash checks pass.
Neither script supplies a global Selmer or full BSD certificate.

## Exact Kurihara witness (2026-09-12)

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/kurihara_witness.py
```

This computes $\widetilde\delta_{41\cdot61}=4\pmod5$ for 389a1, using exact
rational modular symbols and checking every input with both Sage and eclib.
It writes `data/kurihara_389a1_p5.json` and checks an exact mixed character
difference in $\mathbb Q(\zeta_5)$, including the imprimitive Euler factors.
The two independent points plus Kim's structure theorem imply
$\operatorname{Sha}(389a1)[5^\infty]=0$; the proof and precise scope are in
[`continuation-2026-09-12.md`](../docs/synthesis/continuation-2026-09-12.md).
This calculation alone does not certify the complex analytic rank or full BSD.

## Rigorous rank, archimedean, and exceptional-prime certificates

Run in dependency order:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_mellin.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_bsd_interval.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_exceptional_primes.py
```

The first uses rigorous Arb integrals and explicit infinite tails to certify
analytic ranks 2 and 3 for 389a1 and 5077a1. The second proves the full basis,
encloses the correctly normalized regulator and full real period, and certifies
$0.9931<n_{389a1}<1.0077$. The third proves the 2-, 3-, and 389-primary Sha
groups are trivial, retaining the extra zero at 389 and the normalized local
factors. Outputs are `data/analytic_rank_certificates.json`,
`data/bsd_archimedean_interval.json`, and `data/exceptional_primes_389a1.json`.
Proofs and review boundaries are linked in the
[current report](../docs/synthesis/final-report.md).

The archimedean interval does not establish rationality or exact equality to
one, and these finitely many prime calculations do not establish full BSD.

## Checks for the later proof attempts

```sh
python3 compute/scripts/coherent_measure_check.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_eta_correction.py
```

The first checks exact Fermat valuations used by the coherent integral measure
example; its series are not elliptic-curve L-functions. The second proves the
eta correction integral for actual 389a1 lies between 110 and 111, using rigorous
quadrature and three explicit infinite-tail bounds. Outputs:
`data/coherent_measure_example.json` and `data/eta_correction_389a1.json`.
The [eta proof](../docs/synthesis/eta-correction-certificate.md) explains which
proposed derivative identity this rules out. Neither check is a BSD counterexample.

## Arithmetic surface and CM-39 checks

```sh
python3 compute/scripts/arithmetic_surface_check.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39.py
```

The surface check verifies the regular cubic model of 389a1, its split node,
and the exact reciprocal interval for its arithmetic zeta coefficient. Its
cohomology statements are proved separately in the
[Weil–étale note](../docs/synthesis/weil-etale-lattice-attack.md).
The CM check reconstructs Fourier coefficients through 1405 from finite-field
counts and recurrences, then certifies analytic rank two for
`y^2=x^3+39x` with 112-bit balls and cutoff 48. Its interval is strictly
inside the first independent call's interval at 96 bits and cutoff 40.
Outputs are `data/arithmetic_surface_389a1.json` and
`data/cm39_analytic_rank_certificate.json`. Neither proves full Sha finiteness
or a BSD leading-term equality.

## Actual CM derivative and trivial 5-primary Sha group

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39_padic.py
```

This new certificate uses exact modular symbols for
`E:y^2=x^3+39x` (48672i1) and a proved measure error bound to give
`c2=20 mod25` and `c2=70 mod125`, where `c2` is the quadratic
coefficient of the Néron-normalized MTT series in `T=gamma-1`,
with `chi(gamma)=6`. The exact sums are respectively
`(A,B)=(3540,-275)` and `(46545,86450)`. Every required symbol is
checked by eclib and the fixed-denominator numerical algorithm;
their agreement is separate from the infinite error proof.

The [proof](../docs/synthesis/cm-derivative-nonvanishing-attack.md) and
[root review](../docs/synthesis/review-cm-derivative-nonvanishing.md)
deduce nonvanishing of the actual derived class, primary Selmer corank
two and `Sha(E/Q)[5^infinity]=0`. The integral determinant argument
also has a [separate audit](../docs/synthesis/review-cm-derivative-integral-bound.md).
The carry test `A2=-5,C=237` gives `5+15=20 mod25`; discarding the
carry would give a wrong residue. No claim at an uncomputed prime
or equality of the complex BSD quotient follows.

The script reads the existing CM rank certificate and the cached
primary table `.tools/ecdata/allcurves/allcurves.40000-49999`, and
records their hashes along with its own. The output is
`data/cm39_padic_derivative_certificate.json`. Root independently
reproduced the certificate and audited all finite rows with integer
arithmetic. The earlier certificate suite was not rerun.

If that one table cache is absent in a fresh workspace, obtain it from
the [primary Cremona repository](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.40000-49999)
at the indicated path before running the script. The exact row and
source hash are retained in the certificate. Sage's mini-database
warning does not affect the checked optimality and Manin constant1
theorem for this conductor.

## 1. Installation (macOS arm64, no Homebrew; tested 2026-09-11)

```sh
cd /Users/kaveh/bsd-conjecture
mkdir -p .tools
# micromamba 2.9.0 (static binary)
curl -Ls https://micro.mamba.pm/api/micromamba/osx-arm64/latest | tar -xj -C .tools bin/micromamba
export MAMBA_ROOT_PREFIX=$PWD/.tools/mamba          # keep the package cache inside .tools
# PARI/GP 2.17.3 (pthread build) + data packages + cypari2 2.2.4 + Python 3.11 (+ mpmath, numpy, requests)
.tools/bin/micromamba create -y --no-rc -p .tools/env -c conda-forge \
    pari pari-elldata pari-galdata pari-seadata cypari2 python=3.11 mpmath numpy requests
# optional (Step 2): SageMath 10.7 — succeeded in 17 minutes, ~2 GB
.tools/bin/micromamba create -y --no-rc -p .tools/sage -c conda-forge sage python=3.11
```

Installed versions (from `.tools/install-env.log`, `.tools/install-sage.log`): PARI/GP **2.17.3** (released,
arm64 darwin, GMP kernel, pthread engine, compiled Mar 10 2026), `pari-elldata 0.0.20161017` (Cremona's tables,
so `ellinit("389a1")` and `E.gen` work), `pari-galdata`, `pari-seadata`, `cypari2 2.2.4`, Python 3.11,
SageMath **10.7** (Release 2025-08-09; its own PARI is not used by our GP scripts).

### Wrappers

* `compute/scripts/gp` — runs `.tools/env/bin/gp` with `GP_DATA_DIR=.tools/env/share/pari` (elldata/galdata/seadata),
  `parisize=256M`, `parisizemax=32G` (p-adic L-functions are memory hungry), `realprecision=60` (= 256 bits;
  PARI rounds to 64-bit words, `default(realprecision)` reports 77), `nbthreads=16`.
  Usage: `compute/scripts/gp -q script.gp`, or interactively `compute/scripts/gp`.
* `compute/scripts/python` — Python 3.11 with `cypari2` and the same `GP_DATA_DIR`.
* Sage: `.tools/sage/bin/sage` (or `.tools/sage/bin/sage -python script.py`).

### Smoke test

```sh
compute/scripts/gp -q <<'EOF'
E = ellinit("389a1"); print(ellrank(E), " ", ellanalyticrank(E), " ", ellrootno(E), " ", ellbsd(E));
print(lfun(E, 1, 2), " ", ellpadicL(E, 5, 10, , 2), " ", ellpadicregulator(E, 5, 10, E.gen), " ", ellpadicbsd(E, 5, 10));
EOF
.tools/sage/bin/sage -c "print(EllipticCurve('389a1').padic_lseries(5).series(4))"
```
Expected: `[2, 2, 0, [[-2, 0], [4, 8]]]  [2, 1.5186330005768535...]  1  4.98042512171011...`, then
`1.51863300057685...  5^2 + 3*5^3 + ... + O(5^8)  4*5^2 + ... (unsaturated points)  [2, 5^2 + 2*5^3 + ... + O(5^8)]`;
Sage: `O(5^6) + O(5^3)*T + (4 + 4*5 + 5^2 + O(5^3))*T^2 + (2 + 4*5 + O(5^3))*T^3 + (3 + 2*5^2 + O(5^3))*T^4 + O(T^5)`.

## 2. Scripts and how to reproduce every result

| step | script | command (from the repository root) | output in `compute/data/` |
|---|---|---|---|
| (c) LMFDB | `scripts/lmfdb_rank2.py` | `compute/scripts/python compute/scripts/lmfdb_rank2.py --fields --sha --rank34 --reference` (JSON API) | `lmfdb_fields.json`, `lmfdb_rank_ge2_sha_ne1_N_lt_500000.{json,csv}`, `lmfdb_rank3_N_lt_500000.*`, `lmfdb_rank4_*`, `lmfdb_bsd_reference.json` |
|  |  | `compute/scripts/python compute/scripts/lmfdb_rank2.py --ecdata --picks --ecdata-reference 11a1,...,5077a1` (Cremona's `ecdata`, cached in `.tools/ecdata/`, ~130 MB) | `ecdata_rank_counts_by_conductor.{json,csv}`, `ecdata_rank_ge2_sha_gt1_N_lt_500000.*`, `ecdata_rank{3,4}_N_lt_500000.csv`, `lmfdb_rank2_sha_picks.{json,gp}`, `ecdata_bsd_reference.json` |
|  |  | `compute/scripts/python compute/scripts/lmfdb_rank2.py --compare compute/data/bsd_table.tsv` | comparison table (stdout; pasted into RESULTS.md) |
| (a) BSD table | `scripts/bsd_table.gp` | `compute/scripts/gp -q compute/scripts/bsd_table.gp` (60 digits; `BSD_SKIP_PICKS=1` to skip the 10 LMFDB curves) | `bsd_table.tsv` (full precision), `bsd_table.md`, `bsd_table.log` |
| (b) p-adic, PARI | `scripts/padic_ranks.gp` | `PADIC_CURVES=389a1,433a1 PADIC_PMAX=31 PADIC_OUT=compute/data/padic_ranks_pari_1.jsonl compute/scripts/gp -q compute/scripts/padic_ranks.gp` (no env: all 19 rank-2 curves, p ≤ 31, and 5077a1, p ≤ 17) | `padic_ranks_pari_*.jsonl`, `padic_ranks_pari_*.log` |
| (b) p-adic, Sage | `scripts/padic_ranks_sage.py` | `.tools/sage/bin/sage -python compute/scripts/padic_ranks_sage.py --curves 389a1,433a1 --pmax 100 --out compute/data/padic_ranks_sage_1.jsonl` | `padic_ranks_sage_*.jsonl`, `padic_ranks_sage_*.log` |
| (b) report | `scripts/padic_report.py` | `/usr/bin/python3 compute/scripts/padic_report.py > compute/data/padic_ranks_report.md` | `padic_ranks_report.md` (tables curve × p, summary, PARI/Sage cross-check) |
| (d) certification | `scripts/certify_ran.gp` | `compute/scripts/gp -q compute/scripts/certify_ran.gp` | `certify_ran.log`, `certify_ran.json` |

The p-adic runs were executed as 4 parallel chunks each (see the exact `PADIC_CURVES`/`--curves` lists at the top of
`padic_ranks_pari_{1..4}.log` and `padic_ranks_sage_{1..4}.log`); total wall time ≈ 1 h on 16 cores.

## 3. Conventions that matter (details and checks in `RESULTS.md`)

* **Real period.** `E.omega[1]` = least positive real period ω₁ of the minimal model. BSD's Ω_E = ∫_{E(R)}|ω| =
  [E(R):E(R)⁰]·ω₁, i.e. 2ω₁ if Δ>0, ω₁ if Δ<0. `ellbsd(E)` = Ω_E·∏c_p/|T|² (checked to 10⁻⁷⁶ on all curves);
  `elltamagawa(E)` = ∏_p c_p · [E(R):E(R)⁰]; `ellglobalred(E)[3]` = ∏_p c_p (finite places only).
* **`ellanalyticrank(E)`** returns `[r, L^{(r)}(E,1)]` — the derivative, not divided by r!.
* **`ellrank(E)`** returns `[r₁, r₂, s, pts]`, r₁ ≤ rank ≤ r₂; certified iff r₁ = r₂. Its points must be saturated
  (`ellsaturation`) before computing regulators (for 389a1 the raw points have index 3).
* **Heights**: PARI's `ellheight` uses Cremona's normalisation (= LMFDB/Sage; twice Silverman's).
* **p-adic L-functions**: PARI's `ellpadicL`/`mspadicseries` interpolate `(1-1/α)² L(E,1)/ω₁` (least real period), so
  for Δ>0 they are **2 ×** the Mazur–Tate–Teitelbaum series normalised with Ω_E (which is what Sage's
  `padic_lseries` computes). `mspadicseries` and Sage both use T = γ−1 with χ(γ) = 1+p. The p-adic regulators of
  PARI (`ellpadicregulator`) and Sage (`padic_regulator`) agree digit for digit.
* **`ellpadicbsd(E,p,n)`** returns `[r, L_p]` with L_p conjecturally = `ellpadicregulator` × |Sha|; PARI's normalisation
  absorbs (1−1/α)⁻², r!, log_p(1+p)^r, Tamagawa and torsion. Exception found: for 944e1 it returns 2·R_p at every p
  (see RESULTS.md (b)).

## 4. Data provenance

* LMFDB API (`https://www.lmfdb.org/api/ec_curvedata/`, `ec_mwbsd/`, `_format=json`; typed values `rank=i2`, range
  queries via Python literals `conductor=py{"$lt":500000}`; 100 records per page, `_offset` ≤ 10000). The site
  serves a reCAPTCHA page to scripted clients after a few dozen requests, so bulk counting was done from Cremona's
  `ecdata` (the upstream of LMFDB for N ≤ 500000): `https://github.com/JohnCremona/ecdata` files `allcurves.*`,
  `allbigsha.*`, `allbsd.*`, `allgens.*` (format: `docs/file-format.txt` in that repository).
* Cremona labels and generators come from `pari-elldata` (Cremona's tables inside PARI) and `ecdata`.
