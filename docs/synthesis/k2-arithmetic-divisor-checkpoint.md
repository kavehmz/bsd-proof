# Arithmetic noncentral K2 divisor restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
The [complete construction](k2-arithmetic-divisor-attack.md) passed the
[separate seven-section review](review-k2-arithmetic-divisor.md).
Reviewed proof: ad0bd821520518592dbee0023e4119199cf790ea626ccedee3cf019f4d4d463a.
Subsequent status links and a clarification that b is a chosen integral
preimage are editorial. No old numerical certificate was rerun.

## Actual class and exact source scope

Beta2 is the SAME finite class of integrated-spectral-comparison §7,
with regulator L(E,2)/pi. It is a rational coefficientwise trace of
proper transfers of normalized modular-unit symbols on X_mu(389).
It is not replaced by another class with the same regulator.

Schappacher–Scholl, Beilinson's theorem on modular curves (1988),
Theorem1.1.2(iii), definition1.1.1 and7.3.1 prove an actual CLASS-IMAGE
arithmetic integrality theorem for these unramified modular-unit symbols.
Their temporary full-level hypothesis is handled at3*389, with the
covering degree retained in rational pull-push descent (7.3.2).
Scholl0710.5453 §1 gives model-independence and preservation of that
rational K-theoretic arithmetic image under Chow correspondences.
The actual transfer to E and the finite rational coefficient trace
therefore stay in this arithmetic image.

Do NOT assume the model is smooth over Z or invoke an unspecified
strong global K/CH comparison. The reviewed proof restricts the
arithmetic K-class to the regular model over the DVR Z_(389), applies
the rational K'=K / higher-Chow comparison THERE (Geisser Handbook
§1.4.4), and deduces zero rational CH boundary at389. Every good-prime
rational boundary target is zero independently. GLOBAL Bloch localization
then constructs the rational higher-Chow lift. Geisser2004 Theorem3.2,
Corollary3.3 and Lemma2.4 explicitly allow essentially finite type here;
the special fiber need not be smooth.

Integral assertions below concern Bloch CH²(model,2), not an integral
Adams splitting of all Quillen K2. Generic rational weight two is
identified with the unramified Milnor-symbol class by the usual smooth
curve comparison. No p-primary Chern normalization is inferred.

## Explicit bad fiber and arithmetic localization

The actual model is Y²Z+YZ²=X³+X²Z−2XZ². Its only singular fiber
is split nodal at389. Node=(299,194); normalization t satisfies
x=299+t²−120, y=194+t(t²−120). The node branches are148 and241.
The smooth open is G_m via z=(t−148)/(t−241); infinity is retained
at z=1. Field localization gives

    CH¹(D,2)=0,
    CH¹(D,1) = F389* × z^Z.

The boundary of c z^j at the ONE node is the sum of branch valuations,
j−j=0; both residue degrees are1. This is NOT the ordinary unit group
of the proper singular D. The free Z direction is a real possible
arithmetic-boundary obstruction. At every good r the corresponding
groups are0 and Fr*, by smooth weight one and proper integrality.

Arithmetic localization therefore gives an INTEGRAL injection

    A=CH²(model,2) -> A_E=CH²(E,2),

with image the kernel of actual vertical residues. Rationally the
only remaining boundary is the z-exponent at389. The exact modular-unit
arithmetic-image theorem kills this exponent for beta2. Consequently
beta2 has a UNIQUE lift tilde_beta2 in A tensor Q. No finite Sha or
unknown regulator injectivity is used.

## Sufficient finite-data denominator, not primitive integrality

Expand beta2=sum q_ab h_*{U_a,U_b}, with the explicitly traced rational
coefficients from the predecessor. Choose M clearing the finitely many
cusp-divisor denominators, so V_a=M U_a are actual rational functions
with leading coefficient1. Choose D_c clearing all q_ab.

At possible horizontal residue points, the functions have support
only at the RATIONAL infinity cusps of the X_mu model. Rational
unramifiedness makes their tame symbols torsion in Q*, hence ±1.
The factor TWO kills them integrally. Thus

    D0=2M²D_c,
    b=sum (D_c q_ab) h_*(2{V_a,V_b}) in A_E,
    b tensor1 = D0 beta2.

Here b is the SPECIFIED integral preimage. It is not an inverse of
rationalization, and possible integral torsion is not dismissed.
Choose finite S0 over which this finite higher-cycle representative
spreads to model[1/S0]. Outside S0 all vertical residues vanish.
At each good r in S0 the residue is killed by r−1. At389 its integer
z-exponent is zero because its rational boundary iszero, leaving only
F389* torsion killed by388. Hence

    D1=lcm_(r in S0)(r−1), D=D0 D1

kills every boundary. There is a UNIQUE integral B in A restricting
to D1 b, and B tensor1=D tilde_beta2, with regulator D L(E,2)/pi.
No numerical values of M,D_c,S0 or D are certified in this note.
Once the finite choices are fixed, D is independent of any later
coefficient prime or exponent. Z B is a nonzero free integral subgroup,
not a proved saturated or primitive lattice in all arithmetic K-theory.

## Remaining objective

The noncentral divisor now has an actual rational arithmetic lift and
a sufficient integral multiple. The missing object is still a rational
arithmetic source/map for the integrated theta class into
D_pt tensor Q beta2 tensor Q(1)^(-2), with the prescribed coefficient
6N(N−1)n_E and genuine lattice control. D and that large integer are
not declared units. This construction does not prove rationality or
integrality of n_E, Sha finiteness, or full universal BSD.
Read research-state §5 for current team status and next assignments.
