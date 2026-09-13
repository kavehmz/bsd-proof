# Secondary Kummer theta checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Owned proof: [secondary-kummer-theta-attack.md](secondary-kummer-theta-attack.md).
The parent objective remains FULL BSD over Q. No shared synthesis edits,
new agents or old numerical certificate reruns belong to this task.

## Current status

The complete six-section proof passed independent review by
/root/uniform_witness in [review-secondary-kummer-theta.md](review-secondary-kummer-theta.md).
Reviewed mathematical proof SHA256:
eef3cc17f7b26ae2c134d8df6c7c2602c6f6e05c32fde9370a622ccc9c844ca9.
Subsequent proof-header and checkpoint changes are editorial.
The initial checkpoint was saved before sources; the former construction
sketch is superseded by the full proof and this current restart.

## Actual construction and boundaries

On the fine full-level 35N base S and the triple universal elliptic
family A, retain the already nonzero Xi in H5_M(W,Q3), W=A minus A[5].
Choose nonzero 7-torsion rho and the intrinsic rational function
b_u=1+(u-1)(x(sigma)-x(rho))/(x-x(rho)), where
u=N^(-6) Delta(z)/Delta(Nz). Its values are b_u(0)=1 and b_u(sigma)=u.
It is 1 on the second and third graph supports.

The precise finite base shrink S° excludes u=1, zero-divisor collisions
with nonzero 5-torsion, and zeros over the x-coordinate of NONZERO
2-torsion. Its divisor D=D+ disjoint-union D- is then smooth and proper
over S°, with relative dimension two, and lies wholly in W.
The cusp expansion proves this is a nonempty shrink.

The actual product is KUMMER FIRST:

    {b_u} cup Xi|_(W minus D) in H6_M(W minus D,Q4)
      --positive tame residue--> H5_M(D,Q3)
      --proper push--> H1_M(S°,Q1).

Rost's normalization is res{uniformizer,a}=a and
res{a,b}=(-1)^(va vb) b^va/a^vb. Thus the first graph gives
{b_u,F_sigma}/2100. Weil reciprocity gives the exact output {u};
the other graphs give zero. The output extends across all removed
finite base points because the specified u is a unit there.
Fine-level and field trace divide by their actual finite degrees,
so only a rational construction is asserted. No proper push from W
or extension of the abelian-scheme theorem across cusps is used.

## Regulator and compact graph

For the canonical global Kings–Rössler current difference
G_Xi=-1/2(T_(-a)^*g_(A-dual)-g_(A-dual)), the actual divisor contraction
is log|u|. This is interpreted in the conormal-wavefront category:
D avoids the zero and translated zero sections, the canonical
representative is smooth near D, and exact primitives must have
defined pullback. The pushed unit currents intersect D transversely.
Compact Stokes is applied only to these admissible pullbacks, not to
arbitrary representatives modulo partial/partial-bar exact currents.

On the compact rational surface X0(N) times E, the integral graph-unit
cycle Z_u=(Gamma_pi,u)-(X0(N) times O,u) belongs to CH²(-,1).
Its boundary cancels pointwise at both cusps because pi(0)=pi(infinity)=O.
Its real regulator is log|u| times the difference of graph currents.
Contracting with the actual Neron differential and pushing to X gives
log|u| alpha, with alpha=pi^*omega=c_pi 2pi i f dz.
Multiplication by -i/(4pi² c_pi) and d recovers F dmu.
The cycle has motivic type H3(Q2); the differential contraction is
an explicit de Rham operation, not an implicit rational scalar map.

The proper elliptic push is

    (pi times id)_*Z_u=(Delta_E,c)-(E times O,c), c=Norm_pi u=±1.

The norm has zero divisor and Fricke inversion makes c=c^(-1).
The pushed cycle is therefore killed by 2, and is zero rationally.
E-Pi1 then X-Fricke-odd projection also kills the actual class.
Nonzero current transgression does not prove the motivic graph cycle
nonzero and does not contradict either projected vanishing.

## Full radial residual

The exact full analytic family is recovered by (6.1), pairing log|u|
with d_z J_N(s) wedge alpha. Both cusps, all Fourier modes, the pole
coefficient, and the Manin constant are retained.
Naively weighting the graph current by j2 is not Deligne closed:

    ddc(j2 log|u|)
      =log|u| (j1+j0)dmu/(4pi)
       +(i/(2pi))(partial j2 wedge barpartial log|u|
                         +partial log|u| wedge barpartial j2).

Its leading cusp term is
[pi²(N-1)(N²-1)/6] y²(log y)² and has nonzero Laplacian.
This is an interior obstruction before any cusp extension is chosen.
The completed coefficient retains gamma_3 times the Laurent residue.
No product j2 delta_(div u), arbitrary metric rationality or primitive
integral frame is asserted.

The arithmetic comparison SKT-389 into D_pt tensor B2 tensor Q(1)^(-2)
remains missing, with exact requested coefficient 6N(N-1)n_E.
The mass remains -3N(N-1) ell_E L(E,2)/(2pi³).
Root's weighted-theta-adjoint proof supplies a separately reviewed
analytic interface when its review is complete; it is not used to
infer a rational map in this proof.

## Sources and review handoff

Read primary Levine1994 Theorem5.2/Corollary5.3, Rost1996 §1
and proper-boundary compatibility/curve reciprocity, and
KLM math/0409116 §§5.1–5.6. The sign audit fixed Kummer-FIRST
before promotion. Uniform independently rendered Rost p328
and checked KLM's cubical positive-divisor orientation.
The prior Kings–Rössler normalization and all Tate factors remain.

Also assigned: independently review the complete
heegner-tame-nullhomotopy-attack.md in
[review-heegner-tame-nullhomotopy.md](review-heegner-tame-nullhomotopy.md).
The full independent PASS review is saved, SHA256
53936de6a8777a037e250b82a178c9ce906a69ef8c0ca9c08adeb6852809b141,
against corrected mathematical proof90b0925736532683e8ee1ab03b6b5fc155b3b2ddb9f9844c14a47a14e0e3b713.
The inertia-equivariant auxiliary splitting and explicit compact-first
Weil order were inspected. Milne ADT II.2.9 directly supplies the
finite Galois/etale comparison with p inverted; no unproved higher
comparison is needed for the nullcochain search.

This bounded construction and the assigned reciprocal review are complete.
The secondary proof's independent PASS has been inspected and its
editorial status updates completed. Root handles shared integration.
The full BSD goal and original radial arithmetic comparison remain open.
