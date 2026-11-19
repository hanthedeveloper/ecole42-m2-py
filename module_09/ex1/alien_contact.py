from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator
)
from datetime import datetime
from enum import Enum
from typing import Optional


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
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with "AC" (Alien Contact)")
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
            contact_id = "AC_2024_001",
            timestamp = "2024-01-15T10:30:00",
            location = "Area 51, Nevada",
            contact_type = "radio",
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 5,
            message_received = "Greetings from Zeta Reticuli",
            is_verified = False
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print("Valid contact report:")
    print("ID:", ac_instance1.contact_id)
    print("Type:", ac_instance1.contact_type.value)
    print("Location:", ac_instance1.location)
    print(f"Signal: {ac_instance1.signal_strength}/10")
    print("Duration:", ac_instance1.duration_minutes, "minutes")
    print("Witnesses:", ac_instance1. witness_count)
    print("Message:", ac_instance1. message_received)

    print()
    print("======================================")
    print("Expected validation error:")

    try:
        ac_instance2 = AlienContact(
            contact_id = "AC_2024_001",
            timestamp = "2024-01-15T10:30:00",
            location = "Area 51, Nevada",
            contact_type = "telepathic",
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 1,
            message_received = "Greetings from Zeta Reticuli",
            is_verified = False
        )
    except ValidationError as e:
        for err in e.errors():
            print((err["msg"]).replace("Value error, ", ""))

if __name__ == "__main__":
    main()