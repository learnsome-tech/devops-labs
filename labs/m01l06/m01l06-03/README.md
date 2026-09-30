# m01l06-03 · What the gaming script actually does

**Lesson:** [The Pitfalls Of Measurement](https://learnsome.tech/learn/devops-course/m01l06) (lesson 1.6, module 1: Measurement And Outcomes: DORA) · Pro  
**Check:** Read along

## Goal

You can name DORA's own stated pitfalls, demonstrate how a delivery metric is gamed, and choose a way of reporting these numbers that resists gaming.

In the lesson: For honesty, here is what that script does, because a demonstration you cannot inspect is a magic trick. It deletes the real tags, then walks the commits oldest first and tags every commit as if it were a deployment, dating each tag to the moment the commit was authored. There is no clever manipulation of the metric code, and the metric code is not aware that anything unusual happened. That is the point. The numbers are perfectly correct arithmetic over a record that somebody redefined, and no amount of care inside the measuring script can defend against a change in what is being counted.

## Files

- [`starter/gaming.sh`](starter/gaming.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/gaming.sh` alongside the lesson.
2. Notes from the lesson:
   - Line 1: delete the honest deployment tags
   - Line 4: then tag every commit as if it were a deployment

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
