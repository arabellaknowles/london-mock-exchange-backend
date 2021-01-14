release: python lmebackend/manage.py makemigrations --no-input
release: python lmebackend/manage.py migrate --no-input

web: gunicorn lme_backend/lme_backend.wsgi