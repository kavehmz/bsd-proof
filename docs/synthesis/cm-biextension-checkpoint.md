# CM biextension cycle: checkpoint

Date: 2026-09-12. Agent `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Owned files: this file and `cm-biextension-cycle-attack.md` only.

## Scope

Construct an actual cycle or secondary class from P=(3,12), Q=(27,144)
on E:y²=x³+39x whose regulator gives the full determinant
D=4AB−(C−A−B)². Test whether its Poincaré/polylogarithm realization
can supply the torsion-moment comparison CM-Theta. Do not assume
Sha finiteness or rationality of the real BSD quotient. The universal
objective remains full BSD over Q.

The finalized `cm-regulator-tensor-attack.md` and
`cm-moment-source-check.md` have been read. Their restricted moment
normalization is reviewed PASS, including the central character,
Euler factors, exact periods, pole projectors and ray-class multiplicity.
The earlier pending cross-link is resolved. No previous computation
will be repeated in this task.

## Initial candidate and current status

The first candidate is the exterior expression formed from the
degree-zero divisors dP=(P)−(O) and dQ=(Q)−(O), compared with the
secondary Poincaré height pairing and its determinant. Its actual
Chow-motive projector and cohomological degree must be established
before calling it an exterior motivic class: geometric factor exchange
and the graded cohomological tensor exchange carry different signs.

Material results reached (full proofs saved in the attack note;
coordinator independent review **PASS** in
`review-cm-biextension-cycle.md`, with the explicit secondary-regulator
scope retained):

1. For z=dP×dQ on E², z+swap(z)=0 in CH0(E²). Proof: push to
   Sym²E, then its P1-bundle Abel–Jacobi map to E; the resulting
   degree-zero divisor is (P+Q)−(P)−(Q)+(O)=0. Flat pullback returns
   z+swap(z). Its ordinary Deligne regulator is zero because both its
   degree and Albanese class vanish. Under Künneth, geometric swap on
   H1⊗H1 is minus tensor swap, so the geometric minus projector
   selects Sym²H1, not the Tate exterior determinant. No nonzero Chow
   assertion about z has been made.
2. Use T=(0,0), A={O,P,Q}, B={T,P+T,Q+T}. The latter points are
   (13,−52), (13/9,−208/27), respectively. These supports are disjoint.
   The actual relative object H1(E\B,A), or its generalized-Jacobian
   1-motive [Div_A^0→J_B], has weight-graded ranks 2,2,2 at 0,−1,−2.
3. Rational third-kind differentials for the two B-divisors are
   kappa1=((y−52)/(x−13)−y/x)omega and
   kappa2=((y−208/27)/(x−13/9)−y/x)omega. They have exactly residues
   +1 at P_j+T and −1 at T. Integrals from O to P,Q form a 2×2
   period block. Their exterior product on the product relative pair
   gives its determinant by Fubini, with no guessed factor two.
   The genuine global regulator requires the canonical local
   splitting and finite-place height terms; these are now fully
   included in the next construction.
4. The complete admissible intersection calculation gives
   C2=(1/2)[[1,1],[1,1]], C3=−(1/2)[[1,3],[3,5]],
   C7=[[0,1],[1,0]], and zero at every other prime, including13.
   Ogg's formula and integral j show the three bad fibers are typeIII.
   The component correction is r_i*s_j/2. Horizontal depths use only
   x(B1)=13, x(B2)=13/9, x(P−B2)=x(Q−B1)=156/49.
5. Thus H_v=I_v+(1/2)log_v(r), entrywise, for the FIXED rational
   matrix r=[[3/2,27/98],[27/98,243/2]]. The corrected algebraic
   1-motive Msharp has lattice lifts 2u(d_i)+iota(r_i); framing its
   lattice by b_i/2 gives exactly the full global height matrix under
   the real or canonical ordinary splitting. This is a construction
   with rational Kummer points, not an arbitrary height scalar.
6. Its framed ordinary exterior square has graded ranks1,4,5,4,1
   in weights0,−1,−2,−3,−4. If N_v is the central height obstruction
   on the graded realization, then (N_v^wedge)^2/2 on the top frame
   is det(H_v) times the bottom frame. N_v is realization-dependent,
   not a rational motivic endomorphism; no projector is inferred.
7. Any rational 1-motive morphism from a source whose lattice has
   torsion image in its abelian quotient to Msharp has zero map on
   weight0. Compatibility would otherwise give a nonzero rational
   relation aP+bQ torsion. This rules out a direct frame-preserving
   transfer from finite torsion endpoint 1-motives. It does not rule
   out the full polylogarithm's higher extension classes or a derived
   operation creating a new extension.
8. The actual generalized Jacobian has Hom_F(J_B,Gm)=0 over every
   number field F: a torus character (n1,n2) extends exactly when
   its Poincaré pushout n1*e1+n2*e2 is trivial, but this class is
   n1*P+n2*Q and independence forces n1=n2=0. Thus its canonical
   local logarithms are not logarithms of algebraic group characters.
   This rules out a second specific elliptic-unit extraction map.

Primary sources newly read: Beauville–Voisin, math/0111146 (the
elliptic-curve symmetric-product argument); Bloch–de Jong–Sertöz,
2206.01220v2 §§2,4 (biextension periods and local/global heights);
Balakrishnan–Besser,1201.6016v2 §§2–4 (Coleman–Gross and sigma,
including exact −2 log sigma and denominator term); BKT0711.1701v2
connection description, Theorems4.15,4.23 and A.19; Deligne's original
HodgeIII §§10.1–10.3, especially constructions10.1.3 and10.3.4–10.3.13.
The polylogarithm torsion splitting is not being extended to
non-torsion points.

The coordinator checked all finite component and horizontal matrices,
the rational Kummer factors by independent Fraction group-law calculations,
both primary height conventions, the corrected 1-motive, the exterior
factors and weights, and the two arithmetic map obstructions. No formula
was repaired. The note's overbroad assertion that the secondary tensor
was “essential” was narrowed to the precise algebraic-character map
that Proposition7 excludes. The author read the completed review.

Next action: the first
missing equality is CM-Biex(16): construct a rational framed element
Ztheta in the line generated by Xi_PQ with real realization
(L''/2)/(2Omega_E) and p-adic realization c_cmp*M_p/(4e_p) for every
good split prime in scope. Its real equality would prove n_E rational;
this is not assumed. The attempted direct map is excluded by item7,
while the full polylogarithm does not yet give a verified higher map.
No computation was rerun, and no process is running. Neither Sha
finiteness nor a new complex BSD comparison has been proved.
