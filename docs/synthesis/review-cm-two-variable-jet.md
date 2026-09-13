# Independent review of the actual CM two-variable first jets

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
**PASS for the complete bounded construction in
[the proof](cm-two-variable-jet-attack.md), §§1–9.**
Reviewed mathematical revision SHA256: `e7bcdbbee667a7ebfd65797d11305cfd78e0d85ff5cacd40cbf63393024ee3f7`.
A subsequent change of the Shapiro-map label from S to Sh is editorial.
The result constructs actual integral cohomology classes and their exact
specialization; it does not establish the remaining rational BSD comparison.
No old numerical certificate was rerun.

## 1. Actual ray group, finite branch, and exact generators

Root reconstructed the ray-group count directly. For f=39(1+i)^3,
the residue-unit factors have sizes 4,8,12,12, giving phi(f)=4608.
The four Gaussian units inject modulo f. The two split p-adic factors
contribute (p-1)^2 to the finite torsion part and one principal Z_p
direction each. Thus |Delta|=1152(p-1)^2, a p-unit at every allowed
p>=5. Since the quotient by the Gaussian units involves only finite
torsion, it does not alter the two principal directions.

The characters on those directions are fixed by their values, so the
specified gamma_pi and gamma_barpi are genuine unique generators.
Root read Kato's §15.8 in the full primary cache
`/tmp/cm-derived-kato2004.pdf`, SHA256
`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`,
printed pp.256–257. His cohomological character on an Artin ideal is
psi(a)^(-1); the Tate dual gives the convention used here.
The source is [Kato, Astérisque 295 (2004), §15.8](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
The finite character is removed by log_p, so the coordinates in (6)
are integral. Since chi_cyc=Psi Psi^c, BOTH chosen generators map to
the old cyclotomic gamma. The quotient sends X,Y to T, while the
product of the two generators maps to gamma squared. There is no
factor one-half in the actual quotient map.

## 2. Finite units, coefficient twist, and unnormalized norms

Root compared (2) and (9) with the full earlier finite twisting
construction, including the fixed theta twelfth power and coefficient
vector. Schmitt's conventions index the two primes in the opposite
order from this new note; the new note explicitly fixes its first
index, and the actual points and exponents agree after that relabeling.

The actual increasing-exponent unit norms were checked in
[Schmitt, Acta Arith.171 (2015), §§2.2–3.3 and Definition3.12](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf).
No prime is being removed entirely, so no new-prime Euler factor enters.
The modulus has multiple prime factors, which is the relevant unit
condition; the paper's later prime-power-conductor comparison theorem
is not used.

At sufficiently large r,s, the actual ray fields trivialize the finite
Tate components and their twist. Corestriction therefore commutes with
the tensor by the stated invariant vector. Kummer compatibility and
the exact unit norms prove independence of r,s and compatibility in
both directions. This is also the concrete formula in
[Rubin, Euler Systems, VI.3.3 and VI.3.5](https://swc-math.github.io/aws/1999/99RubinES.pdf),
which root read directly. The construction twists before taking the
cyclotomic quotient, as required for rho=(Psi^c)^(-1).

The kernel of the ray field's action on the specified division points
has no principal-unit component: a finite Teichmüller factor cannot
cancel a nontrivial principal component modulo the corresponding
p-power. Hence that kernel is in Delta. The displayed Delta-fixed
bi-layers lie in the division fields at the claimed indices, and
transitivity factors the new ray norm through exactly the older
unit e_(r,s). No new division-field degree is introduced.

Equation (11) is the actual restriction/corestriction norm, equal to
|Delta| times the projector. The pre-twist projector has coefficients
rho(delta), as required for the rho^(-1) branch. This selects the
already established tau-odd source. Being a p-unit permits the
projector but does not authorize deleting |Delta|; the proof retains it.

## 3. Smoothing and comparison with the prior Kato class

For the rational auxiliary ideal (a), both pro-p character coordinates
are log_p(a)/log_p(1+p), since its finite CM value is +/-a. Thus the
smoothing divisor has exactly the two binomial factors in (12).
Its augmentation 12(a^2-+/-a) is a unit for a=5 at the allowed p!=5,
and the choice a=7 is a unit at p=5. The sign is Kato's, opposite
the Schmitt Coleman sign used earlier. Root checked Schmitt3.12–3.13:
the two-variable Coleman image is 12(sigma_a-Na)lambda, with lambda
independent of a. The retained identity between auxiliary units
therefore gives the stated auxiliary independence after twisting.

For balanced finite layers, corestriction to KQ_n is the same direct
corestriction of the same ray unit and coefficient as in the predecessor.
The quotient takes q_a(X,Y) to
12(a^2-u_a(1+T)^(2lambda_a)), exactly the old smoothing divisor.
The integral induced Tate module and its Shapiro map are unchanged.
This verifies the comparison for the actual class, including the tame
norm and rational Betti factor, without a surjectivity assumption on
arbitrary two-variable Iwasawa cohomology.

The previous z_infinity=T w_infinity consequently proves zero
cohomological augmentation over K. It does not prove I-divisibility
in the two-variable H^1 module; the rest of this proof correctly
keeps those assertions separate.

## 4. Corrected finite jets and exact specialization

The finite ray-generator orders are p^n,p^k. Mapping them to 1+X,1+Y
modulo p^m and (X,Y)^2 requires n,k>=m, or ray exponents at least
m+1. This bound is explicitly enforced. The inverse Galois action
then has linear coefficients -c_pi and -c_barpi.

The residual invariant group is zero because a lift of the actual
ray involution tau acts by -1 and fixes the bi-layers. No involution
inside an absolute Galois group is asserted. The coefficient sequence
(18) therefore injects H^1 of its two-coordinate submodule into the
middle H^1. Its image is precisely the kernel of augmentation,
proving the existence and uniqueness of the two first-jet classes.

Root checked the cocycle signs directly. If A=gv-v, subtracting the
DEFORMED coboundary of v changes B to B+c_pi(g)gv and D to
D+c_barpi(g)gv. Their differentials vanish. Changing the initial
cochain by a coboundary changes those corrected terms only by ordinary
coboundaries. Coefficient reduction preserves the unique extraction,
and the invariant groups vanish, so the integral inverse limit has no
lim^1 H^0 ambiguity.

The coefficient quotient X,Y to T sums these two unique derivatives
and matches the actual prior first cyclotomic jet. The old injective
coefficient sequence identifies that sum with d_m and, integrally,
with w_0 after Shapiro. Generator changes scale the coordinate classes
inversely and the quotient coordinates directly, leaving the actual
sum unchanged. Only the sum is asserted to have the established full
Selmer condition. Individual summands are not proved Selmer or nonzero.

## 5. Derived base change and its exact edge terms

The coefficient Koszul resolution on X,Y is exact, continuous and
Galois equivariant. Applying derived continuous cohomology to its
finite total complex computes the required derived tensor product;
this proves (22) without first tensoring the H^1 module as if it were
flat. Continuous Shapiro identifies the coefficient complex with the
actual inverse system. Finite cohomology of the cofinal finite layers
and coefficients gives Mittag–Leffler, and total imaginary p-cohomological
dimension two removes higher rows. H^0 is zero by the same tau action.

Root reconstructed the spectral sequence. Only rows H^1=M,H^2=N
and Tor columns 0,1,2 occur. The differential Tor_2(N,Z_p) to M/IM
is the only one altering the H^1 edge. Zero H^0 of specialization
forces it injective. The two surviving H^1 filtration terms give
exactly

    0 -> Tor_2(N,Z_p) -> M/IM -> H^1(K,T_pi)
      -> Tor_1(N,Z_p) -> 0.

The top term is N/IN=H^2(K,T_pi). Applying the one-element resolution
for X-Y similarly gives (24), retaining N[X-Y]. No flatness or
surjectivity is inferred. The displayed elementary complex with row
(X,Y) correctly demonstrates why zero specialization need not mean
I-divisibility of a module element. It is explicitly not substituted
for the actual unit construction.

## 6. The actual second-order lift and global cup identities

The full unit class lifts the first jet, so it can be represented by
an actual continuous cocycle over the completed coefficient ring.
Its constant cocycle is an integral coboundary. After subtracting a
constant lift of that coboundary, the constant term is zero. Therefore
quadratic terms of the Galois coefficient action do not enter the
quadratic cocycle equations. Comparing X^2,XY,Y^2 gives exactly

    c_pi cup d_pi = 0,
    c_barpi cup d_barpi = 0,
    c_pi cup d_barpi + c_barpi cup d_pi = 0

in ordinary global H^2. These relations depend on the actual higher
unit lift, not on an arbitrary pair of H^1 classes. They are not
identities in a Selmer cone with its additional local terms. Thus
they do not force a p-adic height or regulator to vanish, and do not
prove individual finite local conditions.

## 7. Scope and remaining arithmetic comparison

The projected scalar (26) is the unchanged predecessor identity for
the Selmer SUM, with the same p/(2#E(F_p)), factor four, Euler factor,
CM period and generator. The inverse is restricted to the stated
image where Reg_p is nonzero, with undivided identities otherwise.
The local matrix C_v is not replaced by an unproved global half-height
reference. A single rational framed element with these local and the
required real realizations remains unconstructed.

The new result is an actual two-direction integral cohomological
construction with exact specialization and higher-lift relations.
It neither proves the remaining rationality comparison nor full Sha
finiteness, and it does not prove or disprove universal BSD.
