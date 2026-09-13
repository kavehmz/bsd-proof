# Independent review of the global CM selector

Date: 2026-09-13. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
**PASS for all ten sections after the two scope precisions recorded
below.** I inspected the stable complete
[proof](cm-global-selector-attack.md), SHA256
f1780e7f9f279faf0ac8e0661fee6370a94cceab07705dd028142c6017f57eef,
and [checkpoint](cm-global-selector-checkpoint.md), SHA256
b8ef7d00406d1fd8110df6d1224e0a01de8e76ef0f3f99971e62f312014062ac.
The first complete ten-section revision reviewed was7409731134....
No numerical certificate, point multiplication or prime scan was rerun.

The two repairs were precise wording/scope changes, with no formula
change: augmentation is itself a nonzero equivariant map, although
every scalar map from the full permutation module kills its
augmentation ideal; and tame unit residues are first calculated over
the actual source where rho is trivial, retaining any ramified
coefficient/transfer map at the base.

The verdict is about the actual global finite coefficient classes
and their local detector. It is not a global Selmer theorem, a
nonvanishing theorem for the old cyclotomic c_(2,p), or BSD.

## 1. Primary inputs and actual arithmetic fields

The full point lattice and Kummer image are inherited from the
[reviewed CM source](review-cm-symbol-point-reciprocity.md) and
[asymmetric ray audit](review-cm-asymmetric-ray.md).
The specified R=n_pP,n_pQ,n_p(P+Q) remains primitive in the required
opposite CM point lattice: n_p is a p-unit and P,Q are the fixed
basis. No assertion for an arbitrary unsaturated point is needed.

Over F_m the projected full Kummer image has order p^m. Since
B_m already contains E[barpi^m] and the geometric torsor has exactly
p^m points, this proves [B_m(S_m):B_m]=p^m, with its full translation
group. The torsor is K-defined, so adjoining one point and its torsion
over the Galois ray field also gives a Galois field over K.

For M_r intersect B_m, the quotient of the translation group would
be abelian over K. An actual opposite Cartan element acts by -1
on that group, while preserving the tame ray modulus. In an abelian
intersection quotient it must act trivially. Multiplication by2
therefore kills the quotient, which is zero at odd p. This verifies
the intersection and [M_m:M_r]=p^(2(m-r)).

The isogeny[barpi] is finite etale on the good model at pi: its
differential is a unit and it is the ordinary etale direction.
Pulling back by the integral R section proves that the WHOLE point
torsor, not merely its chosen local point, is unramified there.
Together with B_m this proves M_m is unramified at pi.
The extra pi-ray factor is the full inertia group of F_m/B_m,
so its total ramification gives M_m intersect F_m=B_m.
The same unramified/total-ramification argument gives
M_m intersect K_n=K. No global formal section follows from this.

## 2. Full point norm, augmentation and the actual finite class

I reopened the cached primary [Kato2004, Proposition1.3 and
proof1.10](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
printed pp.121–125. The isogeny norm is exactly normalized, with
constant1. Its applicability is to an isogeny of degree prime to
the smoothing integer, which holds here. The original twelfth
theta power and q_a are retained. The primitive opposite-ray
denominator is not replaced by a full-fiber norm.

The translations of S_m cover the full barpi^m fiber exactly once.
Applying [barpi^m] to beta_m+S_m gives tau_0+R. The numerator of
the point norm is therefore Theta_a(tau_0+R); its fixed denominator
occurs p^m times. This proves(8) with its actual multiplicity.

Finite etale Shapiro identifies the unit class with cohomology in
the permutation module. Tensoring by the prescribed rho vector is
justified at finite level m>=k, where it is invariant, and the
displayed unnormalized corestriction constructs A_(R,m,k).
No invariant rational rho vector or rational motivic extension
is invented in this step.

For augmentation the denominator term is killed by p^m in A_k.
The numerator is defined over F_0. The opposite-ray element fixed
on F_0 acts on its Kummer class trivially and on t_rho by -1.
Corestriction is invariant under this source automorphism; hence
the transferred numerator is killed by2 and is zero. This proves
the augmentation vanishing without p-division.

The coefficient exact sequence then yields the UNIQUE eta:
H0(K,T_k)=0, for instance by the nontrivial cyclotomic Teichmuller
inertia at pi. Tensoring these R-modules by T_k is exact because
T_k is rank-one free over R. Neither a cohomological saturation
claim nor an omitted Tor term is being used.

The full F_m transfer has exactly the extra degree
(p-1)p^(m-1-n) after base change to B_mK_n. Restriction/corestriction
therefore gives(12), and the same factor for eta by injectivity.
The smaller class is directly defined, never obtained by dividing
the zero full-transfer class by this generally nonunit factor.

## 3. Norm, pullback, replication and the two tower operations

For delta=m-r, the extension M_m/M_r has degree p^(2delta), but
beta_m+S_m runs through a fiber of size p^delta. Its arguments have
multiplicity p^delta. More explicitly, norm first over
M_m/(B_m M_r): this gives
Theta_a(beta_r+S_r)/Theta_a(beta_m)^(p^delta).
The remaining ray norm fixes the numerator and norms the base
theta to Theta_a(beta_r), yielding precisely f_r^(p^delta).
The coefficient pushforward consequently gives p^delta A_r.
Since r>=k, rho is fixed over B_r; no additional character occurs
inside this norm.

The stronger formula(14a) also checks. Pullback of the original
origin-reduced class D_(m,k) to the actual torsor subtracts exactly
its O value, giving the ratio f_m. The point lands in its stated
punctured open because a non-torsion division point cannot meet
those torsion translates. Finite etale base change and Shapiro
then identify this pullback with A_m.

The pointed isogeny law for D_m makes this pullback the restriction
of the lower-level torsor class. Under Shapiro, restriction is the
map sending a root to the sum of its lifts. Thus A_m=j_(r,m)A_r,
and eta has the same law. Projection followed by replication has
degree p^delta, agreeing with(14). This is an actual compatible
family of coefficient maps, not independent selection at each level.

For these finite-cochain statements I directly inspected
[Nekovar, Selmer complexes, Proposition3.4.2 and §8.1](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
printed p.83 and pp.189–199, in the cached primary PDF/text.
Sections8.1.2,8.1.5–6 give restriction versus replication and
corestriction versus coefficient projection; §8.1.7 retains all
semilocal components. The hypotheses here are finite discrete
modules, so no Iwasawa control conjecture is needed.

## 4. Exact local selector and genuine global nonzero classes

The unique formal inverse S_m^0(R) is a Qp point, so coefficient
evaluation at that root is a genuine LOCAL equivariant map.
Every root is S_m^0(R)+T with T in E[barpi^m], already present in
each completion of B_m. The point extension therefore splits there.

Localizing global corestriction uses every semilocal double coset.
After a coset sends beta_m to g beta_m and transports the point
coordinate back to S_m^0(R), its unit is exactly(17).
The coefficient transport supplies ONE rho factor. Combining
coset transports with their local traces is precisely the
full semilocal formula checked in
[the core local review](review-cm-local-point-comparison.md).
There is no point-degree factor and no single-completion replacement.
The point-fiber pushforward sums all lifts; this local evaluation
selects only the unique formal lift. Their different tower laws
therefore present no conflict.

The exact matched Omega_j and q_a give the old local class U_pi(R).
Modulo p^k of the integral point-Kummer lattice corresponds to
modulo p^(k+1) of its logarithm in pZp. The repaired finite flat
comparison in the core review is used here; rank-one dimension
is not substituted for it.

I read the independently completed
[Taylor certificate audit, §§7–8](review-cm-local-taylor-certificate.md).
It proves that one fixed R_* in {64P,64Q} has local logarithm
valuation2, hence local lattice valuation1, while both have at
least that valuation. The same U_pi(R_*) is selected at every
m>=2. Its finite local value has order5 modulo25, which proves
the corresponding GLOBAL eta is nonzero for every such m.
The global order is only bounded below by5. The optional cyclotomic
base-change sentence is not used for this corollary.

## 5. Fixed jets and unique growing-depth lifts

The augmentation powers are intrinsic to the torsor: changing
origin multiplies by a group unit, and the affine Galois action
preserves the filtration. With compatible coordinates, the actual
point projection maps sigma_m to sigma_r.

For 1<=j<p^r,
v_p binom(p^r,j)=r-v_p(j). Under(19), the relation
(1+X)^(p^r)-1 is zero through degree d modulo p^k and d<p^r.
The jets at r and m are therefore genuinely identified by the
equivariant projection. Its cohomological factor p^(m-r) kills
the stated fixed jet. These are point groups of order p^r;
the argument does not misindex the 1+p ray generator.

Inertia at pi fixes the entire permutation coefficient module
and all its subquotients. An inertia element acts by -1 on T_k,
so every such tensor quotient has H0=0, even when the quotient
is not R-free. The long exact sequence consequently proves the
UNIQUE lift to the higher augmentation layer. No freeness of the
associated graded or derived base-change shortcut is assumed.

For k=2,p=5, r=m-2 and d=5^(m-3)-1 satisfy those exact inequalities
for m>=4. The same nonzero eta therefore has its unique nonzero
lift in I^(5^(m-3)). This does not prove its next graded image
nonzero. Direct coefficient evaluation of (sigma-1)^j for j<p^m
gives (-1)^j, confirming that this actual detector does not factor
through a fixed jet.

## 6. Origin correction and the opposite tensor factor

Since the augmented cocycle is dv and H0(K,T_k)=0, its primitive
v is unique; an element acting by -1 gives v=-e(h)/2.
Subtracting d(v[S_m]) is therefore the actual augmentation-kernel
cocycle. Its first moment is

    A_1(g)-kappa_(barpi^k)(R)(g) tensor g(v).

This follows from g[S_m]-[S_m] and has the stated minus sign.
It is the positive affine point-torsor action, not the inverse
Artin convention used in the separate Heegner construction.

The map from barpi^m torsion to the first finite moment is
[barpi^(m-k)]. Thus the cocycle is that of the actual barpi^k
division of R. If [p^k]D=R, the division point [pi^k]D gives
(24), retaining the unit [pi^k] on the opposite torsion line.
For the indicated ordered Weil pairing its adjoint is
[barpi^k], giving the stated alpha^k in the selected pi frame.

The Weil contraction remains in H1(mu_(p^k)); it is not an H2 cup
or an H1(T_pi) class. Its eventual zero follows from the proved
first-jet vanishing. The corrected scalar-map sentence now states
the exact valid conclusion: full permutation scalar maps are
multiples of augmentation and therefore kill I. It does not deny
the nonzero augmentation map or classify all subquotient maps.

## 7. Actual common-c corrections and norm-vector depth

The proper point class K_pi used in the predecessor is the pi
projection of the universal [p^k] Kummer class, in the same frame
as the local kappa_pi coordinate. Pulling back by S with
[barpi^m]S=R gives
alpha^m kappa_pi(S)=res kappa_pi(R). Under Shapiro, restriction
of the latter constant class is exactly the norm-vector map.
Thus the actual correction is c N_Y kappa_pi(R), with the
alpha^m canceled by a proved naturality identity, not by dropping
an unexplained unit.

For m>=k, aug N_Y=p^m=0 in A_k, so the correction belongs to the
augmentation ideal. Its equality there follows by the already
proved H1 injection. Replication sends N_r to N_m and projection
sends N_m to p^(m-r)N_r, proving compatibility of the corrections.
Local evaluation satisfies ev N_Y=1, hence gives exactly
U_pi(R)-c kappa_pi(R).

The norm polynomial has coefficients binom(p^m,j+1).
The first nonzero coefficient modulo p^k is at
j=p^(m-k+1)-1 and has valuation k-1. All lower coefficients vanish.
The actual cyclic group relation has no nonzero term through that
degree, so the surviving coefficient cannot be removed in the
quotient by the next augmentation power. This proves the exact
depth(26) in the finite group ring. No nonunit norm vector is divided.

## 8. The common-c quotient and every factor of5

Put x=log_E(64P), y=log_E(64Q). The completed point check gives
v5(x)=v5(y)=1 and v5(x+y)=2, so v5(x-y)=1 as well.
The finite coordinate L_2=Log_omega/5 is defined modulo25
because Log_omega is defined modulo125. Thus a=x/5 and b=y/5
are units modulo25 determined solely by the fixed points.

The displayed covector on the direct sum of global coefficient
groups is therefore an actual homomorphism into Z/25. It kills
every common-c correction because its local point vector is
c(a,b). On the original pair, elementary substitution gives

    b(F_a(x)/5)-a(F_a(y)/5)
                =(yF_a(x)-xF_a(y))/25 mod25.

The division by25 in this last expression is justified by its
preceding product of two integral coordinates. It is not division
by a nonunit of a finite cohomology class.

The linear term cancels exactly. The quadratic term in the numerator
is (C_2/2)xy(x-y), of valuation3 because the independently certified
C_2 is a5-unit. Every term of degree d>=3 has valuation at least
d+1-v5(d!)>=4. Convergence and the integral coefficient bounds
retain this estimate for the whole tail. The quotient therefore
has valuation exactly1 and a nonzero order5 value modulo25.

This proves nonzero global cohomology modulo the entire common-c
line, not merely failure of a scalar picked after evaluation.
For every c at least one of the two corrected global classes
remains nonzero. For m>=4 their correction vectors belong to the
stated deep layer since 5^(m-1)-1>=5^(m-3); uniqueness of the deep
lift then carries the same conclusion there. The detector has
order5, but no assertion that the global quotient class has
exactly that order is needed.

The coefficients of this covector are local point coordinates.
No rational motivic covector or BSD determinant has been inferred.

## 9. Arithmetic boundaries and final scope

The discriminant factors cancel in the actual ratio, leaving the
displayed exact valuation difference with its factor -12 at every
finite place. I inspected the correction clarifying that ordinary
unit-Kummer residues are first computed on the rho-trivial source.
Any ramification of the transported coefficient at the base keeps
its actual residue/transfer map. At p the local cohomology
comparison, not an etale tame valuation formula, is used.
The opposite place has no asserted fixed formal inverse.
No uniform arithmetic support in m is claimed.

The primitive ray denominator, original rho/q, Betti projection,
matched local period, and old determinant/Euler frames remain
explicit. The extension class with permutation coefficients is
not assigned the scalar value of the original ray derivatives.
The full permutation selector obstruction is correctly limited to
that class of coefficient morphisms.

All ten sections pass within their stated hypotheses. The new
positive conclusions are actual nonzero global finite coefficient
classes, unique nonzero growing-layer lifts, and a nonzero quotient
after every allowed common-c proper-point correction. They do not
establish ordinary global Selmer conditions, original cyclotomic
c_(2,p) nonvanishing, a rational BSD frame, or full BSD.
