# m01l04-05 · One recovery, from end to end

**Lesson:** [Restoration: Failed Deployment Recovery Time](https://learnsome.tech/learn/devops-course/m01l04) (lesson 1.4, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Graded

## Goal

You can define failed deployment recovery time exactly, say which failures it covers and which it does not, and compute it from the deployment record.

In the lesson: Here are the two deployments from the credential incident. The failing one landed at four in the afternoon. The one that restored service landed at twenty past nine the next morning, which is seventeen hours and twenty minutes later. The other failed deployment in this history recovered in seventy two minutes, because the fix was a rollback rather than a rebuild. Take the median of the two and you get the number on screen: five hundred and fifty six minutes. One overnight recovery is doing all the damage here, which is exactly the kind of thing a median of two hides and a worst case shows.

## Files

- [`starter/shell-one-recovery-from-end-to-end.sh`](starter/shell-one-recovery-from-end-to-end.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-05/starter`
2. Read `shell-one-recovery-from-end-to-end.sh`.
3. The session types these commands, in order:

   ```sh
   cd dora
   bash make-fixture-repo.sh fixture
   bash deploy_times.sh fixture deploy-0007 deploy-0008
   python3 dora_metrics.py fixture | sed -n '4p'
   ```
4. Run it: `bash shell-one-recovery-from-end-to-end.sh`.
5. Check it from the repository root: `./check m01l04-05`.

## Expected output

```text
fixture repository ready at fixture
deploy-0007  2026-02-10 16:00:00 +0000
deploy-0008  2026-02-11 09:20:00 +0000
failed deployment recovery time 556 minutes (median)
```

## How to check

`./check m01l04-05` copies `starter/` into a scratch directory and runs `bash shell-one-recovery-from-end-to-end.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
