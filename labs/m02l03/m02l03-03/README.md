# m02l03-03 · The release identifier, in the application

**Lesson:** [Build, Release, Run And Processes](https://learnsome.tech/learn/devops-course/m02l03) (lesson 2.3, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can separate build, release and run as three distinct stages with an append-only release ledger, and explain why a stateless, share-nothing process is a deployment requirement rather than a style preference.

In the lesson: Here is the good variant again, with attention on the release. The identifier arrives as config, set by whatever performs the release stage, and it is not something the application can invent for itself. Then every log line carries it. That one habit changes incident work: when two versions are running side by side during a rolling update, and one of them is misbehaving, the logs already tell you which. Without it you are reduced to guessing from timestamps, and during a canary or a blue green cutover the timestamps will not save you.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: the release id arrives as config, set by the release stage
   - Line 8: every log line carries it, so a line identifies its release

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
