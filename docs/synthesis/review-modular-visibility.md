# Coordinator review of the modular visibility argument

Date: 2026-09-12. Result: **PASS for the stated deductions and scope** of
[modular-visibility-attack.md](modular-visibility-attack.md).
This does not certify a proof of BSD or a universal Sha bound.

## Exact sequences and local conditions

The complementary map factors $d-i\pi$ through $B=J/i(E)$ because it
vanishes on E. Surjectivity of q proves both $qj=d$ and $\pi j=0$.
Thus each local and global quotient $C(F)=B(F)/qJ(F)$ is killed by d.
Mordell–Weil makes the global quotient finite.

For Proposition 2.2, a global lift of an everywhere locally trivial J-class
in the kernel to B has local E-classes in the injective connecting images
of $C(\mathbb Q_v)$. Changing the global lift changes these by the image
of one global C-class. This gives exactly the stated obstruction quotient;
it does not give surjectivity onto that quotient. The primary decomposition
commutes with the product because the common exponent d has only finitely
many prime divisors.

For Proposition 3.1, the geometric sequence on n-torsion is exact because
multiplication by n is surjective on geometric E-points. Its boundary for
$b\in B(\mathbb Q)[n]$ maps to the ordinary local boundary in $H^1(E)$.
The local Kummer condition is therefore precisely local liftability of b to J.
The same lift-and-obstruction calculation gives the full finite-level sequence.

For Theorem 3.2, the two actual abelian-variety maps compose in both directions
to multiplication by d. Inverting d on p-primary groups gives isomorphisms
which preserve all local Kummer conditions. No ordinary-reduction or
Sha-finiteness assumption is missing. The conclusion is a direct summand,
not vanishing of the elliptic summand.

## Sources and the concrete counterexample

The coordinator directly inspected:

- [Agashe–Stein, JNT 2002, §4.2 and Proposition 4.2](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf):
  the construction of two independent order-three Sha classes for the stated
  5389 curve is unconditional; the intermediate isogeny has 2-power degree.
- [Cremona–Mazur, physical PDF page 15](https://swc-math.github.io/notes/files/99MazurCremonaV.pdf):
  the modular degree is prime to three. The paper's surrounding Sha-order
  claims are conditional and were not used in place of the later construction.
- [Agashe–Ribet–Stein, Theorem 2.2](https://www.wstein.org/papers/ars-congruence/current.pdf):
  equality of valuations of modular degree and congruence number when
  $p^2\nmid N$. The newform/optimal-quotient setting also makes the dual
  embedding Hecke equivariant, as explained in that source's §4.1.

These support the claimed counterexample to the proposed modular-degree and
congruence-prime bounds. It is explicitly not a BSD counterexample.

The exact J0(389) computation is accompanied by a reproduction command using
integral modular-abelian-variety homology, not the numerical elliptic-curve
modular-degree method. The already published decomposition is consistent with
it. With d=40 and the previously certified zero 2- and 5-primary parts, the
visible subgroup is zero, including any possible divisible part. This indeed
gives an injection of the entire remaining Sha into Sha of J0(389).

## The proposed next criterion

A rank-zero target kills every morphism from a positive-rank elliptic curve:
a nonzero map has finite kernel and would send infinitely many rational
points into a finite group. The winding quotient therefore loses the elliptic
image rather than bounding it.

The bounded-image and Hecke-annihilator criteria pass: apply the retraction
to obtain a fixed integer annihilating Sha(E), then use finiteness of that
integer's Selmer group. Conversely, if Sha(E) has exponent c, an integral
multiple of the elliptic projector followed by c annihilates Sha(J) and has
nonzero E-eigenvalue. The resulting criterion is equivalent to the unresolved
finiteness assertion, not an automatic consequence of the finite congruence module.

No change to the mathematical proofs was required. This review accepts their
maps and limited conclusions; it does not independently rerun the J0(389)
homology computation or every theorem in the cited papers.
