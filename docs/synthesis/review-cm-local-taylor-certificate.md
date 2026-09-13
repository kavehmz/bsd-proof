# Independent audit of the new CM local Taylor certificate

Date:2026-09-13. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. **PASS for section6 and its NEW exact certificate.**
The separate sharper P-or-Q consequence below is also verified.
No mathematical correction is required.

Scope: NEW section6 of cm-local-point-comparison-attack.md,
proof revision2b2210930ef8ee5419055ec5b83965551b09d72f0c0a485ffdcf1de7f4e14f25.
Core §§1–5 have separate PASS in
[review-cm-local-point-comparison.md](review-cm-local-point-comparison.md),
SHA256f2242d2b6b8655c6eb67180719163a47bd77836b810882f23befb029f7ca69e0.
Root owns the proof, script and certificate; this audit did not edit them.

New script: compute/scripts/cm_local_taylor_mod5.py,
SHA2560fffae4120bc9a2632bc174444832fea0bb3f91450bdc984e594d2ee0e336586.
New certificate: compute/data/cm_local_taylor_mod5.json,
SHA256900a9060c40de02e5d541276d358938a7929b6538f4fef23db31f6954462c307.

The independent new reproduction completed with exit0. It used the
different primitive point i*B, a different ideal normal form, direct
Legendre counts with deterministic Frobenius witnesses, and a Hasse/
invariant-Taylor expansion instead of the author's A+yB recurrence.
It verified all12 generators, image/orbit4608, Frobenius order24,
the exact Gaussian scaling of all four sums and the pattern F,T,T,F.
Independent Fraction arithmetic gave parameter valuations1,1,2 and
normalized residues4,1,4 for64P,64Q,64(P+Q).

Root preserved the independent artifacts BYTE FOR BYTE:

- [Independent verifier](../../compute/scripts/verify_cm_local_taylor_mod5.py),
  SHA25672c397c20fcb27e250b282d950305fc36493a4ef1b8231be276adec0eb788027.
- [Independent exact output](../../compute/data/cm_local_taylor_mod5_independent.json),
  SHA256a9c2cc60c05adeee2f06d17c33a16435c0b6c5f5b9ab8bdbf7621e050e7c31ae.

This proves a unit LOCAL Taylor coefficient C2, not a value or unit
claim for the old cyclotomic c2. The additivity defect has logarithm
valuation2 and integral local-lattice valuation1. At least one of the
two P,Q local classes is nonzero modulo25 in that lattice. Full BSD
and the global arithmetic comparison remain open.

## 1. Reproduction and the precise dependency

The original new script and output retained exactly their stated hashes.
The independent run was

    DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python /tmp/cm_local_taylor_independent.py

It exited0 and wrote /tmp/cm_local_taylor_independent.json.
The two durable copies linked above preserve those bytes. The verifier's
workspace ROOT and temporary output destination are intentionally unchanged;
it does not overwrite the author's certificate. No old analytic, rank,
height, cyclotomic-derivative certificate or prime scan was rerun.

The inference from the finite sums uses the separately reviewed core
theorem: all C_d belong to Z5, and C_d-C_(1,d) belongs to5W uniformly in d.
It also uses the original matched Tate period Omega_j, its Frobenius
law, the single rho factor in the complete semilocal trace, and the
integral identification Log_omega:H1(Q5,T_pi)→5Z5. Those statements
have their own PASS; the finite computation alone would not prove them.
The [asymmetric-ray review](review-cm-asymmetric-ray.md) supplies the
actual ray fields and character conventions used here.

I checked the CM character convention against the previously inspected
primary [Kato2004, §15.8](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
Its cohomological character is dual to the action on point Tate modules.
Thus the actual Gaussian point Frobenius Psi has the original coefficient
rho=(Psi^c)^(-1), as used in the script. No extra inverse, second rho
factor, or normalized trace is inserted.

## 2. The Gaussian modulus and the actual Frobenius subgroup

The exact arithmetic is

    f0=39(1+i)^3=-78+78i,
    pi=-1+2i, barpi=-1-2i,
    mu=f0 barpi=234+78i=78(3+i), Norm(mu)=60840.

At the selected prime above5, i=3, so pi has residue0, alpha=barpi
has residue3, and mu has residue3. Consequently the mu-isogeny is
étale at that prime even though its integer degree is divisible by5.

The distinct Gaussian prime divisors are exactly those listed in the
proof:1+i,3,3+2i,3-2i,barpi. The first occurs with exponent3.
The quotient unit-group order is

    60840(1-1/2)(1-1/9)(1-1/13)^2(1-1/5)=18432.

The conductor admits no nontrivial Gaussian unit congruent to1, and
Q(i) has class number one. The actual ray degree is therefore
18432/4=4608, consistently with the reviewed B1/K construction.

I independently counted the reductions at all twelve listed primes
by the Legendre-character sum over the prime field, without calling
the author's point-counting routine. The traces are

    -8,-4,-12,-10,4,-10,-16,10,-8,-20,-20,16

in the displayed prime order. At each prime the possible CM Frobenius
elements have coefficients a=trace/2 and b²=ell-a². The independent
verifier used a deterministic quadratic field and deterministic
point enumeration to distinguish a+bi from a-bi by coordinate
Frobenius. It checks [2b]P!=0 before using the witness, so the
difference [2bi] cannot kill it. All twelve selected Gaussian
generators, prime embeddings and rho weights agree with the certificate.
Their tangent values a+b i_modell are zero modulo ell, also consistently
selecting the degree-ell Frobenius endomorphism.

This tests ACTUAL Frobenius elements, not arbitrary Gaussian elements
of norm ell. The CM action places their images in the actual torsion
Galois image, which is bounded above by the ray degree4608.
The independently generated subgroup has order4608, hence is the
full image.

For an independent reduction algorithm, write a=a0+78a1 and
b=b0+78b1 with0<=a0,b0<78. In O/(3+i), i=-3 and the remaining
coordinate is a1-3b1 modulo10. Thus the verifier uses

    red(a,b)=(a0+78((a1-3b1) mod10), b0).

This differs from the author's parallelogram/floor normal form.
Closure in this quotient and every generated character relation were
checked. The image intersects {1,-1,i,-i} only in1, so the four
Gaussian units give all four cosets of H in the full unit group.

## 3. The original rho weighting and full orbit

For an actual Gaussian Frobenius a+bi, the weight at the specified
5-adic embedding is

    rho=(a-3b)^(-1) mod5.

This is well-defined on O/(mu), because conjugating mu makes it
divisible by the selected pi. The generated relations preserve
these weights. In particular pi itself is in H with rho(pi)=2,
and the independently computed order of pi in H is24.
The sum is over all4608 elements, not one local Frobenius orbit
and not all18432 residue units. Inserting the Gaussian-unit
cosets as extra ray terms would change the character calculation.

The finite-field modulus in the certificate was independently checked
irreducible of degree24 before constructing F_(5^24). The point
coordinates were decoded in that exact polynomial basis and checked
on E. I then used the DIFFERENT primitive point

    B'=[i]B=(-x(B),3y(B)).

Since i is not in H, this is outside the original H orbit. No cached
curve order was needed for the point arithmetic in the independent run.

The exact annihilator checks were repeated for B': [mu]B'=0 and
[mu/lambda]B'!=0 for every distinct Gaussian prime divisor lambda.
They prove that its annihilator ideal is exactly(mu). Indeed any
proper divisor of mu generating that annihilator would divide
mu/lambda for at least one such lambda. The mu-isogeny is étale of
degree Norm(mu), so a point with this exact annihilator identifies
its full geometric kernel with the cyclic O/(mu)-module.

The independent Gaussian power calculation gives

    pi^24=32125393-242017776i,
    (pi^24-1)/mu=-186720-972024i.

Coordinate Frobenius on B' equals [pi]B'. Separately, the integer
trace recurrence t0=2,t1=-2,t_n=-2t_(n-1)-5t_(n-2) gives the stated
curve order59604644711139840. This validates the author's cached
order; the independent orbit check does not rely on setting it.
There are exactly4608 distinct points in the independently evaluated
H orbit.

Étaleness identifies this torsion with its characteristic-zero
reduction over the maximal unramified field. The fixed beta1 and
any other primitive point differ by a unit of O/(mu), necessarily
epsilon h with epsilon a Gaussian unit and h in H.
The exact rational identity Theta_a(epsilon Z)=Theta_a(Z) and
[epsilon]^*omega=epsilon omega imply

    L_d(epsilon Z)=epsilon^(-d)L_d(Z).

Reindexing H contributes rho(h)^(-1). Thus primitive-point changes
multiply S_d by epsilon^(-d)rho(h)^(-1), a NONZERO scalar. This
proves the zero/nonzero invariance needed for the original beta1.
It does not identify the displayed finite-field values with its
unmarked period coordinates.

## 4. Independent invariant-derivative computation

For omega=dx/(2y) in characteristic5,

    D x=2y, D y=3x²+4, y²=f=x³+4x.

Consequently D(A+yB) has even part(3x²+4)B+2fB' and odd part2A',
which confirms the author's recurrence. Also
D log Theta_7=-12 D log psi7=-24y psi7'/psi7. Thus its starting
factor and all derivatives are correct.

The independent calculation did NOT use that recurrence or Sage's
division_polynomial(7). It formed the polynomial from the classical
division recurrences:

    p3=3x^4+4x²+4, B4=x^6+1,
    p5=2f²B4-p3³, psi7=p5 p3³-3f²B4³.

Here psi2=2y and psi4=4yB4; eliminating y² gives these exact formulas.
The resulting psi7 has degree24 and is even. Every orbit denominator
psi7(x) was checked nonzero. This is also forced by the coprimality
of(mu) and(7), since the orbit points are nonzero mu-torsion points.

The alternative invariant Taylor flow is

    x(z)=x+2yz+(3x²+4)z²+4xyz³+2xz⁴ mod z⁵.

Its coefficients follow directly from x'=2y and y'=3x²+4,
with factorials1!,2!,3!,4! invertible modulo5.
The verifier evaluates psi7(x(z)) with its Hasse derivatives,
divides by psi7(x), and computes

    log(1+v)=v-v²/2+v³/3-v⁴/4 mod z⁵.

Multiplication of the degree-d coefficient by-12d! yields L_d.
Thus this is an independent invariant-parameter evaluation, not
a derivative with respect to x mistaken for D_omega.

The weighted sums on B' are exactly

    S'_1=0, S'_2=4S_2, S'_3=S_2, S'_4=0,

where S_2 is the ORIGINAL certificate vector and the equality
S_3=2S_2 in that vector basis is independently respected.
In particular S'_2 has constant coefficient4 and S'_3 constant
coefficient1. The complete polynomial vectors are preserved in
the independent output. All four match the expected i^(-d)
scaling of the original certificate, and give the pattern
false,true,true,false.

Since the L_d have coefficients in F5, Frobenius reindexing gives

    S_d^5=rho(pi)^(-1)S_d=3S_d.

This was also verified exactly for all independently computed sums.
It checks the character direction without replacing the full global
sum by a single Frobenius trace.

## 5. From finite sums to the LOCAL Taylor coefficients

At a=7 the original smoothing scalar is672, a5-adic unit. Its sign
agrees with Psi((7))=-7:7 is inert, and the j1728 reduction has
trace zero (the quadratic-character terms at x and-x cancel);
the square of its7-Frobenius is[-7].
Also alpha=barpi is a unit and the matched Omega_j is a unit by
the independently reviewed core theorem.

Therefore C_(1,d) is zero modulo5 precisely when the corresponding
S_d is zero. The error C_d-C_(1,d) in5W, together with C_d in Z5,
proves exactly

    C1 in5Z5, C2 inZ5^times, C3 inZ5^times, C4 in5Z5.

No numerical value of Omega_j, or identification with an independently
chosen Katz period, is needed for these unit statements.
The finite sums do NOT prove C1 or C4 is exactly zero.
These are coefficients in the formal POINT variable z. They are not
the old cyclotomic c_(2,5), and this review makes no assertion about
that coefficient from this calculation.

## 6. Exact nonadditivity for every pair of nonzero formal parameters

Let r=v5(x)>=1 and s=v5(y)>=1. In the proved convergent series,
the degree-two term of the additivity defect is C2xy, of valuation r+s.
For a higher summand indexed by positive j,k with j+k>=3, its
valuation is bounded below by

    r+s + ((j-1)r-v5(j!)) + ((k-1)s-v5(k!)).

Each parenthesis is nonnegative, and is positive when its index is
at least2. For example v5(n!)<n-1 for n>=2, so the integer
(n-1)r-v5(n!) is then at least1. At least one of j,k is at least2.
All higher terms consequently have valuation at least r+s+1.
The core coefficient integrality and convergence justify applying
this bound to the entire infinite tail.

No term can cancel the leading unit C2xy. This proves(6.4) exactly,
including y=-x, and proves that the actual local map is not additive.
It is not an inference that four computed jets alone determine an
arbitrary analytic function; the all-degree bounds are a proved
dependency from the core theorem.

## 7. The three actual rational points and the integral lattice

The independent run used Python Fraction arithmetic and the rational
short-Weierstrass chord/tangent formulas. It first checked
P+Q=(1/4,25/8), then doubled each of P,Q,P+Q six times.
It did not use the author's finite-field group law or a numerical
p-adic logarithm for this check.

For t=-x/y, the results are

| Point | v5(t) | t/5^v5(t) modulo5 |
|---|---:|---:|
| 64P | 1 | 4 |
| 64Q | 1 | 1 |
| 64(P+Q) | 2 | 4 |

The invariant differential in this integral local parameter has
constant coefficient1 and integral higher coefficients. In its
logarithm, an n-th term for n>=2 has valuation at least
n v5(t)-v5(n)>v5(t). Hence v5(log_E R)=v5(t(R)) here, with
the same leading unit. Put x=log_E(64P), y=log_E(64Q).
Their sum is log_E(64(P+Q)), so the verified valuations are1,1,2.

The particular additivity defect has logarithm valuation exactly2
by the preceding section. Under the exact integral isomorphism
Log_omega:H1(Q5,T_pi)→5Z5, a primitive lattice generator has
logarithm valuation1. Thus the defect has lattice divisibility
exactly5 and is NONZERO modulo25 in H1. This is a statement
about the lattice quotient, not about reduction modulo25 of
the unscaled logarithm in Z5.

## 8. Separately checked sharper P-or-Q consequence

The coordinator proposed this refinement after the main certificate
was saved. It follows from the same completed arithmetic, with no
new run or additional coefficient computation.

Since C1 is divisible by5 and v5(x+y)=2, the linear term of
F_a(x+y) has valuation at least3, while all terms of degree at
least2 have valuation at least4. Thus F_a(x+y) is in125Z5.
The defect F_a(x+y)-F_a(x)-F_a(y) has valuation2, so
F_a(x)+F_a(y) has valuation exactly2.

Each of F_a(x),F_a(y) is in25Z5: its linear term uses C1 in5Z5,
and its quadratic and higher terms have valuation at least2.
Therefore at least one of those TWO values has valuation exactly2.
The associated local class for64P or64Q is consequently divisible
by5 but not by25 in the integral H1 lattice. The sum-point class,
in contrast, has logarithm valuation at least3 and is zero modulo25
in that lattice.

This does not identify which of the two classes has valuation1 in
lattice coordinates. It does prove the sharper alternative without
claiming a value for the unknown linear coefficient beyond C1=0 mod5.

## 9. Verdict and limitations

**PASS.** The actual subgroup, character weights, primitive-point
scope, invariant derivatives, local Taylor unit, exact additivity
defect and rational-point valuations are independently verified.
The sharper P-or-Q consequence is proved in§8 of this review.

The result excludes the specified single linear point-map correction
for this local norm family at the three prescribed points. It does
not prove a global Selmer specialization, an original cyclotomic
coefficient nonvanishing theorem, or BSD. Additional boundary
counterterms and other arithmetic operations are not ruled out.
The original certificate remains unchanged, the independent verifier
and output are durable, and no old numerical run was repeated.
