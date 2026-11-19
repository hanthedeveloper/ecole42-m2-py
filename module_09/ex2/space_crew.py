from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator
)
from datetime import datetime
from enum import Enum
from typing import Optional


class Rank

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Feild(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: DateTime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10_000)

    @model_validator(mode=’after’)
    def validate(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must starts with M")
        if not all(crew_mem.is_active for crew_mem in self.crew):
            raise ValueError("All crew members must be active")
        experienced_crew += 
        if self.duration_days > 365 and not all(rew_mem.years_experience > 5 for crew_mem in self.crew)