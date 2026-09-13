# CM regulator tensor attack: checkpoint

Date: 2026-09-12. Agent: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Owned files: `cm-regulator-tensor-attack.md` and this checkpoint only.

## Objective and current state

Investigate an actual common integral CM theta/elliptic-unit tensor
whose realizations give both the cyclotomic second coefficient and
the full Mordell–Weil regulator for one rank-two CM curve in Banwait,
arXiv:2609.08431v1. Work with their normalized quotient so that
regulator nonunits are permitted. The universal objective remains full
BSD over Q; a result for one test curve would not complete it.

The coordinator's `coherent-moment-attack.md` and current
`research-state.md` have been read. Preserve its proved distinction:
one fixed primitive global object and global mu=0 do not imply that
every leading realization is a unit. The actual realization index and
regulator tensor must be identified.

Banwait2609.08431v1 has now been read at Theorem B, §§2.1–2.6,
3.1–3.3, 6.1–6.3, the curve table, and §13. Chosen test curve:
E: y²=x³+39x, with P=(3,12), Q=(27,144), torsion2, Tamagawa product8,
N=48672, and the source's excluded set contained in{2,3,13}.
Its regulator is allowed to be a nonunit (the source records that
phenomenon atp=5). No finite-prime theorem is the objective of this task.

Primary related sources read:

* Bannai–Kobayashi, math/0610163v4: reduced theta, its relation to
  sigma, torsion translations and p-integral expansions, Katz measures.
* Bannai–Furusho–Kobayashi,0807.4007v2, Theorem1.2/Definition5.1:
  Coleman second Kronecker limit formula
  K_0^col(0,z,1)=−log_p theta(z)−(1/12)log_p Delta_Gamma.
* Stein–Wuthrich published §4.1: canonical sigma equals Bernardi
  sigma times exp(E2*log_E²/24), and the exact height convention.

Material deductions now proved in `cm-regulator-tensor-attack.md`
(the coordinator's `review-cm-regulator-tensor.md` now records PASS
for the CM, height and polynomial deductions, the direct source audit,
and the independent analytic certificate):

1. For j=1728, [i]^* has eigenvalues i on omega and −i on x*omega.
   The ordinary unit-root line commutes with [i] and complements omega,
   so it is exactly the x*omega line. Therefore Katz E2=0 and canonical
   sigma_p is one fixed rational formal sigma at every good splitp.
   The square complex CM lattice likewise has e2*=0, so its reduced
   theta is that same sigma.
2. Using the Coleman limit formula and a common multiplier m carrying
   P,Q into the formal group and all bad identity components, put
   F_p(R)=log_p e(R)+K_0^col(0,R,1)+(1/12)log_p Delta_Gamma.
   The exact regulator identity is
   R_p=m^(−4)[4F_p(mP)F_p(mQ)−(F_p(m(P+Q))−F_p(mP)−F_p(mQ))²].
   This expresses the actual regulator through the same reduced-theta
   family as Katz, with no Sha-finiteness premise. It does not yet
   identify its value with the torsion second moment.
3. The three weight(2p−1) moments determine the numerator only modulo
   p³. For a regulator of valuation3, normalized quotient modulo p
   requires the numerator modulo p⁴. A direct logarithm expansion gives
   the next polynomial: if X=x^(p−1),Y=y^(−(p−1)), then
   ell² ≡(X−Y)²(3−X−Y)/(p−1)² modp⁴. This adds four degree3 moments
   to the three degree2 moments. The full proof and Euler-factor,
   factorial and differing CM-period-power bookkeeping are in §6.

The read-only check in exec session2204 finished. Exact outputs:
ellrank=[2,2,0,[[3,12],[27,144]]]; eclib saturation at all primes returned
(True,1,'[ ]'), rank2; conductor48672, torsion2, Tamagawa product8,
root number+1. Thus the source's full basis was independently verified.
An optional sigma print failed because its E2 argument was a Python
integer rather than a p-adic number; no sigma output was obtained or
used. The preceding E2 print O(5^8) is only a consistency check, not
the proof that E2=0. There is no live process to resume.

A further read-only Mellin certificate was completed using the existing
reviewed algorithm on the explicit equation, after a label-based call
failed because the small installed database lacks this curve. The explicit
call used 96-bit balls, t-cutoff40 and Fourier cutoff1405, and proved
analytic rank2 with L''(E,1)/2 in a positive interval near8.6593044012.
Exact endpoints and reproduction commands are embedded in §8 of the
attack note. No script or data file outside the two owned notes was added.
Both execution sessions have finished; do not restart them.

The source audit now also includes BKT0711.1701v2: Theorem4.15 gives
the full p-adic polylogarithm sheaf and TheoremA.19 the real Hodge
realization at any nonzero point. The explicit syntomic formula in
Theorem4.23, using Lemma4.20, is restricted to nonzero torsion of order
prime to p. The note does not claim non-torsion realizations are absent.

The remaining exact identity is CM-Theta, equation (16). Its repaired
statement first requires proof that the real quotient n_E is rational;
only then is its canonical image in Q_p compared. An arbitrary embedding
of a real value into C_p is not this arithmetic rationality premise.
The torsion second moment, with c_cmp=(156i Omega_p)^(-1), must equal
4*e_p*n_E times the actual non-torsion regulator determinant.
The gamma-log squares cancel in the normalized quotient. The note
proves the common-theta height description and next-precision moment
formula, but not this arithmetic comparison, a global integral analytic
tensor, Sha finiteness or BSD.

## Material finding: direct BK audit completed

The new §6.1 independently derives the restricted moment formula (13)
from BK's integral construction, Lemma 3.4, Proposition 3.5, and the
partial Katz definitions 3.8–3.9. It does not take Banwait's recent
preprint as the proof of this identity.

* BK Proposition 3.3 excludes a zero parameter and therefore cannot
  be applied to our unrestricted w0=0 measure. The discrepancy between
  formal and elliptic-logarithmic pole subtraction is one-variable;
  the other unit projector annihilates it. Work only after restriction.
* For a ray-class ideal a, put q=psi(a). The Néron model descends to K,
  so Lambda(a)=q and Omega_p^sigma=(q/Na)Omega_p. The partial tilde
  measure is q times the fixed-lattice measure pushed by
  (u,v)→(q*u, Nf*v/barq). Its ideal-character factor for
  phi=psi^(k+1)*barpsi^(-l) cancels q^(k+1)*barq^(-l) exactly.
  Therefore the central twist has the extra factor Omega_p, with
  global coordinates x=hatpsi, y=hatbarpsi and xy=chi_cyc. This
  proves equality on continuous test functions, not just a critical cone.
* The finite ray-class parameters are q*alpha0*Omega, or
  epsilon(g)*g*Omega. Sum once per ray class. BK Definition 3.6's
  second display, literally summed over all residue units, would
  repeat our terms four times; that display is not used.
* Theta homogeneity degree −1 gives the essential Euler +1 shifts.
  Retain the CRT element eta when rescaling: beta=eta/barpi lies in
  O_K and is barpi^(-1) modulo f. The parameters beta*z and pi*beta*z
  implement the inverse barp class action. The literal z/barpi need
  not be f-torsion. The two factors are pi^k/barpi^(l+1) and
  pi^l/barpi^(k+1), with double term their product.
* The logarithmic derivatives give Omega_p^(k+l)*k!*l!, the Laurent
  coefficient supplies (-1)^(k+l)*Nf^l/l!, and the exact transfer
  gives the final Omega_p. This proves the period, factorial and sign
  of (13). Neither BK Proposition 3.13 nor Theorem 3.7's displayed
  period power is needed.
* Independently, BK Corollary 3.12 gives the exact comparison
  (156i*Omega_p)^(-1) for matched roots of unity. Changing the root
  system gives a group-like cyclotomic multiplier of constant term1.
  Thus no unknown constant unit remains in (9).

The other live agent independently confirmed the q-cancellation and
the shifted Euler factors by direct BK reconstruction. The coordinator
completed the full §6.1 review with PASS, including the pole-projector
argument, exact character transfer, CRT beta, period powers and factorials.
The elementary mod-p^4 congruence remains logically
independent of this entire source audit.

The coordinator's new `compute/scripts/certify_cm39.py` and
`compute/data/cm39_analytic_rank_certificate.json` are now linked in
the note. The independent run at 112 bits, cutoff48 and Fourier
cutoff1686 lies strictly inside the first interval. Direct finite-field
coefficients and Hecke recurrences through1405 all agreed. No old
numerical work was repeated by this agent, and there is no live process.

## Exact next action

The coordinator's final review of §6.1 is PASS. The separate
`cm-moment-source-check.md` is saved, reviewed PASS, and linked from §6.1.
The next arithmetic target remains to prove
n_E∈Q and construct a Poincaré-biextension or polylogarithmic comparison
that sends the torsion second moment to the full non-torsion determinant
in (16), with these now explicit periods and character coordinates.
Theta addition was already tested and does not give that mapping by
itself. No Sha-finiteness assumption has been added; no new proof of
CM-Theta, primary finiteness, or BSD has been obtained in this audit.
