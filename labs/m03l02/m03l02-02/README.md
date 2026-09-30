# m03l02-02 · Distance makes integration harder

**Lesson:** [Trunk-Based Development Versus Git Flow](https://learnsome.tech/learn/devops-course/m03l02) (lesson 3.2, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can choose a branching strategy deliberately and explain the integration cost of long lived branches.

In the lesson: This fixture makes branch distance visible. The short branch comes back immediately and merges cleanly. The long branch waits while trunk moves nine times, then returns with a conflict in the same file. The exact count is not a universal threshold. It is evidence that every day apart gives the surrounding code more chances to change. Trunk based development reduces the distance by integrating small slices. A team using git flow should name the reason for its release branches and measure whether their isolation is buying safety or only postponing the merge.

## Files

- [`starter/shell-distance-makes-integration-harder.sh`](starter/shell-distance-makes-integration-harder.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `shell-distance-makes-integration-harder.sh`.
3. The session types these commands, in order:

   ```sh
   bash git/distance.sh
   ```
4. Run it: `bash shell-distance-makes-integration-harder.sh`.
5. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
short     0 commits behind trunk   merge clean     conflicted files 0
long      9 commits behind trunk   merge conflict  conflicted files 1
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `bash shell-distance-makes-integration-harder.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
