from pydantic import BaseModel, Field


class Employee(BaseModel):
    name: str = Field(...,min_length=3,max_length=15)
    age: int
    department: str = Field(...,min_length=5,max_length=20)
    is_available: bool