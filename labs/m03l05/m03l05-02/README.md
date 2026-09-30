# m03l05-02 · Build an immutable artifact

**Lesson:** [Building And Versioning The Artifact](https://learnsome.tech/learn/devops-course/m03l05) (lesson 3.5, module 3: Collaboration and Continuous Integration) · Pro  
**Check:** Graded

## Goal

You can build one identifiable artifact and explain how version information follows it through promotion.

In the lesson: The build reads the version from the repository, packages the application and prints a digest derived from its contents. The file name carries version two point four point zero, while the digest distinguishes the exact bytes. A later job can store this artifact, record its identity and promote it without compiling again. The example uses a simple archive and checksum. In a larger system the registry may provide content addressed storage and signing, but the discipline is the same: make the unit of promotion explicit.

## Files

- [`starter/shell-build-an-immutable-artifact.sh`](starter/shell-build-an-immutable-artifact.sh): the listing from the lesson
- 47 files of the course's shared working tree (`shared/lab/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `shell-build-an-immutable-artifact.sh`.
3. The session types these commands, in order:

   ```sh
   cd ci && bash build.sh
   ```
4. Run it: `bash shell-build-an-immutable-artifact.sh`.
5. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
artifact dist/calc-2.4.0.tar
digest   3237998773
```

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `bash shell-build-an-immutable-artifact.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/devops-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
