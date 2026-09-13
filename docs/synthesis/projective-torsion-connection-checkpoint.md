# Torsion-connection obstruction restart checkpoint

Date: 2026-09-12. Agent /root/uniform_witness, GPT-6 Astra/xhigh.
Owned files: projective-torsion-connection-attack.md and this checkpoint.

**Completed and reviewed PASS.** The complete construction is in
[the proof](projective-torsion-connection-attack.md); all seven sections
passed [independent review](review-projective-torsion-connection.md).
Reviewed mathematical revision:
a60a66ce76a0f6c8a5631a96860fd3520e7a8f6b2e77fcc66fac18d254fdff0d.
Subsequent review links and checkpoint updates are editorial.

The parent objective remains full BSD for every elliptic curve over Q.
No full proof, counterexample, uniform splitting bound or Sha-finiteness
result is obtained here. No nonzero Sha class for389a1 is asserted.
All research agents must remain GPT-6 Astra/xhigh. The root owns the
active goal; a null child goal is not cancellation. No old mathematical
scripts were rerun and no additional agent was spawned.

## 1. Exact obstruction: a Cartier-dual differential

For a rigidified n-torsion line L_t and an integral connection ∇0,
write its n-th tensor connection as d+b. The generic finite-order
connection is ∇0−b/n, so its integral obstruction is
o_n(t)=[b] in ω_E/nω_E.

With q=[n] and its canonical frame τ, define χ_t by
τ(x+g)=χ_t(g)τ(x). Pullback of ∇0 is d+a; compatibility of the n-th
tensor trivializations gives na=nb, hence a=b. Translation of an
invariant differential then proves, on the full finite-flat group:
o_n(t)=χ_t*(dlog z) in ω_{E[n]}=ω_E/nω_E.

This fixes the sign by the frame convention. Full group-scheme
descent is retained, including infinitesimal fibers. Pointwise
Galois invariance over a ramified field is not used as descent.

## 2. Ordinary calculation

For G_r=E[p^r], retain the possibly nonsplit sequence
0→G_r^0→G_r→G_r^et→0.
After a finite unramified level extension fix
ι:μ_(p^r)≅G_r^0 and define the exact unit u by
ι*ω_E=u dlog z modulo p^r.

If a(t) in Z/p^r is the image of t in the étale quotient of G_r^D,
then o_(p^r)(t)=(a(t)/u)ω_E.
The kernel is exactly the connected dual subgroup. An étale-generator
point gives a unit obstruction; such points exist over a finite
torsion field. The whole ordinary extension was not assumed split.

## 3. Supersingular calculation and truncation

Scope: good supersingular reduction over an UNRAMIFIED finite
extension of Q_p, p>=3, with v(p)=1. This covers E389a1/Q_p at
each good supersingular prime. No corresponding exact formula is
claimed for arbitrary ramified deformations.

Every nonzero p-torsion parameter has valuation1/(p²−1).
For its cyclic finite-flat closure H, the quotient isogeny q_H has
derivative valuation deg(H)=1/(p+1).
Fargues's order-p formula gives
v(HT_H(t))=deg(H)/(p−1), in a differential module whose annihilator
has valuation1−deg(H)=p/(p+1).

The map E[p]^D→H^D is q_H restricted under principal polarizations,
as fixed by e_p(h,x)=e_(q_H)(h,q_Hx). It is not the dual quotient.
Its actual cotangent pullback multiplies by q_H'(0); no saturated
image or nonunit rescaling is substituted. Thus
v(o_p(t))=1/(p+1)+1/(p²−1)=p/(p²−1)<1.

For a nonzero torsion differential modulo a scalar γ, valuation means
the valuation of a lift strictly below v(γ). Unit changes of an
integral differential basis do not change it. The strict inequalities
above and below prevent truncation from producing zero.

Restriction and inclusion at different levels give, for exact order
p^s in E[p^r],
v(o_(p^r)(t))=r−s+p/(p²−1)<r.
Hence the finite Hodge–Tate map has no nonzero point in its kernel
in this unramified supersingular case.

Fargues's general cokernel bound independently supplies at least one
nonzero obstruction at every good prime p>=3: its target ω/p^r
cannot be killed by an element of valuation1/(p−1)<1. This weaker
argument requires no unramified supersingular hypothesis.

## 4. Integral models and the full torsion packet

Saturate a generic horizontal character line inside any vector bundle
with regular connection on the good regular arithmetic surface.
The quotient is torsion-free; the rank-one kernel is reflexive by
the depth lemma, hence invertible. The connection preserves it
because Ω is invertible and the quotient has no vertical torsion.
Pic(E_R)→Pic(E_K) is injective since the single vertical fiber is
principal. Thus a different unstable or nondiagonal algebra lattice
cannot hide a character line's nonzero obstruction.

The actual rank-n² Poincaré packet from T=f_D⁻¹(O) contains every
n-torsion character difference. Its finite-monodromy connection
therefore has NO regular extension on any Azumaya model at a good
p>=3 dividing n. For389 every possible remaining prime divisor of
a period is good and>=5. The assertion is also true of the Brauer-zero
control with arbitrary n>1; it is not a Sha detector.

The earlier degree-zero construction still supplies regular local
connections with a different generic connection. Regular connection
existence does not imply integral finite-monodromy descent.

## 5. Positive local block and exact global-descent scope

Here n=p^r. Local Selmer data give a finite-flat model of T as a
division fiber. After a finite unramified extension choose a point
in T/(G_r^D)^0 and its coset D_sub. Push its Poincaré family forward.

The resulting rank-p^r block is projectively trivialized by the
ÉTALE dual isogeny of the quotient of the dual elliptic scheme by
(G_r^D)^0. Pullback makes the whole family schematically constant
up to one common line, including nonreduced fibers. Its matrix
connection descends integrally. This is a genuine positive local
construction, not a claim from geometric points alone.

The block's algebra has character support exactly (G_r^D)^0, each
line with multiplicity p^r. Global descent of that algebra, even
after a common line twist of its bundle, would force the support
to be G_Q-stable. For389 the reviewed surjective mod-p image
preserves no such line.

A G_Q-stable subpacket with all differences in the local kernel
must therefore be a singleton. In the supersingular case the zero
kernel gives this already locally. A singleton descending as a
MARKED weight gives a rational point of the fixed T. Descent only
of End(line)=O does not: the scalar algebra is always present.
Moreover fixed-T triviality is stronger than β=0. Equivalence with
β=0 requires allowing the global Kummer adjustment T→f_D⁻¹(P).
All these distinctions are explicit in the proof and reviewed.

## 6. Sources and remaining task

Primary source: L. Fargues, La filtration canonique des points de
torsion des groupes p-divisibles, Ann. Sci. ENS44(2011)905–961,
DOI10.24033/asens.2157.
[Published PDF](https://www.numdam.org/item/10.24033/asens.2157.pdf):
§2 defines Cartier-dual dlog, §2.5 Lemma4 gives the ordinary kernel,
§5.4 Theorem3 gives the general cokernel bound, and §6.5 Lemma9
gives the exact order-p valuation (printedp943, PDFpage40 with cover).
Root independently read the same Lemma9 on p32 of the
[46-page author version](https://webusers.imj-prg.fr/~laurent.fargues/canoniqueHN.pdf).
Scholze–Weinstein arXiv1211.6357v2 Proposition4.3.6 is an additional
check of the integral Hodge–Tate bound over O_C.

This bounded task is finished. On a future explicit continuation,
TC-389 asks for a new uniform splitting construction surviving these
integral conditions, or a rational point of the globally adjusted
character torsor. No p-curvature conjecture was invoked. The
universal BSD objective remains active beyond this completed task.
