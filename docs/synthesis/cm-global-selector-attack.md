# An actual global coefficient class for the local CM inverse selector

Date: 2026-09-13. Owner /root/odd_rank_bridge, GPT-6 Astra/xhigh.
**Completed bounded construction; independent review PASS for all ten sections.**
[Full audit](review-cm-global-selector.md).
[Restart](cm-global-selector-checkpoint.md).
Full BSD over Q remains the universal objective.

The local formal selector is realized by a genuine coordinate map on a
global point-division permutation module. At p=5, one of the two fixed
point inputs gives nonzero GLOBAL cohomology classes modulo25 at every
level m≥2. Their augmentation is zero. At m≥4 these classes lift uniquely
to point-augmentation depth at least5^(m-3), so the nonvanishing is
compatible with the vanishing of every fixed jet. Their pair also has
a nonzero image modulo EVERY common proper-point boundary correction,
with an exact local detector of order5. This is not a
nonvanishing theorem for the original scalar Kato coefficient or an
assertion that the selected local coordinate descends globally.

The inputs are the reviewed [asymmetric construction](cm-asymmetric-ray-attack.md),
its [audit](review-cm-asymmetric-ray.md), the exact
[local map](cm-local-point-comparison-attack.md), its
[core audit](review-cm-local-point-comparison.md) and the separate
[local Taylor audit](review-cm-local-taylor-certificate.md).
No prior numerical certificate is rerun.

## 1. Fixed branch, coefficient lattices and arithmetic fields

Keep E:y²=x³+39x, K=Q(i), omega=dx/(2y), P=(3,12), Q=(27,144)
and their proved full point lattice. The prime range is
p≥5, p≡1 mod4, p∤2·3·13. Write p=pi barpi with pi=Psi(mathfrak p),
K_pi=Qp, alpha=barpi a unit in this completion. Put
\[
 f_0=39(1+i)^3,\quad \tau_0=\Omega_\infty/f_0,\quad
 \tau_m=\Omega_\infty/(f_0p^m),\quad
 \beta_m=[\pi^m]\tau_m=\Omega_\infty/(f_0\bar\pi^m).
\]
Thus beta is the original opposite-ray argument, not a replacement
tame torsion point. Write
\[
 B_m=K(\mathfrak f\bar{\mathfrak p}^{\,m}),\quad
 F_m=K(\mathfrak f p^m),\quad F_0=B_0=K(\mathfrak f).
\]
For m≥1 their degrees are respectively
1152(p-1)p^(m-1) and1152(p-1)²p^(2m-2).

Use A_k=Z/p^k and the ORIGINAL vector t_(rho,k), where
\[
 \rho=(\Psi^c)^{-1},\qquad
 j:\mu_{p^k}\otimes A_k(\rho)\simeq T_k=T_\pi E/p^k.
 \tag{1}
\]
Its Betti origin is gamma_CM=2pr_rho(gamma_E^+). The character rho
modulo p^k is trivial over B_m when m≥k. The theta and smoothing are
\[
 \Theta_a(Z)=\Delta_E^{a^2-1}\psi_a(Z)^{-12},\quad
 \Delta_E=-64\cdot39^3,\quad
 q_a=12(a^2-u_a),\quad u_a=\Psi^c((a))=\pm a,
 \tag{2}
\]
with a=5 except a=7 at p=5. The scalar q_a is a p-unit.
The full original finite cyclotomic operator is
12(a²-u_a gamma^(2lambda_a)), lambda_a=log_p(a)/g_p,
g_p=log_p(1+p), chi_cyc(gamma)=1+p. We first construct classes
over K; their restriction to K_n=KQ_n is gamma-invariant, so that
operator acts on these classes by its augmentation q_a.
We do not change the original two-variable QUOTIENT X,Y→T.

Let N_p=#E(F_p), n_p=8N_p, and take
R in {n_pP,n_pQ,n_p(P+Q)}. The reviewed nonanomalous result makes n_p
a p-unit and these points lie in E_1(Qp). They remain primitive
in the appropriate full O_K tensor Zp point lattice. At p=5,
n_p=64. Define the ACTUAL finite étale K-scheme
\[
 Y_{R,m}=[\bar\pi^m]^{-1}(R),\quad
 {\cal P}_{R,m,k}=A_k[Y_{R,m}],\quad
 {\cal I}_{R,m,k}=\ker({\cal P}_{R,m,k}\xrightarrow{\rm aug}A_k).
 \tag{3}
\]
All permutation coefficients are retained.

Choose compatible points S_m in this torsor, [barpi]S_(m+1)=S_m,
solely to describe fields and cochains. Set M_m=B_m(S_m).
The prior full Kummer-image theorem, projected onto E[barpi^m],
gives [F_m(S_m):F_m]=p^m. Since B_m contains this entire torsion
group and the torsor has p^m geometric points, it follows already
that
\[
 [M_m:B_m]=p^m,\qquad
 \operatorname{Gal}(M_m/B_m)=E[\bar\pi^m].
 \tag{4}
\]
This applies to the p-unit multiples just specified; it is not a
claim for torsion R or an arbitrary unsaturated point.

The fields M_m/K are Galois. For m>r, one has
\[
 M_r\cap B_m=B_r,\qquad [M_m:M_r]=p^{2(m-r)}.
 \tag{5}
\]
Indeed any intersection quotient of the Kummer translation group
would be abelian over K, since B_m/K is abelian. The actual residual
Cartan has an element acting as -1 on that translation group.
An abelian quotient must have trivial conjugation, so multiplication
by2 kills it and it is zero. The required Cartan element exists
with the tame modulus fixed: CRT leaves the whole opposite
(O_K/barp^r)^times factor in the CM ray image. This is the
same full-image input verified in the preceding norm proof.
Equation(5) now follows from(4) and the degree-p ray steps.

At pi the isogeny[barpi] extends to a finite étale isogeny of the
good abelian scheme: its tangent is a unit and its reduction is
the étale ordinary isogeny. Pullback by the integral section R
therefore makes Y_(R,m) unramified at pi. B_m is also unramified
there, so M_m is unramified at pi. Consequently M_m∩K_n=K.
The relative extension F_m/B_m is totally ramified at pi:
its inertia is the full extra (O_K/pi^m)^times ray factor.
Thus
\[
 M_m\cap F_m=B_m.
 \tag{6}
\]
These statements also follow after the displayed disjoint
cyclotomic base change. They do not choose a global formal branch.

## 2. The actual ratio and its finite coefficient class

In the coordinate field of Y_(R,m) over B_m define
\[
 f_{a,R,m}(S)=
       \frac{\Theta_a(\beta_m+S)}{\Theta_a(\beta_m)}
                         \in M_m^\times.
 \tag{7}
\]
The values are finite and nonzero: otherwise a non-torsion
division point would differ from torsion by an a-torsion point.

Kato's exact isogeny norm gives the FULL point-fiber norm
\[
 N_{M_m/B_m} f_{a,R,m}
       =\frac{\Theta_a(\tau_0+R)}
                    {\Theta_a(\beta_m)^{p^m}}.
 \tag{8}
\]
To verify it, [barpi^m](beta_m+S)=tau0+R, and the translations
of S run over all E[barpi^m], once each by(4). The denominator
is constant along that point fiber and occurs p^m times.
No primitive-ray denominator has been removed in this calculation:
it is explicitly a FULL POINT fiber, while beta_m itself retains
its original primitive ray.

Finite étale Shapiro turns the Kummer class of(7) into
H¹(B_m,P_(R,m,k) tensor mu_(p^k)). For m≥k, tensor it with
the prescribed rho vector and use(1), then corestrict:
\[
 {\cal A}_{R,m,k}
 =q_a^{-1}\operatorname{Cor}_{B_m/K}
       \bigl(\delta_k(f_{a,R,m})\otimes t_{\rho,k}\bigr)
       \in H^1(K,{\cal P}_{R,m,k}\otimes T_k).
 \tag{9}
\]
There is no division by [B_m:K], by a point-field degree or by p.
The finite module and class in(9) are defined before any local
selector or formal differentiation.

The coefficient module is an actual Artin permutation lattice
tensored with the CM Tate lattice. After rational p-adic
realization it belongs to the corresponding tensor of the
Artin motive of Y with the CM elliptic motive. The particular
finite class(9) uses triviality of rho only MODULO p^k.
We do not assert a rational motivic extension class by tensoring
an untwisted unit with a nonexistent invariant rational rho vector.
A rational Kummer extension twisted by rho has quotient rho,
not the trivial representation. That endpoint distinction remains.

**[NEW] Theorem2.1.** For every m≥k the augmentation of(9) is zero.
There is a UNIQUE class
\[
 \eta_{R,m,k}\in H^1(K,{\cal I}_{R,m,k}\otimes T_k)
 \tag{10}
\]
mapping to(9).

*Proof.* Augmentation commutes with Shapiro and is the point norm(8).
The denominator's Kummer class is multiplied by p^m and is zero
over A_k. The numerator belongs to F_0. The actual opposite-ray
homothety h, trivial on F_0 and equal to -1 in the opposite
p-primary Tate character, has rho(h)=-1 modulo p^k.
The untwisted restricted Kummer class of that fixed numerator
is h-invariant, whereas its tensor with t_rho is negated.
Corestriction is invariant under h, so twice this transferred
class is zero. Since p is odd it is zero. This proves the
augmentation statement with its original character.

The coefficient exact sequence
\[
 0\to{\cal I}_{R,m,k}\otimes T_k
 \to{\cal P}_{R,m,k}\otimes T_k\to T_k\to0
 \tag{11}
\]
has H0(K,T_k)=0. For example pi-inertia fixes the opposite
ray and acts nontrivially through the cyclotomic character on T_k.
Its Teichmuller element -1 acts by -1. The resulting H¹ map
in(11) is injective and has precisely the augmentation kernel
as image. This proves existence and uniqueness. QED.

In particular (10) determines an ACTUAL finite étale extension
of K-group schemes, with coefficient modules
0→I tensor T_k→E_eta→A_k→0. On an underlying split A_k-module
its action is g(b,t)=(b,gt+b eta(g)). The cocycle is precisely
the one constructed from the theta values; replacing it by a
coboundary gives the isomorphic extension. This is a finite
coefficient extension, not a claimed rational motivic lift.

The same statements hold after restriction to K_n.
For comparison with the COMPLETE original F_m source, at
m≥max(k,n+1), (6) and the unramified-at-pi torsor give exactly
\[
 {\cal A}^{F}_{R,n,m,k}
   =(p-1)p^{m-1-n}\,
           \operatorname{res}_{K_n/K}{\cal A}_{R,m,k}.
 \tag{12}
\]
Here the left side uses the very same ratio and point permutation
module, but first extends it to F_m and transfers from F_m/K_n.
This is the restriction/corestriction formula, using
[F_m:B_mK_n]=(p-1)p^(m-1-n). The corresponding eta classes
satisfy the identical equality by the injectivity in(11).
Thus the complete original transfer is zero at m≥n+k+1;
(9) is a directly defined smaller-field class, not its quotient
by the nonunit factor.

## 3. The exact field norm and point-coefficient tower law

Put delta=m-r with m>r≥k. Then
\[
 N_{M_m/M_r} f_{a,R,m}= f_{a,R,r}^{\,p^\delta}.
 \tag{13}
\]
There are two direct checks of the multiplicity. First,
[M_m:M_r]=p^(2delta), but the theta argument beta_m+S_m
runs through only the full [barpi^delta] fiber above beta_r+S_r,
which has p^delta points. Each argument occurs p^delta times.
Second, norm first over M_m/(B_m M_r). Its translations have
size p^delta, so it gives
Theta_a(beta_r+S_r)/Theta_a(beta_m)^(p^delta).
In the remaining degree-p^delta ray norm the numerator is
fixed and the denominator has exact theta norm
Theta_a(beta_r)^(p^delta). This proves(13) without a scalar
inference from point additivity.

The actual torsor map [barpi^delta]:Y_(R,m)→Y_(R,r)
induces a coefficient pushforward pi_(m,r).
Compatibility of finite étale Shapiro, Kummer norm and
corestriction gives
\[
 \pi_{m,r,*}{\cal A}_{R,m,k}
       =p^\delta{\cal A}_{R,r,k},\qquad
 \pi_{m,r,*}\eta_{R,m,k}
       =p^\delta\eta_{R,r,k}.
 \tag{14}
\]
For clarity, the first pushforward norms the unit over each
point fiber. Corestriction B_m/B_r then takes exactly the
norm in(13); the disjointness(5) identifies the coefficient
fiber with the indicated field compositum. The rho vector
is already fixed over B_r because r≥k, so no character
factor is lost in this norm. Both sides use the same q_a.
The second equality follows from the injective map(11).

There is a stronger actual pullback description. Let D_(m,k)
be the reviewed origin-reduced class on the punctured pair
(U_m,O) from the asymmetric proof, and let s_m:Y_(R,m)→U_m
be its tautological point. Its image is in that open, because
R is non-torsion. Finite étale base change gives exactly
\[
 {\cal A}_{R,m,k}
       =\operatorname{Sh}_{Y_{R,m}/K}(s_m^*{\cal D}_{m,k}).
 \tag{14a}
\]
Here one first forgets the relative framing when pulling
back to Y. Subtracting the value at O is exactly the ratio
in(7), so there is no omitted constant class.

The actual isogeny law D_(m,k)=[barpi^(m-r)]^*D_(r,k)
now gives a second coefficient map j_(r,m), sending a root
of Y_r to the SUM of all its lifts in Y_m, with
\[
 {\cal A}_{R,m,k}=j_{r,m,*}{\cal A}_{R,r,k},\qquad
 \eta_{R,m,k}=j_{r,m,*}\eta_{R,r,k},\qquad
 \pi_{m,r}j_{r,m}=p^{m-r}.
 \tag{14b}
\]
Indeed pullback H1(Y_r,T_k)→H1(Y_m,T_k) is this map under
Shapiro. The coefficient map carries I_r into I_m; injectivity
in(11) proves the eta identity. Thus the growing classes are
specific replications of an actual finite-level class, not
independently chosen cohomology classes at each level.

This is a p-per-step cohomological law. It is neither the
previous symmetric p² law nor an integral Iwasawa norm law
with the p factor suppressed. Rationally multiplying the
untwisted classes by p^-m changes their actual lattices;
no such change is part of(9)–(14).

## 4. Local evaluation is exactly the previously nonzero selector

At the chosen pi completion, [barpi] is an integral formal
automorphism. There is a UNIQUE S_m^0(R) in E_1(Qp) with
[barpi^m]S_m^0(R)=R. As a geometric point of Y_(R,m) it is
fixed by G_Qp. It therefore defines the ACTUAL equivariant
coefficient functional
\[
 \operatorname{ev}_{m,R}:{\cal P}_{R,m,k}|_{G_{\mathbb Q_p}}
          \longrightarrow A_k,\qquad
 \sum_{S\in Y}a_S[S]\longmapsto a_{S_m^0(R)}.
 \tag{15}
\]
This is evaluation on a local direct factor of the finite
étale algebra, not a G_K-equivariant map.

**[NEW] Theorem4.1.** For every m≥k,
\[
 \operatorname{ev}_{m,R,*}\operatorname{loc}_{\mathfrak p}
             (\eta_{R,m,k})
        = {\cal U}_\pi(R)\bmod p^k
                   \quad\text{in }H^1(\mathbb Q_p,T_k),
 \tag{16}
\]
where the left side restricts(15) to I and the right side
is the ORIGINAL selected local class from the reviewed local map.

*Proof.* At pi, M_m/B_m splits completely as a point extension:
all roots are S_m^0(R)+T with T in E[barpi^m], and that
torsion is already defined over each B_m completion.
Local Shapiro consequently identifies the point-algebra
Kummer class with its separate root coordinates. Equation(15)
selects precisely the coordinate S_m^0(R).

Localizing corestriction in(9) uses every double coset for
B_m tensor_K Qp. If a coset carries beta_m to g beta_m,
it carries the coefficient vector to g(t_rho)=rho(g)t_rho.
Its selected root is transported back from S_m^0(R);
the resulting unit is
\[
 \frac{\Theta_a(g\beta_m+S_m^0(R))}{\Theta_a(g\beta_m)}.
 \tag{17}
\]
Summing the local corestrictions over ALL those cosets gives
exactly the full semilocal formula in the preceding local theorem.
There is ONE rho factor, and neither a point-degree multiplicity
nor a division by a ray degree. A trace from only one chosen
completion would not be this formula.

The image of eta in the permutation module is A, so its
evaluation is the same. The exact opposite-ray norm fixes
S_(m+1)^0 as a scalar in Qp and shifts it by [barpi],
giving S_m^0. Hence the selected finite transfers agree
at all levels m≥k with the construction of U_pi. QED.

The exact point coordinate of(16), in
pZp/p^(k+1)Zp, is
\[
 \frac{\Omega_j}{q_a}\sum_{g\in G_m}\rho(g)
 \log_p\frac{\Theta_a(g\beta_m+
          \exp_E(\alpha^{-m}\log_E R))}
                    {\Theta_a(g\beta_m)}
       \equiv F_a(\log_E R)\pmod{p^{k+1}}.
 \tag{18}
\]
Use integral lifts of rho modp^m in that display; their error is
in p^(m+1). The period Omega_j is the matched original Tate
period, with phi(Omega_j)=alpha^-1 Omega_j. Its ratio to
the Katz period Omega_p is retained, not set equal to1.
Equation(18) uses the proved integral formal-Kummer descent
and the exact isomorphism H1(Qp,T_pi)→pZp.
In particular modulo p^k in the LOCAL LATTICE means modulo
p^(k+1) in this logarithm coordinate.

The selected ratios are principal units. Other local root
coordinates need not have ratio1 modulo p, but both theta
values are units: the nonzero tame torsion part avoids E[a].
Their prime-to-p residue-unit parts are p-divisible and do
not change the finite p-primary Kummer class. These remarks
do not assert a corresponding point condition at the opposite
completion, where rho is ramified and [barpi] is not a
formal unit automorphism.

**[NEW] Corollary4.2.** At p=5 there exists ONE fixed
R_* in {64P,64Q} such that eta_(R_*,m,2) is nonzero for
EVERY m≥2. Its local evaluation has exact order5 in
H1(Q5,T_pi/25).

The prior independent Taylor certificate proves that at
least one of U_pi(64P),U_pi(64Q) is divisible by5 but not
by25 in the integral local lattice. Choose that R_*;
no choice of scalar or modification of a point is involved.
Equation(16) proves the claim simultaneously for every m≥2.
The global class has order at least5; it is not asserted
to have exactly that order. The corollary is over K and
uses no additional local-restriction injectivity premise.
This proof uses no new numerical run.

## 5. All fixed jets vanish, but a growing layer is nonzero

The powers I^j are intrinsic submodules of the point torsor:
after a choice of origin P=A_k[E[barpi^m]], and changing
origin multiplies by a group unit. Affine Galois transformations
preserve all those submodules.

**[NEW] Theorem5.1.** For a fixed coefficient k and order d≥1,
choose
\[
 r\ge k+\lfloor\log_p d\rfloor,\qquad m\ge r+k.
 \tag{19}
\]
Then eta_(R,m,k) has zero image in
H1(K,(I_(R,m,k)/I_(R,m,k)^(d+1)) tensor T_k).

With compatible origins and generators the point group ring is
A_k[X]/((1+X)^(p^r)-1). For1≤j<p^r,
v_p binom(p^r,j)=r-v_p(j). Condition(19) makes all its
coefficients through degree d vanish modulo p^k, and implies
d<p^r. The actual projection therefore identifies the order-d
point jets at m and r equivariantly. Equation(14) multiplies
their class by p^(m-r), zero modulo p^k. This proves the theorem.
Over K_n, if its original F_m relation is also to be kept,
replace the bound on r by max(n+1,k+floorlog_p d).
These are POINT groups of order p^r, not ray generators
1+p of order p^(r-1).

There is an additional uniqueness statement. Inertia at pi
acts trivially on Y and hence on EVERY subquotient of its
permutation module. It contains an element acting on T_k
by -1, because rho is unramified there and its cyclotomic
Teichmuller inertia is nontrivial. Consequently
\[
 H^0(K,({\cal I}/{\cal I}^{d+1})\otimes T_k)=0.
 \tag{20}
\]
The exact coefficient sequence for I^(d+1)→I then gives
a UNIQUE higher-layer class mapping to eta whenever
Theorem5.1 applies. This argument retains the actual finite
coefficient modules and their long exact sequences; it
does not discard derived base-change or Tor terms.

Taking k=2,p=5, r=m-2 and d=5^(m-3)-1 gives a concrete result.

**[NEW] Corollary5.2.** For the SAME R_* of Corollary4.2
and every m≥4, there is a unique NONZERO class
\[
 \eta^{\mathrm{deep}}_{R_*,m}
 \in H^1\!\left(K,
       {\cal I}_{R_*,m,2}^{\,5^{m-3}}\otimes T_\pi/25\right)
 \tag{21}
\]
whose image is eta_(R_*,m,2). Its local selector is still
the exact-order5 class in(16).

Thus the construction supplies actual nonzero global classes
in a filtration of exponentially growing depth. It does not
assert that their images in the NEXT associated-graded quotient
are nonzero, or replace that quotient by an unjustified free
symmetric-power lattice.

The local functional itself explains the distinction.
Choose its canonical formal origin S_m^0 and a generator sigma
of E[barpi^m]. In these coordinates, for0≤j<p^m,
\[
 \operatorname{ev}_{m,R}((\sigma-1)^j)=(-1)^j.
 \tag{22}
\]
Only the term sigma^0 in the binomial expansion contributes.
Hence this functional does not factor through any truncated
jet of order d<p^m-1, even over A_k. This is an exact property
of the actual selector, not an abstract power-series example.

The functional also does not commute with the coefficient
pushforward in(14): ev_r pi_(m,r) sums ALL lifts of S_r^0,
whereas ev_m selects the unique formal lift. The other
lifts have nonzero étale reduction. This is why the local
norm law has coefficient1 while the global point-projection
law has coefficient p per step.

## 6. The actual first extension and its opposite CM tensor

Choose an origin S_m and a cocycle A(g) for(9).
Write e=aug A=dv. There is a unique v in T_k, and for
any h acting as -1 on T_k it is v=-e(h)/2.
Then A-d(v[S_m]) is the actual cocycle in I tensor T_k.

Modulo I², identify the point-translation quotient with
E[barpi^k] using[barpi^(m-k)]. In that order of tensor factors
the corrected first moment is
\[
 A_1(g)-\kappa_{\bar\pi^k}(R)(g)\otimes g(v)
     \quad\text{in }E[\bar\pi^k]\otimes T_k.
 \tag{23}
\]
The plus point-torsor action produces that sign; it is not
the inverse cyclotomic-character sign. This formula follows
by differentiating the actual affine coefficient action,
not by inserting an arbitrary primitive. Origin and
representative changes give coboundaries by uniqueness.

The isogeny convention is explicit. If [p^k]D=R, then
[pi^k]D is a barpi^k-division point. Thus
\[
 \kappa_{\bar\pi^k}(R)
       =[\pi^k]\operatorname{pr}_{\bar\pi}
                                  \kappa_{p^k}(R).
 \tag{24}
\]
The displayed endomorphism is a UNIT on the opposite
torsion line and is not deleted. The first tensor is the
opposite CM factor, so its pairing with T_pi is the
nondegenerate Weil pairing into mu_(p^k).
With the order in(23), use e_(p^k)(t_barpi,t_pi).
Moving [pi^k] from its first input to the second gives
[barpi^k] by the Weil adjoint, the retained unit alpha^k
in the selected pi coordinate. Reversing the two inputs
would introduce the alternating sign.

This operation sends the CLASS(23) to H¹(K,mu_(p^k)).
It is not a degree-two cup disguised as H¹(T_pi).
The coefficient extension's connecting map instead has
its actual degree-two target
H²(K,E[barpi^k] tensor T_k).
For m≥2k the first-moment class(23), and hence its Weil
contraction, is zero by Theorem5.1 with d=1.
The nonzero growing classes in(21) therefore do not supply
a nonzero first contraction by this operation. No Tate
weights or divided powers of their full deep coefficient
module are silently simplified.

Every G_K-equivariant scalar map P_(R,m,k)→A_k kills I:
transitivity of the actual point torsor forces all basis
values to be equal, so every such map is a scalar multiple
of augmentation. In particular no coordinate selector
extending nontrivially on I descends globally this way.
This statement concerns maps on the full permutation
module. It is not an assertion about every possible
higher extension or map defined only on a subquotient.

## 7. Actual proper-boundary corrections and a surviving quotient

Equation(14a) lets us test EVERY compatible proper-boundary
correction already constructed in the asymmetric proof:
Xi_(m,k)=D_(m,k)-alpha^m(c modp^k)K_pi,k, for c in Zp.
On the point torsor, [barpi^m]S=R, so naturality of point
Kummer gives alpha^m kappa_pi(S)=res kappa_pi(R).
Under Shapiro that restriction is the coefficient norm map.
Put N_(R,m)=sum_(S in Y_(R,m))[S]. Then the actual pullback
of Xi gives
\[
 \eta^{\,c}_{R,m,k}
  =\eta_{R,m,k}
       -(c\bmod p^k)\,N_{R,m}\,\kappa_{\pi,k}(R).
 \tag{25}
\]
This equality is in H1(K,I tensor T_k), since aug(N)=p^m=0
in A_k for m≥k, and follows uniquely from its equality
in the full permutation module. It retains the cancelling
alpha^m and the original Kummer convention. It is an actual
global realization of the allowed correction, not a
scalar selected from its local value.

The norm vector itself occupies a precisely specified deep
coefficient layer. In a chosen group coordinate X=sigma-1,
\[
 N_{R,m}=\sum_{j=0}^{p^m-1}\binom{p^m}{j+1}X^j
 \in I^{D_{m,k}}\setminus I^{D_{m,k}+1},\qquad
                    D_{m,k}=p^{m-k+1}-1.
 \tag{26}
\]
For j+1<p^m the coefficient valuation is m-v_p(j+1).
Thus every coefficient below D_(m,k) is zero modulo p^k,
while that at D has valuation k-1. The group relation
has zero coefficients through degree D, so it cannot
remove that leading coefficient in the quotient by I^(D+1).
This verifies the assertion in the actual finite group
ring, not merely in a free formal series ring.
Translation changes the chosen origin by a group unit
and fixes the norm vector.

The local functional has ev(N)=1. Thus(25) evaluates to
U_pi(R)-c kappa_pi(R), exactly the original proper-point
correction. The injection into the full module and the
coefficient maps in(14b) also show that(25) retains the
same p-per-step law. It does not turn the nonlinear
selector into a global scalar morphism.

Here is an ACTUAL nonzero quotient component after ALL
these common-c corrections. Work at p=5,k=2. Write
x=log_E(64P), y=log_E(64Q). The completed exact point
check gives v5(x)=v5(y)=1 and v5(x+y)=2; hence
v5(x-y)=1. The local coordinate
L_2:H1(Q5,T_pi/25)→Z/25 is Log_omega/5.
This is defined by the already proved nonanomalous
integral Kummer table, including its finite coefficient
identification. Put a=x/5 mod25, b=y/5 mod25.
They are units, determined by the fixed points and
the Néron differential, not by the theta values.

On the DIRECT SUM of the two actual global coefficient
groups for64P and64Q, define
\[
 {\cal L}_m(z_P,z_Q)
    =b\,L_2(\operatorname{ev}_{m,P}\operatorname{loc}z_P)
      -a\,L_2(\operatorname{ev}_{m,Q}\operatorname{loc}z_Q).
 \tag{27}
\]
It kills the entire common-c line in(25), since that
line has local coordinate c(a,b). For the original pair
its value is
\[
 {\cal L}_m(\eta_P,\eta_Q)
       =\frac{yF_a(x)-xF_a(y)}{25}\bmod25,\qquad
 v_5\!\left(\frac{yF_a(x)-xF_a(y)}{25}\right)=1.
 \tag{28}
\]
Indeed the numerator's quadratic term is
(C_2/2)xy(x-y), of valuation3, because C_2 is a unit.
For d≥3, its d-th term has valuation at least
d+1-v5(d!)≥4. The all-degree integral coefficient bound
and convergence justify this bound for the whole tail.
The C_1 term cancels exactly. Therefore there is no
cancellation of the quadratic term and(28) follows.
This uses only the already certified C_2 and point
valuations; no new arithmetic run is required.

Consequently the PAIR of global theta coefficient classes
has a nonzero image, detected by an element of exact
order5, modulo the entire common-c proper-point correction
line. In particular every allowed c leaves at least one
of the two corrected global classes nonzero modulo25.
For m≥4 the same conclusion holds in their unique deep
lifts(21): D_(m,2)=5^(m-1)-1 is at least5^(m-3), so
the correction vectors also lie in that deep coefficient
submodule. The local covector(27) is used to PROVE
nonzero global cohomology; it is not asserted to be a
rational motivic covector or the BSD determinant.

## 8. Arithmetic boundaries and the original ray comparison

The exact finite valuation of(7) is
\[
 v(f_{a,R,m})=
 -12\bigl(v(\psi_a(\beta_m+S_m))
                      -v(\psi_a(\beta_m))\bigr).
 \tag{29}
\]
The common Delta factor cancels. The formula holds at
EVERY finite place, with its actual normalized valuation.
Outside residue characteristic p it first gives the usual
unit-Kummer residue OVER THE ACTUAL SOURCE FIELD, where
rho modulo p^k is trivial. The chosen tensor and the actual
corestriction/localization maps then transport that class.
At a base place with ramified coefficients those maps are
retained; they are not replaced by an unramified scalar
valuation map. At p use the actual local cohomology classes,
not a tame residue formula. All such valuations have
finite support at each level. No uniform support theorem
in m is supplied.

At pi the ratio in the selected branch is a principal
unit and gives the nonzero local finite class already proved.
At the opposite place the point division is ramified;
there is no Qp-fixed formal inverse or automatic finite-flat
extension of the ramified rho twist to an étale T_pi line.
The precise local class is still the sum of the actual
Kummer classes(7) with the original rho transports in(9).
Neither that class nor any new arithmetic residue is
discarded because log_p(p)=0.

The primitive opposite-ray denominator is also retained.
For m≥1 the complete primitive ray norm of the base theta
is the already proved quotient
\[
 N_{B_m/F_0}\Theta_a(\beta_m)
   =\frac{\Theta_a(\tau_0)}
          {\Theta_a([\bar\pi^{-1}]_{\mathfrak f}\tau_0)}
 \tag{30}
\]
when interpreted away from zeros and poles; here the numerator
at tau0 is a nonzero torsion value. More generally a point
translation has the full endomorphism and imprimitive
denominator from the predecessor's formula(17).
Equation(8) is not an instruction to drop either ray term.
The ratio numerator Theta_a(tau0+R) is not an original
torsion-only Euler-system unit.

Equations(12),(14),(16),(23),(25),(28) are concrete comparisons with
the original branch and its actual local point line. They
give zero complete scalar augmentation, a p-scaled point
tower, the exact nonlinear local selector, a zero eventual first
Weil contraction and a nonzero quotient by the allowed common
proper-point correction. They give no scalar map
to the original cyclotomic derived class w0.
The full Selmer condition for that old class is a separate
established result and is not propagated through an
unconstructed global selector.

## 9. The first remaining identity and its determinant frame

Let z_unit(X,Y), d_pi,d_barpi and w0=Sh(d_pi+d_barpi) be
the ORIGINAL normalized ray class and its reviewed derivatives.
Their coefficient source is the two-variable ray deformation,
whereas(9) uses the actual opposite point torsor and a ratio.
Our class is not assigned the value of any of those derivatives.

For an ordinary coefficient morphism to T_k, the preceding
transitivity forces augmentation, which is zero on eta.
The actual first Weil operation has a DIFFERENT Tate target
and is eventually zero. The local formal coordinate is
nonlinear: the completed p5 test proves that no one scalar
multiple of point Kummer agrees at64P,64Q,64(P+Q).
Thus these three explicit candidate transports have been
tested on the constructed objects, not merely rejected
on abstract rank grounds.

**[OPEN, CM-Global-Selector].** Construct an actual secondary
arithmetic operation on the classes(9)–(10), with their
boundary and coefficient towers, whose output satisfies
all the original global Selmer conditions and has the
specified original-ray value w0 (or the corresponding
determinant-valued comparison). It must explain how its
p-per-step point law and growing local selector relate
to the original ray Bockstein; no division by p or scalar
point adjustment is part of the construction so far.

The exact existing target retains
\[
 h_\Gamma(x,w_0\otimes T)
       =k_\alpha\log_\omega(x)c_{2,p}T^2,\qquad
 k_\alpha=(1-\alpha^{-1})^{-1}(1-(p/\alpha)^{-1}),
 \tag{31}
\]
and the old determinant coordinate
c_(2,p)=iota_p(F_20+F_11+F_02), with
F=(-1)^b u det(A), including u(0).
The CM-to-Néron and Euler conversions remain
\[
 c_{2,p}=\frac{c_{\rm cmp,p}M_p}{2g_p^2},\quad
 c_{\rm cmp,p}=(156i\Omega_p)^{-1},\quad
 e_p=(1-\alpha^{-1})^2,\quad k_\alpha e_p=N_p/p.
 \tag{32}
\]
Only under the separately proved rank/nondegeneracy premises
may the framed projection be inverted, with its factor
p/(2N_p), to give the old coefficient
c_cmp,p M_p/(4 e_p Reg_p). The integral Smith and saturated
P,Q frames are not reselected. Rationality must be proved
before comparing to a SINGLE rational framed element whose
real realization is (L''(E,1)/2)/(2Omega_E).

The local Taylor coefficient C_2 and the old c_(2,p)
are different quantities. This round proves a nonzero
GLOBAL COEFFICIENT class using C_2 at5, without deriving
a new old-coefficient or Sha result. No Sha finiteness,
Selmer corank2 or rationality of the complex quotient
is assumed. All-prime index control, the remaining primes
and full universal BSD remain open.

## 10. Source and verification record

The exact norm and cross-smoothing source is
[Kato2004, Proposition1.3(2),(4), proof1.10](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
printed pp.121–125; the actual CM character convention is §15.8,
printed pp.256–257. These passages were reread in the existing
PDF/text cache /tmp/cm-derived-kato2004.pdf and .txt, PDF SHA256
3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d.
The isogeny norm has constant1 and preserves the original
twelfth power. No primitive-ray norm is identified with
a full fiber without its displayed denominator.

Finite cochains, finite étale Shapiro and the actual
coefficient exact sequences use
[Nekovář, Selmer complexes, §§3.4,6.1,8.1](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
with the same checked conventions as the preceding cone proof.
No flatness or cohomology/base-change identification replaces
these finite exact sequences.

The field degrees, full Kummer image, CM ray branch, formal
inverse and its local integral Kummer identification are
the separately reviewed predecessor inputs. The new
transfer diagram, augmentation, local evaluation and
growing-depth deductions are proved above.
The two-point nonvanishing input is exactly §8 of the
separate local Taylor audit, not an unreviewed numerical print.

The [independent review](review-cm-global-selector.md) passed all ten
sections, including (5)–(6), the finite rho augmentation, the full
semilocal selector in(16), the distinction between its norm law and(14),
the exact pullback and replication, the nonzero growing-layer conclusion
and the common-c quotient(28). The two recorded scope precisions changed
no formula: augmentation itself is nonzero, and ordinary unit residues
are first taken over the actual rho-trivial source. The global Selmer,
original Kato and rational-frame comparison remains open as stated above.
No old numerical run, prime scan, new agent or edit of a
shared/completed proof was made.
