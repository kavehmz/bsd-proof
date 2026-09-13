# Independent review of the CM motivic logarithm derivative

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. Own only this review file for the present task.

**PASS for all eight sections of [the construction](cm-motivic-derivative-attack.md).**
No mathematical correction is required. The checkpoint contains obsolete
initial-status and source-work instructions; its author has been notified
to make those historical or replace them with the completed review status.
The rational-frame gap must remain explicit.

Reviewed proof SHA256:
`855395f9cd86706b30a41b7270ce370914d72514fd871e0a1f517336d28b5827`.
Later review links and checkpoint status edits are editorial.
No old arithmetic, analytic or regulator computation was rerun.

## 1. Exact Sen operator and exclusion scope

The matrix convention is consistent. In basis $(T,1)$ the inverse
cyclotomic action is $1-c_\gamma(g)N$, with $N(1)=T$, $N(T)=0$.
Since $N^2=0$, its matrix logarithm is exactly
$-(\log_p\chi(g)/g_p)N$. Dividing by $\log_p\chi(g)$, or taking
the equivalent infinitesimal quotient by $\chi(g)-1$, gives
$\Theta_U=-N/g_p$. Its sign agrees with the inverse action and with
the coefficient coboundary later in (4).

In the specified convention $\Theta(\mathbb Q_p(1))=1$.
The covariant Tate module of an elliptic curve has Sen eigenvalues
$0,1$; it is the dual of its first étale cohomology, which explains
the sign relative to the geometric cohomological weights. Tensoring
differentiates to $\Theta_V\otimes1+1\otimes\Theta_U$. Diagonalizing
the Hodge–Tate factor therefore gives the two displayed nonzero
nilpotent blocks, at eigenvalues zero and one. Each has a one-dimensional
eigenspace, so the total Hodge–Tate invariant dimension is two, not four.
Restriction to a finite local extension leaves an open cyclotomic
image and does not change this infinitesimal nilpotent part.

The primary criterion and eigenspace formula were checked in
[Berger–Colmez, Ann. ENS 49 (2016), §1.2, Theorem 1.3 and Remark 1.4](https://www.numdam.org/item/10.24033/asens.2300.pdf).
Its zero-eigenspace formula applied to Tate twists gives exactly the
semisimple-integral-eigenvalue test being used. The geometric input is
[Faltings, p-Adic Hodge Theory, III Theorem 4.1, printed p.298](https://public.websites.umich.edu/~bhattb/almost_purity_2011/Faltings_-_p-adic-Hodge-theory.pdf),
for a smooth proper variety over the local characteristic-zero field
with a normal-crossing divisor removed.

Thus the literal coefficient representations cannot occur in the
specified Hodge–Tate geometric class or its sums, tensors, Tate twists
and subquotients. The proof does not assert that all extensions of
Hodge–Tate representations remain Hodge–Tate; indeed this example
shows why that would be wrong. It also does not infer that the derived
class $w_0$, an operation on cohomology, or every possible motive
producing its scalar is excluded.

## 2. The actual Kummer/logarithm motive

The Huber–Kings source has the required characteristic-zero smooth
commutative group objects and the triangle
$H_G\to K(s)\to\mathbb Q\to H_G[1]$. Its first logarithm is
the diagonal Kummer construction, compatible with pullback. For
$\mathbb G_m$ the subobject is $\mathbb Q(1)$; for the elliptic
curve it realizes its covariant Tate module. The number fields and
the open smooth curve used here satisfy the realization hypotheses.
The source's isogeny splitting is rational.
See [Huber–Kings, arXiv:1505.04574v1](https://arxiv.org/pdf/1505.04574v1),
Definitions 4.1.1, 4.2.1 and 4.3.1, Lemma 4.2.3, Remark 4.2.4,
Corollary 4.4.2, Proposition 4.6.1 and Lemma 6.4.1.

The finite pair description in the note independently fixes the
realization's sign. Addition is $(t,j)+(t',j')=(tt',j+j')$; the
relation $(t,j)\sim(tu^a,j+p^ma)$ preserves $t^{p^m}=u^j$.
The quotient is $\mathbb Z/p^m$, and its kernel is $\mu_{p^m}$.
The lift $(u_m,1)$ changes by the positive Kummer cocycle under Galois.
Hence $g e_0=e_0+k_u(g)e_1$, $g e_1=\chi(g)e_1$, and
$k_u(gh)=k_u(g)+\chi(g)k_u(h)$ as stated.

This extension has pure graded weights zero and minus two, with Sen
eigenvalues zero and one. Distinct eigenvalues make its Sen operator
semisimple. No change of basis can turn it into the repeated-eigenvalue
nilpotent operator of §2. Also
$\operatorname{Hom}_{G_F}(\mathbb Q_p(1),\mathbb Q_p)=0$ on a finite
local field, so the proposed equivariant Tate-for-trivial pushout is zero.
The $2\pi i$ and logarithm periods are correctly periods of this
different-weight extension, not invariant trivializations of its Tate piece.

For the elliptic Kummer motive the abelian subobject has rational rank
two and weight minus one. CM makes it rank one only after passing to
the CM coefficient component, not rank one as a rational Tate motive.
At a torsion point of order $d$, the rational Kummer class is killed
by $d$ and is zero; the isogeny splitting supplies the anchored
rational splitting. Nothing here proves integral splitting at primes
dividing $d$.

## 3. Pullback along the actual theta function, norm and twist

The function $\Theta_a$ is a rational morphism to $\mathbb G_m$ on
$E\setminus E[a]$. Pairing $U$ and $-U$ in its displayed product
checks its divisor:
$12((a^2-1)[O]-\sum_{U\ne O}[U])$.
This is exactly (9), with the factor twelve already present. Its
pullback of the first toric logarithm therefore exists on the stated
open curve, and evaluation at $R_r$ is precisely the Kummer motive
of the actual unit value. Coprimality with $a$ ensures the section
avoids the removed torsion divisor.

Norm compatibility is an identity of Kummer extension classes, not
an assertion that raw direct image of the whole rank-two motive
retains rank two. One can express it by first forming the section
of $\operatorname{Res}_{F/L}\mathbb G_m$ associated to $u$, then
using its norm morphism to $\mathbb G_m$. Equivalently use Shapiro
for the induced coefficient module and the norm/trace on that module.
The connecting map sends multiplication of sections to addition of
extension classes. Thus
$\operatorname{Cor}\delta(u)=\delta(Nu)$ with no further degree
or factor twelve. Complex logarithms obey the same identity modulo
their Betti periods, and $p$-adic logarithms obey it exactly with
the compatible embeddings.

The principal divisor residue has zero Abel–Jacobi class, while the
unit's Kummer class need not be zero. These have different coefficients
and are correctly kept separate. Likewise the torsion fiber of the
elliptic logarithm rationally splits without killing the toric unit class.

The twist also has the stated type. With
$R=M_\Psi(-1)$, its chosen realization is
$\rho=\Psi\chi^{-1}=(\Psi^c)^{-1}$, so tensoring the toric extension
gives an extension of $R$ by $M_\Psi$. Its pure weights are plus
one and minus one respectively. It does not produce an extension
of the trivial motive by $M_\Psi$. At a good place of a finite
number field, the other Tate-component Frobenius eigenvalue and its
positive powers have complex modulus greater than one, so its dual
has no invariant vector. A finite-level invariant torsion basis over
a division field is not an invariant rational basis at a fixed finite
field. This checks the coefficient insertion used later.

## 4. Quadratic logarithm and its explicit nullhomotopy

In the geometric basis $(e_0^2/2,e_0e_1,e_1^2)$, the symmetric-square
action has the prescribed logarithm and half-square entries. Its graded
pieces remain $\mathbb Q,\mathbb Q(1),\mathbb Q(2)$.
For the cochain $t(g)=-k_u(g)^2/2$ with target $\mathbb Q_p(2)$,
the differential is
$$\chi(g)^2t(h)-t(gh)+t(g)
 =k_u(g)\chi(g)k_u(h).$$
Expanding $k_u(gh)=k_u(g)+\chi(g)k_u(h)$ cancels both pure squares.
The remaining expression is exactly the cup product, including the
single cyclotomic factor in its second tensorand. This proves the
nullhomotopy in the correct coefficient module. Rational motivic
graded commutativity also kills the square of a degree-one class
when two is invertible. It is not a class in degree one with elliptic
coefficients; no such degree or twist change is made by the proof.

## 5. Finite cochain extraction and invariance

For $n\ge m$, the relation of the finite group ring is respected:
$(1+T)^{p^n}=1+p^nT=1$ modulo $(p^m,T^2)$. Its inverse Galois action
is exactly $1-c_\gamma(g)T$. Increasing $n$ commutes with the
group-ring projection and this map; no extra factor $p$ is a norm
normalization here.

The finite unit input, coefficient insertion before trace, Shapiro
identification, auxiliary smoothing inverse and rational Betti vector
match the already reviewed `cm-derived-unit-attack.md`. In particular
the note uses $12(a^2-\Psi^c((a))\bar\sigma_a)$ rather than the
opposite Schmitt factor and retains $2\operatorname{pr}_\rho(\gamma_E^+)$.
The denominator is a unit in the finite group algebra as well: its
augmentation is a $p$-adic unit, and the algebra of a finite cyclic
$p$-group modulo $p^m$ is local. Consequently (15) is the actual
reduction of $z_\infty$, with its previously proved integral divisibility.

The exact coefficient sequence (18) has the standard $M_m$ action
on both its submodule and quotient. Its map on $H^1$ is injective
because $H^0(G_{\mathbb Q,S},M_m)=E(\mathbb Q)[p^m]=0$. Vanishing
of the augmentation class gives existence of its unique preimage.
This proves uniqueness on cohomology, without assuming a Selmer rank.

The explicit cochain proof was checked independently. Write
$f=a+Tb$ and use the inverse action. The cocycle equation gives
$da=0$ and $db(g,h)=c_\gamma(g)g a(h)$. For $a(g)=gv-v$,
$$d_{B_m}v(g)=gv-v-c_\gamma(g)gv\,T.$$
Subtracting gives the plus correction $b(g)+c_\gamma(g)gv$.
Its differential is zero because
$$d(c_\gamma(g)gv)(g,h)=-c_\gamma(g)g a(h).$$

There is no unrecorded cochain-choice ambiguity. The choice of $v$
is unique since $H^0=0$. If $f$ changes by the coboundary of
$u+Tt$, then $a$ changes by $du$, $v$ by $u$, and $b$ by
$dt-c_\gamma(g)gu$. The corrected expression consequently changes
by just $dt$. This proves the asserted representative invariance
directly, in addition to the long exact sequence argument.

Reducing $z_\infty=Tw_\infty$ proves that the reduction of $w_0$
is this unique preimage. Hence the $d_m$ are compatible. The usual
inverse-limit cohomology sequence has no $\varprojlim^1H^0$ term
here, since all those invariant groups vanish; thus the compatible
family recovers the original integral $w_0$ exactly. No new finite-level
Selmer assertion is inferred. Its rational full-Selmer property is
the already established property of that inverse-limit specialization.

## 6. The precise frame comparison and remaining gap

Formula (20) agrees with the reviewed derived-unit formula (22)–(23).
When $\operatorname{Reg}_p\ne0$, the height matrix defines projection
onto the actual Mordell–Weil plane without asserting that plane is the
whole Selmer space. The nonzero logarithm vector makes
$\operatorname{adj}(H_p)l/g_p$ nonzero, and the proved height identity
puts the projected input on that particular line. Thus
$\mathcal B_p^{-1}$ means its inverse on its one-dimensional image,
not an inverse from the entire Mordell–Weil plane.

All scalar factors check against that input:
$k_\alpha e_p=\#E(\mathbb F_p)/p$, the first cyclotomic frame has
$g_p^{-1}$, and the Kato/Katz second coefficient contains the stated
$c_{\rm cmp,p}M_p/(2g_p^2)$. Multiplying by
$p/(2\#E(\mathbb F_p))$ gives precisely
$c_{\rm cmp,p}M_p/(4e_p\operatorname{Reg}_p)$.
The values $c_{\rm cmp,p}=(156i\Omega_p)^{-1}$ and the real target
$\ell_E/(2\Omega_E)$ are preserved from the reviewed normalization.
No inverse is asserted when the regulator vanishes.

The new construction supplies the finite classes and then recovers
the already existing $p$-dependent framed element. Its attempted
rational lift stops at exactly the distinctions actually calculated:
the toric norm gives the original unit boundary; the elliptic torsion
fiber splits; the quadratic boundary is zero in degree two; the CM
twist has quotient $R$; and the inverse cyclotomic coefficient has
the non-Hodge–Tate Sen block. These do not prove that a different
secondary operation cannot produce a rational framed element.

If the proposed $Z_{\rm alg}=q\Xi$ exists with the stated real
realization, then $q=\ell_E/(2\Omega_E\operatorname{Reg}_\infty)=n_E$.
Thus rationality is a conclusion of the missing comparison, not a
premise imported by defining an inverse real period. No finite Sha,
finite-level Selmer saturation, universal rank statement or full BSD
conclusion follows from this reviewed construction.
