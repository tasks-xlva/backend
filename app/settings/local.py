from .default import *
from dotenv import dotenv_values

env = {**dotenv_values("./.envs/.local/.postgres.env"), **env}

DATABASES["default"]["PASSWORD"] = env["POSTGRES_PASSWORD"]
DATABASES["default"]["HOST"] = "127.0.0.1"
