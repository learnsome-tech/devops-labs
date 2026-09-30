# m01l05-05 · One script, five metrics, one definition

**Lesson:** [The Four Keys History And Retiring MTTR](https://learnsome.tech/learn/devops-course/m01l05) (lesson 1.5, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can explain why almost every article names four DORA metrics, what changed in 2023 and 2024, and why mean time to restore was replaced rather than renamed.

In the lesson: Here is the header of the script we have been running, and it is doing something more valuable than the arithmetic below it. It says what a deployment is in this repository and what makes one count as failed, written down where the numbers are produced rather than in a wiki page nobody opens. When the definitions changed in twenty twenty three and twenty twenty four, teams with their rules in a file like this changed one file. Teams whose rules lived in a dashboard vendor's defaults found out that their history had quietly changed meaning underneath them, and in the same place they learned that nobody could say when.

## Files

- [`starter/dora_metrics.py`](starter/dora_metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/dora_metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 5: the definition of a deployment, written down where it is used
   - Line 7: and the definition of a failure, in the same place

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
