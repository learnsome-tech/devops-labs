def handle(path):
    """IV  the store is a local file, not an attached resource."""
    global HITS
    with LOCK:
        HITS += 1
    if ENV == "production":
        logging.info("served %s in prod", path)
    else:
        logging.info("served %s", path)
    return 200, "hits {}".format(HITS)
