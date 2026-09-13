# Independent review of the twisted Fourier–Mukai construction

Date: 2026-09-12. Reviewer: `/root/higher_period_integrality`,
GPT-6 Astra, xhigh reasoning.

**PASS for §§9–10 of [the construction](twisted-sheaf-lifting-attack.md),
including Propositions 9.1, 9.2 and 10.1 and the integral generic-curve
calculation in §10.2.** Root separately reviews §§1–8: the Kummer lift,
fixed-determinant moduli, arithmetic extension and Azumaya construction.
This review also checks the use of the §5 Poincaré pushforward in §§9–10.

Reviewed complete-file SHA256:
`189b1734c29080858c38f7a945c117a941b3d027154c9c95a9f0336e77a5ab73`.
The author confirmed that its change from the previously announced
`39a92cd53384f6ab9342c762efd53f2287426b994194db4d3199128c7a411d3b`
only clarified the §8 Hecke–Brauer input; §§9–10 were unchanged.
Subsequent review-link or checkpoint changes are editorial.

The only requested correction was to make the canonical-bundle factor
in the inverse explicit. The final version includes its trivialization.
No remaining formula correction is required. No old numerical computation
was rerun, and no author or root proof file was edited by this reviewer.

## 1. Actual kernel and degree convention

Let $C/\mathbb Q$ be the locally soluble period-$n$ torsor and
$\mathscr H=\mathscr P_C^0\to E$ its Picard gerbe of class $\beta$.
Its universal line $\mathcal P$ has weight one. Thus
$$\Phi(A)=\mathbf Rp_{E,*}(\mathcal P\otimes p_C^*A)$$
is weight one, whereas the tensor in
$$\Psi(V)=\mathbf Rp_{C,*}(\mathcal P^\vee\otimes p_E^*V)$$
has weight zero and descends to $C\times E$. The output is ordinary
on the actual $C/\mathbb Q$. No ground-field identification $C=E$
is made in this construction.

The primary equivalence theorem applies to smooth projective geometrically
connected genus-one curves over perfect fields. Its Picard-gerbe
construction includes an inverse Brauer sign under its convention;
here the stated gerbe and inertia weights fix the direction. See
Ramachandran–Rosenberg,
[arXiv:2212.14497v2, Theorem 2 and §§3.1, 3.4–3.6](https://arxiv.org/html/2212.14497v2).
This input has no Sha-finiteness hypothesis.

The degree alignment preceding Proposition 9.1 is necessary and valid.
For the degree-$n$ closed point $D$, the bundle
$W=p_{E,*}(\mathcal P|_{D\times\mathscr H})$ becomes a sum of
degree-zero lines. Its weight-$n$ determinant defines a $\mu_n$
reduction by trivialization. A geometric root of this determinant has
degree zero. Consequently this reduction and the normalized Poincaré
family assign the same geometric degree. This checks the premise $(n,1)$
used in the transform; it is not inferred from an arbitrary equivalence
of gerbes. Root separately reviews extension of the adjusted Kummer lift.

## 2. Rank, degree and inverse shift

For each geometric $c\in C$, the fiber cohomology of $\Psi(V)$ is
that of a stable bundle of rank $n$, degree one, tensored with a
degree-zero line. The dual has negative slope and no section; Serre
duality gives $H^1=0$, and Riemann–Roch gives $h^0=1$. Proper
cohomology and base change therefore makes $\Psi(V)$ a line bundle
in degree zero. This conclusion descends to $\mathbb Q$.

On geometric $E\times E$, put
$d=[\Delta]-[E\times O]-[O\times E]$. The three self-intersections
are zero and the three pairwise intersections are one, so
$d^2=-2[\mathrm{pt}]$. Its degree on each factor is zero and the
relative Todd class is one. Thus the pushforward of
$$(1-d+d^2/2)(n+[\mathrm{pt}]_E)$$
is $1-n[\mathrm{pt}]_C$. This checks $(n,1)\mapsto(1,-n)$ with
the dual kernel as well. The dual of the resulting line has degree $n$;
when $n>1$, this supplies no degree-one class or point on $C$.

The right adjoint is precisely
$$\Phi^R(V)=\Psi(V)\otimes\omega_C[1].$$
The fixed invariant differential of the Jacobian induces one on its
torsor and trivializes $\omega_C$. With that stated choice,
$\Phi^R=\Psi[1]$, so $\Psi\Phi\simeq[-1]$. The adjunction unit and
counit are defined over $\mathbb Q$ and become isomorphisms geometrically;
their cones therefore vanish by faithful flatness. This proves descent
of the inverse without inferring equality of kernels merely from their
geometric isomorphism classes. The final text retains the necessary shift.

## 3. The explicit extension in Proposition 9.2

The neutralization at $O$ gives $W|_O=L$, where
$D=\operatorname{Spec}L$. A local Cartier resolution gives
$$\mathcal Ext^1(k(O),W)=W|_O\otimes T_OE,
\qquad \mathcal Hom(k(O),W)=0.$$
The vanishing removes any extra local-to-global obstruction. Hence the
rational vector $1\otimes\tau$ defines the global twisted extension.

Geometrically, $W$ is a direct sum of distinct degree-zero Poincaré
lines $L_i$, and the coordinates of the field unit are all nonzero.
The lines are distinct because the points of the separable closed point
$D$ are distinct and the Poincaré parametrization is an isomorphism.
In a local presentation $tv=w$ at $O$, a nonzero residue vector has
a unit coordinate; eliminating its generator proves local freeness.
The determinant is $\det W\otimes\mathcal O_E(O)$, hence is
$\mathcal O_E(O)$ in the chosen reduction.

For stability, a proper saturated destabilizing subbundle $U$ has
positive integral degree and surjects onto $k(O)$. Its intersection
$U'$ with $W$ has degree $\deg U-1$, which semistability of $W$
forces to be zero. The injection $W/U'\hookrightarrow V_D/U$ makes
$U'$ a subbundle. In the abelian category of semistable slope-zero
bundles, a subobject of the finite sum of distinct simple objects $L_i$
is a sum of a subset. A proper subset leaves a complementary $L_i$,
and the extension still has a nonzero component in its Ext group. It
cannot be the image of an extension by $U'$, contradicting the
subextension from $U$. This proves geometric stability.

Transforming $0\to\mathcal O_C(-D)\to\mathcal O_C\to\mathcal O_D\to0$
checks the construction independently. The first object has its transform
in degree one because every degree-$-n$ twist has $H^0=0$, $h^1=n$.
The middle transform is $k(O)[-1]$ after the specified cohomology/tangent
choice, and the last transform is $W$. The resulting sequence is (9.2).
The constant one's restrictions to $D$ give its extension coordinates.
The compatible choices therefore yield
$$V_D\simeq\Phi(\mathcal O_C(-D))[1],\qquad
\Psi(V_D)\simeq\mathcal O_C(-D).$$
Scaling $\tau$ changes the framed extension, but not the isomorphism
class of its middle bundle. No canonical unstated scalar is required.

## 4. Cocycle action and stabilizer scope

For $A(x,y)=t_x^*(-)\otimes L_y$, changing the integration variable
and using the biextension identity give
$$F t_x^*\simeq(-\otimes L_{-x})F,\qquad
F(-\otimes L_y)\simeq t_y^*F.$$
For $T=(-\otimes\mathcal O_E(O))$, the identity
$t_x^*\mathcal O_E(O)=\mathcal O_E([-x])$ gives
$T A(x,y)T^{-1}=A(x,y+x)$. Thus the standard-word representatives
act on pairs by the stated $S,T$ matrices. These are explicit generators
defined over $\mathbb Q$, not unspecified lifts of numerical matrices.

For the tensor-descent class $\xi$ defined by (10.1), of order $n$,
the equality $(b\xi,d\xi)=(0,\xi)$ is equivalent to
$n\mid b$, $d\equiv1\pmod n$. The determinant-one identity then
gives $a\equiv1\pmod n$, proving both directions of (10.5).
Changing point-cocycle or dual-kernel convention changes the torsor sign.
The intrinsic kernel fixes its target $C$, and none of the rank or
period conclusions equates $C$ with $E$ over $\mathbb Q$.

The text correctly separates this exact cohomological stabilizer from a
sufficient condition for actual kernel descent. Matching pairs can leave
a scalar obstruction in the base-field Brauer group. The cited source
maintains that distinction:
Antieau–Krashen–Ward,
[arXiv:1409.2580, §§4–5, especially Theorem 5.1](https://arxiv.org/html/1409.2580).
Its comparison up to a base-field Brauer class is not promoted to an
exact untwisted descent theorem here.

The inversion/shift qualification is correct: inversion is numerically
$I$ but negates $(x,y)$; a shift has numerical sign but centralizes
these functors. Composing a standard representative with inversion changes
$a,d\equiv1$ to $a,d\equiv-1$, always retaining $n\mid b$.
The identity $F^2\simeq[-1]_E^*[-1]$ is consistent with both actions.
In particular (10.5) is not used to exclude the actual shift functor.

## 5. Integral group and Euler pairing

The determinant obstruction makes every twisted rank divisible by $n$.
The global types $(n,0)$ and $(n,1)$ generate
$n\mathbb Z\oplus\mathbb Z$, proving equality in (10.6), including
virtual classes. Every actual equivalence with geometric numerical matrix
$g$ preserves this image. Applying it to $(0,1)$ forces $n\mid b$,
independently of the preceding cohomological classification. The image of
$(n,1)$ cannot have virtual rank $1$ or $-1$ when $n>1$.

The stronger generic-curve calculation in §10.2 passes as well. Rank and
determinant identify $K_0(C)$ with $\mathbb Z\oplus\operatorname{Pic}(C)$
for this regular curve. A rational Picard-scheme point has a line-bundle
descent obstruction in $\operatorname{Br}(\mathbb Q)$. Local points of
$C$ kill it at each completion; Brauer–Hasse–Noether kills it globally.
Hence the degree-zero subgroup is exactly $E(\mathbb Q)$, the previously
certified torsion-free rank-two group for 389a1. The degree image is
$n\mathbb Z$, split by $\mathcal O_C(D)$. Consequently
$\operatorname{Pic}(C)\simeq\mathbb Z^3$ and the equivalence gives
$K_0^\beta(E)\simeq\mathbb Z^4$.

Riemann–Roch gives $\chi(A,B)=r_A d_B-d_A r_B$. Its radical is
precisely $\operatorname{Pic}^0(C)$: pairing with numerical types $(1,0)$
and $(0,n)$ forces degree and rank to vanish. On the rank-two quotient
the matrix is
$$\begin{pmatrix}0&n\\-n&0\end{pmatrix},\qquad\det=n^2.$$
The equivalence preserves this form and takes the numerical lattice
$\mathbb Z\oplus n\mathbb Z$ to $n\mathbb Z\oplus\mathbb Z$.
Thus this finite free group has an integral pairing retaining the period.
The file correctly confines the calculation to the generic curve; it
does not infer the analogous twisted arithmetic-surface group.

## 6. Verified boundary

The arguments construct actual optimal-rank twisted bundles, an explicit
elementary modification, a line on the actual torsor, and its generic
Grothendieck group with Euler form. They give no rank-one twisted bundle
on $E$, no period-independent bound and no nonzero Sha class for 389a1.
Matching abstract rank-four groups supplies none of those statements.
GAP TS-389 and the full BSD objective remain unresolved.
