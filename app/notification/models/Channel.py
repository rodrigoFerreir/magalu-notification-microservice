
from dataclasses import dataclass
from . import *


@dataclass
class Channel(models.TextChoices):
    EMAIL = "EMAIL"
    SMS = "SMS"
    WHATSAPP = "WHATSAPP"

