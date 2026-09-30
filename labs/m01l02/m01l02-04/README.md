# m01l02-04 · Turning records into the two throughput numbers

**Lesson:** [Throughput: Change Lead Time And Deployment Frequency](https://learnsome.tech/learn/devops-course/m01l02) (lesson 1.2, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can define change lead time and deployment frequency in DORA's own words, say what each one excludes, and compute both from a real git history rather than from a survey answer.

In the lesson: And here is the arithmetic, which is smaller than people expect. Lead time is the deployment time minus the time the change was authored, for every change in every deployment: one number per change, not one per deployment, because a deployment carrying six commits has six lead times inside it. The window is the span from the first deployment to the last, measured from the history rather than assumed, which matters because a team that stopped deploying for a fortnight should see that fortnight in the denominator. Frequency is then the deployment count divided by that window, scaled to a week, and the median of the lead times is printed beside it.

## Files

- [`starter/dora_metrics.py`](starter/dora_metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/dora_metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: one lead time per change, not per deployment
   - Line 3: the window is measured from the history, not assumed

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
