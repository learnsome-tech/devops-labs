    return HTTPServer(("127.0.0.1", port), Handler)


def shutdown(signum, frame):
    """IX  a fast, clean exit on the signal the platform actually sends."""
    log("shutdown", signal=signum)
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown)
