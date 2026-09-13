# Actual CM division-torsor reciprocity and its surviving relative data

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: bounded construction completed with a
[full independent PASS review](review-cm-symbol-point-reciprocity.md).
Reviewed mathematical revision:
6f08e8f4e1d3142436fb3bbcf1f631d4023448b9070bb36f6e1ed0924b63e22f.
Completion links are editorial; the reviewed mathematics is unchanged.
Restart: [checkpoint](cm-symbol-point-reciprocity-checkpoint.md).
The input is the completed [uniform carry/index theorem](cm-uniform-carry-attack.md)
and its [PASS review](review-cm-uniform-carry.md).
Full BSD over Q remains the objective. No old certificate is rerun.

This note constructs the translated theta units on the actual Kummer
division torsors of the full point basis. It computes their complete
Galois groups and norm multiplicities, tests the proposed transfer
and its first relative point augmentation, and then constructs an
exact cubical norm and its nonzero rational leading coefficient.
The latter has nonzero p-adic logarithm uniformly, but its corrected
canonical height component is zero. These precise arithmetic tests
do not prove nonvanishing of c2,p or the rational BSD frame.

## 1. The fixed objects and source normalization

Keep
\[
 E:y^2=x^3+39x,\quad K=\mathbf Q(i),\quad {\cal O}=\mathbf Z[i],
 \quad P=(3,12),\quad Q=(27,144),\quad P+Q=(1/4,25/8),
 \quad\omega=dx/(2y).
\]
P,Q are the full rational basis modulo torsion. Fix
\[
 \Omega_\infty=(1+i)\Omega_E/2,\quad
 f_0=39(1+i)^3,\quad\mathfrak f=(f_0),\quad
 \Delta_E=-64\cdot39^3,\quad \tau_m=\Omega_\infty/(f_0p^m).
\]
We work at
\[
 p\ge5,\quad p\equiv1\pmod4,\quad p\nmid2\cdot3\cdot13.       \tag{1}
\]
Let F_m=K(f p^m), including F_0=K(f). The points tau_m are
defined over F_m. For example CM reciprocity on E[f p^m]
is trivial on principal generators congruent to1 modulo f p^m;
the conductor condition is already included in that modulus.
Write p=pi bar(pi) using the fixed Hecke-character generators.

The rational function is exactly the preceding one:
\[
 \Theta_a(Z)=a^{-12}\Delta_E^{a^2-1}
          \prod_{0\ne T\in E[a]}(x(Z)-x(T))^{-6}
            =\Delta_E^{a^2-1}\psi_a(Z)^{-12},                \tag{2}
\]
where a=5 except a=7 at p=5, and psi_a is the normalized odd
division polynomial. Its divisor is
12(a²[O]−sum_(T in E[a])[T]). The twelfth power is retained.

The primary [Kato2004, Proposition1.3(1)(ii),(4) and proof1.10](https://www.numdam.org/article/AST_2004__295__117_0.pdf)
gives the EXACT distribution
\[
       \prod_{[n]Z=W}\Theta_a(Z)=\Theta_a(W)
                  \quad((n,a)=1,\ W\notin E[a]).            \tag{3}
\]
This is the norm on the full finite étale fiber, not a norm on
only its primitive ray orbit. The constant is1, by Kato's
normalization and the previously checked identification of its
twelfth power with(2). It is not an equality only up to a root
of unity. The original increasing ray-exponent norm law and
[Schmitt, Definition3.12/Proposition3.13](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf)
remain distinct, compatible inputs.

For comparison with the actual class, retain
\[
 \rho=(\Psi^c)^{-1},\quad \mathbf Z_p(1)\otimes\rho=T_\pi E,
 \quad \gamma_{\rm CM}=2\operatorname{pr}_\rho(\gamma_E^+).
\]
The unnormalized tame norm degree is1152(p−1)^2. The normalized
Kato smoothing factor is
\[
 q_a(X,Y)=12\{a^2-u_a(1+X)^{\lambda_a}(1+Y)^{\lambda_a}\},
 \quad u_a=\Psi^c((a)),\quad\lambda_a=\log_p(a)/g_p,
 \quad g_p=\log_p(1+p).                                    \tag{4}
\]
It is the already proved unit, including its sign. The quotient
X,Y→T uses chi_cyc(gamma)=1+p, with no factor1/2.
All finite coefficient constructions below impose m≥k and
m≥n+1 when the target is the nth cyclotomic layer K_n=K Q_n.
The previous local coordinate iota_p, determinant unit u(0),
CM-to-Néron factor c_cmp,p=(156i Omega_p)^(-1), and the exact
Smith-frame units are not altered anywhere in this note.

## 2. The complete actual Kummer translation group

Choose compatible division points [p^m]P_m=P and [p^m]Q_m=Q
only to name field embeddings. Intrinsically they are the two
finite étale division torsors. Put
\[
                         M_m=F_m(P_m,Q_m).
\]

**[NEW deduction] Proposition2.1.** The extension M_m/F_m is Galois and
\[
 \operatorname{Gal}(M_m/F_m)
        \xrightarrow{\sim}E[p^m]\oplus E[p^m],\quad
 \sigma\longmapsto(\sigma P_m-P_m,\sigma Q_m-Q_m).            \tag{5}
\]
This is independent of changing the named division points.
In particular [M_m:F_m]=p^(4m). For any one of P,Q,P+Q,
the corresponding single-point extension has degree p^(2m).
No Selmer-corank or Sha-finiteness hypothesis is used.

*Proof of the ray and lattice inputs.* The modulus f injects the
four Gaussian units. The ray-class description gives
\[
 \operatorname{Gal}(F_m/F_0)\simeq({\cal O}/p^m)^\times
  \simeq(\mathbf Z/p^m)^\times\times(\mathbf Z/p^m)^\times.
\]
Indeed, represent a ray class in this kernel by a residue whose
f-component is1; the global unit used to obtain this representative
is unique. CRT permits any two p-components. For a principal ideal
with generator1 modulo f, its action on the Tate module is that
generator, by the arithmetic CM reciprocity convention in
Kato15.8 and the [reviewed ray-generator proof](cm-two-variable-jet-attack.md).
Thus the image on E[p^m] is the COMPLETE split Cartan even after
F_0 is fixed. In particular the element with p-components(−1,−1)
and f-component1 is central in Gal(F_m/K), has order two,
fixes F_0 and acts by minus identity on E[p^m].

The full integral point lattice is also known here, not assumed
from the rational rank alone. Complex conjugation splits
E(K)⊗Z_p into its plus and minus parts because2 is invertible.
The plus part is E(Q)⊗Z_p, and multiplication by i identifies
the two parts. The known full rational basis therefore gives
\[
 E(K)\otimes\mathbf Z_p
       =({\cal O}\otimes\mathbf Z_p)P
          \oplus({\cal O}\otimes\mathbf Z_p)Q.               \tag{6}
\]
There is no odd-primary torsion: the full split Cartan has no
invariant vector on E[p]. This also follows from the preceding
reviewed CM descent lemma.

*Proof of(5).* Write G=Gal(F_m/K). A central element acting as−1
kills H¹(G,E[p^j]) for every j≤m. Explicitly for a cocycle z
and a central h,
(h−1)z(g)=(g−1)z(h); hence (h−1)[z]=0 in cohomology.
Since h−1=−2 is invertible, H¹ is zero. Inflation–restriction
therefore injects the global Kummer classes into their restrictions
to G_(F_m). This is the elementary homothety argument; no
semisimplicity in characteristic p is assumed.

Let W be the image in E[p^m]^2 of the pair of restricted Kummer
cocycles. It is stable under the split Cartan. Its reduction modulo p
splits into its two Cartan-character components: the operators
(2,1)−(1,1) and(1,2)−(1,1) give the two projectors, since p≥5.
If either component were a proper subspace of F_p², a nonzero
linear functional annihilating it would give coefficients
b_1,b_2 in O/p, not both zero, such that the restriction of
kappa_p(b_1P+b_2Q) vanishes. Its other Cartan component is zero
by this choice of coefficients. Kummer injectivity and the just
proved inflation–restriction injection would then give a nonzero
relation between P,Q in E(K)/pE(K), contradicting(6).

Thus W maps onto E[p]^2. Nakayama over Z/p^m now gives
W=E[p^m]^2. The field generated by the two division points is
Galois over F_m because all torsion translations already lie in
F_m, and its Galois group is precisely that cocycle image.
Changing P_m,Q_m by torsion does not change their differences
under G_(F_m). Projection to either factor, or their sum,
proves the single-point assertions. ∎

This proof also gives
\[
 [F_{m+1}:F_m]=p^2,\qquad [M_{m+1}:M_m]=p^6.                 \tag{7}
\]
The second equality is a ratio of the now proved total degrees,
using the actual compatible inclusions.

## 3. Translated theta values, exact norms and a uniform finite boundary

For R=P,Q,P+Q, take R_m=P_m,Q_m,P_m+Q_m respectively and put
\[
 u_{R,m}=\Theta_a(\tau_m+R_m),\qquad
 w_R=\Theta_a(\tau_0+R)\in F_0^\times.                        \tag{8}
\]
Every value is nonzero and finite. For example if tau_m+R_m
were a-torsion, multiplying by p^m would make the non-torsion
point tau_0+R torsion, a contradiction.

**[NEW deduction] Proposition3.1.** The actual field norms satisfy
\[
 N_{M_m/F_m}(u_{R,m})=w_R^{p^{2m}},\qquad
 N_{M_{m+1}/M_m}(u_{R,m+1})=u_{R,m}^{p^4}.                  \tag{9}
\]
The exponent p^(2m) is an UNUSED point-direction multiplicity;
the exponent p^4 is a TOWER multiplicity. They are different.

*Proof.* In(5), the value for P depends only on its first translation
coordinate. Each of its p^(2m) translates occurs p^(2m) times.
Their product is w_P by(3). The same holds for Q. For P+Q the
addition map E[p^m]^2→E[p^m] has fibers of size p^(2m), giving
the same formula.

Every conjugate of tau_(m+1)+R_(m+1) over M_m is a p-division
point of tau_m+R_m. The subgroup fixing F_(m+1),P_m,Q_m contains
all E[p]^2 translations by Proposition2.1, so all p² such division
points occur. The degree of the full extension is p^6 by(7);
each therefore occurs p^4 times. Equation(3) gives the second
formula. ∎

For fixed a the units have a genuinely uniform finite boundary.
Let S_a be the finite set of places of F_0 containing those over
6a Delta_E and those where one of
[a](tau_0+P), [a](tau_0+Q), [a](tau_0+P+Q)
reduces to O. These are nonzero algebraic points, so the latter
set is finite, as seen from their coordinate denominators.
At any place outside S_a the elliptic scheme is smooth and
Theta_a is invertible away from E[a]. If a division point in(8)
specialized into E[a], its p^m-multiple would contradict the
definition of S_a. Thus all u_(R,m) are S_a-units in their actual
fields. This set is independent of p and m for the a=5 family;
a=7 adds a second fixed finite set. No prime scan or primary Sha
finiteness is used. The statement is about this new unit source,
not about a finite exceptional set for BSD.

The single-point field M_m^R=F_m(R_m) instead satisfies
\[
                         N_{M_m^R/F_m}u_{R,m}=w_R.           \tag{10}
\]
This is a legitimate alternative norm without the unused point
direction. It is not yet the original ray-class elliptic-unit norm.

## 4. The natural full transfer is exactly zero

For k≤m and m≥n+1, the finite modules mu_(p^k) and rho mod p^k
are trivialized by F_m. One can therefore imitate the original
finite twisted transfer, with the SAME compatible rho vector:
\[
 z^{R,\mathrm{joint}}_{n,k;m}
  =\operatorname{Cor}_{M_m/K_n}
      \bigl(\delta_k(u_{R,m})\otimes t_{\rho,k}\bigr)
       \in H^1(K_n,T_\pi/p^k).                              \tag{11}
\]

**[NEW deduction] Proposition4.1.** Every class in(11) is zero.
The single-point version using M_m^R in place of M_m is also zero.

For the joint version, first corestrict to F_m. Kummer norm
compatibility and(9) give
p^(2m) delta_k(w_R) tensor t_rho,k=0. This is zero in the
FULL finite coefficient module, not just modulo a selected
local quotient.

For the single-point version, (10) gives delta_k(w_R) tensor
t_rho,k over F_m. The central homothety h constructed in§2
fixes F_0 and hence w_R. Its cyclotomic character is1 modulo
p^m, so it fixes K_n, whereas rho(h)=−1 modulo p^k. It therefore
acts as−1 on this twisted Kummer class. Corestriction to K_n is
invariant under h; since2 is invertible, that corestriction is
zero. This proves both assertions.

All the operations in this paragraph use exact norms before any
tame projector. Dividing by the unit(4), taking X,Y→T, or applying
the previous determinant/local frame units cannot change this
zero into the original class. The old certified actual w_0 at5
is nonzero, so(11) cannot realize it. This conclusion is about
the displayed complete transfer, not the raw translated units
or every possible operation on their relative data.

An ordinary cup with a point class pulled back from the base does
not repair it: the projection formula cups that point with the
same zero transferred class. Such a cup also has cohomological
degree two and is not thereby an element of H¹(T_pi).

## 5. A canonical relative norm class retains the actual trivialization

The preceding trace has lost data. There is a concrete relative
construction before taking that trace.

Let B_m be the finite étale F_m-algebra of the PRODUCT of the
division torsors of P and Q. Proposition2.1 says it is a field,
identified with M_m after naming division points. Let
\[
 {\cal T}_m=\ker\{N:\operatorname{Res}_{B_m/F_m}\mathbf G_m
                                             \to\mathbf G_m\}.
\]
Its finite coefficient module fits the exact sequence
\[
 0\to{\cal T}_m[p^k]\to
     \operatorname{Res}_{B_m/F_m}\mu_{p^k}
       \xrightarrow{N}\mu_{p^k}\to0.                       \tag{12}
\]
Over a separable closure the last map is the product of all
coordinates, so it is surjective even when p divides the degree.

For each actual unit(8), choose the SPECIFIED norm root
\[
                         r_{R,m,k}=w_R^{p^{2m-k}},
                 \qquad k\le m.                            \tag{13}
\]
Then Norm(u_R,m)=r_R,m,k^(p^k) exactly. Define the finite torsor
\[
 {\cal X}_{R,m,k}=
 \{v\in\operatorname{Res}_{B_m/F_m}\mathbf G_m:
              v^{p^k}=u_{R,m},\ N(v)=r_{R,m,k}\}.            \tag{14}
\]
It is a torsor under T_m[p^k] and gives
\[
          \widetilde\kappa_{R,m,k}
                       \in H^1(F_m,{\cal T}_m[p^k]).         \tag{15}
\]

To verify existence, choose p^k-th roots of all conjugate units.
Their product differs from r by a p^k-th root of unity; change
one root to obtain the prescribed product. Any two resulting
choices differ by T_m[p^k], so their cocycles are cohomologous.
Thus (15) uses the explicit arithmetic root(13), not an arbitrary
cohomological primitive. Its forgetful image is the Kummer class
of u_R,m. Neither that class nor(15) is asserted zero.

This is an integral finite norm-torus object. Its geometric
coefficients are the augmentation kernel of a permutation
module tensored with mu_(p^k), so they have the toric Tate
weight. Twisting by the fixed rho changes that Tate factor to
T_pi; it does not remove the permutation kernel. Shapiro to
K_n then has the corresponding induced kernel coefficients,
not simply T_pi and not a Mordell–Weil determinant.

The root data respects the same multiplicity as the units:
\[
 N_{F_{m+1}/F_m}(r_{R,m+1,k})=r_{R,m,k}^{p^4}.
\]
Together with(9), first restricting scalars from F_(m+1) to F_m
gives a norm map from Res_(F_(m+1)/F_m) X_(R,m+1,k) to the
p^4-power torsor defined by
(u_(R,m)^(p^4),r_(R,m,k)^(p^4)), over F_m. Its coefficient
map is induced by N_(M_(m+1)/M_m); the target is not the
unmodified X_(R,m,k). No integral
norm-compatible Iwasawa class is inferred by silently dividing
these powers out.

## 6. Its first point-Kummer augmentation also vanishes

Let H_m=Gal(M_m/F_m), canonically identified with E[p^m]^2 by(5).
After splitting(12), its kernel is I_m tensor mu_(p^k), where
I_m is the augmentation kernel of (Z/p^k)[H_m].
There is a canonical first-augmentation map
\[
 I_m\otimes\mu_{p^k}\longrightarrow
  (H_m\otimes\mathbf Z/p^k)\otimes\mu_{p^k},\quad
 \sum_h[h]\otimes z_h\longmapsto\sum_h h\otimes z_h.          \tag{16}
\]
Here the sum of z_h is zero in additive notation. Translating
the chosen origin of the division torsor changes the right side
by a multiple of that zero sum. Translation acts trivially on
I_m/I_m², so(16) is G_(F_m)-equivariant. Multiplication by
p^(m−k) identifies H_m tensor Z/p^k with E[p^k]^2.

**[NEW deduction] Proposition6.1.** The image of(15) under(16)
is zero for each R=P,Q,P+Q and k≤m.

*Proof.* Write translations as(v,w) in E[p^m]^2. For R=P,
choose a p^k-th root a_v of Theta_a(tau_m+P_m+v) and use
that same root in every w-coordinate. Then
\[
 \left(\prod_v a_v\right)^{p^k}=w_P,\qquad
 \prod_{v,w}a_v
       =w_P^{p^{2m-k}}=r_{P,m,k}.
\]
The possible root-of-unity factor disappears because p^k
divides p^(2m). Thus these roots represent the EXACT torsor
(14), not a different norm-root choice.

For any Galois element the resulting kernel cocycle z_(v,w)
is independent of w. Its first v-weighted sum has a factor
p^(2m), hence is zero modulo p^k. Its w-weighted sum is zero
because the sum of all elements of E[p^m] is zero for odd p.
This proves the assertion for P; Q is identical.

For P+Q choose roots depending only on v+w. Their product
again is precisely r. For each fixed sum t, the sum of the
first coordinates over v+w=t is zero; the sum of the second
is p^(2m)t minus that zero sum, also zero modulo p^k.
Both components of(16) therefore vanish at the cocycle level. ∎

After the original rho twist the potential target is
H¹(F_m,E[p^k]^2 tensor T_pi/p^k). Its two CM types involve
Psi² and Psi Psi^c=chi_cyc. It is not H¹(T_pi).
Both types of the image are actually zero here, before further
corestriction. This precise first-augmentation failure does
not assert that every higher relative operation is zero.

## 7. A nonconstant cubical norm and a uniform nonzero rational logarithm

A further alternative avoids complete Kummer-field trace by
taking the norm on the FULL TORSION FIBER itself. Over a field
containing P_m,Q_m, let S range over [p^m]^(-1)(tau_0), and set
\[
 {\cal C}_{a,m}(S)=
 \frac{\Theta_a(S+P_m+Q_m)\Theta_a(S)}
      {\Theta_a(S+P_m)\Theta_a(S+Q_m)}.
\]
All denominators are nonzero. Applying(3) to the four translates gives
the exact identity
\[
 \boxed{\ N_{[p^m]^{-1}(\tau_0)}{\cal C}_{a,m}
  =C_a(\tau_0;P,Q):=
  \frac{\Theta_a(\tau_0+P+Q)\Theta_a(\tau_0)}
       {\Theta_a(\tau_0+P)\Theta_a(\tau_0+Q)}\ }.             \tag{17}
\]
It descends to F_0 and is independent of all division-point choices.
It is an actual finite étale algebra norm; replacing it by the
primitive ray-orbit norm would require the extra imprimitive/Euler
terms. We do not identify it with the c2,p norm map.

As a rational function of Z on the FIXED curve,
C_a(Z;P,Q) is nonconstant. The four E[a]-cosets obtained by
translating by0,−P,−Q,−P−Q are pairwise distinct: any coincidence
would make a nonzero integral combination of the independent
P,Q torsion. Its divisor has nonzero coefficient12(a²−1) at O.
This is a statement about the actual rational points, not a
formal set of height variables.

There is an exact rational leading coefficient using the Néron
logarithmic parameter z at O:
\[
 \lim_{z\to0}z^{-12(a^2-1)}C_a(z;P,Q)
       =\left(\frac{\psi_a(P)\psi_a(Q)}
                         {a\psi_a(P+Q)}\right)^{12}
       =:L_a.                                              \tag{18}
\]
Indeed Theta_a(z) has leading term
a^(-12)Delta_E^(a²−1)z^(12(a²−1)), and substituting(2)
in the remaining three values cancels Delta_E exactly.

Here the quantities in(18) can be computed without a prime scan.
The normalized recurrences
\[
 \psi_2=2y,\quad\psi_3=3x^4+234x^2-1521,\quad
 \psi_4=4y(x^6+195x^4-7605x^2-59319),
\]
\[
 \psi_5=\psi_4\psi_2^3-\psi_3^3,\qquad
 \psi_7=\psi_5\psi_3^3-\psi_2\psi_4^3
\]
give the following REDUCED rational twelfth roots:
\[
 L_5^{1/12}:=
 -\frac{1492700558910669067654726813552214016}
         {271426765008565945},                             \tag{19}
\]
\[
 L_7^{1/12}:=
 -\frac{266925654420752446498484046547590250519297111413581743180410149966708736}
 {16649882913528832821767144028348047}.                      \tag{20}
\]
The notation denotes the specified signed rational ratio in(18);
it is not a choice of a new algebraic root. Direct exact Fraction
arithmetic at P,Q,(1/4,25/8) produced these values. For reproduction,
the intermediate psi5 values are
−74381188032,1196161138641941568,54285353001713189/16777216;
the psi7 values are
3611350396045312782336,262591640158166435735154012666064896,
−2378554701932690403109592004049721/281474976710656.

**[NEW deduction] Corollary7.1.** For every odd prime p,
log_p L_5 and log_p L_7 are nonzero, using log_p(p)=0.

For a nonzero rational number r, log_p(r)=0 implies
r=±p^j: after removing its p-power, the remaining rational
number is a p-adic root of unity, hence the rational root
of unity±1. Conversely these are in the kernel. Both reduced
numerator and denominator in(19),(20) have absolute value
greater than1, so neither ratio is of this form for ANY p.
Taking the twelfth power does not kill a nonzero logarithm.
This proves a genuine uniform nonvanishing result for the
specified auxiliary reciprocity quantity. It is not a
nonvanishing theorem for c2,p.

## 8. Exact comparison with the point-sigma recipe

Let sigma be the fixed CM sigma with Néron logarithmic coordinate,
and write the Poincaré section
\[
 {\cal B}_Z(X,Y)=
       \frac{\sigma(Z+X+Y)\sigma(Z)}
            {\sigma(Z+X)\sigma(Z+Y)}.
\]
Consistent complex lifts, or the matching Coleman realizations,
give from the exact sigma division identity
sigma(aX)=sigma(X)^(a²)psi_a(X) the equality
\[
 C_a(Z;P,Q)=
       \frac{{\cal B}_Z(P,Q)^{12a^2}}
            {{\cal B}_{aZ}(aP,aQ)^{12}}.                    \tag{21}
\]
The individual B are sections with their quasiperiod factors;
the ratio cancels those factors and is the rational function
already constructed in(17). Constants and the twelfth power
are not omitted. The sigma division identity is primary
[Mazur–Stein–Tate, (1.2)–(1.3)](https://wstein.org/papers/pheight/pheight.pdf),
with the same differential as in the reviewed finite recipe.

At Z=O its regularization gives(18); the factor a there comes
from sigma(aZ)~aZ and is essential. Thus this operation computes
an ISOGENY-SMOOTHING DEFECT of the Poincaré section, not its
unsmoothed bilinear height.

Here is the exact finite-correction test. Put X=n_pP,Y=n_pQ,
n_p=8#E(F_p), as in the completed point recipe, and
\[
 D(X,Y)=\frac{d(X+Y)}{d(X)d(Y)},\quad
 \Theta_\sigma(X,Y)=\frac{\sigma(X+Y)}{\sigma(X)\sigma(Y)}.
\]
The ACTUAL point Bockstein entry is
\[
 B_p(P,Q)=\frac{\log_p D(X,Y)-\log_p\Theta_\sigma(X,Y)}
                                  {n_p^2 g_p}.             \tag{22}
\]
All points here and their a-multiples are in the prescribed
formal and bad identity components. This is the already
reviewed finite-height normalization, including the denominator
contributions from every finite place.

If f_a(X,Y)=psi_a(X+Y)/(psi_a(X)psi_a(Y)), then
\[
 \Theta_\sigma(aX,aY)=\Theta_\sigma(X,Y)^{a^2}f_a(X,Y).
\]
Bilinearity of the canonical height, with the SAME finite
corrections, consequently gives
\[
 \log_p\frac{D(aX,aY)}{D(X,Y)^{a^2}}=\log_p f_a(X,Y).         \tag{23}
\]
In particular, if L_a(X,Y) denotes(18) at X,Y, the actual
corrected reciprocity identity is
\[
 \log_p\left[
 a^{12}L_a(X,Y)
       \left(\frac{D(aX,aY)}{D(X,Y)^{a^2}}\right)^{12}
          \right]=0.                                      \tag{24}
\]
This uses canonical-height quadraticity, not BSD. The nonzero
raw logarithms in Corollary7.1 are NOT asserted zero; their
finite/isogeny correction is what(24) retains.

Thus the exact cubical norm has a nonconstant arithmetic source
and uniformly nonzero rational leading logarithm, but its
corrected point-height component is
12a² h(P,Q)−12h(aP,aQ)=0. At the already established prime5
the actual point determinant is nonzero. The displayed smoothing
defect therefore cannot be substituted for that determinant.
Undoing it by division by a²−a² is not an operation; removing
the Kato factor(4) is a different operation on a different
coefficient module and does not remove this zero eigenvalue.

## 9. The precise remaining comparison and source record

The full translated division-torsor transfer and its canonical
first relative point augmentation have been tested on the
actual fixed basis, with their exact norm powers. A separate
cubical norm survives and gives(17)–(24). These constructions
go beyond an abstract series model, but none maps the original
quadratic ray moment to the unsmoothed full point determinant.

The remaining task is an arithmetic operation retaining the
appropriate relative norm/point data and the ORIGINAL ray
branch, whose finite realizations compare the actual
M_(n,p), including A2,p and C_p, with det B_p and the normalized
unit determinant. It must respect the exact previously proved
identity
\[
 c_{2,p}=\varepsilon_p\,\#\operatorname{Sha}[p^\infty]
                              \det B_p\quad(c_{2,p}\ne0),
\]
where
\[
 \varepsilon_p=
 \frac{(-1)^b\iota_pu(0)}
      {\det U\det V\,(\det C)^2\det J}
\]
is the defined Smith/polarization frame unit of the completed
index theorem. No value of this unit is selected afterward.
Nonvanishing is still needed before the finite-Sha/point-space
identification in that theorem.

**[GAP CM-Symbol-Point].** Construct such an operation with a
proved successful coefficient/index test at every prime in(1),
or a finite-exception theorem controlling the remaining primes;
and construct ONE rational framed Z=q Xi_(P,Q), before separate
completions, for which
\[
 q\mapsto\frac{c_{2,p}}{2e_p\det B_p},\qquad
 R_\infty(Z)=\frac{L''(E,1)/2}{2\Omega_E}.
\]
Rationality of q=n_E must follow from that construction. Neither
the zero complete transfer nor the nonzero but height-annihilated
cube leading coefficient supplies it. Bad/nonsplit primes and the
full universal BSD scope also remain.

Primary Kato1.3,1.10,15.8 were read in the existing PDF/text cache
/tmp/cm-derived-kato2004.pdf and /tmp/cm-derived-kato2004.txt.
The full CM reciprocity and theta normalization are the same
ones previously reviewed; the new Kummer-image and norm proofs
are written here. Schmitt's general-conductor construction and
MST's exact sigma division/height conventions were also checked.
The only computation was the new exact rational evaluation
of(18) by the displayed recurrences. No old certificate or
prime scan was run, and no additional agent was created.

The [independent review](review-cm-symbol-point-reciprocity.md)
passed all nine sections, including the full Cartan over the tame
base, Kummer-image saturation, both norm multiplicities, the specified
root in(13), the restriction-of-scalars tower map, the weighted cochain
cancellation, and the distinction between(21),(24) and the unsmoothed
BSD comparison. The reviewer and coordinator independently reproduced
all six new division-polynomial values and both rational leading ratios.
