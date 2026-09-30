# m06l02-02 · Read the incident clocks

**Lesson:** [The Incident Lifecycle](https://learnsome.tech/learn/devops-course/m06l02) (lesson 6.2, module 6: Incident Response and Postmortems) · Pro  
**Check:** Graded

## Goal

You can distinguish detection, declaration, mitigation, outage end and incident closure when reviewing an event.

In the lesson: The timeline separates five useful measures. Detection takes one minute, declaration takes seven, mitigation takes forty two, user impact lasts sixty six, and the whole incident lasts eighty nine. The numbers point to different work. Better alerting may shorten detection. A clearer escalation path may shorten declaration. A safer mitigation may shorten user impact. Waiting thirty minutes before closure protects against declaring victory during a second failure. A postmortem should preserve this distinction instead of reporting one impressive average.

## Files

- [`starter/shell-read-the-incident-clocks.sh`](starter/shell-read-the-incident-clocks.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-02/starter`
2. Read `shell-read-the-incident-clocks.sh`.
3. The session types these commands, in order:

   ```sh
   python3 incident/timeline.py
   ```
4. Run it: `bash shell-read-the-incident-clocks.sh`.
5. Check it from the repository root: `./check m06l02-02`.

## Expected output

```text
14:51  new sonnet discovered, traffic starts to climb
14:53  traffic to the search service increases sharply
14:54  OUTAGE BEGINS, servers start returning errors
14:55  monitoring pages the on-call engineer
15:01  INCIDENT BEGINS, incident commander named
15:36  OUTAGE MITIGATED, traffic moved to a sacrificial cluster
16:00  OUTAGE ENDS, all clusters serving
16:30  INCIDENT ENDS, thirty minutes of nominal performance

time to detect      1 minutes
time to declare     7 minutes
time to mitigate   42 minutes
user impact        66 minutes
incident length    89 minutes
```

## How to check

`./check m06l02-02` copies `starter/` into a scratch directory and runs `bash shell-read-the-incident-clocks.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
