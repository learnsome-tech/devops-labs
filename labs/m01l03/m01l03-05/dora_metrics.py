# DevOps & Site Reliability Engineering — lesson m01l03 — Instability: Change Fail Rate And Deployment Rework Rate
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l03
# © LearnSome.tech
    rework = [d for d in deploys
              if any(TRAILER.search(c["body"]) for c in d["changes"])]
    failed = [d for d in deploys if d["tag"] in remediations]
    total = len(deploys)
