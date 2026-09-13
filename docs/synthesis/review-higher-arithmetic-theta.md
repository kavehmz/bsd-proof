# Independent review of the higher arithmetic theta construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file.

**PASS after the recorded current-class precision.** All six sections
of the [proof](higher-arithmetic-theta-attack.md) were inspected;
the [checkpoint](higher-arithmetic-theta-checkpoint.md) was read.
The result concerns the two specified arithmetic constructions and
their exact projections. It does not supply HAT-389 or full BSD.

Reviewed proof SHA256:
894f745a6ced0eb67bf926adf6f0ef319d311dc984beb7563680f52b68c9d7be.
Reviewed checkpoint SHA256:
8919d0ac770733af0625975cc63e0752b5b9fd9fc44cd35bb2719908c95c4098.
Subsequent review links and completed-status updates are editorial.

## 1. The actual genus-two arithmetic cycle

I read the primary
[SSY 45-page author revision](https://home.cc.umanitoba.ca/~sankaras/ArithSW-rev1.pdf),
especially Definitions2.1,2.5,2.11–2.13, Theorem2.14,
Remark2.7, Corollary4.16 and equations223–236.
It is distinguished from the 43-page arXivv1.
The assumptions N>3 odd squarefree hold for389.

The stated moduli problem retains the condition
alpha_i phi^{-1} in Hom(E',E). The moment matrix is NT,
with the half-bilinear pairing used by the source.
This checks against the quadratic lattice N det with
upper-right entry b/N. The positive definite cycles
have the stated finite-fiber support; they are not
unconditionally nonempty for every T.

The rank-one face is a genuine Fourier-coefficient operation:
zero frequencies in the first diagonal and off-diagonal
real variables leave diag(0,t). For diagonal V its
v_0=t^{-1}tr(TV) is v_2, so det(V)/v_0=v_1.
Definition2.11 therefore gives exactly (2.2), including
the MINUS log(v_1) current. The negative-square
modification has both cusps and the displayed beta_3/2
factor. Definition2.12 gives (2.3), so the zero coefficient
also remains affine in log(v_1).

No informal replacement of stack degree is used.
The effective hyperbolic area is pi(N+1)/3.
Dividing by2pi for Omega and by2 for the central
stabilizer gives stack integral (N+1)/12.
The archimedean factor1/2 in arithmetic degree gives
(N+1)/24, exactly C_N in the theorem. Exceptional
automorphisms in individual special cycles are handled
by the source's stack degree, not counted as extra
generic factors. All arithmetic Chow assertions here
are in the real/rational coefficient setting of that
source; they do not assert disappearance of integral
stack stabilizer torsion.

## 2. Exact conversion to the Du–Yang response

Equation226 of the inspected source is precisely the
normalization A_N(s) in (3.1). It identifies the scalar
mu_0 component, with the genus-one inducing parameter
s-1/2. The source's genus-two classical conversion
is det(V)^{-3/4}, independent of the inducing parameter.
Thus differentiating does not introduce an extra
log(det V) from that conversion. The factor2 in
Corollary4.16 is retained.

Independent differentiation gives
$$
 A_N(1)=-\frac{N^2-1}{24},\qquad
 \frac{A_N'(1)}{A_N(1)}
  =1+2\frac{\xi'(2)}{\xi(2)}
       +\left(\frac2{N^2-1}+\frac32\right)\log N.
$$
The remaining logarithmic coefficient is
$$
 \left(\frac{N-1}{N+1}
           -\frac4{N^2-1}-3\right)\log N
       =-\frac{2N}{N-1}\log N .
$$
Multiplication by C_N/A_N(1)=-1/(N-1) gives
exactly (3.2). In particular there is no additional
factor2 to insert when comparing the two conventions:
the primary analytic equality already fixes it.

Subtracting that formula gives every term and sign
in (3.4). The fixed auxiliary v_1 is independent of
the genus-one Laplacian variable. From the previously
reviewed eigenvalue -s(s-1)/4, the third Laplacian of
the residual is -E_t^(0)/64. The rank-one genus-two
response is killed by its second Laplacian.

The explicit vector of norm1 in the proof supplies
a point of Z(1)(C) by SSYLemma2.4. Equation235 gives
E_DY,1(1)=phi(N)deg(Z(1))q/2, which is nonzero.
This establishes an actual differing Fourier term.
The argument excludes only the specified rank-one
projection, not every projection of a genus-two cycle
or every motive with the required integrated value.

## 3. The finite unit and higher Chow construction

The proper elliptic family over the fine open curve
has omega^{12} trivialized by the nonvanishing
discriminant. Since sigma and zero are disjoint,
$$
 0^*\mathcal O(\sigma-0)=\omega .
$$
Consequently the displayed omega^{-1} twist rigidifies
the degree-zero line. Its relative Picard point has
order5, and rigidified Picard representability makes
its fifth power trivial, with no residual base line.
Taking the twelfth power gives an actual trivialization
of O(60(sigma-0)). This justifies the specified function
and excludes a hidden base divisor.

The norm calculation uses pushforward of divisors,
so [6]_*[sigma]=[sigma] and [6]_*[0]=[0], each with
coefficient1. On a base unit, by contrast, the norm
has exponent36. These two actions give
(T-36)(T-1)u_sigma=0. The polynomial
(36-T)/35 is therefore exactly the projector needed
on this actual element. Its residue is sigma-zero,
and it kills the difference between any two choices
of the function. This proves Lemma4.1 without assuming
a conjectural norm-compatible element.

Each i_j is the restriction of a closed smooth
elliptic subfamily of relative codimension2 in A.
Its intersection with W is U, so the immersion is
closed and regular in W. Gysin shifts
H_M^1(U,Q(1)) to H_M^5(W,Q(3))=CH^3(W,1)_Q.
The three graph divisors telescope as in(4.5).
That nonzero residue proves Xi is nonzero. Multiplying
by2100 clears the stated rational coefficients on
this open space over the chosen number field.
It does not prove an integral arithmetic extension.

The trace computation is also geometric: restricting
the i_j support to [6]^{-1}W restricts its varying
elliptic coordinate to [6]^{-1}U. Then [6]i_j=i_j[6]
because the other coordinates are fixed5-torsion.
Thus the trace on the graph cycle is the elliptic
trace, not multiplication by6^6. Proper pushforward
and restriction give exactly the asserted eigenvalue1.

## 4. Canonical regulator, Tate degree and source scope

I read
[Kings–Rössler1412.2925v2](https://arxiv.org/pdf/1412.2925v2),
17December2014,27pages, Corollary2.2.2, Theorem4.1.1,
Proposition4.2.4 and Lemmas4.2.7–4.2.9.
The residue isomorphism for trace eigenvalue1 identifies
the already constructed Xi with pol_a. Applying the
source's individual-torsion formula with sigma=-a gives
$$
 -2\,\operatorname{cyc}_{\rm an}(\Xi)
       =(T_{-a}^*\mathfrak g_{A^\vee}
                               -\mathfrak g_{A^\vee})|_W .
$$
The minus2 and the minus a are therefore both correct.
The independent elliptic calculation in sourceLemma4.2.9
also fixes this factor through cyc(u)=log|u|.
Gysin functoriality and the motivic product lemma
identify the three pushed regulator terms; no
unnormalized product of logarithms replaces them.

The author applied the requested precision:
g_A is expressly a renaming of the source's
g_{A^vee}, a current ON A, and current classes are
taken modulo im(partial)+im(bar partial). For
relative dimension3 the current has type(2,2)
and lives in degree5 analytic Deligne cohomology
with R(3). Codimension-two Gysin retains the two
additional Tate twists. The real structure is the
one from the conjugation-stable embeddings in the
source; it is not an untwisted real scalar class.

The base is a smooth number-field scheme and A is
an abelian scheme there, so the theorem applies.
The proof does not extend it through generalized
elliptic cusp fibers. It also does not identify
this number-field class with a rational BSD frame
by an unproved descent.

## 5. Both scalar projections

Restriction to U^3 removes every one of the three
graph supports. Thus Xi|_(U^3)=0 already in the
higher Chow group. Any all-nonzero7-torsion section
factors through this open because5 and7 are coprime.
Its pullback is therefore zero. This is consistent
with the original class's nonzero boundary.

The line P=O(0) tensor pi^*omega is rigidified and
symmetric. For a torsion section t, the cubical
identity [D]^*P=P^{D^2} makes t^*P torsion.
On U, O(0) is trivialized by its canonical section,
so P|_U=pi^*omega. Hence each i_j^*L has zero
rational first Chern class. The projection formula
gives Xi cup c_1(L)=0 in H_M^7(W,Q(4)).
There is no use of a nonexistent proper push from W.

The revised proof now checks the analytic integral
directly on the compact fiber, using the canonical
GLOBAL current difference. Against its closed
translation-invariant curvature lambda,
$$
 \int_{A_s}(T_{-a}^*g_A-g_A)\wedge\lambda
       =\int_{A_s}g_A\wedge(T_a^*\lambda-\lambda)=0.
$$
This is well-defined on global current classes:
partial- and bar-partial-exact changes pair to zero
by compact Stokes. It does not extend an arbitrary
equality known only on W. The elliptic pushed-current
calculation is a compatible representative and gives
the same zero average, with integrable logarithmic
singularities. Thus the conclusion about this fixed
canonical projection is justified.

## 6. Verdict and source files

No numerical coefficient needed correction. The only
requested change was the explicit global-current
argument and notation precision, now applied.
The exact remaining gap HAT-389 is preserved.
In particular, neither tested projection gives the
nonzero original f-weighted mass, and there is no
claimed rational or integral BSD comparison.

Primary PDF hashes inspected:

- SSY45-page author revision:
  59c0b417227cbf4858cfc3405fbcf51641019c692a670731492757c44c019053,
  /tmp/higher-theta-ssy.pdf.
- Kings–Rösslerv2:
  6eb0c6ab7208e5630f79f3b35b0b0b998ed8b71ffb371a90c83ba23d0c152893,
  /tmp/higher-theta-kings-rossler.pdf.

Native Poppler text extraction was used for the exact
formulas and primary HTML/PDF reads for source scope.
No old numerical certificate was rerun. Only this
assigned review file was written during the review.
