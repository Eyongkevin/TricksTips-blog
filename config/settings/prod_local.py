from .prod import *


ALLOWED_HOSTS: list[str] = [
    "mtt.local",
]
CSRF_TRUSTED_ORIGINS = ["http://mtt.local.com"]

# -- Redirect all HTTP calls to HTTPS
SECURE_SSL_REDIRECT = False

# -- Instructs the browser to only send cookies over https connection.
SESSION_COOKIE_SECURE = False

# -- Enable csrf protection to reject any post coming from http connection.
CSRF_COOKIE_SECURE = False

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


STATIC_ROOT = (
    "/usr/local/var/www/mtt/staticfiles"  # str(BASE_DIR.joinpath("staticfiles"))
)
