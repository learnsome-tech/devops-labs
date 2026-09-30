# m02l02-05 · One build, two deploys

**Lesson:** [Config And Backing Services](https://learnsome.tech/learn/devops-course/m02l02) (lesson 2.2, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can apply the manifesto's open source test to any repository, move configuration into the environment, and treat a database or queue as an attached resource that can be swapped without a code change.

In the lesson: Let us run the same code twice. The bad variant reports its database and key from the source file: those values are the build. The good variant reports values that came from the environment it was started in, and then a second deploy of the identical build reports a completely different database and a different release, with no rebuild, no branch, and no edit. That is the whole point of factor three. The artifact stops being environment specific, which is the precondition for promoting one tested artifact from staging to production rather than building twice and hoping.

## Files

- [`starter/shell-one-build-two-deploys.sh`](starter/shell-one-build-two-deploys.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-05/starter`
2. Read `shell-one-build-two-deploys.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 demos.py config
   ```
4. Run it: `bash shell-one-build-two-deploys.sh`.
5. Check it from the repository root: `./check m02l02-05`.

## Expected output

```text
bad, from the source file    quotes.db shhh-do-not-tell
good, from the environment   sqlite:///quotes from-the-environment
good, second deploy          postgres://quotes/prod 2026.09.12-ff0011
same build, different config, and no credential in the repository
```

## How to check

`./check m02l02-05` copies `starter/` into a scratch directory and runs `bash shell-one-build-two-deploys.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
