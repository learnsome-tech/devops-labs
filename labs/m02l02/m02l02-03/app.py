# DevOps & Site Reliability Engineering — lesson m02l02 — Config And Backing Services
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l02
# © LearnSome.tech
ENV = "development"             # X    dev and prod take different branches
DB_PATH = "quotes.db"           # III  config is baked into the code
API_KEY = "shhh-do-not-tell"    # III  a credential in version control
PORT = 8080                     # VII  the port is not the platform's choice
LOG_FILE = "quotes.log"         # XI   logs are a file this process manages

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

HITS = 0                        # VI   request state lives in the process
CACHE = {}                      # VI   and dies with the process
LOCK = threading.Lock()         # VIII scale means more threads in here
