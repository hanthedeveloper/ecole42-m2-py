from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        ss_instance1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print("Valid station created:")
    print(ss_instance1.station_id)
    print(ss_instance1.name)
    print(ss_instance1.crew_size)
    print(ss_instance1.power_level)
    print(ss_instance1.oxygen_level)
    print(ss_instance1.last_maintenance)
    print()

    print("========================================")
    print("Expected validation error:")

    try:
        ss_instance2 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

if __name__ == "__main__":
    main()