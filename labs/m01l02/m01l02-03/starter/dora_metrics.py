def deployments():
    """Every deployment tag, oldest first, with the commits it carried."""
    shape = "%(refname:short) %(taggerdate:iso-strict)"
    rows = git("for-each-ref", "--sort=taggerdate", "--format=" + shape,
               "refs/tags/deploy-*").splitlines()
    pairs = (row.split(" ", 1) for row in rows)
    tags = [(name, when(date)) for name, date in pairs]
    out, previous = [], None
    for name, date in tags:
        span = f"{previous}..{name}" if previous else name
        log = git("log", "--format=%H%x1f%aI%x1f%B%x1e", span)
        changes = []
        for entry in (e for e in log.split("\x1e") if e.strip()):
            sha, authored, body = entry.strip().split("\x1f", 2)
            changes.append({"sha": sha, "authored": when(authored),
                            "body": body})
        out.append({"tag": name, "at": date, "changes": changes})
        previous = name
    return out
