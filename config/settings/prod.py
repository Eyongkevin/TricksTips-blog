import os
import environ
import mimetypes
from .base import *

ADMINS = (("Eyong Kevin Enowanyo", "tonyparkerkenz@gmail.com"),)


mimetypes.add_type("text/css", ".css", True)
env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS: list[str] = [
    "web-production-b4c7.up.railway.app",
    ".mytricksntips.com",
]
CSRF_TRUSTED_ORIGINS = [
    "https://web-production-b4c7.up.railway.app",
    "https://www.mytricksntips.com",
]

# INSTALLED_APPS += ["whitenoise.runserver_nostatic"]
# -- Redirect all HTTP calls to HTTPS
# SECURE_SSL_REDIRECT = True

# -- Instructs the browser to only send cookies over https connection.
# SESSION_COOKIE_SECURE = True

# -- Enable csrf protection to reject any post coming from http connection.
# CSRF_COOKIE_SECURE = True

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "csp.middleware.CSPMiddleware",
]
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("DB_NAME"),  # database name
#         "USER": env.str("DB_USER"),  # database user
#         "PASSWORD": env.str("DB_PWD"),  # database password
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

# STATIC_ROOT = (
#     "/usr/local/var/www/mtt/staticfiles"  # str(BASE_DIR.joinpath("staticfiles"))
# )
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (str(BASE_DIR.joinpath("static")),)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Content Security Policy
CSP_DEFAULT_SRC = ["'self'"]
CSP_STYLE_SRC = [
    "'self'",
    "http://fonts.googleapis.com/css?family=Muli",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://fonts.cdnfonts.com/css/glacial-indifference-2",
]
CSP_SCRIPT_SRC = [
    "'self'",
    "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js",
]
CSP_FONT_SRC = [
    "'self'",
    "http://fonts.gstatic.com",
    "https://cdnjs.cloudflare.com",
    "https://fonts.cdnfonts.com/css/glacial-indifference-2",
    "https://fonts.cdnfonts.com/s/31913/GlacialIndifference-Regular.woff",
    "https://fonts.cdnfonts.com/s/31913/GlacialIndifference-Bold.woff",
]
CSP_IMG_SRC = ["*"]
CSP_MEDIA_SRC = ["*"]
CSP_FRAME_SRC = ["*"]

import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}
