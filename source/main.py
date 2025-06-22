from fastapi import FastAPI
from source.database import engine
from source.models import vehicle
from source.routers import vehicles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    # or your React app domain when deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FleetTrack Backend Running"}

app.include_router(vehicles.router)
