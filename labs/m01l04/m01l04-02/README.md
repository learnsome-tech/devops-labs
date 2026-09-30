# m01l04-02 · The incident, as the repository saw it

**Lesson:** [Restoration: Failed Deployment Recovery Time](https://learnsome.tech/learn/devops-course/m01l04) (lesson 1.4, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can define failed deployment recovery time exactly, say which failures it covers and which it does not, and compute it from the deployment record.

In the lesson: Here is the incident this lesson measures, as four lines of history. A change rotated a database credential and revoked a credential the replicas still used. It went out as deployment seven, which is the one that failed. Overnight, somebody put the old credential back, with a trailer naming what it remediates. That fix went out the next morning as deployment eight, which is the deployment that restored service. Nothing in these lines is a metric. They are the ordinary records of an ordinary bad evening, and the measurement is only arithmetic laid over them afterwards.

## Files

- [`starter/make-fixture-repo.sh`](starter/make-fixture-repo.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/make-fixture-repo.sh` alongside the lesson.
2. Notes from the lesson:
   - Line 1: the change that revoked a credential the replicas still used
   - Line 3: deployment seven: the one that failed
   - Line 6: deployment eight: the one that restored service

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
