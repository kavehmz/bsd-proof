# Higher arithmetic theta checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Status: completed bounded constructions; all new deductions passed
[independent review](review-higher-arithmetic-theta.md).
Owned proof: [higher-arithmetic-theta-attack.md](higher-arithmetic-theta-attack.md).
Full BSD over Q remains the parent objective and is unproved.
No shared synthesis, agents, or old numeric certificates were changed.

## Fixed target

Retain Q=E_L'''/6+h0 E_L''/2+h1 E_L'+h2 E_L, with all h_j fixed by
Gamma(1+t)xi(1+t)=1/t+h0+h1t+h2t²+... and
h0=−(gamma+log4pi)/2, in Du–Yang1702.07917v2 conventions.
The original f-weighted pairing and its exact mass
−3N(N−1)ell L(E,2)/(2pi³) remain required.
The target line isD_pt⊗B2⊗Q(1)^(−2), with coefficient6N(N−1)n_E.
The actual arithmetic B2 extension and sufficient integral multiple
are completed inputs; no primitive lattice is inferred.

## Completed genus-two arithmetic construction

On the actual arithmetic modular stack, SSY's rank-one face cycle is
Zhat(diag(0,t),diag(v1,v2))
=Zhat(t,v2)*omega_mod−a(logv1 delta_Zt) for t>0,
omega_mod=−2omega_N−X_N^0+a(logN).
The full negative-square cusp modification and the T=0 cycle
omega_mod²+a(logdetV*[Omega]) are explicitly retained.
Its zero-term degree has slopeC_N=(N+1)/24 inlogdetV,
using source stack and archimedean degree factors.

The native SSY45-page revision Cor4.16 gives2W_t'(.5)
+(logv1+c_N)W_t(.5), with
c_N=2+4xi'(2)/xi2+(N−1)/(N+1)logN.
Its exact normalization(226) is
A_N(s)=−s/(4pi)xi(2s)(1−N^(−2s))N^(.5+1.5s).
A_N(1)=−(N²−1)/24 and
c_N−2A_N'(1)/A_N(1)=−2NlogN/(N−1).
Thus the arithmetic degree coefficient is exactly
−[2E_t'(1)+(logv1−2NlogN/(N−1))E_t(1)]/(N−1).
No informal extra stack factor is inserted.

Subtracting this fromQ gives the explicit residual(3.4).
The selected genus-two response has second Laplacian zero;
the residual's third Laplacian is−E_t(1)/64.
The explicit norm-one vector gives a nonzero t=1 coefficient.
This excludes only the stated face projection, not all genus-two
cycles or all arithmetic constructions.

## Completed higher Chow / analytic torsion construction

LetS be a fine level35N modular curve overa numberfield, E/S
universal, U=E\E[5], A=E³, W=A\A[5].
The relative dimension is3 and total dimension4.
For nonzero5-torsion sigma, rigidified Picard theory andomega^12=O
givef_sigma with exact divisor60(sigma−0).
The actual trace projector defines
xi_sigma=(36−tr[6])[f_sigma]/2100.
Trace acts by36 onbaseunits and1onresidues, proving independence,
norm invariance and residue(sigma−0).

The closed codim2 embeddings are
i1(x)=(x,tau,upsilon),i2(y)=(0,y,upsilon),i3(z)=(0,0,z).
Xi=sum i_j*xi_j is an actual NONZERO class inCH³(W,1)_Q,
with explicit graph cycle and denominator2100.
Residues telescope to(sigma,tau,upsilon)−0.
The trace onthese pushed supports is elliptic trace, not6^6.
KR's weight-zero residue isomorphism identifies this already
constructed cycle with the genuine higher polylogarithm.

Kings–Rössler1412.2925v2 gives
−2cyc_an(Xi)=(T_−a*g_{A∨}−g_{A∨})|W.
This is degree5 analytic Deligne cohomology withR(3), represented
by a(2,2) current class modulo im∂+imbar∂.
The canonical Green current comes from the Poincare bundle and
higher analytic torsion; no adjustable metric is used.

Both natural scalar projections were computed:
- Xi vanishes onU³, hence at any all-nonzero7-torsion section,
  because that open misses every partial-torsion support.
- ForL=product ofrigidified principalP=O(0)⊗omega,
  Xi*c1(L)=0 rationally. Each i_j^*L has torsion/baseomega
  Chern class andomega^12 is trivial.
- The canonical global-current fiber integral also vanishes:
  ∫(T_−a*g_A−g_A)∧c1(L)=∫g_A∧(T_a*c1(L)−c1(L))=0.
  It is proved onthe compact fiber, not by extending an unknown
  equality fromW. The pushed-unit averages agree.

The nonzero Xi remains onthe three partial-torsion strata before
these projections. The theorem does not extend its abelian-scheme
premise through generalized elliptic cusp fibers.

## Exact remaining gap

HAT-389 requires another cycle/projection or secondary extension
realizingQ AND the original f-weighted comparison in the fixed
rational determinant line. The coordinator's adjoint-theta work
is separate and not assumed. Rationality and integral primitivity
ofn_E remain unproved. These bounded tasks are complete.

## Sources and reviews

- SSY43-page arXiv2206.05823v1 was checked against the45-page author
  revision used for exact numbering and coefficients:
  https://home.cc.umanitoba.ca/~sankaras/ArithSW-rev1.pdf .
  Local /tmp/higher-theta-ssy.pdf SHA256
  59c0b417227cbf4858cfc3405fbcf51641019c692a670731492757c44c019053.
- Kings–Rössler1412.2925v2,17Dec2014,27pages.
  Local /tmp/higher-theta-kings-rossler.pdf SHA256
  6eb0c6ab7208e5630f79f3b35b0b0b998ed8b71ffb371a90c83ba23d0c152893.
- Reviewed mathematical proof894f745a6ced0eb67bf926adf6f0ef319d311dc984beb7563680f52b68c9d7be.
- Independent PASS reviewd606d1716bd601c9826792a5abe9991f57ee26d578a53649fb9275cdd8bf2b9a.
  Subsequent proof edits only add PASS links/status.
- The separate [Heegner–Kato review](review-heegner-kato-comparison.md)
  is complete PASS, hash9b3d517a275fc8c632968cf24ff4bf35850d7312f34e01793258c82ab64bfc33,
  against corrected proof84297adc102effbcc5a1d92bafef70330b832bd970c58b31913555e72aa0a64e.
  The requested j_* versus fullGalois localization comparison was
  inspected; all integral derivative, BDV, Shapiro and cup formulas pass.

Parent owns further dispatch and shared synthesis. Do not repeat the
completed cycle or B2 construction as a new result.
