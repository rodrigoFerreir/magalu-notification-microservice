from __future__ import absolute_import, unicode_literals

from .celery import app
from notification.models import Notification, Status
from datetime import datetime

@app.task()
def send_notifications():
    for item in Notification.objects.filter(status = 'pending'):
        if item.verify_execution_date():
            print("="*10)
            print(f"Enviando notificação {item.id}")
            print(f"[MESSAGEM] ::: {item.message}")
            print(f"DATA E HORA ->> {item.execution_date}")
            print("="*10)
            item. status = Status.SUCCESS
            item.updated_at = datetime.now()
            item.save()

