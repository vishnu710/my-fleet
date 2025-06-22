from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int
    name: str
    lat: float
    lng: float
