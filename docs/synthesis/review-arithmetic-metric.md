# Independent review of the arithmetic metric realization

Date: 2026-09-12. Reviewer: /root/uniform_witness, GPT-6 Astra/xhigh.
Reviewed [proof](arithmetic-metric-realization.md) and
[checkpoint](arithmetic-metric-checkpoint.md).

**PASS.** The integral identification
$\widehat{\mathrm{CH}}^2(X)\simeq\mathbb R$, the decorated-current
class, its constant-metric line product, and the two distinct
determinant operations are correct with the stated normalizations.
No mathematical correction is required. This review does not supply
the remaining rational motivic/frame comparison or a BSD conclusion.

Reviewed proof SHA256:
235436d2b99b7cf5161a6478798e893e9ff2ef111156ee3bbfb6e70f32c8b4a6.
Reviewed checkpoint SHA256:
8f41621a7c297500da3a87f90020d6daa227a7fc911aa231accd505475e40764.
Subsequent editorial review links/status updates need not retain these
hashes; these identify the mathematical revision inspected here.

## 1. Scheme and source scope

The proof uses the actual projective cubic model of 389a1.
Its regularity, flatness, geometrically integral fibers, zero section,
and smooth generic fiber were already independently reviewed in the
[arithmetic-surface review](review-weil-etale-lattice.md).
The conclusion $\mathrm{CH}_0(X)=\mathrm{CH}^2(X)=0$ is an input
from the separately [reviewed ordinary K-theory proof](review-k-theory-lattice.md).
It concerns closed points on the arithmetic surface, not the generic
elliptic curve's divisor class group. No finite-Sha premise is added.
This review checks how that established input is used; it does not
rerun the earlier arithmetic computations.

The primary source was read directly:
[Gillet-Soulé, *Arithmetic intersection theory*, PMIHÉS 72 (1990),
93–174, DOI 10.1007/BF02699132](https://www.numdam.org/article/PMIHES_1990__72__93_0.pdf).
The pertinent locations are §1.2.1–1.2.3 (printed pp. 100–103),
§3.2.1 (p. 125), §3.3.3–3.3.5 (pp. 126–129),
§3.4.3 (p. 131), §3.6.1 (pp. 134–135), and the
codimension-one multiplication in §4.2.3 and its proof
(especially pp. 144–145).

Definition 3.2.1 requires flat finite type and smooth generic fiber;
it does not require every special fiber to be smooth. The singular
fiber at 389 therefore does not exclude this model. The structure
map $f:X\to\operatorname{Spec}\mathbb Z$ is proper and both schemes
are equidimensional. Its map on generic fibers is smooth.
Consequently §3.6.1(ii) supplies the **integral** pushforward used
in the arithmetic degree.

## 2. The exact sequence really gives an integral isomorphism

The full source exact sequence has a regulator term on the left:
$$
 \mathrm{CH}^{2,1}(X)\xrightarrow{\rho}
 \widetilde A^{1,1}(X_{\mathbb R})
 \xrightarrow{a}\widehat{\mathrm{CH}}^2(X)
 \longrightarrow\mathrm{CH}^2(X)\longrightarrow0.
$$
The proof correctly uses its final three terms, without assuming
that $\rho$ vanishes. Its injectivity argument subsequently forces
that vanishing in this particular quotient.

Indeed, every smooth real top-degree form on the connected compact
curve with zero integral is $dd^c h$ for a smooth real h, by the
scalar Poisson equation. The antiholomorphic involution c
anticommutes with $dd^c$. If $c^*\eta=-\eta$, then
$dd^c(c^*h)=-c^*\eta=\eta$, so the average
$(h+c^*h)/2$ is an invariant solution. Thus the equivariant quotient
by $\operatorname{im}\partial+\operatorname{im}\bar\partial$ is
exactly one copy of $\mathbb R$, measured by integration.

For the period lattice $\mathbb Z\omega_1+\mathbb Z ib$, the form
$$
 \mu_E=\frac{i}{2\omega_1b}\omega\wedge\overline\omega
$$
has integral one: in a uniformizing coordinate the numerator is
ordinary area measure and the fundamental rectangle has area
$\omega_1b$. Since $c^*\omega=\overline\omega$, its pullback
under c is $-\mu_E$, as required.

Pushforward of $a(\eta)$ is the constant metric class
$a(\int_E\eta)$ on $\operatorname{Spec}\mathbb Z$.
The degree normalization in §3.4.3 assigns half that constant.
Therefore the composite
$$
 \widetilde A^{1,1}(X_{\mathbb R})
       \xrightarrow a\widehat{\mathrm{CH}}^2(X)
       \xrightarrow{\widehat{\deg}}\mathbb R
$$
is $\lambda\mapsto\lambda/2$ after identifying the source by
integration. It is injective. In particular an element in the
omitted regulator image cannot have a nonzero integral; here that
makes its whole class zero. This addresses the possible
kernel/cokernel objection to the argument.

The established $\mathrm{CH}^2(X)=0$ makes a surjective, so the
composite proves it is an isomorphism. No tensoring with Q has
occurred. Its inverse under arithmetic degree is exactly
$q\mapsto a(2q\mu_E)$. Unique divisibility of the additive group
$\mathbb R$ then justifies the corresponding assertion after
tensoring with Q. This is an isomorphism of additive groups;
no finite generation over Q follows.

## 3. Original Green currents suffice

In codimension two on X, the Green current has type (1,1)
on its complex curve. Its $dd^c$ is zero for dimensional reasons,
as is the complex cycle of a codimension-two arithmetic cycle.
The zero algebraic cycle therefore accepts any real (1,1)
current with the required conjugation sign as a Green current.

This statement uses the original definition, which imposes
smoothness on $dd^c g+\delta_Z$, rather than demanding that
every chosen current representative be smooth away from Z.
A Green *form* smooth outside Z is a more specific representative.
GS §1.2.2(i)–(iii), together with §1.2.3, proves that the
current quotient and smooth-form quotient agree in the
$dd^c$-closed case. Equivalently, apply the compact Green
operator to the zero-mass current to express it as $dd^c$
of a distribution. The real and involution conditions are
preserved by the same averaging argument as in §2.

Consequently no singular-metric extension of arithmetic Chow
theory is being invoked. Nor does this argument claim that
the raw pushed current becomes a smooth function pointwise;
it becomes a smooth representative only in the specified quotient.
For j>=3, both the codimension-j algebraic cycle group and
the type (j-1,j-1) current space are zero. Hence
$\widehat{\mathrm{CH}}^j(X)=0$, including before rationalization.

## 4. The decorated Mellin current and its real sign

The current
$\mathcal T=\pi_*(A_2 Fd\mu)$ and its mass M are taken from
the already [reviewed compactified trace construction](review-mellin-trace.md).
That construction retains the effective orbifold normalization,
the degree-40 parametrization, the nonzero rational differential
factor $c_\pi$, local integrability, and the absence of cusp atoms.
This review does not redo its analytic certificate or unfolding.

The new conjugation calculation is correct. Put
$\alpha=\pi^*\omega$ and $l=\log|v|$. Since
$$
 Fd\mu=-\frac{i}{4\pi^2c_\pi}d(l\alpha),
$$
and c fixes l while $c^*\alpha=\overline\alpha$, one obtains
$c^*(Fd\mu)=-\overline{Fd\mu}$. The invariant infinity cusp
Eisenstein series is unchanged by $z\mapsto-\overline z$;
its Laurent coefficient $A_2$ is also real and unchanged.
Thus $c^*\mathcal T=-\overline{\mathcal T}$.
The proper finite holomorphic pushforward commutes with these
conjugations: the orientation reversal on the source and target
is the same, so there is no additional sign.

It follows that $2\operatorname{Re}\mathcal T$ is a real
(1,1) current with precisely the sign $(-1)^1$ in GS §3.2.1.
Section 3 of this review verifies the Green equation for zero cycle.
Its integral is 2M because the previously proved mass M is real.
The degree is therefore M, not 2M or M/2.
Subtracting $2M\mu_E$ leaves a zero-mass current, which is exact
in the Green-current quotient. Hence the asserted equality
$$
 [(0,2\operatorname{Re}\mathcal T)]=a(2M\mu_E)
$$
holds in the actual integral arithmetic Chow group.

The previously calculated extra derivative term contributes the
nonzero mass M. None of the argument discards that term. The
collapse to a mass class is a property of this top Chow group,
not a new equation calculating or rationalizing M.

## 5. The hermitian line product and the two determinants

For the free line $\mathbb Z$ with $\|1\|=\exp(-q)$,
the squared-norm convention gives Green function
$-\log\|1\|^2=2q$, so its degree on Spec Z is q.
This checks the normalization of $\overline L_q$.
The line $\mathcal O_X(O)$ restricts to a degree-one line on E.
Its curvature therefore integrates to one for any smooth invariant
metric. No positivity assumption on that metric is needed.

The product of a metric class with $\widehat c_1(\overline H)$
is $a(2q\,c_1(\overline H))$. This particular product exists
integrally, both from codimension-one multiplication in GS and
directly from the star product. For clarity, taking the zero
algebraic divisor with constant Green function 2q gives the
representative $2q\delta_O$ in the latter construction.
If $g_O$ is the Green function of H, then
$\delta_O=c_1(\overline H)-dd^cg_O$, so this is the same
current class as $2q\,c_1(\overline H)$. There is no singular
current multiplication problem in this constant-factor case.

The difference $c_1(\overline H)-\mu_E$ is an integral-zero
top form. Thus (4.1) equals $a(2q\mu_E)$ integrally and has
degree q. Taking q=M yields exactly the decorated-current
class. The note properly acknowledges that the arbitrary
constant-metric example itself was already in the earlier
arithmetic Green note.

For the height entries, the [reviewed relative-cycle construction](relative-modular-cycle-attack.md#5-an-exact-period-formula-for-the-full-height-matrix)
uses Green current $2g_i$ in GS convention and the arithmetic
one-half at infinity. The negative of its fixed intersection
therefore has degree $H_{ij}$ in the full BSD height convention,
as claimed. Proposition 2.2 then identifies it with
$a(2H_{ij}\mu_E)$; this step introduces no extra factor two.

The product of two such codimension-two classes is in
$\widehat{\mathrm{CH}}^4(X)_{\mathbb Q}=0$.
Accordingly its literal two-by-two cup determinant is zero.
Applying arithmetic degree to each entry first gives the real
matrix H and the independently certified positive determinant
$\operatorname{Reg}_{\mathrm{BSD}}(E)$. These are different
operations. The text correctly restricts the conclusion to
the displayed ordinary cup determinant and does not exclude
secondary products or framed determinant realizations.

## 6. Scope and handoff

The proof retains the exact remaining rational motivic/frame
comparison AM-389. Its arithmetic Chow realization works for
every real q because metrics admit that parameter. Integral or
rational coefficients for the algebraic cycles do not restrict q.
No rationality, integrality in the BSD lattice, or permission
to divide in a rational realization by the L(f,2) regulator
is inferred from the existence of this Chow class.

At the reviewed checkpoint revision, the phrases “candidate
exact calculation,” “would,” and “need verify” describe
pre-review work and should be updated after this PASS.
The final paragraph's parallel-task snapshot is likewise
historical: this reviewer has finished the two-prime Heegner
construction and is reviewing this metric note. These are
editorial continuity repairs for the coordinator, not
mathematical objections. Only this review file was written;
no source proof, shared state, or old numerical script was changed.
