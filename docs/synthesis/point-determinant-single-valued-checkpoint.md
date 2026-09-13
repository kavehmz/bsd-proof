# Restart: the geometric point determinant and the relative transport test

Date: 2026-09-12. Owner: root/coordinator. All seven sections COMPLETE.
[Proof](point-determinant-single-valued-attack.md),
[PASS](review-point-determinant-single-valued.md).
The initial six-section review and the additional §7 audit are recorded
separately. Latest review hash:
e179b03c7c718c64fc11898f065ec73df33d1b87ca76d00c641da05ca6206111.
Full BSD remains active and unresolved. No root process is live.

## Fixed inputs and exact new calculation

Use the ACTUAL corrected 389a1 one-motive M=[Z²→J(E,A)] from the
relative-modular-cycle proof. Its fixed rational principal corrections
make every finite height symbol zero. P,Q are the full point basis.
The Betti realization V has weights0,-1,-2, rank2 each.
Use the FULL support B* of the corrected divisors Z_j, not the three
original endpoints. The marked relative pullback lattice is retained.

For the rectangular periods tau=i t0, write v_j=r_j+s_j tau.
Let gamma'_j=gamma_j-r_j a-s_j b,
k_ij=C_ij-r_j A_i-s_j B_i, and
e_j^D=gamma'_j-sum_i k_ij t_i/(2pi i), with positive punctureloops t_i.
The periods of omega0,rho1,rho2 vanish on e_j^D, and its conjugate
differs only by the torus subspace, proving it is the Deligne lift.
Re k_ij=H_ij, the already normalized FULL BSD point-height matrix.
Consequently

    bar(e_j^D)-e_j^D=-(i/pi)sum_i H_ij t_i,
    delta_V(e_j^D)=sum_i H_ij t_i/(2pi),  delta_V²=0.

This computes the sign directly; it is not transplanted from a dual
biextension. Scalar Betti conjugation is not geometric real Frobenius
or an unmarked rational de Rham single-valued matrix.

## Geometric exterior square and exact lattice

Let N=wedge²V, framed by e1 wedge e2 at top and t1 wedge t2 at bottom.
Its weights0,-1,-2,-3,-4 have ranks1,4,5,4,1.
Relative Kunneth identifies H1(U,B*) tensor² with
H2(U²,B*×U union U×B*), with no Tor because the first group is
free and the relative homology is concentrated in degree1.

Geometric interchange acts MINUS ordinary tensor swap, so the
PLUS geometric projector gives the exterior square. Its rational
projector has denominator2. Integrally use
x wedge y→x tensor y-y tensor x on BOTH extreme frames.
This identifies the exterior lattice with the invariant tensor lattice.
The ordinary tensor-to-wedge quotient would multiply that map by2;
it is not used as the inverse. No ambient saturation claim is needed.

On the actual exterior object,

    delta_N²(e1^D wedge e2^D)=Reg_E(t1 wedge t2)/(2pi²),
    psi^D(bar e_N)=-Reg_E/pi².

The usual imaginary-part height ht1 and linear-delta height ht2
BOTH vanish. The full REAL quadratic coefficient survives.
The specified quadratic functional2pi² psi(delta_N² e_N)=Reg_E.
Canonical delta and Deligne projections are Hodge operations,
not rational MHS morphisms.

For a two-step Tate object supported only in weights0,-4, delta²=0.
Naturality therefore forbids a map fromN retaining its bottom,
or a map toN retaining its top. This is only that actual collapse test.

## The actual K2 extension and tensor vector

The SAME beta2 gives a rational geometric extension
0→H¹(E,Q2)→B_beta→Q0→0. The reviewer explicitly checked its
construction by support localization of the refined rational
higher cycle, rather than inferring rationality from a REAL Ext group.
Its native regulator remains i eta_K, with periodL(E,2)/pi.

If U_beta=bar e_beta-e_beta=-2i delta_beta e_beta, then the
extreme weight-7 vector onN tensor B_beta is

    -Reg_E/pi² ·1(2)_B tensor U_beta.

This is a coefficient of the actual tensor realization. Retain
the comparison of1(2)_B with1(2)_dR. The separately specified mixed
period uses Omega_E=2omega1, Reg_E, L2/pi and(2pi i)^(-2), giving
-Omega_E Reg_E L2/(4pi³). It is not an ordinary rank-one height
or an inferred rational value. The level389 is written explicitly
in §6 to avoid confusing it with exterior objectN.

## Additional §7: the literal relative-extension map fails

For the actual proper pairV0=X×E,B0=two cusp fibers,

    0→H¹(E)→H²(V0,B0)→H²(X) plusH¹(X)tensorH¹(E)→0,
    0→R(-1)→H³(V0,B0)→H³(V0)→0.

Thus D=H²(V0,B0,R2) has weights−3,−2, and H³ aftertwist has
weights−2,−1. The actual relative Deligne cone and strict Hodge
filtration give

    H_D³(V0,B0,R2)=D_C/(F0D_C+D_R)=Ext¹_R-MHS(R0,D).

The realF0 term in degree3 iszero by negative weights.
The quotient/extension correspondence is constructed explicitly
from a real and an F0 lift; no unrestricted absolute-Hodge
equivalence is asserted. Every associatedB_c has weights0,−2,−3,
so delta_Bc²=0.

OnN, delta_N² is nonzero on top and killsW−1.
OnN tensorB_beta,
delta³=3delta_N² tensor delta_beta is likewise nonzero on top
and zero onW−1. Hence NO real MHS mapB_c to either target can
be nonzero on top. This applies toC_j2 and any hypothetical
rational lift in that same relative group.
Twisting only the target byQ(-2) raises its top to4; a map from
B_c=W0 cannot reach it. Twisting both sides preserves nilpotence.

Scope: this tests literal MHS maps, not all coefficient extensions,
secondary operations, rational motivic lifts, or BSD. The next
comparison must actually construct the additional extension data
or another justified secondary operation. PD-389 remains open.

## Sources, reviews and companion work

Primary sources read by root and independent reviewer:
Burgos Gil–Goswami–Pearlstein2410.17167v3,67pages,headerJuly9,2026,
§§1.4/2.1–2.3/5.1; Deligne HodgeIII8.2.10,8.3.8–9,
DOI10.1007/BF02685881; Sertoz–Ouaknine–Worrell2505.20397v1
§6.5 Proposition6.5.43. Exact URLs are in the proof/review.
Brown–Fonseca2508.04844v2 was inspected, but its de Rham
real-Frobenius involution is not applied here.

Root's companion reviews are complete:
review-relative-cup-trace.md (whole K2 retraction and full real image),
review-heegner-native-height.md (actual isogeny/CTP and point/Prym subcase).
Uniform independently reviewed the CM symbol-point construction.
Root read its full606-line proof/review and reproduced only the
NEW psi5/psi7 Fraction values and both rational leading coefficients;
all passed. No old certificate or prime scan was rerun.
Current shared synthesis and next ownership are in research-state §5
and next-research-plan.md. Revalidate tools on resumption.
