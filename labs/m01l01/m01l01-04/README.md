# m01l01-04 · Where the week actually goes

**Lesson:** [What DevOps Actually Is](https://learnsome.tech/learn/devops-course/m01l01) (lesson 1.1, module 1: Measurement And Outcomes: DORA) · Free  
**Check:** Graded

## Goal

You can explain DevOps as a set of measurable capabilities rather than a team or a tool, name DORA's two outcome factors, and read a value stream map to find where delivery time is really spent.

In the lesson: Now run the same numbers. This prints the table, and then it adds them up. Thirteen hours of work. One hundred and eighty eight hours of elapsed time. Divide one by the other and you get flow efficiency, which here is under seven percent. That number is the whole argument of this course in one line. If you tried to make delivery faster by asking people to type faster, you would be optimising thirteen hours and ignoring the other hundred and seventy five. The delay is not in the work. The delay is in the queues between the work, and queues are made of process, not of effort.

## Files

- [`starter/shell-where-the-week-actually-goes.sh`](starter/shell-where-the-week-actually-goes.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-04/starter`
2. Read `shell-where-the-week-actually-goes.sh`.
3. The session types these commands, in order:

   ```sh
   cd sdlc
   python3 value_stream.py
   ```
4. Run it: `bash shell-where-the-week-actually-goes.sh`.
5. Check it from the repository root: `./check m01l01-04`.

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

`./check m01l01-04` copies `starter/` into a scratch directory and runs `bash shell-where-the-week-actually-goes.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
