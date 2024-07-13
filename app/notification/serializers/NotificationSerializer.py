



from typing import Dict, Any
from notification.models import Notification


class NotificationSerializer():

    @staticmethod
    def execute(notification:Notification) -> Dict[str, Any]:
        return {
            "id": notification.id,
            "channel": notification.channel,
            "message": notification.message,
            "type": notification.type_task,
            "execution_date": notification.execution_date,
            "status":notification.status,
            "created_at": notification.created_at,
            "updated_at": notification.updated_at,
            "contact": {
                "id": notification.contact.id,
                "name": notification.contact.name,
                "email": notification.contact.email,
                "phone":notification.contact.phone
            },
        }