from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator
)
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10_000)

    @model_validator(mode='after')
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must starts with M")
        if not all(crew_mem.is_active for crew_mem in self.crew):
            raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            experienced = sum(1 for crew_mem in self.crew if crew_mem.years_experience >= 5)
            if experienced < (len(self.crew) / 2):
                raise ValueError("Long missions need 50% experienced crew")
        if not any(m.rank in (Rank.COMMANDER, Rank.CAPTAIN) for m in self.crew):
            raise ValueError("Mission must have at least one Commander or Captain")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    crew_instances = [
        {"member_id": "C001", "name": "Sarah Connor", "rank": "commander",
         "age": 45, "specialization": "Mission Command",
         "years_experience": 20},
        {"member_id": "C002", "name": "John Smith", "rank": "lieutenant",
         "age": 38, "specialization": "Navigation",
         "years_experience": 15},
        {"member_id": "C003", "name": "Alice Johnson", "rank": "officer",
         "age": 32, "specialization": "Engineering",
         "years_experience": 8},
    ]

    mission = SpaceMission(
        mission_id = "M2024_MARS",
        mission_name = "Mars Colony Establishment",
        destination = "Mars",
        launch_date = datetime(2026, 12, 1),
        duration_days = 900,
        crew = crew_instances,
        budget_millions = 2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for m in mission.crew:
        print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    print("=========================================")

    bad_crew = [
        {"member_id": "C002", "name": "John Smith", "rank": "lieutenant",
         "age": 38, "specialization": "Navigation",
         "years_experience": 15},
        {"member_id": "C003", "name": "Alice Johnson", "rank": "officer",
         "age": 32, "specialization": "Engineering",
         "years_experience": 8},
    ]

    try:
        SpaceMission(
            mission_id = "M2024_MOON",
            mission_name = "Moon Base",
            destination = "Moon",
            launch_date = datetime(2026, 12, 1),
            duration_days = 100,
            crew = bad_crew,
            budget_millions = 500.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        msg = e.errors()[0]["msg"]
        print(msg.removeprefix("Value error, "))


if __name__ == "__main__":
    main()

