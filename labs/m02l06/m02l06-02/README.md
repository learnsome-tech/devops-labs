# m02l06-02 · An admin task, in the codebase

**Lesson:** [Admin Processes And The Open Source Update](https://learnsome.tech/learn/devops-course/m02l06) (lesson 2.6, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can run administrative tasks as one-off processes against the same release, and you can describe accurately what changed when the manifesto was open sourced in 2024, including the proposals in flight.

In the lesson: Here is the good variant's admin entry point. It imports the application, which means it inherits the same code and config as the web process by construction, and it uses the same logging, so the task is visible afterwards in exactly the same stream as everything else. Underneath is a table of named tasks. This is deliberately boring. The value is not in the design; it is in the fact that this file lives beside the application, is built into the same artifact, and is released at the same moment as the code whose data it modifies.

## Files

- [`starter/manage.py`](starter/manage.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/manage.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: imports the application
   - Lines 6–18: a table of named tasks
3. Notes from the lesson:
   - Line 5: same code and config as the web process, by construction
   - Line 9: and the same logging, so the task is visible afterwards

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
