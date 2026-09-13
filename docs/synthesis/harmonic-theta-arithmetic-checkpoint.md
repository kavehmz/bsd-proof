# Harmonic theta arithmetic comparison checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Status: completed bounded construction; every new deduction passed
[independent review](review-harmonic-theta-arithmetic.md).
Owned proof: [harmonic-theta-arithmetic-attack.md](harmonic-theta-arithmetic-attack.md).
The parent objective remains FULL BSD over Q; it is not completed.
No shared synthesis edits, new agents or old numerical reruns occurred.

## Completed construction

The proof retains N=389, the actual normalized eta unit, transported
SOURCE Hodge norm, entire lattice sums, both cusps, both heat endpoints,
the fixed Laurent subtraction and every completion-pole term.

1. The exact integration-by-parts identity is
   M=(1/8)∫u(logu)²log|v_eta| f(z)S_N(z,u)dμdu,
   where S_N is the superlattice-minus-source sum with harmonic
   polynomial w². The heat subtraction has zero z-derivative and the
   cusp boundaries vanish by the joint Gaussian estimates. There is
   no integration by parts in u. The fine-chain denominator194 and
   full base curvature term−(N−1)y/pi remain in the proof.

2. The kernel polynomial Phi_C has divisor[C]−N[0] on the actual
   algebraic Hodge-frame Gm-torsor. Its weight is N−1, scaling by
   lambda^(−(N−1)); it is not a scalar unit on the modular curve.
   Its finite trace is sum wp(a)=−Npi²g/3, orNg/12 in the Tate frame.
   The cyclic torsion/polylog trace atD5 is8pi²g dw², or−2g in that
   frame. The declared KS convention gives−2[dlogv_eta], retaining
   the motivic Kummer Tate twistQ(1).

3. The degree-zero heat family H_C=(Theta'−1)−N(Theta−1) has
   finite partN/12log|v_eta|+N/2logN. Its paired family is exactly
   (N^s−N)M_T(s)/2, hence its second jet is ZERO. The full mass
   remains in residual(N−1)E*(z,s), not an omitted cusp or constant.

4. Du–Yang's full-family theorem givesI_KM(J_N)=xi(s)E_L(s).
   For the completed family use
   Gamma(1+t)xi(1+t)=1/t+h0+h1t+h2t²+...,
   h0=−(gamma+log4pi)/2. Its second coefficient lifts to
   E_L'''/6+h0 E_L''/2+h1 E_L'+h2 E_L. Every constant is defined
   by the fixed function, including the cubic gamma coefficient
   times the original residue.

5. The actual lower arithmetic intersection(5.8) is
   I_KM(j0)=2<phihat,Dhat0+(N/2)X_N^0>.
   HereA=Delta(Nz)^N/Delta(z),
   divA=(N²−1)Pinf−12N X_N^0,
   j0=(N−1)kappa−log||A||0/12 andDhat0=(divA/24,j0).
   The vertical term is necessary. The known Hodge/vertical/constant
   arithmetic span has second weight3/2 Laplacian zero; the full
   second spectral response has THIRD Laplacian−E_L(1)/64≠0.
   This is a scoped test, not a no-motive theorem. Codim3 vanishing
   refers to rational/real arithmetic Chow, not integral stack torsion.

## Exact remaining comparison

HT-389 requires an arithmetic cycle/extension realizing the second
radial moment AND the original f-weighted pairing, with a rational
map toD_pt⊗B2⊗Q(1)^(−2). Its frame value is
−Omega Reg L(E,2)/(4pi³), and the required coefficient is
6N(N−1)n_E. Rationality and integral primitivity remain unproved.
Realizing the unweighted lifted third derivative alone is insufficient.

The actual beta2 regulator line is not conjectural. Its unique rational
lift toCH²(regular389model,2), with a sufficient integral multiple, is
established in [the arithmetic divisor proof](k2-arithmetic-divisor-attack.md),
[independently reviewed PASS](review-k2-arithmetic-divisor.md).
It is not a primitive lattice or a proof of spectral rationality.

## Sources and review record

- Sprang1802.04996v2,19Dec2019, Theorems5.8/6.1. Rendered pp31/35
  showD^(1−w) in a shorthand display butD^(2−w) in the final proof.
  We use the directly checked finite reindexingD^(2−w).
  Sprang1801.05677v3 Theorem4.2 supplies the fixed-index comparison.
- Du–Yang1702.07917v2,4Feb2018,52pages, Theorems1.3–1.6,
  Prop2.2, normalization1.6. The prior v1 attribution was corrected
  to this actual inspectedv2; no formula changed.
- Temporary source /tmp/harmonic-sprang-polylog.pdf has SHA256
  a116198a0c40dd785ac417d5321e3906de26392afd0c6920489f71bc466727b0.
- Temporary source /tmp/harmonic-du-yang.pdf has SHA256
  6cc35991ffe96906f491db9ed005cad3ddb93398ad68d6132461604c4d78659b.
- Reviewed mathematical proof SHA256
  94321e7e1e1ec3bb2f548e9f73945de3f676cbf6f7aa6198cde8da5f056c39ce.
- Independent PASS review SHA256
  586b0ab8bde475ac643767ef78469bd6a31c511b6ac9d7d9877a0f41f0793511.
  Subsequent edits add PASS links, exact version links and the
  completed beta2 arithmetic-extension reference.

The separate [higher-Heegner review](review-heegner-higher-residue.md)
is complete PASS, hash
9739ec86649a7eecf03aa41270c1a57efa6454cef11efbb0b26d10a0fbedd83b,
against corrected proof627ab2762db0c56c94ee8eac3cff963e2dfb21ed2b0e5c89419df89adfc900f6.
The coordinator's polynomial-sign repair was inspected. The full strict
Selmer cyclicity and independent free-R lower direction passed; the
desired class vanishing remains open.

No further task is dispatched this round. Parent owns subsequent
research and shared synthesis. Resume fromHT-389 rather than repeating
the completed heat identities or beta2 construction.
