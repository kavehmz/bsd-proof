# The asymmetric CM ray and the unsmoothed point boundary

Date: 2026-09-13. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: completed bounded construction; independent review **PASS**.
[Full nine-section audit](review-cm-asymmetric-ray.md).
[Restart](cm-asymmetric-ray-checkpoint.md).
Inputs are the reviewed [point-torsor norms](cm-symbol-point-reciprocity-attack.md)
and [coefficient-cone theorem](cm-derived-unsmoothing-attack.md), with
their [norm review](review-cm-symbol-point-reciprocity.md) and
[cone review](review-cm-derived-unsmoothing.md).
Full BSD over Q remains the objective.

The asymmetric norm really retains the opposite ray. Its odd component
is nonzero at a proved depth, and an actual selected-rho class on a
punctured elliptic curve has exact order p^k. Complete transfer still
has a new unused-ray multiplicity. A direct opposite-ray construction
avoids that multiplicity but shifts the point by barpi. Its proper
point component is an explicitly described integral line with an
unselected boundary-lift parameter. A nontrivial local principal-unit
norm system is constructed without dividing p; its direct global-ray
descent fails at a proved depth. None of these statements proves
nonzero c2,p or the rational BSD coefficient.

## 1. Fixed objects and all original normalizations

Keep
\[
 E:y^2=x^3+39x,\quad K=\mathbf Q(i),\quad
 P=(3,12),\ Q=(27,144),\ R\in\{P,Q,P+Q\}.
\]
The Néron differential is dx/(2y) and P,Q are the full rational
basis modulo torsion. As before,
\[
 f_0=39(1+i)^3,\quad \mathfrak f=(f_0),\quad
 \Omega_\infty=(1+i)\Omega_E/2,\quad
 p=\pi\bar\pi,\quad
 \tau_m=\frac{\Omega_\infty}{f_0p^m}.
\]
Here pi=psi_E(mathfrak p), barpi=psi_E(bar mathfrak p). The prime range is
\[
 p\ge5,\qquad p\equiv1\pmod4,\qquad p\nmid2\cdot3\cdot13.     \tag{1}
\]
Use the ORIGINAL two-variable ray field and its opposite subfield:
\[
 F_m=K(\mathfrak f p^m),\quad
 B_m=K(\mathfrak f\bar{\mathfrak p}^{\,m}),\quad
 F_0=K(\mathfrak f),\quad
 \beta_m=[\pi^m]\tau_m
                =\frac{\Omega_\infty}{f_0\bar\pi^m}.         \tag{2}
\]
The symbol B_m here denotes a FIELD, not a height matrix.

The rational theta is unchanged:
\[
 \Theta_a(Z)=\Delta_E^{a^2-1}\psi_a(Z)^{-12},\qquad
 \Delta_E=-64\cdot39^3,\quad
 \operatorname{div}\Theta_a
       =12\bigl(a^2[O]-\sum_{T\in E[a]}[T]\bigr).            \tag{3}
\]
Take a=5 except a=7 at p=5. Its degree as a rational function is
D_a=12(a²−1). Kato1.3(4) gives its EXACT isogeny norm, with
constant one, for every isogeny of degree prime to a. In particular
it applies to[pi],[barpi] and[p]. This does not replace a primitive
ray-orbit norm by a full fiber without its imprimitive term.

Let A_k=Z/p^k, T_k=T_pi E/p^k, K_n=K Q_n and
\[
 m\ge\max(k,n+1),\qquad
 \rho=(\Psi^c)^{-1},\quad\mu_{p^k}\otimes\rho=T_k.            \tag{4}
\]
The rho vector remains the one prescribed by
gamma_CM=2pr_rho(gamma_E^+). The original finite smoothing unit is
\[
 q_{a,n,k}=12(a^2-u_a\gamma^{2\lambda_a}),\quad
 u_a=\Psi^c((a))=\pm a,\quad
 \lambda_a=\log_p(a)/g_p,\quad g_p=\log_p(1+p),               \tag{5}
\]
with chi_cyc(gamma)=1+p. Its augmentation is
q_(a,0,k)=12(a²−u_a), a p-unit. The two-variable map is the
QUOTIENT X,Y→T, not the diagonal subgroup. All traces are
unnormalized. The original tame degree1152(p−1)^2 and the
previous iota_p, u(0), Smith/polarization frame factors and
c_cmp,p=(156i Omega_p)^(-1) remain fixed.

## 2. The actual asymmetric field and its exact norm

Let Y_(R,m)^pi=[pi^m]^(-1)(R), and choose compatible points
R_(pi,m) only to name embeddings. Put
\[
 M_m(R)=F_m(R_{\pi,m}),\quad
 u_m(R)=\Theta_a(\tau_m+R_{\pi,m}),\quad
                         w_m(R)=\Theta_a(\beta_m+R).        \tag{6}
\]

**[NEW deduction] Proposition2.1.**
\[
 \operatorname{Gal}(M_m(R)/F_m)=E[\pi^m],\quad
 [M_m(R):F_m]=p^m,\quad
                  N_{M_m(R)/F_m}u_m(R)=w_m(R)\in B_m^\times. \tag{7}
\]

*Proof.* The preceding proof gives the full p^m Kummer translation
image for each R. Applying[barpi^m] to its division point projects
that image onto E[pi^m], and gives a pi^m-division point of R.
Hence the asymmetric torsor is a field with the group in(7).
Its translated theta arguments are the full pi^m-fiber above
[pi^m]tau_m+R. The normalized isogeny norm(3) gives(7) with
no scalar or root of unity. Every argument is outside E[a],
because its appropriate multiple has the non-torsion point
R plus torsion. ∎

For clarity the CM ray argument also proves
\[
 [B_m:K]=1152(p-1)p^{m-1},\qquad
 [F_m:K]=1152(p-1)^2p^{2m-2}.                              \tag{8}
\]
Over F_0 both residue-unit factors are unrestricted; the conductor
modulus injects the four Gaussian units. The beta_m coordinates
generate B_m. Indeed, for a principal ideal generator t, CM action
is epsilon(t)t, with epsilon(t) a Gaussian unit. If it fixes the
point with annihilator f barp^m, then t is congruent to the global
unit epsilon(t)^(-1) modulo that modulus, so its ray class is
trivial. This uses the actual conductor and class number one,
not an arbitrary Weber-coordinate assumption.

**[NEW deduction] Proposition2.2.** If m>r≥1 and delta=m−r, then
\[
 N_{M_m(R)/M_r(R)}u_m(R)
  =\Theta_a\bigl(\tau_r+[\bar\pi^\delta]R_{\pi,r}\bigr)^{p^\delta}.
                                                               \tag{9}
\]
In particular the one-step tower degree is p³ and its norm is
u_r([barpi]R)^p after the indicated isomorphism of point torsors.

*Proof.* M_r(R) is Galois over K. Its translation group over F_r
is E[pi^r], and the ray homothety acts on it by−1. A subextension
also lying in the abelian ray extension F_m/K would be a quotient
with trivial Cartan conjugation. Multiplication by−2 kills such
a quotient, so
M_r(R) intersect F_m=F_r. Thus every relative ray automorphism
lifts to Gal(M_m(R)/M_r(R)). The total degree is p^(3delta)
by(7),(8).

Put Z=tau_m+R_(pi,m). Its p^delta-multiple is the fixed point
tau_r+[barpi^delta]R_(pi,r). The pi-point translations give the
whole E[pi^delta] direction in its conjugate orbit. The opposite
ray automorphisms give all E[barpi^delta] differences of the
torsion argument; any simultaneous point difference lies in
E[pi^delta]. Thus the orbit is the full E[p^delta]-fiber,
of size p^(2delta). Each argument occurs p^delta times.
Applying the full[p^delta] norm proves(9). This argument
does not require those translation coordinates to be fixed
individually by the whole Galois group.

The target field is unchanged when R is replaced by[barpi]R:
Bezout for barpi and pi^r recovers R_(pi,r) from
[barpi]R_(pi,r) and R. This supplies the stated actual
torsor isomorphism. The POINT endomorphism in(9) is not
replaced by a scalar acting on an unproved linear function. ∎

## 3. The actual odd part is nonzero, but is not the full transfer

Decompose beta_m uniquely as
\[
 \beta_m=\sigma_m+t_m,\quad
 \sigma_m=[\bar\pi^{-m}]_{\mathfrak f}\tau_0\in E[\mathfrak f](F_0),
 \quad t_m\in E[\bar\pi^m]\text{ of exact order }p^m.
\]
The old full homothety h has pi- and barpi-components(−1,−1)
and f-component1. It fixes K_n and acts by−1 on rho, but now
\[
 h\beta_m=\sigma_m-t_m,\qquad
 O_m(R):=\frac{w_m(R)}{h w_m(R)}
       =\frac{\Theta_a(R+\sigma_m+t_m)}
              {\Theta_a(R+\sigma_m-t_m)}.                 \tag{10}
\]
The old fixed-base zero argument does not apply.

**[NEW deduction] Proposition3.1.** If
\[
                      (p-1)p^{m-1}>24(a^2-1),             \tag{11}
\]
then O_m(R) is not a root of unity. In particular the h-odd
part of[w_m(R)] in B_m^times tensor Q_p is nonzero.

*Proof.* The conjugate opposite-ray fields intersect in F_0,
by the two independent CRT factors. Every root of unity zeta
in B_m also belongs to the other ray field: complex conjugation
sends it to zeta^(-1). Hence zeta belongs to F_0.

For any nonzero zeta in F_0 consider, as a rational function of T,
\[
 f(T)=\Theta_a(R+\sigma_m+T)
                      -\zeta\Theta_a(R+\sigma_m-T).
\]
The two pole cosets are distinct, since2(R+sigma_m) is
non-torsion. Thus f is nonzero and its pole degree is at
most2D_a=24(a²−1). If O_m(R)=zeta, all
(p−1)p^(m−1) distinct F_0-conjugates of t_m are zeros
of f. This contradicts(11). Both evaluated theta values
are nonzero and finite, as before. The root-of-unity
observation proves the claim. ∎

The odd projector is precisely one-half of the unit ratio(10)
in additive Kummer notation. The full selected rho transfer
equals the transfer of that odd part: h contributes the minus
rho character. The factor1/2 is a p-unit and is retained.
This proves neither that the other tame/pro-p character sums
are nonzero nor that a specialization has a nonzero class
modulo p^k. No such inference is made from(11).

## 4. Full transfer, minimal descent and the changed tower laws

The field B_m is unramified at mathfrak p. Every nontrivial
subextension of K_n/K is totally ramified there. Consequently
B_m intersect K_n=K. Set L_m=B_m K_n. Equations(8) give
\[
                  [F_m:L_m]=(p-1)p^{m-1-n}=:d_{m,n}.       \tag{12}
\]
The normed unit w_m(R) and rho modulo p^k are already defined
and trivialized, respectively, over L_m.

Define the ACTUAL smaller-field class
\[
 Z_{n,m,k}(R)=q_{a,n,k}^{-1}
       \operatorname{Cor}_{L_m/K_n}
                 (\delta_k(w_m(R))\otimes t_{\rho,k}).       \tag{13}
\]
It is defined from descended data, not by dividing a finite
cohomology class by d_(m,n). The complete asymmetric transfer is
\[
 q_{a,n,k}^{-1}\operatorname{Cor}_{M_m(R)/K_n}
           (\delta_k(u_m(R))\otimes t_{\rho,k})
                         =d_{m,n}Z_{n,m,k}(R).              \tag{14}
\]
This follows by exact Kummer norm and corestriction. Thus(14)
is zero over A_k for m≥n+k+1. The lost factor is a NEW unused
pi-ray factor, not the symmetric p² tower law.

The smaller-field classes have two precise covariance laws:
\[
 Z_{n,m+1,k}(R)=Z_{n,m,k}([\bar\pi]R),\qquad
 Z_{n,m,k}(R)=\operatorname{Res}_{K_n/K}Z_{0,m,k}(R).         \tag{15}
\]
For the first, the degree-p opposite-ray norm is the full
barpi-fiber and gives
\[
 N_{B_{m+1}/B_m}w_{m+1}(R)=w_m([\bar\pi]R).
\]
The rho vector is unchanged modulo p^k when m≥k. For the
second, use the linearly disjoint base-change/corestriction
square. Such a restricted class is G_n-invariant, so(5)
acts on it by its augmentation q_(a,0,k). In particular
\[
 \operatorname{Cor}_{K_{n+1}/K_n}Z_{n+1,m,k}(R)
                              =p Z_{n,m,k}(R).              \tag{16}
\]
Artificially adjoining a cyclotomic layer has not produced
a norm-compatible cyclotomic Iwasawa family.

The bottom primitive-orbit norm also has an exact extra term:
\[
 N_{B_m/F_0}w_m(R)=
 \frac{\Theta_a([\bar\pi^m]R+\tau_0)}
 {\Theta_a([\bar\pi^{m-1}]R+[\bar\pi^{-1}]_{\mathfrak f}\tau_0)}.
                                                               \tag{17}
\]
Indeed all barpi^m-division points of tau_0 have full norm
the numerator. The nonprimitive subset is precisely the
barpi^(m−1)-fiber above the unique tame inverse
[barpi^(-1)]_f tau_0 and has the denominator as its norm.
Removing that subset gives the primitive ray orbit.
At R=O this recovers the first-prime Euler factor. At nonzero
R one must retain the simultaneous endomorphism of R; it is
not merely the same Frobenius factor on a fixed base unit.

## 5. A new full-coefficient fixed-point-jet test

Let P_(R,m,k)^pi=A_k[Y_(R,m)^pi], with augmentation kernel I^pi.
The theta class in these permutation coefficients, after the
original twist, unnormalized transfer and unit(5), has augmentation
(14). For m≥n+k+1 that augmentation is zero. Since
H⁰(K_n,T_k)=0, the coefficient sequence gives a UNIQUE lift
\[
 \eta^\pi_{R,n,m,k}\in H^1(K_n,I^\pi_{R,m,k}\otimes T_k).
\]
No such zero-augmentation lift is presumed at the smaller levels.

**[NEW deduction] Proposition5.1.** For d≥1, choose
\[
 r\ge\max\{n+1,k+\lfloor\log_p d\rfloor\},\qquad m\ge r+k.   \tag{18}
\]
Then the order-d POINT-translation jet of eta^pi is zero.

*Proof.* Projection by[pi^(m−r)] on point torsors corresponds
to the field norm(9). Its permutation-valued class is
p^(m−r) times the class of the ACTUAL function
Theta_a(tau_r+[barpi^(m−r)]S) on Y_(R,r)^pi.
This is zero over A_k under(18), without assuming linearity
in S or R. The projected eta therefore maps to zero in
permutation cohomology. H⁰(T_k)=0 makes the augmentation-kernel
H¹ map injective, so that projected eta is zero.

The translation group here is E[pi^r], of order p^r. Its
group-ring relation is(1+X)^(p^r)−1. For j≤d the exact
valuation r−v_p(j) of binom(p^r,j) is at least k under(18).
Hence all such coefficient jets are canonically identified
by the actual projections. This proves the assertion. ∎

These are POINT-translation jets, not ray variables whose
generator has value1+p and order p^(r−1) at F_r. Their
indices must not be interchanged. The full A_k is retained;
no cohomological tensor/base-change identification is presumed.

The first point factor is E[pi^k]. With the standard[p^k]
Kummer convention its pi-isogeny cocycle equals
[barpi^k] times the pi-projected[p^k] cocycle. This is an
actual p-unit factor, not set to1. Its tensor with T_k has
character Psi². The canonical Weil contraction is zero,
because the pi-line is isotropic. The old full-point tensor
had an opposite component; it cannot be restored by deleting
this distinction. Proposition5.1 is the new norm calculation,
not a reuse of the old symmetric law.

## 6. The full selected-rho geometric class and its exact boundary

There is a stronger positive result than nonzero h-odd units.
Use a variable X on the FIXED elliptic curve. Let D_m be the
union of E[a]−g beta_m over all g in Gal(B_m/K), and U_m=E minus D_m.
It is defined over K and contains O and all three non-torsion R.
Define
\[
 {\cal Z}_{m,k}
 =q_{a,0,k}^{-1}\operatorname{Cor}_{B_m/K}
       \bigl(\delta_k(\Theta_a(X+\beta_m))\otimes t_{\rho,k}\bigr)
                    \in H^1(U_m,T_k).                      \tag{19}
\]
Finite étale transfer is taken on U_m base-changed to B_m.
Its evaluation at R is exactly Z_(0,m,k)(R).

**[NEW deduction] Proposition6.1.** This class has exact order p^k
in the ACTUAL selected rho branch. Its positive Kummer valuation
residues, after geometric base change, are
\[
 \begin{cases}
 \displaystyle\frac{a^2-1}{a^2-u_a}\,g(t_{\rho,k}),
                  &X=-g\beta_m,\\[4pt]
 \displaystyle-\frac1{a^2-u_a}\,g(t_{\rho,k}),
                  &X=T-g\beta_m,\quad0\ne T\in E[a].
 \end{cases}                                               \tag{20}
\]

*Proof.* Distinct conjugates of beta_m give disjoint E[a]-cosets:
their difference is annihilated by f barpi^m, whose ideal is
prime to a. Since beta_m generates B_m, there are no further
repetitions. Over the geometric field the transfer is the sum
over these embeddings. At each displayed point only its one
summand contributes, with the divisor multiplicity in(3).
The residue of the Kummer torsor y^(p^k)=f is the positive
valuation of f modulo p^k. Twisting puts it in T_k(-1)=rho.
Dividing by q_(a,0,k)=12(a²−u_a) gives(20).
These coefficients are p-units, including at p=5 with a=7.
Thus a residue and hence the class has exact order p^k.
No compact-first signed Gysin pairing is invoked here. ∎

This is a geometric/arithmetical class on a punctured curve.
A nonzero residue there does not prove nonzero or Selmer
membership of its specialization at P,Q.

Subtract the base-field value at O:
\[
 {\cal D}_{m,k}
 ={\cal Z}_{m,k}-p_E^*O^*{\cal Z}_{m,k}.
\]
Its restriction at O is zero. Since H⁰(K,T_k)=0, it has a
UNIQUE lift to H¹(U_m,O;T_k), which we denote by the same
symbol. Its geometric residues are still(20), so it cannot
extend to H¹(E,O;T_k).

For m≥k the norm law is an actual pointed isogeny pullback:
\[
 U_{m+1}=[\bar\pi]^{-1}U_m,\qquad
                   {\cal D}_{m+1,k}=[\bar\pi]^*{\cal D}_{m,k}. \tag{21}
\]
The support equality follows because every barpi-division
point of a primitive beta_m is primitive at the next level;
multiplication by barpi is invertible on E[a].
Apply the degree-p ray norm to the function in(19) and
subtract its value at O to prove(21). Coefficient reduction
is compatible whenever m≥k+1.

## 7. The unsmoothed proper point line and its exact remaining parameter

**[NEW deduction] Proposition7.1.** Over K_n,
\[
 H^1(E_{K_n},O;T_k)
       \simeq\operatorname{Hom}_{G_{K_n}}(E[p^k],T_k)
       \simeq A_k.                                        \tag{22}
\]
Its framed generator K_pi,k is the pi projection of the universal
[p^k] Kummer torsor, trivialized by O over O. Evaluation at R
is the pi-projected Kummer class of R.

*Proof.* The geometric relative pair(E,O) has H⁰=0 and its
H¹ is the dual of E[p^k]. The relative Hochschild–Serre
sequence therefore identifies total degree one with the
invariants of that H¹ tensor T_k. There is no base arithmetic
H¹ term, because the relative geometric H⁰ is zero.
Equivalently use the splitting by O of the proper cohomology
complex. The CM idempotents split E[p^k] integrally. Its
pi→pi Hom is A_k; its opposite Hom has no invariant, since
the full residual Cartan has an element acting differently
on the two lines, with unit difference. K_n has p-power
degree, so it does not remove that tame Cartan action.
The universal division torsor represents the identity Hom;
projecting it gives the specified generator. ∎

The localization sequence for the smooth curve, with the
positive valuation residue used in(20), injects(22) into
H¹(U_m,O;T_k). Consequently the set of relative classes with
the residue of D_(m,k) is an actual torsor for A_k K_pi,k.
It is nonempty, since D_(m,k) is one such lift. If Xi_(m,k)
is another boundary lift, the exact decomposition is
\[
                  {\cal D}_{m,k}-\Xi_{m,k}=c_{m,k}K_{\pi,k}.
                                                               \tag{23}
\]
This is a genuine unsmoothed point component. The origin
condition and residues alone do not choose its scalar.

The point endomorphism has a UNIT eigenvalue on this line:
\[
                         [\bar\pi]^*K_{\pi,k}=\bar\pi K_{\pi,k}.
\]
Here barpi is the ordinary p-adic unit root in the chosen
pi-completion. Thus the families Xi compatible with(21)
and coefficient reduction are parameterized EXACTLY by
one c in Z_p:
\[
            \Xi_{m,k}={\cal D}_{m,k}-\bar\pi^m(c\bmod p^k)K_{\pi,k}.
                                                               \tag{24}
\]
Conversely compatibility forces barpi^(-m)c_(m,k) to be
independent of m and compatible in k, proving the assertion.
This inverse unit acts on an actual proper coefficient
line. It is not division by p, by log(a), or by the zero
height-smoothing eigenvalue.

The original norm, coefficient and origin conditions therefore
leave an ACTUAL Z_p ambiguity in selecting the boundary
counterterm. Formula(24) describes that ambiguity; no c is
assigned from a required BSD value. A direct equality between
D_(m,k) and a proper Kummer point class is already excluded
by its nonzero residue(20).

There is also an exact smoothing check on these same
point-variable classes. Before dividing by q_(a,0,k), call
the origin-reduced transfer Phi_(a,m,k). For integers a,b
prime to6fp, define the actual isogeny operator
S_b=b²−u_b[u_b]^*, u_b=Psi^c((b))=±b. Kato1.3(2) gives
\[
                         S_b\Phi_a=S_a\Phi_b                \tag{25}
\]
on a common open of E. To check the character factor,
Frobenius at(b) sends beta to[u_b]beta. In twisted
corestriction a translated b-isogeny term therefore becomes
u_b[u_b]^*Phi_a. Theta_a is even, so the sign in u_b
causes no omitted function constant. This proves(25).
On the proper line(22), S_b acts by b²−u_b²=0.
The old Kato scalar unit and this isogeny operator are
not interchangeable inverses.

## 8. A genuine local point norm system without p-division

Work at mathfrak p, so K_pi=Q_p. The endomorphism[barpi]
has unit tangent barpi and is an integral automorphism of
the formal group. For R in E_1(Q_p), let S_m(R) be its
UNIQUE formal inverse with[barpi^m]S_m(R)=R. This is an
actual local point, with log_E S_m=barpi^(-m)log_E R.

In the semilocal unramified algebra B_m tensor_K K_pi put
\[
 {\cal U}_{a,m}(R)
       =\frac{\Theta_a(\beta_m+S_m(R))}{\Theta_a(\beta_m)}.    \tag{26}
\]
The denominator and numerator are units: the nonzero tame
f-part of beta_m has reduction of order prime to a, and
its barpi-torsion direction is étale at pi. Adding a formal
point preserves that reduction. In fact U_(a,m)(R) is in
1+p times the semilocal integer ring.

**[NEW deduction] Proposition8.1.**
\[
                     N_{B_{m+1}/B_m}{\cal U}_{a,m+1}(R)
                                         ={\cal U}_{a,m}(R). \tag{27}
\]
Its same-rho finite Kummer transfer, normalized by q_(a,0,k),
defines a compatible integral class
\[
                         {\cal U}_{\pi}(R)\in H^1(Q_p,T_\pi).
                                                               \tag{28}
\]
It lies in the local finite formal point lattice.

*Proof.* The formal S_(m+1)(R) is scalar in Q_p and is
fixed in the semilocal norm. The exact theta norm gives
Theta_a(beta_m+[barpi]S_(m+1))/Theta_a(beta_m), which is(26).
This proves(27) even when primes split in a ray step: it is
the norm on the entire semilocal algebra, not a selected
field trace with a forgotten multiplicity.

For m≥k the rho vector is trivialized. Kummer compatibility
with(27) gives independence of m after transfer to Q_p,
and compatibility in k follows from the fixed vectors.
Taking the inverse limit gives(28). The reviewed local
CM table says H¹(Q_p,V_pi) is entirely finite, and the
integral finite subgroup is the whole lattice here by
Kummer saturation and nonanomalousness. This proves the
last assertion. No nonvanishing of(28) is inferred. ∎

There is an exact direct-descent obstruction for the actual
points in the old finite-height recipe. Take
R=n_pP,n_pQ,n_p(P+Q), n_p=8#E(F_p), a p-unit.
The global field B_m(S_m(R))/B_m has degree p^m:
after base change to F_m this is the full opposite Kummer
projection already proved, and p^m is also the upper bound.
If the algebraic value(26) belonged to B_m, all its p^m
point-division conjugates would be the same. The nonconstant
function Theta_a(beta_m+X) has degree D_a. Thus
\[
 p^m>D_a\quad\Longrightarrow\quad {\cal U}_{a,m}(R)\notin B_m.
                                                               \tag{29}
\]
All these conjugates are finite. Otherwise that rational
function minus its common value would have too many zeros.

The chosen formal branch embeds these algebraic values into
the local ray algebra, but does not give a global ray-field
section. In particular(29) also proves the local principal
unit family is nontrivial at that depth. It does NOT prove
its selected-rho class(28) is nonzero. At the opposite
p-adic place barpi is not a formal unit; the same branch
construction cannot simply be repeated there.

For the compatible boundary family(24), evaluating at the
local inverse point gives the exact possible proper correction
c times the local Kummer class of R. Selecting a c for
global gluing would therefore require an actual comparison
of(28) with that point map, plus the other local conditions.
No additivity or Z_p-linear extension of the nonlinear theta
point-value function has been assumed.

## 9. Local boundaries and the first remaining comparison

For a finite place the raw value has the exact valuation
\[
 v(\Theta_a(Z))=(a^2-1)v(\Delta_E)-12v(\psi_a(Z)).            \tag{30}
\]
The valuation identity holds at every finite place. At good places
away from ap it gives the usual étale Kummer tame boundary; at p
the separate formal/semilocal construction of§8 is retained.
For w_m(R), a bad evaluation can only occur, outside the
fixed bad/smoothing set, where
[a]([barpi^m]R+tau_0) reduces to O. This is a finite set
for each m, but a fixed set independent of m has NOT been
proved. Translated non-torsion values have not been called
the original global elliptic units.

The nonzero geometric residues(20), the possible finite
arithmetic residues(30), and the nontrivial local family(26)
are different facts. None proves a nonzero original global
Selmer coefficient at P,Q. The smaller-field classes(13)
are defined integrally, but have the point-shifting law(15)
and the cyclotomic restriction law(16). The old all-fixed-jet
theorem was not reused; the NEW threshold(18) follows from
the proved asymmetric norm multiplicity with its point
endomorphism retained.

**[GAP CM-Asymmetric-Point].** Select an arithmetic boundary
counterterm in the actual torsor(24), compatible with the
original primitive ray source and all local conditions,
and prove its resulting proper point coefficient agrees
with the normalized Kato/Bockstein determinant comparison.
A sufficient framed identity, where the old point map is
defined, is that the resulting c_p Xi_(P,Q) maps under the
OLD Bockstein frame map to
p/(2#E(F_p)) times the actual kappa_p=w_0 tensor T.
No such equality is supplied by choosing c in(24).

It must retain the already established target
\[
 q_p=\frac{c_{2,p}}{2(1-\alpha^{-1})^2\det B_p},
 \quad
 c_{2,p}=\varepsilon_p\,\#\operatorname{Sha}[p^\infty]\det B_p,
 \quad
 \varepsilon_p=
 \frac{(-1)^b\iota_pu(0)}
 {\det U\det V\,(\det C)^2\det J},
\]
with the Sha/point identification only AFTER c2,p≠0.
One rational framed element before separate completions
must still have real realization(L''(E,1)/2)/(2Omega_E).
Rationality, uniform nonvanishing/index control, the other
primes and full universal BSD remain unproved.

The primary exact theta norm and cross-smoothing identities
were checked in Kato1.3 and1.10 in the existing cache.
CM field and coefficient conventions are those verified
in Kato15.8 and the preceding separate reviews. The local
formal/étale distinction and integral Kummer saturation
are the reviewed [local-condition results](cm-ray-local-conditions-attack.md).
Finite étale Kummer, localization with positive valuation,
and the relative degree-one calculation in(22) use their
usual actual cochain/cover models; the new deductions are
proved on the page. No prime scan, old certificate rerun,
new numerical period or additional agent was used.

The [independent adversarial review](review-cm-asymmetric-ray.md) passed
all nine sections, including the asymmetric orbit multiplicities,
smaller-field normalization, odd-component degree bound, primitive
denominator, point-versus-ray jet indices, full-rho geometric residues
and the local/global distinction in(26)–(29). The valuation/tame-residue
scope clarification changed no norm or scalar. The remaining arithmetic
comparison above is not promoted by that verdict.
