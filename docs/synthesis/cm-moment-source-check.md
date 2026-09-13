# Independent source check of the restricted CM moments

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Model: GPT-6 Astra, xhigh reasoning. The coordinator requested an
independent reconstruction of the Euler factors, central twist, ray-class
indexing and one nonzero low moment. No prime scan was performed.

## 1. Result and the exact scope accepted

The **restricted** moment formula in Banwait Lemma 6.5(2) is recovered
directly from Bannai–Kobayashi's theta distribution relation and
Definitions 3.8–3.9, with the following conventions retained:

- x and y are the global p-adic avatars of psi and its conjugate;
  on the principal local-unit subgroup they are the corresponding two
  local coordinates. Their values on ray-class representatives are not
  discarded.
- The sum is over ray classes, hence over residue classes **modulo the
  global units** when K has class number one.
- The theta measure is first restricted to both unit coordinates using
  BK's prescribed formal pole removal. No assertion about unrestricted
  moments is inferred by replacing formal poles with logarithmic ones.
- The auxiliary CRT multiplier is kept until the shifted torsion
  parameter has returned to the original lattice.

With those conventions, the reconstructed identity is

$$
N(k,l)=\Omega_p^{k+l+1}(-1)^{k+l}k!(\mathrm N\mathfrak f)^l
\left(1-\frac{\pi^{k+l+1}}{p^{l+1}}\right)
\left(1-\frac{\pi^{k+l+1}}{p^{k+1}}\right)P_{l,k+1}.
\tag{1.1}
$$

All deductions below are `[NEW]` reconstructions and passed the
coordinator's review, recorded in [the CM review](review-cm-regulator-tensor.md).
This note does **not** accept every literal display
in BK Proposition 3.13, and it does not certify Banwait Lemma 6.5(1)'s
unrestricted pole-removal statement. It verifies the restricted formula
needed for the polynomial moment calculation. The discrepancy exhibited
in §7 concerns a printed source version, not BSD or an elliptic-curve
counterexample.

Primary sources read:

- [Bannai–Kobayashi, arXiv:math/0610163v4](https://arxiv.org/html/math/0610163v4),
  especially Theorem 1.17, Proposition 3.5, Definitions 3.6 and 3.8–3.9,
  the period transformation preceding Definition 3.8, Corollary 3.12,
  and Proposition 3.13. The [PDF, pp. 47–48](https://arxiv.org/pdf/math/0610163v4)
  was checked for the version-specific display issue.
- [Banwait, arXiv:2609.08431v1](https://arxiv.org/html/2609.08431v1),
  Definition 5.1, Proposition 5.2, and Lemma 6.5.

No Sha-finiteness assumption enters the measure identities reconstructed
here. The complex leading-term comparison remains a separate question.

## 2. Explicit setting and ray-class normalization

For the concrete test take

$$
E:y^2=x^3+39x,\quad K=\mathbb Q(i),\quad
\mathfrak f=(f_0),\quad f_0=39(1+i)^3,
$$
$$
\Gamma=\Omega_\infty\mathbb Z[i]=\mathfrak f\Omega,
\qquad \Omega=\Omega_\infty/f_0.
$$

Let psi be the CM Hecke character with
\(\psi((a))=\varepsilon(a)a\). Its values lie in K and
\(\varepsilon\) takes values in \(\mu_K=\{1,-1,i,-i\}\), with
\(\varepsilon(u)=u^{-1}\) for a global unit u. At a split good prime
\(p=\mathfrak p\bar{\mathfrak p}\), choose the embedding corresponding
to \(\mathfrak p\), and put

$$\pi=\psi(\mathfrak p),\qquad \bar\pi=\psi(\bar{\mathfrak p}),
\qquad \pi\bar\pi=p.$$

Thus pi is a uniformizer at the selected prime and bar-pi is a unit.
Also \(\varepsilon(\pi)=\varepsilon(\bar\pi)=1\): their principal
ideals are respectively \(\mathfrak p\) and \(\bar{\mathfrak p}\),
and applying psi to those principal ideals proves the assertion.

**[NEW] Lemma 2.1 (the factor of four).** In this setting

$$D_E=I_K(\mathfrak f)/P_K(\mathfrak f)
\simeq (\mathcal O_K/\mathfrak f)^\times/\mu_K.$$

Every orbit has a unique representative in the kernel of epsilon,
namely \(\varepsilon(g)g\) modulo \(\mathfrak f\). Consequently
an unweighted sum over ray classes has no extra factor four. If it
is rewritten as a sum over **all** invertible residue classes, it
must be divided by four with the corresponding unit weights.

*Proof.* The ray-class exact sequence and class number one identify
the ray class group with the quotient by the image of global units.
The units inject modulo this conductor; equivalently the only unit
congruent to one is one. Since epsilon restricts to inversion on the
units, multiplying g by epsilon(g) puts it in ker epsilon. This
representative is unique in its unit orbit. There are four elements
per orbit. \(\square\)

Put \(z_g=\varepsilon(g)g\Omega_\infty/f_0\). Banwait's class sum is

$$
P_{l,k+1}=\sum_{[g]\in D_E}
\frac{e^*_{l,k+1}(z_g,0;\Gamma)}{A(\Gamma)^l}.
\tag{2.1}
$$

The unit weights have been absorbed into z_g. This convention is
important; simply using epsilon(g) as the coefficient for every
weight does not give the same sum.

## 3. Derivation of both Euler factors, retaining the CRT parameter

Let \(\nu_g^\times\) be the restriction to \(\mathbb Z_p^\times\times
\mathbb Z_p^\times\) of BK's theta measure at z_g, with its second
variable scaled by \(\mathrm N\mathfrak f\). Let
\(\nu^\times=\sum_{[g]\in D_E}\nu_g^\times\).

Because the second torsion parameter is zero, the unrestricted
logarithmic-pole formula needs care. A change between the two usual
pole removals is a sum of functions in just one formal variable.
If \(A_1,A_2\) are averaging over p-torsion in the two variables,
then \((1-A_1)(1-A_2)\) kills every such one-variable term. Thus BK
Lemma 3.4 and Proposition 3.5 legitimately give the **restricted**
four-term theta identity independently of this pole convention.

Choose a CRT element eta in \(\mathcal O_K\) such that

$$
\eta\equiv1\pmod{\mathfrak f\mathfrak p},\qquad
\eta\equiv0\pmod{\bar{\mathfrak p}},\qquad
\beta=\eta/\bar\pi\in\mathcal O_K.
\tag{3.1}
$$

Then \(\beta\equiv\bar\pi^{-1}\pmod{\mathfrak f}\) and its finite
psi-character is one. Its multiplication on the f-torsion parameters
therefore permutes D_E by the inverse conjugate-prime ray class.
Literal division of a chosen complex torsion representative by bar-pi
would not justify this step: the resulting point need not be f-torsion.

**[NEW] Proposition 3.1 (restricted theta moments).** For k,l>=0,

$$
\int u^kv^l\,d\nu^\times
=\Omega_p^{k+l}(-1)^{k+l}k!(\mathrm N\mathfrak f)^l
\mathcal E(k,l)P_{l,k+1},
\tag{3.2}
$$
$$
\mathcal E(k,l)=
\left(1-\frac{\pi^k}{\bar\pi^{l+1}}\right)
\left(1-\frac{\pi^l}{\bar\pi^{k+1}}\right).
\tag{3.3}
$$

*Proof.* Reduced theta has homogeneity degree -1:

$$
\Theta_{a z_0,a w_0}(az,aw;a\Gamma)
=a^{-1}\Theta_{z_0,w_0}(z,w;\Gamma).
$$

In BK Proposition 3.5 the first averaged term is
\(\Theta_{pz_g,0}(pz,w;\bar\pi\Gamma)\), the second is
\(\Theta_{\eta z_g,0}(z,pw;\bar\pi\Gamma)\), and the double term is
\(\Theta_{p\eta z_g,0}(pz,pw;\bar\pi^2\Gamma)\).
After scaling lattices back, these become respectively

$$
\bar\pi^{-1}\Theta_{\pi z_g,0}(\pi z,w/\bar\pi;\Gamma),
$$
$$
\bar\pi^{-1}\Theta_{\beta z_g,0}(z/\bar\pi,\pi w;\Gamma),
$$
$$
\bar\pi^{-2}\Theta_{\pi\beta z_g,0}
             (\pi z/\bar\pi,\pi w/\bar\pi;\Gamma).
$$

Thus their z^k w^l coefficients are multiplied by
\(\pi^k/\bar\pi^{l+1}\), \(\pi^l/\bar\pi^{k+1}\), and their
product. The factors \(\bar\pi^{-1}\) in this computation are the
source of the two **+1** exponents. All three parameter changes are
permutations of the same ray-class set, as just checked.

The regular coefficient of z^k w^l in
\(\Theta_{z_g,0}(z,\mathrm N\mathfrak f\,w;\Gamma)\) is

$$
\frac{(-1)^{k+l}(\mathrm N\mathfrak f)^l}{l!}
\frac{e^*_{l,k+1}(z_g,0;\Gamma)}{A(\Gamma)^l}.
$$

This is BK Theorem 1.17. Taking k and l logarithmic derivatives of
the Amice transform multiplies it by
\(\Omega_p^{k+l}k!l!\). The four-term alternating sum therefore
gives (3.2)–(3.3). All polar terms cancel in that sum before moments
are taken. \(\square\)

Using \(\pi\bar\pi=p\), equation (3.3) is exactly the Euler factor
in Banwait Lemma 6.5. Its shape also agrees with the Euler factors
in BK Theorem 3.7 after substituting a=l,b=k+1. The direct derivative
calculation above, rather than that theorem's printed period exponent,
fixes the power \(\Omega_p^{k+l}\) for this unweighted measure.

## 4. Independent central-twist cancellation from the ray-class definition

This verifies the cancellation found separately by the CM-note author.
It does not use BK Proposition 3.13.

Let \(\mathfrak a\) be prime to \(\mathfrak fp\), put
\(q=\psi(\mathfrak a)\), and set \(n=\mathrm N\mathfrak a=q\bar q\).
Since E and its differential descend to K, the isogeny multiplier in
BK §3.3 is \(\Lambda(\mathfrak a)=q\), and
\(\Gamma^{\sigma_\mathfrak a}=\Gamma\). BK explicitly fixes

$$\Omega_p^{\sigma_\mathfrak a}=(q/n)\Omega_p.$$

Choose \(\alpha_0\in\mathfrak a^{-1}\cap P_K(\mathfrak f)\) as in
the partial-L definition. BK's tilde transform on
\(\mathfrak a^{-1}\Gamma\) is

$$
q\,\widehat\Theta^{*\iota,\sigma_\mathfrak a}_{q\alpha_0\Omega,0}
                ([n]S,[\mathrm N\mathfrak f]T;\Gamma).
\tag{4.1}
$$

In its logarithmic variables, (4.1) is q times the pushforward of the
base theta measure by

$$
(u,v)\longmapsto(qu,\mathrm N\mathfrak f\,v/\bar q).
\tag{4.2}
$$

Indeed the first logarithmic coordinate is
\((q/n)\Omega_p\,n\log(1+S)=q\Omega_p\log(1+S)\), and the second
is \((\mathrm N\mathfrak f/\bar q)\Omega_p\log(1+T)\).
Since q,bar-q and Nf are p-units, these pushforwards preserve the
two-unit restriction. Formula (4.2) is an identity of the restricted
measures, not merely their valuations.

**[NEW] Proposition 4.1 (the central factor is Omega_p).** Use
\(x=\widehat\psi\), \(y=\widehat{\bar\psi}\) as global coordinates,
including the ideal-class factors, and let
\(\mu_\psi=\widehat\psi\,\mu^{\rm Katz}\). Then

$$
\int x^ky^{-l}\,d\mu_\psi
=\Omega_p\int u^kv^l\,d\nu^\times.
\tag{4.3}
$$

*Proof.* The left side evaluates Katz at
\(\varphi=\psi^{k+1}\bar\psi^{-l}\). Write the partial contribution
using the class \(\mathfrak a^{-1}\). BK Definition 3.9 includes
the factor \(\varphi(\mathfrak a)^{-1}\). On the local-unit subgroup,
the character is \(X^{k+1}\bar X^{-l}\).

Definition 3.8 replaces the second Galois coordinate by the inverse
second theta coordinate and weights the measure by \(\Omega_p X^{-1}\).
Hence its polynomial integrand becomes \(X^kY^l\). Applying (4.2)
contributes

$$
\Omega_p\,\varphi(\mathfrak a)^{-1}
q^{k+1}\bar q^{-l}(\mathrm N\mathfrak f)^l
=\Omega_p(\mathrm N\mathfrak f)^l.
$$

The factor \((\mathrm N\mathfrak f)^l\) is already part of the
second-coordinate scaling in the definition of \(\nu_g\). The only
remaining central scalar is therefore Omega_p.

Finally \(q\alpha_0=\psi(\alpha_0\mathfrak a)\), because alpha_0
is congruent to one modulo the conductor. The parameters
\(q\alpha_0\Omega\) are exactly the ray-class parameters in BK
Definition 3.6. Inversion \([\mathfrak a^{-1}]\mapsto[\mathfrak a]\)
permutes the ray classes, so summing the partial contributions proves
(4.3). No fourfold all-residue sum occurs. \(\square\)

Combining Propositions 3.1 and 4.1 proves (1.1). If x,y are instead
used to mean bare local coordinates on separately chosen class charts,
the class factors in this proof must be included explicitly; simply
forgetting them is not the proved statement.

## 5. Zeroth and nonzero fourth moments

At k=l=0, the reconstructed formula gives

$$
N(0,0)=\Omega_p(1-\bar\pi^{-1})^2P_{0,1}.
\tag{5.1}
$$

Here \(P_{0,1}=(f_0/\Omega_\infty)L_{\mathfrak f}(\bar\psi,1)\).
With BK's \(\Omega=\Omega_\infty/f_0\), this is the expected Katz
central normalization, and BK Corollary 3.12 converts its CM period
to the real Néron period by its specified factor u. At a rank-two
curve both sides vanish, so this moment alone cannot test a missing
nonzero scalar.

**[NEW] Proposition 5.1 (a nonzero low moment).** For the Q(i) curve
above,

$$
\boxed{N(4,0)=24\Omega_p^5
(1-\pi^5/p)(1-\bar\pi^{-5})P_{0,5}\ne0.}
\tag{5.2}
$$

Moreover

$$P_{0,5}=(f_0/\Omega_\infty)^5
                 L_{\mathfrak f}(\bar\psi^5,5),$$

and no factor four is present.

*Proof.* Apply (1.1). The sign is positive, the factorial is 4!=24,
and the period power is five. To check nonvanishing and normalization
independently, write the absolutely convergent sum

$$
P_{0,5}=\frac1{4}(f_0/\Omega_\infty)^5
\sum_{a\in\mathbb Z[i],\,(a,\mathfrak f)=1}
                 \varepsilon(a)^{-5}a^{-5}.
\tag{5.3}
$$

The factor 1/4 compensates for writing all residue orbits and all
generators; each integral ideal has four generators. Their value
\((\varepsilon(a)a)^{-5}=\psi((a))^{-5}\) is unchanged by units.
Thus (5.3) equals the stated ideal L-series with each ideal counted
once. The absolute size of its ideal term is \((\mathrm N\mathfrak a)^{-5/2}\),
so its Euler product converges absolutely and is nonzero. Both Euler
factors in (5.2) are nonzero, as are the periods.

This index is tame-compatible: epsilon^5=epsilon, so the character
psi^5 has the same conductor character as psi. In particular it
avoids the unit/parity ambiguity of a bare degree-two monomial in
separately chosen local coordinates. \(\square\)

At p=5, choose \(\pi=-1+2i\) and the embedding \(i\equiv3\pmod5\).
Then pi is zero modulo 5 and bar-pi is 3. The factor in (5.2) reduces to

$$
(1-\pi^4/\bar\pi)(1-\bar\pi^{-5})\equiv1\cdot4=4\pmod5.
$$

This is an exact single-prime algebraic normalization check, not a scan
or an inference about Sha. It does not assert that the whole moment is
a p-adic unit; P_(0,5) can contribute valuation.

## 6. The source displays that must not replace the reconstruction

The literal Euler display in the proof of BK Proposition 3.13v4,
printed p. 48, reads

$$
\left(1-\frac{\pi^k}{\bar\pi^l\varepsilon(\pi)}\right)
\left(1-\frac{\varepsilon(\bar\pi)\pi^l}{\bar\pi^k}\right).
\tag{6.1}
$$

It lacks the degree-minus-one shifts retained in (3.3). Both the PDF
and its HTML transcription have this display. The same proof also
identifies ray classes with all invertible residue classes; in Q(i)
the quotient by four global units must instead be retained. The
unweighted period exponent printed in Theorem 3.7 is not used here:
the derivative calculation and the Katz transfer separately give
Omega_p^(k+l) and then the additional Omega_p.

These observations do not invalidate the distribution identity in
Proposition 3.5 or the ray-class definition in 3.9. They explain why
literal substitution in Proposition 3.13 is not a safe proof of (1.1).

## 7. A nonzero check of the printed Euler discrepancy

**[NEW, version-specific source check]** The discrepancy in (6.1)
can be tested without using a possibly zero central mass. Consider
the weighted, all-residue theta moment with k=2,l=0, precisely as
it appears in the proof of BK Proposition 3.13. Let

$$S_{2,0}=\sum_{a\in(\mathbb Z[i]/\mathfrak f)^\times}
                   \varepsilon(a)c_{2,0}(a).$$

The regular coefficient formula gives
\(c_{2,0}(a)=2e^*_{0,3}(a\Omega,0;\Gamma)\). Since epsilon takes
fourth roots of unity, epsilon^(-3)=epsilon. Therefore

$$S_{2,0}=8P_{0,3}\ne0.$$

Only a coefficient with positive first-variable degree is used here;
none of the one-variable second-leg pole corrections affects it.

Nonvanishing follows by the same ideal-sum argument as in §5, now
from the absolutely convergent Euler product
\(L_{\mathfrak f}(\bar\psi^3,3)\).

The proof of Proposition 3.1 applies also to this weighted sum:
the CRT beta and pi have epsilon-character one, so reindexing
preserves the weights. The restriction multiplier is consequently

$$E_{\rm true}=(1-\pi^2/\bar\pi)(1-\bar\pi^{-3}).$$

The multiplier printed in (6.1) is

$$E_{\rm printed}=(1-\pi^2)(1-\bar\pi^{-2}).$$

At the p=5 embedding above,

$$E_{\rm true}\equiv3\pmod5,\qquad
E_{\rm printed}\equiv2\pmod5.$$

Both denominators here are p-adic units. Since S_(2,0) and Omega_p
are nonzero, these two multipliers cannot give the same exact
weighted theta moment. Thus (6.1), read literally with its stated
definitions in this source version, is inconsistent with the direct
restriction calculation. The degree-two test is used only for this
weighted theta-measure discrepancy; the global central-moment check
is the tame-compatible fourth moment in §5.

This is a discrepancy local to a displayed formula in
arXiv:math/0610163v4. It is not a counterexample to Banwait's correctly
shifted Euler factor, to the corrected measure construction, or to BSD.

## 8. Handoff

The direct reconstruction verifies the exact restricted formula (1.1),
including the ray-class indexing and central scalar. The coordinator
read all eight sections and checked the two nonzero moments before
accepting this source check and equation (13) of the CM note.
The CM-note author independently obtained the same cancellation and
the required CRT correction; this file gives a separate derivation
and the low-moment check.

The saved §6.1 of `cm-regulator-tensor-attack.md` was also inspected
after its final revision. Its continuous-function transfer, explicit
q-cancellation, CRT beta, and once-per-ray-class indexing agree with
the independent calculations here. No further correction was found
in that passage.

The unrestricted formal/logarithmic pole discrepancy remains excluded
from this approval. No CM regulator nondegeneracy, full Sha finiteness,
or complex BSD comparison follows from the moment calculation alone.

Only this source-check file and the previously authorized minor
Green-note clarifications were edited in this task. No numerical prime
scan or expensive certificate rerun was needed.
