# m03l03-03 · A pipeline stops at its gates

**Lesson:** [Continuous Integration](https://learnsome.tech/learn/devops-course/m03l03) (lesson 3.3, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can describe continuous integration and inspect a pipeline that tests every change before it can build and deploy.

In the lesson: Here the local pipeline runs its lint gate, then the unit, integration and end to end tests, then builds one artifact. The digest gives that artifact an identity, and the final gate states that later environments must promote those same bytes rather than rebuild them. The sequence is intentionally plain. Each stage has one job, a failure stops the next stage, and the output gives a person enough context to find the failed boundary. Continuous integration is a team habit supported by this kind of automation.

## Files

- [`starter/shell-a-pipeline-stops-at-its-gates.sh`](starter/shell-a-pipeline-stops-at-its-gates.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `shell-a-pipeline-stops-at-its-gates.sh`.
3. The session types these commands, in order:

   ```sh
   cd ci && bash pipeline.sh
   ```
4. Run it: `bash shell-a-pipeline-stops-at-its-gates.sh`.
5. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
stage:lint checking formatting and obvious mistakes
stage:test running the test suite
unit            4 tests   passed
integration     1 tests   passed
e2e             1 tests   passed
total           6 tests   green
stage:build producing one immutable artifact
artifact dist/calc-2.4.0.tar
digest   3237998773
stage:gate artifact is built once and promoted, never rebuilt
pipeline passed
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `bash shell-a-pipeline-stops-at-its-gates.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
