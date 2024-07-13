import datetime
from dataclasses import dataclass

from .CreateContactDTO import CreateContactDTO

@dataclass
class CreateNotificationDTO:
    message:str
    channel:str
    type:str
    execution_date:str | None
    contact:CreateContactDTO

    def __post_init__(self):
        if self.execution_date is None:
            self.execution_date = datetime.datetime.now() + datetime.timedelta(minutes=1)
            self.execution_date = self.execution_date.strftime("%Y-%m-%d %H:%M")