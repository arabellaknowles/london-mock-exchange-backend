release: python lme_backend/manage.py makemigrations --no-input
release: python lme_backend/manage.py migrate --no-input

web: gunicorn --pythonpath lme_backend lme_backend.wsgi