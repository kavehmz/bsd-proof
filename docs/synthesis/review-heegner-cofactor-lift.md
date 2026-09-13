# Independent review of the integral Heegner cofactor lift

Date: 2026-09-13. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only this review file. Review of the complete nine-section
[proof](heegner-cofactor-lift-attack.md) and
[checkpoint](heegner-cofactor-lift-checkpoint.md).

**PASS for all nine sections after the recorded §3 source/proof repair.**
Reviewed mathematical proof SHA256:
1069acaa79900311139625292de131d1e4d380f768f6d9464cd43d42c995150d.
Reviewed checkpoint SHA256:
5c05af2ae207045245f2c50eb0ae0551e445003b63655e586f3e7dc0aa7eabe7.
Subsequent review-link and completion-status edits are editorial.
No mathematical correction remains.

The initial revision333de169... used ambient-cohomology monotonicity
for Selmer-defined indices. The author replaced that step with a
direct positivity consequence of Kim's SAME structure theorem.
I inspected the saved repair and its checkpoint; the claimed
exponent bound and every later formula are preserved.

No old numerical certificate, prime scan or additional agent was used.
Full BSD remains unresolved. This verdict concerns the
displayed conditional constructions and not the open vanishing claim.

## 1. Fixed classes and the full integral Selmer defect

The original O5 scope includes odd analytic rank at least five.
The new integral defect calculation additionally retains surjectivity,
the Manin-unit condition, nonanomalous good ordinary p, and the
specified K with p-unit class number. All fixed A,B,d0 and coefficient
p^k are preserved. The clean native conditions are added only for
the later local factorization.

I checked the finite/infinite Kummer diagram directly. Globally,
H0(Q,E[p-infinity])=0 makes
H1(Q,E[p^k])→H1(Q,E[p-infinity])[p^k] an isomorphism.
At a local place its kernel need not vanish. That kernel is, however,
already included in the finite point-Kummer image. Taking the
preimage of the infinite point condition therefore recovers the
full finite point condition. This proves
Sel_(p^k)=Sigma[p^k], without deleting local torsion.

The definitions and finiteness used here agree with
[Milne, Arithmetic Duality Theorems, second edition, I.6,
Proposition6.4 and Remark6.7](https://www.jmilne.org/math/Books/ADTnot.pdf),
printed pp.75–77. In particular cofinite generation does not assert
finite Sha.

Write D=Sigma_div and F=Sigma/D. Then T_p Sigma=T_p D is free,
its image at level k is D[p^k], and Sigma[p^k]→F[p^k] is onto:
if p^k x lies in D, subtract an element of D with that p^k multiple.
This proves the canonical exact sequence(3). It uses no splitting
of Sigma. Continuous cohomology realizes the inverse-limit classes;
the finite H0 systems have the Mittag–Leffler property, so there
is no unretained lim1 obstruction. The same inverse limits retain
the point-local conditions.

Consequently delta_n(z) is exactly -d0(a delta_n(A)+b delta_n(B)).
The ordinary global Bockstein factors through this quotient; its
zero is not claimed equivalent to point-local lifting.
The change-of-A,B formula(5) is the actual difference in the full
Selmer group, not only in the two old local coordinates.

## 2. Order of kappa and the source-index precision

Nonzero kappa at index two, together with the established lower
bound s_p(E)≥3 and the rank-zero twist, forces nu=2 and s_p(E)=3.
I reopened [BCGS2312.09301v2, CorollaryA and the refined-index
definitions](https://arxiv.org/html/2312.09301v2).
Its finite coefficient compatibility is explicit in §1.1.2,
Lemma1.1.4 and the following reduction construction.

I also reopened [Kim2203.12161v7, §§2.1,2.3,3.2 and
Theorem3.3](https://arxiv.org/html/2203.12161v7).
The working hypotheses apply with N-minus=1. The plus branch,
since W(E)=-1 and nu=2, reads
a_j^+=partial^(2j+1)-partial^(2j+2).
This is the required branch for the reduced Selmer group over Q;
the initially undetermined opposite-sign summands must not be
inserted into a total-order assertion.

The audit distinction was that Kim defines partial using divisibility
in the modified Selmer group, while BCGS prints its script-M
definition in ambient H1. Equality of those individual definitions
does not follow merely from a coefficient inclusion. In particular
a general finite Selmer subgroup need not be p-saturated in its
ambient cohomology group.

The saved direct repair uses Kim's second displayed formula only
for positivity: when the corank difference is three and i=1,
partial^(2)-partial^(3)=a_3^-≥0. This suffices for
a_1^+=partial^(3)-partial^(4)≤partial^(2).
It needs no identification with ambient indices and no computation
of the undetermined initial minus exponents. I checked the exponent
index i+|r-plus-r-minus|-1=3 and both displayed formulas in the
primary source. The author now explicitly defines every M_r here
using Kim's modified-Selmer convention. This closes the issue.

For the same Selmer-defined indices, the other inequality is sound.
Reducing the actual full-coefficient Heegner class to p^k carries
any p^j divisibility to p^j divisibility of kappa. An element of
order p^s in a module killed by p^k cannot be divisible by
p^j with j>k-s. Thus partial^(2)≤k-s. The raw-to-standard
scalar -1 and degree-two descent are units.

## 3. The integral lift, primitive case and actual Prym cup

Given the exponent bound p^c F_E=0, formula(9) is sufficient to
make both p^r d0 tilde-a and p^r d0 tilde-b divisible by p^c
in Z_p. Formula(11) then reduces to exactly p^r z.
This is an integral division of proved divisible scalar lifts,
not cancellation in R or in finite cohomology.
The case of a zero finite scalar is harmless with the stated
truncated valuation and choice of its integral lift.

In the primitive case, the independent earlier Selmer theorem
gives Sel_n=R^3. Co-rank at least three then forces
Sigma=(Q_p/Z_p)^3: every additional finite summand would
add nonzero p-torsion. Thus all the FIXED A,B lift, with no
claim that the resulting rank-three lattice is Mordell–Weil.
Divisible Sha directions are correctly retained.

The predecessor's exact coefficient calculation gives
B_(i,n)(p^r z)=[epsilon_C cup w_(z,r)].
Two integral Selmer lifts of that finite target differ by n
times an integral Selmer class. Since n[epsilon_C]=0, their
cups agree. Neither this argument nor rational triviality of
epsilon_C proves that the particular cup is zero.
The actual native point-image condition remains a further condition.

## 4. The thicker quotient is a class construction, not divisibility

In R[X_i,X_j]/(X_i^3,X_j^2), exp(X_i) and exp(X_j) have
the required group orders because p≥5 and n divides those orders.
Logarithmic coordinates make reflection exactly X→-X.

The actual point norms kill every coefficient of X_j-degree zero
and the coefficient of X_j with X_i-degree zero. After restriction
to H_ij, the quotient class is therefore zero. The quotient is
R-free and its auxiliary Galois action becomes trivial there.
E(H_ij)[p]=0 follows from irreducibility and its being unramified
at p: full residual torsion would include mu_p by the Weil pairing.
Inflation–restriction thus detects that zero already globally.
The same H0 vanishing gives a UNIQUE preimage in J=(X_i X_j).

The basis u=X_i X_j, v=X_i^2 X_j has action u→u+a_i v,
v→v and reflection signs +,-. This identifies the actual extension
with N_i and its bottom with raw kappa, without division by p.

For the one-prime cubic quotient the norm and the first derivative
are zero. The latter is the previously proved index-one vanishing
under O5. Repeating the quotient/H0 argument constructs eta_i.
The logarithmic quadratic coefficient is the actual half-weighted
sum j_i(g)^2/2; changing integer representatives changes its point
by an n-multiple. No assertion that this raw point is rational
is required or made.

## 5. Exact local invariant and boundary calculation

I computed the quotient C/J directly, retaining its H0.
The inverse-Artin inertia action is multiplication by exp(-X_v),
and the chosen Frobenius gauge has a_v(F_v)=0.

At i, the inertia-invariant quotient basis is X_i^2,X_j.
The Frobenius-invariant vectors are X_i^2 e_+,X_j e_-.
The former lifts invariantly to C. The latter's connecting
cocycle on inertia is
(-u+v/2)e_-.
Its bottom is the primitive singular vector -e_-.
Thus bottom strictness kills its coefficient; no extra top
kernel survives, and loc_i H_i=0.

At j, the quotient inertia invariants are X_i,X_i^2,X_j.
Frobenius selects X_i e_-,X_i^2 e_+,X_j e_-.
Their boundaries on inertia are respectively
-u e_-,-v e_+,0.
Bottom strictness kills the first term. The remaining term
is exactly the transverse top M_D line at j, as in(21).
This checks the asserted local statement over all Z/p^k,
not only after residual reduction.

The actual local point class maps to zero in C at either old
prime: the regular inertia norm has coefficients
d,d(d-1)/2,d(d-1)(2d-1)/12 through the needed degree,
all divisible by n. This is why the preceding H0 boundary
calculation applies to the specified class.

Away from the old primes, the split inertia-coefficient sequence
propagates the unramified condition. The p-unit Tamagawa hypothesis
keeps it the point condition under the relevant unramified p-extensions.
At p, all residual auxiliary factors are trivial unramified factors;
the nonanomalous ordinary quotient still has no invariants.
This gives the needed ordinary exactness and point images.
Order-two inertia at D is exact for odd p. These are the same
native conditions as in the reviewed predecessor; no bad local
group is removed outside the stated clean range.

The one-prime calculation makes eta_i transverse at its own prime
and finite elsewhere. In the primitive case, surjectivity of the
old finite localization implies, by finite Poitou–Tate duality,
that the one-prime relaxed group equals the ordinary Selmer group.
Intersecting finite and transverse gives loc_i eta_i=0.

## 6. The other-old-prime coefficient and its sign

The crucial comparison is GLOBAL over H_i. There the i-coordinate
is trivial, so extraction of X_i^2 is equivariant. The extracted
class is the j-Shapiro class of the actual quadratic companion,
and its norm is a_j(E) Q_i^[2]. Vanishing of H0(H_i,M) makes
its preimage under the j-linear ideal unique. This fixes the
transverse coefficient which a local restriction alone would lose.

I reopened [Howard1202.6340v1, §1.7, equation(13),
Lemma1.7.2 and Proposition1.7.4](https://arxiv.org/html/1202.6340v1).
The norm, reduction congruence and raw division correction are
used directly; the unqualified global coefficient-automorphism
wording of Theorem1.7.5 is not needed.

For a finite point representative U and nV=U, put
x=(F_j^2-1)V. Cayley–Hamilton gives the exact polynomial identity
(a_j-F_j)(F_j^2-1)=(j+1)F_j-a_j.
The norm cofactor therefore has reduction (a_j-F_j)x=-F_jx.
This remains valid for the actual weighted companion because
the norm and reduction identities hold for each compatible
translated pair and extend by Z_(p)-linearity.

The raw derivative has inertia value minus that cofactor.
The inverse-Artin linear coefficient is minus the raw derivative,
so the extracted TOP value is the cofactor itself.
After the same reflection-plus projection, x for eta_i lies in
the plus finite Frobenius line. Its transverse top value is
therefore -x. With beta_j(sigma_j)=t_j^+, this yields
t_(i;j)=-a_j^+(eta_i), exactly(26).

There is no extra factor two on inertia. Restricting an
unramified rational finite class to K evaluates on F_j^2 and
doubles its rational finite coordinate. The proof keeps that
factor when it changes coordinate conventions. The reflection
action on transverse evaluation is -F_j, whereas on finite
evaluation it is F_j; this also agrees with the top odd-degree
coefficient sign.

## 7. Native correction and scope

The global tests b_i,b_j are the actual inverse-localization
classes with transverse value beta at their own prime and
finite conditions elsewhere. Their cross coefficients satisfy
G_ij+G_ji=0 by global reciprocity and the symmetric degree-one
Tate pairing.

Subtracting t_(i;j)b_j from H_i kills its j-defect. At i its
finite change is -t_(i;j)G_ij, because the original class there
was zero. The native local difference is the negative of this
change in the specified compact-FIRST convention.
Thus R_i(kappa)=t_(i;j)G_ij=-a_j^+(eta_i)G_ij.

Only when kappa is primitive is the strict group proved cyclic
with generator kappa. In that case the fixed z has its unique
alpha_z and (29) follows by linearity. The unit detecting
coordinate justifies that coefficient; d0,D,a,b,A,B are retained.
For a nonprimitive kappa the proof does not apply this cyclic
formula to arbitrary z. Nor does it erase nonclean local groups.

The extra complex zero has not been shown to kill this particular
product or its canonical Prym cup. The constructed eta_i is not
identified with a complex derivative or a rational point.
The further mixed/top selection and universal BSD comparison
remain open.
