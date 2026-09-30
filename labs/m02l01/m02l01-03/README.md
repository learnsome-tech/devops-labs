# m02l01-03 · A sample app that fails every factor

**Lesson:** [Codebase And Dependencies](https://learnsome.tech/learn/devops-course/m02l01) (lesson 2.1, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can state the first two factors in the manifesto's own words, tell a codebase from a deploy, and explain why declaration without isolation is not enough.

In the lesson: This is the lab for this module: two variants of one small quote service, and a script that audits both. It runs one check per factor, some by reading the source and some by actually running the code, and prints one row per factor. The bad variant fails all twelve. The good variant passes all twelve. Everything in this module is a walk down that table, and at each row you will see the code that fails, the code that passes, and the check that tells them apart. Start at the top with codebase and dependencies.

## Files

- [`starter/shell-a-sample-app-that-fails-every-factor.sh`](starter/shell-a-sample-app-that-fails-every-factor.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `shell-a-sample-app-that-fails-every-factor.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 audit.py
   ```
4. Run it: `bash shell-a-sample-app-that-fails-every-factor.sh`.
5. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
factor                     bad    good
I   Codebase               FAIL   PASS
II  Dependencies           FAIL   PASS
III Config                 FAIL   PASS
IV  Backing services       FAIL   PASS
V   Build, release, run    FAIL   PASS
VI  Processes              FAIL   PASS
VII Port binding           FAIL   PASS
VIIIConcurrency            FAIL   PASS
IX  Disposability          FAIL   PASS
X   Dev prod parity        FAIL   PASS
XI  Logs                   FAIL   PASS
XII Admin processes        FAIL   PASS
totals                     0/12   12/12
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `bash shell-a-sample-app-that-fails-every-factor.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
