from database import SessionLocal
from models.vehicle import Vehicle

db = SessionLocal()

vehicle1 = Vehicle(name="Truck Alpha", lat=19.0760, lng=72.8777)
vehicle2 = Vehicle(name="Van Beta", lat=28.7041, lng=77.1025)

db.add(vehicle1)
db.add(vehicle2)
db.commit()

db.close()
