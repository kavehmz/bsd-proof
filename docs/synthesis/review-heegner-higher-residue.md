# Independent review of the higher Heegner residue construction

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. **Verdict: PASS for the corrected stated deductions.**

Reviewed [proof](heegner-higher-residue-attack.md), SHA256
`627ab2762db0c56c94ee8eac3cff963e2dfb21ed2b0e5c89419df89adfc900f6`,
and [checkpoint](heegner-higher-residue-checkpoint.md), SHA256
`aec6c2ab207ffbe1cc3c6db4ca181d8540500d86a7029fce97d8cd96039bbc53`.
The coordinator's polynomial-sign correction was inspected in this
revision. No further mathematical correction is required.
The conditional cyclicity theorem concerns the ACTUAL full strict
finite Selmer group. Its proof does not establish the primitive
assumption or the desired rank-five Heegner vanishing.

## 1. Actual classes, local conditions and residue signs

I read the current signed Gysin proof and its independent review.
The compact cone, negative standard Gysin map and signed boundary
are explicitly retained. Their quotient is the perfect dual of the
full strict group specified in §1, not merely a Sha quotient.

Even-index raw classes have plus conjugation sign and hence descend
by the stated half-corestriction. Since 2 is invertible, restriction
of this descent is exactly the original K-class. At the old two
conductor primes the group A_S allows all local cohomology; at its
other finite primes corestriction takes point Kummer classes to point
norms. Thus these actual classes belong to B_T. They have zero tame
residue at fresh primes outside their index. This is precisely what
is needed to annihilate the S-boundary in the strict dual.

The chosen lift of a local ring-class generator has primitive
p^k-Kummer uniformizer value: its tame exponent is prime to p,
because it maps to a generator of a cyclic group whose order is
divisible by p^k. The unramified quadratic restriction changes
neither its inertia nor its uniformizer valuation.

The corrected polynomial identity is
$$(a-F)(F^2-1)=(v+1)F-a.$$
Substitution into the actual INTEGER cofactor (7) therefore gives
$\overline B=-Fx=x$ for the odd-index finite minus class.
The raw cocycle on inertia has the opposite sign, $-\overline B$.
This agrees with the explicit cocycle and finite-singular computation
in [Howard, §1.7](https://arxiv.org/html/1202.6340#S1.SS7), read directly,
and with the project's reviewed sign calculation. The Weil-dual
normalization thus gives residue $-h_{J,v}y_v$, with no factor two.
The factor two belongs separately to the rational Frobenius pairing
with the K-local value in (4). Equations (10) and (11) follow with
their stated signs and full p^k coefficients. The standard scalars
$u_2=u_3=-1$, $u_4=1$, $u_6=-1$ and the nontrivial action on the
stripped tensor factors are consistent.

## 2. Joint translation image at full coefficients

The primary cohomology input was checked directly in
[Lawson–Wuthrich, 1505.02940v2, Lemmas 3–4](https://arxiv.org/pdf/1505.02940v2).
Over Q and for p>=5, irreducibility forces a nontrivial residual
homothety; the induction in Lemma 3 then gives the stated vanishing
at every p^k. It does not require a central homothety lift at every
level. The disjointness of K and the torsion field follows from the
ramified discriminant prime at which the latter is unramified.

The image algebra calculation is stronger than residual irreducibility
alone, and the note supplies the extra input it uses: the image of
G_K contains the matrix of rational complex conjugation. Its plus
and minus summands are free rank-one R-modules. Their idempotents
give E11 and E22. Residual irreducibility supplies unit entries in
both off-diagonal directions; multiplying by those idempotents and
inverting only unit entries gives E12 and E21. Hence the FULL
R-algebra of matrices, not just its mod-p reduction, acts on W.

Here is the double-annihilator check in detail. View V^d as two
rows of R^d. Stability under the diagonal units isolates each row;
stability under E12 and E21 identifies the two row modules. Thus
$W=A\oplus A$ for a single submodule $A\subset R^d$.
A vector r annihilates A under the dot product if and only if
$\sum r_jc_j$ restricts to zero over the torsion field. Restriction
injectivity identifies this with an ACTUAL cohomology relation.
The internal direct-sum hypothesis therefore gives
$A^\perp=\bigoplus_jp^{s_j}R$. The dot product followed by division
by p^k is a perfect finite abelian-group pairing. Its double-annihilator
identity gives $A=\bigoplus_jp^{k-s_j}R$ exactly. No freeness of A
or arbitrary Iwasawa specialization is used.

The rational cocycles with coefficients V or its K-quadratic twist
give a finite Galois extension. For an actual involution tau and
$h$ in the joint translation subgroup,
$$c_j((h\tau)^2)=(1+\epsilon_j\tau)c_j(h).$$
The omitted tau-cocycle term is zero because tau has order two.
Since 2 is invertible, this gives every prescribed value in the
required signed p-power eigenspaces. Conjugacy transport may change
bases, but preserves all zero and exact-order conditions used later.
Thus Proposition 4.2 supplies the simultaneous arithmetic choices
at the full coefficient level without a full-image hypothesis.

## 3. Primitive elimination and control of the entire strict group

A unit base value at v_i makes the actual three-prime class d_i
have full order via its transverse evaluation. Its minus sign
separates it from every plus class. Joint detection supplies v_j
with a_j=0 and h_ji a unit. The scalar relation then gives h_ij=0,
and the vector relation gives g_j=0 in the FULL strict dual.
Before quotienting, (16) retains its explicit old-S boundary.
The detecting g_i survives with order p^k.

For Theorem 6.1, an arbitrary z in the stated full strict group can
be adjusted by a unique scalar multiple of kappa to have zero value
at v_i. If the remainder z' is nonzero, the relation between it and
kappa has zero kappa coefficient, because evaluation there is a unit.
Thus these two plus classes have exactly the internal direct-sum
relations needed for Proposition 4.2; adding d_i preserves this by
the opposite sign. The resulting v_j detects z' but has g_j=0 from
the actual four-prime relation, contradicting perfect duality.
This proves $\mathcal S=R\kappa$ for the actual strict Selmer group,
including any finite or divisible-Sha contribution represented there.
It does not control only a chosen subspace or a quotient.

In the nonprimitive case the scalar annihilator is exactly p^sR.
The note correctly keeps $h_{ij}\in p^sR$ and an h_ji of its actual
order. It neither divides by these nonunits nor replaces the whole
Heegner system by divided hypothetical classes.

## 4. The independent free direction really exists

The prior reviewed odd-rank result is a lower bound on the corank
of the full p-infinity Selmer group. A corank at least three gives
a divisible subgroup $(\mathbb Q_p/\mathbb Z_p)^3$, whose p^k-torsion
is a free $R^3$. Since $E(\mathbb Q)[p^\infty]=0$, the coefficient
exact sequence identifies the finite Selmer group with the p^k-torsion
of p-infinity Selmer: local kernels introduced by coefficient change
are point Kummer classes, so this statement preserves the finite local
conditions. This justifies an actual embedded $R^3$, not merely a
mod-p dimension count.

At either old good prime, Cayley–Hamilton gives F^2=1 on V; the two
idempotents have rank one and F-1 is a unit on the minus summand.
Thus the full finite Kummer target is $V/(F-1)V\simeq R$.
The two localization maps restricted to the embedded $R^3$ form a
2-by-3 matrix over the principal ideal ring R. Smith reduction leaves
a zero source column, giving a free R summand in its kernel.
That summand lies in the actual strict group, proving Proposition 6.2.

The primitive consistency statement also follows: the strict kernel
has order p^k and the old targets have total order at most p^(2k),
whereas the embedded $R^3$ has order p^(3k). Equality forces the whole
finite group to be $R^3$ and its localization onto $R^2$ to split.
This remains compatible with a divisible Sha contribution and does
not prove Mordell–Weil rank three.

## 5. Remaining scope

The complete residue source cannot span every fresh test of a
necessarily nonzero strict dual. This does not force the particular
Heegner class to be nonzero, so it is not a counterexample to O5.
The primitive conditional cyclicity and nonprimitive annihilator
constraints are valid finite arithmetic deductions. They supply no
new relation from the additional untwisted derivatives that vanish
at rank five. HR-TP5 and the universal BSD objective remain open.

Only this review was written. No old numerical certificate, prime
scan or height computation was rerun. Subsequent editorial PASS
links and checkpoint status updates do not alter this verdict.
