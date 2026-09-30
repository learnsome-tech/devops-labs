# m03l03-02 · Validate a workflow without GitHub

**Lesson:** [Continuous Integration](https://learnsome.tech/learn/devops-course/m03l03) (lesson 3.3, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Read along

## Goal

You can describe continuous integration and inspect a pipeline that tests every change before it can build and deploy.

In the lesson: The workflow validator can inspect the file without contacting GitHub. It finds three jobs and seven steps, and it accepts the trigger, runners, dependencies and versioned actions. This is a useful local gate because syntax and structure errors can be caught before a push. It cannot prove that a hosted runner has the required credentials, that a third party action will behave correctly, or that a production deployment is safe. Those limits belong in the report next to the local evidence.

## Files

- [`starter/shell-validate-a-workflow-without-github.sh`](starter/shell-validate-a-workflow-without-github.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-validate-a-workflow-without-github.sh` alongside the lesson.

## How to check

**Read along.** It calls `bun`, which the lab sandbox does not have. Run it where `bun` is installed.

There is nothing to check: `./check m03l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
