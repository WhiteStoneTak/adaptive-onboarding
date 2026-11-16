# Instrumentation and experiments

## Purpose: meaningful value, not completion vanity

Define three separate events:

1. **First output:** system generated or displayed something.
2. **First meaningful value (FMV):** user completed a useful task or demonstrated comprehension/success, measured with an observable proxy and/or validated feedback.
3. **Repeat meaningful value:** user voluntarily repeats a relevant job within a product-appropriate window.

A login is not FMV; clicking 'Finish' is not proof of learning; a meeting note must be useful before its creation counts as success.

## Funnel event contract

Suggested events (adapt names to codebase conventions):

| Event | Description | Required properties |
|---|---|---|
| `onboarding_exposed` | Eligible first screen appeared | anonymous/cohort id, variation, entry source, timestamp |
| `onboarding_step_viewed` | User encountered a decision | step id, session id |
| `onboarding_step_completed` | Step successfully completed | step id, outcome |
| `onboarding_step_skipped` | Optional action declined | step id, explicit reason if known |
| `permission_result` | OS permission decision | permission type, granted/denied (never personal content) |
| `signup_completed` | Identity established | cohort, method category (no credentials) |
| `first_output` | Initial system response | output category, latency |
| `first_value_confirmed` | Useful user outcome observed | metric version, evidence source |
| `repeat_value_confirmed` | Meaningful repeat task | metric version, days since exposure |
| `billing_action` | Trial, subscribe, cancel, refund | product tier, action, no payment secrets |
| `onboarding_error` | Failure/recovery state | safe error class, stage, recovered? |

Use one stable pseudonymous assignment key where allowed, deduplicate retries by event id, and maintain explicit schemas and metric versions. Prefer server-side success confirmation for costly or irreversible actions. Do not log prompts, images, exact health info, personal messages, credentials, or other sensitive content as a default.

## Recommended metrics

- **FMV rate:** distinct eligible exposed users with confirmed FMV / distinct eligible exposed users.
- **Time to value:** distribution (median, p75/p90) for eligible users, handling people who never activate rather than reporting only activated users.
- **Meaningful D7 retention:** proportion of original eligible cohort that returns and performs the designated meaningful task in an appropriate seven-day window. Document timezone, date vs rolling period, and reactivation.
- **Qualified activation:** FMV with task/role relevance; exclude sample-only outputs if they do not fulfill the genuine job.
- **Guardrails:** crash/error, denied consent, unintended messages, user complaints, refund/cancel, support demand, user safety, inaccessible states, infra cost.
- **Business outcome:** net revenue/LTV or team activation depending on product. Do not treat signup or trial-start as the ultimate outcome.

Segment by entry promise, acquisition source, new/returning user, device, locale, buyer/user role, and product cohort where meaningful and permitted.

## Testing strategy

### Low traffic

Run task-oriented usability sessions and user interviews. Inspect completion, confusion, comprehension, errors, and observed usefulness. Qualitative observations do not establish causal uplift. Maintain a prioritized issue log with direct observations and hypotheses clearly separated.

### Adequate traffic

- Write the primary hypothesis, estimand, sample sizing approach, planned duration, and guardrails **before** assignment.
- Assign at the stable user level, not per screen view; prevent sample-ratio mismatch and contamination.
- Compare on an intention-to-treat denominator where feasible; don't analyze only users who reach the paywall.
- Report absolute rate, relative effect, uncertainty interval, and variance; avoid declaring 'significant' without the chosen statistical method.
- Track retention by signup cohort rather than pooling users of different ages.
- Keep backend/business changes stable or document confounding factors.
- Use gradual rollout/flags when appropriate and stop for security, fraud, payment, or safety issues.

## Decision memo

Document: variant and exposure; sample coverage; primary metric result; guardrails; subgroup differences; unknowns and biases; decision (ship/iterate/revert); follow-up experiments; owner/date. If traffic is insufficient, state inconclusive rather than claiming a win.

## Common analytical failures

Survivorship bias, selection by self-reported intent, Simpson's paradox, short windows, instrumentation discrepancies, bot traffic, misattributed deep links, privacy suppression, multiple testing, and confusing relative percentage increases with percentage points.
