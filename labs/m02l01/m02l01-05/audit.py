# DevOps & Site Reliability Engineering — lesson m02l01 — Codebase And Dependencies
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l01
# © LearnSome.tech
def check(variant):
    path = os.path.join(HERE, variant)
    files = sorted(os.listdir(path))
    source = open(os.path.join(path, "app.py")).read()
    live = probe(variant)
    return {
        "I": not [f for f in files if re.search(r"(dev|prod|staging)", f)],
        "II": "requirements.txt" in files,
