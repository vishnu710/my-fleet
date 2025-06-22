from fastapi import APIRouter, Depends
from .sqlalchemy.orm import Session
from .database import SessionLocal
from .models.vehicle import Vehicle as VehicleModel
from .schemas.vehicle_schema import Vehicle as VehicleSchema
from typing import List

router = APIRouter()

# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vehicles", response_model=List[VehicleSchema])
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(VehicleModel).all()
    return vehicles
