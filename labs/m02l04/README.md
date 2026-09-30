# m02l04 · Port Binding And Concurrency

Module 2: The Twelve-Factor App · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/devops-course/m02l04)

**Goal:** You can explain why a twelve-factor app binds a port the platform chooses, describe the process formation model of scaling, and say why processes must never daemonize or write PID files.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | Who decides the port | Read along |
| [m02l04-03](m02l04-03/) | Binding the port you were given | Runs, not graded |
| [m02l04-05](m02l04-05/) | The process formation, declared | Read along |

## Check yourself

- What is the whole contract between a twelve-factor app and its platform?
- Why should the port have no default value in the code?
- What is a process formation, and what does scaling change in it?
- Why is daemonizing harmful under a supervisor or in a container?
- Are threads allowed under factor eight? Explain the distinction.

---

[Course README](../../README.md) · [DevOps & Site Reliability Engineering on LearnSome.tech](https://learnsome.tech/courses/devops-course)
