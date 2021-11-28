from .default import *

DATABASES["default"]["PASSWORD"] = env["POSTGRES_PASSWORD"]
DATABASES["default"]["HOST"] = "postgres"

ALLOWED_HOSTS = [FRONTEND_HOST]
