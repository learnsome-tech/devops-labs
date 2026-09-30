# m02l06-05 · The whole audit, one row per factor

**Lesson:** [Admin Processes And The Open Source Update](https://learnsome.tech/learn/devops-course/m02l06) (lesson 2.6, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can run administrative tasks as one-off processes against the same release, and you can describe accurately what changed when the manifesto was open sourced in 2024, including the proposals in flight.

In the lesson: Run the audit once more, now that you know what every row means. Twelve rows, two variants, and the checks behind them are ordinary: some read the source for a pattern, some run the code and look at what it did. The point of the table is not the score. It is that every one of these rules can be checked mechanically, which means they can be part of a pipeline rather than a code review opinion. When we build a pipeline in a later module, this is the sort of check that belongs in it.

## Files

- [`starter/shell-the-whole-audit-one-row-per-factor.sh`](starter/shell-the-whole-audit-one-row-per-factor.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l06/m02l06-05/starter`
2. Read `shell-the-whole-audit-one-row-per-factor.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 audit.py
   ```
4. Run it: `bash shell-the-whole-audit-one-row-per-factor.sh`.
5. Check it from the repository root: `./check m02l06-05`.

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

`./check m02l06-05` copies `starter/` into a scratch directory and runs `bash shell-the-whole-audit-one-row-per-factor.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
