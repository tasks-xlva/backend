from .default import *
from dotenv import dotenv_values

env = {**dotenv_values("./.envs/.production/.env"), **env}

DATABASES["default"]["PASSWORD"] = env["POSTGRES_PASSWORD"]
DATABASES["default"]["HOST"] = "postgres"

ALLOWED_HOSTS = ["tasks.api.xlvn.ru"]

EMAIL_USE_TLS = env["EMAIL_USE_TLS"]
EMAIL_HOST = env["EMAIL_HOST"]
EMAIL_PORT = env["EMAIL_PORT"]
EMAIL_HOST_USER = env["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = env["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL = env["DEFAULT_FROM_EMAIL"]

SECRET_KEY = env["SECRET_KEY"]
