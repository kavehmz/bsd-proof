# Independent review of the exponential spectral kernel

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only this review for the assigned audit. No old numerical
certificate or arithmetic script was rerun.

**PASS for all seven sections of
[the construction](exponential-spectral-attack.md).**
The rational relative complex, Betti comparison and exact analytic
completion are valid in their stated scope. No substantive formula
correction was needed. The author added the requested chart precision:
the explicit b=1 and positive-ray cycles are written for Z>0;
the rational connection exists over Z≠0 and other cycle charts are
obtained by continuation.

Reviewed final proof SHA256:
452482f39ce66d17347c40d0fedc9ef6bf0fe048fa47ab3a35de2642a920db5f.
This is the initial supplied mathematical proof
aeebd8b51481308e097ea8fbaa9a3ab52f22f462741678281dabadadf34fe37e
with that inspected chart clarification. Later review links and
completed-checkpoint changes are editorial.

## 1. The actual algebraic complex and its free rank

Put A=Q(Z)[t]/t³. The operator on the proposed source vR is
$$D_v f=f'-f+t\left(\frac1v+\frac1{v+Z}\right)f.$$
It lands in R dv because f vanishes at zero. The de Rham source
and target are explicitly defined, rather than inferred from a
dimension statement for an absolute punctured curve.

For f=v/(v+Z)^k, expansion in u=v+Z gives highest derivative
pole Z(k−t)u^(−k−1). This coefficient is a unit of A; k≥1 and
Z is invertible. For f=v^m, m≥1, the highest polynomial term
is −v^m, with lower polynomial degree and at most a simple pole
in all other terms. These reductions prove spanning by dv and
dv/(v+Z). Conversely any primitive with a highest pole has an
unavoidable pole of one larger order; a nonzero polynomial
primitive vanishing at zero has an unavoidable highest polynomial
term. This proves independence and kernel zero even over the
nonreduced coefficient algebra. Therefore H¹ is FREE of rank two
over A, and rational dimension six.

The notation t³=0 is a matrix-package convention for a rank-three
connection over a reduced rational parameter base. The total
one-form −dv+t dlog(v(v+Z)/Z) is closed and its coefficients
commute, so flatness in v,Z is genuine.

## 2. Moderate zero and rapid infinity are different boundaries

In the relative frame e'=ve, the residue at zero is 1+t.
The dual multiplier is vh(v,Z), with h=e^(−v)q_*^t. It behaves
as v times a polynomial of degree at most two in log v. This
does not have rapid decay to every order.

The relative source vR nevertheless makes every Stokes endpoint
term zero: hf=O(v log²v) at zero. Forms in R dv are integrable,
and the integral on a radius-ε boundary circle is
O(ε log²ε). At infinity in a closed right-half-plane sector,
the exponential dominates all allowed rational growth and
logarithmic factors. The second end is genuinely rapid.

I checked [Bloch–Esnault, math/0005137v1](https://arxiv.org/pdf/math/0005137),
Theorem0.1 and Example0.2(i)–(ii). Their regular-singular discussion
and gamma example explicitly allow no nonzero rapidly decreasing
coefficient at the regular end. Their scalar example also is not
itself a theorem about the present nilpotent specialization. The
author correctly supplies a separate relative boundary and direct
integration proof, instead of invoking the absolute theorem to
justify the positive open chain.

## 3. Rational Betti structure and all six loaded cycles

With ε_j coefficient extraction, the factors
λ_j=(2πi)^(−j)ε_j are essential. Expanding the actual logarithm
monodromy gives
$$\lambda_j e^{2\pi it}
=\sum_{r=0}^j\lambda_{j-r}/r!.$$
Thus the Betti monodromy matrix is rational and the lattice on
λ₀,λ₁,2λ₂ is integral. The primal comparison vectors are
(2πi)^j t^j with inverse monodromy. This is consistent with the
second toric logarithm variation and its Tate graded pieces in
[Huber–Kings,1505.04574v1, §§4.3,4.6 and Lemma6.4.1](https://arxiv.org/pdf/1505.04574v1);
coordinate inversion accounts for the chosen horizontal sign.
The Betti nilpotent coordinate is not identified unchanged with t.

Topologically the blown-up surface retracts onto the zero boundary
circle, the path from it to the interior vertex, a loop around −Z,
and a path to the contractible rapid end. Quotienting the entire
zero circle and rapid-end point leaves the relative complex
V_B³→V_B with boundary a−b+(M−1)c. There is no missing zero-loop
cycle in this relative model and no permitted nonrapid open end
at −Z. Its differential is surjective and its kernel has the six
stated generators. The correction
−p₀((M−1)λ_j) in Λ_j cancels its interior boundary.

The endpoint estimates make pairing invariant under this relative
quotient and Stokes. For forms t^kω_i, pairings with load λ_j
vanish for j<k. The j=k block is exactly
$$\frac1{(2\pi i)^j}
\begin{pmatrix}1&e^ZE_1(Z)\\0&2\pi i e^Z\end{pmatrix}.$$
The lower-right entry is the residue at −Z; the lower-left is
zero because e^(−v)dv is entire. Multiplying the three block
determinants gives (2πi)^(−3)e^(3Z), up to ordering sign.
Hence the pairing is perfect, independently of an unproved general
relative comparison theorem.

That determinant is for the stated rational λ-bases. Replacing
λ₂ by 2λ₂ in both j=2 cycles multiplies it by four. The note
does not confuse this different integral lattice with the rational
frame or infer a BSD integrality statement.

## 4. Gauss–Manin and the exact Bessel integral

The dZ coefficient t((v+Z)⁻¹−Z⁻¹) preserves the relative source.
I independently computed
$$D_v\!\left(\frac v{v+Z}\right)
=-1+\frac{Z+2t}{v+Z}+\frac{Z(1-t)}{(v+Z)^2}.$$
Reduction of the second form's Z-derivative therefore gives
$$\frac d{dZ}\begin{pmatrix}I\\J_t\end{pmatrix}
=\begin{pmatrix}-t/Z&t\\-1/Z&1+t/Z\end{pmatrix}
\begin{pmatrix}I\\J_t\end{pmatrix}.$$
Differentiating its first row and substituting its second gives
I''−I'−t(t+1)I/Z²=0 without cancellation of t.

The integral normalization can be rederived directly from
[DLMF10.32.8](https://dlmf.nist.gov/10.32.E8).
Set ν=1/2+t, z=Z/2 and u=1+2v/Z in its integral on [1,∞).
The prefactors reduce exactly to
$$K_{1/2+t}(Z/2)
=\sqrt{\pi/Z}\,e^{-Z/2}\,
\frac{I(t,Z)}{\Gamma(1+t)}.$$
Since K_{1/2}(Z/2)=sqrt(π/Z)e^(−Z/2), no additional power
of Z,2 or π is missing.

For the coefficients of the normalized ratio, integration by parts
gives A(Z)=e^ZE₁(Z) at first order. The second coefficient
B(Z)=∫_Z^∞A(u)du/u satisfies B''−B'=(1+A)/Z² and tends
to zero at infinity. The differential equation and that boundary
condition establish the claimed second coefficient, with the
Taylor factorial already included. This checks the earlier Bessel
input directly; no asymptotic series was differentiated.

## 5. Finite gamma normalization is legitimate here

For q_*=v the same polynomial reduction gives rank one over
Q[t]/t³. Its three positive periods, after the stated Tate
adjustments, give G(t)=Γ(1+t)=1+g₁t+g₂t². The constant
coefficient is exactly ∫₀∞e^(−v)dv=1.

The reciprocal modulo t³ is consequently the POLYNOMIAL
1−g₁t+(g₁²−g₂)t². Each term in I/G is a sum of products
of the explicit framed periods. Product integrals are absolutely
convergent, including their logarithmic endpoints, so the stated
tensor/product-cycle and Fubini operations apply. The coefficient
of order j is first recovered with its (2πi)^j Tate factor;
this calculation does not equate Betti and de Rham t-coordinates.
It neither inverts an arbitrary nonrational period nor constructs
the entire untruncated inverse gamma function in a finite object.

## 6. Completed Fourier factors, both cusps and the pole

Starting with the inspected level-one factor
2sqrt(y)n^(s−1/2)K_(s−1/2)(2πny)/ξ(2s), its half-order
specialization is n^(s−1)e^(−2πny)/ξ(2s). Applying the two
oldform identities gives numerators
$$N1_{N\mid n}\sigma_{1-2s}(n/N)-\sigma_{1-2s}(n),$$
and
$$N^s\sigma_{1-2s}(n)-N^{1-s}1_{N\mid n}\sigma_{1-2s}(n/N).$$
Thus multiplication by Γ(s)ξ(2s)(N^(2s)−1), followed by the
exact Bessel integral above, gives precisely (6.3) and (6.4).
The positive Fourier sign has no missing factor two. For n=1
the modes are −qI and Nq exp(t log N)I respectively.

The zero modes also check directly from the oldform scattering
functions. They are the two expressions in (6.5). Since ξ(u)
has residue one at u=1, ξ(2s−1) has residue1/2 at s=1.
The common completed residue is consequently (N−1)/2.

Multiplication of R/t+A₀+tA₁+t²A₂+⋯ by a holomorphic
completion contributes c₃R to its t² coefficient. This term is
correctly retained before pairing. Only after using the established
vanishing of ∫F,∫FA₀,∫FA₁ can the paired jet be replaced
by c₀ times the old A₂ mass.

At s=1 both completions have c₀=π(N²−1)/6. Multiplication
by the previously reviewed mass gives
$$\frac{\pi(N^2-1)}6
\frac{-9N}{\pi^4(N+1)}
=-\frac{3N(N-1)}{2\pi^3}.$$
For N=389 the numerator is226398. The surviving factor
ell_E L(f,2), the eta correction inside ell_E, and the full
period/Tamagawa conventions are unchanged. No division by L(f,2)
is supplied by this completion.

## 7. What this PASS does and does not establish

The inspected proof constructs the rational irregular kernel
family, its explicit relative period comparison, the finite gamma
jet operations and exact analytic Eisenstein normalization.

It explicitly distinguishes the following outstanding steps:
the substitution Z=4πny=−2n log|q| is not an algebraic map
from the modular curve; finite Fourier kernels are not a single
finite object realizing their infinite modular sum; the zero-mode
constants have not received an arithmetic realization; and a
classical rational period–height determinant comparison has not
been built. Neither the Bloch–Esnault result nor an unread
Fresán–Jossen theorem is used to assume those steps.

The checkpoint's initial-candidate and pending-review language
can now be replaced by completed/PASS status. No further
mathematical correction is required for the stated construction.
