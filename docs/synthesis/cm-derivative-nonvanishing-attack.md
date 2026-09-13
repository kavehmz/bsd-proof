# An actual nonzero CM derivative and the trivial 5-primary group

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: bounded proof and certificate completed, with a
[full coordinator PASS review](review-cm-derivative-nonvanishing.md)
and a [separate integral-bound PASS audit](review-cm-derivative-integral-bound.md).
Reviewed final mathematical version:
190fdbe54ca357dc2b9ec3dcf3b189da1ee23aa13447b79b5e41cf0757806128.
Completion links are editorial; the reviewed mathematics is unchanged.
Full BSD over Q remains the objective. This note proves a fixed-prime
result for E:y²=x³+39x and tests an explicit uniform continuation.

## 1. Fixed normalization and the certified coefficient

Let E be the displayed global minimal model, with Néron differential
ω=dx/(2y), conductor N=48672, and Cremona label48672i1. Its algebraic
and analytic ranks are exactly two by the existing
[reviewed certificate](../../compute/data/cm39_analytic_rank_certificate.json).
It has negative discriminant and one real component. Thus the full real
Néron period Ω_E equals its least positive real period.

At p=5, a_5=−2 and #E(F_5)=8. Let α be the unit root of
X²+2X+5, and β=5/α. The Iwasawa variable is T=γ−1 with
χ_cyc(γ)=6. We use the precisely Néron-normalized MTT series
L_5(E,T), the SAME series as in the
[derived-unit proof](cm-derived-unit-attack.md). Write c_2=[T²]L_5(E,T).

The new [script](../../compute/scripts/certify_cm39_padic.py) and
[complete exact data](../../compute/data/cm39_padic_derivative_certificate.json)
give
\[
 \boxed{c_2\equiv20\pmod{25},\qquad v_5(c_2)=1.}               \tag{1}
\]
The error bound is proved in §3, not inferred from stabilization.
A second independent finite approximation gives c_2≡70 mod125.

All source normalizations remain those already reviewed:
the unnormalized tame norm degree at5 is18432, the auxiliary
theta integer is a=7, the smoothing divisor is
12(a²−u_a(1+X)^lambda_a(1+Y)^lambda_a), the coefficient is
2pr_ρ(γ_E^+), and X,Y both map to T. The twelfth power,
the Kato N(a)−σ_a sign, and finite ray exponents at least m+1
are unchanged. The modular-symbol computation evaluates the
already identified MTT realization; it does not renormalize
the unit class by an afterward chosen scalar.

## 2. Why the modular symbols have the exact Néron scale

For r∈Q set
\[
 m(r)=\Omega_E^{-1}\Re\left(2\pi i\int_{i\infty}^{r}f(z)\,dz\right),
                                                               \tag{2}
\]
where f is the normalized newform of E. The primary normalization
input is [Agashe–Ribet–Stein, with Cremona's appendix, Theorem5.2](https://wstein.org/papers/ars-manin/agashe-ribet-stein-the_manin_constant.pdf):
below conductor60000 the index-one curve is optimal and its
Manin constant is1, apart from the stated990h labeling exception.
The [primary table row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.40000-49999)
is48672 i 1 [0,0,0,39,0] 2 2; the script checks the identical
cached row. Thus this curve's minimal parametrization π has
π^*ω=2πif dz, with its sign chosen positively.
There is no unresolved Manin-constant assumption.

Since L(E,1)=0, the integral from infinity to zero is zero and
π(0)=π(infinity)=O. Every cusp a/p^n, with p∤N and p∤a,
is Γ_0(N)-equivalent to zero: solve b p^n−aNc=1 for b,c.
Consequently its Abel–Jacobi integral belongs to the period
lattice of E. For a negative-discriminant real elliptic curve,
the real projection of that lattice is (Ω_E/2)Z. Hence
\[
                    m(a/p^n)\in\tfrac12\mathbb Z.             \tag{3}
\]
This proves the required p-integrality at EVERY level for
every odd p∤N, not just for the displayed finite values.

The exact eclib modular-symbol algorithm and its Sage wrapper
are described in the
[official source documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html).
For negative discriminant the wrapper multiplies eclib's
slanted-lattice coordinate by1/2 to obtain (2). The script
checks that factor explicitly. There is no additional real-component
division because E(R) is connected.

As an independent check, every needed symbol was also computed
by Wuthrich's fixed-denominator numerical algorithm, which returns
exact rationals using its proved error and denominator bounds:
[Numerical modular symbols, §§2–4 and7.1](https://arxiv.org/pdf/1608.06423).
Its optimal-Manin-constant premise is supplied by the theorem above.
The installed Sage mini-table warning concerns its database size;
it does not place this curve outside that primary theorem.
The two algorithms agreed on all symbols at denominators25,125,625.

## 3. A direct proved measure-error bound, valid also in the CM case

For an odd good ordinary p define, with α its unit root,
\[
 \mu(a+p^n\mathbb Z_p)
   =\alpha^{-n}m(a/p^n)-\alpha^{-(n+1)}m(a/p^{n-1})
          \quad(p\nmid a).                                   \tag{4}
\]
This is the standard modular-symbol measure. For completeness,
its distribution relation follows from
a_p m(r)=m(pr)+Σ_(j=0)^(p−1)m((r+j)/p), translation invariance,
and α²−a_pα+p=0. Summing the p children in (4) gives
\[
 \alpha^{-(n+1)}(a_pm(a/p^n)-m(a/p^{n-1}))
       -p\alpha^{-(n+2)}m(a/p^n)
 =\mu(a+p^n\mathbb Z_p).
\]
Equation (3) and the unit property of α make μ Z_p-valued.
The bounded compatible distribution defines a measure.

Let ω_p(a) be Teichmüller and put
t(x)=log_p⟨x⟩/log_p(1+p). The normalized series is
\[
 L_p(E,T)=\int_{\mathbb Z_p^\times}(1+T)^{t(x)}\,d\mu(x).
                                                               \tag{5}
\]
This fixes the trivial tame-character SUM, not its average.
The interpolation and period conventions are those of MTT,
also stated in
[Stein–Wuthrich §3](https://wstein.org/papers/shark/shark.pdf)
and the official Sage series documentation. Stein–Wuthrich's
later non-CM standing assumption is unnecessary for the elementary
argument here; (4)–(5) are defined for this modular CM curve.

At level n use bins indexed by 1≤a≤p−1 and0≤j<p^(n−1),
with representative ω_p(a)(1+p)^j. For x in such a bin,
t(x)−j∈p^(n−1)Z_p. Since p≥5,
\[
 \binom{t(x)}2-\binom j2
       =\frac{(t(x)-j)(t(x)+j-1)}2\in p^{n-1}\mathbb Z_p.
\]
Integrating this difference against the integral measure gives
\[
 c_{2,p}-[T^2]P_{n,p}(T)\in p^{n-1}\mathbb Z_p,\quad
 P_{n,p}(T)=\sum_{a,j}\mu(\omega_p(a)(1+p)^j+p^n\mathbb Z_p)(1+T)^j.
                                                               \tag{6}
\]
This is an infinite-tail certificate with an explicit valuation.
It uses no stabilization, regulator value, or BSD assumption.

## 4. Exact finite arithmetic giving20 modulo25

For n=3 and p=5 the Teichmüller representatives modulo125 are
1,57,68,124. Write b_(a,j) for their product with6^j modulo125,
and define the finite RATIONAL sums
\[
 A_3=\sum_{a,j}\binom j2m(b_{a,j}/125),\qquad
 B_3=\sum_{a,j}\binom j2m(b_{a,j}/25).
\]
The data list every summand, including the exact rational symbol.
They give
\[
 A_3=3540,\quad B_3=-275,\quad
 [T^2]P_{3,5}=\alpha^{-3}(3540+275/\alpha).                    \tag{7}
\]
Integer Hensel lifting gives α≡13 mod25; hence α^(-1)≡2.
Reducing (7) gives20 modulo25. Equation (6) makes the
error divisible by25, proving (1).

For the second approximation, the independent finite data give
\[
 A_4=46545,\quad B_4=86450,\quad \alpha\equiv113\pmod{125},
 \quad [T^2]P_{4,5}\equiv70\pmod{125}.                         \tag{8}
\]
Its error is125Z_5 by the SAME theorem. Agreement of (7),(8)
is only an implementation check; either proved residue suffices.

Every finite operation after the modular-symbol calls is rational
or integer arithmetic. The Hensel lifts verify a unique root at
each step, and rational denominators are inverted only modulo
powers of5 to which they are coprime. Sage's displayed p-adic
series is a secondary check, not the source of the error bound.
The existing complex/rank certificate is read and hashed, not rerun.

## 5. Nonvanishing of the ACTUAL derived class and full Selmer corank

Let z_cyc=T w_infty and w_0=Sh(d_pi+d_barpi) be the exact classes
of the reviewed [Iwasawa presentation](cm-iwasawa-presentation-attack.md).
For P=(3,12), the proved full-Selmer height identity is
\[
 h_\Gamma(P,w_0\otimes T)
       =k_\alpha\log_\omega(P)c_2T^2,\qquad
 k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1}).                  \tag{9}
\]
The point P is non-torsion, so its local elliptic logarithm
is nonzero. The Euler factors in k_alpha are nonzero and (1)
gives c_2≠0. Therefore w_0≠0. In particular at least one of the
ACTUAL d_pi,d_barpi is nonzero. Neither class was chosen from
the point space or corrected after the computation.

Corollary4.1 of the presentation consequently gives
\[
 \operatorname{corank}_{\mathbb Z_5}\operatorname{Sel}_{5^\infty}(E/\mathbb Q)=2,
 \qquad \operatorname{Sha}(E/\mathbb Q)[5^\infty]\text{ finite}. \tag{10}
\]
This uses the full Selmer group, retaining any possible Sha
directions until the corank argument removes them.
The certificate does not identify which individual ray
derivative is nonzero, prove their independence, or assert
a specific nonzero Kummer reduction modulo5. Its exact finite
residue is the coefficient20 modulo25.

No normalization factor has changed: ν satisfies
φν=β^(-1)ν and[ω,ν]=1, δ_0=k_alpha^(-1)ν,
g_5=log_5(6), e_5=(1−α^(-1))², and
c_cmp,5=(156iΩ_5)^(-1). Thus the older relation
c_2=c_cmp,5 M_5/(2g_5²) and frame multiplier5/(2#E(F_5))
are retained. We do not restore the withdrawn Coleman
factorization on an arbitrary local generator.

## 6. A direct integral argument upgrades finiteness to triviality

Here we prove the stronger fixed-prime result
\[
                    \operatorname{Sha}(E/\mathbb Q)[5^\infty]=0.
                                                               \tag{11}
\]
No regulator computation or version of Schneider's theorem
outside its stated scope is needed.

Use the actual ordinary Selmer complex C_f from the presentation,
specialized to the cyclotomic line S_5=Z_5[[T]]. Write its square
matrix as A_cyc(T), with constant term A_0. The reviewed exact
identities are
\[
 F(X,Y)=(-1)^b u(X,Y)\det A(X,Y),\quad u\in R^\times,\qquad
 c_2=\iota_5(F_{20}+F_{11}+F_{02}),\quad
 \iota_5=(\exp(\delta_0),e_{L,0})_5.                           \tag{12}
\]
At the base the fixed INTEGRAL Shapiro map identifies this CM
cone with the ordinary Selmer cone of T_5E over Q. The
identification is functorial for the coefficient sequence used below.

**[NEW] Lemma 6.1.** In this nonanomalous case, iota_5 is a
5-adic unit.

*Proof.* The local ordinary representation splits integrally
into the two CM lines. At5, H⁰ of each residual line vanishes:
one has nontrivial cyclotomic inertia, the other unramified
Frobenius α≡3. Local Tate duality therefore gives a perfect
Z_5-valued pairing between their free rank-one H¹ lattices.
Its finite sublattice is the local point completion.

Because #E(F_5)=8, that completion is identified with the
formal subgroup. The Néron formal logarithm identifies it
with5Z_5; this follows from the formal logarithm with leading
coefficient1 and its convergent inverse on5Z_5.
The already fixed exponential identity
P=k_alpha log_omega(P) exp(delta_0) shows that
log_omega(exp(delta_0))=k_alpha^(-1). Its valuation is1:
1−α^(-1) is a unit and1−β^(-1) has valuation−1.
Thus exp(delta_0) is a primitive integral local point.
The vector e_(L,0) is a generator of the opposite quotient
lattice. Perfect local duality makes their pairing a unit. ∎

The local duality and formal/Kummer identifications used here
are the primary statements already checked in Rubin I§§4,6
and [Milne, Arithmetic Duality Theorems, I§3](https://www.jmilne.org/math/Books/ADTnot.pdf).
The same argument in the uniformly nonanomalous prime range
is recorded in Proposition7.2. A merely nonzero Coleman
coordinate at an anomalous prime is not thereby a unit.

**[NEW] Lemma 6.2.** The torsion subgroup of H²(C_f(T_5E))
at the base is naturally isomorphic to Sha(E/Q)[5^infty].

*Proof.* Put V=T_5E⊗Q_5 and W=V/T_5E. The ordinary plus
coefficient is saturated, so0→T→V→W→0 and its plus and
minus local versions are exact. The non-p conductor places
have nontrivial μ_4 inertia on the CM constituents, surviving
modulo5; all their5-primary local cohomology is zero.
At the real place the5-primary Tate terms are zero.
Consequently the ordinary Selmer cone commutes with this
coefficient sequence, giving an exact triangle.

Here its H¹ groups are the classical Selmer groups with the
specified coefficients. At5, H⁰(W^−)=0 because α−1 is a
unit. The finite local condition on W is the image of H¹(W^+):
formal Kummer theory and #E(F_5)=8 identify it with
E(Q_5)⊗Q_5/Z_5. For example H²(T^+)=0 by local duality
with H⁰(W^−), so passage from the integral formal Kummer
lattice to its divisible quotient has no extra finite term.
At bad places both descriptions are zero. Outside the chosen
ramification set the unramified conditions already agree.

By (10), H¹(C_f(V))=E(Q)⊗Q_5 and
H¹(C_f(T))=E(Q)^5-completion: the inverse-limit Kummer
sequence has no Tate-module contribution from finite Sha.
The coefficient long exact sequence therefore gives
\[
 \frac{\operatorname{Sel}_{5^\infty}(E/\mathbb Q)}
      {E(\mathbb Q)\otimes\mathbb Q_5/\mathbb Z_5}
 \simeq
 \ker(H^2(C_f(T))\to H^2(C_f(V)))
 =H^2(C_f(T))_{\rm tors}.
\]
The first quotient is exactly Sha[5^infty]. Rational base
change of the perfect complex gives the final equality.
This proof needs no choice of an integral self-duality sign. ∎

For the cone and exact-coefficient formalism see
[Nekovář, §§3.4 and6.1](https://www.numdam.org/item/AST_2006__310__R1_0.pdf);
the actual local hypotheses have been verified on the page.

*Proof of (11).* Let the square size be d. By (10),
A_0 has rank d−2 over Q_5. Smith reduction over Z_5
puts its nonzero entries in the form5^(a_1),…,5^(a_(d−2))
up to units. Its cokernel torsion has order5^s with
s=Σa_i. By Lemma6.2 this is the order of Sha[5^infty].

The coefficient of T² in det A_cyc(T) is, up to a unit,
\[
               5^s\det B,                                  \tag{13}
\]
where B is the lower-right2×2 block of the linear coefficient
after this INTEGRAL Smith change of bases. Every other
determinant term needs at least three T-factors.
In particular B has Z_5 entries; no inverse Smith factor is used.

Equations (1),(12) and Lemma6.1 give
v_5([T²]det A_cyc)=1. Thus (13) implies s≤1.
The finite5-primary Cassels–Tate pairing is nondegenerate and
alternating, since E has its rational principal polarization;
its order is a square. Hence s is even, forcing s=0.

The precise primary pairing facts are in Milne I§6:
the rational-divisor polarization gives alternation, and
Theorem6.26 identifies the kernels with the divisible
subgroups. Apply the full Sha pairing; the now finite
5-primary subgroup has zero divisible kernel. This does
not assume finiteness of the other primary components. ∎

The same argument implies that the cyclotomic Bockstein is
nondegenerate on the two-dimensional point space. Its height
identification gives Reg_5≠0. A numerical regulator or its
exact valuation is not asserted by this certificate.

## 7. An actual uniform finite-sum mechanism, and its unresolved step

The measure argument (3)–(6) applies to EVERY good split
p≥5 for this fixed curve, using the same Néron modular-symbol
map. Define A_(n,p),B_(n,p) by the sums in §4 with125,25
replaced by p^n,p^(n−1). Then
\[
 c_{2,p}\equiv\alpha^{-n}(A_{n,p}-\alpha^{-1}B_{n,p})
                         \pmod{p^{n-1}}.                    \tag{14}
\]
This gives a uniform finite algorithm, not an inference
from a list of sampled primes.

There is an exact simplification at levels2 and3.
Let m be the fixed symbol (2), γ=1+p, and put
\[
 A_{2,p}=\sum_{a=1}^{p-1}\sum_{r=0}^{p-1}
       \binom r2 m(\omega_p(a)\gamma^r/p^2),
\]
\[
 C_p=\sum_{a=1}^{p-1}\sum_{r,t=0}^{p-1}
       t(2r-1)m(\omega_p(a)\gamma^{r+pt}/p^3).
\]
Residues of the Teichmüller values suffice at each denominator.

**[NEW] Proposition 7.1.** For every such p,
\[
 \boxed{c_{2,p}\equiv
       \alpha^{-2}A_{2,p}+\frac{p}{2\alpha^3}C_p\pmod{p^2}.} \tag{15}
\]

*Proof.* Write j=r+pt. The difference of binomial weights is
pt(2r−1)/2+p²t²/2. Sum first over t in the level-three
measure; its distribution relation gives the level-two
measure. Modulo p² the quadratic t² term disappears, leaving
P_3[2]−P_2[2] congruent to
(p/2)Σ t(2r−1)μ_3. In that latter sum modulo p, the
second modular-symbol term of μ_3 is independent of t;
Σt=p(p−1)/2 kills it. The remaining sum is α^(-3)C_p.

Moreover B_(2,p)=binom(p,3)Σ_(a=1)^(p−1)m(a/p)=0:
the Hecke relation at0 gives that inner sum as
(a_p−2)m(0)=0. Thus P_2[2]=α^(-2)A_(2,p).
Combine this with the level-three error p² in (6). ∎

For the actual5-adic certificate the complete rational rows give
\[
 A_{2,5}=-5,\qquad C_5=237.
\]
Equation (15) contributes5+15=20 modulo25. The second term
is essential: treating the level-two approximation as accurate
modulo25 would give the WRONG residue5. This is a concrete
test of the carry term, not merely a symbolic bound.

If A_(2,p) is nonzero modulo p, (15) certifies nonvanishing
immediately. If it is divisible by p, the next test is
\[
 \alpha\,A_{2,p}/p+C_p/2\not\equiv0\pmod p.                  \tag{16}
\]
At5 its residue is3. Whenever either test proves
v_p(c_(2,p))≤1, the same nonanomalous local and Smith/Cassels
argument proves Sha(E/Q)[p^infty]=0. Nonanomalousness for
all these primes was already proved in the local-condition
note; it is not extrapolated from5.

**[NEW] Proposition 7.2 (uniform coefficient bound).** For every
good split p≥5 of this E, the local coordinate iota_p is a
p-unit. If c_(2,p)≠0, then Sha(E/Q)[p^infty] is finite and
\[
 0\le v_p\#\operatorname{Sha}(E/\mathbb Q)[p^\infty]
 \le 2\left\lfloor\frac{v_p(c_{2,p})}{2}\right\rfloor.         \tag{16a}
\]
In particular v_p(c_(2,p))≤1 forces that primary group to be zero.
No nonvanishing or valuation bound at another prime is asserted.

*Proof.* Nonanomalousness was proved uniformly for this curve:
rational two-torsion makes #E(F_p) even; Hasse puts it strictly
between0 and2p for p≥7, so it cannot be a multiple of the
odd prime p. At5 it is8. Thus α−1 is a unit throughout
the stated range. The CM splitting is integral, its two
residual local characters have no invariants, and
v_p(k_alpha^(-1))=1. Formal logarithm identifies the local
point completion with pZ_p. Exactly as in Lemma6.1,
exp(delta_0) is primitive and integral Tate duality proves
iota_p∈Z_p^×.

If c_(2,p)≠0, (9) and the reviewed corank criterion first
give corank two and finite Sha[p^infty]. At every bad
place the nontrivial μ_4 inertia character remains nontrivial
modulo this p; at p the ordinary quotient has H⁰(W^-)=0;
the real Tate terms vanish because p is odd. Therefore
Lemma6.2's exact coefficient-sequence argument applies
unchanged, identifying the torsion of base H² with this
finite primary Sha. The normalized determinant basis,
the iota_p-unit result and integral Smith reduction give
v_p#Sha[p^infty]≤v_p(c_(2,p)). Cassels alternation makes
the left side even. This proves (16a). ∎

I tried to remove the remaining weighted term using the actual
Hecke and distribution relations. The calculation yields (15),
with the NEW carry sum C_p still present. It establishes
neither (16) at all primes nor a bound on its exceptional primes.
A zero test modulo p² also does not prove c_(2,p)=0:
higher levels can still certify it. The precise uniform
nonvanishing statement needed by this route is
\[
 \forall p\text{ good split},\quad
 \exists n\ge3:\ 
 \alpha^{-n}(A_{n,p}-\alpha^{-1}B_{n,p})
                      \not\equiv0\pmod{p^{n-1}}.             \tag{17}
\]
By (14), (17) is equivalent to c_(2,p)≠0 at every such p.
It has not been proved.

The proposed shortcut using known CM height nonvanishing
does not currently establish (17). Nonvanishing of a pairing
does not prove nondegeneracy of its rank-two Q_p matrix.
Even control on rational-point directions would not by itself
exclude a kernel with nonrational coefficient ratio. We use
no stronger assertion about each individual self-height here.
The distinction between nonvanishing and nondegeneracy is explicit in
[Burungale–Disegni, introduction](https://www.numdam.org/item/10.5802/aif.3381.pdf).
Here E(K) has rank TWO over Z[i], not one. CM multiplication
does not reduce the present point determinant to that rank-one
case. No rationality of the hypothetical kernel ratio has
been derived from the finite unit norms.

## 8. Rational comparison and review boundary

We now have a nonzero actual w_0 at5, full Selmer corank two,
and the trivial5-primary Sha group. These are fixed-prime
conclusions for this curve, not a result at every prime.

The integral Iwasawa determinant basis specializes to a
5-adic determinant, now with its point-space identification
available at5. Its coordinate is still a5-adic scalar.
The finite congruences do not identify it with one rational
framed element before separate completions. The exact real
and all-local target remains CM-Presentation-BSD, including
c_cmp,p, the nonunit regulators where present, and the
required real realization (L''(E,1)/2)/(2Ω_E).
The actual local reference C_v is not replaced by H_global/2.

Reproduction from the repository root:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39_padic.py
```
The script contains the corresponding executable shell command.
It records all finite symbol rows, Hensel residues, bounds,
source normalization, source/data hashes and the carry identity.
An initial implementation repeated individual numerical
integrations; it was stopped and replaced by the source's
fixed-denominator routine, checking the SAME values.
No old rank, analytic or regulator certificate was rerun.

The [full review](review-cm-derivative-nonvanishing.md) includes
independent reproduction of the script and every finite-sum check.
The [separate audit](review-cm-derivative-integral-bound.md) verifies
the integral Selmer, Smith and Cassels argument and its uniform
conditional scope. Both passed. No all-prime nonvanishing or rational
global comparison is proved. Full universal BSD remains unresolved.
