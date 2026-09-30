# m05l05-02 · Calculate remaining budget and burn

**Lesson:** [Error Budgets](https://learnsome.tech/learn/devops-course/m05l05) (lesson 5.5, module 5: Service Level Objectives (SRE)) · Pro  
**Check:** Graded

## Goal

You can calculate an error budget and use burn rate to decide whether to keep shipping or pause and fix.

In the lesson: The example has spent one thousand four hundred thirty of its two thousand allowed failures after only one third of the window. That is seventy one point five percent of the budget in thirty three point three percent of the time, a burn rate of two point one four times sustainable. At the current pace the budget ends in four days, so the worked policy says freeze and fix. The policy is a team decision: stop risky releases, restore the service and learn before spending the remaining margin.

## Files

- [`starter/shell-calculate-remaining-budget-and-burn.sh`](starter/shell-calculate-remaining-budget-and-burn.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-02/starter`
2. Read `shell-calculate-remaining-budget-and-burn.sh`.
3. The session types these commands, in order:

   ```sh
   python3 slo/error_budget.py
   ```
4. Run it: `bash shell-calculate-remaining-budget-and-burn.sh`.
5. Check it from the repository root: `./check m05l05-02`.

## Expected output

```text
objective                 99.9 percent over 30 days
error budget              2,000 failed requests
budget spent              1,430 requests, 71.5 percent
window elapsed            33.3 percent
burn rate                 2.14 times the sustainable rate
budget exhausted in       4.0 days
verdict                   freeze and fix
```

## How to check

`./check m05l05-02` copies `starter/` into a scratch directory and runs `bash shell-calculate-remaining-budget-and-burn.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
