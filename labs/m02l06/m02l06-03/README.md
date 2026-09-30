# m02l06-03 · Running a one-off task

**Lesson:** [Admin Processes And The Open Source Update](https://learnsome.tech/learn/devops-course/m02l06) (lesson 2.6, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can run administrative tasks as one-off processes against the same release, and you can describe accurately what changed when the manifesto was open sourced in 2024, including the proposals in flight.

In the lesson: Run the migration as its own process and you get a log line carrying the release and the database it touched, then the result. Now look at the last line, which reports something about the other variant: the bad app runs its migration at import time, inside the web process. That means every process start attempts a schema change, ten processes starting together attempt ten, and a start up is no longer a safe operation. It also means you cannot run the migration without starting a server, and cannot start a server without running the migration.

## Files

- [`starter/shell-running-a-one-off-task.sh`](starter/shell-running-a-one-off-task.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l06/m02l06-03/starter`
2. Read `shell-running-a-one-off-task.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 demos.py admin
   ```
4. Run it: `bash shell-running-a-one-off-task.sh`.
5. Check it from the repository root: `./check m02l06-03`.

## Expected output

```text
one-off process, same code, same config, own life cycle
   {"database": "sqlite:///quotes", "event": "migrate", "release": "2026.09.11-a1b2c3"}
   schema at revision two
bad runs the migration at import time: True
```

## How to check

`./check m02l06-03` copies `starter/` into a scratch directory and runs `bash shell-running-a-one-off-task.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
