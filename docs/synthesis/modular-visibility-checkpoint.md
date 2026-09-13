# Modular visibility restart checkpoint

Date: 2026-09-12. Agent: `/root/uniform_witness`, GPT-6 Astra/xhigh.

Current status: completed and [coordinator review PASS](review-modular-visibility.md).
The initial actions and inventories below are historical snapshots.
The current unresolved construction is H389 at the end, refined to
HB-cycle in `hecke-brauer-annihilator-attack.md`.

Owned files only:

- `docs/synthesis/modular-visibility-attack.md` (completed and reviewed).
- `docs/synthesis/modular-visibility-checkpoint.md` (this checkpoint).

The parent objective is full BSD for every elliptic curve over Q. This bounded
task tests whether optimal embeddings into modular Jacobians, modular degree,
congruence primes, and winding quotients can give a uniform Sha bound. Neither
the task nor a result on 389a1 constitutes completion of the parent objective.

Continuity files read: `AGENTS.md`, `research-state.md`, `research-ledger.md`,
and `final-report.md` under `docs/synthesis/`. Goal tool is null in this
subagent scope; coordinator informed. The worktree has extensive uncommitted
research and must not be reset or cleaned. Live inventory contains root,
higher_period_integrality, odd_rank_bridge, and uniform_witness.

Initial next actions:

1. Derive global/local H^1, finite-level Selmer, and Sha maps for
   `0 -> E -> J -> B -> 0` and a modular retraction with composite `[d]`.
2. Verify primary visibility theorems, especially what is meant by classes
   visible in a specified J and any claims concerning modular-degree primes.
3. Compute J_0(389)'s exact newform dimensions and modular degree if it tests
   whether rank-zero complementary factors could kill the surviving image.
4. Test the full-Sha-to-visible-kernel implication. Push a more precise Hecke
   projector/winding quotient argument and isolate a p-independent residual
   map rather than repeat the prior abstract product-Zp countermodel.

## Material progress

1. For an optimal parametrization `pi:J0(N)->E`, the dual embedding `i`
   satisfies `pi*i=[d]`, where d is modular degree. With `q:J->B=J/iE`,
   `d*id_J-i*pi` factors as `j*q`, and `q*j=[d]`, `pi*j=0`.
   Therefore all finite p^k Selmer groups and p-primary Sha groups split
   as E plus B whenever p does not divide d; local Kummer conditions split
   too, including at p and bad places. Full proof is being written.
2. The visible group is the KERNEL of Sha(E)->Sha(J), not its image. It is
   killed by d. Away from d this gives an injection/direct summand, not vanishing.
3. Exact Sage modular-abelian-variety computation succeeded:
   J0(389) has simple-factor dimensions 1,2,3,6,20. The elliptic factor has
   modular kernel invariants [40,40] and modular degree 40. Reproduce with:

   ```sh
   DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python -c 'from sage.all import *; D=J0(389).decomposition(); print(D); A=[a for a in D if a.dimension()==1][0]; print(A.modular_kernel()); print(A.modular_degree())'
   ```

   Do NOT use E.modular_degree() here: it defaults to sympow's heuristic
   numerical algorithm and attempted an unwritable ~/.sympow cache. No
   numerical modular degree from that failed call is used. The modular
   abelian variety method uses exact integral homology and finite kernels.
4. Combining d=40 with previously proved Sha(389a1)[2-infinity]=0 and
   Sha(389a1)[5-infinity]=0 proves Vis_J0(389) Sha(389a1)=0. Thus the full
   remaining Sha injects into Sha(J0(389)); this fixed visibility route sees
   none of it. Root was informed.
5. Primary Agashe–Stein JNT2002 §4.1 already records the decomposition and
   central-value vanishing at factors of dimensions1,2,3,6; dimension20 is
   rank zero. Their Proposition4.1 instead makes rational points of 389a1
   produce visible 5-torsion in Sha of the dimension20 factor.
6. Actual counterexample to the proposed modular-degree bound: AS2002 §4.2,
   Proposition4.2 proves nontrivial Sha[3] (indeed subgroup( Z/3)^2) for the
   curve y²+xy+y=x³-35590x-2587197 of conductor5389. Cremona–Mazur record
   its modular degree prime to3. Need finish precise source verification;
   do not rely on AS's earlier BSD-predicted order9 as the proof of existence.

## Primary sources read / next source checks

- Agashe–Stein, *Visibility of Shafarevich–Tate groups of abelian varieties*,
  JNT97(2002)171–185, DOI10.1006/jnth.2002.2810:
  https://wstein.org/papers/visibility_of_sha/jnt_version.pdf
  Definitions1.1/1.2, Proposition1.3, Theorem3.1, Propositions4.1/4.2.
- Cremona–Mazur, *Visualizing elements in the Shafarevich–Tate group*:
  https://swc-math.github.io/notes/files/99MazurCremonaV.pdf
  Search-engine extracted paragraph states5389A1 degree prime to3, but
  fetched PDF may be an older23-page version without that paragraph.
  Fetch published version before treating this source step as complete.
- Agashe1999, https://www.math.fsu.edu/~agashe/math/craseng.pdf:
  winding quotient is rank zero; its invisible examples1091/1429 assume
  BSD and must NOT be used as unconditional examples.

## Proof attempt completed and coordinator-reviewed

The full argument now exists in `modular-visibility-attack.md`, with on-page
proofs and explicit remaining statements. Completed additions:

- Global/local visible quotient C(F)=B(F)/qJ(F), d-torsion and finite over Q.
  The actual Sha sequence includes the obstruction
  product_v C(Q_v)/loc C(Q), not automatic exactness at Sha(J).
- Finite-n Selmer kernel is Delta_n(U_n), where
  U_n=B(Q)[n] intersect intersection_v qJ(Q_v), modulo q(J(Q)[n]).
  A full middle-kernel obstruction sequence is proved in Proposition3.1.
- Exact splitting at every p not dividing d includes local Kummer conditions
  at bad and p-adic places, and possible divisible Sha parts.
- Verified Cremona–Mazur preprint DOES contain the5389 degree claim at
  printed p15/PDF page15, §4 (“kernel of multiplication”); an initial direct
  find inexplicably returned no match, but subsequent find+open obtained the
  full paragraph. The old Sha-order9 prediction is distinguished from AS2002's
  subsequent unconditional subgroup( Z/3)^2 proof.
- Agashe–Ribet–Stein Theorem2.2 and Lemmas4.2–4.4 verified from
  https://www.wstein.org/papers/ars-congruence/current.pdf (18-page author
  version); publication DOI10.1007/978-1-4614-1260-1_2. For optimal E,
  modular degree divides congruence number, their ratio has prime support only
  where p²|N, and projector denominators are these two numbers.
- Exact389 lratios: dimensions1,2,3,6 give0; dimension20 gives51200/97 in
  Sage's homology-lattice normalization. Only zero/nonzero flags are used.
  Exact congruence lattice also gives40 independently of the modular kernel.
- T2 polynomial evaluations at E's eigenvalue-2 are2,-2,-1,-14500 on the
  dimensions2,3,6,20 factors. Thus the product polynomial gives -58000 e_E,
  while the full Hecke algebra has numerator40 e_E. Single-operator methods
  artificially introduce29; removing that denominator still does not kill Sha.
- Any positive-rank E has Hom_Q(E,A)=0 for every rank-zero A. Hence winding
  and all rank-zero targets kill E already geometrically and cannot detect
  its residual Sha image.
- A Hecke operator t killing Sha(J) with nonzero E-eigenvalue would give an
  explicit uniform annihilator d*a_E(t). Existence of such a t is proved
  equivalent to Sha(E) finiteness (Proposition8.3), so it is a genuine missing
  input, not supplied by the finite congruence module.

Exact next unresolved statement H389: Theta=40 e_E=i*pi must kill all
everywhere locally trivial J0(389)-torsor classes. This is equivalent to
Sha(389a1)=0 using the completed2/5-primary results. No proof is given.
The general objective remains open. The coordinator reviewed the new exact
sequences and deductions; the review and its scope are linked above.

Root owns the global research state/ledger updates; this agent edited only
its two owned files. No new subagents, model changes, quota changes, or
unrelated certificate reruns occurred.
