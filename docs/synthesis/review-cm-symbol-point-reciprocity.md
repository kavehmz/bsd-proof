# Independent review of the CM symbol–point reciprocity construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file. **PASS after the recorded tower-map type
precision.** No mathematical correction remains.

The complete nine-section [proof](cm-symbol-point-reciprocity-attack.md)
and its [checkpoint](cm-symbol-point-reciprocity-checkpoint.md) were read.
The final restriction-of-scalars and p^4-power-target sentence was
inspected; it clarifies the existing norm calculation without changing it.
Reviewed mathematical proof SHA256:
6f08e8f4e1d3142436fb3bbcf1f631d4023448b9070bb36f6e1ed0924b63e22f.
Reviewed checkpoint SHA256:
3b91aeced90bdbcae6a547d26b67c997b9456f8962eafbc8de84b1b419c877ea.
Subsequent review links and completion statuses are editorial.
Only the newly displayed rational division-polynomial calculations
were independently repeated; no old certificate or prime scan was run.
Full universal BSD remains unresolved.

## 1. The ray image and the full actual point lattice

The fixed modulus f is prime to p and injects the Gaussian units.
In the kernel of the ray reduction to F0, multiplication by a unique
global unit makes the f-component equal to1. CRT then leaves two
unrestricted invertible p-components. Thus Gal(Fm/F0) really is
(O/p^m)^times, including its entire split Cartan action.
The CM reciprocity convention is the one already checked in
[Kato2004 §15.8](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
Possible simultaneous inverse Artin coordinates do not narrow that
image; the specified homothety still acts by minus identity.
The conductor condition is included in f p^m, also for tau_m.

The point-lattice proof is stronger than a rank count. At odd p the
conjugation projectors split the p-completed Mordell–Weil group,
and [i] identifies the minus part with the rational plus part.
Using the previously certified FULL rational basis therefore gives
the displayed free (O tensor Z_p)-basis P,Q. Possible index factors
from quadratic descent divide a power of2 and are invertible here.
The Cartan action rules out odd-primary torsion.

For completeness, Sah's calculation in the proof is exact:
centrality gives (h-1)z(g)=(g-1)z(h), so h-1 annihilates H1.
Here h-1=-2 is invertible on E[p^j] for j<=m.
Inflation–restriction is therefore injective on the relevant
Kummer classes even though the full ray group has a p-part.

The translation image W is stable under the Cartan because the
points P,Q are K-rational and the cocycles are global Kummer
cocycles. Its mod-p image splits by the explicitly available
Cartan operators. A missing component would give a nonzero
O/p-linear relation between P,Q whose Kummer class vanishes
after restriction to Fm; inflation and the full point lattice
exclude that relation. The image modp is therefore all E[p]^2.
Nakayama over Z/p^m gives the entire E[p^m]^2.
This uses the two character components explicitly, not a false
semisimplicity assertion about all mod-p representations.

The field is Galois over Fm because it contains the torsion
translations, and its group is the resulting cocycle image.
Changing division points by that torsion does not change the image
or the marked difference homomorphism. Projection and addition
give the three stated single-point degrees.

## 2. Exact theta distribution and the two norm powers

I directly read the cached primary Kato PDF/text, Proposition1.3
and proof1.10, printed pp.121–125. Its normalized function has
exact norm invariance, and its twelfth power is the fixed rational
Theta_a. In the uniqueness argument, the norm identities for
multiplication2 and3 force the possible constant to have both
cube and eighth power1, hence to equal1.
The isogeny degree is prime to a in every application here.

I also reopened
[Schmitt, Acta Arith.171.1(2015), §§2–3](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf).
Only its general-conductor theta construction is used.
No prime-power-conductor comparison theorem is imported.
The full finite-étale-fiber norm and the primitive ray-orbit norm
are distinguished; no missing-prime Euler factor is deleted.

Over Fm the joint translation group has order p^(4m).
Each translate in a single E[p^m] direction occurs p^(2m)
times, including for P+Q by the fibers of addition.
The product over that one torsion fiber is w_R.
This gives the exact joint norm w_R^(p^(2m)).

The tower degree is p^6, from the already proved total degrees
and compatible inclusions. The subgroup over F_(m+1) fixing P_m
and Q_m contains all E[p]^2 translations, so every p-division
point of tau_m+R_m occurs. There are p² such points, each
repeated p^4 times. Thus the tower norm is u_R,m^(p^4).
No identification of these two exponents is permitted.

For the uniform finite S-unit statement, outside the stated
bad/smoothing/denominator places the theta function is invertible
away from E[a] on the smooth model. If a division point reduced
into E[a], its p^m-multiple would force the excluded reduction
of [a](tau0+R) toO. This argument also covers residue characteristic
p; it does not require that multiplication by p be étale on the
special fiber. Properness supplies specialization of the points.
The exceptional set is finite since the three base points are
nonzero algebraic points. This controls the new units' divisors,
not BSD exceptions.

## 3. Both complete twisted transfers vanish

With k<=m the actual coefficient rho and mu_(p^k) are trivialized
over Fm. Corestriction through the joint field multiplies the
base unit Kummer class by p^(2m), hence gives zero in the full
finite coefficient group.

The single-point norm has no unused-direction power. Its result
is delta(w_R) tensor t_rho,k, with w_R in F0.
The ray homothety fixes F0 and the relevant cyclotomic layer,
while acting by minus1 on rho. Corestriction to that layer is
invariant under the homothety. Since2 is invertible, its value
is again zero. All field/character hypotheses needed for this
argument are stated, including m>=n+1.

The projection formula for an ordinary cup with a base point
preserves this zero and changes the cohomological degree.
Neither the previous smoothing unit nor a determinant/local
frame unit converts it into a nonzero derived H1 class.
The proof correctly does not conclude that the raw unit class
or all relative operations vanish.

## 4. The specified norm-root torsor and its first augmentation

Over a separable closure the norm on Res mu_(p^k) is the product
of coordinates. It is surjective even though the extension degree
is divisible by p. Its kernel is the p^k-torsion of the norm-one
torus, so the finite sequence(12) is exact.

The exact field norm is r^(p^k) with the specified
r=w_R^(p^(2m-k)). Roots of all conjugate units can be adjusted
in one coordinate to have this product. Two tuples with the SAME
product differ by the kernel, yielding the same H1 torsor class.
Thus the root data is genuine additional arithmetic structure;
it is not an arbitrary nullcochain. A different prescribed root
could change the relative class and is not silently used.

For the tower, restriction of scalars to Fm and the two field
norms produce the torsor with equations
v^(p^k)=u_R,m^(p^4) and N(v)=r_R,m,k^(p^4).
The root equality follows because [F_(m+1):Fm]=p² and
w_R lies in F0. This retains the p^4 multiplication;
it is not an unmodified norm-compatible Iwasawa system.

The first-augmentation map is independent of the origin because
the coefficient sum is zero. Translation acts trivially modulo
I², so the map is G_(Fm)-equivariant.
Multiplication by p^(m-k) identifies the quotient Hm tensor
Z/p^k with E[p^k]^2 as stated.

The cochain cancellation uses exactly the specified root.
For R=P take a root a_v in every coordinate with the same first
translation v, independent of the unused w. The total product
is (product_v a_v)^(p^(2m)), which equals the prescribed r,
since (product_v a_v)^(p^k)=w_P.
The resulting cocycle is independent of w: its first weighted
sum has factor p^(2m), and its second weighted sum uses the
zero sum of all elements of E[p^m].
For P+Q choose roots depending on v+w. At a fixed sum, both
coordinate sums vanish in the stated quotient.
Thus the first augmentation vanishes at the actual cocycle level.

The target still contains its point-translation representation
and toric Tate factor. After rho twisting its CM types are
Psi² and Psi Psi^c. It is not T_pi alone, and its zero image
does not prove that the full norm-root torsor class is zero.

## 5. The surviving cubical norm and exact new arithmetic

Translation identifies the four full p^m-fibers occurring in
the cubical ratio. Applying the exact distribution separately
to all four terms proves(17), including its descent to F0
and independence of division-point choices.
Their supports are disjoint E[a]-cosets, because a nonzero
combination among P,Q cannot be torsion. Hence the divisor
coefficient atO is12(a²-1), so the rational function is
nonconstant.

With the Neron logarithmic coordinate, x(z) has leading z^(-2)
and the odd division polynomial has leading a z^(-(a²-1)).
The regularized coefficient is therefore
(psi_a(P)psi_a(Q)/(a psi_a(P+Q)))^12.
The discriminant powers cancel. The factor a cannot be omitted.

I independently evaluated the displayed psi2, psi3 and psi4
polynomials and then their psi5/psi7 recurrences at the three
specified rational points using Python Fraction arithmetic.
All six intermediate values and both reduced signed ratios
in(19),(20) agree exactly. Both reduced numerators and
denominators have absolute value greater than1.
This was a new exact rational check, not a rerun of an old
derivative, rank, height or prime-scan certificate.

For rational r, the kernel of log_p with log_p(p)=0 consists
of r=±p^j. Removing the p-power leaves a rational root of unity,
necessarily±1. Neither reduced ratio has this form at any odd p.
The twelfth power preserves nonzero logarithms in characteristic0.
This establishes the stated uniform nonvanishing of the AUXILIARY
leading logarithms, with no implication for c2,p.

## 6. The sigma identity and all finite height corrections

I directly checked
[Mazur–Stein–Tate, equations1.1–1.3](https://wstein.org/papers/pheight/pheight.pdf),
author pagination585–622, revised2May2006.
The exact division identity for the fixed sigma gives
Theta_a=Delta^(a²-1) times sigma(Z)^(12a²)/sigma(aZ)^12.
Taking the four-term ratio proves(21).
Quasiperiod factors cancel in that ratio, and its regularization
atZ=0 reproduces the factor a in(18).

The off-diagonal point normalization(22) follows by polarization
of the previously reviewed diagonal
2 log_p(d/sigma)/(n_p² g_p). No factor2 is left over in the
off-diagonal formula. The multiplier n_p keeps every point
and its a-multiple in the required formal and bad identity
components, so the stated denominator corrections apply.

Substituting
Theta_sigma(aX,aY)=Theta_sigma(X,Y)^(a²) f_a(X,Y)
into bilinearity gives
log_p(D(aX,aY)/D(X,Y)^(a²))=log_p f_a.
Since a^12 L_a(X,Y)=f_a(X,Y)^(-12), equation(24) follows.
It is the finite-CORRECTED height component which vanishes,
not the raw rational logarithm of(19) or(20).
The operator has value12a² h(P,Q)-12h(aP,aQ)=0.
The Kato smoothing operator lives on a different coefficient
module; its previously proved unit does not invert this zero
eigenvalue on the point-height component.

## 7. Scope of the result and the remaining comparison

The construction keeps the twelfth power, actual smoothing,
unnormalized tame degree, rho twist, gamma_CM projection,
CM-to-Neron period, iota_p and Smith/determinant frame units.
It makes no finite-Sha assumption to prove the new Kummer,
norm or auxiliary-logarithm results.
The prior coefficient/index formula is invoked only after
c2,p is nonzero, in its already reviewed scope.

The complete transfer is zero; the canonical relative norm
class survives as an object but its first point augmentation
is zero; the cubical rational function survives and has a
uniformly nonzero leading logarithm, while its corrected
height component is zero. These are distinct statements.
No one of them supplies the original quadratic ray moment
or its unsmoothed point determinant.

The exact remaining task is CM-Symbol-Point: a successful
operation on the original ray branch and relative point data,
with uniform coefficient/index control and one rational frame
before separate completions. Neither c2,p nonvanishing, a
uniform BSD exception theorem, nor rationality of the desired
frame follows from the auxiliary logarithm. Bad/nonsplit primes
and the full universal objective remain open.
