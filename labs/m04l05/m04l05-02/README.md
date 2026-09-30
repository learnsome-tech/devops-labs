# m04l05-02 · A deterministic percentage rollout

**Lesson:** [Decoupling Release From Deployment: Feature Flags](https://learnsome.tech/learn/devops-course/m04l05) (lesson 4.5, module 4: Continuous Delivery and Deployment) · Pro  
**Check:** Graded

## Goal

You can use a feature flag for a measured rollout and explain the operational duties that come with flag driven release.

In the lesson: The fixture hashes a user and a flag name into a stable bucket, so a user sees the same decision on every request and every server. Zero percent enables nobody, twenty five percent enables five of twenty users, and one hundred percent enables everyone. The kill switch then disables all twenty without changing the deployed code. Determinism makes the rollout measurable. The team still needs privacy rules, an owner, an expiry date and a plan to delete the flag after the release is complete.

## Files

- [`starter/shell-a-deterministic-percentage-rollout.sh`](starter/shell-a-deterministic-percentage-rollout.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `shell-a-deterministic-percentage-rollout.sh`.
3. The session types these commands, in order:

   ```sh
   python3 release/feature_flag.py
   ```
4. Run it: `bash shell-a-deterministic-percentage-rollout.sh`.
5. Check it from the repository root: `./check m04l05-02`.

## Expected output

```text
rollout   0 percent    0 of 20 users   []
rollout  25 percent    5 of 20 users   ['user-1', 'user-4', 'user-11']
rollout 100 percent   20 of 20 users   ['user-1', 'user-2', 'user-3']

kill switch on    0 of 20 users
the code shipped hours ago; only the flag value changed
```

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `bash shell-a-deterministic-percentage-rollout.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
