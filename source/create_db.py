from source.models.vehicle import Vehicle
from source.database import engine, Base

Base.metadata.create_all(bind=engine)
print("✅ All tables created successfully.")
