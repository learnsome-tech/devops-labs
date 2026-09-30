# m02l05-03 · What happens when the platform stops you

**Lesson:** [Disposability, Dev Prod Parity And Logs](https://learnsome.tech/learn/devops-course/m02l05) (lesson 2.5, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can make a process safe to kill at any moment, close the three gaps between development and production, and treat logs as an unbuffered event stream the platform routes.

In the lesson: Let us send each variant the signal a platform actually sends when it wants a process to stop. Look at the exit codes. The bad variant is killed by the signal: it had no handler, so the default behaviour ended it wherever it happened to be, with any request in flight lost. The good variant handled the signal, logged its shutdown with the release identifier, and exited with a status of zero. In an orchestrator this is the difference between a deployment nobody notices and a deployment that shows up as a spike of failed requests every single time.

## Files

- [`starter/shell-what-happens-when-the-platform-stops-you.sh`](starter/shell-what-happens-when-the-platform-stops-you.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `shell-what-happens-when-the-platform-stops-you.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 demos.py signal
   ```
4. Run it: `bash shell-what-happens-when-the-platform-stops-you.sh`.
5. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
bad   exit -15  was killed by the signal
good  exit 0    handled the signal
      logged {"event": "shutdown", "release": "2026.09.11-a1b2c3", "signal": 15}
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `bash shell-what-happens-when-the-platform-stops-you.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
