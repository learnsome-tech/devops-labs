# m06l04-02 · Lint the example postmortem

**Lesson:** [Writing A Postmortem: The SRE Appendix](https://learnsome.tech/learn/devops-course/m06l04) (lesson 6.4, module 6: Incident Response and Postmortems) · Pro  
**Check:** Graded

## Goal

You can check a postmortem against the SRE appendix structure and identify missing or blaming language before review.

In the lesson: The local linter checks the example against sixteen required sections, counts four action items and confirms that all four have a recognised classification. It also searches for blaming language and returns none found, so the document is ready for review. A linter cannot decide whether the impact estimate is true or whether an action will reduce risk. It can make omissions and cultural regressions visible before humans spend time reviewing the analysis.

## Files

- [`starter/shell-lint-the-example-postmortem.sh`](starter/shell-lint-the-example-postmortem.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `shell-lint-the-example-postmortem.sh`.
3. The session types these commands, in order:

   ```sh
   python3 incident/lint_postmortem.py incident/postmortem.md
   ```
4. Run it: `bash shell-lint-the-example-postmortem.sh`.
5. Check it from the repository root: `./check m06l04-02`.

## Expected output

```text
sections required   16
sections missing    none
action items        4
classified items    4
blaming language    none found
verdict             ready for review
```

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `bash shell-lint-the-example-postmortem.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
