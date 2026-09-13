# Independent review of the native Heegner pairing construction

Date: 2026-09-12. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. Own only this review file.

**PASS after inspecting the explicit dual-transport precision.**
All seven sections and the checkpoint were read.
Reviewed mathematical proof SHA256:
e67fb3c138b5425cf3b95fa41feb0349f62a8c59ffc23e9fd9eff126da19bcfd.
Reviewed checkpoint SHA256:
8c8828f62311dd3b4f7ad23f5d93c5d5ed246723e50a84e7bb109619d573755b.
The proof is [heegner-native-pairing-attack.md](heegner-native-pairing-attack.md).
Subsequent PASS links and completed-status edits are editorial.
The actual native scalar remains unproved zero; this review does not
promote the construction to rank-five vanishing or full BSD.

## Reconstructed deductions

The clean hypothesis includes zero FULL finite twist Selmer and
p-unit Tamagawa, in the previously stated surjective/Manin range.
It therefore proves d0 is a unit; no such inverse is asserted in
the nonclean case. All coefficients remain Z/p^k.

Finite Poitou–Tate makes the global local image K and the product
finite condition F self-annihilating. Their intersection is zero
because classical twist Selmer is zero. Orders give K+F=H_S.
The S-strict global kernel also belongs to that Selmer group.
Thus q loc is an actual isomorphism with a unique inverse C.

The classes C_v(q) determine isotropic complements by global
reciprocity. At each old rank-one hyperbolic group the graph-slope
argument and 2 invertible force this complement to be the actual
transverse line. The sign beta_i=-a_i tensor t_i^+ is correct:
a_i has tame value -1, so beta_i has the positive uniformizer
value. With e(y_i^-,t_i^+)=zeta_i, finite-FIRST cup with beta_i
is the usual positive unramified-character/uniformizer pairing.
Quadratic restriction multiplies Frobenius value and invariant
by 2 and leaves tame inertia unchanged.

The correction t_i^natural=t_i+C(q(delta)) leaves every local
difference finite. In the compact-FIRST cone pairing one may take
the global primitive t_i^natural cup b_i. All local finite/finite
terms vanish except the old finite/transverse term. This proves
the scalar evaluator and its native-compatibility criterion.
Changing a global primitive is canceled exactly by the inverse C;
native local changes at i add b_i, with zero old finite coordinate.

The bordered determinant formula follows by the Schur complement
over R with det L a proved unit. Shorter cyclic local factors
are retained in the stated Smith/congruence presentation.
The skew-adjoint G_uv relation is the sum of the only two
nonzero local pairings of C_u(q_u) and C_v(q_v).
The zeta-correction cancellation is correct provided its exact
transported p-normalization is fixed consistently.

The actual ramified old-prime norm has cokernel
E(F_(i²))/p^e E(F_(i²)). The formal kernel is pro-i and uniquely
p-divisible, so its norm is surjective even without an unramified
extension: a base formal point can be divided by p^e.
On the unchanged residue field the norm is multiplication by p^e.
Since Frob_i²=1 on E[p^k] and e>=k, the cokernel modulo p^k is R².

The remaining mixed coefficients are the actual G_lq and G_ql
through the fixed old cup isomorphisms. A unit coefficient allows
unique removal of those local coordinates; a nonunit only permits
values in its actual ideal. The residual global kernel belongs
to E, not to the rank-zero twist. The actual top Heegner ambiguity
and the absence of a complex-derivative identification are retained.

## Exact primary checks completed

[Bertolini–Darmon, Derived p-adic heights, AJM117(1995)](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/pub13.pdf),
printed pp1518–1521, was read directly. Assumption(4) requires
surjectivity of all local point norms. It fails in the actual
ramified old-prime extension by the explicit calculation above.
Their classical finite condition also differs from b_i's
transverse condition. The elementary local-duality and Cassels
exact-sequence inputs remain applicable.

[BKS1910.07404v2, §6.3 and proof of Lemma6.14](https://arxiv.org/html/1910.07404v2)
was read directly. Its finite Coleman definition uses
[exp* z,delta], and its cup identity uses (exp delta,z).
Thus delta0=k_alpha^(-1)nu with [omega,nu]=1 gives the
positive scalar asserted in the untransported twist frame.
The two Euler factors combine with k_alpha^(-1) to the
exact nonanomalous factor (1-alpha^(-1))².
No generalized Perrin–Riou hypothesis is used for these identities.

[BCGS2312.09301v2, Theorem3.2.2](https://arxiv.org/html/2312.09301v2)
provides the actual integral Kato classes and their Coleman
image in the Neron-period normalization fixed in the predecessor.
The non-CM scope follows from the added surjective image range.

## Primitive p-coordinate and the inspected transport correction

The local point-completion argument in Lemma3.1 does not need CM.
Good nonanomalous reduction makes the reduction group prime to p,
so the p-completed point group is its formal group.
At p>=5 the Neron formal logarithm identifies that group with pZ_p.
Since alpha is a unit and alpha is not 1 modulo p,
v_p(1-alpha^(-1))=0, while beta=p/alpha gives
v_p(1-beta^(-1))=-1. Thus v_p(k_alpha^(-1))=1.
The exponential test has exactly a primitive formal logarithm.

There are no local p-primary invariants under the same hypothesis,
so integral H¹ has no p-torsion and H²(T_D)=0.
The local Euler characteristic gives its rank two.
Its rank-one point sublattice is saturated, and perfect local
Tate duality identifies the singular quotient with its integral
dual. The primitive point therefore gives the isomorphism O_p^D.
Its finite reduction is still an isomorphism at the full p^k.
Formula(14) divides logarithms only within the lattice pZ_p:
log(P_i) is given modulo p^(k+1), and division by the
valuation-one primitive log(e_p^D) gives a well-defined R-coordinate.

The predecessor explicitly transports the twist class into M_D
as A=u_iota^(-1) iota_*, and transports its Coleman map.
The revised §3 now explicitly proves the local claim first on T_D.
Since iota_* preserves the Weil pairing, it then transports
the first-slot test by A^(-dagger)=u_iota iota_*.
This is the correct map, since

    e(u_iota iota_*x, u_iota^(-1)iota_*y)=e(x,y).

Accordingly O_p=O_p^D A^(-1) and z_D=A z_D^D, so
(e_p,z_D)=d0 remains EXACT. The local point in(14) is
explicitly the inverse-dual-transport of loc_p(b_i).
The geometric map and the retained p-unit scalar preserve
the point lattice. No unit is silently absorbed.
I inspected these exact clauses in revision e67fb3c1.

With this dictionary, b_p=z_D/d0 is the unique C_p(1):
its p singular coordinate is one and its other localizations
are finite. At p, the pairing of b_i=h_i e_p with b_p is h_i.
At i, the pairing is the finite coordinate f_i(loc_i b_p).
All other terms vanish by finite self-duality. Reciprocity
therefore gives f_i(loc_i b_p)=-h_i, exactly(15).
There is no extra quadratic factor in this Q-local calculation.

## Exact zeta cancellation and native/mixed scope

After replacing t_i by t_i+lambda z_D, the old finite difference
changes by -lambda f_i(loc_i z_D)=+lambda d0 h_i.
Its p singular difference changes by -lambda d0.
Since the p term in the evaluator is +h_i q_p(delta_p),
that contribution changes by -lambda d0 h_i.
They cancel at the full R coefficient, including when h_i
is zero or nonprimitive. The argument does not use cancellation
of h_i or of a nonunit. This also verifies the explicit
invariance under this particular actual global correction,
in addition to the abstract invariance under C.

For a native local change at i, the permitted class is
lambda beta_i. Applying C adds lambda b_i. It changes no
old finite coordinate, while at other places its localizations
are finite. This proves the stated native invariance, rather
than assuming that every finite correction is allowed at i.

If both native values vanish, the allowed remaining global
first-lift changes are exactly the corresponding transverse
twist Selmer R-lines. Their mixed changes have the signs
-lambda_q a_l cup b_q-lambda_l a_q cup b_l, obtained by
substitution in the already fixed mixed cocycle.
At the opposite old prime the character a_i has zero local
class, so only the indicated finite cross coordinate remains.
At bad places in the clean range the unramified cups vanish;
at discriminant places the character group has no relevant
cohomology; at p the elliptic H² target is zero.

The unit/ideal distinction for the two old coordinates is
therefore correct. Once they are removed, the remaining
ordinary global H² kernel is dual to S-strict cohomology
of E. It is not annihilated merely because the twist Selmer
group is zero. Nor does a mixed nullhomotopy select its
top Heegner coefficient: addition of the actual Shapiro
Heegner point class preserves the lower coefficients
and native point images. Its raw/standard minus sign
and quadratic corestriction factor are unchanged.

The nonclean section correctly refrains from inverting(6)
or d0. It retains the actual local preimage groups, finite
Selmer kernel and full Smith factors in a finite presentation.
No theorem from the clean-case inverse is extended to those
groups without its hypotheses.

No old mathematical computation or certificate was rerun.
Only this assigned review file was written during the review.
