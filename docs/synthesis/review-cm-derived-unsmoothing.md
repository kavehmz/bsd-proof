# Independent review: CM coefficient cones and higher augmentation

Date: 2026-09-13. Reviewer: /root/higher_period_integrality,
GPT-6 Astra/xhigh. **PASS for the complete eight-section bounded proof.**
No mathematical correction is required.

Owned file: this review only. Author's proof and checkpoint remain unchanged.
The full BSD objective remains active and unresolved.

Reviewing `cm-derived-unsmoothing-attack.md`, mathematical SHA256
`c37c8b717bea884135fc5a241a6318383f9bfc59c726449821be6bbfe9ac80df`,
and checkpoint
`798d00fa73f0affc9fff0be766bfaef3f4e0ad1f59f92007d527d86a920d5832`.

All eight sections and the complete checkpoint were read. This review
reconstructs the actual coefficient and norm maps, rather than checking
only their scalar summaries. The checkpoint's early exploratory passages
are historical: its final authoritative section and the proof control
the verdict. Editorial replacement of those snapshots and addition of
PASS links do not change this mathematical revision.

## 1. Primary inputs and exact scope

I directly read Kato's *p-adic zeta functions of modular forms*,
Astérisque295(2004), Proposition1.3(1)(ii),(4), the normalization proof
in1.10, and the character conventions in15.8. The
[published primary PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf)
was read from the existing local cache, because a new web fetch exceeded
the tool's size limit. Cache `/tmp/cm-derived-kato2004.pdf` has SHA256
`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.
The norm statement is an equality for the normalized function, with
constant one and degree prime to the smoothing integer. The author's
Theta_a is its already reviewed twelfth power. In the present applications
p is prime to a and the evaluation point is outside E[a]. No primitive
ray-orbit norm is substituted for that full-fiber norm.

I also directly read Nekovář, *Selmer complexes*, Astérisque310(2006),
[primary PDF](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
3.4.1–3.4.3 and8.1.1–8.1.6 (printed pp.82–84 and189–193).
The inspected local PDF `/tmp/cm-presentation-nekovar.pdf` has SHA256
`61c84e5ad3252a2e520747215ac57a282addc2b58c824a3637bcd77bbe02153f`.
These pages give the cochain differential, exactness on the finite
coefficient sequences, Shapiro's map, coefficient augmentation as
corestriction, and the functorial projection/replication maps used here.
No Selmer-control or derived base-change theorem is needed for the new
elementary argument. I checked the inherited division-field, full point
lattice and exact theta inputs against the complete predecessor and its
[separate review](review-cm-symbol-point-reciprocity.md).

The range is exactly the stated good split primes, p>=5, p congruent1
modulo4, p not dividing2·3·13, with m>=max(k,n+1). The full ray
homothety(-1,-1) fixes F0 and the cyclotomic layer: its cyclotomic
character is the product of its two components, hence1. It acts by-1
on rho and T_pi. This simultaneously justifies the transfer-zero and
H0-vanishing uses; it is not a consequence of a conjectural rank bound.

## 2. Actual cone class and the first-moment sign

The point-division scheme Y_R,m is defined over K_n. Its base change to
F_m is the actual single-point field of degree p^(2m). The finite
permutation module and augmentation kernel therefore define(3) before
any choice of division point. T_k is free of rank one over A_k, so
tensoring preserves exactness.

Finite étale Shapiro identifies the theta Kummer class with its stated
permutation-valued class. The rho vector is used only over F_m where
it is trivial modulo p^k. Its subsequent unnormalized corestriction
has the same coefficient module, defined over the base. The natural
G_n-action comes from these K-defined coefficients. Thus the fixed
group-ring unit q_a,n,k can act on this cohomology. Its invertibility
follows from its p-unit augmentation in the finite cyclic p-group
ring; neither the tame degree nor the character factor is removed.

Augmentation is exactly the single-point norm w_R followed by the
already checked rho-twisted transfer. The homothety kills this transfer.
In the long exact sequence, H0(K_n,T_k)=0 makes
H1(I tensor T_k)→H1(P tensor T_k) injective. Its image is precisely
the augmentation kernel. This proves both existence and uniqueness
of eta, without a local-condition or Sha premise.

For the inhomogeneous convention dv(g)=g(v)-v, the zero augmentation
class gives a unique v and, at h acting by-1, e(h)=-2v. Hence(7) has
the required minus sign. In a chosen point origin, the first component
of d(v e_Rm) is g(v) tensor kappa(R)(g), because
g e_Rm=e_Rm+kappa(R)(g) modulo I². Subtracting this coboundary gives
exactly(8), including g(v), not v. The identification of its point
factor is
E[p^m] tensor A_k → E[p^k], t↦[p^(m-k)]t;
it sends the actual point cocycle to kappa_(p^k)(R).
The intrinsic quotient I/I² and uniqueness of eta show that all
changes of origin or transfer representatives affect only the
displayed representative. There is no adjustable nullcochain.

## 3. The exact tower law

Projection of permutation basis vectors e_S↦e_[p]S is the coefficient
map corresponding to fiberwise norm. Over F_(m+1), each lower point
has exactly p² preimages, and their theta product is u_R,m because
[p]tau_(m+1)=tau_m. The resulting class is pulled back from F_m.
The further ray corestriction has degree p²; the rho vector is already
trivial over F_m. Consequently the full coefficient-valued class is
multiplied by p², with no normalization by that factor.

The field description independently agrees: the single-point tower
has degree p^4, while its theta argument runs through p² distinct
p-division points, each with multiplicity p². Its norm is therefore
u_R,m^(p²). This is different from the preceding joint tower's p^4
theta multiplicity. The commuting augmentation sequence and the
injectivity just proved transport this exact law to eta itself.

## 4. Full finite coefficients and every fixed jet

An origin identifies the torsor module with its translation group ring.
A different origin multiplies by a group unit, preserving every power
of the augmentation ideal. The actual torsor projections preserve this
intrinsic filtration and its affine Galois action.

For1<=j<p^r,
v_p binom(p^r,j)=r-v_p(j): the remaining factor
binom(p^r-1,j-1) is a unit, as its reduction is the corresponding
coefficient of(1+X)^(p^r-1). If
r>=k+floor(log_p d), then d<p^r and all defining relations of degree
at most d vanish modulo p^k. The coefficient jet at every level m>=r
is consequently identified, by the actual projection, with the same
truncated polynomial module. This statement concerns full A_k, not
just its residue field. Compatibility of origins gives one coordinate
proof of a Galois-equivariant isomorphism which is intrinsic.

Iterating the proved tower law gives p^(2(m-r))eta_r. It vanishes over
A_k when m-r>=ceil(k/2), yielding the precise threshold(11). Passing
through the coefficient-jet isomorphism proves(12) as a cohomology
statement. It does not replace a derived reduction by a tensor product
of cohomology groups. The full module and operations whose jet order
grows with m are not asserted zero. Comparisons involving additional
division or different normalizations are expressly outside this test.

## 5. The actual replicated higher layer and its coefficient type

The quotient of the joint torsor onto the R-torsor gives replication
of coordinates. This is the finite étale coefficient map, not a
choice of a scalar transfer. With an origin it is multiplication by
the full unused-direction norm. In characteristic p, for q=p^m,
that norm is X^(q-1)Y^(q-1), in exact degree D_m=2(q-1).

The old prescribed roots were repeated in precisely this unused
direction. Thus their cocycle is the replication of the single-point
cocycle. Its degree-D_m term is the augmentation delta_p(w_R) times
the canonical norm line. No nonvanishing of this scalar is assumed.
After the original twist and normalization its leading transfer
vanishes. More strongly, replication of eta already supplies a lift
in I_joint^(D_m+1). The homothety acts on degree D_m by+1 and on
T_pi/p by-1, so H0 of the entire twisted graded quotient is zero.
The coefficient long exact sequence therefore proves uniqueness of
this lift and its asserted canonical identification.

The next active coefficient retains E[p] tensor T_pi/p, with the
two stated CM characters Psi² and chi_cyc. The Weil pairing with
the actual CM summand gives a map to mu_p; it does not give a map
back to T_pi. The first moment and each fixed band of active jets
vanish by the full-coefficient theorem, even when viewed in the
replicated higher layer. No growing-degree filtration is identified
with a fixed integral graded polynomial ring outside the proven
characteristic-p calculation.

## 6. Rational systems and the unsuppressed endpoints

The rational single-point system p^(-2m)delta_Qp(u_R,m) is compatible
under its actual field norm because that norm multiplies the Kummer
class by p². The joint normalization p^(-4m) works for the distinct
joint tower for the same reason. The two ray-field norms in(15) both
equal p^(-2m)delta_Qp(w_R), as the joint full-fiber norm contributes
p^(2m).

The indicated coefficient lattices have unbounded denominators in
the fixed Tate line. This does NOT prove that the actual rational
classes cannot admit bounded representatives in a different proved
lattice; such boundedness remains unproved, exactly as the note says.
Neither system is obtained by rationalizing a finite p^k module.

An actual rational Kummer extension has endpoints Q_p and Q_p(1).
Tensoring with rho changes its quotient to rho and its subobject to
T_pi. It does not produce an extension of Q_p by T_pi. The finite
twisting construction uses the vector only after finite trivialization;
unbounded divisions would require greater absolute precision before
reduction. The text retains this distinction and makes no automatic
integral Iwasawa or full-character evaluation assertion.

## 7. Exact order of the separate higher class

The constant L_a is fixed by the predecessor's rational cube, not
selected from a required regulator. I inspected its two saved reduced
ratios. Their denominators have exactly one factor of a, and their
numerators none; the twelfth powers have valuation-12. Root separately
checked these new integer valuations. No division-polynomial or old
certificate computation was repeated in this review.

At a!=p, the ray field is unramified since its modulus is prime to a.
E has good reduction. Properness extends the rational point sections
over the local integer ring, and the inverse images under[p^m] are
finite étale there because p is invertible. The joint division field
is consequently unramified at a as well. The normalized valuation of
L_a remains-12, prime to p. Its image in M_m^*/M_m^(p^k) therefore
has exact order p^k.

The norm-root equations define an actual torsor under the p^k-torsion
of the norm-one torus. Surjectivity of the product on geometric
mu_(p^k) coordinates does not require the degree to be prime to p.
The specified common root has product L_a^(p^(4m-k)), as required.
Its forgetful image is the preceding Kummer class by Shapiro, so its
order is at least p^k and, since its coefficient module is killed by
p^k, exactly p^k.

Modulo p the constant cocycle is delta_p(L_a) times the full norm
element prod_j X_j^(p^m-1), of exact degree4(p^m-1). The translation
action fixes that norm line. The valuation proves nonzero scalar
cohomology in this line as well as nonzero image in the full relative
module. Its tame residue is-12 times the same constant norm vector.
This is an explicit obstruction to calling it an ordinary Selmer
class, rather than a hypothetical missing local condition.

For transfer the coefficient torus is the one of the global joint
division scheme over K_n; it restricts to the stated torus over F_m.
Every affine permutation fixes its full norm element. L_a is rational,
and the ray homothety has cyclotomic character1 but rho-character-1.
The actual twisted corestriction thus vanishes in that retained
coefficient module. This is compatible with the nonzero untransferred
class and does not erase its local residue by an unnamed projection.

## 8. Verdict and unresolved comparison

The construction proves its cone class, fixed-jet loss theorem,
replicated higher layer, rational norm systems in the indicated
lattices, and separate exact-order example. It does not prove
nonvanishing of the original c2,p, identify a new tensor/permutation
Selmer condition with an old one, or provide a common rational frame.
The inherited conditional identity retains epsilon_p with every
iota_p, u(0), Smith, polarization and determinant factor; the
Sha/point interpretation is used only after c2,p!=0. The target
c2,p/(2e_p det B_p), its exact real normalization, and the remaining
primitive-ray comparison are unchanged.

**PASS.** The specific open task is CM-Derived-Unsmoothing in§8.
These results neither prove nor disprove BSD over Q. No old numeric
certificate, prime scan, shared synthesis edit or new agent was used.
