# m02l05 · Disposability, Dev Prod Parity And Logs

Module 2: The Twelve-Factor App · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/devops-course/m02l05)

**Goal:** You can make a process safe to kill at any moment, close the three gaps between development and production, and treat logs as an unbuffered event stream the platform routes.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-02](m02l05-02/) | Handling the signal the platform actually sends | Read along |
| [m02l05-03](m02l05-03/) | What happens when the platform stops you | Graded |
| [m02l05-04](m02l05-04/) | Factor ten: three gaps to close | Read along |
| [m02l05-07](m02l05-07/) | Two ways to say the same thing happened | Graded |

## Check yourself

- What should a web process do between receiving a stop signal and exiting?
- Name the three gaps in factor ten and one way to close each.
- Why is a local lightweight database a risk rather than a convenience?
- Where does an application's responsibility for logs end?
- What does the exit code tell you about how a process was stopped?

---

[Course README](../../README.md) · [DevOps & Site Reliability Engineering on LearnSome.tech](https://learnsome.tech/courses/devops-course)
