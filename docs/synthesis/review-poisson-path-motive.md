# Independent review of the actual Poisson path motive

Date:2026-09-13. Reviewer: root/coordinator.
**PASS for all seven sections.** Reviewed
[proof](poisson-path-motive-attack.md), mathematical SHA256
`d1b1a3f3fe290c8754d63c526973f1405a9398f3353f870d81ba5bdefbeaa1c3`,
and [checkpoint](poisson-path-motive-checkpoint.md), snapshot
`6102532be7d23262bfc6ef4e48978840165e3ef4e16ecf8bd04896a7f01293dd`.
I reconstructed the labelled complex, its chain maps, chronological
shift sign, realized cofiber and finite-base averaging. No mathematical
repair was required. This is an actual source motive, not the missing
rational arithmetic BSD morphism.

## 1. Motivic category and actual maps

All parameter schemes used for the strict transfer diagrams are smooth
over Q, hence excellent and geometrically unibranch. I checked
[CD2019, Theorem16.1.4](https://deglise.perso.math.cnrs.fr/docs/2019/DM.pdf):
its hypotheses apply and its equivalence is monoidal. The same source's
14.3.4 supplies h-descent over the indicated quasi-excellent schemes,
and15.2.1 preserves constructibility under the operations actually used.
The finite strict diagrams provide the stated nullhomotopies before
passing to motives; no unenhanced-cone choice is hidden.

The reduced homological motive I_Y is the fiber of augmentation, with
no chosen basepoint. The algebraic maps pi and u give the two specified
maps after shifting. The elliptic Chow projector removes all other
homological degrees; the reduced motive of Gm gives Q(1)[1] with its
positive winding frame. Thus lambda is an actual ORDERED tensor map to
H_E,mot(1), with the same2pi i comparison as the reviewed Hodge source.
No rational MHS map is merely assumed to lift to motives.

## 2. Labelled complexes, coincidence and augmentation

Each column of the incidence matrix(2.2) has equal images under its two
geometric face maps, proving d1d2=0 already as correspondences.
For distinct endpoints the closed cover has just three pair intersections
and no triple, so proper descent gives the literal relative motive.
At coincidence the additional triple term of the literal cover has
boundary(-1,+1,-1). Omitting that term is part of the specified augmented
diagram; it gives the triangle(2.5). Projection to the LR point splits
the extra unit with coefficient+1. This is an actual split motivic line,
not an appeal only to the constant-path Betti dimension.

The uniform definition keeps the three copies labelled over all B2×Y.
Thus it does not require the singular total geometric union to satisfy
an unjustified base-change theorem at b=z. All smooth terms commute
with base change, and the finite enhanced totalization does as well.

I checked the truncation map on each incidence column. Selecting R on
faces and(LR,DR) on endpoints lands in R1[1], whose differential is
negative. Consequently LR and DR map to-b and-z on both sides.
Projection to the labelled b endpoint gives the LR corner augmentation.

For the ds wedge dt oriented triangle the boundary is Dgamma-Rgamma-Lgamma.
The face chains(gamma,-gamma,gamma) cancel it. The inner differential
on the face terms has the outer-degree sign minus, so their remaining
boundary cancels d2(-1,+1,-1). Truncation gives(gamma,+b,-z), and
augmentation gives+1. This checks the total-complex signs explicitly.
At a constant path only(-1,+1,-1) remains, consistently with the
motivic split line and both frame maps.

## 3. Shift sign and the cofiber

For unshifted degree k of a, the formula
sigma(a tensorb)=(-1)^(qk)a tensorb is a chain map
A[p] tensorB[q]->(A tensorB)[p+q]: the two differential signs on each
factor agree after using d_(A[p])=(-1)^p d_A. At p=q=-1 and k=-1,
sigma is negative on the two shifted one-cycles. Hence the EXPLICIT
minus in j_chron gives the positive ordered product cycle.

Its pairing with the two-form from eta in the first factor and xi in
the second is(int_h eta)(int_k xi), the earliest-first Chen evaluation
on(h-1)(k-1). There is no antisymmetrizer or factor2. The check agrees
with [Looijenga2403.03748v2, Example4.5](https://arxiv.org/pdf/2403.03748v2).
Truncation and augmentation kill the D0 inclusion strictly, providing
the required specified zero nullhomotopies in the motive itself.

The cofiber of(j_chron,-lambda) is therefore an actual rational motive,
with an actual bottom inclusion and top augmentation. The proof
correctly avoids identifying a motivic kernel from a Betti isomorphism
or claiming an exact sequence in an unconstructed motivic heart.

## 4. Exact realization and variation

A finite graph spine through the endpoints gives a relative CW model
of dimension2 after taking its product. The simultaneous deformation
retraction preserves the diagonal and endpoint faces. Looijenga's
connectivity theorem removes lower relative homology; the dimension
removes higher homology. Together with the actual extra coincident
unit, this gives the full augmented P2 in degreezero after shifting.
I_Y[-1] and the elliptic h1[-1] likewise have their stated degreezero
realizations. Free pi1(Y) identifies the ordered product with the
injective augmentation-square kernel. Hence realization of the
cofiber is exactly the reviewed rational MHS pushout, with its frames.

I checked [Tubach2407.02256v3, Theorem1.4](https://arxiv.org/pdf/2407.02256v3).
It supplies the Hodge realization on finite-type C-schemes with the six
operations, used here AFTER base change to C. No arithmetic category
of mixed Hodge modules over Q is presumed. The previously verified
Hain logarithmic bar comparison identifies the iterated covectors with
the geometric pair. The chronological central covector thus keeps its
exact2pi i factor and all compact-genus corrections.

The terms over the parameter scheme have locally constant Betti
realizations. Their enhanced finite cones remain locally constant in
the derived sense, and fiberwise concentration makes a local system.
Short paths and their prism homotopies identify this transport with
the augmented path variation, including the constant line at b=z.

## 5. Finite-base averaging and verdict limits

For q:B2×Y->Y, finite pushforward retains the full Artin coefficient
A=q_*1. Pulling the top back along1->A gives the diagonal top line.
The bottom K tensorA has its specified zero augmentation homotopy,
so it maps to that pullback. Pushing it out by id_K tensorTr/d is
an actual rational cofiber construction; d is retained as a denominator.
On realizations the top is surjective and bottom is injective, so both
operations stay in degreezero. Functoriality of Deligne splitting then
sends the central components to their average, exactly(6.2).

The source motive with its average top/bottom framing is therefore
constructed. Its real invariant still satisfies
q_F=-(h_av-h_av(infinity))/c_pi by the already proved analytic identity.
The infinity value remains a finite limit, not a newly asserted algebraic
tangential fiber. Neither finite-base descent nor this exact realization
turns delta into a rational morphism, removes the marked obstruction,
or proves the global point/K2/Tate comparison or BSD.

**PASS in this scope.** No old numerical test was run for this review.
