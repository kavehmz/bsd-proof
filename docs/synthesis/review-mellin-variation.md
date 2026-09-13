# Independent review of the Mellin variation construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review. The parent objective remains full BSD over Q.

**PASS after three scope clarifications.** Reviewed all eight sections of
[mellin-variation-attack.md](mellin-variation-attack.md) and its checkpoint.
Reviewed proof SHA256:
14e70782bb5ccaca0945f096e89e3bb53d8430baa1db757f914cdf395374ba69.
Subsequent review links and checkpoint/status changes are editorial.
No old certificates were rerun, and no author proof file was edited here.

The review validates the exact analytic construction and the stated
failures of its two proposed arithmetic repairs. It does not validate a
rational/integral realization of the spectral class, cancellation of its
L(f,2) factor in an integral lattice, or a proof of BSD.

## 1. Eisenstein normalization and both cusps

The oldform identity is correct. Separating primitive pairs according
to divisibility of the second coordinate by N gives
$$E(Nz,s)=N^sE_\infty(z,s)+N^{-s}(E(z,s)-E_\infty(z,s)).$$
Solving it gives the displayed E-infinity formula; level-one inversion
gives E-zero. At infinity the incoming coefficient is one, and the
outgoing coefficients are
$$\psi(s)\frac{N-1}{N^{2s}-1},\qquad
\psi(s)\frac{N^s-N^{1-s}}{N^{2s}-1}.$$
Both residues at one are $3/[\pi(N+1)]$.
The scaled cusp-zero coordinate has width one, as required.

The Laurent boundary terms follow by expanding $y^{1+t}$ and
$y^{-t}$. In particular the $-R(\log y)^3/6$ term of A2 and its
incoming $y(\log y)^2/2$ are correct. Constants c,d,e are explicitly
defined coefficients of the scattering functions, not arbitrary
normalization choices.

I checked the source normalization in Petridis, Duke103(2000),
[author PDF, printedpp113–118](https://www.homepages.ucl.ac.uk/~ucahipe/variationpublished.pdf).
The note's own positive-cosine Fourier expansion has the correct
factor four. This is checked by summing both Fourier signs and then
setting s=1; its finite part agrees with the eta product. The source's
scattering matrix and the note's independent Fourier normalization
must not be conflated with an unexamined printed Fourier prefactor.

## 2. Unfolding, the bad factor, and the central coefficient

Unfolding gives a strip integral of $y^sf\bar g$; hence the Mellin
factor is $\Gamma(s+1)/(4\pi)^{s+1}$. The constant term of g and
unequal Fourier indices disappear upon x-integration.

The good-prime calculation is exact:
$$
\frac{pA_p(pX)-A_p(X)}{p-1}
=\frac{1-p^2X^2}
 {(1-a_pX+pX^2)(1-a_ppX+p^3X^2)}.
$$
At389 the required series is $(1-N^{-w})^{-1}$, whereas the quotient
$L(f,w)L(f,w-1)/\zeta(2w-2)$ has the extra multiplier
$1+N^{1-w}$. Thus the division by $1+N^{-s}$ in the final identity
is necessary and correct.

At s=1 the scalar is
$$
-\frac{24}{(4\pi)^2\zeta(2)(1+N^{-1})}
=-\frac{9N}{\pi^4(N+1)}.
$$
Since $L(f,1+t)=\ell t^2+O(t^3)$, coefficient extraction gives
exactly that scalar times $\ell L(f,2)$, with no missing two.
A2 is the Laurent coefficient, not an unhalved second derivative.
The preceding three integrals vanish because the right side starts
at order two. Euler-product convergence at2, and positivity of its
real local factors, prove the asserted nonzero L(f,2).

Cusp decay of f and moderate growth of g and the Eisenstein coefficients
justify integration of the finitely many Laurent coefficients.
The previously certified correction in $\ell=4\pi(J''-\mathcal C_E)$
is retained; no eta correction was dropped or recomputed.

## 3. Relative form, orbifold normalization and spectral chain

The two-form factor is correct:
$$
\alpha\wedge\overline{d\log v}
=-8\pi^2 i\,f\bar g\,dx\wedge dy.
$$
Thus multiplying by $i/(8\pi^2)$ gives $F\,d\mu$.
Exponential decay times the explicit polynomial/logarithmic cusp terms
is flat in r=1/y at each boundary circle.

The author incorporated the required orbifold clarification. Level389
has elliptic stabilizers; smooth invariant functions need not descend
smoothly in a coarse branched coordinate. The form is now explicitly
a smooth relative orbifold form. Alternatively its pullback to the
torsion-free effective Gamma1(389) cover is smooth. The effective
cover degree is388/2=194, and the integral is divided by194.
No automatic integral descent at the primes dividing this cover degree
is asserted. Rational top cohomology remains the orientation line Q.

The spectral recurrence is correct:
$$\Delta A_0=-R,\quad\Delta A_1=-A_0-R,\quad
\Delta A_2=-A_1-A_0.$$
It gives $\Delta^2A_2=A_0+2R$, $\Delta^3A_2=-R$ and $\Delta^4A_2=0$.
The element $R+tA_0+t^2A_1+t^3A_2$ is indeed killed by
$\Delta+t+t^2$ modulo t4. The specified nonzero boundary cycle is
retained; the homotopy fiber is not silently taken over zero.

The second clarification is also applied: the universal H1 local
system uses the full stack group Gamma0(N), on which -I acts by -1.
Only even symmetric powers descend effectively. Complete reducibility
of finite algebraic SL2 representations makes their Casimir semisimple;
it rules out the stated Laplacian-intertwining homogeneous tensor
realization of this nonsemisimple chain. Its scope does not exclude
mixed variations or new secondary regulator constructions.

## 4. Exact finite parts and Fricke symmetry

Expansion of the gamma/zeta quotient gives
$$b_0=\frac6\pi
 \left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right).$$
The eta product yields the finite part
$b_0-\frac3\pi\log(y|\eta|^4)$.
Inserting z and Nz and differentiating the denominator $N^s+1$
recovers both K_N and the coefficient $-12/[\pi(N+1)]$ of U.

For the odd part,
$$
-\frac3\pi\log N+\frac{12}\pi(\log|\eta(z)|-\log|\eta(Nz)|)
=\frac{\log|v|}{2\pi}.
$$
Thus the factor $1/(N-1)$ in E-minus is correct, including N^-6
in v. Fricke negates both f and g, so F is even. Its pairing with
the entire odd Eisenstein family and its convergent coefficients
vanishes. The vertical divisor is taken from the already reviewed
Du–Yang comparison; it is not suppressed in any arithmetic lift.

## 5. Milnor transfer and its boundaries

Both rational moving functions approach1 at O: $1/(x-4)$ and
$y/(x-4)^2$ vanish there. The cusp images under the normalized
parametrization are both O. Therefore the divisor of Norm(v) is zero,
making it a rational constant. The Fricke relation sends this constant
to its inverse, proving it is±1.

The Milnor projection formula then gives
$$\operatorname{Cor}\{v,\pi^*h_j\}=\{\operatorname{Norm}v,h_j\},$$
and twice this symbol is zero by bilinearity. The needed norm in
degree one and compatibility with all tame residues are exactly
[Elman–Karpenko–Merkurjev, Fact100.8(2)–(4)](https://sites.ualberta.ca/~karpenko/publ/Kniga.pdf).
At a noncuspidal divisor point the tame symbol is the stated power
of v; at cusps it is one. Transfer therefore does not hide a surviving
rational boundary. No arithmetic-surface unramified K2 class is assumed.

## 6. Integral character and exact scope of the response vanishing

For this rectangular real period lattice, the real part of any
elliptic period is an integer multiple of omega1. Consequently k is
integral, additive and trivial on parabolics. Its values on finite
elliptic stabilizers are automatically zero as well.
Multiplication by $(1+T)^k$ in the basis1,T,T2 has matrix
$$
\begin{pmatrix}
1&0&0\\ k&1&0\\ \binom{k}{2}&k&1
\end{pmatrix},
$$
including for negative k. This is an actual integral rank-three local
system. The author removed ambiguous finite-monodromy wording;
a unipotent representation of this kind can have infinite image.

The inverse character in the Eisenstein sum gives the stated
transformation law by changing right cosets. The parameter
$T=e^{2\pi i\epsilon}-1$ matches the unitary family. Direct conjugation
with the positive Laplacian gives the coefficient -4pi i in its
first derivative.

Petridis equations(4.3)–(4.6) use a purely imaginary Fourier direction
for the non-reflection-zero response. The note's
$2\pi i c_\pi f/\omega_1$ has exactly that form. The resulting
diagonal response has factors L(f,1)L(f,2s), and equations(4.9)–(4.12)
provide its oldform/cusp combinations. Hence the precisely defined
B_ab(s) and its common-spectral derivatives vanish. The source's
subsequent assumptions about scattering poles or zeta zeros are not
needed for this meromorphic integral identity.

There is a useful scope distinction: before setting the external
spectral parameter sigma equal to the internal parameter u, the
Dirichlet factors are L(f,sigma+u)L(f,sigma+1-u). Thus asymmetric
spectral differentiation is outside the diagonal vanishing test and
can retain a central second derivative. This is not a contradiction
to the note and supplies no new arithmetic realization by itself.
The review does not identify B_ab with a full scattering derivative
without its boundary correction, or declare the full character jet
or second character variation zero.

## 7. The arithmetic comparison is still open

I checked [KLZ arXiv1501.03289v2](https://arxiv.org/html/1501.03289v2),
§3.5, Definition5.3.1 and Theorem6.2.9. The input eigenspaces are
cuspidal. The motivic class has rational symmetric-power coefficients,
and the displayed regulator formula concerns L'(f,g,j+1) for
0<=j<=min(k,k'). It does not identify the present second spectral
jet with the point height determinant, nor make L(f,2) an integral unit.

The final MV-389 gap correctly retains the extra regulator factor,
the scalar -9N/[pi4(N+1)], both cusp jets, the Hodge/vertical data,
the full real-period index two, and the chosen orbifold-cover
normalization. The analytic equality does not establish rationality
of its coordinate in the required arithmetic frame.

The three requested geometric/local-system clarifications are saved,
all displayed constants and the bounded response assertions pass,
and no further correction is outstanding.

