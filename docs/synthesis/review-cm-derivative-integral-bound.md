# Independent audit of the CM integral coefficient bound

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file.

**PASS.** This is a third, bounded audit of Sections6–7.2 of
[the CM derivative proof](cm-derivative-nonvanishing-attack.md),
mathematical revision
190fdbe54ca357dc2b9ec3dcf3b189da1ee23aa13447b79b5e41cf0757806128.
Those sections were re-read after the whole-file hash changed.
No repair to the stated integral bound is required.

The [reviewed Iwasawa presentation](cm-iwasawa-presentation-attack.md),
revision b8e93f0139ef77987d3f88c57731d66d348d223aa1a3ca01b2f24e5ba6c1db02,
and the certified c_2=20 modulo25 are inputs to this audit.
I did not rerun or independently certify the numerical computation.
The coordinator's broader review covers that certificate.

## 1. The local coordinate is an integral unit

The CM splitting at each good split p>=5 is integral.
Its two rank-one lattices pair perfectly through the
elliptic Weil pairing. Nonanomalousness kills H^0 of
the unramified residual line, while cyclotomic inertia
kills H^0 of the other line. Local duality kills the
corresponding H^2 terms. Finite-coefficient local duality
then shows that the two free rank-one H^1 lattices pair
perfectly over Z_p. In particular this pairing has no
unaccounted p-power index.

Exact local base change in presentation Proposition5.1
identifies e_(L,0) with a generator of the opposite
integral quotient lattice. It is not merely a rational
generator. The integral Shapiro identification is an
explicit input of the reviewed presentation.

Because p does not divide #E(F_p), the p-completion of
E(Q_p) is the formal group E_1(Q_p). The Neron formal
logarithm is an isomorphism onto pZ_p. The fixed
exponential identity gives
$$
 \log_\omega(\exp\delta_0)
    =k_\alpha^{-1}
     =\frac{1-\alpha^{-1}}{1-\beta^{-1}},
           \qquad v_p(k_\alpha^{-1})=1 .
$$
The numerator is a unit and the denominator has
valuation -1. Thus exp(delta_0) is a primitive
integral point, not just a nonzero rational vector.
Pairing it with e_(L,0) is a unit, proving Lemma6.1.
No global integral self-duality is used.

I checked the fixed factor in
[BKS1910.07404v2, equations6.3.1–6.3.2](https://arxiv.org/html/1910.07404v2)
and the local Kummer/duality framework in
[Milne ADT, I.3](https://www.jmilne.org/math/Books/ADTnot.pdf).
The formal logarithm normalization is the Neron one
already fixed in the presentation; it is not changed
to make this coordinate a unit.

## 2. The coefficient sequence gives the finite Sha group

The proof correctly uses finiteness from (10) BEFORE
identifying the torsion of H^2 with full primary Sha.
Without that input, the image of the V-Selmer group
would also contain possible divisible Sha directions;
one could not make the same identification.

Here the saturated plus lattice makes the coefficient
sequences for T,V,W=V/T and for their local plus/minus
modules exact. The ordinary cone therefore gives an
exact triangle. This is the explicit cone construction
in Nekovar Sections3.4 and6.1, whose defining local
sequences were inspected in the cached primary text.

There is no extended-Selmer H^0 term at p:
H^0(W^-)=0 since alpha-1 is a unit. Likewise local
duality gives H^2(T^+)=0. The finite condition on W
is the image of H^1(W^+), equal to the formal point
Kummer condition. At the bad primes the nontrivial
mu_4 inertia survives modulo every p in the stated
range, so the local cohomology terms vanish. Real
Tate cohomology vanishes at these odd primes.
Outside the ramification set the ordinary unramified
conditions match the respective point conditions.

Using already proved primary finiteness, the H^1
terms for T,V are the completed point lattice and
its Q_p span. The coefficient sequence gives
$$
 \operatorname{Sel}_{p^\infty}(E)/
      (E(\mathbb Q)\otimes\mathbb Q_p/\mathbb Z_p)
    \simeq\ker\bigl(H^2(C_f(T))\to H^2(C_f(V))\bigr).
$$
The left side is Sha[p-infinity]. Perfect rational
base change makes the right side exactly the Z_p-
torsion subgroup of H^2(C_f(T)). This proves
Lemma6.2 with the actual local terms, rather than
postulating an integral duality identification.

## 3. Integral Smith expansion and alternation

Over Z_p, put the constant square matrix into Smith
form with nonzero entries p^(a_1),...,p^(a_(d-2))
up to units, and two zero entries. The sum
s=sum a_j is the length of its cokernel torsion,
hence v_p(#Sha[p-infinity]).

To contribute to the coefficient of T^2, a determinant
term must select one linear entry from each of the
two zero rows. All other rows must use their constant
diagonal entries. The remaining columns are exactly
the last two. Consequently
$$
 [T^2]\det A_{\rm cyc}(T)
        =(\text{unit})\,p^s\det B ,
                  \qquad B\in M_2(\mathbb Z_p).
$$
Every other term needs at least three powers of T.
No inverse nonunit Smith entry is used, so the
inequality s<=v_p(c_2) follows from the reviewed
unit u(0), the newly proved iota_p unit and the
exact diagonal second-coefficient identity.

After primary finiteness, the Cassels–Tate pairing
on that primary subgroup is nondegenerate and
alternating. The rational principal polarization
provides the alternating pairing; Milne I.6.26
identifies its kernels with divisible subgroups.
Different primary components pair trivially with
one another, so this use does not assume that
the entire Sha group is finite.
Its order is a square, hence s is even.
At5 the certified valuation1 gives s<=1 and
therefore s=0.

This also makes det B nonzero over Q_5, giving
the stated rational Bockstein nondegeneracy.
It does not identify an exact numerical regulator.

## 4. Uniform conditional scope and finite carry identity

The uniform nonanomalous argument is valid:
the rational point(0,0) of order2 makes #E(F_p)
even. For p>=7 Hasse places this number strictly
between0 and2p; it cannot equal the odd number p.
At5 it is8. Thus the unit proof applies to every
good split prime in the stated range.

For any such prime with c_(2,p) nonzero, the
previous full-Selmer height and corank argument
first proves primary finiteness. The same coefficient
sequence and integral Smith proof then give
$$
 0\le v_p\#\operatorname{Sha}[p^\infty]
       \le2\left\lfloor v_p(c_{2,p})/2\right\rfloor .
$$
This is conditional on nonzero c_(2,p); it does
not prove that nonvanishing for another prime.

The algebra in Proposition7.1 checks as well.
The weight difference for j=r+pt is
pt(2r-1)/2+p^2t^2/2. Distribution removes the
second term modulo p^2; the old-symbol part
of the first term vanishes after summing t
modulo p. The Hecke relation and m(0)=0
give B_(2,p)=0, leaving the stated carry
coefficient pC_p/(2alpha^3).
With the supplied rational rows at5, this
indeed contributes5+15=20 modulo25.
This was an algebraic check of supplied values,
not a numerical certificate rerun.

The requested integral argument is sound in its
stated scope. It supplies Sha[5-infinity]=0
for this curve and the conditional uniform bound;
it supplies no all-prime nonvanishing, rational
global regulator comparison or universal BSD proof.
Only this assigned review file was written.
