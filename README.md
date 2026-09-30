<p>
  <a href="https://learnsome.tech/courses/devops-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# DevOps & Site Reliability Engineering

**DORA Metrics, Twelve-Factor Apps, Platform Engineering & SRE**

8 modules, 39 lessons: Measurement And Outcomes: DORA; The Twelve-Factor App; Collaboration and Continuous Integration; Continuous Delivery and Deployment; Service Level Objectives (SRE); Incident Response and Postmortems; Platform Engineering and IDPs; The Modern DevOps Toolchain Handoff. Advanced level, about 2 hours.

This repository holds the labs of the LearnSome.tech course [DevOps & Site Reliability Engineering](https://learnsome.tech/courses/devops-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/devops-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7 and Git 2.34 (Ubuntu 22.04's), as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/devops-labs.git
  cd devops-labs
  ./check m01l01-04
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7 and Git 2.34 (Ubuntu 22.04's). Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-04`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 28 |
| Runs, not graded | Runs the program and shows its output; the site gives no pass or fail, and the lab README says why. | 1 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 25 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: Measurement And Outcomes: DORA

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [What DevOps Actually Is](https://learnsome.tech/learn/devops-course/m01l01) | [2 labs](labs/m01l01/) | Free |
| 1.2 | [Throughput: Change Lead Time And Deployment Frequency](https://learnsome.tech/learn/devops-course/m01l02) | [4 labs](labs/m01l02/) | Free |
| 1.3 | [Instability: Change Fail Rate And Deployment Rework Rate](https://learnsome.tech/learn/devops-course/m01l03) | [3 labs](labs/m01l03/) | Free |
| 1.4 | [Restoration: Failed Deployment Recovery Time](https://learnsome.tech/learn/devops-course/m01l04) | [3 labs](labs/m01l04/) | Free |
| 1.5 | [The Four Keys History And Retiring MTTR](https://learnsome.tech/learn/devops-course/m01l05) | [2 labs](labs/m01l05/) | Free |
| 1.6 | [The Pitfalls Of Measurement](https://learnsome.tech/learn/devops-course/m01l06) | [2 labs](labs/m01l06/) | Pro |

### Module 2: The Twelve-Factor App

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Codebase And Dependencies](https://learnsome.tech/learn/devops-course/m02l01) | [3 labs](labs/m02l01/) | Pro |
| 2.2 | [Config And Backing Services](https://learnsome.tech/learn/devops-course/m02l02) | [3 labs](labs/m02l02/) | Pro |
| 2.3 | [Build, Release, Run And Processes](https://learnsome.tech/learn/devops-course/m02l03) | [4 labs](labs/m02l03/) | Pro |
| 2.4 | [Port Binding And Concurrency](https://learnsome.tech/learn/devops-course/m02l04) | [3 labs](labs/m02l04/) | Pro |
| 2.5 | [Disposability, Dev Prod Parity And Logs](https://learnsome.tech/learn/devops-course/m02l05) | [4 labs](labs/m02l05/) | Pro |
| 2.6 | [Admin Processes And The Open Source Update](https://learnsome.tech/learn/devops-course/m02l06) | [4 labs](labs/m02l06/) | Pro |

### Module 3: Collaboration and Continuous Integration

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [SDLC: From Request To Running Software](https://learnsome.tech/learn/devops-course/m03l01) | [2 labs](labs/m03l01/) | Pro |
| 3.2 | [Trunk-Based Development Versus Git Flow](https://learnsome.tech/learn/devops-course/m03l02) | [2 labs](labs/m03l02/) | Pro |
| 3.3 | [Continuous Integration](https://learnsome.tech/learn/devops-course/m03l03) | [2 labs](labs/m03l03/) | Pro |
| 3.4 | [Testing Strategies And The Test Pyramid](https://learnsome.tech/learn/devops-course/m03l04) | [1 lab](labs/m03l04/) | Pro |
| 3.5 | [Building And Versioning The Artifact](https://learnsome.tech/learn/devops-course/m03l05) | [2 labs](labs/m03l05/) | Pro |

### Module 4: Continuous Delivery and Deployment

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Continuous Delivery Versus Continuous Deployment](https://learnsome.tech/learn/devops-course/m04l01) | – | Pro |
| 4.2 | [Deployment Strategies: Rolling Updates](https://learnsome.tech/learn/devops-course/m04l02) | [1 lab](labs/m04l02/) | Pro |
| 4.3 | [Deployment Strategies: Blue Green](https://learnsome.tech/learn/devops-course/m04l03) | [1 lab](labs/m04l03/) | Pro |
| 4.4 | [Deployment Strategies: Canary Releases](https://learnsome.tech/learn/devops-course/m04l04) | [1 lab](labs/m04l04/) | Pro |
| 4.5 | [Decoupling Release From Deployment: Feature Flags](https://learnsome.tech/learn/devops-course/m04l05) | [1 lab](labs/m04l05/) | Pro |

### Module 5: Service Level Objectives (SRE)

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Service Level Indicators](https://learnsome.tech/learn/devops-course/m05l01) | – | Pro |
| 5.2 | [Percentiles Rather Than Averages](https://learnsome.tech/learn/devops-course/m05l02) | [1 lab](labs/m05l02/) | Pro |
| 5.3 | [Service Level Objectives](https://learnsome.tech/learn/devops-course/m05l03) | – | Pro |
| 5.4 | [Service Level Agreements: The Consequence Discriminator](https://learnsome.tech/learn/devops-course/m05l04) | – | Pro |
| 5.5 | [Error Budgets](https://learnsome.tech/learn/devops-course/m05l05) | [1 lab](labs/m05l05/) | Pro |

### Module 6: Incident Response and Postmortems

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [On-Call And Incident Response](https://learnsome.tech/learn/devops-course/m06l01) | – | Pro |
| 6.2 | [The Incident Lifecycle](https://learnsome.tech/learn/devops-course/m06l02) | [1 lab](labs/m06l02/) | Pro |
| 6.3 | [The Blameless Postmortem](https://learnsome.tech/learn/devops-course/m06l03) | – | Pro |
| 6.4 | [Writing A Postmortem: The SRE Appendix](https://learnsome.tech/learn/devops-course/m06l04) | [1 lab](labs/m06l04/) | Pro |

### Module 7: Platform Engineering and IDPs

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 7.1 | [Developer Toil And Cognitive Load](https://learnsome.tech/learn/devops-course/m07l01) | – | Pro |
| 7.2 | [Team Topologies: Stream Aligned And Platform Teams](https://learnsome.tech/learn/devops-course/m07l02) | – | Pro |
| 7.3 | [Internal Developer Platforms](https://learnsome.tech/learn/devops-course/m07l03) | – | Pro |
| 7.4 | [The CNCF Platforms White Paper](https://learnsome.tech/learn/devops-course/m07l04) | – | Pro |

### Module 8: The Modern DevOps Toolchain Handoff

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 8.1 | [Infrastructure As Code Context](https://learnsome.tech/learn/devops-course/m08l01) | – | Pro |
| 8.2 | [Containers And Orchestration Context](https://learnsome.tech/learn/devops-course/m08l02) | – | Pro |
| 8.3 | [Pipelines And GitOps Context](https://learnsome.tech/learn/devops-course/m08l03) | – | Pro |
| 8.4 | [Observability Context](https://learnsome.tech/learn/devops-course/m08l04) | – | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
