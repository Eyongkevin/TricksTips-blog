web: python manage.py migrate --settings=config.settings.prod && gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.prod -c config/prod/gunicorn/prod.py