# m02l03-01 · Factor five: three stages, strictly separated

**Lesson:** [Build, Release, Run And Processes](https://learnsome.tech/learn/devops-course/m02l03) (lesson 2.3, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can separate build, release and run as three distinct stages with an append-only release ledger, and explain why a stateless, share-nothing process is a deployment requirement rather than a style preference.

In the lesson: Factor five: strictly separate build and run stages. There are three. Build turns a commit into an executable bundle, once, with dependencies fetched and assets compiled. Release joins that bundle to the config of one particular deploy, producing something ready to execute, and gives it a unique release identifier. Run starts processes against a chosen release, and does nothing else. The manifesto's strongest sentence here is that releases are an append-only ledger and a release cannot be mutated once it is created. If you need to change something, you make a new release, which is also what makes rolling back a selection rather than a rebuild.

## Files

- [`starter/factor-five-three-stages-strictly-separated.txt`](starter/factor-five-three-stages-strictly-separated.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/factor-five-three-stages-strictly-separated.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
