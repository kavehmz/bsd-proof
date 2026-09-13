# Exponential spectral kernel restart checkpoint

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
Own exponential-spectral-attack.md and this checkpoint. Full BSD remains
the parent objective. No new agents or old certificate reruns.

Assigned positive construction: realize modulo t³ the exact kernel
Γ(1+t)^−1 ∫₀∞ e^−v v^t(1+v/Z)^t dv by a rational irregular/logarithm
connection and a relative rapid-decay cycle. Retain the endpoint at0;
it has logarithmic, not rapid, behavior. Give actual rational Betti and
de Rham frames and account for every Tate/gamma normalization.

The completed construction over Q(Z), Z≠0, uses q(v,Z)=v(v+Z)/Z and
the rank3 module Q(Z)[t]/t³ with connection
∇=d−dv+t dlog(q). Its dual positive section is
e^−v exp(t log q). At0, q/v→1, fixing a rational tangential normalization.
The relative fiber de Rham complex has source vR and target R dv,
R=Q(Z)[v,(v+Z)^−1]⊗Q[t]/t³. This forces vanishing at0, while rational
growth at∞ is killed by the exponential. Its relative/tangential
integration, finite bases and perfect comparison have been proved.

Gamma normalization is handled by the SAME exponential-log object
with q=v: Γ(1+t)=1+g1t+g2t². Its inverse modulo t³ is the polynomial
1−g1t+(g1²−g2)t², so sums/tensors suffice without inverting an
arbitrary nonrational period. A second option is to multiply the completed
Eisenstein family by Γ(s), whose value at1 is1.

## Positive construction independently reviewed PASS

Full proof saved in exponential-spectral-attack.md §§1–7, with PASS
in review-exponential-spectral.md. Reviewed mathematical revision:
452482f39ce66d17347c40d0fedc9ef6bf0fe048fa47ab3a35de2642a920db5f.
The positive-ray chart explicitly assumes Z>0; the rational connection
is overZ≠0 with other cycle charts obtained by continuation. Later
header/checkpoint changes are editorial.

- Exact rational flat rank3 connection ∇=d−dv+t dlog(v(v+Z)/Z), t³=0.
  Relative complex vR→Rdv has residue1+t in the relative frame at0.
  The dual is moderate at0, rapid only at∞. Primitives vanish at0,
  making every Stokes endpoint term zero. No absolute all-punctures
  rapid-decay theorem is improperly used for the open positive chain.
- H¹ is free rank2 overA=Q(Z)[t]/t³, basisdv,dv/(v+Z); reduction of
  higher poles uses unitZ(k−t), and reduction of positive polynomial
  degrees uses the leading−v^m term. Uniqueness is proved the same way.
- Rational dual Betti basisλ_j=(2πi)^−j coeff_t^j has monodromy
  Mλ_j=Σλ_(j−r)/r!. Thus t is not unchanged across realizations.
  Stable integral latticeλ0,λ1,2λ2; the primal Tate factors are(2πi)^j.
- Relative boundary: the entire logarithmic circle at0 is relative,
  framed by its positive tangent; at∞ only the positive rapid arc is
  relative; the−Z loop stays. Graph boundary(a,b,c)=a−b+(M−1)c.
  Six cyclesΓ_j=(p0+p∞)λj,Λ_j=loopλj−p0((M−1)λj).
  Exact integration pairs withdeRhamframes. Diagonalperiodblocks
  (2πi)^−j[[1,e^ZE1(Z)],[0,2πie^Z]] prove perfection directly.
- Actual rational Gauss–Manin system:
  I'=−t I/Z+t Jt; Jt'=−I/Z+(1+t/Z)Jt.
  Hence I''−I'−t(t+1)I/Z²=0 without dividing bynilpotentt.
- Gamma jet comes fromsame relativeobject withq=v, H¹ rank1 overA0.
  G(t)=1+g1t+g2t². Inverse1−g1t+(g1²−g2)t² is a polynomial
  in actualperiods; sums/tensorproducts andexplicitTatefactors give
  I/G. No arbitrary nonrationalperiod is inverted.
- Completion C0=ξ(2s)(N^(2s)−1), orC1=Γ(s)C0, has valueπ(N²−1)/6.
  Pairedsecondjet changesonlybythatvalue, butunpairedcoefficient
  c0A2+c1A1+c2A0+c3R retains thecubic×pole term.
  C1E∞ firstFouriermode is−q I(t,4πy), atzeroNq e^(tlogN)I.
  Generalmodesarefinite rationallog/divisorsum combinations withI.
  Exactzero modesand theircommonresidue(N−1)/2 arekeptin(6.5).
  Pairedmass=−3N(N−1)/(2π³) ellL2, i.e.−226398/π³ ellL2 at389.

Primary sources inspected: Bloch–Esnaultmath/0005137v1 Thm0.1,
Example0.2 andrapidchain definitions (explicitly regularsing0 isnotrapid);
the previously checked Huber–Kings logarithm variation supplies theTate
coefficientobject. The relativepairing is proved directly here. Fresán–Jossen
book URLs were located but fullPDF fetches timed out; no unread theorem
from that book is relied upon. No old numerical script was rerun.

The relative-circle chain model, rational Betti frames, finite pairing,
gamma tensor normalization and all completed Fourier/cusp constants
passed review. Remaining mathematical steps are the nonalgebraic
substitutionZ=−2nlog|q|, the infinite modular
sum with one rational realization, and the classical BSD determinant
comparison. None is inferred from the individual kernel construction.
