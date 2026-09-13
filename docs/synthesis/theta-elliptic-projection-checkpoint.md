# Restart: theta elliptic projection and the actual metric pairing

Date: 2026-09-12. Owner: root/coordinator. Bounded construction complete.
All eight sections of the [proof](theta-elliptic-projection-attack.md)
passed [independent review](review-theta-elliptic-projection.md) by
/root/odd_rank_bridge, GPT-6 Astra/xhigh. Universal BSD remains active.
No mathematical task or exec session is running under this checkpoint.

## Completed results

- For N=389, conjugation by W_N sends (a,b,c) to (c,-b,a)
  in the actual Du–Yang lattice and mu_r to mu_-r. The actual
  Kudla–Millson kernel is even in its lattice vector. Its components
  and all positive weighted CM point cycles are Fricke invariant.
- The actual degree-40 elliptic quotient satisfies pi W_N=-pi and
  sends both cusps to O. Its degree-zero point projection therefore
  kills the ENTIRE untwisted Du–Yang arithmetic theta series, not
  only the previously tested eta Hodge class. Positive indices use
  the weighted cycle symmetry; nonpositive indices retain the
  cusp, Hodge, vertical and pure metric terms. Hodge^12 is generically
  cuspidal. This is only the stated elliptic quotient, not every
  Jacobian quotient or theta variant. Point-height pairings vanish;
  arithmetic metric pairings need not vanish.
- The original forcing F=y²f conjugate(g) and its transgression are
  Fricke EVEN, since both f and g are odd and v_eta W_N=1/v_eta.
  Thus its known nonzero Mellin mass is not killed by this symmetry.
- The actual smooth Kummer 1-motive [Z→Gm], 1→v_eta, exists over
  the open modular curve, including v_eta=1. Fricke inversion is
  identity on the lattice and minus one on its Tate torus. The
  connection is nabla e0=-dlog(v)e1, with horizontal vectors
  e0+log(v)e1 and 2pi i e1. Deligne HodgeIII10.1.10 directly
  supports a 1-motive over the base scheme. Its transgression eta
  has d eta=F dmu and is not thereby a closed rational class.

## Mandatory compactification correction

The former single smooth Gillet–Soulé class a(2 ReF) was WITHDRAWN.
ReF has leading algebraic-cusp term
(1-N)/(4pi²) Re(q) log²|q|, which is not even C1 at q=0.
Borel–Serre flatness in 1/y does not imply algebraic-cusp smoothness.

The final proof uses genuine smooth cutoff classes a(2chi_epsilon ReF).
Cut off at cusps, and at elliptic points if coarse smoothness is used;
choose cutoffs compatible with complex conjugation. It proves ONLY
this convergent pairing limit:

    I_L(F)=lim_epsilon <phi_hat,a(2chi_epsilon ReF)>_GS.

No limit in an arithmetic Chow group is asserted. The metric factor
two cancels the actual source pairing's one-half. Complex conjugation
of z makes ImF odd and the scalar kernel coefficients invariant,
so I_L(F)=I_L(ReF), without conjugating the second theta variable.

Cusp cutoff errors are O(epsilon(1+|logepsilon|)²), and elliptic-point
errors of order e are O(epsilon^(2-2/e)); all tend to zero. The locally
integrable distribution dd^c ReF has no boundary atoms. Consequently
the exact source decomposition gives

    I_L(F)=degree(phi_hat)/degree(Delta_GS) int ReF mu_GS
                                    +int phi_SM dd^c ReF.

DO NOT set the first integral to zero. The previous cancellation was
against hyperbolic dmu, not the source's chosen smooth measure mu_GS.
Orbifold charts or an analytic fine cover retain effective degree;
no new integral arithmetic-stack/current theorem is imported.

## Exact next target

TPJ-389 is an actual weighted adjoint/doubling or arithmetic comparison
for int F j2, with the fixed boundary terms and a rational realization
in D_pt tensor Q beta2 tensor Q(1)^(-2). Its scalar must then be
6N(N-1)n_E as a consequence. Computing I_L(F) and I_L(j2) separately
does not permit multiplying the lifts to recover the original pairing.
The noncentral beta2 already has its arithmetic higher-Chow extension.

The next attempt must supply this missing operation and source, not
re-prove the point projection or define a metric from the desired value.
Use the full proof's source versions: Du–Yang1702.07917v2 (52 pages),
especially §§2,4,8, and Deligne, DOI10.1007/BF02685881, §10.1.
Preserve all Tate twists, both cusps, and the Fricke parity distinction.

The reviewed mathematical proof hash before editorial completion is
530e386d819e2e972b132c985311e8d331b1d7cd1798f3fff35e122d0487fd91.
The current file hashes are recorded in the root checkpoint manifest.
