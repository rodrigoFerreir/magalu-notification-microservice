
from notification.models import Notification

class SendNotificationService():


    @staticmethod
    def execute() -> None:
        for item in Notification.objects.filter(status = 'pending'):
            if item.verify_execution_date():
                print("="*10)
                print(f"Enviando notificação {item.id}")
                print(f"[MESSAGEM] ::: {item.message}")
                print(f"DATA E HORA ->> {item.execution_date}")
                print("="*10)
                item.send_notification()