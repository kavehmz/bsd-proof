# A full-modular-curve spectral source for the central Mellin derivative

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
The `[NEW]` deductions below passed
[independent review](review-mellin-variation.md). The objective remains
full BSD over Q, not only this test curve.

## 1. An actual analytic source, with an extra regulator factor

Put $N=389$, let $f=\sum a_mq^m$ be the normalized newform of 389a1,
and write
$$\ell=\frac{L''(f,1)}2=4\pi(J''(0)-\mathcal C_E).$$
The reviewed certificates give exact analytic order two, split
multiplicative reduction at $N$, $a_N=1$, and Fricke sign $-1$.
The nonzero correction $110<\mathcal C_E<111$ is retained through this
exact definition of $\ell$; none of the integrals below replaces it by
$4\pi J''(0)$.

This note constructs a full-curve spectral integral with exact value
$$\boxed{\int_{Y_0(N)} y^2 f\bar g\,A_2\,d\mu
 =-\frac{9N}{\pi^4(N+1)}L(f,2)\ell,} \tag{1.1}$$
where $g=E_2-NE_2(Nz)$ and $A_2$ is the second Laurent coefficient
of the cusp Eisenstein series at its pole $s=1$, specified below.
All level, gamma, zeta, residue and boundary factors are explicit.
It therefore gives an analytic source for the target after division by
the nonzero, independently defined $L(f,2)$. That division is not claimed
to preserve any rational or integral regulator lattice.

Two concrete arithmetic repairs are tested. The rational modular-unit
part of the spectral family is killed by the relevant Fricke pairing.
Combining that actual unit with the noncuspidal moving functions produces
Milnor symbols whose elliptic transfer is killed by two, including their
tame boundaries. An integral character deformation retaining all of
$X_0(N)$ is also constructed; its first scattering-response integrals
retain a factor $L(f,1)$ and vanish after spectral differentiation. None
of these tests rules out a different secondary comparison.

## 2. Exact Eisenstein series and both cusp boundaries

Use the effective group $\Gamma=\Gamma_0(N)/\{\pm1\}$, hyperbolic
measure $d\mu=dx\,dy/y^2$ and positive Laplacian
$\Delta=-y^2(\partial_x^2+\partial_y^2)$. The normalized cusp scalings
are $\sigma_\infty=1$ and
$\sigma_0=\left(\begin{smallmatrix}0&-1/\sqrt N\\\sqrt N&0\end{smallmatrix}\right)$;
both scaled cusp coordinates have width one. Define for $\Re s>1$
$$E_\infty(z,s)=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
                      \Im(\gamma z)^s,\qquad
E_0(z,s)=E_\infty(\sigma_0z,s).$$
Let $E(z,s)$ denote the analogous level-one series, and put
$$\psi(s)=\frac{\sqrt\pi\,\Gamma(s-1/2)\zeta(2s-1)}
                         {\Gamma(s)\zeta(2s)}.$$

**[NEW] Lemma 2.1 (normalization by oldforms).**
$$E_\infty(z,s)=\frac{N^sE(Nz,s)-E(z,s)}{N^{2s}-1},\qquad
E_0(z,s)=\frac{N^sE(z,s)-E(Nz,s)}{N^{2s}-1}. \tag{2.1}$$
The scattering matrix, in the stated scaled coordinates, is
$$\Phi(s)=\frac{\psi(s)}{N^{2s}-1}
\begin{pmatrix}N-1&N^s-N^{1-s}\\N^s-N^{1-s}&N-1\end{pmatrix}.
\tag{2.2}$$

*Proof.* In the primitive-pair sum for $E(Nz,s)$, separate $N\nmid d$
and $N\mid d$. The first part is $N^sE_\infty(z,s)$; writing
$d=Nd'$ in the second gives $N^{-s}(E(z,s)-E_\infty(z,s))$.
Solve for $E_\infty$. Level-one inversion interchanges $E(z,s)$ and
$E(Nz,s)$ under $\sigma_0$, proving the other formula. Substitution
of the level-one constant term $y^s+\psi(s)y^{1-s}$ proves (2.2).
The identities continue meromorphically. $\square$

The analytic continuation, Fourier expansion and this same scattering
normalization are recorded in Petridis, *Perturbation of scattering poles
for hyperbolic surfaces and central values of L-series*, Duke Math. J.
103 (2000), §§2 and 4.3, especially (4.8) and the matrix preceding (4.9)
([author PDF](https://www.homepages.ucl.ac.uk/~ucahipe/variationpublished.pdf)).
Its later hypotheses about nontrivial zeta zeros are not used for this
explicit series or its Laurent expansion at one.

Write $t=s-1$ and
$$E_\infty(z,1+t)=\frac R t+A_0(z)+tA_1(z)+t^2A_2(z)+O(t^3),
\qquad R=\frac{3}{\pi(N+1)}. \tag{2.3}$$
For each cusp $a$, define the exact constants $c_a,d_a,e_a$ by
$$\phi_{a\infty}(1+t)=R/t+c_a+d_at+e_at^2+O(t^3). \tag{2.4}$$
These are coefficients of the explicit meromorphic functions (2.2),
not omitted or freely chosen renormalization constants. Equivalently
they are successive derivatives of $\phi_{a\infty}(1+t)-R/t$ at zero,
with the coefficient factorials retained.

The constant Fourier terms of the three functions at the cusp $a$ are
$$\begin{aligned}
A_0(\sigma_a z)_0&=\delta_{a\infty}y+c_a-R\log y,\\
A_1(\sigma_a z)_0&=\delta_{a\infty}y\log y+d_a-c_a\log y
                                      +\tfrac R2(\log y)^2,\\
A_2(\sigma_a z)_0&=\tfrac{\delta_{a\infty}}2y(\log y)^2+e_a-d_a\log y
                       +\tfrac{c_a}2(\log y)^2-\tfrac R6(\log y)^3.
\end{aligned} \tag{2.5}$$
These follow by multiplying $y^{1+t}$ and $y^{-t}$ into (2.4).
The nonconstant Fourier terms and their finitely many derivatives have
exponential decay times polynomial/logarithmic factors. Thus (2.5)
retains the incoming term, outgoing term and every Laurent boundary
constant at both cusps.

## 3. The rational differential and exact unfolding

Use the actual normalized modular unit from the reviewed Green note,
$$v=N^{-6}\frac{\Delta(z)}{\Delta(Nz)},\qquad
g=E_2(z)-NE_2(Nz)=\frac{1}{2\pi i}\frac{d\log v}{dz}. \tag{3.1}$$
Here $E_2(z)=1-24\sum_{m\ge1}\sigma_1(m)q^m$. The logarithmic
derivative proves modularity of $g$ and its rationality without treating
the level-one quasimodular form as modular. At finite level its exact
arithmetic divisor is
$$\operatorname{div}_{\mathcal X_0(N)}v
 =(N-1)(\mathcal P_0-\mathcal P_\infty)
       +6(\mathcal X_N^0-\mathcal X_N^\infty). \tag{3.2}$$
In particular its vertical term and $N^{-6}$ normalization have not
been discarded. Formula (3.2) is proved with the Du–Yang normalizations
in [arithmetic-green-comparison.md, Proposition 3.2](arithmetic-green-comparison.md).

Set $F(z)=y^2f(z)\overline{g(z)}$, a scalar automorphic function.
Its exponential decay at both cusps makes the following integral and
all its Laurent coefficients well defined:
$$I(s)=\int_{\Gamma\backslash\mathfrak H}F(z)E_\infty(z,s)d\mu.
\tag{3.3}$$

**[NEW] Proposition 3.1 (complete Rankin–Selberg identity).**
$$I(s)=-\frac{24\Gamma(s+1)}{(4\pi)^{s+1}}
       \frac{L(f,s+1)L(f,s)}{\zeta(2s)(1+N^{-s})}. \tag{3.4}$$

*Proof.* First take $\Re s$ sufficiently large for absolute convergence.
Unfold (3.3) to the width-one strip. Write
$$c_m=\sigma_1(m)-N\sigma_1(m/N),$$
with the second term zero if $N\nmid m$. Integration in $x$ kills
the constant coefficient of $g$ and all unequal Fourier indices, giving
$$I(s)=-\frac{24\Gamma(s+1)}{(4\pi)^{s+1}}
                  \sum_{m\ge1}\frac{a_mc_m}{m^{s+1}}. \tag{3.5}$$
The coefficients $c_m$ are multiplicative, with
$c_{p^r}=1+p+\cdots+p^r$ at $p\ne N$ and $c_{N^r}=1$.

For $p\ne N$, let
$A_p(X)=\sum_{r\ge0}a_{p^r}X^r=(1-a_pX+pX^2)^{-1}$.
Then the local series is
$$\frac{pA_p(pX)-A_p(X)}{p-1}
 =\frac{1-p^2X^2}
 {(1-a_pX+pX^2)(1-a_ppX+p^3X^2)}. \tag{3.6}$$
This identity follows by multiplying both denominators: the numerator
is $(p-1)(1-p^2X^2)$. Substituting $X=p^{-w}$ produces the local
factor of $L(f,w)L(f,w-1)/\zeta(2w-2)$.

At the split multiplicative prime, $a_{N^r}=1$, so the required local
factor is $(1-N^{-w})^{-1}$. The corresponding factor in that quotient
of L-functions is
$$\frac{1-N^{2-2w}}{(1-N^{-w})(1-N^{1-w})}
 =\frac{1+N^{1-w}}{1-N^{-w}}.$$
It must therefore be divided by $1+N^{1-w}$. With $w=s+1$ this
gives (3.4). Meromorphic continuation extends the equality. The cusp
decay of $F$ justifies coefficientwise integration near $s=1$ after
subtracting the explicit pole. $\square$

Since $L(f,s)$ has exact order two at one and $L(f,2)\ne0$, the right
side has order two there. Nonvanishing at two follows directly from
the absolutely convergent Euler product: at good primes the Satake
roots have modulus $\sqrt p$, giving summable $O(p^{-3/2})$ terms,
and the bad Euler factor is nonzero. In fact $L(f,2)>0$ since every
real local factor there is positive.

Taking the four Laurent coefficients gives
$$\int Fd\mu=0,\qquad \int FA_0d\mu=0,\qquad
\int FA_1d\mu=0,\tag{3.7}$$
and (1.1), because
$$-\frac{24\Gamma(2)}{(4\pi)^2\zeta(2)(1+N^{-1})}
       =-\frac{9N}{\pi^4(N+1)}.$$
The coefficient is the second Laurent coefficient $A_2$, not its
unhalved second derivative. In particular the analytic source in (1.1)
is nonzero. This is a fixed weight-two central second derivative times
$L(f,2)$, rather than a first derivative of a different-weight L-function.

## 4. The analytic relative class and the spectral jet complex

Let $\overline Y^{\rm BS}$ be the Borel–Serre compactification of the
effective modular **orbifold**, with cusp coordinates $(x,r)$, $r=1/y$,
and its two boundary circles $B$. The elliptic stabilizers in
$\Gamma_0(389)/\{\pm1\}$ are retained; invariant smooth functions
need not be smooth in a coarse branched coordinate at an elliptic point.
The two-form
$$\omega_2=A_2F\,d\mu
 =\frac{i}{8\pi^2}A_2\alpha\wedge\overline{d\log v},
\qquad \alpha=2\pi i f(z)dz, \tag{4.1}$$
is invariant on the full modular curve. The coefficient $F$ decays
exponentially, whereas (2.5) has polynomial/logarithmic growth. In
the coordinate $r$ their product is flat at $r=0$. Hence (4.1) extends
by zero to a smooth relative orbifold form on $(\overline Y^{\rm BS},B)$.
It is closed because it has top degree. Its orbifold integral is (1.1).
Equivalently pull it back to the torsion-free cover from $\Gamma_1(389)$.
The effective index of this cover is $(389-1)/2=194$: $\Gamma_0(N)$
maps onto $(\mathbb Z/N)^\times$ with kernel $\Gamma_1(N)$, and
passing to effective groups divides that index by two since $-I$ is
not in $\Gamma_1(N)$. The integral in (1.1) is precisely $1/194$
times the integral of the pullback over this cover's relative integral
fundamental class. This factor cannot be discarded in an integral
comparison, particularly at 2 and 97. We obtain a relative analytic
de Rham class with its rational orbifold normalization, not an asserted
integral class. No geodesic is first projected to the elliptic quotient.

**[NEW] Proposition 4.1 (inhomogeneous spectral chain).**
$$\Delta A_0=-R,\qquad \Delta A_1=-A_0-R,\qquad
\Delta A_2=-A_1-A_0. \tag{4.2}$$
In particular $\Delta^3A_2=-R\ne0$ and $\Delta^4A_2=0$.

*Proof.* Apply $\Delta E_\infty=s(1-s)E_\infty$ to (2.3), use
$s(1-s)=-t-t^2$, and compare powers of $t$. Applying $\Delta$ twice
more gives $\Delta^2A_2=A_0+2R$ and the stated last two identities.
$\square$

An actual two-term analytic complex packaging these equations is
$$\mathscr A\otimes\mathbb C[t]/t^4
  \xrightarrow{\ \Delta+t+t^2\ }
  \mathscr A\otimes\mathbb C[t]/t^4, \tag{4.3}$$
where $\mathscr A$ consists of smooth automorphic functions with the
polylogarithmic polynomial cusp growth at issue. The element
$$R+tA_0+t^2A_1+t^3A_2$$
is a degree-zero cycle. Its specified boundary is the constant-term
expansion of $t(\delta_{a\infty}y^{1+t}+\phi_{a\infty}(1+t)y^{-t})$
modulo $t^4$. Constant-term restriction is a map to the corresponding
boundary complex with $\Delta_0=-y^2\partial_y^2$. One may retain
the data in its homotopy fiber over this specified boundary cycle,
which is an affine fiber, not the fiber over zero. The boundary must
not silently be set to zero.
The functions themselves have trivial scalar monodromy. Complex (4.3)
is a spectral differential equation, not an algebraic flat connection.

**A precise failed Gauss–Manin identification.** The universal elliptic
curve on the modular stack has integral local system
$\mathbb H=R^1\pi_*\mathbb Z$, with the usual integral
$\Gamma_0(N)\subset\mathrm{SL}_2(\mathbb Z)$ action. This is the
noneffective stack group, distinct from the effective $\Gamma$ used
for scalar functions above: $-I$ acts by $-1$ on $\mathbb H$.
Even symmetric powers descend to the effective orbifold; odd powers
remain on the modular stack or may be pulled back to the torsion-free cover.
Its symmetric powers have ranks $m+1$ and weights $m$; Tate twists and
tensor decompositions remain finite-dimensional algebraic $\mathrm{SL}_2$
representations. Such a representation is a sum of irreducibles, and
its Casimir acts diagonally by scalars. Consequently a nonzero spectral
module containing the chain $A_2$ in (4.2) cannot be embedded into one
of those finite algebraic representations by an intertwiner identifying
its Casimir with the hyperbolic Laplacian: that Laplacian has a nontrivial
nilpotent Jordan block. This tests precisely the proposed direct
homogeneous Gauss–Manin tensor realization. It does not exclude
unipotent relative completions, mixed variations, nonhorizontal gauges,
or new regulator identities after integration.

If one forgets the spectral decoration and keeps only (4.1), rational
relative orbifold cohomology is
$H^2(\overline Y^{\rm BS},B;\mathbb Q)=\mathbb Q$
with its rational orientation line, agreeing with rational coarse
top cohomology. Using the integral marking from the torsion-free cover
requires exactly the degree normalization just specified.
The coordinate of this analytic class is its already evaluated integral.
Choosing an inverse real period map and calling that coordinate rational
would therefore assume the required arithmetic comparison. The actual
rational structures on $\alpha$ and $d\log v$ do not supply a rational
structure on the solution of the spectral chain (4.2).

## 5. Exact finite parts: the modular-unit repair has the wrong symmetry

Put $E_+=E_\infty+E_0$ and $E_-=E_\infty-E_0$. Then
$$E_+(z,s)=\frac{E(z,s)+E(Nz,s)}{N^s+1},\qquad
E_-(z,s)=\frac{E(Nz,s)-E(z,s)}{N^s-1}. \tag{5.1}$$
Let
$$b_0=\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right).$$
The level-one finite part is
$$E(z,1+t)=\frac3{\pi t}+b_0
             -\frac3\pi\log(y|\eta(z)|^4)+O(t). \tag{5.2}$$
For clarity, (5.2) can be checked directly by Poisson summation in
$$E(z,s)=\frac1{2\zeta(2s)}
       \sum_{(m,n)\ne(0,0)}\frac{y^s}{|mz+n|^{2s}}.$$
The nonconstant Fourier expansion is
$$\frac{4\sqrt y}{\xi(2s)}\sum_{m\ge1}m^{s-1/2}
 \sigma_{1-2s}(m)K_{s-1/2}(2\pi my)\cos(2\pi mx),
\quad\xi(2s)=\pi^{-s}\Gamma(s)\zeta(2s).$$
The factor four here counts both nonzero Fourier signs. In this normalization,
the constant term of $\psi(1+t)$ is $b_0$, its residue is $3/\pi$,
and $K_{1/2}(2\pi my)=e^{-2\pi my}/(2\sqrt{my})$ gives the
nonconstant term $(12/\pi)\sum_{m\ge1}\sigma_{-1}(m)e^{-2\pi my}
\cos(2\pi mx)$. The product expansion of $\eta$ identifies this
with $-12\log|\eta|/\pi-y$. This proves the constants as well as
the function in (5.2).

**[NEW] Proposition 5.1 (the two exact finite parts).** For the same
invariant Petersson logarithm
$$U=\log|\eta(z)\eta(Nz)|+\tfrac12\log y+\tfrac14\log N,$$
one has
$$\begin{aligned}
\operatorname{FP}_{s=1}E_+(z,s)
 &=K_N-\frac{12}{\pi(N+1)}U(z),\\
K_N&=\frac{2b_0}{N+1}-\frac{6N\log N}{\pi(N+1)^2},\\
E_-(z,1)&=\frac{\log|v(z)|}{2\pi(N-1)}.
\end{aligned} \tag{5.3}$$
These follow by substitution in (5.1), differentiating its denominators
when they multiply the pole. In particular the $\log N$ in the
normalized unit and the derivative of $N^s+1$ are both necessary.

The Fricke map sends $v$ to $v^{-1}$, so $g|_2W_N=-g$.
Also $f|_2W_N=-f$, hence $F|_0W_N=F$. Consequently
$$\int FE_-(z,s)d\mu=0\quad\text{identically in }s. \tag{5.4}$$
All convergent Laurent coefficients vanish as well. Therefore replacing
the even spectral chain in (1.1) by the rational modular-unit finite part
in (5.3) loses the required nonzero pairing. This is a calculation for
the actual two cusps of level 389, not a general prohibition on using
modular units. The surviving even finite part is the already constructed
Hodge Green function with its curvature and vertical terms.

## 6. A secondary symbol using the actual noncuspidal functions

Let $\pi:X_0(389)\to E$ be the degree-40 modular parametrization,
normalized by $\pi(\infty)=O$. Its cusp image at zero is also $O$,
and $\pi W_N=[-1]\pi$, as in the reviewed relative-cycle note.
Use its explicit moving functions
$$h_1=1-\frac{332}{27(x-4)}+\frac{1040y}{27(x-4)^2},\qquad
h_2=1-\frac{41}{3(x-4)}+\frac{20y}{3(x-4)^2}. \tag{6.1}$$
They were chosen from finite point intersections alone and have $h_j(O)=1$.
The full noncuspidal point divisors and all finite cancellations remain
those of [relative-modular-cycle-attack.md, §§2–4](relative-modular-cycle-attack.md).

The symbols
$$\kappa_j=\{v,\pi^*h_j\}\in K_2^M(\mathbb Q(X_0(389))) \tag{6.2}$$
are concrete secondary candidates incorporating both kinds of data.
Their regulator one-form on the complement of their divisors is
$\log|v|d\arg(\pi^*h_j)-\log|\pi^*h_j|d\arg v$. They must initially
be kept with their tame boundaries; no unramified $K_2$ class is asserted.

**[NEW] Proposition 6.1 (the elliptic transfer is two-torsion).**
The field norm $c=\operatorname{Norm}_\pi(v)$ belongs to $\{1,-1\}$.
For each $j$ the transfer of (6.2) is $\{c,h_j\}$, hence is killed
by two and is zero after rationalization.

*Proof.* On the generic curve, $\operatorname{div}v=(N-1)(0-\infty)$.
Pushing this divisor to $E$ gives zero. Hence the norm is a constant
in $\mathbb Q^\times$, since $E$ is geometrically connected and proper.
Norm commutes with the diagram $\pi W_N=[-1]\pi$. But
$W_N^*v=v^{-1}$, so $c=[-1]^*c=c^{-1}$, proving $c^2=1$.
The transfer projection formula gives
$$\operatorname{Cor}_\pi\{v,\pi^*h_j\}
 =\{\operatorname{Norm}_\pi v,h_j\}=\{c,h_j\}.$$
Bilinearity gives $2\{c,h_j\}=\{c^2,h_j\}=0$. $\square$

The projection formula can be checked in the Bass–Tate definition:
the residue maps in its rational-function exact sequence are linear
over the base Milnor K-ring, so the induced norm is linear over that
ring, and in degree one it is the ordinary field norm. The same residue
construction commutes with finite transfer. Exact statements are in
Elman–Karpenko–Merkurjev, *The Algebraic and Geometric Theory of
Quadratic Forms*, §100, Fact 100.8(2)–(4)
([author text](https://sites.ualberta.ca/~karpenko/publ/Kniga.pdf)).

For example, the tame symbol at a noncuspidal point $x$ in the divisor
of $\pi^*h_j$ is $v(x)^{\operatorname{ord}_x\pi^*h_j}$; at the two
cusps it is one because $h_j(O)=1$. Their transferred products are
the tame symbols of $\{c,h_j\}$, hence have square one. Thus the
rational vanishing does not omit the noncuspidal boundary. Equation
(3.2) remains necessary for an integral arithmetic-surface lift of
(6.2); none is being assumed. The proposition holds already in the
generic residue complex, so adding an unproved integral extension
cannot turn this same transferred rational symbol into the nonzero
spectral period.

## 7. Repair by actual integral character monodromy

There is also an integral local system defined on the full modular
curve. Choose the real period $\omega_1>0$ of
$E$ and write $\pi^*\omega=c_\pi\alpha$, retaining its nonzero rational
Manin factor. For a closed loop define
$$k(\gamma)=\frac{\Re\int_\gamma\pi^*\omega}{\omega_1}\in\mathbb Z.$$
The real component of every elliptic period is an integer multiple of
$\omega_1$ for this rectangular real period lattice. The map $k$ is
an integral homomorphism and vanishes on cusp parabolics. Put
$$\rho_T(\gamma)=(1+T)^{k(\gamma)}\quad\text{in }
       (\mathbb Z[T]/T^3)^\times. \tag{7.1}$$
In the basis $1,T,T^2$ multiplication has integral entries, since
$\binom{k}{2}$ is integral even for negative $k$. This constructs an
actual rank-three integral Betti local system; it is not merely an
arbitrary real rescaling of monodromy. It does not by itself specify
an admissible Hodge filtration or an integral arithmetic regulator.

The corresponding character Eisenstein series is, initially in a
half-plane of convergence,
$$\mathcal E_\infty(z,s,T)
 =\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
       \rho_T(\gamma)^{-1}\Im(\gamma z)^s\pmod{T^3}. \tag{7.2}$$
Parabolic triviality makes the sum well defined, and a change of cosets
gives $\mathcal E_\infty(\delta z,s,T)=\rho_T(\delta)
\mathcal E_\infty(z,s,T)$. It is the truncated Taylor expansion of
the usual unitary-character family under $T=e^{2\pi i\epsilon}-1$.
This provides an actual rank-three local system for the scalar spectral
construction, including its relative cusp condition. Its unipotent
monodromy is not claimed to be a finite group.

A specific proposed extraction from this repair nevertheless vanishes.
Set $w=\Re(\pi^*\omega)/\omega_1$, and let $\dot\Delta$ be the
first derivative of the Laplacian after conjugating the character
family to untwisted functions. With our positive Laplacian,
$$\dot\Delta u=-4\pi i\langle du,w\rangle_{\rm hyp}.$$
Consider precisely the first-response integrals
$$B_{ab}(s)=\int E_a(z,s)\dot\Delta E_b(z,s)d\mu,
\qquad a,b\in\{0,\infty\}. \tag{7.3}$$
The decaying harmonic form $w$ makes them convergent away from the
Eisenstein poles and meromorphic in $s$.

Petridis §4.3, (4.9)–(4.12), computes these bilinear integrals using
the oldform basis, before applying residues to study scattering poles.
Their scalar Dirichlet-series factor is $L(f,1)L(f,2s)$.
Our direction uses the purely imaginary scalar multiple
$2\pi i c_\pi f/\omega_1$ in his convention. His Laplacian sign changes
the overall sign, without affecting vanishing. Thus $B_{ab}(s)=0$
identically. Spectral derivatives vanish as well: equality first holds
off the discrete poles and then as a meromorphic identity. This asserts
the vanishing of (7.3), the specific first-order pole/scattering response
used in that construction. It does not assert vanishing of the full
character Eisenstein jet, nor identify (7.3) with an arbitrary convention
for the full scattering-matrix derivative without its boundary correction.

Thus first varying an honest integral character and then taking more
spectral derivatives of its first scattering response does not recover
$\ell$. A comparison using second character variation, or a mixed
relative extension coupling it directly to the point 1-motive, remains
an actual further construction problem.

## 8. Exact arithmetic comparison still required

The known point 1-motive supplies a genuine integral frame
$$\mathcal T_{\mathbb Z}
 =\det X\otimes\det L\otimes\mathbb Z\gamma_{\mathbb R}
                         \otimes\mathbb Z\omega,$$
whose real realization sends its specified generator to
$\Omega_{\rm full}\det H$. The two point lattices are saturated;
$\gamma_{\mathbb R}=2a$ has index two in the primitive positive real
homology lattice. Every finite local height correction for its chosen
marked divisors is zero by the explicit functions (6.1). These exact
normalizations remain as in the reviewed relative-cycle note.

By (1.1), an arithmetic realization of the new spectral source would
have to compare to $\mathcal T$ **with an additional factor whose real
regulator is $L(f,2)$**, including the explicit multiplier
$-9N/(\pi^4(N+1))$. Constructing such a factor at the level of ordinary
noncentral Beilinson regulators would still not construct the tensor
comparison for the spectral second jet. Nor may it simply be cancelled
as an integral unit. No rational or integral realization of $A_2$ with
that tensor identity has been obtained.

The standard Rankin–Eisenstein theorem does not fill this exact gap.
Kings–Loeffler–Zerbes, [arXiv:1501.03289v2](https://arxiv.org/html/1501.03289),
§§3.4, 5.3 and Theorem 6.2.9, constructs rational motivic classes on
$Y_1(N)^2$ with symmetric-power coefficients and computes a first
leading derivative of the tensor-product L-function in its specified
range. Its $f,g$ eigenspaces are cuspidal; the present $g$ is Eisenstein.
It is not a theorem identifying second spectral derivatives of its
regulator classes with the fixed weight-two BSD determinant. Its use
of rational coefficients also supplies no automatic integral lattice.

**[GAP MV-389]** Construct a rational (and for the interval argument,
integral) secondary comparison carrying the explicit full-curve analytic
class (4.1), or a corrected mixed-character realization of it, into
the above point determinant tensor with the exact scalar (1.1).
The comparison must retain both cusp scattering jets, the Hodge curvature,
the vertical term at 389, the full real-period index two and any
orbifold-cover denominator such as the explicit degree 194 above. The
point/unit Milnor symbol and the first-character scattering repairs
tested here do not provide it. This gap is not filled by defining the
inverse real image of $\ell$ to be rational.
