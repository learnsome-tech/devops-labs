# DevOps & Site Reliability Engineering — lesson m02l03 — Build, Release, Run And Processes
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l03
# © LearnSome.tech
RELEASE = os.environ.get("RELEASE", "unknown")      # V   build, release, run
DATABASE_URL = os.environ["DATABASE_URL"]           # III IV config from env
API_KEY = os.environ["API_KEY"]                     # III secrets from env


def log(event, **fields):
    """XI  one event per line, on stdout, for the platform to route."""
    record = {"event": event, "release": RELEASE}
    record.update(fields)
    print(json.dumps(record, sort_keys=True), flush=True)
