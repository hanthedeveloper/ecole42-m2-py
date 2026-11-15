from pydantic import BaseModel, Field


class MyModel(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field()
    power_level: float
    oxygen_level: float
    last_maintenance: ??
    is_operational: bool = Filed(default=True)


    @model_validator(mode=’after’)

def main():