# m02l05-04 · Factor ten: three gaps to close

**Lesson:** [Disposability, Dev Prod Parity And Logs](https://learnsome.tech/learn/devops-course/m02l05) (lesson 2.5, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can make a process safe to kill at any moment, close the three gaps between development and production, and treat logs as an unbuffered event stream the platform routes.

In the lesson: Factor ten: keep development, staging and production as similar as possible. The manifesto frames it as three gaps. The time gap is how long a change waits between being written and being run, which should be hours. The personnel gap is the distance between the people who wrote it and the people who run it, which should be zero. The tools gap is the difference in backing services, and this is the one engineers create themselves, with a lightweight database locally and a real one in production. The manifesto is direct: the twelve-factor developer resists that urge.

## Files

- [`starter/factor-ten-three-gaps-to-close.txt`](starter/factor-ten-three-gaps-to-close.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/factor-ten-three-gaps-to-close.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
