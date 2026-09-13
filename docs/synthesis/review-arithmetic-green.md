# Independent review of the arithmetic Green comparison

Date: 2026-09-12. Reviewer: `/root/uniform_witness`, GPT-6 Astra/xhigh.
Reviewed [arithmetic-green-comparison.md](arithmetic-green-comparison.md)
and [its checkpoint](arithmetic-green-checkpoint.md).

**Result: PASS for the stated construction, identities, and limited
nonexistence claims concerning the literal candidates.** No mathematical
repair is required for the divisor, metric, theta-pairing, or point-projection
formulas. Two nonblocking presentation clarifications were sent to the
author: specify absolute convergence in Proposition 7.1, and keep its final
interpretation confined to the proposed representation rather than a
general impossibility claim. Stray commas in superscripts are cosmetic.

The review does not assert a nonzero elliptic regulator tensor, leading-term
rationality, integrality, or BSD. It also does not assert that the whole
arithmetic Chow class vanishes: only its stated degree-zero generic
Picard/Mordell–Weil projection does.

## 1. Source versions, model, and degree conventions

I read the following primary statements directly:

- Du–Yang, [arXiv:1702.07917v2](https://arxiv.org/html/1702.07917v2):
  §§4, 6.2–6.3, Proposition 3.4, Lemma 6.4, Theorems 1.3 and 1.6,
  and Propositions 8.2–8.3.
- Burgos Gil–Kramer–Kühn,
  [arXiv:math/0502085v1](https://arxiv.org/html/math/0502085):
  Theorems 2.15, 2.17, and 5.3.
- Sankaran–Shi–Yang,
  [arXiv:2206.05823v1](https://arxiv.org/pdf/2206.05823v1):
  the introduction, §2.1, and Theorem 2.14.

Du–Yang §6.2 explicitly specifies the regular proper flat DM stack of
cyclic isogenies of generalized elliptic curves at squarefree level.
The kernel is required to meet each geometric fiber component. It is
smooth away from $N$. For $p\mid N$ the two bad-fiber components meet
at supersingular points and are labeled by the corresponding cusps.
This is the model used in the note; it is not silently replaced by an
arbitrary regular coarse model.

The convention counting points by $2/|\operatorname{Aut}(x)|$ is explicitly
in that source. The note appropriately claims agreement with coarse
degree at the generic order-two stabilizer, not at every exceptional
stabilizer. In particular the rational cusp degrees and the ordinary
hyperbolic-volume normalization used in the curvature check are compatible.
Changing to the usual stack weight $1/|\operatorname{Aut}(x)|$ requires
changing the numerical normalization as well.

BKK's ring is rationally graded-commutative, and Theorem 2.17 requires a
projective arithmetic variety for its stated direct image. The note uses
Du–Yang's actual stack pairing for the modular calculation and treats BKK
as background for the log-growth formalism. That distinction must be
retained; BKK is not an automatic extension of every integral pushforward
to the modular stack.

## 2. The modular section and both vertical divisors

For prime $N$, the exponents in Du–Yang's generalized discriminant are
$a(1)=-1$ and $a(N)=N$. Hence its section is exactly
$$A=\Delta(Nz)^N/\Delta(z),\qquad k=12(N-1).$$
Direct use of $\Delta(-1/z)=z^{12}\Delta(z)$ with the determinant-normalized
slash action gives
$$A|_kW_N=N^{-6(N+1)}\Delta(z)^N/\Delta(Nz)=B.$$
The negative exponent of $N$ includes both the slash determinant factor
and the scaling in the discriminant transformation.

Substituting $k=12(N-1)$ and $r=N+1$ into Du–Yang Lemma 6.4 gives precisely
the two source divisors in equations (3.2)–(3.3) of the note. Their sum,
together with
$$AB=N^{-6(N+1)}(\Delta(z)\Delta(Nz))^{N-1},$$
gives
$$\operatorname{div}(\Delta(z)\Delta(Nz))
 =(N+1)(\mathcal P_\infty+\mathcal P_0)-12\mathcal X_N^0.$$
Adding the divisor of $N^6$ consequently gives the claimed product divisor
$$D_U=(N+1)(\mathcal P_\infty+\mathcal P_0)
                    +6(\mathcal X_N^\infty-\mathcal X_N^0).$$

Solving separately for the two ordinary discriminant sections gives
$$
\begin{split}
\operatorname{div}\Delta(z)&=\mathcal P_\infty+N\mathcal P_0,\\
\operatorname{div}\Delta(Nz)&=N\mathcal P_\infty+\mathcal P_0
                                      -12\mathcal X_N^0.
\end{split}
$$
Subtracting and adding $\operatorname{div}(N^{-6})$ gives the claimed
modular-unit divisor
$$D_v=(N-1)(\mathcal P_0-\mathcal P_\infty)
                    +6(\mathcal X_N^0-\mathcal X_N^\infty).$$
Thus both vertical signs and the coefficients six are correct. The
arithmetic principal relation includes these vertical terms and the
archimedean constant coming from $N^{-6}$.

I also checked these linear relations using exact Python `Fraction`
arithmetic at $N=2,3,5,389$. Each check passed. This verifies the displayed
algebra independently; no numerical period or BSD calculation was rerun.

## 3. Petersson normalization, curvature, and boundary currents

The section $s=N^6\Delta(z)\Delta(Nz)$ has weight 24. Its standard norm gives
$$
\log\|s\|_{24,0}
 =6\log N+24\log|\eta(z)\eta(Nz)|+12\log y=24U.
$$
Therefore its Green function is $-48U$, not $-24U$. It represents the
first arithmetic Chern class of the actual metrized Hodge power.

For the declared operator $dd^c=(i/2\pi)\partial\bar\partial$,
$$dd^c\log y=-\frac1{4\pi}\frac{dx\,dy}{y^2},\qquad
dd^cU=-\frac1{8\pi}\frac{dx\,dy}{y^2}.$$
The eta product is nonvanishing on the upper half-plane, so its absolute
logarithm contributes no interior curvature. Multiplication by $-48$
gives $(6/\pi)dx\,dy/y^2$ as claimed.

The cusp expansion has coefficient $(N+1)/24$ on $\log|q|$, coefficient
$1/2$ on $\log(-\log|q|)$, and constant
$\tfrac14\log N-\tfrac12\log(2\pi)$. The resulting divisor-current
coefficient in $dd^c[-48U]$ is $-(N+1)$ at each cusp; Poincaré–Lelong
therefore yields equation (4.3). Fricke invariance supplies the other cusp.
The hyperbolic area check gives curvature mass $2(N+1)$, matching the
horizontal divisor degree. The logarithmic and log-log coefficients are
within Du–Yang §4's stipulated singularity class.

## 4. Theta lift and arithmetic pairing constants

The normalized Du–Yang norm is exactly
$$\|F\|_{k,\rm DY}=|F|(cy)^{k/2},\qquad
c=4\pi\exp\!\left(-\frac{\log(4\pi)+\gamma}{2}\right).$$
No factor of $4\pi$ may be absorbed into the ordinary Petersson norm
without changing the constant term.

Re-expanding the sum of logarithmic norms independently gives
$$
\log\|A\|_{k,\rm DY}+\log\|B\|_{k,\rm DY}
 =24(N-1)U-12N\log N+12(N-1)\log c.
$$
Du–Yang Theorem 1.6 then yields
$$
I(U)=-\frac{\mathcal E_L'}{N-1}
 +\frac{1}{N-1}\left(\frac{N\log N}{N-1}-\log c\right)\mathcal E_L,
$$
with values at $s=1$. This is equation (5.4).

The metric change satisfies
$\widehat\omega_0=\widehat\omega_{\rm DY}+a(\log c)$, because the
squared weight-one norm increases by $c$. Substituting Theorem 1.3 gives
$$
\langle\widehat\phi,\widehat D_U\rangle
 =\frac{24}{N-1}\mathcal E_L'
 +\frac{24}{N-1}
       \left(\log c-\frac{N\log N}{N-1}\right)\mathcal E_L
 =-24I(U).
$$
Thus the coefficient $-24$, the metric-change sign, and the vertical
normalization all pass review. The theorem integrates a $(1,1)$-valued
theta kernel over the full modular curve; it is linear in $U$. It gives
an Eisenstein first derivative, not the fixed elliptic second derivative.

The supplemental genus-two citation also has the stated scope:
Sankaran–Shi–Yang assume $N>3$ odd squarefree and Theorem 2.14 uses a
first derivative at $s=0$, with scalar factor
$\prod_{p\mid N}(p+1)/24$. The note does not equate it with $L''(E,1)$.

## 5. The literal square and differential-form obstruction

Arithmetic codimension-one Green objects have type $(0,0)$ and their
arithmetic product has a type-$(1,1)$ Green current. Du–Yang's
cusp-regularized star product has evaluation, curvature, and explicit
boundary terms. It is not the pointwise product of two Green functions.
Its arithmetic degree integrates over the complex curve, whereas the
proposed $U^2\alpha$ is a one-form integrated along a relative real path.
The table in §4 correctly keeps these locations distinct.

The leading $(\log|q|)^2$ growth of $U^2$ cannot be removed by changing a
divisor, which changes a Green function only by linear logarithmic
singularities. It is outside the log-singular line-metric class being used.
This statement does not concern all arbitrary-current theories.

For $\alpha=2\pi if(z)dz$,
$$d(U^2\alpha)=2U\bar\partial U\wedge\alpha.$$
On an open set where $U\alpha\ne0$, identically vanishing right side
would force the real function $U$ to be holomorphic, contradicting its
nonzero curvature. For the real part, at $x=1/4$ the leading terms are
$U\sim-ay$, $dU\sim-a\,dy$, and
$\operatorname{Re}\alpha\sim-2\pi e^{-2\pi y}dx$, where
$a=\pi(N+1)/12$. Their wedge has leading coefficient
$4\pi a^2y e^{-2\pi y}$ on $dx\wedge dy$. This confirms the explicit
real nonclosedness argument.

Ordinary unramified $K_2$ regulator forms are closed with their stated
residue conditions, so the literal nonclosed form is not such a
representative. The note correctly leaves open a secondary construction
with additional terms or data; the degree check is not a universal
nonexistence theorem about arithmetic regulators.

## 6. Cuspidal torsion and the precise zero projection

The definition
$$\operatorname{AJ}_\infty(D,g)=[D_{\mathbb Q}-\deg(D_{\mathbb Q})\infty]$$
is well-defined in the rational Jacobian after the chosen degree
convention. Principal relations, vertical divisors, and metric changes
behave as claimed.

For $D_U$ the image is $(N+1)[0-\infty]$. The explicitly exhibited
modular unit already proves $(N-1)[0-\infty]=0$, so this is zero after
tensoring with $\mathbb Q$. The quotient's entire arithmetic class is
principal and therefore also has zero image. No analytic estimate or
conjecture is needed for this step.

At $N=389$ the image of $[0-\infty]$ in the elliptic curve is rational
torsion. The independently certified torsion group is trivial, so
$\pi(0)=\pi(\infty)=O$ integrally. Every degree-zero divisor supported
on the two rational cusps maps to zero. The claimed zero Gram
determinant for point classes obtained from these divisors follows.

This checks exactly the point-valued projection, and is compatible with
Du–Yang's separation of degree, vertical, Mordell–Weil, and metric pieces.
It does not annihilate the full arithmetic Hodge class or its nonzero
theta pairing, nor does it rule out correspondences using other cycles.

## 7. Added potentials, convergence, and review scope

For even $\rho,U,H$ and $u=U-t/2$,
$$
\rho\bigl((u+H)^2-(U+H)^2-(u^2-U^2)\bigr)=-\rho Ht.
$$
Under absolute convergence this is an odd integrable function and its
integral is zero. Likewise the remaining mixed term $-\rho Ut$ integrates
to zero, leaving $\tfrac14\int\rho t^2$. Proposition 7.1 therefore
passes, in particular for every compactly supported smooth even $H$.
The author was asked to specify this convergence convention explicitly.

The invariance is a property of the corrected path expression. By itself
it does not prove that every conceivable arithmetic interpretation must
use a particular sort of auxiliary data. The note's conclusions should
continue to concern the literal class, square, and projections that it
actually constructs; the residual AG-389 problem remains a substantive
unmet construction.

No existing numerical certificate was rerun in this review. At initial
review the SHA-256 digests were:

- Main note: `3dec7cb6cf3f0bd89c1f5b22663b0fd2b4d392f098cb195cd57335c2149c4997`.
- Checkpoint: `33a75211cbcb8bb5ee2d9c332b618f2451ded640702ea66f397e11f53598156c`.

The original author may incorporate the nonblocking clarifications; these
hashes identify the version whose displayed mathematical formulas were checked.
