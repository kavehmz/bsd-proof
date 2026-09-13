# Independent review of the global tame nullhomotopy construction

Date: 2026-09-12. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. Own only this review file.

**PASS after inspecting the two explicit convention precisions.**
All eight sections of the [proof](heegner-tame-nullhomotopy-attack.md)
and the [checkpoint](heegner-tame-nullhomotopy-checkpoint.md) were read.
Reviewed mathematical proof SHA256:
90b0925736532683e8ee1ab03b6b5fc155b3b2ddb9f9844c14a47a14e0e3b713.
Reviewed checkpoint SHA256:
13046322fc1e65dadb54a7789965f6bed77c8fa903461d8620dff8ba49532e5c.
Subsequent PASS links and completed-status changes are editorial.

The actual first global cup classes are annihilated by the full
rank-zero twist factor in the stated additional surjective range.
The proof retains a separate native-local obstruction and an actual
top Heegner ambiguity. It does not prove rank-five vanishing, erase
a nonunit, or establish the full BSD objective.

## 1. Fixed arithmetic scope and primary valuation input

The input is the actual cofactor-corrected class x, strictly zero
at BOTH old primes, and z=d0 x. The earlier Kato and BDV identities,
their period/Euler factors, the full common coefficient p^k and
the raw-to-standard sign remain unchanged. The extra p not dividing
h_K is retained for constructing the two independent tame characters;
no assertion that every auxiliary twist satisfies it is made.

I directly read
[Castella–Sano2601.14504v1, §§1.1.1–1.1.4](https://arxiv.org/html/2601.14504v1).
The theorem requires p>3, surjective residual image and a p-unit
Manin constant. Its ordinary case has no squarefree-conductor
hypothesis. The rank-zero display identifies the Sha valuation
with the normalized L-value valuation minus M_infinity, and
Theorem B identifies that last term with the Tamagawa valuation.
The normalization there uses the full real Neron period.
Thus its application to the twist gives equation(6), with
nonsquarefree conductor ND² allowed. This is an exact consequence
of the cited theorem in the stated range, not a BSD assumption.

The surjectivity transfer to the twist checks: the quadratic field
ramifies at a prime outside Np, where the residual torsion field
is unramified. Their intersection is therefore Q. The untwisted
matrix and the quadratic sign can be prescribed independently,
so twisting preserves the full matrix image. Surjectivity also
excludes CM in this range, as required by the cited setup.
There is no p-isogeny under the irreducibility hypothesis;
passing to the optimal curve changes the relevant integral
structures only by p-units. The cited Manin condition at the
good prime is therefore available.

Nonanomalous reduction makes 1-alpha^(-1) a unit. The full real
period versus a plus-cycle period differs only by 1 or 2, so
its valuation is unchanged at p>=5. This establishes
d0=u_D p^(t+s); it does not replace d0 by that power in the
underlying identity without its actual unit.

At N the quadratic twist is locally trivial. At D the original
curve is good and its ramified quadratic twist is additive;
the component group has order at most 4. Hence no new p>=5
Tamagawa valuation comes from D. Rank zero and irreducibility
make Sel_(p^k)(E^D)=Sha(E^D)[p^k], whose order is at most p^s.
All these uses concern the rank-zero twist, not unknown Sha(E).

## 2. Unramified norm and the actual local annihilation

Lemma3.1 is valid even when the unramified degree is divisible
by the residue characteristic. On the connected special fiber,
N_n=1+F+...+F^(n-1) has finite kernel because
(F-1)N_n=F^n-1. A homomorphism of the connected smooth group
with finite kernel is surjective. If N_nQ=P with FP=P,
then F^nQ=Q, so the preimage is rational over the required
residue extension. Formal-group norm on each successive
filtration quotient is the residue-field trace. That trace
is surjective for a finite separable finite-field extension,
including degree divisible by its characteristic.
Successive corrections converge in the complete formal group.

At a bad prime, the point class is considered modulo p^k.
The prime-to-p part of its component-group image can be changed
by a p^k multiple; multiplication by p^t kills its remaining
p-primary component. It then has an E0 representative and the
preceding norm theorem supplies a point preimage. This constructs
the lift through the actual regular Shapiro module and then its
specified quotient N_i. Its connecting class is a_i cup x, with
the action in(11), and so the claimed local annihilation follows.

The other local cases in Proposition3.2 also check. The strict
input kills the old-prime terms. At p, nonanomalous reduction and
local duality give H²=0. At primes of D, quadratic inertia acts
as -1 on the otherwise unramified elliptic coefficient, giving
H⁰=H²=0. At remaining good places unramified cups factor through
a residue group of cohomological dimension one. Odd coefficients
remove the real Tate term. Quadratic restriction is injective
on p-primary groups because its corestriction composite is 2.

When local Shapiro decomposes into several places, a chosen norm
preimage in one summand suffices. The proof correctly avoids an
extra multiplicity from a diagonal choice of points. It does not
claim that norm is surjective on arbitrary component groups.

## 3. Finite Poitou–Tate and genuine finite cochains

I checked
[Demarche–Harari1804.03941v3, Theorem1.1, Proposition2.1 and §5](https://arxiv.org/html/1804.03941v3)
and
[Milne, Arithmetic Duality Theorems, second edition](https://www.jmilne.org/math/Books/ADTnot.pdf),
I.4.10(a)–(c), the finite-kernel sequence in I.5,
and II.2.9. These apply to the finite etale p-power
coefficients on the stated affine U, with p inverted.
Milne II.2.9 explicitly supplies the Galois/etale comparison
in all degrees here. I.4.10(c) supplies the odd-p vanishing
of global degree three. No unproved higher K(pi,1) assertion
is needed to justify the finite Galois cochain calculations.

Here is the finite annihilator argument independently.
The kernel of global H² localization is dual to the kernel
of H¹ localization for the Cartier-dual coefficient.
The Weil pairing identifies that coefficient with M_D.
An S-strict twist class is finite outside S because the
curve is good there and the coefficient is unramified.
It is zero, hence finite, at every place of S.
It is consequently a subgroup of the actual classical
twist Selmer group, of order at most p^s.
Thus p^s annihilates the entire dual H² kernel.
Applying this only AFTER the local p^t calculation gives
p^(t+s)(a_i cup x)=0 at the full coefficient p^k.

This proves Theorem3.3 and, with the actual unit u_D,
the nullcochain equation for z=d0 x. No conclusion that
all H² vanishes is made. In particular its full old
local terms can have order p^k.

Continuous cochains with finite coefficients factor through
a finite quotient after the action has been included in that
quotient. A continuous primitive therefore appears in one
finite refinement of the input quotient. The proposed search
over such finite data is an existence construction with
finite linear equations, not a stated efficient algorithm
or a canonical choice. If v_p(d0)>=k, it legitimately gives
the zero scaled input and cannot recover an unscaled class.

## 4. Native point image and the permitted correction groups

At the ramified old prime the regular inertia invariants are
norm elements. Their image in the first jet is
p^e+p^e(p^e-1)Y/2, which is exactly zero modulo p^k because
e>=k and 2 is invertible. Point Kummer is unramified there
over the extension because E has good reduction.
This proves the ZERO native point image in H¹(N_i).

The kernel from H¹(M_D) into H¹(N_i) is different.
By the coefficient long exact sequence it is the boundary
of H⁰(M). The latter is the plus Frobenius line at an old
prime. The actual inverse Artin coordinate sends it to
a primitive tame class, spanning the transverse line in
the twist. Restriction kills that class in F_i. It is
injective on the finite line because the ramified p-part
does not multiply residue Frobenius and the residual
quadratic degree is the unit 2. This checks(13).

Away from p,D,i in the clean Tamagawa range, finite Kummer
is unramified also over the relevant unramified extensions.
The author added the requested precision: the R-splitting
of the auxiliary coefficient quotient is inertia-equivariant
because inertia acts trivially on that auxiliary factor.
This does not say inertia acts trivially on M.
Tensoring with M and then taking inertia invariants is
therefore exact, and Frobenius coinvariants are right exact.
The native image is the unramified image. The same split
inertia sequence shows its preimage on M_D is unramified.

At D the twist H¹ is zero by local Euler characteristic
and the vanishing of H⁰,H². At p, all residual simple
factors of the unramified auxiliary p-group module are
trivial; tensoring them with the ordinary quotient keeps
its eigenvalue different from 1. The dual H⁰ vanishing
makes the plus-kernel H² vanish and gives the needed
surjectivity on H¹ of plus parts. With nonanomalous
reduction the finite point condition is exactly this
ordinary-plus image. This checks the p clause of(16).
Outside the clean range, the proof retains the actual
groups J_i,v defined by preimages, rather than extending
the clean formula across component defects.

## 5. Signed compact pairing and the remaining group

The current authoritative
[Gysin convention](heegner-gysin-bridge.md) and
[defect duality convention](heegner-defect-duality.md)
are explicitly COMPACT-FIRST:
P(b,c)=tr_c(c cup b), using
e_(p^k)(compact coefficient, ordinary coefficient).
The final tame proof now says this explicitly at(18).
There is no sign reversal to make from the current files.

For the fiber differential
D(c,tau)=(dc,res c-d tau), the pair
c_i=(-a_i cup z,tau_i,v) is closed by its defining local
equations. Changing a native local lift changes tau by
a cocycle in exactly J_i,v, modulo a local coboundary.
A zero class modulo partial^+J is equivalent, by writing
D(t,b), to a global primitive whose local class is native.
This is precisely the additional compatibility that the
ordinary global equation does not ensure.

The compact-first cup is
((-a_i cup z) cup b, tau_i,v cup b_v).
A global u with du=(-a_i cup z) cup b exists by the
verified degree-three vanishing. Subtracting D(u,0)
leaves (0,tau_i,v cup b_v-u_v). The signed trace is
positive on this chosen partial^+ boundary, giving
EXACTLY(18). Changing u adds a global degree-two
class, whose summed local invariant is zero.

Finite compact duality identifies the quotient by
partial^+J with the dual of the FULL group satisfying
the perpendicular local conditions. When one restricts
to the ordinary-H²-zero part, its dual is the image
of localization of that group, or equivalently its
quotient by the S-strict kernel. The proof explicitly
retains this distinction in(19).

For Proposition5.2, zero classical twist Selmer makes
the relaxed singular localization at i an isomorphism
onto R by finite Poitou–Tate. Its full local image is
a rank-one graph over the transverse line. Weil cup
on degree-one classes is symmetric: the cohomological
interchange sign and the alternating coefficient sign
cancel. The finite and transverse axes are isotropic
and pair by a unit. A graph of slope c thus has
self-pairing 2c times a unit. Global reciprocity forces
this to vanish, and p odd forces c=0. The relaxed
group is therefore already the transverse Selmer
group and is R at FULL coefficients.

This proves an actual remaining group, not a nonzero
value of the particular obstruction. Conversely it
prevents an inference that a zero classical twist
Selmer group automatically removes the native test.

## 6. Mixed choices, old-prime constraints and actual top ambiguity

I rederived closure and all signs in(20)–(23). The identity
d a_lq=-(a_l cup a_q+a_q cup a_l) cancels the first two
differentials when d t_i=-a_i cup z. Replacing t_i by
t_i+h_i changes the mixed class by exactly
-a_l cup h_q-a_q cup h_l. For coboundaries h_i=d b_i,
this difference is the boundary of
a_l cup b_q+a_q cup b_l.
If z changes by d r, the compatible changes are
t_i plus a_i cup r and mixed primitive plus a_lq cup r.
Thus(22) is the correct global obstruction coset.

Native compatibility permits only changes with local
classes in J_i,v. The suggested Kato-twist corrections
are actual cocycles, but their coefficients are the
actual finite old-prime localizations and need not
be units. At p that class is relaxed; the local condition
on lambda_i loc_p is retained without scalar cancellation.
At its ramified old prime, finite and transverse lines
intersect trivially, so its allowed correction requires
the specified finite value to vanish after multiplication.
The Q/K factor two is unchanged and does not affect
the coefficient-one tame inertia coordinate.

Finally the already constructed full Shapiro Heegner
point class has only its mixed coefficient. Adding it
preserves every lower coefficient and, when achieved,
the native local point conditions. Its top coefficient
changes by the actual kappa_raw, with the injectivity
provided by the no-p-torsion hypothesis retained.
This is an arithmetic ambiguity, not a formal unrelated
power-series example.

Consequently solving the global first equations, or even
the compatible mixed equations, would still require an
additional comparison selecting the actual top lift.
No equation here uses the extra complex third-derivative
vanishing to prove that selection or its Heegner
coefficient zero. TN-TP5, and full BSD, remain open.

No old numerical script or certificate was rerun.
Only this assigned review file was written in the review.
