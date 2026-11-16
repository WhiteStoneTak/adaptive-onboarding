# Accessibility, privacy, and user safety

Accessibility and trust are product requirements, not optional optimization metrics.

## Accessibility checklist

- Support screen readers with labels, focus order, descriptive errors, and meaningful progress announcements.
- Keyboard navigation must access every action; visible focus; no keyboard traps.
- Ensure readable contrast and responsive text scaling; support Dynamic Type where relevant.
- Do not rely on color, motion, timer expiration, or gestures alone to convey meaning.
- Honor reduced-motion preferences and avoid disabling information under reduced motion.
- Provide alternatives to drag-only, camera-only, or gesture-only entry when feasible.
- Localize copy, input formats, date/time, currencies, and right-to-left layouts as needed.

## Safety and consent

- Never expose private data to make guest access possible.
- Preserve required SSO/KYC/MFA/age gates and safe role assignment.
- Ask permissions transparently with accurate purpose and timing.
- Preview output must be labeled demo/sample when not based on user data.
- Subscription/trial messaging must clearly disclose current and future charges, renewal, and exit/cancellation.
- Avoid false scarcity, forced continuity, hidden opt-ins, manipulative defaults, and unnecessary notifications.
- Collect only data needed for specified purposes; minimize retention; do not send personal data to analytics by default.
- For sensitive domains, require domain-specific human review and current official platform/legal requirements.

## Failure and recovery

Plan for: offline, slow network, declined permission, invalid input, API failure, payment rejection, auth session expiry, abandoned setup, reinstallation, returning member, partially imported data, and multi-device handoff.

For each failure, specify message, safe next action, data persistence, rollback, and whether the system retries automatically. Avoid repeating irreversible actions.

## Implementation safeguard

Before modifying production-facing code, inspect environment configuration and use feature flags or isolated changes where practical. Run tests; state clearly what was actually tested. Do not deploy, publish, message external users, create subscriptions, or change permissions unless explicitly authorized.
