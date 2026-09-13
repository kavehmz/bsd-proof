# Independent review of the uniform-witness argument

Date: 2026-09-12. Reviewed
[Uniform Kurihara witnesses: the exact index and the remaining obstruction](uniform-witness-attack.md).
The principal assigned checks were residual surjectivity, joint cocycle
images, Chebotarev realization, the local dimension, and the point-lattice
index condition.

**Review result: no actionable mathematical gap found in these claims.**
The residual-surjectivity deduction and the local-functional realization
lemma pass this independent review. So do the unit-index calculation and
the two-point kernel identification, with their stated hypotheses. The
conclusion remains a reduction to the absence of extra Selmer classes;
the note does not supply that missing arithmetic assertion.

## 1. Residual surjectivity for 389a1

The displayed invariants of
$y^2+y=x^3+x^2-2x$ check directly:
$$
b_2=4,\quad b_4=-4,\quad b_6=1,\quad b_8=-3,
\quad c_4=112,\quad\Delta=389.
$$
The integral equation is minimal because no discriminant valuation can
be decreased by twelve. It is good away from $389$ and multiplicative
of type $I_1$ at $389$, with $c_{389}=1$ for either splitting type.

The semistable reducibility input has the required scope. The statement
read directly in
[Agashe–Winters, arXiv:2510.04323v1, §2](https://arxiv.org/html/2510.04323v1#S2)
says that the two diagonal characters of a reducible residual representation
of a semistable rational elliptic curve are the identity and the cyclotomic
character; optimality is explicitly unnecessary. It attributes this fact
to Serre, Invent. Math. **15** (1972), p. 307. The review read this explicit
restatement rather than the original Serre page.

There is also a local explanation of why this character statement is
appropriate here. Outside $p$, semistability makes the diagonal inertia
characters trivial. At a good ordinary prime $p$, a stable line has inertia
character either $1$ or the mod-$p$ cyclotomic character; good supersingular
reduction is incompatible with local reducibility for $p\ge5$. After
dividing by the appropriate cyclotomic character, a diagonal character is
unramified at all finite primes of $\mathbb Q$ and is therefore trivial.
This checks that no auxiliary character or bad-prime ramification factor
has been silently dropped.

Reducibility thus gives $a_\ell\equiv1+\ell\pmod p$ at good $\ell\ne p$,
equivalently $p\mid\#E(\mathbb F_\ell)$. Direct counts give five points
over $\mathbb F_2$ and six over $\mathbb F_3$. No $p\ge5$ divides both,
so reducibility is impossible for every such $p$.

For $p\ne389$, the Tate parameter at $389$ has valuation one. In an
unramified extension containing $\mu_p$ and splitting any nonsplit torus,
adjoining a $p$th root of this parameter gives a totally ramified extension
of degree $p$. Inertia therefore contains a nonidentity unipotent on $E[p]$.
The argument remains valid for nonsplit multiplicative reduction because
the splitting quadratic twist is unramified.

The final group argument is sound over the prime field. An irreducible
subgroup containing a transvection has a conjugate transvection with a
different fixed line. In a basis consisting of these two lines, the two
elements have matrices
$$
\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
\begin{pmatrix}1&0\\b&1\end{pmatrix},\qquad a,b\ne0.
$$
Their integer powers realize every coefficient in the two root groups,
since the coefficient field is $\mathbb F_p$. These groups generate
$\mathrm{SL}_2(\mathbb F_p)$. The determinant of $E[p]$ is the surjective
cyclotomic character, so the image is $\mathrm{GL}_2(\mathbb F_p)$.

**[THEOREM, reviewed deduction]** The claimed surjectivity for every
$p\ge5$, $p\ne389$ follows. This supplies the explicit good-prime
hypothesis-exception set $\{2,3,389\}$ used in the note. It does not
identify the possible primes supporting $\Sha[p]$.

## 2. Joint restrictions of independent cocycles

Put $V=E[p]$, $K=\mathbb Q(E[p])$, and
$G=\mathrm{GL}_2(\mathbb F_p)$. The central-scalar proof of
$H^1(G,V)=0$ is correct: for a cocycle $c$ and $z=aI$ with $a\ne1$,
$$
(a-1)c(g)=(g-1)c(z),
$$
so $c$ is a coboundary. Inflation–restriction consequently makes restriction
to $G_K$ injective on $H^1(\mathbb Q,V)$.

For a basis $c_1,\ldots,c_d$ of the chosen finite-dimensional cohomology
space, restriction to $G_K$ is a homomorphism into $V^d$. Its image $W$
is a vector subspace: any additive subgroup of an elementary abelian
$p$-group is $\mathbb F_p$-linear. It is $G$-stable because
$$
c_i(\gamma h\gamma^{-1})=\bar\rho(\gamma)c_i(h)
\qquad(h\in G_K).
$$

The step that forces $W=V^d$ is valid in characteristic $p$. It does
**not** assert that every $\mathbb F_p[G]$-module is semisimple. The
particular ambient module $V^d$ is a direct sum of simple modules, hence
is semisimple, so any proper submodule admits a nonzero quotient map to
$V$. The natural representation has endomorphism ring $\mathbb F_p$,
giving the scalar-row relation that contradicts independence of the
cohomology classes.

For an elementary verification avoiding any possible ambiguity about
semisimplicity, the algebra generated by $G$ is all of
$M_2(\mathbb F_p)$. Indeed $E_{12}$ and $E_{21}$ are differences between
unipotents and the identity, and their products give the diagonal matrix
units. Identify $V^d$ with $\mathbb F_p^d\oplus\mathbb F_p^d$ by its two
coordinate rows. Stability under the matrix units forces
$$
W=A\oplus A
$$
for some subspace $A\subseteq\mathbb F_p^d$: the diagonal units isolate
the two rows and the off-diagonal units interchange them. If $A$ is
proper, choose a nonzero scalar row $(b_i)$ annihilating it. Then
$\sum_i b_i c_i$ restricts identically to zero on $G_K$. Injectivity of
restriction contradicts independence. Thus $A=\mathbb F_p^d$ and $W=V^d$.

**[THEOREM, reviewed argument]** The full joint image assertion holds;
there is no invalid application of Maschke's theorem.

## 3. Frobenius translation, conjugacy, and localization

The map defined by the cocycles and the residual representation is a
continuous homomorphism
$$
G_{\mathbb Q}\longrightarrow V^d\rtimes G.
$$
Its image contains $V^d$ by §2 and projects onto $G$, hence equals the
whole semidirect product. There is no need to assume in advance that an
extension splits: subtracting the translation coordinate from any lift
of $g\in G$ produces $(0,g)$ inside the image.

Fix a nonidentity unipotent $\tau$ and a vector $e$ spanning
$V/(\tau-1)V$. For a desired functional $\lambda$, the element
$$
((\lambda(c_1)e,\ldots,\lambda(c_d)e),\tau)
$$
therefore occurs in this Galois group. Chebotarev supplies infinitely
many unramified primes in its conjugacy class.

The conjugacy qualification causes no loss of the functional. Conjugating
$(v,\tau)$ by $(b,g)$ replaces it by
$$
\bigl(gv+(1-g\tau g^{-1})b,\ g\tau g^{-1}\bigr).
$$
In each coordinate, the added term vanishes modulo
$(g\tau g^{-1}-1)V$, and $g$ identifies the old one-dimensional quotient
with the new one. Thus the same choice of basis transports the prescribed
values on all $c_i$ simultaneously.

For these primes the residual Frobenius has determinant one and trace two,
so $\ell\equiv1\pmod p$ and $a_\ell\equiv\ell+1\pmod p$. Nonidentity
unipotence gives rank one for $\tau-1$. At a good prime $\ell\ne p$, local
Kummer classes are unramified, and
$$
H^1_f(\mathbb Q_\ell,V)
=H^1_{\mathrm{ur}}(\mathbb Q_\ell,V)
\simeq V/(\tau-1)V
$$
has dimension one. The good-reduction formal group is $p$-divisible, so
the finite-field quotient of local points used in the note gives this
same space. Excluding the finitely many primes ramifying in the joint
extension also ensures that every class in the chosen space is
unramified at the selected primes.

**[THEOREM, reviewed deduction]** Every nonzero functional can be
realized as stated. Consequently a $d$-dimensional Selmer space can be
separated by $d$ distinct such primes, and fewer cannot suffice because
each target has dimension one.

## 4. Point-lattice and kernel checks

If $P_1,P_2$ form a basis of the free Mordell–Weil group and rational
$p$-torsion is zero, their Kummer images span the entire two-dimensional
space $E(\mathbb Q)/pE(\mathbb Q)$. More generally, the same conclusion
holds for two independent points only when $p$ does not divide their
index in the free group. The note states this necessary restriction.
Independence over $\mathbb Q$ alone would not justify it at an index-dividing
prime; that error has not been made here.

For a pair of primes whose localization matrix on this Kummer space $K_p$
is invertible, write $L:H\to\mathbb F_p^2$ for the combined map. Since
$L|_{K_p}$ is an isomorphism, for each $c\in H$ there is a unique $k\in K_p$
with $c-k\in\ker L$. Also $K_p\cap\ker L=0$. Hence the natural quotient
map induces
$$
\ker L\overset\sim\longrightarrow H/K_p=\Sha(E/\mathbb Q)[p].
$$
This is a valid isomorphism, not merely an equality of dimensions. Its
construction shows explicitly why checking the rational-point determinant
does not remove additional Selmer classes.

## 5. Unit index and the theorem inputs

The higher-Fitting-ideal formula and paired invariant factors were checked
in [Kim, arXiv:2203.12159v6, Theorem 1.8](https://arxiv.org/html/2203.12159v6),
and opposite-parity vanishing in its Proposition 3.14. The first unit
Fitting index of
$X\simeq\mathbb Z_p^s\oplus\bigoplus_{j=1}^t\mathbb Z_p/p^{a_j}$
is $s+t=\dim X/pX$. Since $t$ is even, this first index lies in the
parity to which Kim's formula applies. Thus the proof that
$$
u_p=\dim_{\mathbb F_p}\operatorname{Sel}_p
   =\operatorname{rank}E(\mathbb Q)+\dim_{\mathbb F_p}\Sha[p]
$$
when $M_\infty=0$ is valid. The exact comparison of finite and infinite
Kummer sequences uses divisibility of
$E(\mathbb Q)\otimes\mathbb Q_p/\mathbb Z_p$ and the absence of rational
$p$-torsion; it makes no assumption on divisibility inside Sha.

The ordinary and squarefree-conductor supersingular alternatives are
indeed the two cases of
[Castella–Sano, arXiv:2601.14504v1, Theorem B](https://arxiv.org/html/2601.14504v1).
Its surjectivity and Manin-constant hypotheses match those retained in the
note. With $c_{389}=1$, it gives $M_\infty=0$ and some unit witness for
each good $p\ge5$. It does not bound that witness's index.

The two formal module countermodels in §6 of the reviewed note have the
claimed Fitting valuations. In particular
$\mathbb Z_p^2\oplus(\mathbb Z/p)^2$ has first nonzero Fitting ideal at
index two and first unit Fitting ideal at index four. The examples
correctly refute the proposed deductions from the listed abstract data,
and are expressly not presented as elliptic-curve counterexamples.

The common integral presentation criterion in §7 is also valid: a
nonzero $(a-2)$-minor bounds the cokernel dimension by two away from its
prime divisors, and the Kummer injection supplies the opposite bound.
The difficult assertion is the unconstructed surjection from this fixed
integral model onto every varying mod-$p$ Selmer group. That assertion
remains explicitly tagged as a gap.

The reviewed conclusions therefore preserve the distinction between
constructing local tests, proving that they are injective on all Selmer
classes, and controlling the first unit Kurihara index. No passage between
these three assertions is justified by Chebotarev alone.
