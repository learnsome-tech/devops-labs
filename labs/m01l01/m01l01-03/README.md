# m01l01-03 · One change, timed end to end

**Lesson:** [What DevOps Actually Is](https://learnsome.tech/learn/devops-course/m01l01) (lesson 1.1, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Read along

## Goal

You can explain DevOps as a set of measurable capabilities rather than a team or a tool, name DORA's two outcome factors, and read a value stream map to find where delivery time is really spent.

In the lesson: Before any tool, measure one change. Here is a list of steps that one small change went through last month, and each step carries two numbers. The first is process time: how long somebody had their hands on the work. The second is lead time: how long the clock on the wall ran, including every minute the change spent sitting in a queue. Look at the difference. Writing the change took four hours of work and four hours of clock. Waiting for a review took half an hour of work and more than a day of clock. Then the release train, the manual regression pass, the advisory board, and at the very end, the deployment itself.

## Files

- [`starter/value_stream.py`](starter/value_stream.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/value_stream.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: a list of steps
   - Lines 2–5: waiting for a review
   - Lines 6–9: the deployment itself
3. Notes from the lesson:
   - Line 2: process time first: hands actually on the work
   - Line 5: lead time second: the clock on the wall, queue included

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
