# Review of the finite CM moments and sharp point-height index

Date: 2026-09-12. Reviewer: root/coordinator. Review of
[the construction](cm-uniform-carry-attack.md) and its
[checkpoint](cm-uniform-carry-checkpoint.md).

**PASS.** All nine sections were read and reconstructed. The proof gives
the exact conditional integral index formula and a finite arithmetic
construction of the actual point-Bockstein determinant. It does not
prove uniform nonvanishing, remove the actual index factors, or descend
the separate p-adic frame coordinates to one rational scalar.
No old numerical certificate was rerun.

Mathematical proof inspected:
6faa3fc9826eb23610c719fb83818d8c5464d4c1d21eb17bed754e2f3f366faa.
Checkpoint:
6cce4ddde931b77f59365e45c93a1d7ca4fd90e0c52f85df823362486af405f5.
Subsequent completed-status links are editorial.

## 1. Actual measure, augmentation coordinate and finite paths

The curve, full point basis, differential, Tamagawa/torsion factors,
unit-root choices and the p-prime smoothing/norm are the reviewed
predecessor inputs. Direct addition gives P+Q=(1/4,25/8).
The nonzero coefficient premise in later sections concerns the
precisely normalized MTT series, not a different isogeny lattice.

For q=p^(n-1), reducing the actual group ring modulo T³ gives
qT+binom(q,2)T²=0 and qT²=0. Since binom(q,2)=q(q-1)/2,
these are exactly qT=0 and qT²=0. No smaller annihilator of T²
is introduced: a relation with no T-term has its T² coefficient
in qZ_p. This verifies both augmentation quotients in (8).
The image of the genuine T²-divisible Iwasawa series belongs to
J_n². Its quadratic coordinate is the certified coefficient modq.
The group-ring quotient is continuous since T is topologically
nilpotent there, so passage from the formal series is legitimate.

The binomial-error proof and the actual carry formula agree with
the earlier reviewed certificate. The integer Teichmüller residues
are used at each denominator; the symbolic notation does not
apply a real modular-symbol map to a nonrational p-adic argument.
The closed-loop interpretation after the parametrization follows
from the actual cusp images. Adding conjugates gives period2Omega m,
an integral multiple of the primitive real period. None of this
converts the finite group-ring element into a rational point.

## 2. Integral self-duality with the finite Ext term retained

I read the cached primary Nekovář, *Selmer complexes*,
[Theorem6.3.4,6.3.5 and6.7.4–6.7.9](https://www.numdam.org/item/AST_2006__310__R1_0.pdf).
The local ordinary plus lattice is primitive and isotropic under
the integral Weil pairing, and the quotient is its integral Tate
dual. Thus the ordinary local error complex is acyclic. At every
bad prime the nontrivial CM inertia survives modulo the stated p,
so the full local complex and its dual error vanish. Odd-p real
Tate terms vanish as well. These are the actual hypotheses needed
for the integral duality theorem, not a generic unramified assertion
at an arbitrary Tamagawa prime.

The resulting perfect base complex is self-dual with shift minus3.
For a two-term free complex over Z_p its universal-coefficient
sequence in degree2 is exactly

    0→Ext¹(H²,Z_p)→H²→Hom(H¹,Z_p)→0.

The Ext group is finite and the last term is free. Consequently
it is exactly the entire torsion kernel, and the induced map on
H² modulo torsion is an INTEGRAL isomorphism. This conclusion
needs no finite-Sha hypothesis. Over this DVR the direct two-term
calculation has no unaccounted higher Ext group or pseudo-null
quotient. The finite term has been retained explicitly.

The point lattice is saturated in integral Selmer because T_pSha
is torsion-free. This does not make it the entire Selmer lattice.
The further finite-coefficient exact sequence in (15) correctly
keeps H²[p^m]. The point matrix does not identify that extra finite
term with zero.

I also read the primary height setup in Nekovář11.1–11.3 and
[BKS5.1.1 and (5.3.2)](https://arxiv.org/pdf/1910.07404v2).
The defined height uses minus the natural connecting map and the
corresponding global duality convention. BKS explicitly uses the
§6.3 duality map, and sends gamma-1 to log_p chi_cyc(gamma), with
no extra factor1/p. The alternating polarization gives a symmetric
height pairing in this convention.

## 3. The exact Smith-frame formula

Nonzero c2 FIRST gives actual derived-class nonvanishing, full
Selmer corank two and finite primarySha by the reviewed argument.
Only then does the point lattice become all of H¹ and torsH²
become the full primarySha group via the coefficient triangle.
The proof keeps this order, so no divisible Sha direction is lost.

The Smith calculation is integral. If U A0 V has nonzero diagonal
entries p^(a_i) and two zero entries, a determinant term of degree2
must use every one of those constant entries. Its remaining block
is exactly the lower-right linear2×2 matrix D. Therefore

    [T²]det A(T,T)=(detU detV)^(-1) p^(sum a_i) detD.

The kernel basis consists of the last columns of V; the free
cokernel basis consists of the last columns of U^(-1). If (P,Q)=kC
and J_ij=Dcal(q_j)(k_i), then C,J are integral invertible matrices.
Evaluation of the minus-Bockstein gives precisely
B=-C^t J D C. Thus detB=(detC)² detJ detD, with no additional
sign in ranktwo. This reconstructs every factor of epsilon_p in
(21). Its value is defined by the actual frames and element; it
is not an afterward chosen correction set equal to one.

The Fitting-ideal equality and valuation identity follow exactly.
In particular, a coefficient valuation e and a determinant divisible
by p^(e-1) leave a primarySha valuation at most one. The already
finite primary group has even valuation by Cassels alternation,
so it is zero. When its exact order is desired, precision p^(e+1)
is sufficient because the actual determinant valuation is at most e.
No nonunit Smith factor or regulator is divided modulo p^m.

## 4. The actual sigma normalization and finite tail

I directly checked [Mazur–Stein–Tate, pp.586–588, (1.1)–(1.3)
and Theorem1.3](https://wstein.org/papers/pheight/pheight.pdf).
Its functional is log_p(chi)/p, its quadratic height is minus
one-half of its bilinear diagonal, and its formula is
p^(-1)log_p(sigma/d). Scaling that bilinear pairing by p/g_p,
and dividing by n_p², gives EXACTLY

    2/(n_p² g_p) log_p(d_R/Sigma(t_R)).

This proves the stated sign and factor2; it does not import MST's
quadratic height as though it were the BKS bilinear pairing.
The point comparison uses the same global logarithm and the same
ordinary complement, as in the previously checked Nekovář/Besser
comparison. It applies on point classes without identifying all
Selmer classes with points or using a BSD regulator theorem.

The already reviewed CM sigma identification supplies the SAME
rational formal series at every stated ordinary prime. Its integral
series is in the parameter t, not in the elliptic logarithm. The
multiplier n_p=8N_p is a p-unit, kills every bad component group,
and puts each of the three points in the formal subgroup. For its
reduced rational coordinates a,b are p-units and v_p(t)=v_p(d)>=1.
These are exactly the hypotheses of the cited height formula.

Truncation through degree m+1 has absolute error valuation at least
(m+2)v_p(t). Dividing by the leading sigma value loses v_p(t), and
then dividing its logarithm by g_p loses one. The resulting height
error is therefore at least m. Thus the finite rational unit in(24)
is sufficient; it cannot be zero because its leading p-adic valuation
is fixed by t.

Equation(25) is an exact finite coordinate: 1+p has order p^m
modp^(m+1), p-1 is invertible modp^m, and raising the unit to p-1
removes its Teichmüller part. It gives log_p(u)/g_p modulo p^m.
The three diagonal values and symmetric polarization prove (27),
including the denominator2. This is a proved finite approximation
to the actual point pairing, not a stabilization experiment.

## 5. First Fermat determinant and the existing prime5

I independently expanded the formal equation. From
a=39 one gets x=t^(-2)-39t²+O(t^6) and
omega=(1+78t^4+O(t^8))dt. If Sigma=t(1+s t^4+...),
its differential equation gives156-12s=-39, hence s=65/4.
The rational CM symmetry excludes degrees not congruent to1mod4.
So the indicated truncation is t for m<=3, and its unit is -b/a.

Modulo p², equation(25) reads
1-p lambda=1+p mathfrak_q_p(u), so lambda=-mathfrak_q_p(u) modp.
In the2×2 determinant its common minus sign cancels, giving
exactly n_p^(-4)(4x_P x_Q-(x_(P+Q)-x_P-x_Q)²).
Higher requested precision still needs the full finite coordinate
and longer sigma truncation; the proof does not use this first
Fermat quotient at every precision.

At the existing certified prime5, the sharp index with Sha5=0 gives
v5(detB5)=1. The Néron logarithmic bilinear matrix is g5 B5 and
v5(g5)=1, hence the regulator valuation is3. This is a deduction
from the new normalization and existing certificate; it is not a
new numerical regulator output.

## 6. Remaining uniform and rational scope

For a fixed nonzero rational point nP, formal reduction at a good
prime is equivalent to divisibility of its fixed denominator by p.
Its support is finite. A finite list of fixed multipliers therefore
cannot put P in the formal group at almost all primes. This tests
that precise attempted common finite evaluation, while leaving
other global constructions and Coleman continuation open.

The exact index identity relates the two ACTUAL arithmetic inputs,
but it does not establish a successful coefficient test at every p.
A larger coefficient valuation can be entirely a point determinant;
the old sufficient bound was not necessary. The finite tests (32)
remain sufficient, not asserted universally true.

Finally Reg_p=g_p² detB_p and c_cmp,p M_p=2g_p²c2 reconstruct
(33) with its fixed2e_p denominator. Thus q_p is integral and has
valuation equal to that of primarySha wherever c2 is nonzero.
The explicit unit epsilon_p/(2e_p) is not identified with1 and
is not compared across different completions. The rational frame
and real leading coefficient in (34) remain a conclusion to prove.
All other primes and full universal BSD remain outside the result.
