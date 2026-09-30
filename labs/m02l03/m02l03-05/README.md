# m02l03-05 · State that dies with the process

**Lesson:** [Build, Release, Run And Processes](https://learnsome.tech/learn/devops-course/m02l03) (lesson 2.3, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can separate build, release and run as three distinct stages with an append-only release ledger, and explain why a stateless, share-nothing process is a deployment requirement rather than a style preference.

In the lesson: Here is the violation in the bad variant. A module global counter, incremented under a lock. It looks harmless and it is correct inside one process. Now run two copies behind a load balancer and ask what a user sees: the number depends on which copy answered, and both numbers are wrong. Restart either copy and the count resets. This is the pattern behind session data in memory, upload directories on local disk, and caches that quietly become the source of truth. The fix is not a bigger lock. The fix is to put the fact somewhere that outlives any single process.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: a module global: this counter exists once, in this process
   - Line 10: so the number a user sees depends on which copy answered

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
