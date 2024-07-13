from __future__ import absolute_import, unicode_literals

from .celery import app
from notification.services.SendNotificationService import SendNotificationService
from datetime import datetime

@app.task()
def send_notifications():
    SendNotificationService.execute()
