
from typing import Dict, List, Any, Optional
from notification.models import Contact, Notification, Status
from notification.serializers.NotificationSerializer import NotificationSerializer


class NotificationService():

    def __init__(self,) -> None:
        pass

    
    def create(self, data: dict) -> dict:
        contact, created = Contact.objects.get_or_create(name=data['contact']["name"], phone=data['contact'].get('phone'), email=data['contact'].get("email"))
                                                        
                                                        
        if created: print("Novo contato adicionado ao banco de dados")
        
        
        notification = Notification.objects.create(
            message=data['message'], 
            channel=data['channel'], 
            execution_date=data['execution_date'],
            type_task=data['type'],
            contact=contact
        )

        return NotificationSerializer.execute(notification)                                        
    
    def get(self, notification_id:Optional[str], status:Optional[str]) -> List[Dict[str, Any]]:
        data = Notification.objects.all()

        if notification_id is not None:
            data = data.filter(id = notification_id)
        if status is not None:
            data = data.filter(status = status)
        
        return [NotificationSerializer.execute(item) for item in data]

    

    def delete(self, notification_id: str) -> bool:
        data = Notification.objects.get(id=notification_id)
        if data and data.status == Status.PENDING:
            data.status = Status.CANCELLED
            data.save()
            return True
        return False

