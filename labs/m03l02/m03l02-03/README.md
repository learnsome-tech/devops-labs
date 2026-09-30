# m03l02-03 · Semantic conflicts can merge cleanly

**Lesson:** [Trunk-Based Development Versus Git Flow](https://learnsome.tech/learn/devops-course/m03l02) (lesson 3.2, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can choose a branching strategy deliberately and explain the integration cost of long lived branches.

In the lesson: A textual merge is not the same as a valid integration. One branch renames a function while another continues calling the old name. Git reports clean merges because the lines do not overlap. The build then fails because the program's meaning no longer fits together. Continuous integration exists partly to catch this class of semantic conflict. The shorter the branch, the smaller the change set that must be understood at once, but a test suite and a build gate remain necessary even on a trunk based team.

## Files

- [`starter/shell-semantic-conflicts-can-merge-cleanly.sh`](starter/shell-semantic-conflicts-can-merge-cleanly.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `shell-semantic-conflicts-can-merge-cleanly.sh`.
3. The session types these commands, in order:

   ```sh
   bash git/semantic_conflict.sh
   ```
4. Run it: `bash shell-semantic-conflicts-can-merge-cleanly.sh`.
5. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
merge rename   clean, no conflict
merge caller   clean, no conflict
build    red: cannot import apply_discount from app.calc
verdict  git merged the text; only the build noticed the meaning
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `bash shell-semantic-conflicts-can-merge-cleanly.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
