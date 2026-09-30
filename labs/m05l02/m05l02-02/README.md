# m05l02-02 · The mean hides the afternoon tail

**Lesson:** [Percentiles Rather Than Averages](https://learnsome.tech/learn/devops-course/m05l02) (lesson 5.2, module 5: Service Level Objectives (SRE)) · Pro  
**Check:** Graded

## Goal

You can read latency percentiles and explain why an average can hide a slow tail.

In the lesson: The two samples have the same mean, fifty point five milliseconds. Their distributions differ sharply. In the afternoon, one request in twenty takes ninety eight milliseconds, while the morning ninety fifth percentile is fifty. The mean says nothing changed, but the tail moved. Percentiles make that change visible and give a release review a better question: which users got slower, and is that degradation inside the service objective?

## Files

- [`starter/shell-the-mean-hides-the-afternoon-tail.sh`](starter/shell-the-mean-hides-the-afternoon-tail.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `shell-the-mean-hides-the-afternoon-tail.sh`.
3. The session types these commands, in order:

   ```sh
   python3 slo/percentiles.py
   ```
4. Run it: `bash shell-the-mean-hides-the-afternoon-tail.sh`.
5. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
hour        mean    p50     p90     p95     p99
morning     50.5    50      50      50      60
afternoon   50.5    48      48      48      98

the mean says nothing changed; one request in twenty got twice as slow
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `bash shell-the-mean-hides-the-afternoon-tail.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
