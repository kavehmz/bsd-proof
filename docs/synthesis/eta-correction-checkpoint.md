# Checkpoint: higher-period review and eta correction

Date: 2026-09-12. Agent: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
This bounded task is complete; the universal BSD objective remains active
with the coordinator and is neither proved nor disproved.

## Completed and reviewed

* `review-higher-period-integrality.md` gives an independent PASS for the
  anchored Chen sign/factorial, logarithmic translation orbit, vanishing
  of ordinary higher rational group cohomology, corrected eta second jet,
  and period-height determinant normalization.
* `eta-correction-certificate.md` proves, for the actual normalized form
  of 389a1 and the exact rho/U definitions in the higher-period note,
  `110 < C_E = integral rho(x)*U(x)^2 dx < 111`.
* `compute/scripts/certify_eta_correction.py` generates
  `compute/data/eta_correction_389a1.json` using exact Fourier and eta
  logarithm coefficients, rigorous Arb integration, and three explicit
  tails. The eta coefficient is sigma_1(n)/n <= n.
* The coordinator independently rederived the analytic bounds and checked
  the implementation. A second run with 128 bits, T=50 and decay=70 has its full
  correction interval strictly inside the principal 96-bit, T=40, decay=60
  interval; this inclusion was independently verified using exact fractions.

The full correction is near 110.303049551948660. The headline theorem is
the exact positive interval, not the extra digits of the truncated finite
integral before adding its tail.

## Exact consequence and scope

The already proved relation is
`L''(E,1)/2 = 4*pi*(J''(0)-C_E)`.
Consequently the uncorrected shortcut `L''(E,1)/2 = 4*pi*J''(0)` is
false on 389a1: its two sides differ by 4*pi*C_E, strictly between 440*pi
and 444*pi. This is not a counterexample to BSD or to a published
first-derivative theorem.

No rationality, integrality or arithmetic regulator interpretation of
`J''(0)-C_E` has been proved. That corrected difference remains the
meaningful target for a subsequent secondary-period/Green-function
arithmetic construction.

## Reproduction

From `/Users/kaveh/bsd-conjecture`:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
  compute/scripts/certify_eta_correction.py
```

The independent alternative was saved in
`.tools/research-2026-09-12/eta_correction_check.json` with
`--bits 128 --cutoff 50 --decay 70 --out <chosen-path>`.
Exact file hashes and error formulas are recorded in the certificate.

The contemporaneous family-specialization review fixes were also completed
in `family-specialization-attack.md`; its separate checkpoint now records
the independent PASS and the explicit Bockstein-descent premise.
