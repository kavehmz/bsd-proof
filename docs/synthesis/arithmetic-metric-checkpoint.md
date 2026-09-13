# Arithmetic metric realization restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
The previous goal turn was progress; constructions through ledger §14
have independent PASS reviews. No old certificate is to be rerun.

Completed root task, independently reviewed PASS in
`review-arithmetic-metric.md`: construct the decorated Mellin current as an
actual arithmetic Chow class on the already reviewed regular 389 model,
and test whether that is the rational realization required by MT-389.
Do not confuse rational coefficients in arithmetic Chow theory, whose
metrics contain real data, with membership in the fixed rational motivic
determinant line.

Reviewed exact calculation using the primary definitions:
the known CH₀(𝓔)=0 and the standard arithmetic Chow exact sequence
give a surjection from real (1,1) forms modulo ∂/bar∂ onto
widehat CH²(𝓔). On compact E(C), that form quotient is one-dimensional
by integration. Arithmetic degree composed with a(η) is (1/2)∫η,
so a is injective as well, and widehat CH²(𝓔)≅R via degree.
This is an actual group computation, not an abstract countermodel.

If M is the proved real mass of the decorated Mellin current and μ_E
is a smooth invariant probability form, a(2Mμ_E) has degree M.
Equivalently pull back the trivial line on SpecZ with ||1||=exp(−M)
and multiply its arithmetic Chern class by that of O(O), of generic
degree one. It has underlying cycle zero and realizes any real M.
The constant-metric example was already in the earlier arithmetic Green
note; the new results identify the entire top group and the actual
decorated-current class. Exact normalization, real-involution condition,
smooth/current quotient, and product were all checked in the PASS review.
The ordinary cup determinant in codimension four is zero, whereas the
determinant of the actual height degrees is positive. These constructions
do not prove rationality of the BSD scalar; the motivic/frame map remains
GAP AM-389. No old certificate was rerun.

Current handoff is in research-state §5. At the latest snapshot the
CM blended-extension task is running, the spectral regular-singular
draft is saved for independent review, and the O5 draft's explicit
scalar normalization repair is awaiting root's final check. All Astra/xhigh.
