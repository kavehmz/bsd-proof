# An actual weighted adjoint for the Kudla–Millson Eisenstein family

Date: 2026-09-12. Owner: root/coordinator. All six sections passed
[independent review](review-weighted-theta-adjoint.md).
Full BSD remains unresolved.
Restart: [checkpoint](weighted-theta-adjoint-checkpoint.md).

This constructs an analytic operation for the original weighted integral,
not an inverse of the theta lift on every function. Its test domain is the
rapidly decreasing, mean-zero scalar functions. Pointwise theta integrals
in the opposite direction need not converge; that issue is kept explicit.

## 1. Fixed measures, two Eisenstein normalizations and the original input

Let N=389, Gamma=Gamma_0(N), and Y=Gamma\H. Use the effective measure
$d\mu_z=dx\,dy/y^2$, and $d\mu_\tau=du\,dv/v^2$ on $SL_2(Z)\backslash H$.
Write $\Theta_L(\tau,z)=\theta_L(\tau,z)d\mu_z$ for the ACTUAL kernel of
[Du–Yang1702.07917v2](https://arxiv.org/pdf/1702.07917v2), (2.3)–(2.7).
The lattice and positive-line vector are
\[
 L=\left\{\begin{pmatrix}b&-a/N\\c&-b\end{pmatrix}:a,b,c\in Z\right\},
 \quad Q(A)=N\det A,\quad
 w(z)=\frac1{\sqrt N y}\begin{pmatrix}-x&|z|^2\\-1&x\end{pmatrix}.
\]
Set $p_A(z)=(A,w(z))$, and $q_z(A)=(A,A)_z$, the positive majorant.
Thus $q_z(A)=p_A(z)^2-2Q(A)$ and the scalar kernel is
\[
 \theta_L(\tau,z)=\sum_{A\in L^\sharp}
 \left(vp_A(z)^2-\frac1{2\pi}\right)
       e^{-\pi vq_z(A)}e^{2\pi i uQ(A)}e_{A+L}.              \tag{1.1}
\]
The zero-vector term is $-e_0/(2\pi)$. This form of (1.1) combines
both exponentials in the source; it does not change its Gaussian.

Put $E_\infty(z,s)=\sum_{\Gamma_\infty\backslash\Gamma}\Im(\gamma z)^s$,
where the cusp stabilizer contains minus the identity, so its leading
term at infinity is $y^s$. Let $E_0(z,s)=E_\infty(w_Nz,s)$, using
the width-one Fricke scaling. The completed source is exactly
\[
 J_N(z,s)=b_N(s)E_\infty(z,s),\qquad
 b_N(s)=\xi(2s)(N^{2s}-1),\quad
 \xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).                      \tag{1.2}
\]
Write $J_N^+=(J_N+J_N\circ w_N)/2$.

For the metaplectic Poincaré series define $\mathbb E_L(\tau,s)$ using
the FULL inverse-image stabilizer of infinity, with seed
$v^{(s-1)/2}e_0$ and the source's weight3/2 slash operator. Its leading
coefficient is ONE. In Du–Yang's raw series $E_L^{DY}$ that coefficient
is TWO:
\[
 E_L^{DY}(\tau,s)=2\mathbb E_L(\tau,s),\qquad
 \mathcal E_L(\tau,s)=a_N(s)E_L^{DY}(\tau,s),\quad
 a_N(s)=-\frac{s}{4\pi}b_N(s)N^{(1-s)/2}.                  \tag{1.3}
\]
The second formula is exactly their (1.6), since
$b_N=N^{2s}\pi^{-s}\Gamma(s)\zeta^{(N)}(2s)$.
The factor two in the first formula is not a stack-degree adjustment.
In their proof of Theorem1.4, the sum over primitive bottom rows
$(c,d)$ is over BOTH signs before it is rewritten as their metaplectic
coset sum. The combined slash action of the central lift of minus the
identity fixes the seed $e_0$. Thus both signs give the same summand,
whereas the full stabilizer in $\mathbb E_L$ identifies them. The two
lifts above a fixed matrix act identically under the combined slash.

For a direct normalization check, the zero-frequency one-dimensional
Gaussian in that Poisson computation has
\[
 \sum_{a\in Z}\left(t a^2-\frac1{2\pi}\right)e^{-\pi t a^2}
       =-t^{-3/2}\sum_{n\ne0}n^2e^{-\pi n^2/t}.
\]
With $t=v/(Ny^2)$, its Mellin integral with $y^{s-2}dy$ gives
$-sN^{(1-s)/2}\xi(s)v^{(s-1)/2}/(2\pi)$: the sum over $n\ne0$
contributes both signs. The source's forward coefficient is
$-sN^{(1-s)/2}\xi(s)E_L^{DY}/(4\pi)$, confirming the leading TWO.
Equivalently at s=1, $a_N(1)=-(N^2-1)/24$, and the degree/zero-vector
formula gives constant term $-(N^2-1)/12$ for $\mathcal E_L(\tau,1)$.
All subsequent pairings retain (1.3).

The original input from the [reviewed projection note](theta-elliptic-projection-attack.md)
is $F=y^2 f\overline g$, where
$g=(2\pi i)^{-1}d\log(N^{-6}\Delta(z)/\Delta(Nz))/dz$.
It is Fricke even and rapidly decreasing in the hyperbolic height at
BOTH cusps. The proved scalar identities are
\[
 \int_YF\,d\mu_z=\int_YFj_0\,d\mu_z=\int_YFj_1\,d\mu_z=0,
 \quad \int_YFj_2\,d\mu_z=\mathcal M
 =-\frac{3N(N-1)}{2\pi^3}\ell L(E,2)\ne0,                 \tag{1.4}
\]
where $j_i$ are the Laurent coefficients of $J_N(z,1+t)$ and
$\ell=L''(E,1)/2$. These are completed inputs, not new calculations.

## 2. The mean-zero theta lift is rapidly decreasing in the other variable

Let h be a smooth Gamma-invariant function with, at both cusps,
$|h(x+iy)|\le C y^B e^{-cy}$, and with $\int_Yh\,d\mu_z=0$.
All fixed derivatives of the present F also satisfy such bounds in
uniformizing coordinates. Put
\[
 H(\tau)=I_L(\tau,h)=\int_Yh(z)\theta_L(\tau,z)d\mu_z.
\]

**[NEW] Lemma2.1.** Uniformly for $|u|\le1/2$ and $v\ge1$, H and
any fixed number of its tau derivatives have a bound
$C v^B\exp(-c v^{1/3})$, with possibly different constants.
In particular its Petersson pairing with every fixed Laurent
coefficient of the Eisenstein family converges absolutely.

*Proof.* Subtract the zero-vector term using the exact mean-zero
condition BEFORE estimating:
\[
 H(\tau)=\int_Yh(z)\sum_{A\ne0}
 \left(vp_A^2-\frac1{2\pi}\right)e^{-\pi vq_z(A)}
             e^{2\pi iuQ(A)}e_{A+L}\,d\mu_z.               \tag{2.1}
\]
Since $p_A^2\le2q_z(A)$, the polynomial factor can be absorbed into
a Gaussian with a smaller positive exponent. In a standard cusp strip
of height y, a fixed lattice-coordinate Euclidean norm satisfies
$q_z(A)\ge c\|A\|^2/y^2$. This follows directly by conjugating with
the upper triangular matrix carrying i to z: its adjoint and inverse
have norm bounded by a constant times y on a bounded x-strip.
On the compact core there is a uniform positive lower bound instead.
The same estimates hold at the other cusp by Fricke conjugation of L.

The resulting lattice sum is bounded by $C(1+y/\sqrt v)^3$; when
$y\le Y$ and $v/Y^2$ is large, excluding A=0 improves it to
$C\exp(-cv/Y^2)$ times a harmless polynomial. Split Y into its
compact-height portion y≤Y and the two tails y>Y, taking
$Y=v^{1/3}$. The first part has bound $C\exp(-cv^{1/3})$.
On the tails the polynomial lattice bound and the assumed decay
of h give $Cv^B\exp(-cY)$. All integrations include $dy/y^2$.
Tau derivatives only introduce fixed additional polynomials in
v, $Q(A)$ and $q_z(A)$, which the same Gaussian absorbs.
This proves the statement, without equating algebraic-cusp smoothness
with hyperbolic decay. The known Eisenstein coefficients have
polynomial/logarithmic cusp growth, so their pairings converge. ∎

## 3. The actual isotropic sum and its Mellin integral

At prime N the only isotropic discriminant coset is zero: if
$Q(\mu_r)=-r^2/(4N)$ is integral, then $2N\mid r$. Hence the
constant Fourier coefficient of the zeroth component in (2.1) is
\[
 H_0(v)=\int_Yh(z)\sum_{\substack{0\ne A\in L\\Q(A)=0}}
 \left(vp_A(z)^2-\frac1{2\pi}\right)e^{-\pi v p_A(z)^2}d\mu_z.
                                                                    \tag{3.1}
\]
Here $H_0(v)=\int_0^1H_{\mu_0}(u+iv)du$.

**[NEW] Lemma3.1.** For real part s>1,
\[
 \sum_{\substack{0\ne A\in L\\Q(A)=0}}|p_A(z)|^{-s}
      =2\zeta(s)N^{s/2}\big(E_\infty(z,s)+E_0(z,s)\big).  \tag{3.2}
\]

*Proof.* Every rational isotropic line corresponds to a rational cusp.
For prime N there are exactly the two Gamma-orbits infinity and zero.
The primitive generators in the displayed lattice on those lines are
\[
 A_\infty=\begin{pmatrix}0&-1/N\\0&0\end{pmatrix},\qquad
 A_0=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
Their stabilizers are the cusp stabilizers. Conjugation by Gamma
preserves lattice primitivity. Every nonzero isotropic vector is
therefore a UNIQUE nonzero integer multiple of one of these
primitive orbit vectors, after choosing one of the two signs.
The signed multiples give $2\zeta(s)$, with no averaging.
Direct calculation gives
$|p_{A_\infty}(z)|^{-s}=N^{s/2}y^s$ and
$|p_{A_0}(z)|^{-s}=N^{s/2}\Im(w_Nz)^s$.
Equivariance proves (3.2), including the width-one scaling at zero. ∎

For any fixed nonzero isotropic A and real part s>0, elementary
Gamma integration gives
\[
 \int_0^\infty v^{s/2-1}
 \left(vp_A^2-\frac1{2\pi}\right)e^{-\pi v p_A^2}\,dv
 =\frac{s-1}{2\pi}\pi^{-s/2}\Gamma(s/2)|p_A|^{-s}.        \tag{3.3}
\]
Replacing the minus by plus inside the absolute value yields the
same sort of bound with a finite constant on any compact s-strip.
By (3.2), the sum of those bounds paired with |h| is finite for
real part s>1: the scalar Eisenstein series has only polynomial
cusp growth and h is exponentially small. Thus all exchanges of
v-integration, the isotropic sum and z-integration in (3.1)–(3.3)
are justified by absolute convergence in that region.

## 4. The genuine weighted adjoint identity

Use the sesquilinear Petersson convention linear in the first entry.
For analytic dependence on s define
\[
 \mathscr P_h(s)=\int_{SL_2(Z)\backslash H}
 \sum_\mu H_\mu(\tau)
        \overline{\mathcal E_{L,\mu}(\tau,\overline s)}
                          v^{3/2}\,d\mu_\tau.             \tag{4.1}
\]
This is an ordinary absolutely convergent integral wherever the
Eisenstein family is finite, by Lemma2.1. It is meromorphic in s.
The bar on s in (4.1) is essential; it makes the formula linear
and holomorphic in the chosen parameter. The scalar $a_N$ satisfies
$\overline{a_N(\overline s)}=a_N(s)$.

**[NEW] Theorem4.1.** On the above mean-zero rapidly decreasing test
space, and by meromorphic continuation,
\[
 \boxed{\mathscr P_h(s)=r_N(s)\int_Yh(z)J_N^+(z,s)d\mu_z,\qquad
 r_N(s)=-\frac{\sqrt N}{\pi^2}s(s-1)\xi(s).}              \tag{4.2}
\]
For Fricke-even h, $J_N^+$ can be replaced by the ORIGINAL $J_N$.

*Proof.* Start with real part s>2, so the raw metaplectic Poincaré
series is absolutely convergent. Its full-stabilizer version unfolds
against the modular H with seed $v^{(s-1)/2}e_0$. The Petersson factor
$v^{3/2}$ and measure $du\,dv/v^2$ give exactly $v^{s/2-1}du\,dv$.
The source's raw series has the factor TWO in (1.3). Therefore
\[
 \mathscr P_h(s)=2a_N(s)\int_0^\infty v^{s/2-1}H_0(v)dv. \tag{4.3}
\]
Absolute unfolding can also be checked using boundedness of the
invariant norm $v^{3/4}\|H(\tau)\|$ on a fundamental domain; at the
bottom of the strip real part s>2 is sufficient. Use (3.1)–(3.3):
\[
 \int_0^\infty v^{s/2-1}H_0(v)dv
 =\frac{s-1}{\pi}N^{s/2}\xi(s)
              \int_Yh(E_\infty+E_0)d\mu_z.
\]
Insert (1.3) and $b_N(E_\infty+E_0)=2J_N^+$ to obtain exactly
(4.2). Both sides continue meromorphically by the known Eisenstein
continuations and rapid test-function bounds. Fricke change of
variables proves the last claim. ∎

This is an actual adjoint as a functional on mean-zero test functions,
or equivalently modulo constant functions on Y. At a fixed z the
opposite theta integral contains its zero-vector term and diverges
at large v in the initial half-plane. We have NOT interchanged an
unregularized pointwise divergent integral. Its problematic term
was annihilated by the exact mean-zero condition before unfolding.
The right side's possible pole at s=1 is a constant function and is
annihilated in the same way.

For the generalized Eisenstein family, the known forward theorem
$I_L(J_N(s))=\xi(s)\mathcal E_L(s)$ and (4.2) give the tested
adjoint-composition multiplier
\[
 -\frac{\sqrt N}{\pi^2}s(s-1)\xi(s)^2                    \tag{4.4}
\]
on its Fricke-even part, in this distributional sense. This is not
an inverse on all cusp or continuous spectral components, nor a
justification for multiplying two forward lifts without the multiplier.

## 5. Recovering the original nonzero mass with a second theta derivative

The scalar $r_N(s)$ is regular and nonzero at one, because
$(s-1)\xi(s)\to1$. In particular
\[
                        r_N(1)=-\sqrt N/\pi^2.           \tag{5.1}
\]
For the original F, (1.4) gives
$\int_YFJ_N(1+t)d\mu_z=\mathcal M t^2+O(t^3)$.
Differentiation of (4.2) is legitimate under its convergent pairing.
Consequently
\[
 \langle I_L(F),\mathcal E_L(1)\rangle_{3/2}=0,\quad
 \langle I_L(F),\mathcal E_L'(1)\rangle_{3/2}=0,
\]
\[
 \boxed{\mathcal M=-\frac{\pi^2}{2\sqrt N}
       \langle I_L(F),\mathcal E_L''(1)\rangle_{3/2}.}     \tag{5.2}
\]
There is no omitted factorial: the second derivative is twice the
coefficient. The lower derivatives of $r_N$ multiply the known zero
lower pairings. In particular the right pairing is NONZERO, and so
$I_L(F)$ itself is nonzero. Its exact value is
\[
 \langle I_L(F),\mathcal E_L''(1)\rangle_{3/2}
       =\frac{3N^{3/2}(N-1)}{\pi^5}\ell L(E,2).           \tag{5.3}
\]
This is compatible with the entire theta POINT projection being zero.
The lift retains real metric/curvature data beyond that projection.

The preceding forward lift of the unpaired $j_2$ had a third
Eisenstein derivative because the factor $\xi(s)$ had a pole.
The actual adjoint for this mean-zero weighted pairing instead has
its pole canceled by the isotropic Mellin factor s-1. Thus (5.2)
uses the SECOND derivative, not the forward third-derivative combination.
Both statements keep their own exact operations and are consistent.
Multiplying the scalar source by the old Gamma completion does not
change this weighted second coefficient because the lower pairings vanish.
It still changes the unpaired forward series, as previously recorded.

## 6. The arithmetic operation that remains

The [previous cutoff theorem](theta-elliptic-projection-attack.md) gives
$I_L(F)$ as the limit of actual pairings
$\langle\widehat\phi_L,a(2\chi_\epsilon\Re F)\rangle_{GS}$,
with its source measure and no cusp or elliptic-point atoms.
It does not give a single smooth arithmetic class $a(2\Re F)$.
Equation(5.2) supplies the previously missing ANALYTIC weighted adjoint
on the required Eisenstein family. It does not promote those real
metric test functions to rational motivic data.

In particular the nonzero Petersson pairing with $\mathcal E_L''(1)$
has not been expressed as a rational arithmetic height, a primitive
integral cycle or a determinant of rational points. The known Hodge,
vertical and degree formulas supply only the zero-th and first
Eisenstein derivatives, against which this input pairs to zero.
The tested genus-two face also supplies only those lower derivatives.
Another secondary operation is still needed for this second derivative.

**[GAP WTA-389].** Construct an arithmetic operation on the actual
Kummer forcing source, the theta cycle and an arithmetic realization
of the adjoint second-derivative test that yields ONE rational class
in $D_{pt}\otimes Q\beta_2\otimes Q(1)^{-2}$ whose real evaluation
is the number in (5.2), with all finite places, full real period,
covering degrees and Tate normalizations retained. Its coefficient
must then be $6N(N-1)n_E$ as a conclusion. The beta2 arithmetic
extension is already available. The real scalar in (5.2) cannot
be used to define the desired rational class.

The separate adversarial review verified all new deductions, including
the raw Eisenstein factor two, simultaneous convergence, the isotropic
orbit multiplicities and the derivative order in (5.2).
No numerical certificate was rerun. The source kernel and normalization
were read directly in the 52-page Du–Yangv2 and its cached primary PDF
/tmp/harmonic-du-yang.pdf. The Kiefer general orthogonal-lift paper
was inspected as context, but no theorem from a different signature
is imported into this direct calculation.
