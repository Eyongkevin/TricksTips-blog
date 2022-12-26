dev:
	python manage.py runserver --settings=config.settings.dev

prod:
	python manage.py runserver --insecure --settings=config.settings.prod

dev-shell:
	python manage.py shell --settings=config.settings.dev

prod-shell:
	python manage.py shell --settings=config.settings.prod

dev-install:
	pip3 install -r requirements/dev.txt

prod-install:
	pip3 install -r requirements/prod.txt

migrate:
	python manage.py migrate

dev-migrate:
	python manage.py migrate --settings=config.settings.dev
	
prod-migrate:
	python manage.py migrate --settings=config.settings.prod

prod-local-migrate:
	python manage.py migrate --settings=config.settings.prod_local

dev-makemigration:
	python manage.py makemigrations $(m) --settings=config.settings.dev

prod-makemigration:
	python manage.py makemigrations $(m) --settings=config.settings.prod

prod-local-m:
	python manage.py makemigrations $(m) --settings=config.settings.prod_local

prod-check:
	python manage.py check --deploy --settings=config.settings.prod

dev-g:
	sudo gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.prod_local -c config/prod/gunicorn/dev.py

cs-g:
	python manage.py collectstatic --settings=config.settings.prod_local

cs:
	python manage.py collectstatic --settings=config.settings.prod