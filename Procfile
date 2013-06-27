web: gunicorn PCS.wsgi
worker: celery -A tasks worker -B --loglevel=info
