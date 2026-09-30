# m02l05-02 · Handling the signal the platform actually sends

**Lesson:** [Disposability, Dev Prod Parity And Logs](https://learnsome.tech/learn/devops-course/m02l05) (lesson 2.5, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can make a process safe to kill at any moment, close the three gaps between development and production, and treat logs as an unbuffered event stream the platform routes.

In the lesson: In the good variant this is six lines. A handler that logs the shutdown and exits cleanly, and one call registering the handler for the termination signal. Registering the handler is the entire difference between a graceful stop and a kill. Logging it matters too: that line is how you prove it was graceful when somebody asks why requests failed during a deployment. Real services do more inside that handler, draining connections and finishing in flight work, but the shape does not change, and the deadline is short because the platform will escalate to an unblockable kill.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Notes from the lesson:
   - Line 2: log the shutdown: this is how you prove it was graceful
   - Line 6: registering the handler is the entire difference

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
