# CM derived elliptic-unit attack: checkpoint

Date: 2026-09-12. Agent `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Owned files: `cm-derived-unit-attack.md` and this checkpoint only.

## Objective and scope

Construct the cyclotomic rank-two derived/Bockstein specialization
of a genuine finite-level elliptic-unit Euler system for
E:y²=x³+39x, and test whether it descends to the single rational
framed element required by CM-Biex. Preserve exact norm relations,
height, Euler and CM-period factors. Do not assume finite Sha,
Selmer corank two, or rationality of the complex BSD quotient.

The previous CM relative 1-motive, rational Kummer correction and
secondary determinant are reviewed PASS. Its target is a rational
element Ztheta in det(L_A) tensor det(L_B) whose real realization
is (L''/2)/(2Omega_E) and whose p-adic realization is
c_cmp*M_p/(4e_p). The existing direct torsion-frame and algebraic-
character obstructions are completed results, not work to repeat.

## Construction status

The primary finite-level construction has now been verified in
U. Schmitt, A comparison of elliptic units, author PDF at
https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf,
Definitions2.1–2.7,3.12, Proposition3.13, and the explicit norm relations
on printedpp47–49. It uses Theta=Theta0^12; for an integer a prime
to6fp, Theta_a is the unambiguous rational function
a^(-12)*Delta^(a²−1)*product_(0≠U∈E[a]) (x−x(U))^(-6).
On F_r=K(f p^r), evaluate at Omega∞/(f0 p^r), and norm down to
L_r=K(E[p^r]). The resulting global units e_r are norm compatible.
The conductor has several distinct prime factors, so these are
global units, not merely p-units. Norms at newly introduced primes
have factor1−sigma_q^(-1); repeated prime levels have factor1.

The exact p-adic twist has been checked in Rubin, Euler Systems
VI.3.5 and VI.5.3 (https://swc-math.github.io/aws/1999/99RubinES.pdf):
T_pi E=Zp(Psi), rho=Psi*chi_cyc^(-1)=(Psi^c)^(-1).
Twisting must precede passage from the full two-variable ray tower
to the cyclotomic quotient. At coefficient level p^m the tensor
rho is trivial over sufficiently high L_r, so one can form the
twisted Kummer class and corestrict to the cyclotomic layer K_n.
Norm compatibility proves independence of the high r and compatibility
in m,n. This gives an actual cyclotomic Iwasawa cohomology class.

Schmitt's Coleman map has EXACT image12*(sigma_a−Na)*lambda on
e(a). Twisting sends sigma_a to rho(sigma_a)^(-1)*sigma_a, so
the smoothing factor becomes12*(Psi^c(a)*sigma_a−Na).
For a=(5), or a=(7) if p=5, its cyclotomic augmentation is
12*(±a−a²), always a p-unit in the good split scope. Thus its
inverse exists integrally in the cyclotomic Iwasawa algebra.
The normalized class is independent of a by the common lambda
and injectivity of Schmitt's Coleman map.

The exact reciprocity dictionary has now been derived from the primary
Kato2004 §§15.4–15.16 and Theorem16.6, read in the full downloaded PDF.
Kato's normalized elliptic unit uses Na−sigma_a, opposite to Schmitt's
sign. Its twelfth power is the Theta used above, so the Néron class
is NEGATIVE the preliminary Schmitt-normalized class after fixing
the same coefficient vector. The factor12 is retained.

The coefficient is now fixed rationally: if b has period Omega∞, then
gamma_E^+=(bdual−(ib)dual)/2 has per(omega)^+=Omega_E*gamma_E^+.
Choose gamma_CM=2*pr_rho(gamma_E^+), whose induced plus component is
exactly gamma_E^+. Kato's CM comparison15.12.2/15.16.1, followed by
the Tate twist(1) and Theorem16.6, gives EXACT Col(z∞)=L_p(E,T).
Thus there is no unknown Iwasawa unit or arbitrary period scalar.
The previously reviewed BK comparison gives c2=c_cmp*M_p/(2g_p²),
with c_cmp=(156i Omega_p)^(-1). The source audit and all Betti
choices are explicit in §3 of the attack note.

Other primary sources inspected: BKS1910.07404 (current60-pagePDF)
Hypothesis2.2 and Theorem6.2 explicitly require primary Sha finite;
Howard1202.6343v1 Theorem4.5 gives a derived-height formula on full
Selmer groups from a local singular divisibility hypothesis without
assuming MW exhausts Selmer; Bullach–Hofer2102.01545v3 §6 directly
treats the one-prime Zp extension in the split case, not cyclotomic;
Castella author Kato-cm.pdf concerns a different generalized Kato
class. None of those scopes has been silently enlarged.

All of the following deductions are saved with full proofs and have
received independent mathematical review
[PASS](review-cm-derived-unit.md), including the exact scalar,
integral divisibility and full-Selmer scope:

1. For the ordinary Selmer complex with inverse cyclotomic action
modulo T², the Bockstein on a lifted cocycle f is represented globally
by −c_gamma cup f, c_gamma(g)=log_p chi_cyc(g)/log_p(1+p), with
the compatible cone-local terms. This exists without a corank2
or Sha hypothesis. The height uses the MINUS connecting map, matching
BKS's exact sign convention. On the known two-dimensional MW subspace, its
determinant gives Reg_p/log_p(1+p)^2 times T², using the canonical
height comparison; it need not be the determinant of the full Selmer.

2. The rational-descent test at genuine finite levels fails in a
precise way: for Gamma_n=C_(p^n), the augmentation ideal of
Q[Gamma_n] is idempotent, so every positive graded piece is zero.
Integrally I_n/I_n²=Z/p^n, with compatible generator gamma_n−1;
the inverse limit is Zp. Rationalizing BEFORE the finite-level
Bockstein therefore destroys its derivative direction. This does
not rule out a different higher motivic descent construction.

3. First T-divisibility of the actual unit class does NOT need Sha
finite: global H¹_Iw has rank1 and H²_Iw is torsion by Kato12.4.
Kato12.5(3), proved for CM using Rubin15.2/15.17, supplies the
augmentation-local length inequality; the local correction term
is absent because p is good. Global Euler characteristic−1 and
the injection of P,Q show dim H²(G_Q,S,V)≥1. H³_Iw=0 and derived
base change make H²_Iw/T=H²_global, so T divides the characteristic
ideal and hence the unit class. To lift from height-one to integral
divisibility, H¹_Iw/T injects into H¹_global(T_pE), which is
Z_p-torsion-free since E(Q)[p∞]=0. Any nonzero augmentation value
of a localized denominator then acts injectively. Division by T
is unique. This retains the integral/local distinction root flagged.

4. Write z∞=T*w∞ and kappa_p=w0 tensorT. Since Col(w∞)=L_p/T
has zero constant term, the nonzero dual-exponential interpolation
factor implies w0 lies in FULL Selmer. No corank identification
is made, and kappa_p is allowed to be zero.

5. Reproduce the local/global cone proof of Rubin's formula on
full Selmer, using only w0's Selmer membership; this avoids BKS6.2's
unnecessary whole-Selmer=MW identification. The explicit Coleman
test vector is delta0=k_alpha^(-1)*nu, [omega,nu]=1. Its factor
follows from Tr(zeta_p)=−1 and phi(nu)=beta^(-1)nu. Therefore
h_gamma(x,kappa∞)=k_alpha*log_omega(x)*c2*T²,
k_alpha=(1−alpha^(-1))^(-1)*(1−beta^(-1)), beta=p/alpha.

6. If Reg_p on the KNOWN MW subspace is nonzero, it defines a
canonical height-orthogonal projection of full Selmer onto that
subspace. No global Selmer corank2 assumption is needed. Its
projection of kappa_p equals
(g_p²*k_alpha*c2/Reg_p)*R_Boc, where
R_Boc=(adj(H_p)*log_vector)/g_p tensorT.
Since k_alpha*e_p=#E(Fp)/p, multiply by p/(2#E(Fp)) and invert
the Bockstein map on its one-dimensional image to construct Z_p
in the actual rational frame line tensored Q_p. It satisfies
Z_p=(c_cmp*M_p/(4e_p Reg_p))*Xi and
R_p(Z_p)=c_cmp*M_p/(4e_p), EXACTLY. This inverse requires Reg_p≠0;
the earlier class and height formula do not. Extra Sha directions
remain in the projection kernel and have not been proved absent.

7. The rational descent before separate p-completion was tested
on the actual finite unit tower and fails by item2. Keeping integral
levels produces the separate Z_p directions, not a proved rational
framed element. CM-Derived in §8 now asks for one rational Ztheta
with these localizations and real realization (L''/2)/(2Omega_E).
Its existence would prove n_E rational; this is not a premise.

No old numerical certificate or unit scan was rerun. No process is
running. The downloaded Kato PDF is /tmp/cm-derived-kato2004.pdf,
SHA2563c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d;
its extracted text is /tmp/cm-derived-kato2004.txt. Both the download
and extraction finished; do not restart them. Exact source URL and
hash are preserved in the attack note.

## Final source and convention audit

The independent reviewer verified the three final clarifications:

1. Kato's length bound initially concerns Z(f), generated by all
Betti coefficients. His conjugation relation12.5(1), after Tate
twist(1) and passage to the even cyclotomic branch, kills the minus
Betti part. The nonzero Néron plus coefficient therefore generates
Z(f) over the augmentation-local ring. The bound genuinely applies
to the individual z_infinity used here.

2. Apply Kato with the conjugate CM type selected by rho=(Psi^c)^(-1).
On the diagonal tower, conjugating Omega_infinity and f0 sends
R_(r,r) to its negative. Theta_a is rational and even, so the
diagonal normed elliptic units are conjugation-invariant. Exchanging
CM components preserves the specified induced plus Betti coefficient
and, after Tate twist(1), the even branch. No period sign is hidden.

3. The apparent Frobenius inconsistency is resolved by distinguishing
absolute cohomological F from phi=F/p on D_cris(V_pE). With alpha
the ordinary unit root and beta=p/alpha, the exact table is:

| Line | F eigenvalue | phi eigenvalue |
| --- | --- | --- |
| Q_p omega | beta | alpha^(-1) |
| Q_p eta, eta=x omega | alpha | beta^(-1) |

CM multiplication diagonalizes the two lines and commutes with F.
Mazur–Stein–Tate§3.2 explicitly gives F(omega) in pH^1, proving
which ordinary root belongs to each. The canonical unit-root
complement refers to F and is the eta-line; BKS6.9's nu has
phi-eigenvalue alpha/p=beta^(-1), so it lies in that complement and
is transverse to omega. SW§4.1's printed reciprocal-alpha label is
inconsistent with its own §3.5 normalization and is not used.
The earlier CM E2=0 calculation remains valid directly from MST:
F^n eta has zero omega coefficient. The alternating pairing obeys
[phi u,phi v]=p^(-1)[u,v]. No delta0, k_alpha, height or
p/(2#E(Fp)) factor changes.

The linked MST author PDF is paginated585–622; its published
pagination is577–614 (DOI10.4171/DMS/4/17). Both root and the
independent reviewer checked the Frobenius dictionary against that
primary source. The final review permits the subsequent review-link,
bibliography and checkpoint edits as editorial.

Next mathematical target, only on explicit resumption of this bounded
task: construct a rational framed Ztheta satisfying CM-Derived in§8,
including the real comparison, by a mechanism that survives the
finite-level augmentation obstruction. The remaining rational
descent and complex comparison have not been proved. No Sha-finiteness,
full-Selmer corank-two or regulator-nondegeneracy conclusion has been
added by the completed source audit.
