# m01l03-05 · Counting the two ratios

**Lesson:** [Instability: Change Fail Rate And Deployment Rework Rate](https://learnsome.tech/learn/devops-course/m01l03) (lesson 1.3, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can state DORA's definitions of change fail rate and deployment rework rate, explain how they differ, and derive both from the record a repository already keeps.

In the lesson: In code the difference is two list comprehensions that read the same evidence from opposite ends. Rework is the set of deployments that carried a remediation into production. Failed is the set of deployments that a later remediation pointed at. Both are divided by the same denominator, the total number of deployments, and both are reported as percentages. If you take one idea from this lesson, take that: these are ratios over deployments. Not over commits, not over incidents, and not over tickets. When somebody hands you a change fail rate, the first question to ask is what they put on the bottom of the fraction.

## Files

- [`starter/dora_metrics.py`](starter/dora_metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/dora_metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: rework: deployments that carried a remediation
   - Line 3: failed: deployments a later remediation pointed at

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
