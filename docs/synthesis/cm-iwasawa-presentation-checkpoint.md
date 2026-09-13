# Actual CM two-variable Iwasawa presentation: checkpoint

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only cm-iwasawa-presentation-attack.md and this checkpoint.
Full BSD over Q remains the parent objective. No subagents or old
numerical certificate reruns are authorized for this bounded task.

## Completed assignment and independent review

All nine sections of [the proof](cm-iwasawa-presentation-attack.md)
passed the coordinator's independent [source and deduction review](review-cm-iwasawa-presentation.md).
Reviewed mathematical revision:
407f2915bf07aa46a3e1608c0d4ddab264b9580e9dca5fe891457f5cda826708.
The review checked the corrected cofactor sign and the direct
Rubin-derivative coefficient formula. No correction remains pending.
Completion headers and this checkpoint update are editorial only.

The construction proves perfectness, the actual two-term free model,
free rank-one H¹, the normalized integral determinant basis and its
local Selmer comparison. It retains augmentation Tor and the actual
first ray jets. Freeness does not imply I-divisibility from zero
cohomological augmentation. Nonvanishing, independence, primary
corank two, Sha finiteness and rational BSD comparison are not assumed.

## Material finding: actual perfect presentation and free rank one

Nekovář's full primary Selmer complexes PDF is now cached at
/tmp/cm-presentation-nekovar.pdf (568 PDF pages). Inspected directly:
3.4.2–3.4.4, 4.2.1–4.2.9 and 5.1.1–5.1.2. The global G_K,S
satisfies the finite-cohomology condition and cd_p=2; the actual
rank-one R=Z_p[[X,Y]] coefficient is finite free. Proposition4.2.9
therefore gives a perfect model in degrees0,1,2. Coefficient Koszul
base change and tau acting as−1 give residualH⁰=0; cancelling unit
differentials to a minimal local free model removes degree0.

The actual cyclotomic quotient is R/(X−Y). Its H² is torsion by
the already verified Kato12.4 CM theorem, with the exact Shapiro
and Tate twist. Thus N/(X−Y)N is torsion. Localizing at(X−Y)
and Nakayama forces N to have rankzero overR. The Euler
characteristic gives rankP−rankQ=1 in the actual [P→Q] model.

The rank-one kernel is FREE, with a direct UFD proof: choose a
fraction-field kernel vector, clear denominators and divide the gcd
of its coordinates. Every other integral kernel vector is an R
multiple, since its scalar is integral at every height-one prime.
This primitive vector need not be unimodular; all its coordinates
can still lie in I=(X,Y). Freeness does not remove augmentation Tor.

## Reviewed arithmetic determinant basis and local comparison

The complete nine-section proof is cm-iwasawa-presentation-attack.md.
Its actual finite free model has ranks b+1,b and free rank-oneH¹.
For a primitive kernel vector h, write z=f h and the signed maximal
cofactor vector Delta=c h. Smith normal form gives charN=(c).
Kato15.2(b,c),15.6.2–15.6.4 on the full two-variable tower gives
char(M/Rz)=(c), including at(p): the Hilbert class field isK,
roots have order4, |Delta|=1152(p−1)² is p-prime, andp splits.
Twist and finite branch are the actual reviewed ones. The non-p
conductor primes have nontrivial μ4 inertia surviving modp, so their
local complexes are acyclic on this branch. The fixed Betti vector
has CM coefficient(1±i)/2, a p-unit; its value is still retained.
Consequently u=f/c is an R-unit and eta_z=u epsilon is the EXACT
integral determinant basis mapping to the actual normalized unit.
This does not set u to1 or identify u(0) with a rational real scalar.

The free resolution gives Tor2N=ker(h0:Z_p→P/IP), eitherzero orZ_p,
and Tor1N=kerD0/Z_p h0; the latter may have torsion. Cyclotomic
specialization retains N[X−Y]=S_c/(s), where h(T,T)=s e_c.
Zero cohomological augmentation still does not imply z∈IM.
The exact two coefficient vectors are the actual d_pi,d_barpi.
All first coefficients vanish if the rational Selmer corank is≥3,
because z is a unit times the maximal-minor vector. Thus nonzero
either derivative would force corank2 and finite Sha[p∞], but no
nonvanishing has been proved or computed.

At barpi the actual local perfect complex is free rankone in degree1,
using residual nonanomalous H0/H2=0. Adding its localization row
produces a square ordinary Selmer presentation A. The actual unit
localization F has the exact identity F=(−1)^b u detA, and F∈I² because
both actual derivatives have their unique zero-localization lifts.
The quadratic equations are in the SELMER cone, retaining its local
terms: partial_pi d_pi=F20 j+, partial_pi d_barpi+partial_barpi d_pi
=F11 j+, partial_barpi d_barpi=F02 j+. Here partial is the natural
connecting map; the BKS height Bockstein is MINUS partial. j+ is
explicitly the positive coordinate class[(0,e_L)], not an unstated
canonical purity/triangle convention.

The fixed Coleman coordinate gives c2=iota_p(F20+F11+F02), where
iota_p=O_p(e_L0) is nonzero but not assumed integralunit. All old
k_alpha, delta0, g_p², e_p, c_cmp=(156iOmega_p)^(-1), and p/(2#E(Fp))
factors remain. The local reference C_v remains distinct fromH/2.
The integral determinant basis specializes perfectly to basep
cohomology, but retains H2 and possible extra Selmer directions.
The rational global point frame and real identity CM-Presentation-BSD
are still required as conclusions. No full BSD result is claimed.

The reviewed determinant orientation is: the canonical kernel
cofactor is Delta_j=(−1)^(j+1)detD_hatj, sending
(h wedge lifts of Q-basis)/(Q-basis) to h. With the localization
row LAST, expansion has detA=(−1)^b c*l and F=(−1)^b u detA.
This fixes stabilization compatibility without changing any unit
class, j+=(0,e_L), quadratic identity, or old Kato constant.
The reviewed proof includes that sign everywhere it is used.

The separately assigned theta-elliptic-projection review is now
complete PASS in review-theta-elliptic-projection.md. It required
withdrawal of a nonsmooth single GS metric class and verified its
replacement by actual smooth cutoffs and a convergent pairing limit.
That task and the CM presentation are both complete and reviewed.
No mathematical work or old certificate rerun remains in this bounded task.

## Independent review repair: use the actual Rubin derivative

Root's review requested removal of the unnecessary assertion
that Col(e_L|cyc) is a bounded power-series germ. A defined
augmentation value alone does not prove that statement for
the unrestricted local module or inverse finite-group targets.
That factorization and a(T) have now been WITHDRAWN from §6.

The exact coefficient formula is proved directly on the already
constructed global w_infty. Since z_cyc=T w_infty and L_cyc
is free, loc^-w=(F(T,T)/T)e_L. The proved F∈I² makes this
quotient T-divisible. Consequently the uniquely defined Rubin
derivative is D(w)= (F20+F11+F02)e_L0 tensorT, with a PLUS
coefficient inclusion as in BKS(6.4.1). BKS Lemma6.14 then
gives Col(w) modT²=iota_p(F20+F11+F02)T. Global reciprocity
for this actual normalized class yields the same c2 formula.
There is no asserted arbitrary local Coleman factorization
and no division in an unrestricted inverse group algebra.
All natural/height Bockstein signs, norms and constants remain.

The repair was rechecked against the primary definition after
BKS(6.4.1), Lemma6.14 and its proof, then independently inspected
and passed by root. The main presentation, Rubin all-height-one
comparison and Tor arguments also passed. The withdrawn arbitrary
local Coleman factorization must not be restored on resumption.

## Restart boundary and unchanged global objective

This bounded task is complete. Do not begin a new mathematical
direction from this checkpoint without the coordinator's next
assignment. Any continuation must go beyond the proved presentation,
retain the explicit nonvanishing and CM-Presentation-BSD gaps, and
conclude rationality rather than assume it. The parent universal
BSD objective remains active and unresolved.
