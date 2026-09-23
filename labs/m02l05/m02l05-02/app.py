# DevOps & Site Reliability Engineering — lesson m02l05 — Disposability, Dev Prod Parity And Logs
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l05
# © LearnSome.tech
    return HTTPServer(("127.0.0.1", port), Handler)


def shutdown(signum, frame):
    """IX  a fast, clean exit on the signal the platform actually sends."""
    log("shutdown", signal=signum)
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown)
