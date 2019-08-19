release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn self_examination_site.wsgi --log-file -
