# Independent review of the Poisson tangential fiber

Date: 2026-09-13. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
**PASS for all eight sections. No mathematical correction required.**
Reviewed [construction](poisson-tangential-fiber-attack.md), SHA256
3c46ea64a8e448f5ae54c752ebb2962753eab7959dab53334dde0f6f3b905fba,
and [checkpoint](poisson-tangential-fiber-checkpoint.md), SHA256
8d75ac45a1aa2563d647e224385dfa0c4f1c49401479fa54f75bb58fda5fdfa7.
The checkpoint's initial candidates and review assignments are historical;
the current eight-section proof is the mathematical object audited here.
Only this review file was written. No old numerical computation or
certificate was rerun and no additional agent was used.

The [path motive review](review-poisson-path-motive.md) and
[canonical Hodge framing review](review-poisson-hodge-framing.md) are
explicit inherited inputs. The new conclusions are an actual tangential
source, its exact central limit value, and the weighted algebraic
fiber trace removing the cusp subtraction. They do not construct a
rational motivic delta/Petersson operation or prove BSD.

## 1. Actual algebraic parameter and logarithm motive

The rational formal q parameter at the rational cusp determines a
nonzero rational cotangent vector. Surjectivity of the local maximal
ideal onto its cotangent space therefore supplies t in O_(X,c) with
leading coefficient one relative to q. Shrinking makes it a regular
function with exactly the indicated simple zero and an etale map to
A1 near the cusp. This does not identify the formal q series with a
global rational function.

The Delta leading terms give m_infinity=-388 and a_infinity=389^-6.
Since u composed with the rational Fricke involution equals u^-1,
the corresponding other-cusp values are m_0=388 and a_0=389^6.
The normalized tangent, rather than a discarded leading unit, fixes
these constants.

I directly inspected [Ayoub, The motivic nearby cycles and the
conservation conjecture, §4.6](https://user.math.uzh.ch/ayoub/PDF-Files/Leiden.pdf),
the42-page author PDF. Definitions4.29 and4.32 give K and Sym^n K;
Definition4.38 uses Hom(Log_n,-). Proposition4.42 identifies this
logarithmic system with Upsilon, and the paragraph after
Corollary4.46 explicitly proves constructibility preservation.
These are characteristic-zero rational motivic statements applicable
to the present smooth Q schemes and their finite field extensions.

Because the finite logarithms are dualizable, Hom(Log_n,M) is
M tensor Log_n^dual. This is the exact dual ind-system used in(2.1).
Its Hodge weights are0,2,...,2n. With the determinant identification,
the twist is -n, not+n. The construction uses the dual itself and its
specified transition maps, avoiding any unproved motivic heart,
kernel, or inference from Betti stabilization.

The etale-parameter constant specialization is the constant
coefficient with its unit frame. Applying the exact functor to the
existing bottom and top maps therefore gives the actual frame maps
in(2.2). Compatibility with the finite proper basepoint map preserves
the preceding Artin unit and trace construction; no new denominator
appears in specialization.

## 2. Realization and the ordinary/perverse shift

I checked [Ivorra–Morel, Lemma3.13 and Corollary3.14](https://morel.perso.math.cnrs.fr/PerverseMotives.pdf),
printed pp.33–34 of the62-page author PDF. Their logarithmic Betti
functor is ordinary unipotent nearby cycles; its shift[-1] is
perverse t-exact. This is the Betti normalization used in the proof.

[Tubach2407.02256v3, Theorem1.4 and Proposition3.31](https://arxiv.org/html/2407.02256v3)
give the colimit-preserving six-operation Hodge realization and
Upsilon[-1]=Saito's perverse nearby functor on the stated finite-type
complex schemes. Its proof supplies the logarithmic colimit model.
The realization is applied after base change to C; it does not
presume a category of arithmetic mixed Hodge modules over Q.

I also directly checked [Saito1990, Extension of mixed Hodge modules,
§1.1 and Proposition1.3](https://www.numdam.org/item/CM_1990__74_2_209_0.pdf),
printed pp.210–213. The positive-weight logarithmic system and
the perverse shift agree. An ordinary local system V on a smooth
curve corresponds to the perverse object V[1]. Thus
psi_perv(V[1]) is its limit in degreezero, and
Upsilon(V)=psi_perv(V[1]); there is no additional[-1].

The explicit polynomial check is consistent. Dual positive
Kummer transport sends T to T-1, so the total logarithm is
L-d/dT. Conjugation by exp(TL) reduces this operator to -d/dT.
It is surjective on V[T] over Q, and its kernel is exp(TL)V.
The resulting cohomology is the full fiber in degreezero,
not merely ker L. This illustrates the normalization; the
actual motivic constructibility follows from Ayoub's theorem.

## 3. Monodromy, weights and chronological sign

Appending the positive cusp loop adds the cusp Tate class to the
top-to-length-one quotient. On a prefix-loop difference, the
degree-two addition is the ordered compact-prefix/cusp product.
Its push by pi_* tensor u_* lies in K. A cusp first factor is killed
by pi_*, and all degree-two elements are fixed modulo lengththree.
Consequently L^2=0, L kills K and the middle Tate direction, and
L lowers W by at least two. No genus contribution has been removed.

I inspected [Saito1605.00435v5, §3.1 and Theorem3.4](https://arxiv.org/html/1605.00435v5).
The geometric smooth realization, with its ordinary/perverse shift
understood, is an admissible variation. Here the graded pieces of W
are constant and L acts trivially on each of them. The filtration W
itself satisfies the relative-monodromy conditions: on Gr_r^W the
induced filtration is concentrated in degree r, and every required
nonzero-power isomorphism is between zero spaces. Uniqueness therefore
identifies the limit weight filtration with W.

The positive PATH TRANSPORT logarithm is a real Betti endomorphism.
The de Rham factor2pi i belongs to the Tate comparison, not a rational
change of that Betti frame. On the coordinate Kummer example the
Deligne top lift is eB-(logt/(2pi i))tB while positive transport sends
eB to eB+tB. This fixes the homological orbit sign

    F(t)=exp(-logt/(2pi i) L)F_tan.

The alternative inverse-transport convention would rename L; it
does not change this actual period table.

For the limit and tangent comparison I read [Hain, published2025
version, §11, Propositions11.1–11.2](https://dukespace.lib.duke.edu/server/api/core/bitstreams/757f44c8-ab9d-4eda-b0e3-315bd58b160d/content),
the40-page paper, printed pp.25–26. It supplies the tangent-dependent
limit MHS, the Tate-valued monodromy morphism, and the holomorphic
canonical-extension correction. I used this actual PDF endpoint
rather than the repository's HTML download landing page.

## 4. The complete corrected period table

For alpha, A=A_c+O(t) and theta=m_c dt/t plus a regular differential.
Thus df_alpha has precisely logarithmic residue m_c A_c.
For the second-kind row, Atilde may have poles, but xi_b has the
FULL prescribed principal part of (bar A_c-Atilde)theta.
Their sum has residue m_c bar A_c and no higher pole. Subtracting
the holomorphic Lambda10 does not change that residue.
This proves both finite parts in(4.3) after the actual correction.
It would not justify taking a finite part of the uncorrected rho word.

The prefix-loop Chen formula gives the two rows
I_alpha,theta(h)+a_h B and
I_rho,theta(h)+int_h xi_b-int_h Lambda10+bar a_h B.
Their logarithmic terms are exactly m_c a_h logt and
m_c bar a_h logt. The cusp middle direction has a_h=0.
On K the constant restrictions still have the2pi i factor and
f_rhoD=-bar f_alpha. Thus the untwisting removes precisely the
monodromy on EVERY graded piece, including the middle directions
and the retained top constant.

The resulting row limits belong to the limiting Hodge filtration,
by the canonical extension comparison. The weights of the lower
first-path quotient are unchanged, so it still has no F2; this
fixes the canonical I^(2,1) lift. For the other row, the lower
restriction remains Lambda01+2Re(B_c^tan)bar alpha with its possible
weight-zero constant and no Tate component. The same Deligne
I^(1,2) formula from the completed proof therefore applies.
No top constant or compact-genus period is silently discarded.

The first Kummer row has real finite part log|a_c/2|, not zero.
The imaginary branch is retained consistently with transport.

## 5. Exact central limit and tangent dependence

Using the complete table in the already checked finite-dimensional
Deligne calculation gives exactly(5.3). The finite-endpoint formula
has the same compact correction int bar Lambda01. Its possible
unbounded real term is

    Re[2m_c log|t| A_c-m_c(A_c+bar A_c)logt].

Writing A_c=a+ib and logt=l+i theta shows the bracket is purely
imaginary. It is therefore zero after taking the real part, with
no missing constant. The remaining errors are O(|t||log|t||)
and O(|t|) on a bounded branch, and tend to zero. Single-valuedness
of the original scalar then gives its unrestricted cusp limit.
This proves h_tan=lim h for THIS full period table, rather than
invoking unproved continuity of an arbitrary mixed height.

The structural check also works. Functoriality with the Tate-valued
monodromy gives [delta_tan,L]=0. For w=-logt/(2pi i),
delta_orbit=delta_tan+Im(w)L makes the split filtration
exp(Re(w)L)exp(-i delta_tan)F_tan real. The Deligne top and projections
transform by exp(wL). Since L maps the top Deligne type(0,0) to
the pure Tate type(-1,-1), its weight-minus-three projection is zero.
The central scalar is consequently constant on that orbit.
This also proves its asserted independence under a nonzero complex
tangent rescaling, without identifying the full framed motives.

The finite proper-base averaging has the unchanged trace denominator.
It yields the average of all conjugate central limits and hence(6.2).
The two zero cusp values of q_F are inherited proved inputs; the
resulting equality of the two central tangent values does not identify
their Kummer leading units or their full motive objects.

## 6. Proper pushforward of the curvature and branch values

I reconstructed the curvature normalization. With
dd^c=i/(2pi)partial barpartial, differentiating the original real
Poisson numerator gives one-half of
alpha wedge bar theta+theta wedge bar alpha. Dividing by its
4pi c_pi normalization gives exactly

    dd^c q_F=i/(16pi^2 c_pi)
                    (alpha wedge bar theta+theta wedge bar alpha).

The corrected cusp expansion has size O(|q| |log|q||) after its
constant, and its first derivative has logarithmic growth. Boundary
flux tends to zero, so extending the equation to X introduces no
delta mass. Its right side is an L1 measure at both cusps.

For r=u, theta=r*(dw/w) off0,infinity. The differential trace of
alpha is holomorphic even at branch points. Locally w=z^e, a term
z^n dz contributes only when n=e-1+je, in which case its trace
is the corresponding holomorphic w^j dw term. The reciprocal
coordinate gives the same assertion at infinity. A global
holomorphic differential on P1 is zero.

Proper pushforward commutes with dd^c. Off the finite set of branch
values and0,infinity the curvature pushforward is therefore zero.
The push of the L1 measure has no atoms there, since each fiber is
finite and has zero area. More strongly it is absolutely continuous:
away from the finite critical set the map is locally a diffeomorphism,
and that critical set and its fibers have measure zero. In either
form, no measure supported on the exceptional finite set survives.

Thus r_*q_F is a harmonic distribution on compact P1 and is a smooth
constant. Off the branch values it is the usual sum over inverse
branches. Continuity of q_F makes its value at a branch limit the
sum with the actual ramification multiplicities. At infinity there
is one point of multiplicity388 with q_F=0. The constant is zero.
This proves(8.2) without assuming an unramified u=2 fiber.

## 7. Actual fiber multiplicities, both traces and spectral factor

The pole divisor of u-2 is388[c_infinity]. Its zero divisor has
the same degree, so the multiplicities e_b, including closed-point
residue degrees, sum to388 after complex base change. They are
Galois-stable. The reduced fiber is finite etale over Q, while its
possibly nontrivial multiplicities give the indicated Artin
endomorphism. Neither fact requires that r be unramified at b.

The coincident constant path satisfies h_b(b)=0 in the completed
augmented source. Its exact endpoint formula therefore gives
h_b,infinity=c_pi q_F(b). Applying(8.2) gives the weighted sum(8.3).
Individual cusp constants are not asserted zero.

The old top pullback along the Artin unit is unchanged. Replacing
the bottom map by Tr_e, respectively Tr_e/388, is an actual rational
cofiber/pushout construction. On realizations, functorial Deligne
splitting gives the weighted sum, respectively its division by388.
The composite Tr_e with the unit is388, not degree(B2). Hence

    h_Sigma=-388 c_pi q_F,       h_e=-c_pi q_F.

The unnormalized map uses the integral divisor multiplicities. The
normalized version deliberately divides by388 and therefore retains
the primes2 and97. It does not certify primitivity of all the other
rational projectors used in constructing the source.
Both central tangent scalars are zero; the cusp motives themselves
are not thereby zero.

Finally, substituting q_F=-h_Sigma/(388 c_pi) in the completed
linear spectral operation
-pi*388/(4sqrt(389))<I_L(q_F),R_omega>
gives exactly pi/(4sqrt(389)c_pi)<I_L(h_Sigma),R_omega>.
This checks the sign and the single cancellation of388 in(8.6).
The normalized bottom trace would require its corresponding388
factor instead; the proof uses the unnormalized source as stated.

## 8. Verdict limits

All eight sections pass with their exact source and realization
scope. The tangential source is an actual constructible rational
motive with the indicated framed Hodge realization. Its central
invariant equals the finite cusp limit, and the weighted u=2
Artin source removes that constant from the Poisson formula.

These conclusions do not make the Deligne splitting rational,
produce a motivic weight/kernel t-structure, identify a Petersson
functional with an arithmetic morphism, remove the marked point–K2
obstruction, or prove the BSD determinant. The universal objective
remains unresolved. No author file or shared synthesis was edited.
