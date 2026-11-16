# Worked example: enterprise analytics SaaS

**Illustrative design exercise; not experimental results.**

## Context

An analyst receives a secure invite to a private analytics dashboard. The buyer is a finance director; IT is the administrator. SSO, roles, audit trails, and protected data are mandatory.

## FMV

The analyst securely opens the intended authorized dashboard, understands a reliable result, and completes a relevant work action. Merely accepting an invite does not count.

## Alternative flows

### A. SSO and authorization first

Invite deep link → verify identity and SSO → check workspace role → open intended dashboard → contextual guide → real task completion → optional preferences.

This should be the default for actual protected enterprise data.

### B. Sample preview, then authenticated workspace

Public landing → explicitly synthetic demo data → clarify product value → account/SSO + permissions → real dashboard.

Appropriate for prospects still evaluating the product, but **not** a bypass for an invited employee's authorization.

## Failure and recovery

Expired invite; wrong identity provider; missing administrator approval; insufficient role; failed connector; incomplete data import; offline or slow network. Recover safely without exposing data.

## Measurement

Invitation exposure denominator, authorized first meaningful task, time to FMV, repeat work, support contacts, security/role violations, and error recovery. Split analyst/admin/buyer and invited/prospect cohorts.

## Counterexample

A solo freelancer with public dummy data and self-serve signup may benefit from sandbox-first instead.
