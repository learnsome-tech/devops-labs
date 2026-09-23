# DevOps & Site Reliability Engineering — lesson m02l06 — Admin Processes And The Open Source Update
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l06
# © LearnSome.tech
"""XII  admin processes: one-off tasks, same code, same config, own process."""
import os
import sys

import app


def migrate():
    app.log("migrate", database=os.environ["DATABASE_URL"])
    return "schema at revision two"


def seed():
    app.log("seed", rows=3)
    return "three quotes inserted"


TASKS = {"migrate": migrate, "seed": seed}
