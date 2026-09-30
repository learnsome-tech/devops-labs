# m03l01-03 · A value stream map exposes queues

**Lesson:** [SDLC: From Request To Running Software](https://learnsome.tech/learn/devops-course/m03l01) (lesson 3.1, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can map a software request through delivery and find the queues that make its lead time long.

In the lesson: A value stream map separates process time from lead time. Here the team actively works for thirteen hours, but the clock runs for one hundred eighty eight hours. Review, a release train, testing and an approval board are queues. Flow efficiency is only six point nine percent. That number is not a verdict on the people waiting. It is a prompt to ask which handoff can become a small automated check, which batch can become a continuous flow, and which approval is protecting a real risk.

## Files

- [`starter/shell-a-value-stream-map-exposes-queues.sh`](starter/shell-a-value-stream-map-exposes-queues.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `shell-a-value-stream-map-exposes-queues.sh`.
3. The session types these commands, in order:

   ```sh
   python3 sdlc/value_stream.py
   ```
4. Run it: `bash shell-a-value-stream-map-exposes-queues.sh`.
5. Check it from the repository root: `./check m03l01-03`.

## Expected output

```text
step                        process  lead
write the change            4.0      4.0
wait for review             0.5      26.0
review and rework           1.5      3.0
wait for the release train  0.0      96.0
manual regression test      6.0      18.0
change advisory board       0.5      40.0
deploy                      0.5      1.0

process time  13.0 hours
lead time     188.0 hours
flow efficiency 6.9 percent
the queues, not the work, are the delivery problem
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `bash shell-a-value-stream-map-exposes-queues.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
