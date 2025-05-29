from pymongo import MongoClient
from backend.config import Settings
from functools import lru_cache

@lru_cache()
def get_settings():
    return Settings()

def connect_database():
    settings = get_settings()
    client = MongoClient(settings.mongo_uri)
    db = client["Employees_Database"]
    print("Connected to database")
    return db


