# m02l04-05 · The process formation, declared

**Lesson:** [Port Binding And Concurrency](https://learnsome.tech/learn/devops-course/m02l04) (lesson 2.4, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can explain why a twelve-factor app binds a port the platform chooses, describe the process formation model of scaling, and say why processes must never daemonize or write PID files.

In the lesson: Here is the formation in the good variant, in the file format the manifesto's own platform used. One line per process type, and each line is a command that runs in the foreground and stays there. That last part is what makes it operable. A process that stays in the foreground can be supervised, restarted, counted, stopped and logged by whatever is running it. A process that forks into the background and writes its own identifier into a file has taken over a job that the platform does better, and it has made itself invisible to the thing that is meant to keep it alive.

## Files

- [`starter/Procfile`](starter/Procfile): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/Procfile` alongside the lesson.
2. Notes from the lesson:
   - Line 1: one line per process type, each a foreground command

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
