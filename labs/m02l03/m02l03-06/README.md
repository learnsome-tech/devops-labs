# m02l03-06 · The same handler, with the state outside

**Lesson:** [Build, Release, Run And Processes](https://learnsome.tech/learn/devops-course/m02l03) (lesson 2.3, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can separate build, release and run as three distinct stages with an append-only release ledger, and explain why a stateless, share-nothing process is a deployment requirement rather than a style preference.

In the lesson: And the good variant's handler. The store is handed in rather than reached for, which is factor four wearing different clothes: it is an attached resource, and in production it is a database rather than a dictionary. Nothing survives in this process between requests. That makes the process disposable, which is factor nine, and horizontally scalable, which is factor eight, and it is why these factors are best learned as a group. The stateless process is the hinge that the rest of the deployment story turns on.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: the store is handed in: it is an attached resource
   - Line 3: nothing survives in this process between requests

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
