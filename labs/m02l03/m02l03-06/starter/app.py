def handle(path, store):
    """VI  every request is served from a backing service, not from memory."""
    store["hits"] = store.get("hits", 0) + 1
    log("request", path=path, hits=store["hits"])
    return 200, "hits {}".format(store["hits"])
