# m03l04-02 · Run the three layers

**Lesson:** [Testing Strategies And The Test Pyramid](https://learnsome.tech/learn/devops-course/m03l04) (lesson 3.4, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can distinguish test layers and choose a balanced suite that gives fast feedback without abandoning realistic checks.

In the lesson: The sample runner reports its layers separately. Four unit tests, one integration test and one end to end test all pass, giving six tests in total. The summary is useful because a failing layer points to a different investigation. A unit failure may be local logic. An integration failure may be a contract or environment problem. An end to end failure may be a broken route or a missing dependency. The counts are not a target to maximise. They are a compact view of where confidence comes from.

## Files

- [`starter/shell-run-the-three-layers.sh`](starter/shell-run-the-three-layers.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `shell-run-the-three-layers.sh`.
3. The session types these commands, in order:

   ```sh
   cd ci && python3 run_tests.py
   ```
4. Run it: `bash shell-run-the-three-layers.sh`.
5. Check it from the repository root: `./check m03l04-02`.

## Expected output

```text
unit            4 tests   passed
integration     1 tests   passed
e2e             1 tests   passed
total           6 tests   green
```

## How to check

`./check m03l04-02` copies `starter/` into a scratch directory and runs `bash shell-run-the-three-layers.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
