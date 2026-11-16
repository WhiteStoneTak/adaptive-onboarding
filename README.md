# Adaptive Onboarding

**Evidence-aware onboarding design, audit, implementation, and experimentation for Codex and Claude Code.**

This open-source agent skill adapts to the product. It does **not** assume that every application should delay registration, provide guest access, ask fewer questions, use a progress bar, or display a paywall after the first win. It starts with the user's job, entry point, prerequisites, safety constraints, business model, and available evidence.

**Maintainer:** [Takumi Shiraishi](https://github.com/WhiteStoneTak) · **License:** MIT

## What it does

- **Audit** an existing onboarding journey against actual code, screenshots, analytics, and user intent.
- **Design** alternatives with explicit trade-offs, interruptions, accessibility, privacy, and failure states.
- **Implement** the chosen flow in an existing codebase, with tests and safe rollback.
- **Experiment** with well-defined first meaningful value (FMV), cohorts, guardrails, and defensible conclusions.
- **Research** design options using documented experiments and official guidance—without treating case studies as universal rules.

Supported contexts include B2C mobile apps, educational software, creative AI, B2B SaaS, enterprise SSO, fintech/health, developer tools, marketplaces, subscription media, and hardware pairing.

## Install

Both platforms use a standard `SKILL.md` folder. A single canonical skill lives in [`adaptive-onboarding/`](adaptive-onboarding/).

### Codex (global)

```bash
git clone https://github.com/WhiteStoneTak/onboarding.git ~/onboarding-skill
mkdir -p ~/.agents/skills
ln -sfn ~/onboarding-skill/adaptive-onboarding ~/.agents/skills/adaptive-onboarding
```

Then in Codex, invoke `$adaptive-onboarding`, or ask to audit/design/implement onboarding.

### Claude Code (global)

```bash
git clone https://github.com/WhiteStoneTak/onboarding.git ~/onboarding-skill
mkdir -p ~/.claude/skills
ln -sfn ~/onboarding-skill/adaptive-onboarding ~/.claude/skills/adaptive-onboarding
```

Then use `/adaptive-onboarding`, or ask naturally about an onboarding problem.

**Using both:** Clone only once, then run both sets of `mkdir` and `ln` commands. If you already have a checkout, skip cloning. Avoid overwriting an existing installed skill without reviewing it. Restart the agent if discovery is stale.

### Per-project install

Copy or symlink `adaptive-onboarding/` into `.agents/skills/` for Codex or `.claude/skills/` for Claude Code. The repo also includes project-local symlinks for opening this repository directly in both tools.

## Example requests

```text
$adaptive-onboarding Audit the first-run flow of this iOS app.
Account creation is required for private household data. Identify unnecessary friction without weakening security.
```

```text
/adaptive-onboarding Design two onboarding alternatives for a B2B tool requiring SSO, admin provisioning, and data import. Include recovery paths and guardrail metrics.
```

```text
$adaptive-onboarding Implement the selected guest-first flow in this repo. Keep pricing and auth contracts unchanged; add tests and feature-flag rollback.
```

## Evidence, not dogma

The skill distinguishes controlled experiments, observations, company guidance, and product-specific hypotheses. One particularly instructive [Atlassian experiment](https://www.atlassian.com/blog/how-we-build/life-of-a-growth-experiment) found that more specific product explanations increased Trello→Jira expansion by nearly 30%, while a similar change for Bitbucket→Jira decreased expansion by 12% and retention by 11%. Copying a famous app's flow without considering the audience can backfire.

Read [the evidence dossier](adaptive-onboarding/references/evidence.md), [product archetypes](adaptive-onboarding/references/product-archetypes.md), and [measurement guidance](adaptive-onboarding/references/instrumentation-and-experiments.md).

## Structure

```text
adaptive-onboarding/
  SKILL.md
  references/
    evidence.md
    product-archetypes.md
    pattern-decision-guide.md
    instrumentation-and-experiments.md
    accessibility-and-safety.md
  assets/
    onboarding-brief.md
    audit-template.md
    experiment-plan.md
  examples/
    learning-app.md
    enterprise-saas.md
    security-sensitive-app.md
```

The main `SKILL.md` is deliberately concise; supporting files are loaded only when needed.

## Safety and methodology

No universal screen count, conversion benchmark, or paywall timing is prescribed. Product-specific safety and regulatory requirements take precedence over conversion optimization. The skill never silently sends notifications, signs users up, exposes private data, bills customers, or deploys production changes. Research citations include limitations.

## Contributing

Improvements and corrections are welcome. In issues/PRs, describe the product context, proposed change, evidence level, and how it can be evaluated. Do not add unsupported universal heuristics or unverified statistics.

## Documentation

- [OpenAI — Building skills](https://learn.chatgpt.com/docs/build-skills)
- [Anthropic — Claude Code skills](https://code.claude.com/docs/en/skills)
- [Agent Skills specification](https://agentskills.io/specification)
