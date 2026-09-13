# Independent review of the Hecke–Brauer construction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed file: [Hecke–Brauer attack](hecke-brauer-annihilator-attack.md),
all nine sections. Verdict: **PASS for the stated deductions**. No
annihilator or finiteness theorem is obtained by this note.

## Source checks

The reviewer fetched González-Avilés,
[J. Math. Sci. Univ. Tokyo 10 (2003), 391–419](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms100207.pdf).
The setup is a regular connected surface proper over the indicated open
arithmetic base. Equations (5)–(6), printed p.401, give the generic/local
Picard–Brauer sequences. Lemma 2.2(b), printed p.402, gives the model
restriction kernel without the main theorem's additional hypothesis on
infinitely divisible Sha. The local pairing at pp.398–399 explicitly
uses the norm quotient at archimedean places. These exact statements,
rather than the paper's order formula, are sufficient here.

The reviewer also fetched McCallum,
[Brauer Points on Fermat Curves, August 2000](https://math.arizona.edu/~wmc/Research/BrauerFermat.pdf),
§2, printed p.4. It states the compatibility between normalized Brauer
evaluation and the local Tate pairing used in Proposition 8.1. The
finiteness hypothesis in a different theorem in its introduction is not
a premise of this identity.

Finally, [Ribet–Wake, PNAS 119 (2022), e2210032119](https://pmc.ncbi.nlm.nih.gov/articles/PMC9565053/)
§§2.2 and 2.5 were checked. Lemma 2.4 uses an injection of rational
torsion into reduction. The attack correctly declines to transfer that
injection to locally trivial Brauer classes.

## Reconstruction of the deductions

1. **Normalization and all local conditions.** A rational point splits
   the constant Brauer group and the degree part of the geometric Picard
   group. Under the resulting normalized identification, a Sha class is
   locally a constant class evaluating to zero at the point, hence is
   locally zero. Conversely, all local restrictions zero imply that the
   global constant evaluation is zero by Brauer–Hasse–Noether. Thus the
   strict group in (1.3) is the entire Sha group, with no quotient by its
   divisible subgroup.

2. **Finite coefficients, including even coefficients.** In the
   Hochschild–Serre spectral sequence the geometric degree class lifts
   via the rational point's line bundle. A section also splits pullback
   from base-field cohomology in every degree. Therefore differentials
   entering the base row vanish, including the possible differential
   from bidegree (1,1) to (3,0). There are no other differentials affecting
   (1,1). Removing the base summand from the geometric restriction kernel
   gives exactly the asserted H¹ of J[n]. Kummer classes of degree-zero
   line bundles have zero evaluation at the point because a line bundle
   on a field has zero first Chern class. This verifies (2.2), and the
   local Kummer conditions give (2.4). No vanishing of H³(F,μ_n) at the
   real place has been assumed.

3. **Transfers.** Pullback is the Picard map E→J; norm is J→E. After
   quotienting constants their actions on H¹ are these same maps.
   Subtracting the value at the base point realizes this quotient action
   on normalized representatives. Restriction–corestriction gives [d],
   and gives zero correction on the strict local kernel. This verifies
   both the orientation and the scalar in (3.1)–(3.2). Constants are
   preserved by correspondence actions, so inserting normalization
   between two such actions does not change their induced composition.

4. **The proposed zero tests.** A strict class evaluated at any closed
   point becomes zero in every completion of the residue number field;
   its evaluation is therefore zero globally. Correspondences factoring
   through points do not detect the Jacobian component. Independently,
   T₂−T₃+1 has eigenvalue 3−4+1=0 on constants and geometric degree, but
   eigenvalue −2−(−2)+1=1 on the elliptic image. This remains an identity
   on the image of pullback when a finite-coefficient direct summand is
   unavailable at primes dividing d.

5. **Cocycle identity.** Direct expansion gives
   g z(g⁻¹σg)=z(σ)+(σ−1)z(g). The defect of coefficient multiplication
   alone is (gσ−σg)z(τ). The coefficient relation supplied by
   Eichler–Shimura consequently does not give the asserted global
   cohomological identity by inner conjugation. The attack makes no
   stronger impossibility claim about constructing another homotopy.

6. **The arithmetic model and real place.** The exact kernel theorem
   identifies its real-trivial Brauer subgroup with the strict generic
   group. For an elliptic curve with a rational point on the second real
   component, properness extends that point and O to integral sections.
   Both evaluations lie in Br(Z)=0. The norm image of E(C) is connected,
   and contains the doubled real identity component, which is that whole
   component. Thus the nonidentity point generates the norm quotient;
   its zero pairing kills the normalized real class. The remaining
   constant is killed by evaluation at O. This retains the 2-primary
   information. On 389a1, x=0 belongs to the bounded component using the
   three stated root brackets, so the criterion applies.

7. **Image and final gap.** The previously proved vanishing of the 2-
   and 5-primary Sha groups makes [40] an automorphism of the remaining
   torsion group. Pullback is injective, norm is surjective, and the
   image of their composition is exactly the asserted copy of Br(𝓔).
   Equation (9.2) would annihilate its n-torsion for every n because the
   finite Selmer sequence surjects onto that torsion. A fixed nonzero
   multiple would bound the group's exponent; its bounded torsion is
   finite by finite descent. Neither existence statement is proved.

No mathematical repair was required. The generic-fiber action extended
to the identified Brauer subgroup is correctly distinguished from an
unconstructed integral cochain action. The source hypotheses and the
remaining global line-bundle construction must be preserved on reuse.
