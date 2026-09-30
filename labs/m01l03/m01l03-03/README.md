# m01l03-03 · How a repository already records this

**Lesson:** [Instability: Change Fail Rate And Deployment Rework Rate](https://learnsome.tech/learn/devops-course/m01l03) (lesson 1.3, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can state DORA's definitions of change fail rate and deployment rework rate, explain how they differ, and derive both from the record a repository already keeps.

In the lesson: You do not need a new tool to record this. Here is a piece of the fixture history. A change goes out, and that is a deployment that went badly. The next commit puts the old search index back, and it carries a trailer: a line in the commit message naming the deployment it is remediating. Then a second deployment carries that fix to production. Two facts are now permanently in the repository. The deployment named in the trailer failed, and the deployment carrying the fix was unplanned. That is a fail rate numerator and a rework rate numerator, recorded by the people who were there, at the moment they knew.

## Files

- [`starter/make-fixture-repo.sh`](starter/make-fixture-repo.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/make-fixture-repo.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a deployment that went badly
   - Lines 4–6: a second deployment
3. Notes from the lesson:
   - Line 3: a trailer names the deployment this commit remediates

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
