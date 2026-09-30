# m02l02-04 · The same values, taken from the environment

**Lesson:** [Config And Backing Services](https://learnsome.tech/learn/devops-course/m02l02) (lesson 2.2, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can apply the manifesto's open source test to any repository, move configuration into the environment, and treat a database or queue as an attached resource that can be swapped without a code change.

In the lesson: And here is the good variant. Three values, all read from the environment at start up. Notice the difference between the first and the other two. A default is fine for the release identifier, because an unknown release is a reporting problem rather than a security one. There is no default for the database address or the application key, which means missing config stops the process immediately and loudly at start up, rather than at three in the morning when the first request arrives and something falls back to a development database that happens to still exist.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 7: a default is fine for a release tag, never for a secret
   - Line 8: no default: missing config should stop the process now

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
