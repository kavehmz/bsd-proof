# The geometric point determinant and its Deligne conjugation coefficient

Date: 2026-09-12. Owner: root/coordinator. Completed bounded construction.
The original six sections passed [independent review](review-point-determinant-single-valued.md),
including the geometric rational K2 extension and the level/object notation repair.
The additional §7 comparison test also passed its separate audit in that review.
[Restart](point-determinant-single-valued-checkpoint.md).
Full BSD over Q is neither proved nor disproved.

## 1. Fixed geometric input and the meaning of the coefficient

Use the ACTUAL 389a1 one-motive
$M=[L\to J(E,A)]$ from
[the relative point construction, §§3–6](relative-modular-cycle-attack.md).
Here $A=\{O,P,Q\}$, $P=(-1,1)$, $Q=(0,-1)$,
$X=\mathbb ZD_1\oplus\mathbb ZD_2$ with $D_i=(P_i)-(O)$,
and $L=\mathbb Ze_1\oplus\mathbb Ze_2$.
The prescribed divisors $Z_j$ include the fixed principal modifications
by the actual functions $h_1,h_2$. Every finite height contribution
then vanishes; no real height or L-value chose those functions.

Write $V=T_{\rm B}(M)$ for its rank-six homological realization,
$T=X^\vee\otimes\mathbb Z(1)$, and $H=H_1(E,\mathbb Z)$.
The weight pieces of $V$ are $T,H,L$ in weights $-2,-1,0$.
Let $t_i$ be the positive puncture loop dual to $D_i$:
$\int_{t_j}\rho_i=2\pi i\,\delta_{ij}$.
This is an abstract integral Betti generator of the Tate lattice;
its comparison period is $2\pi i$, which is retained.

The established height matrix is
$$
 H_{ij}^{\rm ht}=\operatorname{Re}\int_{\gamma_j}\eta_i,
 \qquad \partial\gamma_j=Z_j,\qquad
 \det H^{\rm ht}=\operatorname{Reg}_E>0.                 \tag{1.1}
$$
All entries use the full Mordell–Weil basis and the same BSD height
normalization as the certificate. Superscript ht distinguishes this
matrix from the pure homology $H$.

We construct a canonical Deligne-conjugation coefficient of the
rational geometric object $\bigwedge^2 V$. This is a single-valued
Hodge invariant with declared weight frames. It is NOT asserted to be
an entry of a de Rham period matrix in an unspecified rational basis.
In particular, Betti scalar conjugation and geometric real Frobenius
are different operations. No comparison with the de Rham
single-valued involution of Brown–Fonseca is silently imposed.

**[THEOREM, source input]** Deligne's bigrading is functorial, and
there is a unique real operator $\delta_V$, of strictly negative
bidegrees, for which $e^{-i\delta_V}F$ is real split.
The framing and height conventions used below are those of
[Burgos Gil–Goswami–Pearlstein, 2410.17167v3](https://arxiv.org/pdf/2410.17167v3),
§§2.1–2.3, especially Proposition2.16 and Definitions2.14,2.19.
This is the 67-page revision with header July9,2026.
We use only these Hodge definitions, not a conjectural global height.

The two scalar heights in that source take, respectively, the
imaginary part of the extreme conjugation coefficient and the
extreme coefficient of $\delta$. Keeping the full complex coefficient
is essential in this application.

## 2. The actual height matrix is the Deligne splitting block

Choose the rectangular period basis from the completed construction,
$\omega_0=\omega_E/\omega_1$, $\int_a\omega_0=1$ and
$\int_b\omega_0=\tau=it_0$, $t_0>0$.
Let
$$
 A_i=\int_a\rho_i,\quad B_i=\int_b\rho_i,\quad
 C_{ij}=\int_{\gamma_j}\rho_i,\quad
 v_j=\int_{\gamma_j}\omega_0.
$$
The already fixed real-normalized differential is
$\eta_i=\rho_i-c_i\omega_0$ with
$c_i=\operatorname{Re}A_i-i\operatorname{Re}B_i/t_0$.

**[NEW] Proposition2.1.** In the fixed integral top and bottom frames,
$$
 \delta_V(e_j^{\rm D})
       ={1\over2\pi}\sum_i H_{ij}^{\rm ht}t_i,\qquad
 \delta_V(W_{-1}V)=0,\qquad \delta_V^2=0,                \tag{2.1}
$$
where $e_j^{\rm D}\in I^{0,0}_V$ is the Deligne lift of $e_j$.

*Proof.* Write $v_j=r_j+s_j\tau$ uniquely with $r_j,s_j$ real.
The real relative vector
$\gamma'_j=\gamma_j-r_ja-s_jb$ has zero $\omega_0$ period. Put
$k_{ij}=C_{ij}-r_jA_i-s_jB_i$ and
$$
 e_j^{\rm D}=\gamma'_j-\sum_i{k_{ij}\over2\pi i}t_i.    \tag{2.2}
$$
It is annihilated by $\omega_0,\rho_1,\rho_2$, which span
$F^1$ in the dual realization. Thus it lies in $F^0V_\mathbb C$.
Its conjugate differs from it only by puncture loops.
The defining Deligne-bigrading condition therefore puts it in
$I^{0,0}$, and its given top image makes this lift unique.

The normalization of $c_i$ gives
$$
 \operatorname{Re}k_{ij}
   =\operatorname{Re}(C_{ij}-c_i v_j)=H_{ij}^{\rm ht}.
$$
Taking conjugates in (2.2), with the Betti loops fixed by scalar
conjugation, gives the exact identity
$$
 \overline{e_j^{\rm D}}-e_j^{\rm D}
   =-{i\over\pi}\sum_iH_{ij}^{\rm ht}t_i.               \tag{2.3}
$$
The only possible strictly negative bidegree on this weight pattern
is the map $I^{0,0}\to I^{-1,-1}$. Hence $\delta_V$ is zero on
$W_{-1}$ and squares tozero. The identity
$\overline{e_j^{\rm D}}=e^{-2i\delta_V}e_j^{\rm D}$
now yields (2.1). This derives the sign directly, without transferring
a convention for a dual biextension. For the pure Kummer special
case, the lift is path$-\log u\cdot t/(2\pi i)$, giving the same sign.
$\square$

Changing the relative chains or lifted compact cycles changes the
intermediate period entries but not (2.3), since (1.1) and the
Deligne lifts are intrinsic to the marked one-motive. A change of
the marked point bases transforms the matrix in the usual two-sided
way; it is not an arbitrary renormalization of the height.

## 3. A geometric exterior square with the integral factor controlled

Let
$$
 N=\bigwedge\nolimits^2 V,\qquad
 \varphi:\mathbb Z(0)\longrightarrow\operatorname{Gr}_0^W N,
 \quad1\longmapsto e_1\wedge e_2,
$$
and use $D_1\wedge D_2$ to frame its bottom as
$$
 \psi:\operatorname{Gr}_{-4}^W N
     =\bigwedge\nolimits^2T\longrightarrow\mathbb Z(2),
 \qquad t_1\wedge t_2\longmapsto1(2)_{\rm B}.            \tag{3.1}
$$
The graded ranks in weights $0,-1,-2,-3,-4$ are $1,4,5,4,1$.

**[NEW] Proposition3.1.** This is a rational geometric framed mixed
Hodge structure, with the stated free integral exterior lattice.
In an actual product of relative curve pairs, its exterior projector
is the PLUS geometric interchange projector, not the minus one.

*Proof.* Let $B^*$ be the full support of the corrected $Z_1,Z_2$,
not merely their original three endpoints, and put $U=E\setminus A$.
The completed one-motive realization is the marked pullback of
$H_1(U,B^*)$ along $e_j\mapsto Z_j$. These two divisors are independent:
an integral relation would map to the same relation on the independent
points $P,Q$ in $\operatorname{Pic}^0(E)$. Thus the marked pullback
maps injectively into the relative homology. Its precise integral
lattice is the previously constructed pullback lattice; saturation
inside every larger unmarked lattice is not needed.

The generalized-Jacobian period realization can also be read directly
in [Sertöz–Ouaknine–Worrell, 2505.20397v1](https://arxiv.org/html/2505.20397v1),
§6.5, Proposition6.5.43. It retains the rational principal changes.

Set $B^{(2)}=(B^*\times U)\cup(U\times B^*)$. The relative product
cross-map identifies
$$
 H_1(U,B^*;\mathbb Z)^{\otimes2}
       \simeq H_2(U^2,B^{(2)};\mathbb Z).                \tag{3.2}
$$
Indeed the relative homology of the connected punctured curve and
its nonempty finite marking is free and concentrated in degree1.
The chain cross-product and relative Künneth theorem therefore have
no Tor or other-degree term. They respect the rational mixed Hodge
structures: Deligne's
[Hodge III](https://www.numdam.org/item/10.1007/BF02685881.pdf),
Proposition8.2.10 and §§8.3.8–8.3.9, give the product and relative
mixed-Hodge constructions. Taking cones for the relative factors
gives the same cross-map on the corresponding filtered complexes.

Geometric interchange $\sigma$ acts on degree1 cross degree1 by
$\sigma_*(x\times y)=-y\times x$. Consequently
$(1+\sigma_*)/2$ is the antisymmetrizer on the underlying ordinary
tensor square. Restrict to the marked subobject $V^{\otimes2}$.
Its rational image is precisely $\bigwedge^2V$.

Integrally the map
$$
 \jmath:\bigwedge\nolimits^2V_\mathbb Z
       \longrightarrow V_\mathbb Z^{\otimes2},\qquad
 x\wedge y\longmapsto x\otimes y-y\otimes x               \tag{3.3}
$$
identifies its source with the geometric-interchange invariant
lattice. In a free basis, such invariants have zero diagonal entries
and opposite off-diagonal entries, proving this equality directly.
The projector itself contains a denominator2 and is not an integral
endomorphism of the entire tensor lattice. We use (3.3), on both
top and bottom frames; no extra factor2 enters their coefficient.
The ordinary quotient from the antisymmetric tensor to the abstract
exterior square would multiply (3.3) by2 and is not used as its inverse.
$\square$

This constructs an exterior-square geometric realization, not a
rank-one algebraic biextension or an asserted algebraic cycle whose
ordinary height has been prescribed to be the determinant.

## 4. The determinant is a real quadratic coefficient; both usual heights vanish

Let $e_N=e_1^{\rm D}\wedge e_2^{\rm D}$, $t_N=t_1\wedge t_2$,
and extend the bottom frame $\psi$ by the Deligne projection:
$\psi^{\rm D}=\psi\pi_{-4}$, recording its coefficient in $1(2)_{\rm B}$.

**[NEW] Theorem4.1.** On this ACTUAL object,
$$
 \psi^{\rm D}(\delta_N e_N)=0,\qquad
 \psi^{\rm D}(\delta_N^2 e_N)
                   ={\operatorname{Reg}_E\over2\pi^2},\qquad
 \psi^{\rm D}(\overline{e_N})
                   =-{\operatorname{Reg}_E\over\pi^2}.  \tag{4.1}
$$
In particular, the two framed scalar heights of 2410.17167v3 both
vanish for $(N,\varphi,\psi)$, although its full extreme conjugation
coefficient is nonzero.

*Proof.* The Deligne splitting is compatible with tensor operations.
One can verify this here directly: the real derivation
$\delta_V\otimes1+1\otimes\delta_V$ makes the tensor product real split
after applying its exponential, has strictly negative bidegrees,
and so is the unique Deligne operator on that tensor product.
It restricts to $N$ and acts by
$$
 \delta_N(x\wedge y)=\delta_Vx\wedge y+x\wedge\delta_Vy.
$$
Thus $\delta_Ne_N$ has weight $-2$, while
$$
 \delta_N^2e_N=2\delta_Ve_1^{\rm D}\wedge\delta_Ve_2^{\rm D}
             ={\det H^{\rm ht}\over2\pi^2}t_N,
 \qquad \delta_N^3=0.                                  \tag{4.2}
$$
The exponential is $1-2i\delta_N-2\delta_N^2$.
Projecting its value on $e_N$ to the bottom proves (4.1).
Equivalently, take the exterior product of the two explicit formulas
(2.3). The imaginary-part height sees only zero, and the linear
$\delta$ height also sees zero. These are their definitions, not
an inference from the zero of one of the individual point heights.
$\square$

The canonical quadratic functional on these fixed frames is therefore
$$
 \mathcal Q(N,\varphi,\psi)
    =2\pi^2\psi^{\rm D}(\delta_N^2e_N)
    =-\pi^2\psi^{\rm D}(\overline{e_N})
    =\operatorname{Reg}_E.                             \tag{4.3}
$$
Its value is not assumed rational. The operations $\pi_{-4}$ and
$\delta_N$ are the specified canonical Hodge operations; neither is
being called a rational morphism of mixed Hodge structures.

**[NEW] Corollary4.2.** Let $B$ be any mixed Hodge structure supported
only in weights0 and-4 with Tate graded pieces. No morphism
$N\to B$ can be nonzero on the bottom frame, and no morphism
$B\to N$ can be nonzero on the top frame.

*Proof.* On $B$, $\delta_B^2=0$. Naturality gives
$f\delta_N^2=\delta_B^2f=0$. By (4.2), $\delta_N^2$ has nonzero
image equal to the entire bottom line, so the first assertion follows.
In the other direction, $\delta_N^2$ kills $W_{-1}N$ and is nonzero
on its top quotient, again by the derivation formula. The relation
$\delta_N^2f=f\delta_B^2=0$ therefore forces zero top map.
$\square$

Thus collapsing all intermediate weights into a two-step extension
cannot preserve the relevant framed data. This tests these actual
objects and morphisms, not every higher arithmetic construction.

## 5. The K2 factor inside an actual tensor object

The fixed rational higher cycle $\beta_2$ supplies a geometric Hodge
extension
$$
 0\longrightarrow K=H^1(E,\mathbb Q(2))
  \longrightarrow B_{\beta}\longrightarrow\mathbb Q(0)
  \longrightarrow0.                                  \tag{5.1}
$$
**[THEOREM, regulator input]** The extension realization of a higher
cycle and its real Deligne regulator is the construction recalled in
2410.17167v3, §1.4 and §5.1; here $p=n=2$.
Its associated regulator is the SAME $\beta_2$ already constructed,
with native one-form $i\eta_K$ and period $L(E,2)/\pi$.
No different scalar normalization or dimension-one assertion about
rational $K_2(E)$ is used.

The pure bottom $K$ has weight-3, with types $(-1,-2),(-2,-1)$.
Let $e_\beta\in I^{0,0}_{B_\beta}$ be its unique top Deligne lift and
write
$$
 U_\beta=\pi_{-3}(\overline{e_\beta})
         =\overline{e_\beta}-e_\beta
         =-2i\delta_\beta e_\beta.                       \tag{5.2}
$$
It is a vector, not a choice of a rational period coordinate.

**[NEW] Proposition5.1.** The actual tensor object
$N\otimes B_\beta$ has a canonical extreme conjugation vector
$$
 \begin{split}
 U_{N,\beta}
  &=(\psi\otimes1)\pi_{-7}
                   (\overline{e_N\otimes e_\beta})\\
  &=-{\operatorname{Reg}_E\over\pi^2}\,
                        1(2)_{\rm B}\otimes U_\beta
       \quad\hbox{in }K(2)_\mathbb C.                  \tag{5.3}
 \end{split}
$$
This is a coefficient of one tensor realization, not a claim that
an arbitrary formal product of real numbers is a rational period.

*Proof.* The Deligne bigrading on the tensor product is the tensor
bigrading, as can be checked by its defining properties. The only
way to reach the lowest weight-7 is weight-4 in $N$ and weight-3
in $B_\beta$. Thus its coefficient is the product of the two
specified extreme coefficients. Equation(4.1) proves(5.3).
All frames and the extension were fixed before this calculation.
$\square$

The equation determines the vector in the Betti-framed Tate factor.
One must retain the comparison of $1(2)_{\rm B}$ with
$1(2)_{\rm dR}$ before interpreting a de Rham period. No operation
that deletes this factor or multiplies by an additional real period
is implicit in (5.3). Nor does (5.3) assert that a real multiple of
$\beta_2$ has a rational motivic preimage.

For the already specified mixed period functional, keep the separate
full real cycle $\gamma_\mathbb R=2a$, the rational differential
$\omega_E$, and the ordinary inverse Tate period. The value is
$$
 \left(\int_{\gamma_\mathbb R}\omega_E\right)
 \mathcal Q(N,\varphi,\psi)\,
 \mathscr R_E(\beta_2)\,(2\pi i)^{-2}
       =-{\Omega_E\operatorname{Reg}_E L(E,2)\over4\pi^3}. \tag{5.4}
$$
Equations(4.3) and(5.3) now specify the geometric tensor coefficient
underlying its quadratic height factor. Equation(5.4) does not
turn that secondary Hodge functional into an ordinary rank-one
height or a rational morphism.

## 6. Exact comparison still to construct

Here the modular level is389; the symbol $N$ above denotes the
exterior-square object, not that integer.
The relative radial class and its rational boundary comparison give
$$
 \mathscr P(\mathcal C_{j_2})=\mathcal M,\qquad
 \mathscr P(\operatorname{reg}j_B(\beta_2))
        ={388\,\omega_1L(E,2)\over8\pi^3c_\pi}.
$$
Their scalar quotient lacks precisely the point determinant. This
note supplies its actual geometric exterior-square coefficient and
its tensor with the fixed K2 extension. It does not construct a map
from the spectral relative class to that tensor object.

**[GAP PD-389].** With all objects, integral point frames, finite
Kummer corrections, real cycle $2a$, and Tate comparisons fixed as
above, construct a rational arithmetic comparison for the original
spectral class (or the canonical Poisson/Hodge-height operation)
whose specified secondary period is (5.4) times
$6\cdot389\cdot388\,n_E$, and prove the required lattice statement with $n_E$
as a conclusion. An arbitrary real rescaling of either class does
not satisfy this statement.

The current compact cup/trace construction is being investigated
separately. Its eventual real projected value, even if fully
determined, cannot simply be declared to be (5.3). The required
rational comparison remains a substantive theorem. Full universal
rank equality, Sha finiteness and the leading formula for every
elliptic curve remain the completion test.

## 7. A direct comparison of the relative extension and determinant weights

This is an additional bounded deduction, saved after the original
six-section review and separately audited PASS in the linked review's §7.

Let $V_0=X_0(389)\times E$ and
$B_0=\{0,\infty\}\times E$. These names distinguish the surface
from the homological one-motive realization $V$ above.
Write
$$
 D=H^2(V_0,B_0;\mathbb R(2)).
$$
We now test a literal morphism of mixed Hodge structures as a
possible comparison. General secondary arithmetic operations are
not presumed to be such morphisms.

**[NEW] Lemma7.1.** The mixed Hodge structure $D$ has only weights
$-3,-2$. There is a natural identification
$$
 H^3_{\mathcal D}(V_0,B_0;\mathbb R(2))
      \simeq\operatorname{Ext}^1_{\mathbb R\text{-MHS}}
                         (\mathbb R(0),D).               \tag{7.1}
$$
For every real relative Deligne class $c$, its corresponding extension
$B_c$ has only weights $0,-2,-3$ and satisfies $\delta_{B_c}^2=0$.

*Proof.* Both inclusions of the boundary fiber induce the identity
on the E cohomology and zero on positive-degree X cohomology.
Künneth and the relative exact sequence therefore give
$$
 0\longrightarrow H^1(E,\mathbb R)
 \longrightarrow H^2(V_0,B_0;\mathbb R)
 \longrightarrow
  H^2(X,\mathbb R)\oplus
       \bigl(H^1(X,\mathbb R)\otimes H^1(E,\mathbb R)\bigr)
 \longrightarrow0.                                      \tag{7.2}
$$
The left group is the cokernel of the diagonal
$H^1(E)\to H^1(E)\oplus H^1(E)$; the right group is the kernel
of the H² restriction. They are pure of weights1 and2.
After twist2 this gives precisely the asserted weights.

In the next degree the sequence similarly gives
$$
 0\longrightarrow\mathbb R(-1)
 \longrightarrow H^3(V_0,B_0;\mathbb R)
 \longrightarrow H^3(V_0;\mathbb R)\longrightarrow0,       \tag{7.3}
$$
where the right side is pure of weight3. Thus
$H^3(V_0,B_0;\mathbb R(2))$ has only weights$-2,-1$.

For completeness, use the actual relative Deligne cone
of the real and Hodge-filtered relative cochain complexes.
Its long exact sequence, and strict Hodge filtration for this
proper algebraic pair, identify its degree-three group with
an extension of
$$
 {D_\mathbb C\over F^0D_\mathbb C+D_\mathbb R}
$$
by the real classes in
$F^0H^3(V_0,B_0;\mathbb C(2))$.
That latter group is zero: a real vector in $F^0$ would define
a morphism $\mathbb R(0)$ into a mixed Hodge structure with
strictly negative weights. Strictness forces its image tozero.
The relative filtered-cone and product statements are
Deligne HodgeIII, §§8.3.8–8.3.9 and Proposition8.2.10; this is
not an assertion of an unrestricted equivalence of Deligne and
absolute Hodge cohomology.

For a mixed Hodge structure of negative weights, the quotient
$D_\mathbb C/(F^0+D_\mathbb R)$ classifies extensions of
$\mathbb R(0)$ by $D$: choose a real lift of1 and a Hodge lift
in $F^0$, and take their difference modulo those two subspaces.
Conversely this construction defines the Hodge filtration on
the extension and gives its inverse. This proves(7.1).

Every strictly negative Deligne bidegree lowers total weight by
at least two. In an extension with weights$0,-2,-3$ it can only
map the top into the bottom subobject, and vanishes on that
subobject. Hence its square iszero. $\square$

**[NEW] Theorem7.2.** For every $c$ as in Lemma7.1, no morphism
of real mixed Hodge structures
$$
 B_c\longrightarrow N
 \quad\hbox{or}\quad
 B_c\longrightarrow N\otimes B_\beta                    \tag{7.4}
$$
can be nonzero on the weight-zero top quotient. In particular,
this holds for the actual real class $\mathcal C_{j_2}$ and for
any hypothetical rational motivic lift through this relative group.

*Proof.* On $N$, $\delta_N^2$ kills $W_{-1}$ and is nonzero on
the one-dimensional top by(4.2). Naturality with
$\delta_{B_c}^2=0$ rules out a nonzero top map to $N$.

On the tensor target, the exact derivation formula gives
$$
 \delta_{N\otimes B_\beta}^{\,3}
       =3\delta_N^2\otimes\delta_\beta.                  \tag{7.5}
$$
Here $\delta_N^3=0$ and $\delta_\beta^2=0$.
The right side kills $W_{-1}(N\otimes B_\beta)$:
a tensor in that subspace has either its N factor in $W_{-1}N$,
annihilated by $\delta_N^2$, or its $B_\beta$ factor in $K$,
annihilated by $\delta_\beta$.
It is nonzero on the top because $\operatorname{Reg}_E>0$
and the already constructed real regulator of $\beta_2$ is
nonzero. For this two-step extension, zero $\delta_\beta$
would mean a split real extension and zero real regulator.
Applying naturality to(7.5), with $\delta_{B_c}^3=0$, rules out
a nonzero top map in the second case as well. $\square$

The inverse Tate twist in the target period does not cure this
literal-morphism problem. Twisting $N\otimes B_\beta$ by$(-2)$
raises its top weight to4, which a map from $B_c=W_0B_c$ cannot
reach at all. Twisting both source and target preserves the
nilpotence obstruction just proved. This tracks the twist rather
than treating a numerical inverse power of$2\pi i$ as a
weight-preserving morphism.

The full real K2 projection supplied by the compact cup/trace is
compatible with this result: its target is a degree-one extension
with bottom $H^1(E,\mathbb R(2))$ and square-zero Deligne operator.
It does not by itself carry the quadratic operator in(4.2) or
the cubic operator in(7.5).

This rules out only a literal framed MHS transport from that
relative Deligne extension to the completed determinant tensor.
It does not prove that $\mathcal C_{j_2}$ has no rational motivic
preimage, nor that no different coefficient extension or secondary
operation can compare their evaluations. An arithmetic comparison
along this route must construct and justify the additional
extension data or an operation beyond the maps(7.4); it cannot
be obtained solely by naming the two real values equal.
