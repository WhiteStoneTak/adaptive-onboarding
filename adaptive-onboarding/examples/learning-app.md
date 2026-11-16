# Worked example: learning application

**Illustrative design exercise; not experimental results.**

## Context

Audience: high-school learners arriving from an Instagram post explaining parallel electrical resistance. Their job is to understand the concept and solve a related problem. Some users may be minors. Avoid unneeded personal information and misleading learning claims; account for model inference costs.

## First meaningful value (FMV)

The learner successfully applies the concept to a short, novel problem or otherwise demonstrates understanding. An AI-generated explanation alone does not prove learning.

## Alternative flows

### A. Lesson-first, then optional saved progress

Relevant deep link → sample or typed problem → guided explanation → comprehension check → offer to save progress with an account → optional reminder.

Pros: aligns with acquisition intent; minimizes pre-value decisions.
Risks: abuse/cost, lost unsaved progress, limited safe personalization.

### B. Account-first learning workspace

Identity and necessary eligibility → choose learning goal → problem → explanation → comprehension check → saved plan.

Pros: persistent history, parental or school controls where necessary.
Risks: may block a learner's immediate objective.

## Conditional decision

Start with A for safe sample problems if there is no mandatory identity requirement. Use B for school-managed SSO or legally required protections. Protect minors either way.

- If a deep link already establishes the subject, do not redundantly ask for it.
- Request camera access only when the user chooses to scan a question.
- Explain exactly when progress is temporary vs saved.
- Keep the paywall optional or intent-triggered as a hypothesis, not a universal rule.
- Math must be accessible to assistive technology; don't hide the explanation under motion effects.

## Measurement

Eligible deep-link exposures → completed and verified comprehension; time to FMV; meaningful repeat learning within a week; error and misinformation rates; privacy/consent incidents; compute spend.

## Counterexample

An employee assigned a mandatory compliance course may need identity, enrollment, and audit logging before learning begins. Do not force guest mode.
