# **IDAI-700 PORTFOLIO: ENTRIES 2-6 RAPID SYNTHESIS GUIDE**
## **Your Notes → Polished Entry Format (Fast Track)**

---

## **ENTRY 2: LEKADIR ET AL. (2025) - FUTURE-AI Guidelines**

### **Citation (APA):**
Lekadir, K., Frangi, A. F., Porras, A. R., Woodruff, H. C., Glocker, B., … & FUTURE-AI Consortium. (2025). FUTURE-AI: International consensus guideline for trustworthy and deployable artificial intelligence in healthcare. *The BMJ*, 388, e081554. https://doi.org/10.1136/bmj-2024-081554

---

### **Why This Fits Your Theme (1–2 sentences):**
FUTURE-AI operationalizes **global consensus on six trustworthiness principles (Fairness, Universality, Traceability, Usability, Robustness, Explainability)** with 30 concrete practices, directly addressing policy/governance gaps in Nadarzynski's implementation roadmap and providing **enforcement mechanisms** Luke Munn argues are missing from abstract ethics frameworks.

---

### **SUMMARY (~400 words)**

**Central Claim:**
Trustworthy healthcare AI requires **systematic integration of fairness, universal applicability, traceability, usability, robustness, and explainability** across the entire AI lifecycle—not as afterthoughts but as foundational design principles operationalized through concrete best practices.

**Key Premises/Evidence:**
- Developed by **117 international experts from 50 countries**, ensuring diverse, global perspectives
- Framework grounded in existing standards (FDA, EU AI Act, WHO) + community advisory board input
- 30 specific practices mapped across 6 lifecycle stages (data collection, design, validation, regulation, deployment, monitoring)
- Explicitly addresses **CLD populations**: "Diverse data for bias prevention," "culturally sensitive validation," "patient/provider governance"

**Argument Structure:**
**Problem** (abstract principles fail without enforcement) → **Solution** (FAIR principles) → **Operationalization** (30 practices with accountability checkpoints) → **Verification** (governance structures, audits, ongoing monitoring)

This mirrors your EQUITAS logic: equity isn't asserted; it's **built into systems with measurable outcomes at each stage**.

**Scope & Limits:**
- Framework is **prescriptive but context-sensitive** (must adapt to specific healthcare systems)
- Emphasizes practices over technologies (generalizable)
- Acknowledges trade-offs (fairness vs. accuracy, speed vs. deliberation)—doesn't pretend perfect equity is achievable
- Requires organizational commitment + funding

**Evidence Hooks:**
- "Fairness must be embedded from data curation through post-deployment monitoring—not added retroactively"
- FAIR principles as mnemonic ensuring nothing gets forgotten
- Governance structures with patient/community involvement (not just expert-driven)

---

### **EVALUATION (~400 words)**

**Persuasiveness:**
I am convinced because:

1. **Specificity vs. Abstraction:** Unlike typical ethics frameworks, FUTURE-AI provides **concrete decision trees** at each stage. For example, "Diversify training data" becomes "conduct stratified analysis of performance across demographic subgroups; document disparities and mitigation strategies." This directly answers Munn's critique.

2. **Global + Local Balance:** The framework is created *by* 117 international experts *for* diverse healthcare contexts. Not imposed from the Global North on others—genuinely pluralistic.

3. **CLD Integration:** Explicitly mentions linguistic minorities, cultural validity, accessible documentation in multiple languages. Not tokenistic; woven throughout all 6 principles.

4. **Aligns with Your EQUITAS Framework:** The FAIR principles map cleanly onto your pillars: Fairness (Equity-Centered), Universality (Universal), Traceability (Traceable), Usability (Usable), Robustness (Robust), Explainability (Explainable). Provides institutional scaffolding for your conceptual framework.

**Weaknesses/Gaps:**

1. **Enforcement Mechanisms Unclear:** The framework prescribes practices but doesn't specify *who audits* or *what consequences* follow if organizations ignore it. Is this voluntary? Does it have legal teeth? Munn would still critique the gap.

2. **Implementation Burden:** 30 practices + 6 lifecycle stages = substantial resource requirements. The paper doesn't deeply address how under-resourced healthcare systems can implement without cutting corners.

3. **Limited Evidence Base:** While consensus-based, the guidelines lack **longitudinal evidence** showing that implementing all FAIR practices actually produces trustworthy AI in real-world settings. Is this aspirational or proven?

4. **Cultural Context:** "Culturally sensitive validation" is mentioned but under-specified. What does this look like operationally? How do you avoid tokenistic cultural consultation?

**Standards & Accountability:**
**Moderately concrete:**
- ✅ Specifies *what* practices (30 listed)
- ✅ Specifies *when* (across 6 lifecycle stages)
- ⚠️ Doesn't specify *who verifies* or *enforcement pathway*
- ⚠️ Relies on organizational good faith

**EQUITAS Alignment:**
- ✅ All 6 pillars directly addressed
- ✅ Systems-level thinking (not individual behavior)
- ⚠️ Robustness: limited evidence of effectiveness at scale
- ⚠️ Usability: may not scale to low-resource settings

**Implications for CLD Trust & Practice:**
For **CLD patients:** FUTURE-AI, if implemented, ensures their perspectives inform data practices, model design, validation, and deployment—building trust through inclusion.

For **healthcare providers:** Provides defensible standard (reduces liability risk) + practical checklist (reduces ambiguity).

For **my research:** FUTURE-AI provides the **policy/governance backbone** that operationalizes EQUITAS principles. Paired with Nadarzynski's design roadmap, they create a **complete architecture**: design HOW (Nadarzynski) + policy framework (Lekadir).

---

### **Quick Evidence Hooks:**
- **Quotes:** "Trustworthiness requires systematic integration of fairness, universality, traceability, usability, robustness, and explainability across the entire AI lifecycle."
- **Metrics:** Demographic parity, fairness audits, transparency reporting, community governance participation
- **Deployment Notes:** Community advisory boards, diverse validation datasets, post-deployment drift monitoring, transparent retirement criteria

### **Notes for Final Paper:**
- Pairs with Nadarzynski as **policy enforcement** of participatory design
- Provides **institutional structures** (governance, audits, stage gates) that Nadarzynski assumes but doesn't detail
- Shows how **abstract principles become organizational practice**
- Demonstrates that ethics ≠ aspirational; ethics = operational accountability

**WORD COUNT: Summary [__] + Evaluation [__] = _____ / ~800**

---

---

## **ENTRY 3: CHEN ET AL. (2023) - Algorithmic Fairness**

### **Why This Fits Your Theme (1–2 sentences):**
Chen et al. provide the **technical foundation** for operationalizing fairness—defining fairness metrics, bias sources, and mitigation techniques—showing that equitable healthcare AI requires both **ethical commitment** (Nadarzynski + Lekadir) AND **technical rigor** (mathematical fairness definitions, validated bias mitigation strategies).

---

### **SUMMARY (~400 words)**

**Central Claim:**
Healthcare AI systems are only equitable if fairness is **technically embedded through rigorous bias detection and mitigation** across the entire ML pipeline—bias in data, model choice, and evaluation all affect whether AI helps or harms CLD populations.

**Key Premises/Evidence:**
- Real-world examples: Dermatology AI performs worse on darker skin (CLD populations); hospital algorithms discriminate against Black patients
- Bias sources: Training data skewed toward majority groups, proxy variables encoding historical discrimination, evaluation metrics hiding disparities
- Solutions exist: Fairness-aware preprocessing (reweighting), algorithmic techniques (constrained optimization, post-hoc recalibration), rigorous auditing
- Tools available: IBM AI Fairness 360, other open-source frameworks for detecting/mitigating bias

**Argument Structure:**
**Problem** (healthcare AI inherits biases) → **Technical diagnosis** (identify where bias enters pipeline) → **Solutions** (fairness definitions + mitigation methods) → **Validation** (audit across demographic subgroups)

This translates philosophical equity into **mathematical accountability**.

**Scope & Limits:**
- Acknowledges fairness trade-offs (accuracy vs. fairness, group vs. individual fairness)
- Notes that fairness definitions are **context-dependent** (no single metric works everywhere)
- Emphasizes that technical fixes alone insufficient—require organizational commitment + governance

---

### **EVALUATION (~400 words)**

**Persuasiveness:**
I am convinced because:

1. **Grounded in Evidence:** Real examples (dermatology, hospital algorithms) show this isn't theoretical—CLD populations are *actually* harmed by biased AI today. This validates ED-415 diagnostic harm evidence.

2. **Operational Detail:** Doesn't just say "be fair"; shows *how*: preprocessing techniques, fairness metrics (demographic parity, equalized odds, calibration), post-hoc methods. Makes abstract principle concrete + testable.

3. **Honest About Trade-Offs:** Acknowledges you can't maximize all fairness definitions simultaneously. No false promises—instead, shows how to **choose trade-offs consciously with stakeholder input**.

4. **Connects to Your Framework:** Shows that EQUITAS "Robust" pillar requires **mathematical rigor**, not just intention.

**Weaknesses/Gaps:**

1. **Implementation Gap:** Describes fairness methods but less clear on **who decides fairness priorities** or **how to ensure decisions include CLD voices**. Technical ≠ automatically ethical.

2. **Limited on CLD Context:** While examples include racial/ethnic bias, less specific guidance on **linguistic diversity** (how do fairness metrics work for multilingual AI?) or **cultural context** (fairness defined how?).

3. **Assumes Resources:** Fair ML requires data scientists, computational resources, time for auditing. How do under-resourced clinics implement?

**Standards & Accountability:**
- ✅ Defines fairness mathematically (concrete, verifiable)
- ✅ Shows auditing methods (transparent)
- ⚠️ Doesn't specify who audits or organizational enforcement

**EQUITAS Alignment:**
- ✅ Quantitative-Based, Robust, Traceable
- ⚠️ Equity-Centered: needs human context for fairness definitions
- ⚠️ Usable: technical complexity may limit implementation

**Implications for CLD Trust & Practice:**
For **CLD patients:** Ensures AI is validated to *actually work* for them, not just for majority populations. This is credibility foundation for trust.

For **healthcare providers:** Provides auditable fairness standards, reducing liability + uncertainty.

For **my research:** Shows that **operationalizing equity requires technical + ethical integration**. Can't separate them. EQUITAS framework needs both Nadarzynski (participatory design) + Chen (technical rigor) + Lekadir (governance structures).

---

### **Quick Evidence Hooks:**
- **Quotes:** "Insufficiently fair AI systems can undermine equitable care."
- **Metrics:** Demographic parity, equalized odds, calibration, individual fairness, subgroup AUC
- **Deployment Notes:** Fairness-aware preprocessing, model selection with fairness constraints, bias auditing tools (IBM AI Fairness 360)

### **Notes for Final Paper:**
- **Technical proof** that equity isn't just ethical aspiration; it's *mathematically operationalizable*
- Shows CLD patients deserve AI validated specifically for them, not just for majority
- Pairs with Nadarzynski (participatory HOW) + Lekadir (governance WHEN) to complete framework

**WORD COUNT: Summary [__] + Evaluation [__] = _____ / ~800**

---

---

## **ENTRY 4: SAGONA ET AL. (2025) - Trust in AI-Assisted Health Systems**

### **Why This Fits Your Theme (1–2 sentences):**
Sagona et al. directly address your core research question by examining **how trust is earned in healthcare AI**—showing trust as an *outcome* of equitable design, transparency, and accountability rather than an assumption, and explicitly analyzing how systemic inequalities erode trust for marginalized communities.

---

### **SUMMARY (~400 words)**

**Central Claim:**
Trust in healthcare AI is **bidirectional and fragile**: patients/providers trust AI when they can verify fairness and transparency; simultaneously, AI systems must rely on trustworthy human inputs. For marginalized populations, **trust erodes if historical biases persist or accountability falters**—rebuilding trust requires rigorous fairness in design + shared governance.

**Key Premises/Evidence:**
- Trust influences whether patients seek care (access) + whether providers adopt AI (implementation)
- Marginalized communities have justified historical distrust of medical systems + AI
- Trust requires: transparent algorithms, diverse development teams, fairness validation, community involvement, clear accountability pathways
- Trust is relational, not technical; depends on organizational integrity + shared values

**Argument Structure:**
**Historical context** (why CLD communities distrust healthcare + AI) → **Mechanisms of trust-building** (transparency, fairness, shared governance) → **Consequences of betrayal** (AI that harms = permanent trust loss) → **Requirements for trustworthiness** (systemic accountability)

This frames trust as **verifiable process integrity**, not faith-based.

**Scope & Limits:**
- Trust is context-specific, cultural, dynamic
- Framework is conceptual; limited prescriptive implementation guidance
- Applies across populations but especially critical for historically marginalized groups

---

### **EVALUATION (~400 words)**

**Persuasiveness:**
I am convinced because:

1. **Addresses Historical Injustice:** Acknowledges that CLD communities' distrust is *rational response to real harm*, not deficiency. Trust must be *earned back through demonstrated equity*, not demanded.

2. **Bidirectional Insight:** Shows trust as mutual relationship, not one-way (patient ← AI). This complexity reflects real clinical dynamics.

3. **Connects Directly to Your Question:** Your research asks "how can healthcare providers and patients... *can trust*?" Sagona shows trust = **outcome of equitable design + transparency + accountability**. Not technology problem; relationship problem.

4. **Operationalizable:** While conceptual, offers concrete paths to trustworthiness (fairness validation, community advisory boards, transparent governance).

**Weaknesses/Gaps:**

1. **Limited Empirical Measurement:** How *do* you measure trust in marginalized communities? The paper discusses trust conceptually but less specific on measurement/validation.

2. **Power Dynamics Under-explored:** Who determines what "transparency" means? Whose values define "fairness"? Could inadvertently recreate power imbalances if not careful.

3. **Doesn't Address Structural Barriers:** Even transparent, fair AI won't build trust if healthcare system remains discriminatory in other ways. Trust requires *holistic equity*, not just AI equity.

**Standards & Accountability:**
- ✅ Defines trust mechanisms (transparency, fairness, community involvement)
- ⚠️ Limited on verification methods or enforcement structures
- ⚠️ Relies on organizational good faith

**EQUITAS Alignment:**
- ✅ Equity-Centered, Universal, Systems-Level
- ⚠️ Traceable: less on documentation/auditing
- ⚠️ Usable: how does this scale to real clinics?

**Implications for CLD Trust & Practice:**
For **CLD patients:** Trust in healthcare AI becomes possible when they see themselves in design, understand decision-making, and have recourse if harmed.

For **healthcare providers:** Trustworthy AI adoption requires transparency + fairness + community participation—not just good technology.

For **my research:** Sagona shows **trust as your outcome metric**. Your research question succeeds if CLD patients/providers say "I trust this AI system." That requires meeting all conditions: equitable design (Nadarzynski), policy enforcement (Lekadir), technical fairness (Chen), AND transparent relationships (Sagona).

---

### **Quick Evidence Hooks:**
- **Quotes:** "Trust in healthcare AI requires fairness in algorithm design, transparency, and shared accountability frameworks."
- **Trust factors:** Algorithmic transparency, diverse development teams, fairness validation, community governance, clear redress mechanisms
- **Deployment Notes:** Community advisory boards, transparent risk communication, escalation pathways, post-deployment monitoring with public reporting

### **Notes for Final Paper:**
- **Completes your research question** by showing trust as measurable outcome
- Connects all previous papers: Nadarzynski (how to design trust), Lekadir (how to govern it), Chen (how to verify fairness supporting it), Sagona (why it matters)
- Shows relationship-centered approach balances technical approaches

**WORD COUNT: Summary [__] + Evaluation [__] = _____ / ~800**

---

---

## **ENTRY 5: MARKO ET AL. (2025) - Examining Inclusivity (Systematic Review)**

### **Why This Fits Your Theme (1–2 sentences):**
Marko et al.'s systematic review of 129 studies **documents where AI fails CLD populations**—providing the empirical evidence base justifying every equity checkpoint in Nadarzynski's roadmap and Lekadir's framework, grounding your research in proof that inclusive design isn't optional but necessary.

---

### **SUMMARY (~400 words)**

**Central Claim:**
Healthcare AI systematically underperforms for diverse, marginalized populations due to **biased training data, lack of representation in development, and insufficient evaluation across subgroups**. Equitable AI requires explicitly designing *for* diverse populations throughout the lifecycle, not assuming one-size-fits-all.

**Key Premises/Evidence:**
- Systematic review of 129 peer-reviewed studies
- Consistent pattern: AI performs worse for women, racial/ethnic minorities, low-socioeconomic groups, LGBTQ+ populations, people with disabilities
- Root causes: skewed datasets, homogeneous development teams, evaluation metrics hiding disparities
- Solutions: diverse data, community co-design, subgroup-specific validation, inclusive governance

**Argument Structure:**
**Evidence of disparities** (systematic review confirms harm is real + widespread) → **Root causes** (bias in data, design, evaluation) → **Solutions** (inclusive practices + rigorous subgroup validation) → **Need for systemic change** (policy, funding, organizational culture)

This validates ED-415's evidence base at scale: harm to CLD populations isn't anecdotal; it's systematic and documented across 129 studies.

**Scope & Limits:**
- Focuses on health/social care AI; methods may transfer to other domains
- Identifies problems + general solutions; specific implementation varies by context
- Calls for policy change + resource allocation

---

### **EVALUATION (~400 words)**

**Persuasiveness:**
I am convinced because:

1. **Systematic Evidence:** 129 studies provide overwhelming evidence this isn't edge case. Every AI category studied (diagnostics, treatment planning, risk prediction) shows disparities for CLD populations. Undeniable pattern.

2. **Directly Validates ED-415:** Your research brief documents diagnostic harm; Marko proves this harm extends across all healthcare AI. Personal experience (Dominican ADHD underdiagnosis) is exemplar of broader systemic pattern.

3. **Solutions-Oriented:** Doesn't just catalogue problems; recommends concrete solutions (inclusive data, community co-design, rigorous validation, policy guardrails). Connects to Nadarzynski + Lekadir frameworks.

4. **Calls for Power-Sharing:** Emphasizes that solutions require CLD communities in **governance + decision-making**, not just consultation. Aligns with your EQUITAS framework's systems-level approach.

**Weaknesses/Gaps:**

1. **Limited on Solutions Effectiveness:** Reviews problems + suggested solutions but provides limited evidence that these solutions actually work. Are there studies showing inclusive design prevents disparities? Need follow-up research.

2. **Implementation Burden:** Calls for systemic change but less specific on how to overcome organizational/financial barriers.

3. **Intersectionality Gaps:** While covering multiple marginalized groups separately, less on *intersectional analysis* (e.g., Black + low-SES + woman = compounded bias).

**Standards & Accountability:**
- ✅ Documents disparities rigorously (systematic review)
- ✅ Recommends specific practices
- ⚠️ Limited evidence those practices eliminate disparities

**EQUITAS Alignment:**
- ✅ Equity-Centered, Universal, Systems-Level
- ✅ Highlights structural change needed
- ⚠️ Robustness: limited evidence on effectiveness of solutions

**Implications for CLD Trust & Practice:**
For **CLD patients:** Proof that AI designed without them harms them. Trust-building requires evidence developers *did* design for diverse populations.

For **healthcare providers:** Shows liability risk if using non-inclusive AI. Risk mitigation = inclusive design.

For **my research:** Marko provides **empirical justification** for every equity requirement in your framework. Can't hand-wave equity; 129 studies prove it's necessary.

---

### **Quick Evidence Hooks:**
- **Quotes:** "AI systems often perform poorly for women, racial/ethnic minorities, lower socioeconomic groups due to biased data and lack of inclusivity."
- **Evidence:** Disparities documented across diagnostics, treatment planning, risk prediction
- **Solutions:** Diverse training data, community co-design, subgroup-specific validation, policy enforcement

### **Notes for Final Paper:**
- **Empirical anchor** for all 5 other papers' recommendations
- Shows that calls for equity aren't performative; they're responses to documented harm
- Bridges ED-415 evidence (your research) to IDAI-700 solutions (Nadarzynski + Lekadir + Chen + Sagona)

**WORD COUNT: Summary [__] + Evaluation [__] = _____ / ~800**

---

---

## **ENTRY 6: [YOUR 6TH PAPER - TBD]**

**Which paper are you selecting?**
- Option A: **Goisauf et al. (2025)** - Trustworthiness & multistakeholder AI
- Option B: **Baumgartner et al. (2023)** - Fair & equitable AI: social science perspectives
- Option C: **Another paper** from your research?

**For now, I've provided ENTRIES 2-5 in this format.**

---

## **HOW TO USE THIS GUIDE:**

1. **Read the Summary section** - pulls from your notes
2. **Customize with your voice** - add personal insights, reframe language, emphasize *your* perspective
3. **Expand Evaluation** - this is where your intellectual work shows most; adjust "I am convinced because..." to match YOUR reasoning
4. **Add specific quotes** from papers - these templates show structure; populate with actual text
5. **Fill word counts** as you write
6. **Polish for voice + purpose** - ensure it amplifies your goal (equitable AI for CLD communities)

---

## **TIME MANAGEMENT:**

- **Entries 2-5 template complete:** ~30 min to customize each (2.5 hours total)
- **Entry 6 (if you choose one of these):** ~30 min
- **Total writing:** ~3 hours
- **Buffer for revision/submission:** ~4 hours

**You have 7.5 hours. This is doable.** ✓

---

## **NEXT STEP:**

Would you like me to:

**Option A:** Help you complete **Entry 2 (Lekadir)** with full customization, then you use that model for 3-5?

**Option B:** Fill in Entry 6 (help you choose/synthesize your 6th paper)?

**Option C:** Create a **checklist for your polish pass** (voice amplification guide)?

What serves you best right now?