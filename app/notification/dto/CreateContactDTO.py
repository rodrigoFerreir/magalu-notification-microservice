
from dataclasses import dataclass

@dataclass
class CreateContactDTO:
    name: str
    phone: str
    email: str