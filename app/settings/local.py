from .default import *

env = {**dotenv_values("./.envs/.local/.postgres.env"), **env}

DATABASES["default"]["PASSWORD"] = env.get("POSTGRES_PASSWORD")
DATABASES["default"]["HOST"] = "127.0.0.1"
