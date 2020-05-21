web: gunicorn news.wsgi --log-file -
worker: celery -A schedules worker -B -l debug