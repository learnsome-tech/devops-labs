# DevOps & Site Reliability Engineering — lesson m01l02 — Throughput: Change Lead Time And Deployment Frequency
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l02
# © LearnSome.tech
    lead = [(deploy["at"] - change["authored"]).total_seconds() / 3600
            for deploy in deploys for change in deploy["changes"]]
    window = (deploys[-1]["at"] - deploys[0]["at"]).total_seconds() / 86400
