# Independent review of the CM cyclotomic p-unit pairing

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. Own only this review file for the current audit.

**PASS for all nine sections of [the corrected proof](cm-cyclotomic-pairing-attack.md).**
The requested integral-symbol and chosen-lattice clarifications have
been inspected directly. No formula changed and no correction remains.
The checkpoint's initial and superseded character-construction snapshots
can now be marked historical or replaced by the completed status.

Reviewed proof SHA256:
`3a22ad8a684e9b9e9431bef0de721c391878aa406489a8574cfd5dd708581262`.
Reviewed checkpoint SHA256:
`658312ad742bba186e2343e6752f87a004f9b823407fdc65fcca157ef8b1481a`.
Later review links and status edits are editorial. No old numerical
or arithmetic computation was rerun.

## 1. Actual ray fields, unit input and degree

The conductor is prime to the stated good split $p$, and its residue
group detects all four Gaussian units. Since $K=\mathbb Q(i)$ has
class number one, the kernel of ray reduction from
$\mathfrak f p^{r+1}$ to $\mathfrak f p^r$ is the product of the
two split principal-unit quotients, each of order $p$. A global unit
in this kernel would be one modulo $\mathfrak f$ and hence would
be the identity. Thus the field degree is exactly $p^2$ for every
$r\ge1$, not merely eventually.

The raw theta value is a global unit because this modulus has at
least two distinct prime divisors. This is the actual statement in
Schmitt Remark 2.4(ii), not a conclusion inferred solely from its
norm to $L_r$ being a unit. His distribution used in §3.2 and the
system of Definition 3.12 have the required increasing-prime-power
norms. Each of the two steps here removes an exponent at least two,
so no new-prime Euler factor occurs; the torsion argument is multiplied
successively by $\pi$ and $\bar\pi$, whose product is $p$.
Consequently $NU_{r+1}=U_r$ with the already fixed twelfth power.
Source: [Schmitt, Acta Arith. 171 (2015), §§2.2–3.3](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf).
His prime-power-conductor comparison theorem is not being applied to
the present conductor.

The cyclotomic field has degree $\varphi_r$ over $K$: the quadratic
field $K$ and the cyclotomic field are disjoint, as their finite
ramification sets are disjoint for odd $p$. The norm-residue character
on the ray kernel is onto the order-$p$ cyclotomic kernel, using
$(1+p^r,1)$ in its two split factors. Thus every cyclotomic conjugate
of $1-\zeta_{r+1}$ occurs $p$ times in the degree-$p^2$ ray norm.
The displayed cyclotomic polynomial identity gives exactly
$Nv_{r+1}=v_r^p$.

## 2. The finite p-boundary and centering

For every primitive conjugate, $(1-\zeta^b)/(1-\zeta)$ and its
inverse are integral geometric sums. These are units. Their product
identity is $\prod_b(1-\zeta^b)=p$, so
$\varphi_r\operatorname{div}(v_r)=\operatorname{div}(p)$ after
extension to $F_r$. This proves
$\operatorname{ord}_w(v_r)=e(w/p)/\varphi_r$ at $w\mid p$ and
zero elsewhere. The divisibility implicit in this integer is supplied
by the cyclotomic subfield.

Norm transitivity gives $N_{F_r/K}v_r=p^{D_r/\varphi_r}$.
The theta norm is a Gaussian global unit and hence lies in $\mu_4$.
It follows that $w_r=v_r^{\varphi_r}/p$ is an actual global unit.
The two centered norm formulas follow without division in finite
coefficients:
$$Nw_{r+1}=w_r^{p^2},\qquad
N([v_{r+1}]-[p]/\varphi_{r+1})
 =p([v_r]-[p]/\varphi_r).$$
Consequently the rational normalization $p^{1-r}[v_r]$ is norm
compatible. Its growing $p$-power denominators are correctly retained;
neither $p$ nor $\varphi_r$ is treated as invertible modulo $p^m$.

Centering does leave the analytic pairing unchanged, because the
mean theta logarithm is zero. At infinity the subtracted logarithm
is $\log p/\varphi_r$; at $p$ the chosen logarithm of $p$ is zero.
This identity of period functionals does not remove the integral
valuation or Kummer class of $p$.

## 3. Reference-independent determinant and exact covariance

For an arbitrary two-by-two matrix $C_v$, expanding its diagonal
translations shows that the only term involving both increments is
$xy$. The four-term difference in (9) is therefore exactly
$\ell_v(U_r)\ell_v(v_r)$, with coefficient one. It uses the actual
coefficient-one Kummer translations and retains the local reference
$C_v$; it never imports the unproved local normalization $H_v/2$.
The ordinary signs and Tate factors of each log translation are the
ones already checked in the mixed-extension review.

Since $v_r\in C_r\subset L_r$, grouping the summed logarithms over
$L_r$ gives (11) exactly. Only normalized averages introduce
$[F_r:L_r]^{-1}$. Cohomological corestriction remains the norm/sum
without that denominator.

In a fiber of $p^2$ embeddings the two means are different:
$\bar X=p^{-2}\ell_v(U_r)$ and
$\bar Y=p^{-1}\ell_v(v_r)$. Expanding $XY$ around these means
gives the coefficient $p^{-3}$ and precisely the covariance in (13).
It also gives
$R_{r+1}-R_r=p^{3r}\operatorname{Cov}_r$ for the stated normalization.
If the second input is replaced by $p^{1-r}[v_r]$, then
$P'_r=p^{1-r}P_r$ and
$P'_{r+1}=p^{-4}P'_r+p^{-r}\operatorname{Cov}_r$.
Thus the stated change to $p^{-4}$ is correct. None of these
identities proves convergence or permits suppression of the covariance.
They are algebraic identities also over $\mathbb C_p$, where no
positivity is asserted.

## 4. Integral cup and the two-input norm formula

The corrected §5 starts with the integral symbol
$\{U_r,v_r\}\in H_M^2(F_r,\mathbb Z(2))$.
Its rationalization and its reduction/cycle class are different maps.
The latter gives the finite cup in (15); the former is not itself
reduced modulo $p^m$. This resolves the coefficient issue in the
initial draft.

The finite cup has degree two and twist two. The toric identity
$\varphi_r[v_r]=[w_r]+[p]$ gives (16) by bilinearity, retaining its
last term. Local Tate duality indeed pairs a representation with its
dual twisted by one. In particular its application to $\mathbb Q_p(2)$
has dual $\mathbb Q_p(-1)$, whose invariant space over a fixed finite
$p$-adic field is zero. That rational vanishing does not erase a
finite cup. Source: [Rubin, Euler Systems, I §4, Theorem 4.1](https://swc-math.github.io/aws/1999/99RubinES.pdf).

For the cup norm, the projection formula gives
$$\sum_{g\in G}\operatorname{Cor}(a'\cup gb')
 =\operatorname{Cor}(a'\cup\operatorname{res}\operatorname{Cor}b')
 =\operatorname{Cor}(a')\cup\operatorname{Cor}(b').$$
The two norm laws make the last term $p c_{r,m}$.
Removing the identity summand proves (17), including its sign.
No interchange of cup factors is made, so no graded sign is missing.
After localization one must use the entire semilocal algebra and
the sum of local corestrictions; the proof correctly does so instead
of assuming a fixed splitting pattern at a selected upper prime.

## 5. The exact ray involution and CM sign

The CRT class with residues one modulo $\mathfrak f$ and minus one
modulo $p^r$ is compatible as $r$ varies. Its square is the ray
identity. It is nontrivial: a global unit eliminating it would be
one modulo $\mathfrak f$ and hence one, contradicting its $p$-residue.
Thus it gives the claimed order-two element of the ray Galois
quotient. It is not an order-two element asserted in the absolute
Galois group, and is not complex conjugation; it fixes $K$.

The two residue components have product one, so its cyclotomic
action is trivial. Kato §15.8 has the cohomological action by the
inverse Hecke value; dualizing gives the Tate-module action.
For a principal ideal with generator one modulo the conductor, the
type-$(-1,0)$ Hecke value is that generator, and the conjugate
component is its conjugate. Both have residue minus one here.
Taking inverses or the inverse Artin convention retains that sign.
Therefore $\Psi,\Psi^c,\rho,\rho'$ all take the value $-1$ on
this compatible ray element.

The primary text was checked at printed pp.256–257 in
[Kato, Astérisque 295 (2004), §15.8](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
using the already cached PDF and its extraction after the web fetch
timed out. Cached PDF SHA256:
`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.
The conductor and arithmetic-Artin conventions in §15.7–15.8 were
retained, rather than replacing this element by an arbitrary Frobenius.

Because two is a $p$-adic unit, $(1\pm\tau)/2$ are actual integral
projectors on the completed unit module. They do not require choosing
an algebraic square root of a ratio. Norms commute with the compatible
ray action.

The unweighted period pairing is even by reindexing the embeddings,
since $v_r$ is fixed by $\tau$. Equivalently, grouping over $C_r$
gives (20). The finite CM-twisted map is odd: applying $\tau$ to
both Kummer factors multiplies the coefficient vector by $-1$, while
corestriction is invariant under the combined inner action of a lift
of $\tau$ to the target absolute Galois group. This proves (21).
The smoothing operator commutes with this action in the abelian tower;
all later maps are linear. The unique derivative extraction, where
its augmentation vanishes, is linear as well. Thus all signs in
(19) and their propagation to the framed map are correct.

This yields an obstruction to a proposed factorization of operators:
the ratio $U/\tau U$ has zero even period but twice the original
odd derivative. A factorization through those periods would force
that derivative to vanish. The note does not assume it is nonzero
or infer a BSD counterexample from this conditional conclusion.

## 6. Dual companion: separate trace and before-trace cup

The corrected companion coefficients are genuinely Tate dual:
$A_m\otimes B_m\simeq\mu_{p^m}$. With compatible bases,
$t_{\rho,m}\otimes t_{\rho',m}$ is the dual Tate vector of
character $\chi^{-1}$, fixed over $C_r$ when $r\ge m$.

For the separately traced companion, $\tau$ fixes $v_r$ and negates
its coefficient. Thus the corestricted class is equal to its own
negative, and is zero since two is invertible modulo $p^m$. This
argument retains the actual $p$-unit; it does not use $\log_p p=0$.

The cup before tracing is a different operation. Once the product
of coefficient vectors has been formed, its dual Tate factor descends
to $C_r$. Applying the projection formula there gives exactly (24).
For $U/\tau U$, its ordinary norm to $C_r$ is one, so the before-trace
cup also kills the odd theta component. Further trace or localization
preserves that zero. This does not claim equality with the cup of
the two separate traces in general.

Before finite insertion, the rational motivic product has type
$\operatorname{Ext}^2(k(-1),k(1))$, not an elliptic degree-one class.
The corrected text explicitly passes to the chosen integral lattice
of the source before pulling back along $t_{-1,m}$. No reduction of
a bare rational motive or invariant rational trivialization of
$k(-1)$ is asserted.

## 7. The derivative normalization is unchanged

All finite comparisons are used with
$r\ge\max(m,n+1)$, so the division field trivializes the necessary
torsion coefficients and contains the cyclotomic layer. Norming the
raw theta input to $L_r$ gives the exact old $e_r$ class with no
averaging denominator. The coefficient-one integral difference,
Kato smoothing factor
$12(a^2-\Psi^c((a))\bar\sigma_a)$,
Betti vector $2\operatorname{pr}_\rho(\gamma_E^+)$ and generator
logarithm $g_p$ remain unchanged.

The first-jet map has the same inverse action. Therefore its unique
cochain derivative is the already reviewed
$D(g)+c_\gamma(g)gv$, with the same plus sign and $H^0$-based
uniqueness. The local framed expression retains
$p/(2\#E(\mathbb F_p))$, $c_{\rm cmp,p}=(156i\Omega_p)^{-1}$,
$e_p=(1-\alpha^{-1})^2$ and the denominator
$4e_p\operatorname{Reg}_p$. The inverse remains restricted to its
indicated line when the point regulator is nonzero, with the undivided
identity otherwise. Extra Selmer directions are not removed by this
operator comparison.

The note has constructed the polarized determinant, the integral cup
and the properly dual finite companion, and has computed their norm,
boundary and character behavior. None gives the remaining rational
frame. If a frame satisfying its real condition is constructed later,
its rational coefficient will equal $n_E$ as a conclusion. No leading
formula, uniform Sha bound or full BSD result follows from the
present comparison of operators.
