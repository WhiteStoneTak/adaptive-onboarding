---
name: adaptive-onboarding
description: Evidence-aware design, audit, implementation, and experimentation for onboarding in any digital product. Use for first-run experiences, signup, guest access, setup, permissions, personalization, activation, paywalls, tutorials, and retention. Tailor the flow to the actual audience, job, constraints, and business model.
license: MIT
metadata:
  author: Takumi Shiraishi (WhiteStoneTak)
  version: "1.0.0"
---

# Adaptive Onboarding

Design **the right path to meaningful value for this product**, not a universal collection of welcome screens.

## Non-negotiable principles

1. **Inspect before prescribing.** Study the actual product, audience, entry channel, available code/screens, analytics, and existing decisions. Do not assume that a famous product's flow transfers.
2. **Define the user's job.** Specify who arrives, why, what was promised, the triggering situation, and the observable first meaningful value (FMV).
3. **Protect prerequisites.** Authentication, identity, security, billing entitlement, privacy consent, accessibility, and regulatory gates may be essential. Do not bypass them for conversion.
4. **Distinguish output from value.** A generated answer, completed signup, or clicked CTA does not prove that the user obtained a useful result. Label simulations and sample content honestly.
5. **Optimize for sustained outcomes.** Track meaningful activation and later retention, not only registration or onboarding completion.
6. **Treat evidence conditionally.** Cite population, intervention, measure, time horizon, uncertainty, and transfer risks. A company result is not a universal rule.
7. **Prefer reversible changes.** Instrument, test, use flags when practical, and preserve rollback. Do not silently deploy, charge, message, or collect personal data.
8. **Respect the user's scope.** Design/research requests are not authorization to edit code; implementation requests call for targeted changes with verification.

## Choose the mode

- **AUDIT:** Review existing screens/code, document actual drop-offs and inferred concerns, rank fixes by severity and expected impact.
- **DESIGN:** Provide a context brief, 2+ plausible flows when meaningful alternatives exist, step purposes, dependencies, copy, failures, and metrics.
- **IMPLEMENT:** Inspect code conventions, make minimal changes, preserve auth and safety contracts, add tests and rollback instructions.
- **EXPERIMENT:** Form falsifiable hypotheses, define cohorts/denominators, guardrails, analysis plan, and go/no-go criteria.
- **RESEARCH:** Compare first-party studies, controlled tests, observational evidence, and official guidance; explain limitations.

## Workflow

### 1. Context, constraints, and existing evidence

Review actual files, product documentation, user research, screen recordings, existing funnel events, and entry sources when available. Record a **Known / Assumed / Unknown** table. If critical details are missing, ask only questions needed for a correct or safe recommendation; otherwise proceed with labeled assumptions.

Capture:

| Dimension | Required considerations |
| --- | --- |
| User / buyer | Who uses, pays, decides, administers, and invites? Different roles? |
| Job & trigger | What happened before opening? What concrete outcome is sought? |
| Entry context | Organic search, ad promise, deep link, invite, SSO rollout, returning user? |
| First value | Observable meaningful result and how to validate it; time and effort to reach it |
| Dependencies | Account, KYC, approval, pairing, permissions, integration, data, other users, payment |
| Risk | Financial, medical, legal, child safety, privacy, reliability, accessibility |
| Model | Freemium, prepaid, trial, subscription, enterprise contract, usage billing |
| Platform | iOS, Android, web, desktop, embedded, API, hardware |
| Maturity | Prototype, launched product, established product, available cohort sizes |

Use [product archetypes](references/product-archetypes.md) as prompts rather than prescriptions.

### 2. Define value and its prerequisite graph

Write:

> For [person] arriving from [context], first meaningful value is [outcome], supported by [behavior and/or feedback].

Distinguish **first output**, **first understood value**, **first repeat value**. Work backward from the outcome and tag every prerequisite as **required now**, **deferrable**, **optional**, or **removable**. Separate security/consent requirements from UX preferences. Include returning, interrupted, denied, and offline states where relevant.

### 3. Compare conditional flows

Consider at least two paths if there is a material tradeoff: try-before-signup vs signup-first; sample preview vs live data; self-service vs guided enterprise; immediate paywall vs post-value vs intent-triggered; full setup vs progressive disclosure.

For each step record **intent, user benefit, required data, failure/recovery, skip/defer option, measurement**. Remove a step if it serves no user value, safety, comprehension, or legitimate downstream operation. A necessary question may actually *improve* outcomes.

Read [pattern decision guide](references/pattern-decision-guide.md) and [accessibility & safety](references/accessibility-and-safety.md). Never assume:
- Fewer screens always win.
- Signup must always be last.
- Every question must change the immediately following screen.
- Progress bars reliably improve completion.
- The first win must trigger a paywall.
- Personalization justifies collecting every available data point.
- Better signup conversion proves better retention.

### 4. Apply the evidence carefully

Check [evidence dossier](references/evidence.md) before quoting studies and company lifts.

Mark claims as **controlled experiment**, **synthesis/observational**, **official guidance/company case**, or **hypothesis**. Include denominators and relative-vs-percentage-point distinctions where known. Never extrapolate an experiment's exact effect size to another product; verify current policies against official docs when implementing.

### 5. Specify measurement and test strategy

Use [instrumentation & experiments](references/instrumentation-and-experiments.md). Define eligibility, exposures, cohorts, first-value event, D1/D7 (or product-appropriate) meaningful return, failures, consent and support guardrails, refund/cancel rates where relevant, and instrumentation integrity.

Small sample: usability observation, interviews, task-based tests. Adequate traffic: randomized controlled experiment with precommitted success metrics and guardrails. Interpret retention by cohort and avoid survivor/selection bias.

### 6. Deliver the requested artifact

- AUDIT: use [audit template](assets/audit-template.md); distinguish observed from inferred problems.
- DESIGN: use [brief template](assets/onboarding-brief.md); include alternatives and state transitions.
- EXPERIMENT: use [experiment plan](assets/experiment-plan.md); include rollback and follow-up.
- IMPLEMENT: report inspected files, exact changes, tests run, accessibility checks, constraints preserved, and production claims not verified.
- RESEARCH: source matrix, conflicting results, applicability, uncertain or missing evidence.

## Mandatory self-check

- Did the proposal fit the product and entry intent rather than a template?
- Is FMV a user outcome rather than merely an event?
- Did we preserve mandatory auth, permissions, consent, legal and safety requirements?
- Are errors, refusal, interruption, and returning flows defined?
- Are misleading previews, dark patterns, hidden fees, and fabricated progress excluded?
- Are cohorts, denominators, guardrails, and sustained-value metrics explicit?
- Is every external effect size contextualized and citation-grounded?
- Are changes reversible and limited to the requested scope?

**Never claim that untested implementation or unreleased changes improved conversion.**
