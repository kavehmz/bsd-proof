# Independent review of the signed Heegner–Gysin bridge

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only this review for the assigned audit. No earlier numerical
certificate or mathematical script was rerun.

**PASS for all eight sections of
[the corrected construction](heegner-gysin-bridge.md), including
the irreducible-image extension in §6.2.**
The initial identification of the signed cone class with the
standard positive-divisor Gysin required the convention repair
recorded below. The coordinator applied it both here and in the
predecessor duality note. Those revisions have been inspected.
No pairing, detection or residue formula needs a further change.

Reviewed mathematical revision SHA256:
3e2cc2808e57da5e75f6e3893fdf7e3b2d718a87f32963084cad7ae197f4103b.
Later review/status links and the noted missing typesetting
backslash on the second restriction operator in (3.2) are editorial.

## 1. Actual support and the necessary sign dictionary

At v outside S the coefficient is finite étale and its order is
invertible. Over the strict henselian trait it is constant, units
have n-th roots, and the fraction-field Kummer quotient is valuation
modulo n. This gives the support term V(−1) in degree two and,
after residue-field descent,
H²_v(U,V)=H⁰(F_v,V(−1)). The construction uses this actual
closed support, whose proper inclusion supplies its map to compact
cohomology, retaining the trivializations at S.

The primary support and trace calculations in
[Milne, Arithmetic Duality Theorems, II.1.5–II.1.7](https://www.jmilne.org/math/Books/ADTnot.pdf)
are applicable. The completed-trait excision and cup functoriality
are also explicitly supported by
[Demarche–Harari,1804.03941v3, Proposition2.12 and Lemma4.7](https://arxiv.org/html/1804.03941).
No higher arithmetic-surface purity or K(pi,1) assertion is used.

The sign correction is essential. In a fiber model
F^r=A^r⊕B^(r−1), D(a,b)=(da,f(a)−db), with natural
PLUS projection to A, the canonical connecting map is
β↦(0,−β). To verify it, lift a closed β to a with f(a)=β.
Its usual connecting cocycle da maps to (da,0), and
D(a,0)=(da,β), so its class equals (0,−β).
Equivalently this follows by the standard shifted-cone identification.

The corrected proof now expressly keeps the predecessor's SIGNED
boundary ∂⁺β=(0,+β), and its signed compact trace positive
on that class. Thus ∂⁺=−∂_can and tr_signed=−tr_can,
where the latter trace is normalized positively on ∂_can.
It also defines G_v=−g_v^std, the negative of the standard
positive-valuation Gysin. It no longer calls (0,+δ(v)) the
usual positive-divisor support representative.

These choices are coherent: changing the compact trace and closed
class by the same minus sign leaves their evaluated functional
unchanged. Perfectness, images of boundary subgroups and the
relevant zero tests are unaffected. This audit does not silently
erase the distinction between a signed convention and canonical purity.

## 2. The excision chain maps give the claimed signed formula

With A for U', O for the trait, K for its fraction field and L
for the old S terms, the actual compact model has differential
$$D(a,o,h,s)=(da,do,\operatorname{res}_v a-
\operatorname{res}_v o-dh,\operatorname{res}_S a-ds).$$
The use of res_A−res_O is fixed by the homotopy fiber giving
ordinary cohomology on U.

I independently substituted both maps:
the local support map (o,b)↦(0,o,−b,0), and
the compact extension-by-zero map
(a,s,l)↦(a,0,l,s). Both commute with the displayed differential.
Thus the signed support representative (0,β) goes to
(0,0,−β,0), while j_!∂⁺β goes to (0,0,+β,0).
This proves G_v(y)=−j_!∂'_vβ_y in the now explicitly signed
notation. It concerns actual support and extension-by-zero maps;
perfect duality is not used to choose a representative afterward.

## 3. Independent cup-order and Frobenius calculation

Let r^n=π_v and let c(g)∈{0,…,n−1} be the continuous
integer lift of an unramified R-valued character χ. For the
multiplicative cochain q(g)=r^c(g),
$$dq(g,h)=\delta(\pi_v)(g)^{c(h)}
\pi_v^{(c(g)+c(h)-c(gh))/n}.$$
The first factor is exactly δ(π_v) cup χ in the order
declared in the paper. Consequently its Brauer class is the
negative of π_v to the integer Bockstein of χ/n.

By [Milne,I.1.5–I.1.6](https://www.jmilne.org/math/Books/ADTnot.pdf),
valuation identifies the invariant of that unramified cyclic
class with χ(F_v)/n, using arithmetic Frobenius. Hence
inv_v(δ(π_v) cup χ)=−χ(F_v)/n. This independently gives
the second sign, without assuming the desired final pairing.

For y:μ_n→V, the functional λ_y defined using
e_n(y(ζ),x)=ζ^λ_y(x) is Galois equivariant to the trivial
module R. It therefore kills (F_v−1)V. Since z extends
over U, its localization at v is unramified. The local cup of
β_y with z is precisely δ(v) cup (λ_y∘z); the pairing order
is unchanged. Combining this negative local invariant with the
negative support-to-boundary relation gives
$$\mathscr P(z,G_v(y))=\lambda_y(z_v(F_v))/n.$$
This is the declared signed pairing, and its value agrees with
the standard trace paired with the standard positive Gysin.

## 4. The factor two and the raw Heegner normalization

The fresh-prime conditions are congruences:
a_v≡0 and v≡−1 modulo p^k. No exact equality a_v=0 for
the rational elliptic curve is inferred from Chebotarev.
They give F_v²=1 on V, with free rank-one eigenspaces.
The source λ_v is an R-ISOMORPHISM on V_v⁺; an arbitrary
zero functional would not give the claimed tests.

The Weil pairing identifies its extension by zero on V_v⁻
with a unique y_v∈H⁰(F_v,V(−1)). Inertness in K gives
an unramified quadratic local extension. Directly,
c(F_v²)=(1+F_v)c(F_v), and applying λ_y multiplies its
value by two. Thus the finite toric functional in the reviewed
reciprocity note pairs with 2G_v(y_v), exactly as (5.1) states.
The factor two is a unit and is distinct from the separate
raw-to-standard two-prime scalar u₂=−1 and its tensor generators.

## 5. Lawson–Wuthrich removes full image in the stated Q-range

I inspected the actual primary
[Lawson–Wuthrich,1505.02940v2, Lemmas3–4](https://arxiv.org/pdf/1505.02940v2),
including their proofs on PDF pp.3–4. Its arXiv header says
23 September2015 and the internal manuscript date is27 June2018.
Lemma4 applies because the base is Q, the cyclotomic determinant
is surjective, and residual irreducibility rules out containment in
a Borel. It supplies a nontrivial residual scalar.

Lemma3 then proves H¹(G_k,E[p^k])=0 at EVERY k. Its induction
uses the action on the successive kernels in Mat₂(F_p):
the residual scalar acts trivially by conjugation on those kernels
and nontrivially on E[p]. The relevant equivariant Hom groups
vanish. No lift of the residual scalar to a central scalar matrix
at all higher levels is presumed. The reducible exceptional cases
of the paper are not imported.

The new stable-submodule argument also checks without matrix units.
For nonzero W⊂R² stable under the residual-irreducible image,
choose minimal valuation t. Its image modulo p^(t+1) is a
nonzero invariant subspace and hence all p^tV/p^(t+1)V.
For M=p^tV/W this says pM=M; iteration or Nakayama gives M=0.
Thus W=p^tV. Semisimplicity in characteristic p is not used.

## 6. Exact-order detection for every global class, then generation

The restriction of any nonzero z∈H¹(U,V) to L=Q(E[p^k])
is injective on its cohomology class by the preceding H¹
vanishing. Over L it is a homomorphism, whose stable image W
therefore has exponent equal to the exact order p^s of z.
The stable-submodule lemma gives W=p^(k−s)V.

The finite cocycle field L_c has Gal(L_c/L)=W, a p-group.
K cannot lie in L because a prime dividing its discriminant D
ramifies in K but not in L. It cannot lie in L_c either:
otherwise LK/L would be quadratic inside a p-extension.
Hence K and L_c are disjoint over Q.

For an actual complex conjugation τ, c(τ) is in V_τ⁻.
Take w∈p^(k−s)V_τ⁺ of exact order p^s. Disjointness
allows h fixing LK with c(h)=w. The element γ=hτ has
the required K action and torsion representation, and
$$c(\gamma^2)=(1+\tau)(w+c(\tau))=2w.$$
Conjugating γ acts invertibly on this squared translation because
ρ(γ²)=1, so its order and the plus-eigenspace condition survive
the Frobenius-conjugacy ambiguity. Chebotarev gives infinitely many
fresh primes avoiding the whole specified finite set.

This argument applies to EVERY H¹(U,V) class, not just the
Heegner class. Any fixed isomorphism λ_v preserves the detected
order. Thus the signed G_v(y_v) have zero common annihilator.
Finite perfect duality makes their span all H²_c(U,V); finiteness
gives a finite generating subset. The same holds in the strict
Selmer and defect dual quotients. It supplies no uniform size
bound or rank-sensitive vanishing.

## 7. The residue presentation retains all specified S data

For a tuple y_v use β_v=y_vδ(v), and let α be a SPECIFIED
tuple of S-local H¹ classes. In the repaired signed model,
the difference of the Gysin sum and ∂⁺_Sα is
(0,0,−β,−α). It is a boundary precisely when closed a,o
and cochain homotopies h,s satisfy
$$\operatorname{res}_T a-\operatorname{res}_T o-dh=-\beta,
\qquad \operatorname{res}_S a-ds=-\alpha.$$
Then b=−[a] has exactly the positive tame residues y_v
and S-localization α. Conversely, those properties of b let
one choose the unramified local classes and homotopies and
produce the displayed boundary with a=−b. This proves both
directions of the iff statement; it is not merely a relation
modulo unspecified local choices.

Taking α=0 describes the kernel of the signed Gysin sum.
Allowing α in the precisely declared A_S describes its kernel
after quotient by L_m=∂⁺_S(A_S). At the old primes ell,q,
A_S uses full local H¹, while at the other inverted primes
it uses point Kummer groups; odd-p real terms vanish.
These are exactly the dual annihilator conditions from the
strict-Selmer predecessor, not a pairing only on Sha.

The finite generating set therefore yields the exact presentation
B_T→⊕W_v→H²_c(U,V)/L_m→0. Its first term and image remain
arithmetic cohomology with actual local constraints. The
presentation does not compute that image from analytic rank five.

## 8. Scope after the repair

The corrected note gives actual signed closed-support classes,
their exact arithmetic evaluations and their global residue
relations, and it removes full-image assumptions from detection
over Q in the original irreducible O5 range.

It does not show that the raw Heegner class vanishes on the
generators. Its annihilation of the residue relations is the
already known descent to the strict dual quotient, not zero
on the entire generating module. Gysin-TP5 and universal BSD
remain unresolved. The sign dictionary must remain explicit in
future reuse; replacing the signed G_v by the standard positive
Gysin without also changing the trace would change the formula.
