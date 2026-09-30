# m02l03 · Build, Release, Run And Processes

Module 2: The Twelve-Factor App · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/devops-course/m02l03)

**Goal:** You can separate build, release and run as three distinct stages with an append-only release ledger, and explain why a stateless, share-nothing process is a deployment requirement rather than a style preference.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-01](m02l03-01/) | Factor five: three stages, strictly separated | Read along |
| [m02l03-03](m02l03-03/) | The release identifier, in the application | Read along |
| [m02l03-05](m02l03-05/) | State that dies with the process | Read along |
| [m02l03-06](m02l03-06/) | The same handler, with the state outside | Read along |

## Check yourself

- Name the three stages and say exactly what each one produces.
- Why must a release be immutable, and what does that make rollback?
- What does the manifesto say about sticky sessions, and why?
- Where must the hit counter live for two processes to agree?
- Why is compiling assets on first request a factor six violation?

---

[Course README](../../README.md) · [DevOps & Site Reliability Engineering on LearnSome.tech](https://learnsome.tech/courses/devops-course)
