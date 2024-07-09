from __future__ import absolute_import, unicode_literals
from core import settings
from celery import Celery
import django
from celery.signals import celeryd_init

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('celery', broker=settings.CELERY_BROKER_URL, include=['config.tasks'])  # type: ignore
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {
    'tasks': {'queue': 'celery'},
}
app.autodiscover_tasks()


@celeryd_init.connect
def message_test_connection(sender=None, conf=None,  **kwargs):
    print("[CELERY => run ok 🚀]")


if __name__ == '__main__':
    django.setup()
    app.start(print_stdout=True)