def choose_port():
    """VII  the platform hands the port down; the app binds it."""
    return int(os.environ["PORT"])
