from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import validator
from statistics import mean

class Beer(SQLModel, table=True):
    id: Optional(int) = Field(primary_key=True, default=None, index=True) 
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    # Comentary
    # NEW
    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field): 
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculator_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)

beer = Beer(name="Lagunitas", style="NEIPA", flavor=3, image=6, cost=8)