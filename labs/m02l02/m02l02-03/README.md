# m02l02-03 · Config baked into the source

**Lesson:** [Config And Backing Services](https://learnsome.tech/learn/devops-course/m02l02) (lesson 2.2, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can apply the manifesto's open source test to any repository, move configuration into the environment, and treat a database or queue as an attached resource that can be swapped without a code change.

In the lesson: Here is the bad variant's head. Five constants that should not be there. The database path is decided at edit time, not deploy time, so the only way to point this app at a different database is to edit it and build again. The interesting one is the second: an application key, sitting in version control, which fails the open source test on its own. There is also state in the process, which belongs to factor six later. Everything here was normal practice for years, and every line of it makes the app harder to deploy twice.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: five constants
   - Lines 6–11: state in the process
3. Notes from the lesson:
   - Line 3: a credential in version control fails the open source test
   - Line 2: the database path is decided at edit time, not deploy time

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
