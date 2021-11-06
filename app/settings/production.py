from .default import *

DATABASES["default"]["PASSWORD"] = env["POSTGRES_PASSWORD"]
DATABASES["default"]["HOST"] = "postgres"

ALLOWED_HOSTS = ["tasks.api.xlvn.ru"]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
