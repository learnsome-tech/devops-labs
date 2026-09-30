# m01l04-04 · Recovery, as arithmetic over the record

**Lesson:** [Restoration: Failed Deployment Recovery Time](https://learnsome.tech/learn/devops-course/m01l04) (lesson 1.4, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can define failed deployment recovery time exactly, say which failures it covers and which it does not, and compute it from the deployment record.

In the lesson: The computation is three lines. For every deployment that a later trailer named as failed, find the deployment that carried the remediation into production, and take the difference between the two moments. Notice what is not in there. There is no ticket system, no alert timestamp, and no human judgement about when the incident felt over. Two deployment times, subtracted. That is deliberately crude, and it has one enormous advantage over a nicer definition: everybody computes the same number, so a team can compare this quarter with last quarter and argue about the software instead of about the measurement.

## Files

- [`starter/dora_metrics.py`](starter/dora_metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/dora_metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 2: only deployments a later trailer named as failed
   - Line 3: the deployment that carried the remediation into production

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
