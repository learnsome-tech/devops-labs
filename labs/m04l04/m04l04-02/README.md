# m04l04-02 · The gate aborts at twenty five percent

**Lesson:** [Deployment Strategies: Canary Releases](https://learnsome.tech/learn/devops-course/m04l04) (lesson 4.4, module 4: Continuous Delivery and Deployment) · Pro  
**Check:** Graded

## Goal

You can use a canary gate to limit blast radius and decide whether to promote or roll back from observed evidence.

In the lesson: The canary begins with one percent and then five percent of traffic. Its error ratio remains below the threshold, so the gate promotes both waves. At twenty five percent the observed rate is four point four five times the baseline, above the allowed three times, and the gate aborts and rolls back. The blast radius is one wave of twenty five percent for the measured interval. The important behaviour is automatic and predeclared: a person does not negotiate with a failing signal while users are exposed.

## Files

- [`starter/shell-the-gate-aborts-at-twenty-five-percent.sh`](starter/shell-the-gate-aborts-at-twenty-five-percent.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `shell-the-gate-aborts-at-twenty-five-percent.sh`.
3. The session types these commands, in order:

   ```sh
   python3 release/canary.py
   ```
4. Run it: `bash shell-the-gate-aborts-at-twenty-five-percent.sh`.
5. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
wave  traffic  canary errors  ratio  decision
1     1 percent0.0021         1.05   promote
5     5 percent0.0024         1.20   promote
25    25 percent0.0089         4.45   abort and roll back

blast radius: 25 percent of users, for one wave
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `bash shell-the-gate-aborts-at-twenty-five-percent.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
