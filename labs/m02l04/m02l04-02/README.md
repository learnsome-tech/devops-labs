# m02l04-02 · Who decides the port

**Lesson:** [Port Binding And Concurrency](https://learnsome.tech/learn/devops-course/m02l04) (lesson 2.4, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can explain why a twelve-factor app binds a port the platform chooses, describe the process formation model of scaling, and say why processes must never daemonize or write PID files.

In the lesson: The good variant's answer is three lines, and the important detail is what is missing: there is no default. The platform must say which port to use, and every platform that runs this kind of application does say, because it is allocating that port to you. A hard coded default looks friendly and causes a specific, tedious failure: two copies of the service on one host, the second one refusing to start, at the exact moment you were trying to scale out. The bad variant has that hard coded constant, which is why the audit fails it on this row.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: no default: the platform must say, and it always does

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
