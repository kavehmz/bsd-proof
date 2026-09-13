# Independent review of the asymmetric CM ray construction

Date: 2026-09-13. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file. **PASS for all nine sections after the
recorded arithmetic tame-residue scope precision.**

Reviewed [proof](cm-asymmetric-ray-attack.md) SHA256:
7a9904d53c63062f29439b83b278ec28e0d6891b2aba08580268e815188804ed.
Reviewed [checkpoint](cm-asymmetric-ray-checkpoint.md) SHA256:
e9e93f766d5d127616abe1b4867f030941e837add3d0741f7e492016130a72e8.
Subsequent review links and completion statuses are editorial.
No mathematical correction remains.

The asymmetric norms, selected geometric class and semilocal
inverse family are constructed in their stated scope. None proves
selected-character nonvanishing at P,Q or the rational BSD frame.
No old numerical run, new agent, or author/shared proof edit occurred.

## 1. Original CM data and actual asymmetric fields

The source keeps the original tau_m=Omega_infinity/(f0 p^m).
Multiplication by pi^m therefore gives beta_m with denominator
f0 barpi^m, not a fixed tame argument.
The fixed rho is (Psi^c)^(-1), with mu_(p^k) tensor rho=T_pi/p^k.
The opposite ray B_m trivializes rho modulo p^k when m>=k;
it is not claimed to trivialize mu_(p^k) by itself.
The full field F_m does supply the earlier trivializations.

The asymmetric point-field degree follows by applying barpi^m
to the already proved full p^m Kummer torsor. That projects
onto the complete E[pi^m] direction, of order p^m.
The fixed points P,Q,P+Q are primitive in the stated CM
point lattice. The same remains true for the later
p-unit multiples n_pP,n_pQ,n_p(P+Q).

The CRT ray degrees in(8) are correct. The conductor injects
the Gaussian units, leaving one unrestricted residue-unit
factor for B_m and two for F_m. The argument that beta_m
generates B_m is also valid: fixing a primitive point with
annihilator f barp^m forces its principal generator to be
congruent to a Gaussian unit, which is the trivial ray class.
No unproved Weber-coordinate faithfulness is substituted.

These actions use the previously inspected arithmetic CM
reciprocity convention in Kato15.8. Its cohomological
inverse-character convention is dualized as in the prior
CM proofs; all present rho, period and basis factors agree.

## 2. Exact norms and the unused ray multiplicity

I reused the directly inspected primary
[Kato2004, Proposition1.3 and proof1.10](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
in the existing PDF/text cache, printed pp.121–125.
The isogeny norm has constant1, including for the noninteger
CM isogenies pi and barpi, whose degrees are prime to a.
The rational theta includes the same twelfth power.
I also reopened
[Schmitt, Acta Arith.171.1(2015), general-conductor norm formulas](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf).
No prime-power-conductor comparison theorem is imported.

Norm over the pi^m point torsor is the full pi^m fiber
and gives exactly Theta_a(beta_m+R).
For the tower, M_r intersect F_m=F_r follows from the
homothety: any common ray subextension is abelian over K,
while conjugation acts by minus1 on the Kummer translation
quotient. Odd-primary such a quotient must be zero.

There is also a direct two-step check of(9). First norm
over the E[pi^(m-r)] translations; the theta argument becomes
pi^(m-r)tau_m+R_(pi,r). Its remaining opposite-ray orbit is
the full barpi^(m-r) fiber, while the other relative ray
direction repeats each member p^(m-r) times.
The resulting argument is
tau_r+[barpi^(m-r)]R_(pi,r), with exactly that power.
This agrees with the total degree p^(3(m-r)).
The point endomorphism is not replaced by a scalar on
an unproved linear theta function.
Bezout for pi^r and barpi verifies the stated isomorphism
of the two named point torsors.

B_m is unramified at the chosen pi place, while any
nontrivial K_n/K subextension is totally ramified there.
Their intersection is K. Thus the complete transfer
retains exactly (p-1)p^(m-1-n), and its finite reduction
is zero at the stated depth. The smaller class(13) is
defined directly on the smaller field, not by division
by that nonunit.

## 3. The odd ratio and the primitive norm denominator

The decomposition beta_m=sigma_m+t_m is the coprime
tame/p-primary torsion decomposition.
The tame inverse sigma_m=[barpi^(-m)]_f tau0 is fixed
over F0, while t_m has the full primitive opposite-ray
orbit. The old homothety negates t_m and fixes sigma_m.

Every root of unity in B_m is in F0: its complex conjugate
is its inverse and belongs to the conjugate one-sided ray;
the two one-sided rays intersect in F0.
For a putative root-of-unity value of the ratio, the
displayed difference of rational functions has disjoint
pole cosets and degree at most2D_a.
The non-torsion of R makes those cosets disjoint.
The primitive orbit has (p-1)p^(m-1) distinct points, so
the strict degree inequality in(11) excludes that value.
This proves a nonzero h-odd multiplicative class.
It does not prove a nonzero full rho-selected specialization
or a nonzero finite p^k Kummer class.

For the opposite-ray step, the p conjugates are a FULL
barpi-fiber. Its norm shifts R to [barpi]R.
At the bottom, the nonprimitive subset is itself a
barpi^(m-1) fiber with tame base [barpi^-1]_f tau0.
Dividing out its norm gives exactly the denominator
in(17). This is the actual primitive-ray Euler term,
with the point endomorphism retained.

The base-change/corestriction square proves that the
cyclotomic label of the smaller class is a restriction
from K. Hence the smoothing acts by its augmentation,
and cyclotomic corestriction multiplies by p.
Neither law is an unmodified cyclotomic Iwasawa norm law.

## 4. Point jets, not normalized ray jets

The order-d jets in§5 belong to the POINT translation
group E[pi^r], which has order p^r.
For j<=d<p^r, the valuation of binom(p^r,j) is
r-v_p(j); the stated lower bound makes every such
coefficient divisible by p^k.
The inequality also ensures d<p^r.
Thus the actual point-torsor projections identify the
coefficient jets equivariantly.

The projected permutation class is p^(m-r) times the
class of the retained point-shifted function, so it
is zero when m-r>=k. Injectivity from the augmentation
kernel, using H0(K_n,T_k)=0, then gives the asserted
jet zero. A lower-level zero-augmentation class is not
needed for that injectivity argument.
No tensor/cohomology base-change shortcut is used.

An indexing question raised during review was resolved
by this distinction: point-translation order is p^r,
whereas the ray generator1+p has order p^(r-1) at F_r.
The proof now states that distinction explicitly.
There is no missing extra ray level in this POINT-jet bound.

The first factor is only E[pi^k]. The pi-isogeny Kummer
convention differs from the pi projection of the universal
p^k Kummer convention by barpi^k, as follows by composing
the two isogenies. Its tensor with T_pi has character Psi²,
and its alternating Weil contraction is zero on this
isotropic line. No opposite CM factor can be silently added.

## 5. The actual full-rho geometric class and its residues

Distinct conjugates of beta_m give disjoint translates
of E[a], because their differences have annihilator
prime to a. Faithfulness of beta_m prevents repetitions.
Thus, after geometric base change, every indicated
puncture receives exactly one summand of the corestriction.

Its raw multiplicities are12(a²-1) at the translated zero
and -12 at the other a-torsion translates.
The positive Kummer valuation residue, the fixed rho twist,
and q_(a,0,k)=12(a²-u_a) give EXACTLY(20).
For the specified a=5, or a=7 at p=5, the indicated
coefficients are units in the prime range.
The fixed primitive rho vector is retained.
A residue therefore has full order p^k, proving the
same order for the actual selected geometric class.
This is stronger than the earlier odd-ratio statement,
but still gives no nonvanishing after evaluating at P,Q.

Subtracting the value at O gives the unique relative
class. The nonzero residue prevents its proper extension.
The support identity under [barpi] follows from primitive
torsion lifting and its invertible action on E[a].
The exact degree-p norm, with the rho vector fixed at
m>=k, then proves the pointed pullback law(21).

## 6. Proper relative coefficients and the boundary-family parameter

For the proper geometric pair(E,O), relative H0 is zero.
Hochschild–Serre in total degree1 therefore identifies
the arithmetic relative H1 with the invariant geometric
Hom(E[p^k],T_k), with no base arithmetic H1 contribution.
The full residual Cartan kills the opposite-character Hom;
its pi-to-pi endomorphism line is A_k.
The p-power extension K_n cannot remove that residual
tame distinction.

The universal[p^k] torsor, with its zero-origin framing,
represents the identity homomorphism in the positive
Kummer convention. Its pi projection is therefore the
stated generator and evaluates to the point Kummer class.
The unit barpi^k for a pi^k-isogeny convention is not lost.

Curve localization injects this proper relative line into
the punctured relative group. Since the class D exists,
the fiber of its fixed residue vector is a nonempty torsor
for that line. This gives(23) without an arbitrary chosen
boundary subtraction.
Pullback by barpi acts on the generator by barpi.
Compatibility in m and in finite coefficient k consequently
leaves exactly the parameter c in Z_p in(24).
This is for the indicated fixed p/base, with the stated
restriction-compatible cyclotomic interpretation; it is
not a rational parameter common to all p.

The inverse barpi is a unit on this actual integral point
coefficient line. The origin and residue data do not select c.
In particular the result does not choose a BSD comparison
scalar merely by solving a real or p-adic equation.

## 7. Cross-smoothing with the character factor

I checked Kato1.3(2) in the same primary cache and
reconstructed the twisted transfer.
The unshifted identity is the equality of
b² Theta_a-b^*Theta_a and its a,b interchange
in additive unit notation.
At the shifted point, Frobenius of(b) sends beta to
[u_b]beta, while sending the rho vector to u_b^-1
times that vector. Invariance of corestriction therefore
contributes a factor u_b to the transferred pullback.
Evenness of Theta replaces b by u_b=±b without a constant.
This proves the operator S_b=b²-u_b[u_b]^* in(25).

On the proper point line the pullback contributes another
u_b, so S_b acts by b²-u_b²=0.
Both occurrences of u_b are required.
The scalar Kato smoothing unit is not the inverse of
this zero operator on the point component.
All pullbacks and identities can be made on the displayed
common open containing O; no undefined puncture evaluation
is needed.

## 8. The semilocal inverse family and direct global non-descent

At the chosen pi completion, barpi has unit tangent.
The formal-group inverse exists integrally and uniquely.
Its logarithm is barpi^-m log_E(R).
This is a local selector, valid for the stated formal
points; it is not a global ray-field section.

The torsion argument has nonzero tame part and an étale
opposite p-primary direction at pi. Reduction therefore
avoids E[a]. Adding a formal point preserves that reduction.
The two theta values are units and their ratio is in1+pO
in the entire semilocal unramified algebra.

In the semilocal norm the selected inverse point is a
scalar in Q_p and is fixed. The theta isogeny norm
then shifts it by barpi, giving exactly the preceding
inverse branch and proving(27).
All completions are included even when a ray step splits.
Finite Kummer transfer with the fixed rho vectors is
compatible in m and k, producing the integral local
class. The reviewed CM/nonanomalous local table makes
the entire T_pi H1 lattice finite here.
No nonvanishing of that transferred class is inferred.

For the algebraic points n_pP,n_pQ,n_p(P+Q), the p-unit
multiplier preserves full Kummer image. Since B_m contains
the opposite torsion, their inverse-division field has
degree exactly p^m: the degree remains p^m after base
change to F_m and cannot be larger beforehand.
If the theta ratio belonged to B_m, all p^m distinct
point-division conjugates would have the same value.
The degree D_a of the rational function excludes this
when p^m>D_a. This proves(29) for the actual algebraic
values and hence the nontriviality of the local family
at that depth. It does not prove the local rho transfer
or any global Selmer specialization is nonzero.

Evaluating the proper correction of(24) at the local
inverse point gives c times the fixed local Kummer class
of R: the pullback factor barpi^m cancels the actual
inverse point's unit factor.
No additivity of the nonlinear theta-value map or
global choice of c follows from this identity.

## 9. Arithmetic boundary scope and remaining comparison

The valuation formula(30) follows directly from the
unchanged rational theta expression at every finite place.
During review the author clarified that the ordinary
étale tame-residue interpretation excludes residue
characteristic p, in addition to the indicated smoothing
places. At p the separate formal/semilocal argument applies.
This scope repair changes no valuation or norm formula.

The possible global arithmetic boundary depends on
[a]([barpi^m]R+tau0). Its support is finite for each level,
but no uniform global support theorem is asserted.
This differs from the earlier fixed-argument symmetric
construction and is correctly retained.

The nonzero geometric residue, nonzero odd multiplicative
component, nontrivial local unit family and their
selected-rho specializations are distinct assertions.
The boundary family still has its actual Z_p parameter.
Its arithmetic selection, all other local conditions,
comparison with the original primitive ray coefficient
and the old Bockstein/Smith frame remain open.
No finite-Sha conclusion is used before the required
c2,p nonvanishing. Uniform nonvanishing/index control,
one rational frame and full universal BSD are not
proved by this construction.
