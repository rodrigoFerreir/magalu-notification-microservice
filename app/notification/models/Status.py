
from dataclasses import dataclass
from . import *

@dataclass
class Status(models.TextChoices):
    PENDING = "pending"
    FAILED = "failed"
    SUCCESS = "success"
    CANCELLED = "cancelled"

