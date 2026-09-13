# Projective monodromy restart checkpoint

Date: 2026-09-12. Agent /root/uniform_witness, GPT-6 Astra/xhigh.
Own only projective-monodromy-attack.md and this checkpoint.

The parent objective remains full BSD over Q for every elliptic curve.
This bounded continuation of TS-389 tests finite projective monodromy of
the actual stable twisted bundle and its extension on the fixed regular
389a1 model. No old mathematical scripts are to be rerun; no new agents.

Reviewed inputs: twisted-sheaf-lifting-attack.md and both reviews construct,
for each β∈Br(𝓔)=Sha(E) of periodn, a stable twisted(n,1) bundleV and
AzumayaA=EndV of degreen; generic index=n. Its actual twisted K0 isZ4,
with numerical Euler determinantn². Root's reviewed model hasπ1(𝓔)=1.
None of these statements is a uniform splitting bound.

Completed construction sequence:
1. Prove geometric projective trivialization after[n] using the n²
   self-twists of a stable(n,1) bundle. Compute the finite Heisenberg
   matrices/commutator and intrinsic projective monodromy.
2. Use the ordinary stable V_n(O), which exists for every n even whenβ=0,
   as a control. A nontrivial finite projective monodromy does not measureβ.
3. Track the Galois descent cocycle ofA relative to ordinaryEnd(V_n(O)):
   expected E[n]-torsor with local Kummer conditions, rather than local
   triviality as an E[n]-torsor.
4. Extend[n] over the good abelian scheme away from389; it is finite flat
   of degreen² everywhere there, étale only where n is invertible.
   At389 track the Tate/nodal model instead of assuming a finite étale
   cover of the entire proper arithmetic model.
5. Construct the induced projective/adjoint connection from the finite
   étale cover where available and examine its integral extension,
   including primes dividingn. π1(model)=1 applies only to covers
   actually étale on that complete model.

Root separately handles étale K-theory/Bott comparison; do not duplicate.
The first proof checkpoint is saved before further source research.
All new deductions passed independent coordinator review in
`review-projective-monodromy.md`. The proof's mathematical body was
reviewed before the editorial PASS link was added.

## Reviewed material results

1. Geometric End(V)=⊕M over all n-torsion degree0 lines M. Proof uses
   stable self-twists and trace orthogonality; trace of inverse components
   is n times a nonzero scalar, so this is characteristic0 (or p∤n).
   Thus[n]*End(V) is geometrically a trivial algebra. H0/evaluation atO
   descends it overQ as a constant algebra, and the O-framing makes it
   M_n(O_E). This is an actual generic finite étale trivialization of
   degree n², with faithful E[n] projective action/Heisenberg commutator.
2. Aut_E(End(V_n(O)))=Pic0(E)[n]. Comparing Aβ with this ordinary
   control gives a concrete Galois form torsor η∈H1(Q,E[n]); its image
   is±β, and local Selmer data putη_v in local Kummer images. They do
   not forceη_v=0 as a finite torsor. Globallyβ0 meansη is globalKummer.
3. On U=SpecZ[1/n389], ordinary stableV_n(O) extends by successive
   generator extensions, remaining stable on all smooth fibers.
   Its projective automorphisms give finite étaleE[n]. The unramified
   form torsorη extends overU; twisting gives an actual integralAβ model
   there, trivialized by[n], and a relative projective connection by
   finite étale descent ofd. No claim that this extends acrossn389.
4. Strong exact connection obstruction at p|n (p good): for ANY ordinary
   rankn vector bundleW of deg≡1modn, trace End(W)→O descends through
   End(W)/O incharp. The projective Atiyah class maps to c1(detW),
   whose Serre/residue trace isdegW=1modp. Hence no projective connection.
   This needs NO stability. Any Azumaya extension of genericAβ to the
   good Zp-model is Brauer-trivial there (localβ0 plusregularinjection),
   hence End(W), and its degree remains≡1modn. So choosing an unstable
   extension cannot remove the obstruction. Same phenomenon forβ0control.
5. Multiplication[n] on the good abelian scheme is finite flatdeg n²,
   with relative differential cokernel(O/n)ω, hence nonétale atp|n.
   At389, v(q_T)=1 and n isprime to389. q_T^(1/n) has ramificationn;
   inertia onE[n] is the full tame transvection. There is no finite étale
   extension of this faithful projective cover overthewholemodel.
6. The finite-monodromy degree0 alternative is now constructed in§9:
   degree-nD givesn-coverf_D:C→E, c↦O(nc−D), degree n². The finite
   E[n]-torsorT=f_D⁻¹(O) supplies a rank-n² degree0 Poincaré bundle.
   Its [n]-pullback algebra is constant split; the geometric representation
   is a sum of characters, with zero commutator. Its commutative theta
   extension has weight-one character torsor exactlyT (viaPoincaré/Weil
   duality), proved by the affine Galois action on its weight labels.
   Changing the rational fiber adds a globalKummer class. Local rational
   points supply local adjustments, not the missing globalone.

Verified sources: Brion arXiv1104.0818v4, Props3.1/3.9 and§2.3,
all used only inchar0 or p∤n (paper explicitly excludesp|n in§3);
Kuhn, The Atiyah class on algebraic stacks, Example4.10, DOI
10.1017/fms.2024.109, trace–determinant identity (also directČechproof);
Stacks0BFG for multiplication degree; reviewed exceptional-prime note
already contains the Tateuniformization/v(q)=1 input. No scripts rerun.

## Full proof saved and independently reviewed

projective-monodromy-attack.md now has §§1–10 and the completed degree0
repair requested byroot. New positive local proof at EVERYgoodp:
choosec0∈C(Qp), integralclosureA of degree-nD, a=D−c0∈E(A).
Its Poincaré line has relative degree0, and its full line Atiyah class
vanishes in H¹(E_A,Ω)=A (line trace is identity; generic class0 and
torsion-freecohomology suffice). Pick an integral relativeconnection and
push alongfinite-flatA/Zp withprojectionformula. This supplies the actual
rank-n degree0 bundle andintegralendomorphismconnection withoutaveraging
or1/n, evenwhenA isramified. It is not an inference fromvectortracezero.

An arbitrarydegree-nD can have nontorsion conjugatedifferences; those
preclude finiteprojectivemonodromy for ANYconnection. The n-coverfiberT
variant aboveforces torsiondifferences buthasrankn²/coverdegreen².

Exact integral finite-orderconnection condition (§9.3): for
t∈E[n](A), chooseintegrallift t̃∈E^natural(A); n t̃=b∈ω(A).
The unique generic n-torsionlift is t̃−b/n and extends iff
[b]=0 inω(A)/nω(A). Equivalently if∇0 isanyintegralconnection on
the torsionline, itsnthpowerisd+b, and∇tor=∇0−b/n. Pointwise checks
must still retain full descent overA⊗_R A, includingnilpotents;
Galoisinvariance overa ramifiedfield is not enough. A regularconnection
is not automatically a crystalline stratification or anétale localsystem.

Source Cais arXiv0909.1849v1 Theorem1.2 verifies the relative Picard
connection/universalextension interpretation onregularsmoothmodels,
and onregularsemistablemodels withgeometricallyreducedfiber usingthe
relative dualizing sheaf. At389 andramificatione, Tatecomponent is
v_L(u)mod e inZ/e. Keep that identity-component obstruction and
the dualizing/log-node differential; do not substitute smooth-familyΩ.

Exact next mathematical target: PM-389 asks for a global Kummer
adjustment of T or a uniform splitting degree, with an actual integral
or étale comparison before invoking π₁(model)=1. The local connection
construction and the integral torsion-lift criterion are usable inputs;
neither supplies this global adjustment. No such uniform bound or full
BSD proof/disproof has been obtained. Independent review is complete.
