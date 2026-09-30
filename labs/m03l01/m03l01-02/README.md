# m03l01-02 · Little's law and unfinished work

**Lesson:** [SDLC: From Request To Running Software](https://learnsome.tech/learn/devops-course/m03l01) (lesson 3.1, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can map a software request through delivery and find the queues that make its lead time long.

In the lesson: Little's law gives a useful warning for the life cycle. Lead time is work in progress divided by throughput. The first row has eighteen items moving at six per week, so the lead time is three weeks. Adding people raises both work in progress and throughput, and the lead time stays three weeks. Halving unfinished work cuts it to one and a half weeks. Increasing deployment while keeping work in progress low cuts it again. The lesson is a management choice: finish work before starting more, because queues are part of the product experience.

## Files

- [`starter/shell-little-s-law-and-unfinished-work.sh`](starter/shell-little-s-law-and-unfinished-work.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `shell-little-s-law-and-unfinished-work.sh`.
3. The session types these commands, in order:

   ```sh
   python3 sdlc/littles_law.py
   ```
4. Run it: `bash shell-little-s-law-and-unfinished-work.sh`.
5. Check it from the repository root: `./check m03l01-02`.

## Expected output

```text
scenario                             wip  per week  lead time
today                                18   6         3.0 weeks
hire two people, same habits         24   8         3.0 weeks
halve the work in progress           9    6         1.5 weeks
halve it and deploy twice as often   9    12        0.8 weeks

more people changed nothing: work in progress grew with the team
the lever is finishing, not starting
```

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `bash shell-little-s-law-and-unfinished-work.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
