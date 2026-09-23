# DevOps & Site Reliability Engineering — lesson m01l04 — Restoration: Failed Deployment Recovery Time
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l04
# © LearnSome.tech
    recovery = [(fix["at"] - broken["at"]).total_seconds() / 60
                for broken in deploys if broken["tag"] in remediations
                for fix in [remediations[broken["tag"]]]]
