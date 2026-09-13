# Signed Heegner Gysin bridge restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
The [full construction](heegner-gysin-bridge.md), including §6.2's
irreducible-image extension, passed the complete
[independent review](review-heegner-gysin.md).
Reviewed mathematical revision:
3e2cc2808e57da5e75f6e3893fdf7e3b2d718a87f32963084cad7ae197f4103b.
Subsequent status links and one missing LaTeX backslash are editorial.

## Actual comparison and the sign correction that must survive

Keep original U=Spec Z[1/(Np|D|m)], its exact complement S, V=E[p^k],
the raw two-prime class kappa_Q and its strict finite Selmer condition.
No local condition or K(pi,1) hypothesis is silently replaced.

For natural PLUS projection and D(a,b)=(da,f(a)-db), the canonical
connecting map sends beta to (0,-beta). The predecessor FIXED instead
the SIGNED map partial^+(beta)=(0,+beta), and a positive invariant
trace on that signed map. Hence partial^+=-partial_can and its trace
is correspondingly the negative of the canonical-boundary-normalized
trace. This is now explicit in the predecessor proof/checkpoint too.

G_v is SIGNED: G_v=-g_v^std, minus the standard positive-valuation
Gysin. Its local support representative is (0,+beta), beta=y delta(v).
The excision model has D(a,o,h,s)=(da,do,res_v a-res_v o-dh,res_S a-ds).
The support map takes (o,b) to(0,o,-b,0); open extension sends
(a,s,l) to(a,0,l,s). Thus G_v=-j_!partial^+_v beta.
The local cup delta(v) cup chi has invariant -chi(Frob_v)/p^k.
Together these signs give the EXACT retained formula

    P(z,G_v(y)) = lambda_y(z(Frob_v))/p^k.

Do not call (0,+beta) the standard positive-divisor representative.
Changing both the trace and Gysin to their standard versions leaves
the evaluated functional unchanged, but changing only one reverses it.

At fresh inert v with a_v congruent0, v congruent-1 modulo p^k,
choose lambda_v an R-ISOMORPHISM on the plus eigenspace and its Weil
dual y_v in H0(F_v,V(-1)). Quadratic unramified restriction gives

    P(kappa_Q,2G_v(y_v)) = psi_(v,k)(D_(v,m))/p^k
                        = psi_(v,k)(e_tD_(v,m))/p^k.

This factor two is separate from the raw-to-standard u_2=-1 scalar.

## Full-image restriction removed, with primary input verified

Theorem6.3 proves full-p-power exact-order detection and generation
under the ORIGINAL irreducible O5 hypotheses over Q. No full GL2
hypothesis is needed. Primary Lawson-Wuthrich1505.02940v2 Lemmas3-4
(full proofs read by root and reviewer) give H1(G_k,E[p^k])=0 for allk
when E[p] is irreducible over Q. This is a cited theorem, not a new
homothety result. No uniform central lift is assumed.

The actual translation submodule W has minimal valuationt. Its leading
mod-p layer is a nonzero invariant subspace, hence all by irreducibility;
Nakayama gives W=p^tV. Exact class orderp^s forces t=k-s. Ramification
keeps K outside the torsion field and its further p-group cocycle field.
The same h*tau element has square translation2w, preserving exactorder
under Frobenius conjugacy. Chebotarev detects EVERY H1(U,V) class.
Finite perfect duality makes the signed G_v span all H2_c; a finite
subsetT suffices. There is no uniform bound onT or onSha.

## Actual residue presentation and exact open task

Positive tame residue is normalized by res(y delta(v))=y. For actual
b in H1(U\T,V), the signed cone proves

    sum_v G_v(res_v b) = partial^+_S(loc_S b).

More strongly, sumG_v(y_v)=partial^+_S(alpha) for a SPECIFIED alpha
iff some globalb has residue tupley and S-localizationalpha. Both
directions were checked from cochain equations; local trivializations
are retained. Let A_S be finite Kummer away fromell,q and fullH1 at
ell,q, and B_T={b:loc_S b inA_S}. For generatingT,

    B_T -> direct_sum_T H0(F_v,V(-1)) -> H2_c(U,V)/L_m ->0

is exact. It presents the entire strict finite Selmer dual, retaining
point directions. Its relation image is not computed fromanalyticrank5.

Gysin-TP5/LR-TP5 remains the vanishing of kappa_Q on these generators,
equivalently the actual finite toric values. Being zero on the known
residue relations only lets the functional descend; it does not make
it identicallyzero. The parallel level-Nv construction identifies
that same obstruction in the reduction of an actual trace-zero point
B2; see heegner-toric-vanishing-checkpoint.md. Future work must obtain
rank-sensitive information on those actual values. Global full BSD
is still neither proved nor disproved.
