# m01l02-06 · Checking the measurement against the repository

**Lesson:** [Throughput: Change Lead Time And Deployment Frequency](https://learnsome.tech/learn/devops-course/m01l02) (lesson 1.2, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Graded

## Goal

You can define change lead time and deployment frequency in DORA's own words, say what each one excludes, and compute both from a real git history rather than from a survey answer.

In the lesson: Never trust a metric you cannot take apart. Count the tags yourself and you get ten, which is the deployment count the script printed. Look at the last three commits and you see plain subjects with plain dates. This matters more than it sounds. A delivery metric that arrives from a dashboard, with no way to trace it back to the events that produced it, is an opinion with a decimal point. If your team adopts these measurements, make sure that anybody can run the query themselves and land on the same answer.

## Files

- [`starter/shell-checking-the-measurement-against-the-reposit.sh`](starter/shell-checking-the-measurement-against-the-reposit.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `shell-checking-the-measurement-against-the-reposit.sh`.
3. The session types these commands, in order:

   ```sh
   cd dora
   bash make-fixture-repo.sh fixture
   git -C fixture tag -l 'deploy-*' | wc -l
   git -C fixture log --format='%ad %s' --date=short -3
   ```
4. Run it: `bash shell-checking-the-measurement-against-the-reposit.sh`.
5. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
fixture repository ready at fixture
10
2026-02-13 document the runbook
2026-02-13 drop the unused column
2026-02-12 log the release identifier
```

## How to check

`./check m01l02-06` copies `starter/` into a scratch directory and runs `bash shell-checking-the-measurement-against-the-reposit.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
