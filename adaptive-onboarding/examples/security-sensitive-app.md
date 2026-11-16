# Worked example: security-sensitive health or finance product

**Illustrative design exercise; not legal, medical, or regulatory advice.**

## Context

A user needs to access private account information. Identity/eligibility verification, consent, secure auth, auditability, and reliable error handling may be required. Always verify jurisdiction-specific requirements.

## FMV

An authorized user receives accurate, actionable, private information or completes a safe meaningful task. Verification itself is a prerequisite, not the result.

## Alternative flows

### A. Verification-first

Explain benefit/trust → check eligibility and identity → required consent and authentication → secure data connection → validated real result → optional customization.

Prioritize this where identity is mandatory before protected data access.

### B. Honest sample preview

Show expressly synthetic example (not personal information) → explain needed checks → verification and consent → live result.

Suitable when early product explanation is valuable and demos are lawful and safe; never imply demo output is real.

## Safety guardrails

Never skip mandatory age, KYC, MFA, medical consent, or entitlement checks for conversion. Do not collect credentials in untrusted screens. Preserve alternative access, screen-reader support, error recovery, privacy disclosures, and human escalation where needed.

## Measurement

Authorized FMV, comprehension of consent, errors and recovery, security incidents, support burden, and safe repeat use. A conversion lift is not success if harms increase.

## Counterexample

An informational, non-personal health education website may be useful without identity verification. Do not impose verification-first by default.
