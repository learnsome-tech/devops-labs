# m02l05-07 · Two ways to say the same thing happened

**Lesson:** [Disposability, Dev Prod Parity And Logs](https://learnsome.tech/learn/devops-course/m02l05) (lesson 2.5, module 2: The Twelve-Factor App) · Pro  
**Check:** Graded

## Goal

You can make a process safe to kill at any moment, close the three gaps between development and production, and treat logs as an unbuffered event stream the platform routes.

In the lesson: Handle one request in each variant and watch where the evidence goes. The bad variant prints nothing at all and writes a file, which it must now rotate, ship and eventually lose. The good variant prints one structured line on standard output, carrying the event, the path, the counter and the release. That line can be collected by the platform, parsed without a regular expression, and searched by field. Structured output is not required by the manifesto, but it is the obvious thing to do once you accept that a machine, not a person, reads these first.

## Files

- [`starter/shell-two-ways-to-say-the-same-thing-happened.sh`](starter/shell-two-ways-to-say-the-same-thing-happened.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-07/starter`
2. Read `shell-two-ways-to-say-the-same-thing-happened.sh`.
3. The session types these commands, in order:

   ```sh
   cd twelve-factor
   python3 demos.py logs
   ```
4. Run it: `bash shell-two-ways-to-say-the-same-thing-happened.sh`.
5. Check it from the repository root: `./check m02l05-07`.

## Expected output

```text
bad on stdout    ''
bad wrote        quotes.log, which it now has to rotate
good on stdout   {"event": "request", "hits": 1, "path": "/quotes/1", "release": "2026.09.11-a1b2c3"}
good wrote       nothing: routing is the platform's problem
```

## How to check

`./check m02l05-07` copies `starter/` into a scratch directory and runs `bash shell-two-ways-to-say-the-same-thing-happened.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
