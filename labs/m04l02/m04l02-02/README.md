# m04l02-02 · Five rolling waves

**Lesson:** [Deployment Strategies: Rolling Updates](https://learnsome.tech/learn/devops-course/m04l02) (lesson 4.2, module 4: Continuous Delivery and Deployment) · Pro  
**Check:** Graded

## Goal

You can explain a rolling update and identify the compatibility constraint created when two versions serve traffic together.

In the lesson: The fixture has ten replicas, one extra slot and one allowed unavailable replica. Each wave replaces two old instances, while ten serving instances remain available. The last line states the operational cost: both versions serve traffic at once, so the schema must accept both. This is why a destructive database change should be split into compatible steps. Add a field, deploy code that can use either shape, migrate data, and remove the old shape only after the old version has gone.

## Files

- [`starter/shell-five-rolling-waves.sh`](starter/shell-five-rolling-waves.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `shell-five-rolling-waves.sh`.
3. The session types these commands, in order:

   ```sh
   python3 release/rolling.py
   ```
4. Run it: `bash shell-five-rolling-waves.sh`.
5. Check it from the repository root: `./check m04l02-02`.

## Expected output

```text
step  old  new  serving  capacity
1     8    2    10       100 percent
2     6    4    10       100 percent
3     4    6    10       100 percent
4     2    8    10       100 percent
5     0    10   10       100 percent

both versions serve traffic at once, so the schema must accept both
```

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `bash shell-five-rolling-waves.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
