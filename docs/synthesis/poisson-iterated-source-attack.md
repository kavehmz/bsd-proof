# A finite iterated-period formula for the canonical Poisson input

Date: 2026-09-13. Owner: root/coordinator.
All six sections completed with [independent PASS review](review-poisson-iterated-source.md),
including the single-valued cusp-remainder precision.
[Restart](poisson-iterated-source-checkpoint.md).
Full BSD over Q remains active and unresolved.

## 1. The exact input and the algebraic path data

Keep X=X0(389), Y=X minus its two cusps, E=389a1, and
$$
 \alpha=\pi^*\omega_E=c_\pi(2\pi i)f(z)\,dz,\qquad
 u=389^{-6}{\Delta(z)\over\Delta(389z)},\qquad
 \theta=d\log u,\qquad l=\log|u|.
 \tag{1.1}
$$
These are the fixed rational algebraic differential and modular unit.
Their normalizations are not changed. The
[completed Poisson theorem](theta-doubling-arithmetic-attack.md)
constructs a real function q_F with
$$
 dd^c q_F=\operatorname{Re}F\,d\mu,\quad
 q_F(0)=q_F(\infty)=0,\quad \int_Yq_F\,d\mu=0,
 \qquad dd^c={i\over2\pi}\partial\bar\partial.              \tag{1.2}
$$
It is bounded, smooth on Y, and has the proved O(q log|q|)
local form after its constant is removed. It is rapidly decreasing
in hyperbolic cusp coordinates. Existence of this function is an
INPUT, not a new theorem to be rerun.

We now give a finite formula from genuine algebraic path periods,
including the global corrections. We do not infer a rational
motivic morphism merely from that formula.

Choose a basepoint b in the REDUCED algebraic fiber
$$
                         B_2=(u^{-1}(2))_{\rm red}.       \tag{1.3}
$$
This is a specific nonempty finite étale Q-scheme: the nonconstant
rational map u:X→P1 is surjective, and neither cusp maps to2.
No L-value selects the fiber or a point in it.
Work initially over a number field containing b, with an embedding
in C. All its Galois-conjugate basepoints are retained when descending
the family of period data. Put L_b=log2.

We fix EARLIEST-FIRST word order:
$$
 I_{\eta,\xi}(\gamma)
     =\int_{0\le s\le t\le1}\gamma^*\eta(s)\gamma^*\xi(t)
     =\int_\gamma\left(\int_b^x\eta\right)\xi.
 \tag{1.4}
$$
Thus d I_{\eta,\xi}=A_\eta\,\xi on the universal cover.
All later signs follow from this equation. A reversed word
convention is not imported from another source.

**[THEOREM, geometric input]** For b≠z, the dual of the length-two
truncated path module is the actual relative cohomology
$$
 H^2\!\left(Y^2,\,
      (\{b\}\times Y)\cup\Delta_Y\cup(Y\times\{z\});\mathbb Q\right).
 \tag{1.5}
$$
For b=z, the corresponding group describes the augmentation ideal
modulo its third power; the constant line is handled separately.
This is [Looijenga2403.03748v2, Theorem1.1](https://arxiv.org/pdf/2403.03748v2),
the 13-page revision with arXiv stamp23June2024.
The path triangle (gamma(s),gamma(t)), oriented by ds wedge dt,
fixes our comparison with (1.4).
The algebraic de Rham/Betti and Hodge comparisons are
[Hain math/0109204v2, Theorems13.2,13.6,13.7](https://arxiv.org/pdf/math/0109204v2).
These apply to the actual affine curve and its algebraic forms;
no guessed rational structure on a transcendental connection is used.

For variable z away from B2, the pairs in(1.5), for all b in B2,
form a rational algebraic family with the endpoint and diagonal
subspaces displayed. Restriction of scalars/direct sum over the
finite basepoint scheme gives its rational realization over Q.
This statement concerns the PERIOD SOURCE, not rationality of
the real normalizing coefficients constructed below.

## 2. A finite de Rham representative of the conjugate differential

Let g be the genus of X and choose a rational basis
$\nu_1,\ldots,\nu_{2g}$ of H1_dR(X/Q), represented by meromorphic
second-kind differentials whose only possible pole is infinity.
One may take pole order at most 2g+1.
Indeed Riemann–Roch gives a quotient of dimension2g
$$
 H^0(X,\Omega_X((2g+1)\infty))/
                dH^0(X,\mathcal O_X(2g\infty)).
$$
The only possible residue is zero by the residue theorem.
Exactness of a form in this space forces its primitive to have
no other pole and the indicated smaller pole order, so this
quotient injects into H1_dR(X); dimension then makes it an
isomorphism. Equivalently use the algebraic de Rham comparison
on X minus infinity. This construction uses rational linear
algebra and keeps all genus-g directions.

Take a symplectic integral basis gamma_1,...,gamma_(2g) of H1(X).
Let P be the complete period matrix with entries integral_gamma_l nu_j,
and let a be the period column of alpha.
The integration pairing is nondegenerate. Define
$$
                 c=P^{-1}\overline a,\qquad
                 \rho=\sum_j c_j\nu_j.                    \tag{2.1}
$$
Then the periods of rho equal the complex conjugates of those
of alpha. Its cusp residues vanish. The coefficients c_j are
SPECIFIED comparison periods; they are not asserted rational.

On the universal cover of Y based at b put
$$
 A=\int_b^z\alpha,\qquad \widetilde A=\int_b^z\rho,\qquad
 L=\log2+\int_b^z\theta .
 \tag{2.2}
$$
Then Re L=l and $\overline A-\widetilde A$ is single-valued.
The latter follows because its increment around any loop is
$\overline{a_\gamma}-\int_\gamma\rho=0$, also for cusp loops.

## 3. The explicit length-two expression and its full monodromy

Define the real function on the universal cover
$$
 \Phi_b(z)=
 \operatorname{Re}\!\left(2l(z)A(z)
                  -I_{\alpha,\theta}(z)-I_{\rho,\theta}(z)\right).
 \tag{3.1}
$$

**[NEW] Proposition3.1.** It satisfies
$$
              dd^c\Phi_b=4\pi c_\pi\,\operatorname{Re}F\,d\mu.
 \tag{3.2}
$$
Its increment around a based loop gamma is the CONSTANT
$$
 C_\gamma=2\log2\,\operatorname{Re}a_\gamma
       -\operatorname{Re}\!\left(
            I_{\alpha,\theta}(\gamma)+I_{\rho,\theta}(\gamma)\right).
 \tag{3.3}
$$
These constants form an additive real character of pi1(Y,b).

*Proof.* Both iterated integrals are holomorphic locally on Y.
Also 2l A=AL+A barL and AL is holomorphic, so the curvature
of (3.1) is dd^c Re(A barL). Direct differentiation gives
$$
 dd^c\operatorname{Re}(A\overline L)
       ={i\over4\pi}
           (\alpha\wedge\overline\theta+\theta\wedge\overline\alpha).
$$
Using (1.1),
$\alpha\wedge\overline\theta=-8\pi^2i c_\pi F\,d\mu$.
This proves the EXACT scalar(3.2).

For a loop gamma followed by a path to z, Chen concatenation
in the order(1.4) gives
$$
 \begin{split}
 A&\longmapsto A+a_\gamma,\\
 I_{\alpha,\theta}
   &\longmapsto I_{\alpha,\theta}
            +I_{\alpha,\theta}(\gamma)+a_\gamma(L-\log2),\\
 I_{\rho,\theta}
   &\longmapsto I_{\rho,\theta}
            +I_{\rho,\theta}(\gamma)+\overline{a_\gamma}(L-\log2).
 \end{split}
$$
The z-dependent remainder in the increment of the expression
inside Re is $a_\gamma\overline L-\overline{a_\gamma}L$,
which is purely imaginary. Its real increment is (3.3).

Finally $\int_\gamma\theta\in2\pi i\mathbb Z$ because u is
single-valued. Applying concatenation once more shows that
the possible defect in additivity of(3.3) is the real part of
$(a_\gamma+\overline{a_\gamma})\int_\delta\theta$, hence iszero.
This proves the character assertion. $\square$

The character is not assumed to vanish. Dropping it would replace
the actual Poisson function by a multivalued expression.

## 4. Cusp corrections from a finite Riemann–Roch problem

Use the fixed rational formal coordinates at the two rational
cusps. Near a cusp c, write
$$
 A=A_c+a_c(q_c),\quad a_c(0)=0,\qquad
 L=m_c\log q_c+h_c(q_c),
$$
where $m_0=388$, $m_\infty=-388$.
The primitive tilde A is meromorphic there: rho has no residue.
It may have a pole at infinity, and is holomorphic at0.

Define the finite principal-part datum
$$
 s_c=\operatorname{pp}_c\!\left[
                    (\overline{A_c}-\widetilde A(q_c))\theta\right].
 \tag{4.1}
$$
It does not depend on the path used to reach the cusp, since the
changes of bar A_c and tilde A are the same conjugate period.

**[NEW] Lemma4.1.** The data(4.1) are the principal parts of an
actual global meromorphic differential xi_b, with poles only at
the two cusps. Such a differential can be chosen by a finite
Riemann–Roch linear system using those data.

*Proof.* Locally integration by parts rewrites(3.1) as the real
part of
$$
 A\overline L+\int L\alpha-\int\widetilde A\,\theta
 \quad\hbox{plus a constant}.
$$
The singular term from A_c barL has the same real part as
bar A_c L. The terms with a_c contribute
$m_c a_c(q_c)\log|q_c|^2$ and bounded regular terms.
Consequently Phi_b minus the real part of a primitive of s_c
is bounded and single-valued on the punctured cusp disk: its
remaining logarithm is log|q_c|², multiplied by a_c(q_c), and
the other terms are regular functions of q_c and its conjugate.
In particular the remainder is O(q_c log|q_c|) plus regular terms;
there is no leftover argument-of-q term.

To verify the global compatibility of these principal parts, use
the ALREADY PROVED existence in(1.2). The difference
G=Phi_b-4pi c_pi q_F is harmonic on the universal cover and
has constant monodromy. Thus 2partial G descends to a holomorphic
differential on Y. Locally, after subtracting a primitive of s_c,
the remaining real harmonic function is bounded and extends across
the puncture. Therefore 2partial G has exactly the principal parts
s_c. In particular their residues sum tozero.

The Mittag–Leffler/Riemann–Roch differential criterion now
constructs xi_b with those principal parts. Explicitly the finite
principal-part map on a space H0(X,Omega(D)) for a sufficiently
large cuspidal divisor D has image exactly the residue-zero data.
Its coefficients are obtained by linear algebra in rational
Riemann–Roch bases and the displayed s_c coefficients.
The proof used existence of q_F to verify compatibility; it does
NOT use a value, period or Green integral of q_F to choose xi_b.
$\square$

The last distinction is essential. This is a new formula for an
already constructed solution, not a new proof of Poisson solvability
from unproved algebraicity. All s_c coefficients are given by the
finite local expansions and ordinary regularized periods in(2.2).

## 5. The compact-period correction and exact cusp normalization

Set
$$
 \Phi_b^0=\Phi_b-\operatorname{Re}\int_b^z\xi_b .
$$
It is bounded at the cusps, with constant monodromy. Its character
$$
 C_\gamma^0=C_\gamma-\operatorname{Re}\int_\gamma\xi_b
 \tag{5.1}
$$
is zero on cusp loops by(4.1), so descends to H1(X,Z).

**[NEW] Lemma5.1.** There is a unique holomorphic differential
eta_b on X for which
$$
                 \operatorname{Re}\int_\gamma\eta_b=C_\gamma^0
                     \quad(\gamma\in H_1(X,\mathbb Z)).
 \tag{5.2}
$$
It is determined by a finite invertible real period matrix.

*Proof.* The real-linear map from H0(X,Omega) to real compact
periods is injective: if all real periods vanish, the real part
of an abelian primitive is a globally defined harmonic function
on the compact curve. It is constant, forcing the differential
tozero. Both spaces have real dimension2g, so the map is an
isomorphism.

For a rational holomorphic basis omega_j, with holomorphic period
matrix P_hol, write eta_b=sum_j(x_j+i y_j)omega_j. Equation(5.2)
is precisely the finite real system
$$
       [\,\operatorname{Re}P_{\rm hol},-\operatorname{Im}P_{\rm hol}\,]
                       \binom{x}{y}=(C_{\gamma_l}^0)_l.    \tag{5.3}
$$
The matrix is invertible by the preceding argument. $\square$

Define
$$
 U_b(z)=\Phi_b(z)-\operatorname{Re}\int_b^z(\xi_b+\eta_b).
 \tag{5.4}
$$
This is single-valued and bounded, and its finite limit at infinity
exists by the local expansion in Lemma4.1.
Its value there is the finite part of the explicit algebraic
iterated integrals and corrections in the chosen cusp coordinate:
all polar and logarithmic terms have been canceled first.

**[NEW] Theorem5.2.** The original canonical Poisson input is
$$
 \boxed{\displaystyle
 q_F(z)={U_b(z)-U_b(\infty)\over4\pi c_\pi}.}
 \tag{5.5}
$$
This formula is independent of b in B2, of the auxiliary rational
de Rham bases, and of the chosen solution xi_b to its principal parts.

*Proof.* The corrected function in(5.5) is single-valued, bounded,
has the curvature of q_F by Proposition3.1, and has cusp valuezero
at infinity. Its difference from q_F is a bounded harmonic function
on the punctured compact curve, hence extends and is constant.
The normalization at infinity makes that constant zero.
This also proves independence of every auxiliary choice.
The other cusp value and hyperbolic mean are therefore the already
known zero ones of q_F; they are not additional arbitrary conditions.
$\square$

Averaging (5.5) over the Galois-stable finite fiber B2 gives the same
function, and retains a rational family of underlying path pairs.
The averaging denominator is rational and is not asserted integral
or a unit at every prime.

## 6. What the geometric representation does and does not establish

The formula has only length-one and length-two VARIABLE path words
on the FULL modular curve. Its constants use finitely many ordinary
and length-two loop/cusp periods, rational Riemann–Roch linear algebra,
and the explicit real comparison matrices(2.1),(5.3).
Products of these period coefficients are retained.
This is not a claim that (5.5) is one rational linear combination
of length-two periods or one entry in an unmarked rational basis.

The actual rational sources are the path-pair cohomology(1.5),
its loop counterpart, and the original compact cohomology.
The Hodge and Betti comparisons are genuine. However taking
conjugates, solving the real normalization(5.3), and taking the
specified finite part have not been identified here with a
rational motivic morphism producing the BSD tensor.
In particular (5.3) is a PURE-CURVE real period normalization,
not division by the unknown point regulator or BSD quotient.

The genus-g correction eta_b must not be discarded by projecting
only to E. Its constants encode the monodromy of the actual
length-two periods around all compact cycles of X.
Similarly the period object uses Y itself; the previously tested
contractible pushed cusp loop on punctured E is a different source.

This representation supplies a finite iterated-period input for
the already exact arithmetic operation
$$
 \mathcal M=-{\pi\cdot388\over4\sqrt{389}}\,
                     \langle I_L(q_F),R_\omega\rangle_{\rm Pet}.
$$
The ordinary A_q/Hodge intersection iszero and cannot replace this
Petersson operation. No genus-two diagonal identity is assumed.

**[GAP PI-389].** Construct an arithmetic comparison from these
specified geometric path data and their exact normalizations,
together with the actual marked point coefficient source, to the
fixed point/K2/Tate determinant, retaining all finite and integral
frames and producing the coefficient6·389·388 n_E as a conclusion.
The real formula(5.5) and the rationality of its underlying path
pairs alone do not prove rationality or integrality of n_E.

No old certificate or numerical computation was rerun.
The existence and normalization of q_F are the reviewed inputs(1.2).
All six sections passed independent adversarial review. The finite real
formula is not promoted to the missing rational arithmetic comparison.
