from . import *

class TypeTaskNotification(models.TextChoices):

    PERIODIC = "periodic"
    SCHEDULE = "schedule"