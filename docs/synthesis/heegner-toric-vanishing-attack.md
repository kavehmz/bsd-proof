# A level-raising lift of the two-prime toric obstruction

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded proof attempt; all [NEW] deductions passed
[independent review](review-heegner-toric-vanishing.md).
Restart: [checkpoint](heegner-toric-vanishing-checkpoint.md).
The universal objective remains full BSD for elliptic curves over Q.
No new rank-five vanishing is claimed.


**Subsequent reviewed scope extension.** The
[signed Gysin continuation, Theorem6.3](heegner-gysin-bridge.md#62-removing-full-image-the-original-irreducible-o5-range-suffices)
removes the extra full mod-p^k image hypothesis from exact-order detection
over Q, using the ORIGINAL residual irreducibility in O5. Its
[independent review](review-heegner-gysin.md) checks the primary
Lawson–Wuthrich input and the replacement Nakayama argument. The
full-image argument below remains a valid historical proof in that
subrange; the later theorem supplies detection in the full original
irreducible range. This extension proves no rank-sensitive vanishing.

## 1. The proposed operation and its exact input

Keep the full hypotheses and choices in
[the reviewed two-prime construction](two-prime-heegner-height-attack.md)
and [its local reciprocity continuation](heegner-local-reciprocity-attack.md).
Thus E/Q is non-CM, p>=5 is good ordinary, E[p] is irreducible,
$r_{\mathrm{an}}(E)$ is odd and at least five, and K has odd
fundamental discriminant D different from -3, prime to Np.
Every prime of Np splits in K and $L(E^D,1)\ne0$.
Fix distinct inert Heegner Kolyvagin primes $\ell,q$, put
$m=\ell q$, and retain
$$
 k=\min\{v_p(\ell+1),v_p(a_\ell),v_p(q+1),v_p(a_q)\}.
$$
Let $F=H_m$, $h_m=[F:K]$, and retain the actual point
$$
 A_m=S_GD_\ell D_q,\qquad P=P_m=A_my_m\in E(F).
 \tag{1}
$$
The parametrization $\pi:X_0(N)\to E$ sends infinity to O;
its degree is $d_\pi$, with no assumption that it is one
or a p-adic unit.

Take a fresh inert prime $v\nmid6NpDm$ with
$p^k\mid v+1,a_v$. Put
$$
 L=H_{mv},\quad M_v=v+1,\quad a=a_v,\quad
 \delta_\pm=M_v\pm a,\quad d_v=M_v^2-a^2 .
 \tag{2}
$$
Here $[L:F]=M_v$ because the CM unit quotient is one.
Both $\delta_\pm$ are nonzero by Hasse's bound and are
divisible by $p^k$. Consequently $p^{2k}\mid d_v$.
Enough such v detect the full global class under the
additional image hypothesis
$\rho_{E,p^k}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb Z/p^k)$,
as previously proved. The point identities below require
only the displayed fresh-prime conditions.

The attempted vanishing argument is concrete: lift the
weighted divisor to level Nv, separate its f-old part
using the two degeneracy maps, and test whether the
additional untwisted derivative vanishing kills its
integral complementary part. The calculation produces
two actual cofactor points. One has zero trace to F,
but its reduction is exactly the finite obstruction.
Its primitive character-height expansion is computed
in §5. This is the term the operation leaves.

## 2. The actual level-Nv CM divisor, including the cusp term

Write $J=J_0(N)$, $J_v=J_0(Nv)$, and let
$\alpha,\beta:X_0(Nv)\to X_0(N)$ be the two degeneracy
maps, sending a cyclic v-isogeny of enhanced N-curves
to its source and target. Choose a CM v-isogeny
$\widetilde x_{m,v}$ with
$$
 \alpha(\widetilde x_{m,v})=x_m,\qquad
 \beta(\widetilde x_{m,v})=x_{mv}.
 \tag{3}
$$
The compatible CM choice in (3) can be obtained from
$\mathcal O_{mv}\subset\mathcal O_m$; multiplying the
target lattice by v gives the indicated direction
of the cyclic v-isogeny. It is defined over L.

The inertia factors $G_\ell,G_q,G_v$ form the product
in $\operatorname{Gal}(L/H_1)$. Lift the class-group
transversal S compatibly to L and put
$\widetilde A_m=\widetilde S_GD_\ell D_q$ there.
There is no $D_v$ in this operator. Define
$$
 Z=A_m([x_m]-[\infty])\in J(F),\quad
 z=\widetilde A_m([\widetilde x_{m,v}]-[\infty])
                       \in J_v(L),\quad
 Y=\widetilde A_my_{mv}\in E(L).
 \tag{4}
$$
Then $\pi_*Z=P$,
$\pi_*\alpha_*z=P$ and $\pi_*\beta_*z=Y$.
All expressions are actual points before rationalization.

**[THEOREM, primary geometric input]** The degeneracy
correspondences and CM-isogeny orbit are the ones in
[Bertolini-Darmon, *Euler systems and Jochnowitz
congruences*, Amer. J. Math. 121 (1999), 259–281,
§2 and Proposition 5.1](https://www.math.mcgill.ca/darmon/pub/Articles/Research/21.Jochnowitz/paper.pdf).
The latter is written for conductor one; the orbit
calculation below verifies its current conductor-m
version directly. The classical point trace and
reduction relations are also recorded in
[Howard, arXiv:1202.6340v1, §1.7](https://arxiv.org/html/1202.6340#S1.SS7).
No characteristic-zero level-raised eigenform is
assumed in this construction.

Let $c_N$ be the cusp represented by $1/N$ on
$X_0(Nv)$ and $C_v=[c_N]-[\infty]\in J_v(\mathbb Q)$.
Put
$$
 d_A=\operatorname{aug}(A_m)
      =\frac{h_K\,\ell(\ell+1)q(q+1)}4\in\mathbb Z.
$$

**[NEW] Proposition 2.1 (exact norm of the lifted divisor).**
$$
 \operatorname{Tr}_{L/F}Y=aP,\qquad
 \operatorname{Tr}_{L/F}z
       =\alpha^*Z+v\,d_A C_v .
 \tag{5}
$$

*Proof.* At the inert fresh prime v, all $v+1$ cyclic
v-isogenies of the CM enhanced curve have conductor mv
targets and form the orbit of
$\operatorname{Gal}(L/F)$. There are no extra unit
identifications in the present discriminant range.
The first equality is the Heegner trace relation,
with the same weighted operator applied.

For the second equality, the two cusps above infinity
under $\alpha$ are infinity, of ramification index one,
and $c_N$, of ramification index v. The indices follow
from the cusp widths: width one at infinity and
width v at $1/N$ on level Nv. Their sum is the degree
$v+1$, so they account for the entire fiber. Thus
$\alpha^*[\infty]=[\infty]+v[c_N]$.
The norm of each chosen CM lift is its entire
$\alpha$-fiber. Subtracting the norm of the
$(v+1)$ copies of infinity therefore differs from
$\alpha^*([x_m]-[\infty])$ by $vC_v$.
Sum with the exact weights in (4).
$\square$

The cusp term is torsion, but (5) retains it rather
than discarding it before an integral calculation.
Its two degeneracy images are zero in J because
both cusps map to infinity under both degeneracy
maps.

## 3. The degeneracy projector and what clearing it loses

Let $i=\pi^*:E\to J$ and $q_E=\pi_*:J\to E$,
so $q_Ei=[d_\pi]$. Define actual homomorphisms
$$
 j:E^2\to J_v,\quad j(P_1,P_2)=\alpha^*i(P_1)+\beta^*i(P_2),
 \qquad
 q_v:J_v\to E^2,\quad
 q_v=(q_E\alpha_*,q_E\beta_*).
$$
The standard identities
$\alpha_*\alpha^*=\beta_*\beta^*=v+1$ and
$\alpha_*\beta^*=\beta_*\alpha^*=T_v$
give the exact matrix equality
$$
 q_vj=d_\pi\Delta_v,\qquad
 \Delta_v=
 \begin{pmatrix}M_v&a\\a&M_v\end{pmatrix}.
 \tag{6}
$$
These are the maps and multiplicities in the
primary §2 just cited.

**[NEW] Proposition 3.1 (rational old projection).**
The rational endomorphism
$$
 e_{\mathrm{old}}=j(d_\pi\Delta_v)^{-1}q_v
                         \in\operatorname{End}^0(J_v)
 \tag{7}
$$
is the projector onto this f-old E-squared block.
Writing $j_\pm(T)=j(T,\pm T)$, it gives
$$
 e_{\mathrm{old}}z
 =j_+\left(\frac{P+Y}{2d_\pi\delta_+}\right)
  +j_-\left(\frac{P-Y}{2d_\pi\delta_-}\right)
           \quad\text{in }J_v(L)\otimes\mathbb Q.
 \tag{8}
$$

*Proof.* The determinant $d_v$ is nonzero.
Equation (6) directly proves $e_{\mathrm{old}}^2
=e_{\mathrm{old}}$ and its identity action on
the image of j. Diagonalizing $\Delta_v$ on
the vectors $(1,1),(1,-1)$ gives (8).
$\square$

The complement here is the kernel of $q_v$ in
the rational isogeny category. It can contain
other old factors as well as v-new factors;
it is not declared purely v-new without a
further justified Hecke localization.
In fact, if $\mathcal R=(1-e_{\mathrm{old}})z$,
then (5) gives exactly
$$
 \operatorname{Tr}_{L/F}\mathcal R
   =\alpha^*(1-iq_E/d_\pi)Z
          \quad\text{in }J_v(F)\otimes\mathbb Q.
 \tag{9}
$$
This explicitly retains the other old contribution.

Now form the actual points
$$
 B_1=\frac{M_v}{p^k}P-\frac a{p^k}Y,\qquad
 B_2=\frac{M_v}{p^k}Y-\frac a{p^k}P
                  \quad\text{in }E(L).
 \tag{10}
$$
The coefficients in (10) are integers. They
are the adjugate coordinates of (6), divided
by their known common factor $p^k$.

**[NEW] Proposition 3.2 (the actual integral remainder).**
The cleared complementary point is
$$
 W=d_\pi d_v z-p^k j(B_1,B_2)\in\ker(q_v)(L).
 \tag{11}
$$
It lies in $p^kJ_v(L)$ without using analytic
rank five. Its specified quotient
$$
 W^{(1)}=d_\pi(d_v/p^k)z-j(B_1,B_2)\in J_v(L)
$$
satisfies
$$
 W^{(1)}\equiv-j(B_1,B_2)
                         \pmod{p^kJ_v(L)}.
 \tag{12}
$$
Moreover
$$
 \operatorname{Tr}_{L/F}B_1=(d_v/p^k)P,\qquad
 \operatorname{Tr}_{L/F}B_2=0.
 \tag{13}
$$

*Proof.* Multiply the rational complementary
projection by $d_\pi d_v$, use the adjugate
of $\Delta_v$, and apply (6). This proves
(11) exactly on points. Because $p^{2k}\mid
d_v$, the displayed $W^{(1)}$ is integral,
$p^kW^{(1)}=W$, and its first term is zero
modulo $p^k$, proving (12). Taking norms
in (10), using (5) and
$\operatorname{Tr}_{L/F}P=M_vP$, gives (13).
$\square$

Thus clearing the rational projector
denominator and then reducing modulo
$p^k$ always gives zero. It cannot be
used as rank-sensitive vanishing. The
first divided remainder still contains
the concrete points $B_1,B_2$.
No reduction modulo $p^k$ of an
unspecified rational division point
in (8) has been made.

## 4. The trace-zero cofactor still carries the toric obstruction

Fix the reduction place above v, as
in the local reciprocity construction.
All reductions of points of E(L) are
in $\widetilde E(\mathbb F_{v^2})$:
the extension L/F is totally ramified
there and F has completion $K_{(v)}$.
Let $\mathsf F$ be arithmetic
Frobenius on the reduction and let
$$
 x=\delta_v(\overline P)
  =(\mathsf F^2-1)Q
       \in E[p^k],\qquad p^kQ=\overline P.
 \tag{14}
$$
This x is the finite localization of
the raw two-prime class.

**[NEW] Proposition 4.1 (exact reductions of both cofactors).**
$$
 \overline{B_1}=-x,\qquad
 \overline{B_2}=-\mathsf F x
                 \quad\text{in }\widetilde E[p^k].
 \tag{15}
$$
In particular, for the plus basis
$\lambda_v$ already fixed in LR-TP5,
$$
 -\lambda_v\operatorname{pr}_+
       (\overline{B_2})
 =\operatorname{ev}_v(\operatorname{loc}c_m)
 =\psi_{v,k}(e_t\mathcal D_{v,m})
                      \quad\text{in }\mathbb Z/p^k .
 \tag{16}
$$

*Proof.* Specialization of the chosen
CM v-isogeny is relative Frobenius
on its supersingular source. This
holds for every conjugate lift:
the degree-v subgroup specializes
to the unique subgroup of that
order in the supersingular
v-torsion, namely the Frobenius
kernel. It also follows from the
two degeneracy maps at the
supersingular node. The prime-to-v
N-structure specializes compatibly.
Applying the parametrization, which
is defined over $\mathbb F_v$, and
the same weights gives
$\overline Y=\mathsf F\overline P$.

The characteristic polynomial
$\mathsf F^2-a\mathsf F+v=0$
gives the exact endomorphism
identities
$$
 M_v-a\mathsf F=1-\mathsf F^2,\qquad
 M_v\mathsf F-a=(a-\mathsf F)(\mathsf F^2-1).
$$
Using $p^kQ=\overline P$ in (10)
therefore gives
$$
 \overline{B_1}=(1-\mathsf F^2)Q=-x,\qquad
 \overline{B_2}=(a-\mathsf F)x=-\mathsf Fx,
$$
where $a x=0$ because $p^k\mid a$.
These formulas in particular prove
that the reductions are p^k-torsion,
although the original points need
not be torsion. The raw two-prime
class is plus, so x is fixed by
$\mathsf F$. This proves (16)
using the previous exact reciprocity.
$\square$

This calculation recovers the local
finite-singular sign independently:
$$
 (\sigma_v-1)D_vY
       =M_vY-aP=p^kB_2 .
 \tag{17}
$$
Thus $B_2$ is the *specified*
division term in the three-prime
raw cocycle at $\sigma_v$.
That cocycle has reduction
$-\overline{B_2}=\mathsf Fx$.
The finite conjugation action on
x is $\mathsf F$, whereas the
transverse action is
$v^{-1}\mathsf F=-\mathsf F$;
the raw three-prime sign is -1.
Under O5 the normalizing scalars
are $u_2=u_3=-1$. There is no
extra quadratic-corestriction
factor in (15) or (16), which
are K-local identities.

Consequently the operation has
not destroyed the original
obstruction before clearing
denominators: it appears in
the torsion reduction of the
actual trace-zero point $B_2$.
At a prime detecting a class
of order $p^s$, this reduction
has that same exact order.

## 5. Attempting geometric vanishing by the cofactor height

A sufficient way to make the right
side of (16) zero is to prove that
$B_2$ is torsion. Indeed
$E(L)[p]=0$ by the same
unramified-at-p/irreducibility
argument as for H_m. A torsion
point B_2 would have order prime
to p, whereas (15) makes its
reduction p-primary; hence that
reduction would be zero.

We test this sufficient geometric
argument by computing the height
of this *specified* point. This
is not a height of an arbitrary
lift of a cohomology class.

Let $\mathcal G=\operatorname{Gal}(L/K)$,
$h_{mv}=M_vh_m$ and $G_v=\operatorname{Gal}(L/F)$.
For each complex character chi of
$\mathcal G$ let $c_\chi\mid mv$
be its exact conductor and
$\chi_c$ the corresponding
primitive character. Use the
same Artin/projector convention
as in the reviewed height note.
Write
$$
 a_\chi^{\mathrm{op}}
   =\widetilde A_m(\chi)
   =\left(\sum_{s\in\widetilde S}\chi(s)\right)
                d_\ell(\chi)d_q(\chi),
$$
where
$$
 d_r(\chi)=
 \begin{cases}
 r(r+1)/2,&\chi(\sigma_r)=1,\\
 (r+1)/(\chi(\sigma_r)-1),&\chi(\sigma_r)\ne1.
 \end{cases}
 \tag{18}
$$
There is again no $D_v$ in this
evaluation.

**[NEW] Proposition 5.1 (the exact remaining character sector).**
The point $B_2$ has zero rational
projection onto every character
trivial on $G_v$. Its height is
$$
 \boxed{\displaystyle
 \widehat h_K(B_2)=
 \frac{d_\pi\sqrt{|D|}}
 {8\pi^2(f,f)_{\Gamma_0(N)}\,p^{2k}h_m^2}
 \sum_{\substack{\chi\in\widehat{\mathcal G}\\
                    \chi|_{G_v}\ne1}}
 c_\chi\,|a_\chi^{\mathrm{op}}|^2
 \left(\prod_{r\mid mv/c_\chi}a_r^2\right)
 L'(E/K,\chi_c,1).}
 \tag{19}
$$
In this sum $v\mid c_\chi$, so
each missing-prime factor is at
ell or q. The height convention
is exactly the fixed $\widehat h_K$
of Cai-Shu-Tian, unchanged across
fields of definition.

*Proof.* If chi is trivial on
$G_v$, the norm identity
$\operatorname{Tr}Y=aP$ gives
$e_\chi Y=(a/M_v)e_\chi P$.
Insert (10) to get $e_\chi B_2=0$.
If chi is nontrivial on $G_v$,
then $e_\chi P=0$ and
$e_\chi B_2=(M_v/p^k)e_\chi Y$.

For the unnormalized primitive
toric point $Y_{\chi_c}(c_\chi)$,
the actual conductor trace
identities give
$$
 e_\chi Y=\frac{a_\chi^{\mathrm{op}}}{h_{mv}}
       \left(\prod_{r\mid mv/c_\chi}a_r\right)
            Y_{\chi_c}(c_\chi).
$$
Each removed prime is inert
and fresh for the smaller
conductor, so these are the
a_r-only trace factors in
their valid range. Orthogonality
of the Hermitian character
components, followed by the
elliptic-quotient formula in
[Cai-Shu-Tian, arXiv:1408.1733v2,
Theorem 1.1](https://arxiv.org/html/1408.1733),
gives (19). The factor
$M_v^2/h_{mv}^2=1/h_m^2$
accounts for the displayed
denominator.

For all primitive conductors
here, $(c_\chi,N)=1$, every
prime of N is split, and
$(N,D)=1$. The source's
common-discriminant factor
and CM-unit correction are
therefore one. Its
$8\pi^2(f,f)$, conductor,
discriminant and parametrization
degree are all retained.
$\square$

The right side of (19) is a
sum of nonnegative character
heights, expressed through
their own first derivatives.
It contains only characters
ramified at the *new* prime v.
The untwisted term, whose
third central derivative is
zero under rank five, has
already been eliminated from
this actual point by the
cofactor operation.

Thus the sufficient proposal
“prove $B_2$ torsion by its
height” leaves exactly (19).
No source used here asserts
that this sum vanishes from
$L'''(E/K,1)=0$.
We do not claim that torsion
of B_2 is necessary for
LR-TP5; a non-torsion point
can have zero reduction.
Nor do we assert that every
summand is nonzero. Formula
(19) states precisely which
actual analytic terms remain.

## 6. Why deleting the level-raising Euler factor does not repair it

There is a precise match between
the denominator in the
degeneracy projector and the
old local Rankin Euler factor.
For the untwisted base change
at this inert prime,
$$
 Q_v(s)=1-(a_v^2-2v)v^{-2s}+v^{2-4s},\qquad
 L^{(v)}(E/K,s)=Q_v(s)L(E/K,s).
 \tag{20}
$$
This follows by squaring the
two Frobenius eigenvalues
over the unramified quadratic
extension. All other finite
Euler factors are retained.
At the central point
$$
 Q_v(1)=\frac{(v+1)^2-a_v^2}{v^2}
                      =\frac{d_v}{v^2}.
 \tag{21}
$$

**[NEW] Proposition 6.1 (the extra derivative in this operation).**
Under the already known
untwisted vanishing through
order two,
$$
 \big(L^{(v)}(E/K,\cdot)\big)'''(1)
             =\frac{d_v}{v^2}L'''(E/K,1).
 \tag{22}
$$
Under O5 both sides are zero.
The same product rule preserves
vanishing through order four.

*Proof.* Differentiate the
product (20) three times.
All terms differentiating
$Q_v$ multiply a derivative
of L of order at most two
and are zero. This proves
(22). The higher stated
vanishing follows by the
same rule.
$\square$

The complex number $d_v/v^2$
is nonzero, so (22) is a
valid complex identity.
It is not a reduction of a
complex derivative modulo
$p^k$. In the integral
degeneracy construction,
the same d_v is divisible
by $p^{2k}$. Equation (11)
shows concretely that
clearing this denominator
erases the finite test
irrespective of analytic
rank. Dividing the known
factor once leaves the
cofactor points in (10),
whose reduction and height
are (15) and (19).

Replacing the original
unramified local L-factor
by a v-new Steinberg factor
is an additional operation:
for a v-new eigenform with
$U_v=\pm1$, its base change
local factor is
$(1-v^{-2s})^{-1}$.
That is not (20) for E.
Identifying its primitive
toric values with our
finite tests requires a
level-raising/Jochnowitz
comparison with the relevant
coefficient precision.
The primary Bertolini-Darmon
Theorem 6.1 supplies a
residual conductor-one
comparison under its extra
optimal-curve and
$p\nmid2N d_\pi$ assumptions,
as audited in the prior
note. It does not identify
the ramified-character
height sum (19) with the
untwisted third derivative.
No such extension is
being assumed here.

## 7. The remaining arithmetic step after this test

The proposed level-Nv
operation has been carried
out on actual divisors,
Jacobians and points:

- Its norm includes the
  explicit cusp term (5).
- Its rational f-old
  projector has the
  exact matrix (6).
- Clearing its denominator
  gives an automatically
  p^k-divisible point (11).
- The specified
  cofactor $B_2$ has trace
  zero but reduces to
  $-\mathsf F x$, where x
  is the entire finite
  two-prime Kummer value.
- Its height is the
  explicit primitive
  v-ramified sum (19).

This identifies the term
left by a concrete attempt,
rather than replacing the
arithmetic objects with an
abstract norm-relation
module. It does not force
the term to vanish.

**[GAP TV-TP5].** Under
the hypotheses of §1,
construct a geometric or
derived-reciprocity
comparison using the
additional untwisted
$L'''(E/K,1)=0$ which
proves
$$
 \overline{B_2}=0
            \quad\text{in }\widetilde E[p^k]
 \tag{23}
$$
for every fresh detecting v.
By (15)–(16) and full-image
fresh-prime detection, this
would prove LR-TP5 in its
stated image range.
One must control the
specified reduction, not
the automatically zero
norm or the cleared
projector, and not assign
a height to an unspecified
cohomology representative.

The positive-height
criterion tested in §5 is
stronger than (23) and
remains unsupported.
An eventual comparison
could instead control
(23) directly without
vanishing of (19).
The current identities
leave that precise
arithmetic step open.

No shared synthesis file
was edited, no new agent
spawned, and no numerical
certificate rerun.
All [NEW] deductions
passed the linked review.
TV-TP5 remains open.
