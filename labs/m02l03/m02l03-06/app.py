# DevOps & Site Reliability Engineering — lesson m02l03 — Build, Release, Run And Processes
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l03
# © LearnSome.tech
def handle(path, store):
    """VI  every request is served from a backing service, not from memory."""
    store["hits"] = store.get("hits", 0) + 1
    log("request", path=path, hits=store["hits"])
    return 200, "hits {}".format(store["hits"])
