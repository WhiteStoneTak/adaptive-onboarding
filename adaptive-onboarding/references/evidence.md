# Research evidence dossier

Updated: 2026-11-17. Evidence is **contextual, not a set of universal conversion promises**. Inspect the original source before quoting exact numbers. Distinguish relative change from percentage-point change.

## Company experiments

### Atlassian: the same idea can help one cohort and hurt another

Source: [Atlassian — Life of a Growth Experiment](https://www.atlassian.com/blog/how-we-build/life-of-a-growth-experiment).

In cross-product onboarding, clearer Jira use-case messaging reportedly raised Trello→Jira click-through approximately 20% and expansion nearly 30%. In a Bitbucket→Jira test, similar messaging **reduced** expansion by 12% and affected a retention guardrail by −11%. **Limit:** existing customers discovering another product, not new consumer installs. **Use:** segment by entry context; test rather than transplanting a screen.

### Duolingo: delaying signup, not a magic screen count

Source: [First Round Review interview with Duolingo growth leader](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker/).

An account-creation timing experiment reportedly improved DAU around 20%. **Limit:** operator interview, not an independently reproduced published experiment; no universal '16 screens' recommendation. **Use:** consider try-first for safely accessible value.

### Duolingo: lower early commitment

Source: [Duolingo — Improving the streak](https://blog.duolingo.com/improving-the-streak/).

Allowing a completed lesson rather than a personal daily goal to maintain a streak reportedly improved D14 retention 3.3%, DAU 1%, and streak-holding user share 10.5% over twenty days. **Limit:** an existing learning product and streak system; engagement is not necessarily learning.

### Pinterest: signup wins may hide retention damage

Source: [Pinterest Engineering — Signup flow experiments](https://medium.com/pinterest-engineering/).

Pinterest has described optimizing signup while inspecting longer-term cohort retention; changes that improve short-term signup can fail longer-term guardrails. **Limit:** verify the specific article and metric before quoting a numerical result; an engineering anecdote is not an externally audited randomized dataset. **Use:** never ship on registration uplift alone.

### Google Firebase / Fabulous

Source: [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing).

A public Google case study described removal of an introductory letter and commitment request from a habit-building app, with roughly 7% higher onboarding completion and no reported retention decline in the measured period. **Limit:** case-study reporting and product-specific flow.

## Usability research and peer-reviewed synthesis

### Nielsen Norman Group: deck-of-cards tutorials

Source: [Mobile Tutorials: Wasted Effort or Efficiency Boost?](https://www.nngroup.com/articles/mobile-tutorials/).

A usability experiment with 70 people and four relatively simple mobile apps did not find a statistically significant advantage to upfront card tutorials for task success or time. Users with tutorials felt tasks were harder. **Limit:** don't generalize to safety-critical or complex enterprise setup. **Use:** test contextual help.

### Choice overload is conditional

Source: [Scheibehenne, Greifeneder & Todd (2010), Journal of Consumer Research](https://doi.org/10.1086/651235).

A meta-analysis of 50 experiments (63 conditions, 5,036 participants) reported mean choice-overload effect near zero and substantial between-study variability. **Use:** reduce confusing choices based on task evidence, not a fixed maximum number.

### Progress indicators are not guaranteed to help

Source: [Villar, Callegaro & Yang (2013), meta-analysis of web survey experiments](https://research.google/pubs/where-am-i-a-meta-analysis-of-experiments-on-the-effects-of-progress-indicators-for-web-surveys/).

Across 32 randomized survey experiments, a constant-speed progress indicator did not yield a significant overall reduction in dropout. **Limit:** web surveys, not onboarding apps. **Use:** only show accurate and useful progress.

### Permission requests depend on expectation

Source: [Google Research / USENIX Security — A large-scale study of users' Android permission behavior](https://research.google/pubs/a-large-scale-study-of-users-behaviors-expectations-and-engagement-with-android-permissions/).

Study of 1,719 users across ten regions found unexpected requests more than twice as likely to be declined; explained requests had roughly half the denial rate. **Limit:** largely observational/statistical associations, not proof a particular pre-permission screen increases retention. **Use:** align permission timing with the action that needs it.

### Endowed progress

Source: [Nunes & Drèze (2006), The Endowed Progress Effect](https://doi.org/10.1086/500480).

Experimental evidence that presented head starts can affect goal persistence in some loyalty settings. **Limit:** not a blanket endorsement for gamification or fabricated accomplishments. **Use:** authentic early wins, truthful achievement.

## Official recommendations and observational benchmarks

### Apple Human Interface Guidelines

Sources: [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple).

Prefer useful early interactions and appropriately delayed account requests when feasible; communicate permissions and requirements. **Not an RCT;** essential security/identity may override try-first.

### Android

Source: [Android design — Onboarding](https://developer.android.com/design/ui/mobile/guides/patterns/onboarding).

Progressive, contextual, user-focused onboarding recommendations. **Not proof** that any screen count or form pattern wins.

### RevenueCat subscription benchmarking

Source: [State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps).

In this vendor dataset, median day-35 download-to-paid conversion was reported around 10.7% for hard-paywall apps and 2.1% for freemium apps. **Limit:** observational comparison across products and audiences, not the causal effect of inserting a hard paywall. **Use:** product-specific trial/paywall experiments with churn and refund guardrails.

## Do not repeat unsupported claims

- "82% of users only see onboarding" — no verified universally defined primary source.
- "Duolingo always asks for an account after 16 screens" — varies by experiment, version, and audience.
- "A first-win paywall always outperforms other models" — not established.
- "More personalization or fewer choices always helps" — contradicted by context-dependent findings.
- "An A/B-tested improvement elsewhere will deliver the same uplift here" — invalid transfer.

## Source-use protocol

For any empirical claim, record: publisher; link; publication date; cohort and sample; intervention and comparator; metric (denominator); time window; numerical effect; absolute vs relative; design; caveats. When original content is unavailable, do **not** present numerical effects as verified. Recheck rapidly changing platform and payment policies at implementation time.
