# m01l06-02 · Gaming a metric, demonstrated

**Lesson:** [The Pitfalls Of Measurement](https://learnsome.tech/learn/devops-course/m01l06) (lesson 1.6, module 1: Measurement And Outcomes: DORA) · Pro  
**Check:** Graded

## Goal

You can name DORA's own stated pitfalls, demonstrate how a delivery metric is gamed, and choose a way of reporting these numbers that resists gaming.

In the lesson: This is not hypothetical, so let us do it. Here is the same repository twice. The first measurement treats a deployment as something that reached production. The second relabels every single commit as a deployment, and changes nothing else at all: same code, same tests, same people, same customers. Measure it twice and watch. Deployment frequency rises. Change lead time falls to zero, because every change is deployed at the instant it is written. Change fail rate collapses to zero, because the remediation trailers now point at deployment names that no longer exist. Better on three metrics, in ten seconds, having improved nothing.

## Files

- [`starter/shell-gaming-a-metric-demonstrated.sh`](starter/shell-gaming-a-metric-demonstrated.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l06/m01l06-02/starter`
2. Read `shell-gaming-a-metric-demonstrated.sh`.
3. The session types these commands, in order:

   ```sh
   cd dora
   bash make-fixture-repo.sh fixture
   bash gaming.sh fixture
   ```
4. Run it: `bash shell-gaming-a-metric-demonstrated.sh`.
5. Check it from the repository root: `./check m01l06-02`.

## Expected output

```text
fixture repository ready at fixture
honest, deployments tagged when they reached production
  deployments                     10 over 11.2 days
  change lead time                4.0 hours (median)
  deployment frequency            6.2 per week
  failed deployment recovery time 556 minutes (median)
  change fail rate                20 percent
  deployment rework rate          20 percent
gamed, every commit relabelled a deployment
  deployments                     14 over 12.2 days
  change lead time                0.0 hours (median)
  deployment frequency            8.0 per week
  failed deployment recovery time no failed deployments in this window
  change fail rate                0 percent
  deployment rework rate          14 percent
```

## How to check

`./check m01l06-02` copies `starter/` into a scratch directory and runs `bash shell-gaming-a-metric-demonstrated.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
