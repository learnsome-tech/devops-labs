# m04l03-02 · Switch the router, keep rollback ready

**Lesson:** [Deployment Strategies: Blue Green](https://learnsome.tech/learn/devops-course/m04l03) (lesson 4.3, module 4: Continuous Delivery and Deployment) · Pro  
**Check:** Graded

## Goal

You can describe blue green deployment and weigh its fast rollback against the cost of a second production sized environment.

In the lesson: The stages show blue serving while green is prepared and smoke tested. The router switch makes green live, and blue stays warm for rollback. The final line names the tradeoff: two production sized environments at once. Blue green is attractive when a clean boundary and fast reversal matter more than infrastructure cost. It is less attractive when the service is expensive to duplicate or when data changes cannot be shared safely between the two environments.

## Files

- [`starter/shell-switch-the-router-keep-rollback-ready.sh`](starter/shell-switch-the-router-keep-rollback-ready.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `shell-switch-the-router-keep-rollback-ready.sh`.
3. The session types these commands, in order:

   ```sh
   python3 release/bluegreen.py
   ```
4. Run it: `bash shell-switch-the-router-keep-rollback-ready.sh`.
5. Check it from the repository root: `./check m04l03-02`.

## Expected output

```text
stage                         blue  green
blue live, green idle         100   0
green built and warmed        100   0
smoke tests against green     100   0
router switched               0     100
blue kept warm for rollback   0     100

rollback is one router change back to blue, not a redeploy
cost of the strategy: two production sized environments at once
```

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `bash shell-switch-the-router-keep-rollback-ready.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
