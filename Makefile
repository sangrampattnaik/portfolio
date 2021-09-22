manage=./manage.py
python=python3

runserver:
	$(python) $(manage) runserver 0.0.0.0:8000

check:
	$(python) $(manage) check

superuser:
	$(python) $(manage) createsuperuser

install:
	pip install -r requirements.txt

migrate:
	$(python) $(manage) makemigrations  && $(python) $(manage) migrate

freeze:
	pip freeze > requirements.txt

shell:
	$(python) $(manage) shell_plus

reset-db:
	$(python) $(manage) reset_db
	make migrate

createsuperuser:
	$(python) $(manage) createsuperuser
