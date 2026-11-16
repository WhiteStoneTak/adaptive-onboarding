# Pattern decision guide

Do not score a flow from screen count alone. For each decision describe context, candidate options, tradeoffs, required prerequisites, risks, expected mechanisms, and a falsifiable validation plan.

## Signup and identity

- **Guest/try-first:** useful when real value can be safely delivered without identity, data loss, high resource abuse, or protected content. Offer save/sync signup at a relevant moment.
- **Signup-first:** appropriate when identity is essential (banking, enterprise SSO, protected records, organization workspace, age eligibility, entitlement).
- **Preview-first:** when true value requires a meeting, hardware, team adoption, or external data. Clearly mark synthetic/demo content.
- **Progressive account:** defer noncritical profile fields while meeting necessary legal/security needs.

Test task completion, qualified activation, privacy failures, and retention—not only signup.

## Explanations and tutorials

- Contextual hints and learn-by-doing can reduce pre-task burden.
- A richer upfront explanation can help unfamiliar, complex, consequential, or cross-product workflows.
- Show relevant benefits/constraints; avoid feature lists that do not affect next action.
- Provide user-controlled skip and replay when appropriate; never hide required safety guidance.
- Distinguish comprehension from taps; usability-test the real task.

## Questions and personalization

- Ask when answers improve experience, eligibility, safety, clarity, permissions, or legitimate later operations.
- Prefer inferred *nonsensitive* information when reliable and privacy-respecting; allow correction.
- A question can provide useful orientation even when it doesn't immediately alter the next screen.
- Consider bundles of related fields instead of an arbitrary one-question-per-screen rule.
- Measure whether personalization actually increases meaningful outcomes and whether data collection causes friction.

## Progress and motivation

- Show progress when bounded and meaningful; never fabricate steps or completion.
- For long/unknown processes, status messages may be more truthful than a percentage.
- Give authentic small wins and helpful next actions; avoid artificial urgency, shame, or coercion.
- Optional reminders should explain purpose and be requested at a relevant point.

## Permissions and consent

- Ask at the moment users understand the need, unless an earlier gate is essential.
- State what data is accessed, processed, stored, or shared; permit refusal/retry paths when feasible.
- Never use faux operating-system dialogs to trick consent.
- Check current iOS, Android, browser, and legal requirements.

## Paywalls and trials

Candidate patterns: hard paywall; first-win paywall; usage-limit; premium-intent; team/contract-led purchase.
Evaluate fit with buyer awareness, free-user network effects, unit economics, entitlement, refunds, cancellations, long-term value, and compliance. No universal optimal placement.
Show price, billing period, trial conditions, renewal, and cancellation clearly. Do not start a trial silently.

## Entry-aware flow design

A user from a calculus tutorial should not automatically land on the same generic homepage as an enterprise-invited admin. Deep links should preserve the user promise and destination securely, but never skip authentication/authorization where required.

## Adversarial checks

Ask what will break if users are minors, multilingual, using assistive tech, offline, interrupted, returning, not ready to subscribe, or unwilling to grant permission. Explore a second plausible flow before selecting one.
