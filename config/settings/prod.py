import os
import environ
import mimetypes
from .base import *

mimetypes.add_type("text/css", ".css", True)
env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS: list[str] = ["*"]

# -- Redirect all HTTP calls to HTTPS
# SECURE_SSL_REDIRECT = True

# -- Instructs the browser to only send cookies over https connection.
# SESSION_COOKIE_SECURE = True

# -- Enable csrf protection to reject any post coming from http connection.
# CSRF_COOKIE_SECURE = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),  # database name
        "USER": env.str("DB_USER"),  # database user
        "PASSWORD": env.str("DB_PWD"),  # database password
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
