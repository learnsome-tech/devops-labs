# m02l01-05 · What breaking factor one looks like

**Lesson:** [Codebase And Dependencies](https://learnsome.tech/learn/devops-course/m02l01) (lesson 2.1, module 2: The Twelve-Factor App) · Pro  
**Check:** Read along

## Goal

You can state the first two factors in the manifesto's own words, tell a codebase from a deploy, and explain why declaration without isolation is not enough.

In the lesson: The audit's check for the first factor is deliberately blunt: it looks for files named after environments. A file per environment is the usual first symptom of a codebase that has started to fork by deploy, because the moment a repository holds one settings file for development and another for production, the two deploys have stopped being the same application with different config and started being two applications. The bad variant has exactly that pair of files, and the good variant has neither. The second line of that same check is factor two, which is the next thing we look at.

## Files

- [`starter/audit.py`](starter/audit.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/audit.py` alongside the lesson.
2. Notes from the lesson:
   - Line 7: a file per environment is the usual first symptom

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
