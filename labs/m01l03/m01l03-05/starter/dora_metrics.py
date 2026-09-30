    rework = [d for d in deploys
              if any(TRAILER.search(c["body"]) for c in d["changes"])]
    failed = [d for d in deploys if d["tag"] in remediations]
    total = len(deploys)
