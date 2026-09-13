# Independent review of the biquadratic Heegner corner

Date: 2026-09-13. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
**PASS for all seven sections. No mathematical correction requested.**
Reviewed [proof](heegner-mixed-quadratic-attack.md) SHA256:
51d6f6e481ac6c99cb96910b3734f2a1d346bf9bb49abb34bc74e1f61491ca26.
The complete [checkpoint](heegner-mixed-quadratic-checkpoint.md) was also
read. Later review-link/status edits are editorial.

The actual corner, compact mixed class and conditional primitive
gluing theorem hold in the stated scopes. The first native products
are not proved zero, and the last top class is not selected.
This verdict does not prove BSD. No old numerical script, new agent,
author-file edit or prime scan was used.

## 1. Inherited hypotheses and genuine global corner

The note retains the original odd analytic rank at least five,
good ordinary nonanomalous p≥5, the stated surjectivity/Manin range,
specified K and p-unit class number. The latter is needed for its
two independent tame characters. The clean Tamagawa and zero twist
Selmer hypotheses are added for the explicit native test classes.
Primitivity of kappa is used only for the finite cyclic dual.
The fixed A,B,d0 and full Z/p^k coefficient remain in place.

I reopened [Howard1202.6340v1, §1.7](https://arxiv.org/html/1202.6340v1#S1.SS7),
including the actual point norm, reduction relation and raw
division-cofactor cocycle in Lemma1.7.2. Those source inputs
and the already reviewed cofactor lift are used in their exact
scope. The unqualified coefficient-automorphism wording in
Theorem1.7.5 is not needed.

The group orders divisible by n make exp(x),exp(y) a genuine
quotient of the finite group ring in R[x,y]/(x³,y³).
All denominators which survive the truncation are p-units.
The axis coefficients, including the quadratic ones, vanish
by the actual opposite point norms. Thus the quotient class
in C/(xy) vanishes on the ring-class field.

The quotient is R-free. Its auxiliary action becomes trivial
on that field, whose elliptic p-torsion is zero. Consequently
inflation–restriction detects the zero quotient class and
H0 makes the preimage in J unique. This is a coefficient
exact-sequence argument about the actual Shapiro class;
no cohomological xy-divisibility is assumed.

The projections to the two cubic-linear quotients give
the previous H_i,H_j by uniqueness. With u=xy,v=x²y,
w=xy²,t=x²y², the action is
u→u+a_i v+a_j w+a_i a_j t, v→v+a_j t, w→w+a_i t.
Reflection gives precisely M,M_D,M_D,M.

Expanding the inverse-Artin point sum gives coefficient
j_i²j_j²/4 on t, the negative half-weights on v,w, and
the positive product on u. These are actual point moments
over H_ij. Integer representative changes are n-multiples.
There is no asserted global projection to that quartic point.

## 2. Mixed differential and all old local H0 terms

I recomputed the inhomogeneous cocycle equation with the
epsilon twists, rather than treating a_i as untwisted scalars.
Writing a_ij(g)=a_i(g)a_j(g), one obtains
d a_ij=-(a_i cup a_j+a_j cup a_i).
The mixed target in(4) is closed:
the two terms from dh_i,dh_j cancel those from d a_ij.
The actual class H supplies its global primitive.

At i the quotient C/J has inertia invariants x²,y,y².
Frobenius retains x²e_+,ye_-,y²e_+.
The first vector lifts invariantly. On the chosen inertia
generator exp(-x)-1, the other boundaries are exactly
(-u+v/2)e_- and(-w+t/2)e_+.
The primitive bottom singular value removes the former.
For the latter, its coefficient is minus tau_j, because
beta_i has inertia e_+. Thus its top cochain is
-tau_j a_i²e_+/2. Interchanging i,j gives the second
formula in(7). The half-square is essential.

The native point image is zero: the regular norm
coefficients through the relevant quadratic degree are
d,d(d-1)/2,d(d-1)(2d-1)/12, each zero in R.
The analogous quotient map into J is multiplication by xy,
which is Galois-equivariant and keeps the actual point origin.

For Q/Mt, the i-invariants are v,w with H0 vectors ve_-,we_-.
Only the latter has top boundary, a_i e_-.
It spans the transverse E line. This proves the full kernel(8);
it is not the finite line. The same holds at j.

Away from the two old primes, the R-split inertia quotient,
the clean Tamagawa hypothesis and the nonanomalous ordinary
plus sequence give exactly the native finite top preimage.
The odd-p quadratic inertia and real Tate scopes are retained.
These are the predecessor's actual point-image conditions,
not conditions assigned separately to the associated grades.

## 3. Self-cup compact class and exact cup homotopy

Let a=a_r, b=b_r, h=h_r and c(g)=a(g)b(g).
Here a has scalar twist epsilon, b and h have coefficient M_D,
and c has coefficient M. Direct expansion gives
dc=-(a cup b+b cup a).

Since dh=-a cup kappa and db=d kappa=0, the two terms
in U=-b cup h-c cup kappa have differentials
-b cup a cup kappa and
+(a cup b+b cup a) cup kappa.
Thus dU=(a cup b) cup kappa with the stated Weil order.
This verifies(14) without interchanging degree-one cups
by an unsupported sign rule.

At the own old place, beta=-a e_+, and
d(a²e_+/2)=a cup beta. At the opposite old place the
other tame coordinate is zero in the chosen gauge.
At the remaining clean places the finite complexes
supply the stated primitives; at p the plus-coefficient
H2 and pairings vanish. Changing finite primitives
changes only the indicated finite boundary class.

Normalizing a cohomologous b locally uses the same
cochain homotopy on gamma. A change of its normalizing
zero-cochain by a local M_D invariant changes the
primitive by a multiple of a_r e_-: exactly the
transverse E kernel above. Thus the compact class is
well-defined modulo J_top.

For the fiber differential D(c,b)=(dc,res c-db), subtracting
the compact coboundary of U gives local integrand
b cup h+(gamma+c) cup kappa. I use the DECLARED project
signed boundary/trace convention, positive on(0,+beta),
inherited from the reviewed compact-first construction.
The primary canonical triangle has the previously
recorded opposite boundary sign; it is not newly
identified with(0,+beta). Perfectness is unchanged by
that overall signed convention.

There is no need for one global cocycle representative
vanishing at both decomposition groups. Replacing the
local bottom by kappa-dq changes h to h-a cup q.
Since d(gamma+c)=-b cup a, the change of the integrand is
exactly d[(gamma+c) cup q]. This independently verifies
the local-normal-form argument in the checkpoint.

At r, the possible h top representative is transverse
and pairs trivially with beta_r. At the other old place s,
h=tau_r beta_s while b_r is finite. Its contribution is
tau_r G_sr/n=-tau_r G_rs/n. The other contributions vanish
in the finite complexes. This proves(13), with no extra
factor two in rational trace or tame inertia. The existing
K-Frobenius-square convention is already included in G.

## 4. All first corrections and the native mixed cone

The forms(16) follow because the relevant transverse twist
test groups are the actual R-lines generated by b_i,b_j.
They do not replace A,B or choose a new inverse-localization
map. The own native conditions are exactly(17).
Projection of a native Q class, which is zero at both old
places, also requires(18). If G is not a unit these are
annihilator conditions over R.

Substitution of(16) into the mixed differential gives
the two positive alpha tau self-cups and the two negative
lambda cross-cups in(19). Every coefficient and sign matches.
Under(18), a lambda cross-cup has zero old local cocycle
in the chosen finite frame, so its old primitive can be zero.

The self-cup primitive at i is alpha tau_j a_i²e_+/2.
It cancels exactly the old mixed top cochain(7); likewise at j.
There is a useful extra check on the remaining lower term:
after(17),(18), the possible lower cochain lambda_i beta_i
in the v slot is the Q-boundary of -lambda_i u e_+.
Its boundary has no extra quadratic top when the other
coordinate is zero. Thus the lambda freedom introduces
no omitted half-square term.

A global top solution differs from those specified local
primitives by precisely J_top,v. The fiber-cone exact
sequence therefore makes g(alpha,lambda)=0 equivalent
to an actual native top adjustment for these first lifts.
This proves both directions claimed after(20), including
the necessity rather than only global cup vanishing.

Repeating the explicit cup homotopy with lambda_s b_s
makes the cross compact pairings with kappa zero.
At r their finite value is killed by(18); at s the two
entries are transverse; elsewhere they are finite.
The self terms then cancel because G_ji=-G_ij.
This proves(22) without dividing alpha,tau or G.

## 5. Primary compact duality and primitive gluing

I reopened [Demarche–Harari1804.03941v3,
Theorem1.1, Proposition2.1 and the number-field discussion](https://arxiv.org/html/1804.03941v3).
They give the finite compact duality and localization sequence
for this p-inverted arithmetic open. The cup is compact first.
I also checked [Milne, Arithmetic Duality Theorems,
second edition, I.4.10](https://www.jmilne.org/math/Books/ADTnot.pdf),
for the finite Poitou–Tate annihilator statement.
No infinite-Sha duality assumption enters either application.

In the primitive case the reviewed finite Selmer result
gives R³ and surjectivity to BOTH old finite local lines.
The Poitou–Tate sequence then has zero relaxed singular
quotient: its map to the dual global Selmer is injective,
dual to that surjective old localization. Thus the
two-old-prime relaxed Selmer equals classical Selmer.
Intersecting its finite old conditions with the two
transverse conditions leaves exactly the strict group
R kappa.

Every J_top,v is self-annihilating. Quotienting H_c²
by its local boundary therefore gives a group perfectly
dual to that two-transverse Selmer group. Since the
latter is R kappa, the exact zero pairing in(22) proves
the compact class is zero. This establishes Theorem6.1:
for the specified first lifts, conditions(17),(18)
are necessary and sufficient; no further compact mixed
obstruction survives in this primitive clean subcase.

It does NOT establish the first conditions themselves.
When alpha=alpha_z all fixed cofactor data remain present.
Possible divisible Sha directions are allowed in the
already used finite Selmer structure.

## 6. Surviving top torsor and nonprimitive scope

For P=Q/Mt, the coefficient sequence
0→P→N_i direct-sum N_j→M→0
gives injectivity on H1 into the pair of first classes,
because H0(U,M)=0. Also H0(U,P)=0 by its filtration,
so H1(U,Mt)→H1(U,Q) is injective.
Thus the difference of two native mixed lifts with
fixed first classes is exactly a top E class satisfying
the conditions J_top. Its global group is R kappa
in the primitive clean case.

Multiplication by xy on the original Shapiro class
sends its actual bottom u coefficient to t kappa and
kills the other coefficients. It is an actual
point-coefficient quotient, preserves native images,
and gives the stated exact-order-n generator of that
top ambiguity. It does not select a preferred top class.

Without primitivity the compact correction is still
computed, but one pairing against kappa need not detect
its whole dual. The proof does not apply the cyclic
argument there. Nor does it express an arbitrary
nonprimitive cofactor as alpha kappa. The predecessor's
scaled integral-lift theorem and its exact defects remain.
Outside the clean range the actual top native preimage
groups are retained, without the b_i inverse simplification.

The remaining statement MQ-TP5 therefore has its correct
scope: annihilate the particular first products from
the extra complex zero, handle the nonprimitive/nonclean
compact class, and select the later top through an
arithmetic comparison. The actual quartic point moment
is not declared a complex derivative. Full BSD and its
rational leading-term comparison remain open.

