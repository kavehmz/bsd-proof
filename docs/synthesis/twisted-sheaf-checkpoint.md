# Twisted-sheaf lifting restart checkpoint

Date: 2026-09-12. Agent `/root/uniform_witness`, GPT-6 Astra/xhigh.
Own only `twisted-sheaf-lifting-attack.md` and this checkpoint in
`docs/synthesis/`.

The parent objective is full BSD for every elliptic curve over Q. This
bounded task attempts an actual HB-cycle construction using twisted sheaves,
Azumaya algebras, determinants, Poincaré moduli, and arithmetic descent on the
fixed regular model of389a1. A test-curve reduction is not completion.

Required inputs: AGENTS.md, current research-state, the final reviewed
Hecke–Brauer note, and the explicit Weil–étale model. The key established
fact is Br(𝓔)=Sha(389a1), as whole groups. Local Selmer line bundles and
extension to one fixed arithmetic model are already available; neither is
the missing global lift. No finite-Sha premise may be added.

Historical starting candidate, completed below: an n-torsion Brauer class
was lifted to a mu_n gerbe, with stable weight-one twisted sheaves of
fixed rank and determinant and a zero-section framing. Local triviality
supplied local objects, and their actual moduli descent obstruction was
then analyzed. A uniform rank/degree was not obtained from this construction
or from boundedness at a fixed Hilbert polynomial.

No prior mathematical script has been rerun. No new subagent was spawned.

## Material construction saved; both independent reviews PASS

Let β∈Br(𝓔)=Sha(E) have period n, E=389a1, and choose a μ_n Kummer lift
z on𝓔 with geometric degree0 (adjust by the zero-section divisor). On
generic E, consider geometrically stable weight-one twisted bundles of
rank n, determinant O_E(O) with a chosen determinant identification.

Over Qbar this moduli stack has one coarse point and automorphism μ_n:
stable rankr degree1 bundles with fixed determinant on an elliptic curve
are geometrically unique. There is a short on-page proof by induction:
V1=D; Vr is the nonzero extension0→O→Vr→Vr−1→0; Ext¹ is1-dimensional;
any destabilizing subbundle would split the extension. Conversely a stable
degree1 bundle has one nowhere-vanishing section and stable quotient of
rankr−1. This avoids applying Lieblich's genus≥2 corollary to genus1.

The trace/Serre-duality calculation gives H¹End0=H²End0=0, excluding
infinitesimal thickening. The fixed-determinant moduli is a μ_n-gerbe overQ.
At every completion β=0, and z=c1(M_v) with degM_v=0. The root gerbe's
tautological line T_v, tensored with the ordinary stable rankn degree1
bundle of determinant O(O)⊗M_v^−1, supplies a local twisted object with
the desired determinant. The base-field moduli gerbe is locally neutral;
H²(Q,μ_n)=Br(Q)[n] and BHN make it neutral globally. This constructs a
global twisted rankn bundle. It does NOT construct a twisted line or splitβ.

Lieblich math/0511244v4 Props3.1.2.1(1)–(3), Lemma3.1.3.1 and
Prop3.1.3.9 verify extension of generic twisted sheaves via reflexive hull
on a regular surface. Use the G_m gerbe for this step, so no false
invertibility assumption on n at arithmetic fibers. Change-of-band
equivalence is Lemma3.1.1.12. The global End bundle is Azumaya of degree n.
Section4 preserves the entire generic bundle by spreading it to an open
and extending that sheaf, rather than only a generic vector space.
Pic(𝓔)→Pic(E) is already an isomorphism, so its descended determinant
extends as O_𝓔(O). Stability at every bad fiber is NOT asserted.

Determinants show periodβ divides the rank of every twisted vector bundle.
Thus minimal rank is exactly n, and the rank image of twistedK0 is nZ.
This retains precisely the information ordinaryK0 may lose; no Brauer
splitting conclusion is inferred from root's ordinaryK0 lattice.

Root suggested an independent Poincaré construction, now proved in §5:
for the genus-one torsor C corresponding to ±β, period=index supplies a
degree-n effective divisor Z. The universal twisted Poincaré line on
C×PicardGerbe(C) restricted to Z and pushed to E yields rankn twisted
bundle. The Poincaré sign is fixed via cocycle t_sigma=σP−P, whose
translation factor is L_{−t_sigma}; dualize/replace C to matchβ.
This supplies an optimal period-dependent rank, not a uniform bound.

First exact remaining step after constructing A_β=End(V): produce a
rational section over E of its Severi–Brauer bundle, or a splitting cover
of degree bounded independently ofβ. Local sections follow fromβ_v=0;
a global section is precisely a rank-one twisted object. Any finite
splitting degree and any twisted rank must be divisible by n.

Primary sources verified:

- Lieblich, Twisted sheaves and the period-index problem, math/0511244v4,
  https://arxiv.org/html/math/0511244; Compositio144(2008)1–31,
  DOI10.1112/S0010437X07003144. Use the exact gerbe/Azumaya/extension
  statements above; do NOT use finite-field/algebraically-closed-field
  period-index theorems over the arithmetic surface.
- Atiyah, Vector Bundles Over an Elliptic Curve, Proc.LMS(3)7(1957)414–452,
  DOI10.1112/plms/s3-7.1.414; degree1 case is proved directly.
- Lieblich2011, Arithmetic aspects of moduli spaces of sheaves on curves,
  Clay Math.Proc14 pp95–119 (in fullvolume cmip014c.pdf): its global
  period-index theorem3.4 is CONDITIONAL on a moduli Hasse-principle
  conjecture; do not quote as unconditional. Our genus1 coarsepoint
  argument uses BHN directly and no general rationally-connected
  Hasse principle or finite-Sha assumption.

## Latest positive step: Fourier–Mukai rank one with its actual target

The full proof is saved in twisted-sheaf-lifting-attack.md, §§1–11.
Sections9–10 are the latest addition and have passed independent review.

- Let H=PicardGerbe^0(C), with universal weight-one P on C×H.
  Dual-kernel transform Ψ(V)=Rp_C*(P∨⊗p_E*V) has target D(C).
  The tensor is weight0 and descends to C×E. The target is the actual
  torsor C, not a geometric identification Cbar=Ebar.
- Before claiming (n,1)→(1,−n), align degrees: det(Wβ) of the rankn
  Poincaré pushforward is weightn, with geometric degree0. Its
  trivialization gerbe defines a μ_n reduction G′ ofH. Geometric
  nth roots of the degree0 determinant have degree0, so this reduction
  agrees with Poincaré degree. Extend its Kummer lift by Pic(surface)=Pic(E)
  and repeat the stable fixeddet construction onG′.
- Fibers of Ψ(V) have H¹=0,h⁰=1 by stability/degree1, so it is an actual
  ordinary line bundle onC. For normalized P, D=Δ−E×O−O×E has D²=−2.
  GRR gives degree−n. Its dual yields a degree-n effective divisor onC.
- Retain the shift: ΨΦ=[−1], so the actual inverse is Ψ[1]. The unshifted
  transform is itself an equivalence but not the stated inverse.
  The Jacobian's fixed Néron differential induces an invariant differential
  onC, trivializingω_C in the actual right-adjoint formula.
- Additional explicit positive construction in Prop9.2: identifyW|O=L,
  choose rational nonzeroτ∈T_OE and use extension vector1⊗τ to construct
  0→W→V_D→kO→0. All conjugate coordinates are nonzero. This makesV_D
  locally free and stable: any destabilizing subbundle would intersectW
  in a degree0 sum of a proper subset of its distinct geometric lines,
  while the extension has nonzero projection to every complementary line.
  The detW μ_n reduction makesdetV_D=O(O). This is also
  V_D=Φ(O_C(−D))[1], so Ψ(V_D)=O_C(−D). Rank reduction returns exactly
  the individual degree-n divisor class used as input.
- Explicit descent: A(x,y)=t_x* tensorL_y; standard Fourier S acts
  (x,y)→(y,−x), tensorO(O) T acts(x,y)→(x,y+x).
  Thus the twistedE pair(0,ξ) moves to(ξ,0), meaning a torsor.
  For g=(a b;c d), the exact standard-action H¹-pair stabilizer is
  b≡0,a≡d≡1modn. It is NOT asserted sufficient for actual kernel
  descent, whose scalar/base-field Brauer2-cocycle is retained.
- Numerical matrix alone has inversion/shift ambiguity. Inversion has
  numericI but negates the pair; shifts multiply numerical signs but
  centralize translation/tensor. The inverted version allows
  a≡d≡−1modn, alwaysb≡0. Do not forget this sign qualification.
- A separate full-category check is independent of that classification:
  numerical image K0β(E)=nZ⊕Z because Wβ=(n,0),V=(n,1).
  Every actual self-equivalence preserves it, forcing n|b and rank
  of the image of(n,1) divisiblebyn. It cannot become a line onE
  when n>1. No nonzeroβ for389 is asserted.
- Section10.2 computes the actual generic-curve twisted lattice:
  K0β(E)≅K0(C)=Z⊕Pic(C)≅Z⁴. Local solubility+BHN descends every
  rational Picard class, Pic⁰(C)=E(Q)=Z², and degreePic(C)=nZ split byD.
  The Euler form has radicalPic⁰ and matrix(0 n;−n 0) on its numerical
  quotient, determinantn². Thus fixed abstract rank retains the period
  in a genuine arithmetic pairing. This is explicitly not a computation
  of twistedK0 of the arithmetic surface.

New primary sources: Ramachandran–Rosenberg arXiv:2212.14497v2,
Theorem2 and§§3.1,3.4–3.6 for the torsor/Picardgerbe equivalence
(track inverse sign convention); Antieau–Krashen–Ward arXiv:1409.2580
§§4–5 for scalar Brauer-orbit versus H¹-pair descent distinction.
The kernel, rank-degree calculation and S,T formulas are proved directly.

Root reassigned the independent ordinary-K0 review to odd_rank_bridge;
it is now PASS in review-k-theory-lattice.md. Formula(6.2) consequently
uses the reviewed actualK0 lattice; this note's own deductions have now
passed their separate reviews as well. Do not duplicate that K0 review.

Both independent reviews are complete, with no outstanding repair. The construction
target TS-389 remains §8: a rank-one splitting onE or uniform degreeB.
The Fourier–Mukai line-onC construction does not solve it. FullBSD
remains the active universal objective.

Completed review allocation: root reviewed§§1–8 and the global-gerbe
construction; higher_period_integrality reviewed§§9–10.
Root-requested precision repairs have been applied: fixed-determinant
rigidity follows from H¹End0=H²End0=0 (trace/Serre duality, characteristic0);
the regular-surface extension uses étale neighborhoods of the base,
not a purported étale scheme atlas of the Gm gerbe. The FM reviewer
requested the differential normalization ofω_C, also applied.

Both complete PASS records are saved:
[global gerbe, extension and Azumaya review](review-twisted-sheaf-lifting.md)
and [Fourier–Mukai and generic lattice review](review-twisted-fm.md).
The latter records the reviewed mathematical revision SHA256
189b1734c29080858c38f7a945c117a941b3d027154c9c95a9f0336e77a5ab73.
Subsequent edits only update review links/status and this checkpoint.
The bounded construction task is complete. No uniform splitting bound,
Brauer annihilator, or proof/disproof of fullBSD has been obtained.
