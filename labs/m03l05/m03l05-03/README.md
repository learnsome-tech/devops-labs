# m03l05-03 · Environment configuration arrives at deploy time

**Lesson:** [Building And Versioning The Artifact](https://learnsome.tech/learn/devops-course/m03l05) (lesson 3.5, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can build one identifiable artifact and explain how version information follows it through promotion.

In the lesson: The deployment command combines the versioned artifact identity with a staging environment. The output says that configuration comes from the environment, not from the artifact. That separation lets the same tested bytes move forward while a database address, endpoint or secret changes by policy. The command is a local transcript of the deployment contract; it does not contact a cloud provider. A hosted deploy would need credentials, permissions and a target, so those parts must be marked no verify when shown in a lesson.

## Files

- [`starter/shell-environment-configuration-arrives-at-deploy-.sh`](starter/shell-environment-configuration-arrives-at-deploy-.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `shell-environment-configuration-arrives-at-deploy-.sh`.
3. The session types these commands, in order:

   ```sh
   cd ci && ENVIRONMENT=staging bash deploy.sh
   ```
4. Run it: `bash shell-environment-configuration-arrives-at-deploy-.sh`.
5. Check it from the repository root: `./check m03l05-03`.

## Expected output

```text
release  2.4.0-staging
config   from the environment, not from the artifact
deployed staging
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `bash shell-environment-configuration-arrives-at-deploy-.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
