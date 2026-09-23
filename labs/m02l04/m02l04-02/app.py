# DevOps & Site Reliability Engineering — lesson m02l04 — Port Binding And Concurrency
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l04
# © LearnSome.tech
def choose_port():
    """VII  the platform hands the port down; the app binds it."""
    return int(os.environ["PORT"])
