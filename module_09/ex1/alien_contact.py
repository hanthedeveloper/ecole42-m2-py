from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator
)
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(max_length=15, min_length=5)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Feild(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_reeived: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode=’after’)
    def validate(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self 


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        ac_instance1 = AlienContact(
            contact_id = AC_2024_001
            contact_type = radio
            location = Area 51, Nevada
            signal_strength = 8.5
            duration_minutes = 45
            witness_count = 5
            message_received = "Greetings from Zeta Reticuli"

        )
