# Global tame nullhomotopies and the remaining native local obstruction

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-tame-nullhomotopy.md](review-heegner-tame-nullhomotopy.md).
All eight sections were checked against mathematical revision
90b0925736532683e8ee1ab03b6b5fc155b3b2ddb9f9844c14a47a14e0e3b713.
Subsequent header, source-location and checkpoint changes are editorial.
Restart: [checkpoint](heegner-tame-nullhomotopy-checkpoint.md).
The objective remains full BSD over Q.

The actual rank-zero twist zeta value kills the first GLOBAL cup
obstructions in the additional surjective range below. This produces
global finite-coefficient nullcochains for the cofactor-corrected
input, without dividing that zeta value. The local conditions inherited
from points in the regular representation are stricter than merely
allowing every finite twist correction. We compute their old-prime
condition and an actual remaining finite duality test. The mixed
class and its ambiguity are then explicit. Rank-five vanishing is
not proved.

## 1. Fixed actual input, fields, and coefficients

Keep the hypotheses, normalization and classes of the
[reviewed Heegner–Kato construction](heegner-kato-comparison-attack.md).
In particular p>=5 is good ordinary and nonanomalous,
E[p] is irreducible, K has odd discriminant D prime to Np,
all primes of Np split in K, L(E^D,1) is nonzero, and
p does not divide h_K for the independent tame coordinates.
The extra h_K condition is not asserted for every auxiliary twist.
Put
$$
 m=\ell q,\quad k=M(m),\quad R=\mathbb Z/p^k,\quad
 M=E[p^k],\quad M_D=M\otimes\epsilon_K,\quad
 U=\operatorname{Spec}\mathbb Z[1/(Np|D|\ell q)] .
 \tag{1}
$$
S is precisely the finite complement of U and the real place.
These are invertible finite etale coefficients on U; finite
cohomology groups at primes in S are not suppressed.

Let w_k be the finite reduction of the actual integral Kato
second derivative. Fix ACTUAL finite Selmer classes A,B and
the old local determinant operation from the preceding proof:
$$
 x=\mathcal P_{A,B}(w_k)\in
 \operatorname{Sel}_{p^k}(E/\mathbb Q)
                   _{\operatorname{loc}_\ell=\operatorname{loc}_q=0}.
 \tag{2}
$$
The theorem below applies to every such fixed x, even when
the determinant or x is nonprimitive. The choices A,B are
not used to manufacture a unit comparison. Their exact
ambiguity remains the one in the preceding note.

Set d_0=F_D(0), with the fixed Neron/Coleman normalization,
and z=d_0x. The input is a correction of the actual second
BF coefficient d_0w_k; it is not an asserted canonical
replacement of that coefficient.
The inverse Artin characters
$$
 a_i\in Z^1(G_{\mathbb Q,S},R\epsilon_K),\qquad i=\ell,q,
 \tag{3}
$$
are the genuine ones constructed from the p-part of the
ring-class extension of conductor i. Write F_i/K for that
cyclic extension, of degree p^{e_i}, e_i=v_p(i+1)>=k.
It is ramified only at i over K, totally ramified there,
and conjugation acts on its group by inversion.
The coordinate a_i takes value -1 on the fixed tame
generator. No new local cup isomorphism is assumed or
reproved in this note.

The first equation is
$$
 d t_i=-a_i\cup z \quad\text{with coefficients }M_D .
 \tag{4}
$$
The raw Heegner class and its rational descent are unchanged:
kappa_Q=cor_(K/Q)(kappa_K)/2, u_2=-1 for conversion to
the standard class. Rational finite Frobenius tests are
one-half the corresponding K-tests; tame inertia has no
additional quadratic factor.

## 2. A zeta annihilator with its full valuation

Let
$$
 t=v_p(\operatorname{Tam}(E^D)),\qquad
 s=v_p(\#\operatorname{Sha}(E^D/\mathbb Q)[p^\infty]),
       \qquad A_D=p^{t+s}.
 \tag{5}
$$
Rank-zero theorems give finiteness in (5); it is not assumed
for E. Irreducibility gives E^D(Q)[p]=0, and the rank-zero
twist has no p-primary point contribution. Thus
Sel_(p^k)(E^D)=Sha(E^D)[p^k] has order at most p^s.

For identifying A_D with the actual d_0, add the explicit
hypothesis that E[p] is **surjective**. Then E^D[p] is
surjective as well. Indeed K ramifies at a prime outside
Np whereas Q(E[p])/Q is unramified there, so their
intersection is Q; quadratic twisting leaves the full
matrix image available.

**[THEOREM, exact primary input and consequence]**
[Castella–Sano2601.14504v1, Theorem B and Section1.1.3](https://arxiv.org/html/2601.14504v1)
give, in the good ordinary surjective range with p-unit
Manin constant,
$$
 v_p\left(\frac{L(E^D,1)}{\Omega_{E^D,\rm full}}\right)
       =t+s.
 \tag{6}
$$
To check scope: the displayed rank-zero formula there is
v_p(#Sha)=M_0-M_infinity, delta_1=L/Ω, and Theorem B
identifies M_infinity with v_p(Tam). The ordinary case
does not require squarefree conductor, so the conductor
ND^2 causes no failure. An optimal parametrization of
E^D has p-unit Manin constant because p is good;
prime-to-p isogenies and the fixed period convention
do not change (6).

The Euler factor (1-alpha^{-1})^2 in d_0 is a p-unit by
nonanomalous reduction. The full real period differs
from the plus-cycle period by a factor1 or2, also a
p-unit. Therefore in this range
$$
 d_0=u_D p^{t+s},\qquad u_D\in\mathbb Z_p^\times.
 \tag{7}
$$
No factor is deleted from d_0 as an identity of classes.
In the merely irreducible range, A_D remains the proved
annihilator below; replacing it by d_0 requires the
corresponding valuation bound, which is not inferred here.

At primes dividing N the twist is locally isomorphic to E.
At primes dividing D the twist of good reduction is additive,
with component-group order at most4 (including the possible
small-residue-characteristic additive types). Hence for p>=5
$$
 t=\sum_{v\mid N}v_p(c_v(E)).
 \tag{8}
$$
This records the full p-part of the Tamagawa factor used below.

## 3. Local norm construction and the global first equations

**[NEW] Lemma 3.1.** If L'/L is finite unramified over a
nonarchimedean local field, then
N:E_0(L') to E_0(L) is surjective.

*Proof.* On the connected special fiber G, write F for
Frobenius and n for the residue degree. The endomorphism
N_n=1+F+...+F^{n-1} has finite kernel, since its kernel
is contained in ker(F^n-1). Consequently it is surjective
on the connected algebraic group. For P in G(F_q), choose
Q with N_nQ=P; then (F^n-1)Q=(F-1)P=0, so Q belongs
to G(F_(q^n)). This proves surjectivity on residue points.
On successive formal-group filtration quotients the norm
is the trace of the unramified residue extension, hence
surjective. Successive correction and completeness lift
the chosen residue preimage to E_0(L'). This proof includes
unramified extensions whose degree is divisible by the
residue characteristic. Square.

**[NEW] Proposition 3.2.** For i=ell,q,
$$
 p^t(a_i\cup x)
   \in\ker\left(H^2(U,M_D)\longrightarrow
                       \bigoplus_{v\in S}H^2(\mathbb Q_v,M_D)\right).
 \tag{9}
$$

*Proof.* At both old primes x is strictly zero. At p,
nonanomalous reduction gives H^0(Q_p,M_D)=0 and hence
H^2(Q_p,M_D)=0 by local duality. At v dividing D,
E is good and the nontrivial quadratic inertia on the
twist makes H^0(Q_v,M_D)=0, so H^2 is zero there too.
The real Tate group vanishes because p is odd.

At v dividing N, the character a_i is unramified.
Multiplication by p^t kills the component of a point
Kummer class modulo p^k. Explicitly, the prime-to-p
component can first be changed by a p^k multiple;
the remaining p-primary component is killed by p^t,
so the resulting class has a representative in E_0(Q_v).
Lemma3.1 supplies its norm preimage in the unramified
local extension cut out by a_i. Shapiro and the quotient
of its regular representation to the first tame extension
therefore give a local lift. The connecting homomorphism
of that extension is cup with a_i, proving its vanishing.
At any remaining good prime in S, both classes are
unramified (away from the old conductor), so the cup
vanishes by the cohomological dimension1 of the finite
residue-field group. The same argument after quadratic
restriction is valid because its degree2 is a p-unit.
The Shapiro group at a split or partially decomposed place
is a sum over local places. A norm preimage may be placed
in one such summand; no factor equal to the number of
places is introduced by restricting to diagonal tuples.
Square.

For clarity, the coefficient extension just used is
$$
 0\longrightarrow M_D\longrightarrow N_i
                   \longrightarrow M\longrightarrow0 .
 \tag{10}
$$
It is an actual subquotient of
M tensor Ind_K^Q R[Gal(F_i/K)]. In the sum/difference
theta basis, take the summand spanned by e_+ and Y_i e_-,
where Y_i^2=0. The involution exchanging the two induced
characters and replacing Y_i by -Y_i commutes with G_Q,
and its integral projector is (1+involution)/2.
The action on (z,t) is
$$
 g(z,t)=(g z,\ \epsilon_K(g)\,g t+a_i(g)\,g z).
 \tag{11}
$$
Here g on z,t on the right denotes the elliptic coefficient
action before the displayed quadratic twist.
Equation(11) gives connecting cocycle a_i cup z and
the nullhomotopy equation(4). All norm constructions use
this specified quotient; no arbitrary extension is postulated.

**[NEW] Theorem 3.3 (global first nullhomotopies).**
A_D(a_i cup x)=0 in H^2(U,M_D). In the surjective
range of (6), equation(4) for the ACTUAL z=d_0x
has continuous global solutions at the full R coefficient.

*Proof.* Finite Poitou–Tate gives a perfect pairing
$$
 \Sha_S^2(M_D)\times\Sha_S^1(M_D)\longrightarrow
                      p^{-k}\mathbb Z/\mathbb Z ,
 \tag{12}
$$
where Sha_S^j denotes the kernel of localization at all S.
The module is self-dual by the Weil pairing. The second
group in (12) is a subgroup of Sel_(p^k)(E^D), including
the unramified finite conditions outside S. Its order is
at most p^s. Thus p^s kills the group containing (9).
This proves the first assertion; (7) gives the second.
Square.

This is not an annihilation theorem for all H^2(U,M_D).
Its old-prime local terms can have order p^k. The strict
input in (2), followed by (9), is essential.

The solutions can be constructed at finite coefficients:
choose continuous representatives of a_i,x, then search
finite quotients of G_Q,S containing their coefficient
data and solve the finite linear equations
d:C^1(G,N) to C^2(G,N) over R with target -a_i cup z.
The theorem ensures that a quotient admitting a solution
exists: a continuous primitive factors through a finite
quotient. Fixing an ordering and choosing a solution in
that finite linear system gives an actual nullcochain.
This construction is not canonical. Modulo coboundaries,
all solutions form a torsor under H^1(U,M_D).
If v_p(d_0)>=k the input is already zero; the theorem
does not recover an unscaled class by cancellation.

The duality input(12) is finite, not rational.
It follows directly from
[Demarche–Harari1804.03941v3, Theorem1.1 and Proposition2.1](https://arxiv.org/html/1804.03941v3):
H_c^2 is dual to H^1, and quotienting by all local
H^1 boundary classes leaves the dual of Sha_S^1.
Equivalently it is Milne ADT second edition I.4.10,
whose I.5.1 discussion records the finite kernel sequence.

## 4. The point image at the ramified prime and its transverse kernel

Define the native local condition on N_i to be the image
of the actual point-Kummer group in the regular Shapiro
representation under the specified coefficient quotient(10).
This definition retains the origin of the desired lift.
It is not replaced by an arbitrary finite condition on
the two graded pieces.

**[NEW] Proposition 4.1.** At the ramified old prime i
that native image in H^1(Q_i,N_i) is zero. However
$$
 \ker\left(H^1(\mathbb Q_i,M_D)
                     \longrightarrow H^1(\mathbb Q_i,N_i)\right)
                  =H^1_{{\rm tr},i}(\mathbb Q_i,M_D),
 \tag{13}
$$
the free rank-one transverse line. It is not the finite line.

*Proof.* E has good reduction at i. Over F_i the point
Kummer condition is unramified. Shapiro identifies it
with the unramified cohomology of the regular coefficient
module, whose inertia invariants contain the regular
norm element. Its image in R[Y_i]/Y_i^2 is
$$
 \sum_{r=0}^{p^{e_i}-1}(1+Y_i)^r
   =p^{e_i}+\frac{p^{e_i}(p^{e_i}-1)}2Y_i=0 .
 \tag{14}
$$
Both coefficients vanish in R, and the denominator2 is
a unit. The induced map on unramified cohomology is
therefore zero. Quadratic restriction/corestriction does
not change that conclusion.

The coefficient sequence(10) says that its H^1 kernel
is the boundary of H^0(Q_i,M). That invariant module
is the plus Frobenius line. Formula(11) sends its generator
to the primitive tame class a_i tensor that generator.
It spans the transverse line of M_D: this class is killed
on restriction to F_i, whereas the finite line restricts
injectively by the p-unit residue degree2. This proves
(13). Square.

Thus local native compatibility of a global nullcochain
does not allow arbitrary finite twist corrections.
The relevant permitted changes at i are transverse.
The first global theorem did not assert this extra
compatibility.

At other places define the exact permitted correction
subgroup by
$$
 J_{i,v}=\{h\in H^1(\mathbb Q_v,M_D):
       \operatorname{im}(h)\text{ lies in the native
                                    image for }N_i\}.
 \tag{15}
$$
This uses actual finite maps. It also makes sense at bad
primes with component defects; those groups are retained.

In the additional clean range p not dividing Tam(E),
one has
$$
 J_{i,v}=
 \begin{cases}
 H^1_{{\rm tr},i}(\mathbb Q_i,M_D),&v=i,\\
 H_f^1(\mathbb Q_v,M_D),&v\ne i.
 \end{cases}
 \tag{16}
$$
Here are the local checks. Away from p,D,i, the coefficient
extension is unramified. Finite Kummer equals unramified
cohomology in this range, also over the odd-degree
unramified extensions at bad reduction. Taking inertia
invariants in the regular-module quotient is exact,
since its underlying coefficient quotient is R-split.
The chosen splitting is inertia-equivariant: inertia
acts trivially on the auxiliary regular and quotient
coefficient factors. It may still act on the elliptic
factor M, which is tensorized with that split sequence.
Passing to Frobenius coinvariants is right exact.
The resulting native image is exactly the unramified
condition, and its preimage on M_D is the same condition.
At D, H^1(Q_v,M_D)=0 by quadratic inertia and local Euler
characteristic.

At p use the ordinary filtration. Its unramified quotient
has residual eigenvalue alpha not equal to1. Tensoring
with the unramified p-group coefficient modules does
not create invariants; all their residual simple
unramified factors have eigenvalue1. Local duality
therefore makes the H^2 of the plus-kernel in the
coefficient quotient zero. H^1 of that plus quotient
is consequently surjective. Finite Kummer over these
unramified p-extensions is the ordinary plus condition,
and its preimage on M_D is exactly its plus condition.
This verifies the remaining case of(16).
For arbitrary Tamagawa factors we use (15), not (16).

## 5. The remaining finite native-local test

All actual native local lifts of z exist after its Tamagawa
factor: at i and the other old prime use the zero lift of
the strict class; at unramified places use Lemma3.1 and
the quotient of the regular point class. At good places
the same norm argument applies without a Tamagawa factor.
Choose local primitives tau_(i,v) with
d tau_(i,v)=-a_i cup loc_v(z) corresponding to these
point-image lifts.

With the reviewed signed compact convention,
$$
 D(c,b)=(dc,\operatorname{res}c-db),\qquad
 \partial^+(b)=(0,+b),
 $$
form the actual compact class
$$
 \mathfrak c_i=(-a_i\cup z,\ (\tau_{i,v})_v)\in H_c^2(U,M_D).
 \tag{17}
$$
It has a well-defined image modulo partial^+(direct-sum J_i,v);
different native local lifts change it by precisely such
permitted local classes. A global nullcochain satisfying
all those native local requirements exists if and only if
that image is zero. This equivalence follows directly by
writing a compact boundary as D(t,b).

**[NEW] Proposition 5.1.** The quotient containing (17)
is perfectly dual to the ACTUAL Selmer group with local
conditions J_i,v perpendicular. For a class b in that
group its value is the explicit cochain expression
$$
 \mathscr P(b,\mathfrak c_i)
   =\sum_{v\in S}\operatorname{inv}_v
          \bigl(\tau_{i,v}\cup b_v-u_v\bigr),\qquad
        du=(-a_i\cup z)\cup b .
 \tag{18}
$$
Coefficient cup products in (18) use
e_(p^k)(compact coefficient, ordinary coefficient)
on M_D, in exactly that order. The odd-p global H^3
vanishes, so u exists.

*Proof.* The local boundary pairing is
sum inv(h_v cup b_v), in the stated order. Therefore
the annihilator of partial^+(direct-sum J_i,v) is
exactly the global group with perpendicular local
conditions. Finite compact duality proves perfectness.
For (18), the compact-first product is
((-a_i cup z) cup b, (tau_i,v cup b_v)_v).
Subtracting D(u,0) gives the displayed local boundary.
Global reciprocity and compact boundaries prove
independence of u and cocycle representatives. Square.

Theorem3.3 says that the ordinary H^2 component of(17)
is zero. It does not set this compact class to zero.
Equivalently its remaining obstruction is in
$$
 \frac{\bigoplus_{v\in S}H^1(\mathbb Q_v,M_D)}
      {\operatorname{loc}H^1(U,M_D)+\bigoplus_v J_{i,v}},
 \tag{19}
$$
which is dual to the image of localization of the Selmer
group in Proposition5.1. The S-strict kernel
must be quotiented when making this latter identification.

In the clean range(16), both finite and transverse
rank-one local lines are self-annihilating. The dual
group is therefore Sel_(p^k)(E^D) with the single
transverse condition at i, classical finite conditions
elsewhere.

**[NEW] Proposition 5.2 (a sharp rank-zero control case).**
If additionally Sha(E^D)[p-infinity]=0, that actual
transverse twist Selmer group is isomorphic to R.

*Proof.* Its classical Selmer group is zero. Finite
Poitou–Tate for relaxing only i makes the singular
localization an isomorphism from the relaxed group
onto the rank-one singular quotient R. Its full local
image is a graph over the transverse line. Global
reciprocity makes this image isotropic. The local
pairing is symmetric hyperbolic with the finite and
transverse axes isotropic; a graph with slope c has
self-pairing 2c times a unit. Since2 is invertible,
c=0. The relaxed image is exactly the transverse
line, proving the assertion. Square.

This computes an actual residual group in a clean
arithmetic range. It does not assert that (18) is
nonzero. Even when d_0 is a unit, a zero classical
twist Selmer group does not make (19) zero: its
native transverse group in Proposition5.2 is R.
No arbitrary old-local section is used to normalize
or cancel (18).

## 6. The mixed obstruction on the constructed global first lifts

Choose the global solutions t_ell,t_q of Theorem3.3.
Let a_ell,q(g)=a_ell(g)a_q(g). The actual mixed
two-cocycle is
$$
 \Omega(t_\ell,t_q)
    =-a_\ell\cup t_q-a_q\cup t_\ell-a_{\ell,q}\cup z
                       \in Z^2(U,M).
 \tag{20}
$$
It is closed by (4) and
d a_ell,q=-(a_ell cup a_q+a_q cup a_ell).
There is a global mixed primitive v exactly when
its H^2 class vanishes.

**[NEW] Proposition 6.1.** Its exact choice ambiguity is
$$
 [\Omega(t_\ell+h_\ell,t_q+h_q)]
   =[\Omega(t_\ell,t_q)]-
       a_\ell\cup[h_q]-a_q\cup[h_\ell],
 \tag{21}
$$
for h_i in Z^1(U,M_D). Thus a well-defined obstruction
coset lies in
$$
 \frac{H^2(U,M)}
 {a_\ell\cup H^1(U,M_D)+a_q\cup H^1(U,M_D)} .
 \tag{22}
$$
If native local compatibility is imposed, only those
h_i with localizations in J_i,v may be used in(21).

*Proof.* Substitute into (20). A change by a coboundary
adds the boundary of a_ell cup b_q+a_q cup b_ell.
Changing z by dr changes t_i by a_i cup r, and changes
the mixed primitive by a_ell,q cup r. These give the
same cohomology coset. The last assertion follows
from (15). Square.

One actual possible global adjustment is the finite
reduction of the twist's rank-zero Kato class:
h_i=lambda_i z_D,0,k. It changes the mixed class by
$$
 -\lambda_q\,a_\ell\cup z_{D,0,k}
             -\lambda_\ell\,a_q\cup z_{D,0,k}.
 \tag{23}
$$
At each old prime, its cup coefficient is the corresponding
ACTUAL finite localization of z_D,0,k under the already
specified tame cup coordinate; it is not presumed a unit.
Over K the finite Frobenius value is twice its Q value.
At p this Kato class is p-relaxed. Its nonzero rational
dual exponential does not supply an allowed finite
adjustment. At finite coefficients the exact requirement
is lambda_i loc_p(z_D,0,k) in J_i,p; no nonunit scalar
may be cancelled in that condition. Thus (23) is an
explicit candidate operation with a retained local defect,
not a solution of the mixed equation.
At the ramified old i it is a finite point-Kummer class,
so finite/transverse intersection zero further requires
lambda_i loc_i(z_D,0,k)=0. The actual old-prime values
therefore constrain which zeta adjustments are permitted.

## 7. Comparison with the actual top Heegner class

If (20) has a primitive v, the full cochain
$$
 (z,0)+Y_\ell(0,t_\ell)+Y_q(0,t_q)
                       +Y_\ell Y_q(v,0)
 \tag{24}
$$
is a class in the actual two-variable induced theta
coefficient module. The preceding reviewed proof identifies
the actual Shapiro Heegner point class with
Y_ell Y_q kappa_raw at full p^k. The top-ideal map on
global H^1 is injective by the no-p-torsion hypothesis.

Consequently, adding that ACTUAL Heegner Shapiro class
to (24) preserves its constant and both single-variable
coefficients and changes its top coefficient by kappa_raw.
It also preserves native point-image local conditions
whenever those have been achieved, since the added
class comes from the actual point y_m and Shapiro.
This is an arithmetic ambiguity of the constructed
coefficient module and point class, not an abstract
norm-relation countermodel.

Thus solving first and mixed equations does not on its
own identify the resulting top class. A specific integral
motivic or Rankin comparison must choose the lift and
prove its relation to the Heegner coefficient. The present
global first annihilator uses rank-zero twist arithmetic
and the already known Selmer-corank-three input for w_0.
It has not used the additional complex equality
L'''(E,1)=0. No formula in (18), (20), or (23) has been
identified with that complex derivative.

**[OPEN, TN-TP5].** Evaluate the native finite pairing(18)
for the constructed Kato input and its actual transverse
twist tests, and solve the compatible mixed problem with
its ambiguity(21). Then construct an integral comparison
selecting the top coefficient and prove rank-sensitive
vanishing from the additional COMPLEX input. All p^k,
the valuation of d_0, and the nonprimitive quotient
must survive that comparison.

## 8. Primary inputs and completed scope

- Castella–Sano2601.14504v1, Sections1.1.1–1.1.4,
  especially the exact rank-zero formula and Theorem B,
  read directly. This proves (6) in the additional
  surjective range, including non-squarefree ND^2.
- [Milne, Arithmetic Duality Theorems, second edition](https://www.jmilne.org/math/Books/ADTnot.pdf),
  I.4.10 and the finite kernel sequence in I.5.1,
  together with local abelian duality in I.3. The independent
  reviewer additionally verified II.2.9 (printed pp.170–171),
  identifying the finite etale cohomology on this U with
  G_Q,S cohomology for our p-invertible coefficients, and
  I.4.10(c) for the odd-p global H^3 vanishing.
- Demarche–Harari1804.03941v3, Theorem1.1 and
  Proposition2.1, read in the primary HTML, supply
  finite compact duality, exact localization and
  the actual cone interpretation. The project's
  signed boundary/trace convention is retained.
- The ring-class, Shapiro, tame-coordinate, integral
  Kato derivative and BDV normalizations are those
  of the linked independently reviewed predecessor.
  No old computation was rerun.

Only the assigned proof/checkpoint files were written.
No new subagent or shared synthesis edit was made.
