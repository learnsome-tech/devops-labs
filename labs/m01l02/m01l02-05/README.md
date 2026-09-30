# m01l02-05 · Measuring a real history

**Lesson:** [Throughput: Change Lead Time And Deployment Frequency](https://learnsome.tech/learn/devops-course/m01l02) (lesson 1.2, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Graded

## Goal

You can define change lead time and deployment frequency in DORA's own words, say what each one excludes, and compute both from a real git history rather than from a survey answer.

In the lesson: Let us build the fixture repository, which has a pinned history so the numbers are the same for you as for me, and then run the measurement. Ten deployments over eleven days. A median change lead time of four hours. A deployment frequency of about six per week. Those two numbers are the ones a team can actually act on: four hours means a change written in the morning is usually live in the afternoon, and six per week means roughly one working day between deployments. Notice that nothing here asked anybody's opinion. It read tags and commit dates.

## Files

- [`starter/shell-measuring-a-real-history.sh`](starter/shell-measuring-a-real-history.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-05/starter`
2. Read `shell-measuring-a-real-history.sh`.
3. The session types these commands, in order:

   ```sh
   cd dora
   bash make-fixture-repo.sh fixture
   python3 dora_metrics.py fixture
   ```
4. Run it: `bash shell-measuring-a-real-history.sh`.
5. Check it from the repository root: `./check m01l02-05`.

## Expected output

```text
fixture repository ready at fixture
deployments                     10 over 11.2 days
change lead time                4.0 hours (median)
deployment frequency            6.2 per week
failed deployment recovery time 556 minutes (median)
change fail rate                20 percent
deployment rework rate          20 percent
```

## How to check

`./check m01l02-05` copies `starter/` into a scratch directory and runs `bash shell-measuring-a-real-history.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
