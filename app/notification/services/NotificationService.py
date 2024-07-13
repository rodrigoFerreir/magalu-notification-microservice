
import logging
from typing import Dict, List, Any, Optional
from notification.dto.CreateNotificationDTO import CreateNotificationDTO
from notification.models import Contact, Notification, Status
from notification.serializers.NotificationSerializer import NotificationSerializer

logger = logging.getLogger(__name__)

class NotificationService():

    def __init__(self,) -> None:
        pass


    def create(self, data: dict) -> dict:
        notification_dto = CreateNotificationDTO(**data)
        contact, created = Contact.objects.get_or_create(**notification_dto.contact)
                                                        
                                                        
        if created: logger.info("Novo contato adicionado ao banco de dados")
        
        notification = Notification.objects.create(
            message = notification_dto.message,
            channel = notification_dto.channel,
            type_task = notification_dto.type,
            execution_date = notification_dto.execution_date,
            contact=contact
        )
        
        logger.info(f"Notificação {notification.id} foi criada")
        return NotificationSerializer.execute(notification)                                        
    

    def get(self, notification_id:Optional[str] = None, status:Optional[str] = None) -> List[Dict[str, Any]]:
        logger.info(f"Buscando por notificações, filtro notification_id: {notification_id}, status: {status}")
        data = Notification.objects.all()

        if notification_id is not None:
            data = data.filter(id = notification_id)
        if status is not None:
            data = data.filter(status = status)
        
        logger.info(f"Foram encontradas {len(data)} notificações")
        
        return [NotificationSerializer.execute(item) for item in data]


    def delete(self, notification_id: str) -> bool:
        data = Notification.objects.filter(id=notification_id).last()
        if data and data.status == Status.PENDING:
            data.status = Status.CANCELLED
            data.save()
            logger.info(f"Notificação {notification_id} foi cancelada")
            return True
        
        logger.warning(f"Notificação {notification_id} nao foi encontrada")
        return False

