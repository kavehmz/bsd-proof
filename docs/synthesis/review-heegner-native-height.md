# Independent review of the native isogeny and Cassels–Tate construction

Date: 2026-09-12. Reviewer root/coordinator.
**PASS for all seven sections, including the separate norm-Prym subcase.**
Reviewed [proof](heegner-native-height-comparison.md), SHA256
75370e6e4a132e2b0311991e421770fbe97db56c2c030aed9c48ad213ab5c693,
and [checkpoint](heegner-native-height-checkpoint.md), SHA256
7e994737ff65d772826d6a2701d5f041ad7b2457f82c4be14e42702a555ee99a.
Subsequent completion and review-link changes are editorial.

I read the full saved proof and reconstructed each new assertion.
The operation identifies the particular native obstruction with a
classical Cassels–Tate pairing on actual isogeny quotients.
It does not prove that this pairing vanishes from the complex zero.
The point subcase is expressly additional and not assumed for Kato.

## 1. Actual isogenies and the exact native local conditions

For A=Res_(F/Q)E, Galois descent of the product gives the stated
dimension2p^e and its induced torsion module. The fixed quotient
rho:A[n]→N_i therefore defines a finite subgroup scheme K.
I checked [Milne AV v2.0](https://www.jmilne.org/math/CourseNotes/AV.pdf),
I Remark8.12 and IV Lemma2.1 (PDF pp44,140): the quotient exists
over Q because the finite characteristic-zero kernel is Galois stable.
Multiplication[n] factors through it. Thus B=A/K and psi:B→A
have the marked kernel N_i and degree n^4.

Quotienting B by its actual M_D subgroup gives B→C→A,
with degree n² for each factor and the original marked finite
kernel sequence. No arbitrary isomorphic extension is substituted.

For a local point P of A, naturality sends its n-Kummer cocycle
to its psi-Kummer cocycle. Shapiro uses all local E(F_w) points,
so the image is exactly the native condition. The preimage on M_D
is the kernel of the SAME map into H¹(B). This proves the equality
even when H¹(M_D)→H¹(N_i) is not injective, retaining H0 terms.
The image on M is the psi2-Kummer condition because both images
range over all A(Q_v). In particular, the zero old native image
and nonzero transverse preimage are compatible.

## 2. The actual two torsors and the pairing sign

I checked [Morgan–Smith2103.08530v2](https://arxiv.org/pdf/2103.08530v2),
Definition3.2, Proposition6.1 and §6.1 in the explicit 44-page
revision with arXiv stamp26June2022. Its HTML/re-rendered header
date is not used as evidence of a newer theorem. Proposition6.1
identifies exact dual isogeny Kummer annihilators; §6.1 identifies
the factor-isogeny pairing with the classical Sha pairing.

Thus the input z and lambda_D(b_i), with
lambda_D(b)(m)=e_n(m,b), give the specified locally trivial
torsors xi_i(z) on C and upsilon_i on C^dual. This uses native
LOCAL lifts and makes no assumption of a global native lift.
Their vanishing or primitivity is not asserted. The two exact
point quotients in(14) are ordinary isogeny Kummer sequences.

For the sign, choose the already constructed global cocycle f
and the native local cocycles f_v. In Definition3.2, df=0 permits
epsilon=0. The required difference is GLOBAL minus LOCAL,
namely -eta_v. Evaluation against lambda_D(b_i) is exactly
e_n(-eta_v,b_i), with the first coefficient in the declared
compact-first position. Finite/finite terms vanish away from i,
leaving -R_i/n. Hence
$$
 \operatorname{CT}_{C}(\xi_i(z),\upsilon_i)=-R_i(z)/n.
$$
The source comparison has exactly C as its intermediate abelian
variety, so both torsors occur on the correct dual pair.
No finite Sha assumption is used. The nonclean formula retains
the full local sum rather than replacing its dual Selmer group
by a free line.

Restriction of both classes from Q to K multiplies the pairing
by2, by the local invariant formula and summing split places.
This has no effect on the finite tame inertia coordinate.
The preexisting point-dual transport, d0, and top-Heegner sign
are correctly kept separate from this new minus sign.

## 3. The marked finite inclusion has no elliptic extension

The plus coordinate in the stated sum/difference basis is half
the norm on A[n]. Since2 is a unit modulo n, its kernel is P0[n],
where P0 is the connected norm kernel. Thus C=A/P0[n].
The geometric sum map has connected kernel, proving that P0
is an abelian variety.

In the non-CM range, End_F(E)=Z. Weil restriction adjunction
gives Hom_Q(E,A)=Z times the diagonal j. Because
Norm j=[2p^e] and n divides p^e, q2j kills E[n] and factors
through[n] as j0[n]. Then psi2j0=j.
For any h:E→C, write psi2h=mj; the two isogeny identities give
nh=mn j0. Hom groups have no torsion, so h=mj0.

If h(E[n]) lies in ker psi2, then mj kills E[n].
Injectivity of j forces n dividing m, hence h kills E[n].
Clearing a denominator prime to p gives the same conclusion
in that coefficient range. This proves the claimed failure on
the actual varieties; it does not exclude arbitrary more elaborate
correspondences or complexes.

## 4. The separate rational-point subcase and its factor2

For z=Kum_n(P), the pushout of
0→P0→A→E→0 along[n] on P0 is
0→P0→C→E→0, with q2|P0=j_P[n].
The induced map from ker psi2 to E[n] is twice its MARKED
identification, as follows from the half-norm quotient.

I independently checked the cocycle formula. Choose nQ=P
and Norm(a)=Q. Then d(na) has values in P0.
For each g choose r_g with n r_g=d(na)_g; the point
u_g=da_g-r_g lies in A[n] and has norm dQ_g.
The marked kernel inclusion therefore gives
2q2(u_g)=2d(q2a)_g-2j_P d(na)_g.
Taking cohomology yields exactly
$$
 \xi_i(\operatorname{Kum}_nP)=-j_{P,*}\partial_{\rm Norm}(2P).
$$
Changing r_g by n-torsion has no effect after q2.

The psi2 Kummer class of Q_A in A(Q_v) maps to half the
n-Kummer class of Norm(Q_A). Hence its native local condition is
2P in Norm A(Q_v)+nE(Q_v); the global version is equivalent
to xi_i=0 by the global Kummer sequence. Alternatively the kernel
of H¹(P0)→H¹(C) is the image of n times the norm boundary, giving
the same global criterion.

The proof correctly does not put the unpushed norm torsor in Sha(P0).
Only its push is locally trivial under these congruences.
Nor does it identify the actual Kato input with a point.

## 5. The tame character and all arithmetic constituents remain

The local tame relation Frob sigma Frob^-1=sigma^(i²) forces
(i²-1)chi(sigma)=0 for any additive Z_p-valued abelian character.
Since Z_p is torsion-free, its tame value iszero. This cannot
reduce to the actual a_i(sigma)=-1 modulo p^k.
The finite character exists because v_p(i²-1)>=k, which does
not contradict the torsion-free statement.

I checked [Howard1202.6343v1, Definition2.4 and Theorem2.5](https://arxiv.org/html/1202.6343v1):
its derivative is the coefficient of the propagated Iwasawa
Selmer class with its own local conditions.
I also checked [Macias Castillo–Sano2603.23978v1, §4.1](https://arxiv.org/html/2603.23978v1):
it explicitly fixes a Z_p-extension, good ordinary reduction,
the Tamagawa/reduction-unit and Cartan-image hypotheses;
Theorem4.2 compares the BD and Nekovar pairings in that setting.
Neither statement identifies the finite ramified coordinate or
the untwisted complex third derivative with this native value.

Finally the regular representation of the dihedral group has
the trivial and quadratic characters once and every nontrivial
two-dimensional induced representation twice. Artin formalism
therefore gives exactly(20), with complete local factors.
Passing to the isogenous C does not remove these constituents.
The untwisted zero alone has not been proved to kill either
specified torsor or their Cassels–Tate pairing.

The sufficient point-preimage, divisibility, norm-congruence and
specific orthogonality targets are correctly stated as unproved.
The mixed/top Heegner ambiguity remains even after hypothetical
vanishing of the first two pairings. No old computation was
rerun for this review.
