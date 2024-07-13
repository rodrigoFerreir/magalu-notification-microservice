
#!/bin/bash



set -e
set -u

echo Iniciando projeto celery 🚀...
docker exec -it app-magalu-ms python -m celery --app config.celery worker -B -E -Q celery -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

