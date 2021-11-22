## Run the Celery worker
celery -A hyperion_backend.celery_worker.celery_app worker --loglevel=info -c 1 -P solo

## Run the Flask server
python -m hyperion_backend