from .default import *

DATABASES["default"]["PASSWORD"] = env["POSTGRES_PASSWORD"]
