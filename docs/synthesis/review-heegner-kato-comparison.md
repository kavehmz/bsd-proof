# Independent review of the Heegner–Kato comparison

Date: 2026-09-12. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. Review of
[the proof](heegner-kato-comparison-attack.md) and
[checkpoint](heegner-kato-comparison-checkpoint.md).

**PASS after the explicit cohomology-comparison repair.** All eight
sections and the final old-prime cup map are verified.
Final mathematical proof reviewed:
84297adc102effbcc5a1d92bafef70330b832bd970c58b31913555e72aa0a64e.
Checkpoint:
0d925be445e6b0778bbe103bb0e6e0e2bf3405f0db7fff73d5ee1c24e0190069.
The Kato j_* versus full Galois comparison and the p-relaxed third
BF coefficient clarification were inspected in this exact revision.
No further mathematical correction remains. The required rank-five
comparison and universal BSD remain unproved.

## 1. The requested comparison has been repaired

Kato's §8.2 defines cohomology on the arithmetic scheme using j_* of
the representation, and §12.2 uses that convention in the cyclotomic
tower. The new proof instead works with the full S_0-Galois complex.
Before applying Theorem 12.5(3) to its H², the local complexes
at bad primes must be checked acyclic at the height-one prime (X).
Changing only the zeta element's Euler factors does not by itself
identify these two cohomology complexes.

The final proof now supplies that comparison. At v≠p the rational local
cohomology of the elliptic Tate module vanishes in degrees one and
two. The relevant finite-field inertia-cohomology localization
complex consequently has no Frobenius eigenvalue one at the trivial
character; its Iwasawa Euler polynomial has nonzero augmentation.
Its bounded Iwasawa local complex has finitely generated cohomology
and this acyclic derived rational augmentation fiber. Derived Nakayama
over the height-one DVR makes its localization acyclic. This identifies
Kato's complex with the full Galois complex at (X). The integral
saturation argument then independently uses the FULL Galois coefficient
sequence (5). I inspected the added argument directly. It repairs the
proof's source/target comparison without changing the X² conclusion.

## 2. Second Kato division and finite local conditions

I read Kato, Astérisque295(2004), §§8.2,12.2–12.5 and18.4 directly
in the complete cached primary source, including the rendered
printed p.281 for18.4. The exact rational height-one inequality is
$$\operatorname{length}H^2_{(X)}
 \le\operatorname{length}(H^1/Z(f))_{(X)}
       +\operatorname{length}H^2_{{\rm loc},(X)}.$$
The exceptional p-local term vanishes at good reduction. The
conjugation relation selects a single nonzero Betti coefficient on
the stated trivial finite branch, so the resulting length estimate
concerns the actual Kato class. The integral big-image part of12.5
is not used.

The full compact Selmer group has rank at least three even if a
divisible Sha contribution is present. Global Euler characteristic
then gives dimension at least two for rational H². Derived
cyclotomic specialization gives H²/X and an injection H¹/X into
global H¹. Thus, after the comparison in §1, the length estimate
gives X²-divisibility at (X).

The integral descent from that localization is correct. Global H¹(T)
has no p-power torsion because E(Q)[p∞]=0. An element outside (X)
acts on H¹/X through a nonzero Z_p augmentation scalar. Its
annihilation of an image in that torsion-free group forces the image
to vanish. Applying this argument twice gives actual integral
division, and X-torsion-freeness gives uniqueness.

Kato18.4 bounds the cyclotomic p-adic order below by Selmer corank,
not only Mordell–Weil rank. Hence F_E∈X³. The Coleman specialization
then gives zero dual exponential for w_0 at p. At v≠p all integral
H¹(T) is the completion of the local point Kummer group, since the
local Weil–Châtelet p-primary group is finite. This verifies the full
finite local conditions after reduction. No finite global Sha
hypothesis or complex-to-p-adic rank equality enters.

The initial nonanomalous/modular-lattice range is retained. The
prime-to-p isogeny assertion follows from irreducibility: a
p-primary kernel either contains a stable line or all E[p], and
the latter permits factoring a minimal isogeny through [p].

## 3. Published BDV normalization and all jets

I inspected the published 50-page BDV source at pp.32–38,
Theorems4.2–4.3 and equations23–30. Its basis is exactly
$e_+=v_g^++v_g^-$, $e_-=v_g^+-v_g^-$ and
$\Omega_{g,\gamma}=2\langle v_g^+,\omega_g\rangle$.
At weight two and good p the stabilization scalar is exactly
$\alpha(p-1)(1-\alpha^{-2})(1-p^{-1}\alpha^{-2})$.
The smoothing factor has exponent2t+1 because k_0=2; its level
power is then one. The source's twist transport uses precisely
$u_\iota^{-1}\iota_*z_D$.

The resulting equality is global Iwasawa cohomology, not merely
equality of logarithms. Its normalized integral image is specified
by the right side of (8); no saturation of the geometric BF lattice
is inferred. I also checked the exact Néron-period interpolation
in BCGS2312.09301v2 Theorems3.2.1–3.2.2.

Substituting z_E=X²w and F_E=X³C proves d_0w_0 as the second
plus coefficient and c_3z_D,0 as the third minus coefficient.
The twist's nonzero dual exponential proves z_D,0≠0; it also
shows this bottom twist class is p-relaxed rather than classical
Selmer. The note does not assign it a Selmer height.
The next plus coefficient satisfies its displayed non-cocycle
Bockstein equation. Under the inverse-character action, direct
expansion gives d w_1=ell_gamma cup w_0 with the stated sign.
The chain-rule coefficient is exactly
$L_p^{(3)}(E,1)/(6\log_p(1+p)^3)$, which cannot be reduced by
dropping its logarithmic denominator.

## 4. The actual old-prime cofactor map

For any finite Selmer classes a,b, the alternating identity in R²
proves that (13) lands in the full strict group. No determinant is
inverted. Its signed fresh-prime test has the Q/K factor2 exactly.
In the primitive case, the earlier reviewed full strict cyclicity
and surjectivity of old localizations justify the chosen sections.
Changing them by tκ,sκ gives exactly
$A_{a+tκ,b+sκ}=A_{a,b}-t\,l_\ell(w_k)-s\,l_q(w_k)$.
Thus neither the scalar nor its unit status is made canonical.
The residual class in S/Rκ is correctly retained outside the
primitive case.

## 5. Genuine tame representation and full Shapiro coefficient

The extra condition p∤h_K is essential and is stated only for this
part. It makes the p-primary ring-class group the product of the
two displayed cyclic groups. Their orders are divisible by p^k,
so σ_i↦1+Y_i defines the actual quotient with Y_i²=0.
The inverse Artin character has precisely the mixed coefficient
$a_\ell a_qY_\ell Y_q$. Changing from its two characters to
sum/difference basis gives matrix(20), including the identity
matrix on the mixed coefficient and the correct conjugation.
Nontrivial p-power characters have no map to1⊕epsilon_K in
characteristic zero; the finite nonsemisimple quotient is therefore
doing substantive work.

On restriction to H_m, Shapiro gives the inverse group-ring sum
(23). The prime-to-p trace introduces no averaging denominator.
The compatible representatives can have zero p-Artin coordinates.
The constant and each single coefficient vanish by actual Fourier
factors a_ell(E),a_q(E), while the two minus signs in the mixed
term give the actual Kummer image of S D_ell D_q y_m.
Restriction is injective because E(H_m)[p]=0. The quotient by the
top ideal has a filtration with invariant-free E[p^k] factors, so
the top-ideal H¹ map is injective as claimed. This verifies (22)
at the full R coefficient, not only after rational projection.

## 6. First and mixed lifting equations, and the old local cup map

For a rational g, the full induced matrix is the matrix in (20)
followed by diag(1,epsilon_K(g)). Thus its first coefficients
act from the plus component to the twist, and the mixed coefficient
acts back to plus. Expanding the cocycle equation gives exactly
(25), with the twist action in each cup product. In particular
$$d(a_\ell a_q)=-(a_\ell\cup a_q+a_q\cup a_\ell).$$
The Leibniz rule and the two first equations make the final right
side closed. Altering the first nullhomotopies changes it by the
specified cups; the mixed coefficient is not thereby a cocycle
or an identified Heegner class.

At an old prime i, R epsilon_K has no unramified H¹, since its
Frobenius is−1. The class a_i is primitive tame, with value−1
on the chosen generator. Local duality identifies H²(T/p^k
tensor epsilon_K) with the dual of the minus Frobenius line
of E[p^k]. The Weil pairing identifies the old finite plus
Kummer line with the unramified line dual to that tame class.
Their perfect Tate pairing therefore proves the isomorphism(25a)
over all R. The other a_j is unramified and hence zero locally.
This verifies the stated d_0 times old-local-coordinate obstruction.
Its sign is fixed by choosing the old generators through this map,
not by dropping an uncomputed tame scalar.

Quadratic unramified restriction multiplies the invariant pairing
by2 and also sends the finite Frobenius value to twice its plus
value. It leaves inertia unchanged. The local factor2 and the
absence of an inertia factor2 are consequently consistent.
The cofactor construction cancels those local obstructions for
its corrected class; it does not prove the original augmentation
class lifts globally or satisfies all other Shapiro local conditions.

## 7. Primary comparison scope

BKS1910.07404v2 Hypothesis2.2 explicitly assumes positive
Mordell–Weil rank and finite primary Sha. Its determinant comparison
uses r_alg−1 and its Definition2.4 uses the actual leading term.
These hypotheses cannot be replaced with Selmer corank or a
vanished third complex derivative. The proof does not do so.

I also checked the published Longo–Vigni paper, DOI
10.1007/s40687-026-00646-7, Theorem B and Theorem9.2. Its conditional
rank-one TNC and odd≥3/even≥2 higher-rank bounds do not supply
the missing rank-five comparison. The normalized cyclotomic
c_3z_D,0 and the finite mixed obstruction remain distinct actual
residuals. Neither is forced to zero by the extra untwisted
complex vanishing.

Only this review was written. No numerical certificate or prime
scan was rerun. All requested repairs are included in the reviewed
revision. Subsequent PASS links and checkpoint status changes are editorial.
