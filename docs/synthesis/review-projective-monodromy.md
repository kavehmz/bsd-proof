# Independent review of the projective-monodromy construction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed [projective monodromy](projective-monodromy-attack.md), all ten
sections, against the preceding twisted-bundle proof. **PASS for the
constructions and stated obstructions.** No uniform bound or Sha vanishing
is inferred from regular connections.

## 1. Generic trivialization and the form torsor

The trace-pairing proof of the geometric decomposition is correct. For
each n-torsion degree-zero line M, stable fixed-determinant uniqueness
supplies M→End(W). Products pair only inverse characters; on each
inverse pair the trace is n times a nonzero scalar. In characteristic
zero this is a perfect fiberwise pairing, proving the rank-n²
decomposition. Pullback by [n] trivializes every summand.

Global sections and evaluation then prove a statement about algebras,
not only their Brauer classes: after geometric trivialization the
evaluation map is an isomorphism, and its algebra at O is the framed
split matrix algebra. Thus [n]*A_β is a constant split matrix algebra
over Q. Properness forces its deck-action matrices to be constant in
the elliptic coordinate. The adjoint characters exhaust all n²
characters, so the projective representation is faithful.

Its theta extension has nondegenerate commutator: a finite central lift
is semisimple, its invariant endomorphisms are scalars, and a lift of
a radical element would be scalar by Schur's lemma. The Heisenberg
matrices have the stated commutation relation. The ordinary differential
therefore descends along the actual finite étale cover. The difference
space of projective connections is zero, giving uniqueness and monodromy
order n². These statements also hold for the ordinary Brauer-zero control.

The geometric automorphism group is exactly Pic⁰(E)[n]: an algebra
automorphism is induced by a line twist of the stable bundle; its
determinant is n-torsion and stability removes the remaining scalar.
The resulting arithmetic form torsor maps to the normalized Brauer
class. Local neutralization therefore means local Kummer membership,
not triviality of the finite torsor. This distinction is preserved.

The relevant geometric scope was checked in
[Brion, 1104.0818v4, §§2.3 and 3.1](https://arxiv.org/html/1104.0818v4).
The source assumes characteristic prime to n for these assertions;
the note applies them only there or in characteristic zero.

## 2. Integral model and the characteristic-p obstruction

The ordinary stable bundle extends over Z[1/389] by generator extensions:
relative Ext¹ is a line, its generator remains nonzero in every fiber,
and the affine principal ideal base removes a global extension ambiguity.
The characteristic-free degree-one induction proves the required stability.
After also inverting n, projective automorphisms form the finite étale
n-torsion group. The local Kummer torsor is unramified and extends there.
Twisting gives the asserted model and [n] trivialization, with no extra
unspecified set of primes. Evaluation at O splits the constant algebra.

On the good abelian scheme, [n] has finite-flat degree n² and induces
multiplication by n on invariant differentials. Its relative differential
quotient is consequently (O/n)ω; it is not étale at p|n.

The stronger projective Atiyah argument is valid without stability. In
characteristic p dividing n, trace annihilates scalar matrices and hence
factors through End(W)/O. It sends the projective Atiyah obstruction to
the first Hodge Chern class of det(W), whose Serre trace is its degree.
If that degree is prime to p the obstruction is nonzero. The determinant
trace identity was checked in
[Kuhn, Example 4.10](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/atiyah-class-on-algebraic-stacks/92C44757D4DCF43E4B6F368DDC5179EC).

For any local Azumaya extension of the specified generic algebra, local
Brauer triviality and regular injectivity give End(W). Its generic
degree is 1 modulo n, since equal projective bundles differ by a line.
That degree specializes, so the obstruction excludes every such regular
projective connection at p|n, even for an unstable extension. The same
argument applies to β=0, as the control requires. It therefore cannot
be used to detect a nonzero Sha class.

## 3. Ramification at 389

The already proved 389-primary vanishing gives (n,389)=1 for the period.
Tate uniformization with valuation v(q_T)=1 makes q_T^(1/n) an
Eisenstein extension of ramification degree n. Over the maximal
unramified extension all n-th roots of unity are present, and tame
inertia gives the full transvection modulo n. Thus the torsion group
has no finite étale extension at 389. A finite-flat group of invertible
order would be étale, so does not give a replacement there.

The degree of z↦z^n on the smooth part of the I₁ fiber is n, not
the generic degree n². This rules out a finite-flat self-map of the
same proper I₁ model. Normalization in the generic cover is nevertheless
finite: excellence gives finiteness, and normal two-dimensional local
rings are Cohen–Macaulay. Over the regular target they are finite flat
by the maximal-Cohen–Macaulay criterion. Its regular resolution has
generic degree n² and splits the pulled-back Brauer class. This does
not identify the resolution as a finite étale cover or assume generic
Brauer injectivity on the unresolved singular normalization.

## 4. The degree-zero repair is an actual integral construction

For a good prime, the integral closure of Z_p in L⊗Q_p is finite free,
possibly ramified. A local point of C identifies its degree-zero Poincaré
line over that algebra A. On the smooth genus-one family, H¹(Ω)=A.
Its line-bundle Atiyah class is generically zero by degree zero and
hence zero integrally, since A is torsion-free over Z_p. This argument
uses the entire class of a line; it does not infer existence of a
vector-bundle connection from trace zero alone.

Pushforward along the finite-flat base change gives a connection by
projection formula. The Leibniz rule is in the elliptic-curve direction;
Ω_(E_A/A) is the pullback of Ω_(E_R/R). No replacement of Ω_(E_A/R)
by this sheaf, no étaleness of A/R, and no division by n is used.
Curvature is zero because the relative curve has no two-forms.
Its generic algebra is exactly End(W) under the chosen local gerbe
neutralization. Thus Proposition 8.1 is a successful local construction.

The representing interpretation was checked in
[Cais, 0909.1849v1, Theorem 1.2](https://arxiv.org/html/0909.1849v1).
The good model satisfies its hypotheses. At 389, the regular resolved
semistable model also satisfies them, but the theorem uses the dualizing
sheaf and degree zero on every geometric component. The note retains
both restrictions rather than importing the smooth formula unchanged.

## 5. Finite monodromy and the remaining arithmetic descent

A finite projective trivialization of an arbitrary degree-zero pushforward
would pull its difference lines to trivial lines under an isogeny. The
kernel of an isogeny on Pic⁰ is finite, so non-torsion differences exclude
finite projective monodromy. This is a necessary condition, not an assertion
that the particular torsor's chosen point has such differences.

The map c↦[O_C(nc−D)] is an actual n-covering. Its zero fiber T is an
E[n]-torsor of degree n². Pushing the Poincaré line from it gives rank n²
with every difference torsion, and [n] trivializes its endomorphism algebra.
The geometric representation has all characters and zero commutator.
Its weight-one character torsor is still T: in the zero-section fiber,
the geometric weight lines are indexed by T and Galois permutes them
by the torsor's affine cocycle. A rational character is equivalent to
a point of that finite torsor. Changing the target fiber by a rational
point gives a global Kummer adjustment, which is the remaining Sha question.

For a torsion point t over a finite product of good DVRs, an integral
lift to the vectorial extension has n-times equal to b in the vector
part. The unique torsion lift over the fraction fields is obtained by
subtracting b/n. Its integrality is equivalent to b=0 modulo nω,
independent of the initial integral lift. The line-connection formula
is the same calculation on the n-th tensor power of the rigidified line.
For projective connections only differences matter, with their additive
compatibility. The full A⊗A descent datum after ramified base change,
and the distinction from a crystalline stratification, remain explicit.

After ramification e at 389 the component v_L(u) modulo e on an I_e
model must also be retained. Clearing it by e is not a period-independent
bound. The reviewer accepts all these computed conditions; none has
been proved to yield an everywhere étale splitting object of uniformly
bounded degree. PM-389 and full BSD remain open within the program.
