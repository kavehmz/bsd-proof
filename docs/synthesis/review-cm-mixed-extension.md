# Independent review of the CM blended-extension construction

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. Own only this review file for the present audit.

**PASS for all ten sections of [the corrected proof](cm-mixed-extension-attack.md).**
The initial local/global reference identification required correction;
the saved final version separates the actual local block $C_v$ from
the global component $H_v/2$. It also makes coefficient-equivariant
lifts and the coefficient-one integral difference explicit. Those
repairs have been inspected directly. No correction remains outstanding.

Reviewed proof SHA256:
`30dd3934b267872465b352c189da939ef7565febd3083d0a46908439c7d6a5a4`.
Reviewed checkpoint SHA256:
`5506f8072c97fdfd67a200cc65fa51a2aa70f1f90d42b06cbb90989115b5b44c`.
Later review links and completed-status edits are editorial. No old
numerical or arithmetic computation was rerun.

## 1. Actual coefficient objects and the split pullback test

The pure objects satisfy $A\otimes B=k(1)$ and $R=B^\vee=A(-1)$
under the fixed polarization. Hence tensoring by $B$ carries the
proposed grades $A,k,R$ to $k(1),B,k$, with the genuine 1-motive
weights minus two, minus one and zero. The untwisted grades were
minus one, zero and plus one. The argument does not pretend that
this weight change is a trivialization of a Tate factor.

The point extension is pushed out along the pure abelian quotient
$H\to A$. The linear dual of the original point extension is then
pulled back along the pure injection $R\to H^\vee$. These are valid
maps of exact sequences. They do not require a geometric CM
endomorphism of a marked rank-one lattice fixing its point. The
$k$-coefficient action is obtained by coefficient extension and the
pure projectors; it is distinguished from such a nonexistent marked
CM action.

The simple fiber product $K_R(u)\times_RY_j$ restricts to $A\oplus k$
over $k\subset Y_j$: its map to $R$ is zero, so the first coordinate
lies in the fixed kernel $A$. The section $t\mapsto(0,t)$ is canonical.
Thus this pullback cannot realize a prescribed nontrivial lower
point extension. Proposition 2.1 has exactly the claimed scope.

## 2. Geometric blends and their coefficient action

The Poincaré description and Cartier duality were checked in
[Bertolin, arXiv:math/0402080v1, §1.2](https://arxiv.org/pdf/math/0402080):
the two lattice-to-abelian marking maps, together with a trivialization
of the pulled-back Poincaré biextension, define the 1-motive. Its
Cartier dual exchanges the two marking maps. This input does not
assert a general geometric construction of arbitrary tensor products
of 1-motives. The proof avoids requiring one by exhibiting the
constructed object after tensoring by the fixed invertible pure $B$.

The corrected construction first forms the lower semiabelian extension
as the Baer negative of the Cartier dual of $X_i$. Thus its $k$-action
already exists. For two lower directions, the fiber product over the
pure abelian $B$ retains that action and has a split torus. After
clearing the denominator of each upper marked point, its fiber is a
split-torus torsor over $K$, hence has a rational point. Choose lifts
of the free upper $k$-basis and extend with the existing action on
$G(K)\otimes\mathbb Q$. Clearing finitely many remaining denominators
gives a marking of an isogenous 1-motive. This justifies equivariance;
arbitrary completed fiber choices are not being assigned a CM action
afterward.

For fixed adjacent extensions and their maps, the Yoneda obstruction
and blend torsor assertions are exactly
[Bertrand, November 2010 author version, §1, Lemmas 1–2](https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/rpdf/Extpanaut_Nov10.pdf).
They are statements in an abelian category with the adjacent arrows
fixed. The later self-duality and rigidity hypotheses in that paper
are not needed or claimed here. Geometric trivialization changes form
the explicit Kummer subgroup; the proof does not identify every
extension in an unspecified larger category with that subgroup.

## 3. Dual sign, projected cup and matrix equation

Dualizing the matrix of the $B$-point extension gives the off-diagonal
entry $-b_j(g)b(g)^{-1}$. Normalizing by the quotient character
$r(g)=b(g)^{-1}$ leaves $y_j=-b_j$, proving (6). Equivalently, the
minus sign is the dual-extension identity in Bertrand's Lemma 5(i).

The projected obstruction can be checked directly. The two Weil cups are
$$C(P_i,P_j)=x_i\cup b_j-b_i\cup x_j,$$
$$C(P_i,iP_j)=-i x_i\cup b_j-i b_i\cup x_j.$$
Their stated half-sum isolates $x_i\cup b_j$. These are identities
of normalized cochains, including the Galois action on the second
factor. Ordinary geometric Poincaré blends provide the required
nullhomotopies; the construction does not infer motivic Ext-squared
vanishing from a possibly nonfaithful étale comparison.

Multiplying the two block matrices in (9), then dividing the
upper-right block by $r(gh)$, gives
$$Z(gh)=Z(g)+\chi(g)Z(h)+x(g)b(g)y(h).$$
Thus $dZ=-x\cup y=x\cup b_j$, with central coefficient
$a/r=\chi$. The other two off-diagonal equations are the cocycle
identities for $x$ with coefficient $A$ and $y$ with coefficient $B$.
Tensoring by $B$ changes the diagonal to $\chi,b,1$ and leaves the
central entry equal to $Z$. Adding a toric Kummer cocycle therefore
changes only that central extension. Individual $Z_{ij}$ need not
be closed; differences between solutions are closed, exactly as a
torsor of blends requires.

## 4. Global half-height versus the actual local reference

The normalized global height over $K$, divided by $[K:\mathbb Q]=2$
relative to the raw restriction/corestriction sum, restricts to the
original height on rational points. Conjugation fixes $P_i$ and
sends $iP_j$ to $-iP_j$, so invariance and bilinearity give
$h_v(P_i,iP_j)=0$. The cyclotomic global $p$-height has the same
invariance because its character and ordinary splittings are
conjugation compatible. Therefore its $A\otimes B$ component is
$H_{v,\mathrm{glob}}^{AB}=H_v/2$ and its determinant is
$\operatorname{Reg}_v/4$. The two negative point markings cancel
in this bilinear identity.

This is a global assertion. At $p$, conjugation exchanges the two
places of $K$ above $p$ and cannot be used to set a chosen local
period of $(P_i,iP_j)$ to zero. The original draft used that invalid
identification in its determinant baseline. The corrected proof
explicitly names the actual local block $C_v$, records that its
additional mixed-pair finite and local corrections have not been
constructed, and makes no assertion $C_v=H_v/2$.

The local translation rule itself is correct. The period-matrix height
formula is
[Bloch–de Jong–Sertöz, arXiv:2206.01220v2, Definition 2.8 and Theorem 2.9](https://arxiv.org/html/2206.01220v2).
Its matrix version is explicitly discussed in §5.4 and also follows
entrywise by selecting one upper and one lower marking. Changing the
central entry by $\log(u)/(2\pi i)$ changes the height by
$-2\pi\operatorname{Im}(\log(u)/(2\pi i))=\log|u|$.
The corresponding toric Coleman integral is $\log_pu$ for the
fixed local splitting. The abelian period correction is unchanged.
Thus (14) is exactly $C_v\mapsto C_v+J\ell_v(u)$.

Real and imaginary parts are taken using the underlying rational real
structure before applying the chosen coefficient functional. A single
complex coefficient embedding is not silently substituted for it.
On a doubled marking, $u^2$ has twice the log period, which the
rational half-frame divides back by two. Finally the proof correctly
distinguishes these local translations with fixed reference corrections
from a global canonical height, whose changes cancel by the product
formula or the global idèle character.

## 5. Reference-dependent norm and genuine affine averaging

The difference group has coefficient
$A\otimes R^\vee=k(1)$, so after tensoring by $B$ the translating
class is an ordinary toric Kummer class. Norm compatibility gives
$\operatorname{Cor}[K_R(u)]=[K_R(Nu)]$. This is a transfer of
extension classes with their correct quotient, not a character-weighted
trace after an invariant vector was discarded.

For the actual global units $e_r$, their norm to $K$ is a unit of
$\mathbb Z[i]$ and hence lies in $\mu_4$. Its rational Kummer class
is zero. Thus the rational affine averaging in (17) returns the
chosen reference for the translated system. Its reference independence
is checked by replacing $B_0$ by $B_0+e$: the inside difference loses
$\operatorname{res}(e)$, whose corestriction is $de$, and the outer
$e$ cancels after dividing by $d$.

This normalized averaging is not the transition that made the system
in (15) norm compatible. The latter was explicitly defined using
$B_0+\operatorname{Cor}(B_r-B_0|)$ without the degree denominator.
Both operations are legitimate, but different. The proof retains this
distinction and does not use a rational average as an integral
cyclotomic transition; its degree can be divisible by $p$.

## 6. Determinant-before-trace and its exact norm law

Symmetric squares give the half-square logarithm period. At infinity
including the conjugate square and cross tensor produces
$((\log u+\overline{\log u})/2)^2=(\log|u|)^2$, with the stated
quarter factor and cancellation of imaginary branch changes. This
constructs a framed secondary period, not an ordinary degree-one
extension or an invariant rational scalar.

For the corrected local reference, direct expansion gives
$$4\det(C_v+tJ)=4\det C_v+
  4t\operatorname{tr}(\operatorname{adj}(C_v)J)+4t^2\det J.$$
The mean of $t=\ell_v(\sigma u)$ is zero when the norm is torsion,
proving the corrected (19) with baseline $4\det C_v$. The proof
does not replace this baseline by $\operatorname{Reg}_v$.
The condition $C_v=H_v/2$ would suffice for that specialization,
but is not asserted to be necessary or proved.

For a tower of degree $e$, the mean within an embedding fiber is
$\mu_\tau=e^{-1}\ell_v(\tau Nu)$. Expanding each squared log
about that mean cancels the cross term, and averaging gives exactly
$$Q_{F',v}(u)=e^{-2}Q_{F,v}(Nu)+
 \frac1{[F:K]}\sum_\tau\frac1e\sum_{\sigma|\tau}
                   (\ell_v(\sigma u)-\mu_\tau)^2.$$
This calculation works over $\mathbb C_p$ as well, where it is an
algebraic square identity without a positivity assertion. It shows
why the original unit norm relation does not make these quadratic
periods norm compatible.

The nonconstant term scales by four on $u^2$, whereas an additive
Kummer-class operation scales by two. Their equality as natural
operations on all powers would therefore force that term to vanish.
This does not rule out equality at a particular input. Polarization
becomes additive in one input only after fixing the other; choosing
a root of unity for that second input gives zero in both logarithms.
No identity with the distinct cyclotomic-character moment $M_p$ is
claimed from these formulas.

## 7. The exact finite difference still recovers the old derivative

The corrected §8 chooses $J=E_{ij}$ with coefficient one. Hence the
selected difference is exactly $K_R(e_r)$, rather than a multiple.
It explicitly uses that unit extension's canonical integral Kummer
model and the fixed integral CM coefficient lattice before reduction.
It does not reduce an arbitrary rational reference blend modulo $p^m$.

At the sufficiently large division level, the quotient vector
$t_{\rho,m}$ is actually invariant. Pullback of the difference along
that vector gives exactly $\delta_{p^m}(e_r)\otimes t_{\rho,m}$,
with coefficients in $T_{\mathfrak p}E/p^m$. Simultaneously changing
the two reference partners leaves the difference and this class
unchanged. No invariant rational vector at one finite field is used.

The subsequent corestriction, Shapiro, Betti vector and smoothing
factor match the reviewed input: $\gamma_{\rm CM}=2\operatorname{pr}_\rho
(\gamma_E^+)$ and $12(a^2-\Psi^c((a))\bar\sigma_a)$, with the
inverse cyclotomic action and $n\ge m$. Thus the first-jet class is
the old $\mathcal Z_m$, not one with a changed norm law. Its derivative
is the previously proved plus-corrected cocycle
$D(g)+c_\gamma(g)gv$. Vanishing of the invariant $p^m$-torsion
group proves its uniqueness and its inverse-limit identification
with $w_0$. No extra finite-level Selmer assertion is inserted.

The final frame expression consequently retains every old constant:
$p/(2\#E(\mathbb F_p))$, $g_p=\log_p(1+p)$,
$c_{\rm cmp,p}=(156i\Omega_p)^{-1}$ and
$4e_p\operatorname{Reg}_p$ in the denominator. The inverse is only
on its indicated line when the point regulator is nonzero, with
the undivided identity retained otherwise. Extra Selmer classes may
remain in the projection kernel.

## 8. Completed scope

The proof constructs actual geometric blends and an exact unit
translation/difference operation. It computes both the affine average
that kills the rational unit translation and the quadratic period
whose tower law has an additional variance term. The corrected local
baseline no longer claims a regulator comparison that was not constructed.

Recovering the old $p$-dependent derivative from the difference does
not descend it to a single rational frame. If such a frame $q\Xi$
with the required real realization is eventually constructed, its
coefficient will equal $n_E$ and prove rationality as a conclusion.
GAP CM-Mixed-Derived, Sha finiteness and full BSD remain unresolved.
