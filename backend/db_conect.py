from backend.config import Settings
from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient

@lru_cache()
def get_settings():
    return Settings()

def connect_database():
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client["Employees_Database"]
    print("Connected to database")
    return db


