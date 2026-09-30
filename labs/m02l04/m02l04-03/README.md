# m02l04-03 · Binding the port you were given

**Lesson:** [Port Binding And Concurrency](https://learnsome.tech/learn/devops-course/m02l04) (lesson 2.4, module 2: The Twelve-Factor App) · Pro  
**Check:** Runs, not graded

## Goal

You can explain why a twelve-factor app binds a port the platform chooses, describe the process formation model of scaling, and say why processes must never daemonize or write PID files.

In the lesson: Let us ask each variant which port it would bind. The bad one says eight thousand and eighty, whatever the environment asked for, because that number is a constant in its source. The good one reads the port it was given and serves a request on that port for real. The demo starts the server and makes one request over the loopback interface. The two lines show factor seven in action, while the surrounding application still follows the other factors it has been taught.

## Files

- [`starter/shell-binding-the-port-you-were-given.sh`](starter/shell-binding-the-port-you-were-given.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `shell-binding-the-port-you-were-given.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 demos.py port
   ```
4. Run it: `bash shell-binding-the-port-you-were-given.sh`.
5. Check it from the repository root: `./check m02l04-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
bad chooses    8080 whatever was asked for
good chooses   7654 which is what PORT asked for
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `bash shell-binding-the-port-you-were-given.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
