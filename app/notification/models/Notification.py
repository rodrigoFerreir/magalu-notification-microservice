
from . import *
from datetime import datetime, timedelta

class Notification(BaseClassModel):
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    channel = models.CharField(max_length=10, choices=Channel.choices)
    message = models.TextField(null=False, blank=False)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    execution_date = models.DateTimeField(default=datetime.now() + timedelta(minutes=2))
    start_date = models.DateField(null=True, default=None)
    end_date = models.DateField(null=True, default=None)
    type_task = models.CharField(max_length=10, choices=TypeTaskNotification.choices)


    def __str__(self) -> str:
        return str(self.id)
    

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'



    def verify_execution_date(self) -> bool:
        return self.execution_date <= datetime.now()

    def verify_periodic_task(self) -> bool:
        return self.start_date >= datetime.date() and self.end_date <= datetime.date()

    def send_notification(self) -> None:
        try:
            if self.channel == Channel.EMAIL:
                print("[INFO] Enviando mensagem via email...")
                self.status = Status.SUCCESS
            elif self.channel == Channel.SMS:
                print("[INFO] Enviando mensagem via sms...")
                self.status = Status.SUCCESS
            elif self.channel == Channel.WHATSAPP:
                print("[INFO] Enviando mensagem via whatsapp...")
                self.status = Status.SUCCESS
            else:
                self.status = Status.FAILED
                raise Exception("Type channel not implemented!")
        except Exception as error:
            self.status = Status.FAILED
            raise Exception(error)
        finally:
            self.updated_at = datetime.now()
            self.save()