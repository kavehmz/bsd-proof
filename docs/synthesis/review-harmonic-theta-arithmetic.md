# Independent review of the harmonic theta arithmetic construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file.
Reviewed [proof](harmonic-theta-arithmetic-attack.md) and
[checkpoint](harmonic-theta-arithmetic-checkpoint.md).

**PASS after the recorded frame, coefficient and source-version
precisions.** All seven sections are verified. No numerical formula
needed correction. The result is a construction and test of the
specified arithmetic components, not the missing rational BSD comparison.

Reviewed proof SHA256:
94321e7e1e1ec3bb2f548e9f73945de3f676cbf6f7aa6198cde8da5f056c39ce.
Reviewed checkpoint SHA256:
433ef6c35ab8bdba15b998566eb9f977c8c3b8073122145c7c328def58d8c809.
Subsequent PASS links and checkpoint status changes are editorial.

## 1. Harmonic insertion and all boundaries

The norm on the second lattice is explicitly the transported source
norm. Under a modular coordinate change its vectors acquire
$(cz+d)^{-1}$ while their normalized lengths remain unchanged.
Consequently the full sum with insertion $w^2$ has weight -2
and its product with f is a scalar. The polynomial is harmonic
in the two real coordinates; the identification is not with the
different rank-three orthogonal lattice used later.

Direct calculation gives
$$
 \bar\partial\frac{|mz+n|^2}{y}
       =-\frac{i(mz+n)^2}{2y^2}\,d\bar z.
$$
This holds with n/N in place of n as well. It gives the
positive $i\pi u/(2y^2)$ in the derivative of the Gaussian.
Wedging with $\alpha=c_\pi2\pi if\,dz$ and using
$d\bar z\wedge dz=2i\,dx\wedge dy$ gives
$-2i\pi^2c_\pi u fS_Nd\mu$.
Together with the integration-by-parts factor
$i/(16\pi^2c_\pi)$ this is exactly the factor 1/8
in (1.2), with positive sign.

The integrated construction's bounds apply to l alpha and
the differentiated theta kernel with only polynomial losses.
The subtraction of $(N-1)\chi(u)/u$ has zero z-derivative
and zero paired integral, rather than being removed from
an unpaired expression. Its differentiated remainder decays
at both heat ends. On the fine Borel-Serre cover, all
forms in the Stokes calculation are flat at both joint
heat/cusp boundaries, so the cusp terms vanish. No
integration by parts in u is being assumed. The integral
covering factor 1/194 remains the same as in the reviewed
relative construction.

The Mellin integral of the harmonic family is entire in s
for fixed z after the constant small-heat derivative has
vanished. In the absolutely convergent half-plane its
gamma integration gives (2.2), and differentiation gives
(2.3). The explicit base moment (2.4) checks as well:
the Kronecker finite part has derivative
$i\pi\bar E_2/12-i/(4y)$. Applying it to z and Nz
produces the coefficient $N^2\bar E_2(Nz)$ and the
retained curvature term $-(N-1)y/\pi$.
The second s-derivative is a radial logarithmic moment;
it has not been replaced by a change of integer weight.

## 2. The actual cyclic Kummer construction

The product in (3.1) is over the unordered nonzero pairs
in the cyclic subgroup, so it is a rational symmetric
function of their x-coordinates. Its divisor is
$(C\setminus0)-(N-1)[0]=[C]-N[0]$.
On the stated characteristic-zero Hodge-frame torsor
the short Weierstrass coordinate is defined. If the
differential frame changes by lambda, x changes by
$\lambda^{-2}$ and the product by
$\lambda^{-(N-1)}$. The final proof explicitly records
its Hodge weight N-1. This avoids claiming it is a
scalar unit downstairs without a frame or a base
divisor. Its fiberwise logarithmic derivative is
intrinsic in the stated sense.

For one pair,
$x(w)-x(a)=w^{-2}(1-x(a)w^2+O(w^4))$.
Logarithmic differentiation gives the pole -2 dw/w
and the coefficient $-2x(a)w\,dw$. Summing the
pairs proves (3.2), including its factor two.
The trace coefficient is a section of the square
of the Hodge line.

The degree-zero heat correction has small-u limit
N-1 and zero large-u limit; its s=1 pole cancels.
In the finite part of $N^sE^*(Nz,s)-NE^*(z,s)$,
the derivative of $N^s$ times the pole cancels
the extra $\log N$ from $\log\operatorname{Im}(Nz)$.
The result is $2N\log|\eta(z)/\eta(Nz)|$, or
$N\log|v_\eta|/12+N\log N/2$ with the given unit.
The constant is therefore fixed and correctly retained.

The harmonic moment follows by differentiation and equals
$-Ny^2\bar g/3$. The convergent Weierstrass differences,
or the regularized G2 difference, give
$\sum_{a\ne0}\wp(a)=-N\pi^2g/3$.
The area terms cancel because the correction has
degree zero. Dividing by the square of the Tate
frame changes its coefficient to Ng/12.

The exact paired family is
$\frac12(N^s-N)M_T(s)$. The first factor has
a simple zero at s=1 and $M_T$ has order two.
Its second paired jet is thus zero, also after
the gamma completion. The residual family is
exactly $(N-1)E^*(z,s)$. This conclusion is
about the second jet of the specified coherent
family; it does not assert that every possible
higher operation on that family vanishes.

## 3. Sprang's actual component and the exponent discrepancy

The primary versions checked are
[Sprang, arXiv:1802.04996v2, Theorems 5.8 and 6.1](https://arxiv.org/pdf/1802.04996v2)
and
[Sprang, arXiv:1801.05677v3, Theorem 4.2](https://arxiv.org/pdf/1801.05677v3).
The former temporary PDF and rendered printed pp. 31
and 35 were inspected directly. The latter supplies
the algebraic Eisenstein-Kronecker comparison at its
fixed integer indices.

The assumptions for the chosen specialization hold:
N=389 and D=5 are coprime, both torsion sections in
each summand are nonzero, and the N-torsion sections
avoid the removed D-torsion. On a full-level fine
cover they are actual sections; summing the entire
finite orbit permits rational descent by transfer.
This division by cover degree is rational and is
not declared integrally primitive.

There is a genuine source-display discrepancy:
printed p. 31 uses $D^{1-w}$ in the shorthand
D-variant definition, while the final reindexing
on p. 35 gives $D^{2-w}$. The latter is exactly
what the direct lattice calculation yields:
restricting to vectors divisible by D contributes
$D^{-w}$, multiplied by $D^2$.
The proof uses this direct calculation, consistent
with the explicit geometric specialization calculation,
rather than importing the contradictory shorthand.
It does not infer failure of the polylogarithm
construction from that display discrepancy.

Finite Fourier orthogonality in the cyclic
N-torsion sum gives
$G_2^*(z)-NG_2^*(Nz)=\pi^2g/3$.
At weight two the D-map permutes those nonzero
cyclic labels, so D=5 multiplies the trace by
$25-1=24$. The resulting form is
$8\pi^2g\,dw^2=-2g(2\pi i\,dw)^2$.
Under the declared Tate Kodaira-Spencer convention
this is exactly $-2[d\log v_\eta]$.
This is an actual degree-one de Rham component with trivial
symmetric-power coefficient. The final type clarification
correctly retains the motivic Kummer Tate twist Q(1);
it does not call that Tate-twisted coefficient weight zero.
This wording change from the earlier b692f394 revision
changes no class or formula. In particular,
changing its integer coefficient degree to one
or two changes both the symmetric-power system
and the modular weight. It is not the second
spectral derivative at the same weight.

## 4. Exact Du-Yang version, scalar input and Laurent extraction

The inspected temporary Du-Yang PDF is **v2**, 52 pages,
with arXiv header 4 February 2018, rather than v1.
The author corrected its source attribution and links
to [arXiv:1702.07917v2](https://arxiv.org/pdf/1702.07917v2).
This matters for the numbering of the normalization:
it is definition (1.6) in the inspected version.
The relevant Theorems 1.3–1.6, Proposition 2.2,
and Lemma 6.4 were read directly. No formula
needed to change with this citation repair.

The arithmetic hypotheses hold because N=389
is squarefree. The effective stack multiplicity
and normalized Petersson convention are retained.
Its scalar Eisenstein normalization is precisely
$$
 N^{2s}\pi^{-s}\Gamma(s)\zeta^{(N)}(2s)E_\infty
       =\xi(2s)(N^{2s}-1)E_\infty=J_N.
$$
Thus its full theta-lift identity gives (5.1)
with no adjustment. Proposition 2.2 gives
Gaussian decay $O(e^{-Cy^2})$ uniformly in
the cusp angle, so the Laurent coefficients
with their polynomial/logarithmic growth
can be integrated after subtraction of the
explicit pole.

The residue relation uses
$I_L(1)=2\mathcal E^{(0)}/(N-1)$,
so $R_NI_L(1)=\mathcal E^{(0)}$.
Coefficient extraction from $\xi(1+t)$
then gives exactly
$\mathcal E^{(3)}/6+\kappa\mathcal E^{(2)}/2
+a_1\mathcal E^{(1)}+a_2\mathcal E^{(0)}$.
The fully completed version uses the coefficients
of $\Gamma(1+t)\xi(1+t)$ and retains the cubic
gamma coefficient times the residue.
Equality of the original paired masses does
not justify dropping these unpaired lower terms.

## 5. The arithmetic Kronecker divisor and its vertical term

For the modular section
$A=\Delta(Nz)^N/\Delta(z)$, the source gives
weight $12(N-1)$ and divisor
$(N^2-1)\mathcal P_\infty-12N\mathcal X_N^0$.
The normalized Green component of one twenty-fourth
of its arithmetic divisor is
$-\log\|A\|_0/12$, using the squared-norm
arithmetic convention. Adding the forced constant
$(N-1)\kappa$ proves (5.6) with its exact
horizontal and vertical coefficients.

For $c=4\pi e^{-(\log4\pi+\gamma)/2}$,
$\log c=-\kappa$ and
$\widehat\omega_0=\widehat\omega_{\rm DY}
+a(\log c)$. Consequently
$$
 \widehat D_0=\frac{N-1}{2}\widehat\omega_{\rm DY}
                    +a((N-1)\kappa/2).
$$
Using the three source intersections in (5.7)
then gives
$$
 2\langle\widehat\phi,\widehat D_0\rangle
 =\mathcal E^{(1)}+\kappa\mathcal E^{(0)}
       -\frac{N\log N}{N-1}\mathcal E^{(0)} .
$$
The additional $N\mathcal X_N^0/2$ inside
the pairing cancels exactly the last term.
This verifies (5.8), including its factor two.
The vertical correction is necessary and is
not omitted from a purported archimedean
comparison.

## 6. The higher response and the exact limit of the tested span

On $v^{(s-1)/2}$ the displayed weight-3/2
Laplacian has eigenvalue $-s(s-1)/4$.
Slash invariance and the tau-independent
normalization preserve that eigenidentity.
At s=1 its first two derivatives are
$-1/4$ and $-1/2$.
It follows by repeated differentiation that
$\Delta_{3/2}^3\mathcal E^{(3)}
=6(-1/4)^3\mathcal E^{(0)}$, while
three Laplacians kill derivatives of
order at most two. The coefficient one-sixth
in either response therefore gives
$-\mathcal E^{(0)}/64$ exactly.
The value $\mathcal E^{(0)}$ is nonzero.

Two Laplacians kill the specific span
of $\mathcal E^{(0)},\mathcal E^{(1)}$
coming from the stated Hodge, vertical
and constant classes. Thus that span
cannot remove the higher response.
The assertion is not about every
arithmetic Chow class or every possible
theta construction.

The codimension-three vanishing has
also been made precise: it is in the
Q/R arithmetic Chow theory used here.
Integral modular-stack stabilizer torsion
is not covered by the elementary
dimension assertion. Ordinary triple
products in this stated setting do not
supply the higher response; a different
space or secondary operation would
need its own comparison theorem.

## 7. Remaining comparison and verification scope

The theta variable tau and its rank-three
kernel do not replace the original
newform f or the rank-two universal
elliptic heat lattice. The full f-weighted
pairing is still required. Even an
arithmetic realization of the lifted
higher derivative alone would not
automatically give its rational
factorization through the fixed
point-height determinant.

The rational K2 divisor line with
regulator $L(E,2)/\pi$ is correctly
treated as an established input.
The target line, Tate factor, full
real period and coefficient
$6N(N-1)n_E$ remain unchanged.
No primitivity, BSD rationality or
finite Sha conclusion is inferred.

Only this review file was written
for this audit. The author's own
precision fixes were inspected;
no old certificate, prime scan or
height computation was rerun.
The universal BSD objective and
GAP HT-389 remain open.
