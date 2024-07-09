
from . import *
from datetime import datetime

class Notification(BaseClassModel):
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    channel = models.CharField(max_length=10, choices=Channel.choices)
    message = models.TextField(null=False, blank=False)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    execution_date = models.DateTimeField()
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

