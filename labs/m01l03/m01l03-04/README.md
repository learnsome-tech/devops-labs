# m01l03-04 · The remediations are searchable

**Lesson:** [Instability: Change Fail Rate And Deployment Rework Rate](https://learnsome.tech/learn/devops-course/m01l03) (lesson 1.3, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Graded

## Goal

You can state DORA's definitions of change fail rate and deployment rework rate, explain how they differ, and derive both from the record a repository already keeps.

In the lesson: Because the fact lives in a commit message, you can ask the repository directly. Two remediations in this history: one that restored a search index, one that put a credential back. Now look at the three instability lines the script prints. Recovery time, change fail rate of twenty percent, rework rate of twenty percent. Ten deployments, two of which failed, and two of which existed only to clean up. In this history those are the same pair of incidents seen from opposite ends, which is the normal case, and is why the two numbers so often move together.

## Files

- [`starter/shell-the-remediations-are-searchable.sh`](starter/shell-the-remediations-are-searchable.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `shell-the-remediations-are-searchable.sh`.
3. The session types these commands, in order:

   ```sh
   cd dora
   bash make-fixture-repo.sh fixture
   git -C fixture log --grep=Remediates --format='%s'
   python3 dora_metrics.py fixture | tail -3
   ```
4. Run it: `bash shell-the-remediations-are-searchable.sh`.
5. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
fixture repository ready at fixture
put the old credential back
restore the old search index
failed deployment recovery time 556 minutes (median)
change fail rate                20 percent
deployment rework rate          20 percent
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `bash shell-the-remediations-are-searchable.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
