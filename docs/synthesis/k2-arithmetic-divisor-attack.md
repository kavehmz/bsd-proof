# The actual noncentral divisor on the regular arithmetic model

Date: 2026-09-12. Owner: coordinator. Status: completed; all [NEW] deductions passed
[independent adversarial review](review-k2-arithmetic-divisor.md), including
the local-at-389 comparison and integral denominator construction. Full BSD over Q remains neither proved nor disproved.

## 1. The fixed class and the integral theory used here

Let E=389a1 and let the actual regular proper flat model be

$$\mathcal X:\quad Y^2Z+YZ^2=X^3+X^2Z-2XZ^2
                         \subset\mathbb P^2_{\mathbb Z}.$$

Its regularity and all fibers were proved in
[the model construction](weil-etale-lattice-attack.md), independently
checked by [its review](review-weil-etale-lattice.md). All fibers are
geometrically integral and reduced. The only nonsmooth fiber is a
split nodal cubic at N=389. No geometric property is inferred from
an approximate point count or from finite Sha.

The [integrated spectral construction](integrated-spectral-comparison-attack.md)
and its review construct the fixed rational class

$$\beta_2\in H^2_M(E,\mathbb Q(2))
             =K_2^{(2)}(E),\qquad
\mathscr R_E(\beta_2)=\frac{L(E,2)}\pi.\tag{1.1}$$

Here the right K-group notation denotes the rational Adams weight-two
part, equivalently the rational unramified Milnor-symbol group in
this degree. It is not an assertion that the entire Quillen K_2 has
only one weight. The real regulator uses the fixed negative-conjugation
cycle b on E, exactly as in that construction.

For integral statements in this note use BLOCH HIGHER CHOW GROUPS

$$A=\operatorname{CH}^2(\mathcal X,2),\qquad
A_E=\operatorname{CH}^2(E,2).\tag{1.2}$$

They are defined by the actual codimension-two cycle complexes.
No integral Adams splitting of Quillen K-theory is assumed. On the
smooth generic curve, the usual coniveau calculation and the
field Milnor-K_2 comparison identify A_E with the kernel of the tame
symbols of K_2^M(Q(E)). The rational higher-Chow/K-theory comparison will be used only after
localizing the arithmetic model over the DVR Z_(389). We do not need
a blanket global comparison theorem on a nonsmooth scheme over Z.

For completeness retain the finite construction of beta_2. Let
C=X_mu(N), h:C -> X_0(N) -> E, and G=(Z/N)^*/{+/-1}.
Use the same normalized rational units U_a with divisor P_a-P_1,
the same nontrivial even character chi with b_chi nonzero, and
K_chi=Q(chi). Put

$$d_\chi=\frac1N S_\chi S_{\bar\chi},\qquad
q_{ab}=\frac1{[K_\chi:\mathbb Q]}
\operatorname{Tr}_{K_\chi/\mathbb Q}
\left(\frac{N d_\chi}{2(N-1)b_\chi}
                 \bar\chi(a)\chi(b)\right)\in\mathbb Q.$$

Then the actual class in (1.1) is the FINITE expression

$$\beta_2=\sum_{a,b\in G}q_{ab}\,h_*\{U_a,U_b\}.
\tag{1.3}$$

The coefficient trace in this formula is a trace on scalars of a fixed
rational vector space. It is not a base-field norm from C over K_chi.
All character bars, Gauss factors and homology normalizations remain
those independently checked in the predecessor; no new regulator
normalization is introduced here.

## 2. Primary localization and arithmetic-image inputs

**[THEOREM, arithmetic localization]** Bloch's cycle-complex localization
is valid for schemes essentially of finite type over a discrete
valuation ring, without a smoothness assumption. Geisser,
*Motivic cohomology over Dedekind rings*, Math. Z.248 (2004),773–794,
Theorem3.2 (Levine), Corollary3.3 and Lemma2.4 give its extension over
Dedekind bases and passage to the generic fiber. These assertions
were read in the [primary paper](https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf),
DOI10.1007/s00209-004-0680-x. The proof cites Levine,
*Techniques of localization in the theory of algebraic cycles*,
J. Algebraic Geom.10 (2001),299–363, Theorem1.7.

The weight-one calculation on SMOOTH schemes is Z(1)=G_m[-1].
The rational higher-Chow/K-theory comparison OVER A DVR and its
localization compatibility are recalled in Geisser, *Motivic Cohomology, K-Theory
and Topological Cyclic Homology*, Handbook of K-Theory (2005),
§§1.2.2,1.2.4,1.2.5 and1.4.4, in the
[author version](https://www2.rikkyo.ac.jp/web/geisser/Handbook.pdf).
The singular fiber below is calculated by localization; Z(1)=G_m[-1]
is NOT simply asserted on that nodal curve.

**[THEOREM, actual arithmetic image]** Schappacher–Scholl,
*Beilinson's theorem on modular curves*, in *Beilinson's conjectures
on special values of L-functions*, Perspectives in Mathematics4
(1988),273–304, Theorem1.1.2(iii), proves that the unramified modular-unit
symbol space P_K belongs to the image of rational weight-two K_2 of
regular arithmetic models. The definition is in1.1.1, and the
integrality proof is Theorem7.3.1 with descent in7.3.2. Root read the
[full authored paper](https://ncatlab.org/nlab/files/SchappacherScholl.pdf),
DOI10.1016/B978-0-12-581120-0.50015-X.
This theorem is about the CLASSES, not only equality of regulator images.

The rational K-theoretic arithmetic image is independent of the regular proper model and
is preserved by Chow correspondences. See also Scholl,
*Integral elements of K-theory and products of modular curves II*,
[arXiv:0710.5453, §§1–2](https://arxiv.org/pdf/0710.5453).
We use these established rational image and functoriality statements;
no integral pullback along an arbitrary arithmetic resolution is assumed.

**[NEW] Proposition 2.1.** The particular beta_2 of (1.3) belongs to

$$\operatorname{im}\left(A\otimes\mathbb Q
                    \longrightarrow A_E\otimes\mathbb Q\right).
\tag{2.1}$$

*Proof.* Every symbol {U_a,U_b} is unramified on the actual proper
curve C by the predecessor's precisely checked Brunault Proposition86.
It is, by definition, in the unramified modular-unit symbol subspace
Q_K, hence in P_K. Schappacher–Scholl's theorem puts it in the
rational arithmetic image for C.

The full-level integrality proof temporarily requires a level that is
a product of two coprime integers at least three. This premise can be
satisfied here by refining to full level 3N. Pullbacks of the stated
symbols are still modular-unit symbols and are unramified at all
cusps. Apply7.3.1 there and push back, using pull-push equal to the
finite covering degree; divide by that degree in the rational vector
space, exactly as7.3.2 does. This division is not declared an integral
unit. Equivalently use their final theorem1.1.2(iii), whose conclusion
already applies to arbitrary compact-open level. No theorem restricted
to full prime level is being applied outside its hypotheses.

The actual finite morphism h defines a Chow correspondence, so its
pushforward preserves the arithmetic image. Every q_ab in (1.3) is
rational; their finite linear combination stays in that image. To pass to the precise higher-Chow assertion (2.1), restrict this
K-theoretic arithmetic lift to X over Z_(389). The rational comparison
in §2 applies here OVER A DVR, with K'=K because this model is regular.
Its compatibility with generic restriction identifies the generic
higher-Chow class with our beta_2. Hence the higher-Chow boundary at
389 is zero rationally. At every other prime its target is rationally
zero by the independent smooth-fiber calculation in Proposition3.1
below. Arithmetic localization of Bloch's cycle complex therefore
supplies a GLOBAL rational higher-Chow lift; the exact sequence is
written in (4.5). This argument uses no smooth-over-Z assertion and
no stronger unstated global K/CH comparison. It retains beta_2 itself,
rather than replacing it with a class having the same real regulator. ∎

## 3. The exact bad-fiber group, including its free direction

Write D=X_(F_389) and s for its unique node. The already verified
coordinates are x=299+u, y=194+w, with

$$w^2=u^2(u+120).$$

Its normalization is P^1 over k=F_389, with

$$u=t^2-120,\qquad w=t(t^2-120).$$

The two points above the node are t=148 and t=241, since these are
the two square roots of120. Thus

$$D\setminus\{s\}\simeq\mathbb G_{m,k},\qquad
z=\frac{t-148}{t-241}.\tag{3.1}$$

Infinity on P^1 maps to z=1 and is retained in this smooth open.
The zero and pole of z are the two branches above the one node.

**[NEW] Proposition 3.1.** With these explicit choices,

$$\operatorname{CH}^1(D,2)=0,\qquad
\operatorname{CH}^1(D,1)\overset\sim\longrightarrow
  k[z,z^{-1}]^*=k^*\times z^{\mathbb Z}.\tag{3.2}$$

For every other prime r,

$$\operatorname{CH}^1(X_{\mathbb F_r},2)=0,\qquad
\operatorname{CH}^1(X_{\mathbb F_r},1)=\mathbb F_r^*.
\tag{3.3}$$

*Proof.* Apply the field localization sequence to the closed node in D.
For the degree-two term it gives

$$\operatorname{CH}^0(s,2)\to\operatorname{CH}^1(D,2)
                      \to\operatorname{CH}^1(\mathbb G_m,2).$$

Both outside groups vanish: codimension-zero higher Chow groups of a
field vanish in positive degrees, and the smooth weight-one complex
G_m[-1] gives CH^1(G_m,2)=0. This proves the first assertion.
For the degree-one term the sequence is

$$0\to\operatorname{CH}^1(D,1)
 \to k[z,z^{-1}]^*
 \xrightarrow{\partial_s}\operatorname{CH}^0(s,0)=\mathbb Z.$$

The boundary is the divisor at the missing node, computed by summing
the valuations at both normalization branches with residue-field degrees.
Both degrees are one. Constants have zero divisor, and z has orders
+1 and -1 at the two branches, so partial_s(cz^j)=j-j=0.
This proves the isomorphism in (3.2), including its actual coordinate z.
For a good fiber, the smooth weight-one calculation gives CH^1(-,2)=0
and CH^1(-,1)=global units. Proper geometric integrality makes those
units precisely F_r^*. ∎

The free Z direction in (3.2) is a REAL arithmetic-boundary possibility.
It is not removed because the fiber has only one irreducible component.
Nor does (3.2) identify CH^1(D,1) with the ordinary global units of the
proper singular curve D, which are only k^*. This is a homological
higher-Chow calculation on a singular fiber.

## 4. Restriction is injective and only one rational boundary remains

**[NEW] Theorem 4.1.** Integral restriction is injective,

$$A\hookrightarrow A_E,\tag{4.1}$$

and its image is the kernel of the ACTUAL vertical boundary map

$$\partial:A_E\longrightarrow
 \left(\bigoplus_{r\ne389}\mathbb F_r^*\right)
                  \oplus(\mathbb F_{389}^*\times z^{\mathbb Z}).
\tag{4.2}$$

No surjectivity onto the displayed target is asserted. Rationally,
only the z-exponent at389 survives; writing ord_z for that exponent,

$$\operatorname{im}(A\otimes\mathbb Q)
 =\ker\left(A_E\otimes\mathbb Q
          \xrightarrow{\operatorname{ord}_z\partial_{389}}\mathbb Q\right).
\tag{4.3}$$

In particular the actual beta_2 has a UNIQUE rational lift

$$\widetilde\beta_2\in A\otimes\mathbb Q,\qquad
\widetilde\beta_2|_E=\beta_2.\tag{4.4}$$

*Proof.* Apply the verified arithmetic cycle-complex localization and
pass to the generic fiber as in Geisser Lemma2.4/Corollary3.3. The
relevant exact part is

$$\bigoplus_r\operatorname{CH}^1(X_{\mathbb F_r},2)
 \longrightarrow A\longrightarrow A_E
 \xrightarrow{\partial}\bigoplus_r\operatorname{CH}^1(X_{\mathbb F_r},1).
\tag{4.5}$$

Proposition3.1 makes the first term zero and computes the last term,
proving (4.1)–(4.2). Tensoring with Q is exact, and every F_r^* is
finite, whereas the z-exponent gives Z. This proves (4.3).
Proposition2.1 supplies existence in (4.4), and (4.1) gives uniqueness. ∎

Thus arithmetic extension of this PARTICULAR noncentral divisor is
now proved. It does not imply that all elements of A_E extend, because
the possible free nodal boundary has not vanished as a group.
It also does not prove that beta_2 itself is integral without a denominator.

## 5. A fixed denominator can be cleared by explicit finite data

The following construction specifies sufficient denominators in terms
of actual finite algebraic inputs. It is not a numerical computation of
their values or a claim of minimum denominators.

Choose a positive integer M such that every M U_a is represented by a
rational function V_a on C, with its leading Fourier coefficient at
P_1 equal to one. Such M exists by the torsion cusp-divisor theorem
and the precise rational normalization in the predecessor. Equivalently,
choose a common multiple of the orders of the finitely many divisors
P_a-P_1 in the Jacobian, and normalize their principal functions.
The units and cusp divisors are fixed independently of any BSD quotient.

Choose D_c>0 with D_c q_ab in Z for every coefficient of (1.3), and put

$$D_0=2M^2D_c.\tag{5.1}$$

**[NEW] Lemma 5.1.** There is an actual integral generic class

$$b=D_0\beta_2\in A_E.\tag{5.2}$$

*Proof.* The rational unramifiedness of {U_a,U_b} implies that the
actual symbol {V_a,V_b} has torsion tame symbols. Its divisor support
consists only of the rational cusps P_a. At those cusps a tame symbol
lies in Q^*, whose torsion is {+/-1}; elsewhere both functions have
order zero and its tame symbol is one. Therefore 2{V_a,V_b} is
integrally unramified on C.

For a smooth curve over Q, localization/coniveau and the field Milnor
K_2 identification give CH^2(C,2) as this tame-symbol kernel. Hence
2{V_a,V_b} is an actual class of CH^2(C,2). Proper pushforward along h
is integral, and

$$D_0\beta_2=\sum_{a,b}(D_cq_{ab})\,h_*\bigl(2\{V_a,V_b\}\bigr)
\quad\text{in }A_E\otimes\mathbb Q$$

constructs the asserted integral preimage. Here b denotes this specified
preimage; no inverse map from A_E tensor Q to A_E is asserted, and
possible torsion has not been discarded. No finite covering degree
or modular degree is divided out in this pushforward. ∎

Choose a finite set S_0 of rational primes over which this actual
finite higher-cycle representative b spreads to X[1/S_0]. Such a
finite set exists directly: write a closed cycle representative with
finitely many rational equations and close it in the arithmetic
cycle complex; all failures of proper face intersection or of the
cycle equality lie over finitely many primes. Enlarge S_0 to contain389
if desired. Define

$$D_1=\operatorname{lcm}_{r\in S_0}(r-1),\qquad
D=D_0D_1,\tag{5.3}$$

with the empty lcm interpreted as one.

**[NEW] Theorem 5.2.** The actual integral class D_1 b has a unique
integral extension B in A. Its rationalization is
D times the lift (4.4), and

$$\mathscr R_E(B|_E)=D\frac{L(E,2)}\pi.\tag{5.4}$$

*Proof.* The vertical residues of b vanish outside S_0 by its spread.
At a good r in S_0 they belong to F_r^*, killed by r-1. At389 their
z-exponent is zero: the rational class of b is D_0 beta_2 and (2.1)
annihilates its rational boundary. An integer z-exponent with zero
rational image is zero. Its remaining boundary is in F_389^*, killed
by388. Thus D_1 kills EVERY actual vertical residue of b. Exactness
of (4.5) gives an integral extension B. Integral injectivity gives
uniqueness for this specified b and D_1. Rationalizing and using
(4.4) gives B tensor1=D tilde_beta_2. The generic regulator proves
(5.4). ∎

The uncomputed finite data M,D_c,S_0 in this construction are not
silently replaced by one. They can be obtained from the finite rational
unit/character construction and a chosen spread; no value is certified
here. Once chosen, D is independent of a later coefficient prime or
coefficient exponent. The subgroup Z B is a nonzero free rank-one
integral subgroup because its regulator is nonzero. It is NOT asserted
to be a saturated lattice in all arithmetic K-theory, or that the
intersection of its rational line with A is finitely generated.

## 6. The other finite fibers and the remaining comparison

This result gives the noncentral line an actual arithmetic lift and
one specified integral multiple. It does not divide by its real value
inside an unspecified period algebra. Its dual rational line remains
exactly the line used by the integrated spectral construction, so the
comparison target is still

$$D_{\rm pt}\otimes\mathbb Q\beta_2\otimes\mathbb Q(1)^{-2}.
\tag{6.1}$$

The frame beta_2 in that rational line continues to have regulator
L(E,2)/pi; passing to the integral generator B multiplies this frame
by the known-in-principle integer D, not by a silently omitted unit.
No change is made to the full real period, the saturated point basis,
the factor6N(N-1), or the reviewed finite point-height corrections.

The proof's uniqueness is in CH^2(X,2), not a statement that Quillen
K_2(X) has only this one weight or is a rank-one group. The free
nodal boundary is computed explicitly and is killed for beta_2 by
the modular-unit integrality theorem, not by assuming a conjectural
rank or finiteness statement for K-theory or Sha.

**[GAP K2-IS-389].** Construct a rational arithmetic source/class for
the actual integrated theta cocycle and a compatible map into (6.1),
whose real regulator coefficient is6N(N-1)n_E, and control its integral
image against the actual point and K2 subgroups rather than declaring
D or that large integer a unit. The construction here completes the
arithmetic extension of the noncentral divisor, not the missing map
from the spectral value. Rationality/integrality of n_E and full BSD
are still neither proved nor disproved.

## 7. Verification record

Root read the full predecessor construction and its independent review,
the exact regular model, Schappacher–Scholl1.1.1–1.1.3 and7.3–7.4,
Scholl0710.5453 §§1–2, and Geisser's actual arithmetic localization
statement and rational comparison scope. The bad-fiber higher-Chow
calculation and denominator-killing argument are proved directly above.
No old arithmetic-surface or analytic certificate was rerun. The node
coordinates and tangent slopes were read from their existing exact
certificate and proved model, not recomputed as a new result.
All new deductions require independent adversarial review before promotion.
