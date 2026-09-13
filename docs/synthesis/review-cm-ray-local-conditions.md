# Independent review of the CM ray-derivative local conditions

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
**PASS for all eight sections of
[the local-condition proof](cm-ray-local-conditions-attack.md).**
Reviewed mathematical revision SHA256: `39275d6deea6e97e3370e7ee1599a5001a386767e0bf89140499644b3343de34`.
No mathematical repair was needed. Later PASS/status links are editorial.
The deduction is from established local/global duality, applied to the
actual integral ray classes. It is not claimed as a historically new
general duality theorem. Full BSD remains unresolved.

## 1. The general positive-rank statement over Q

Root reconstructed the local dimension argument. At every fixed finite
extension F of Q_l, E(F) has a torsion-free open formal subgroup and
finite quotient, so its p-primary torsion is finite. Therefore
H^0(F,V_pE)=0. The principal polarization identifies V^dual(1) with V,
and local duality gives H^2(F,V)=0. Local Euler characteristics give
H^1(Q_l,V)=0 for l different from p and dimension two at Q_p.
The p-completed point group at Q_p has rank one, so the finite
Kummer space has dimension one and is its own exact annihilator.

The pertinent primary statements were checked in
[Rubin, Euler Systems, I §§4,6 and Theorem7.3](https://swc-math.github.io/aws/1999/99RubinES.pdf),
including the point-Kummer/Bloch–Kato identification and Remark6.6's
orthogonal complements; and in
[Milne, Arithmetic Duality Theorems, I.3](https://www.jmilne.org/math/Books/ADTnot.pdf).
There is no assumption that a local Weil/Tate pairing is a p-adic height.

For any actual global cohomology class z, global reciprocity pairs it
with the Kummer class of the fixed non-torsion rational point. The
finite-coefficient sum-of-invariants argument, followed by compatible
limits and rationalization, is valid. Outside a fixed finite S the
unramified pairings vanish, so no interchange of an infinite nonzero
sum with that limit is used. Every remaining rational local term
except p is zero by the local dimension calculation. The odd-p real
term is zero as well.

The local logarithm of a non-torsion rational point is nonzero. A
multiple lies in a small formal neighborhood where the logarithm is
injective; a point in the global logarithm kernel would therefore be
torsion locally, hence torsion as the same rational point globally.
Its Kummer class spans the entire one-dimensional finite local line.
Global reciprocity puts loc_p z in that line's annihilator, which is
the line itself. This proves the asserted equality of rational global
H^1 with its finite subgroup. For the reverse unramified inclusion,
outside S the representation is unramified and a local coboundary
restricts to zero on inertia; the global finite class therefore factors
through G_Q,S. The argument is specifically over Q, not over an
arbitrary number field with more local finite directions.

## 2. Integral saturation and all finite reductions

The inverse system of finite Kummer sequences has surjective maps
on E(F)/p^mE(F). Its terms are finite locally, so Mittag–Leffler
removes lim^1 and gives

    H^1(F,T_pE)/E(F)^completion = T_p H^1(F,E).

The middle inverse limit is continuous T-cohomology. For any abelian
A, a compatible element of T_p A killed by p is zero since
x_m=p x_(m+1)=0. Thus this quotient is p-torsion-free and its
rationalization embeds it in a Q_p-vector space. It follows that
the inverse image of the rational finite line is EXACTLY the
integral point-Kummer image, retaining possible local finite torsion.

Root checked that the transition in the H^1(F,E)[p^m] term is
multiplication by p, while the point-quotient transition is the ordinary
reduction. These are the maps required for the displayed inverse-limit
sequence. Reduction of the integral Kummer image is the finite Kummer
image. Consequently the actual global T-classes give classical finite
Selmer classes at every p^m. The proof does not assert this for all
finite H^1 classes, which need not have integral compatible lifts.
No logarithm or Euler factor is divided modulo p^m in this argument.

## 3. Applying Shapiro to each actual ray class

Each ray derivative already exists as an integral base-field
cohomology class. The fixed identification Ind_K^Q T_pi=T_pE
and Shapiro therefore apply separately to both derivatives, not only
to their known sum. The non-torsion point P=(3,12) is in the existing
certified basis, so the general theorem applies to both images.

The base restriction/projection formula pr_pi res Sh(d)=d is the
counit for that SAME integral identification. Point Kummer classes
remain Kummer under local restriction; the CM idempotents act on
the p-completed local point groups and preserve their images.
This verifies both split-place component assertions. Linearity gives
the difference and all integral combinations, with compatible finite
coefficients. No correction to a derivative has been chosen afterward.

## 4. Formal and unramified CM components

At the chosen prime mathfrak p, [pi] has nonunit tangent scalar and
purely inseparable degree-p reduction, while [barpi] has invertible
tangent and an étale kernel. The roles reverse at the conjugate prime.
The formal component therefore has finite local dimension one and
its entire one-dimensional H^1 is finite. The unramified component
has finite local dimension zero; its rational finite class must vanish.

The Frobenius table agrees with the previously audited dictionary:
formal D_cris eigenvalue is beta^(-1), unramified eigenvalue alpha^(-1).
In the H^1_dR(1) realization, omega has phi eigenvalue alpha^(-1)
and x omega has beta^(-1); polarization interchanges the marking
interpretation, so the formal Tate component is the latter line.
This is not a reversion to the contradictory SW reciprocal label.
The local Tate-dual invariants also vanish, as their coefficients have
no eigenvalue allowing a fixed vector in this good ordinary setting.

## 5. Anomalous torsion and actual integral zero

For the unramified lattice, the torsion in local H^1 is exactly
(V/T)^G, since V^G=0. Its identification with
(alpha-1)^(-1)Z_p/Z_p is correct in the arithmetic-Frobenius convention.
A rational zero would in general leave this finite torsion group;
the proof explicitly retains that possibility.

For this actual E39 the rational point (0,0) has order two and reduces
nontrivially at every good odd prime. Thus #E(F_p) is even. For p>=7,
Hasse gives a positive number strictly less than 2p, so p cannot divide
that even number. At p=5 the existing a_5=-2 gives eight points; root
also checked the elementary count from the five residue classes without
rerunning a certificate suite. Hence p does not divide #E(F_p) at any
allowed split prime. Since #E(F_p)=(1-alpha)(1-beta) and 1-beta is a
p-unit, alpha-1 is a p-unit as well. The possible unramified torsion
therefore vanishes, proving the stronger INTEGRAL zero and all its
finite reductions. This stronger assertion uses the actual curve,
not merely the general positive-rank theorem.

## 6. Exact Coleman coordinate, with all constants retained

Root read the local construction in
[Burns–Kurihara–Sano,1910.07404v2, Lemma6.9 and §6.3](https://arxiv.org/pdf/1910.07404),
including the delta_n formula, its trivial-character specialization,
the Coleman definition and the exponential calculation after Lemma6.14.
Only these local identities are used, not their separate global
Sha-finiteness hypotheses for determinant statements.

Substituting phi nu=beta^(-1)nu into the displayed operator gives

    delta_0=(1-alpha^(-1))/(1-beta^(-1)) nu = k_alpha^(-1)nu.

Root checked this algebra directly with alpha beta=p. The functional
[exp^* xi,delta_0]=(exp(delta_0),xi)_p is exactly the declared local
augmentation coordinate, with kernel H^1_f. The identity
loc kappa(P)=k_alpha log_omega(P) exp(delta_0) retains the original
normalization [omega,nu]=1. Applying the already proved global
reciprocity zero therefore gives precisely zero for each derivative's
Coleman obstruction, not equality only up to a p-adic unit.

The division by k_alpha log_omega(P) is in Q_p and is legitimate
because both factors are nonzero. Neither is asserted invertible
modulo p^m. Integral conclusions were proved independently by
Kummer saturation, and the unramified integral zero by nonanomalous
point counts. These distinct arguments are not conflated.

## 7. What the result does and does not supply

Both actual derivatives and their difference are now Selmer, resolving
the individual-local-condition question left in the previous two-jet
construction. The unramified split-place localizations are integrally
zero for this curve. All tame norms, two-variable smoothing, generator
choices, Tate/period factors and finite ray exponents remain unchanged.

No nonvanishing, independence, or identification with rational points
is proved. Possible Tate-module Sha directions remain. In particular,
the original projected determinant identity belongs to the SUM;
individual Selmer membership does not place each projected derivative
in the one-dimensional image of the Bockstein determinant map.
The Tor_2/Tor_1 edge, N[X-Y] term and possible failure of two-variable
I-divisibility are unaffected. The required single rational global
frame with its real BSD realization remains unconstructed.
