from fastapi import FastAPI
from backend.routes import employee

app = FastAPI()

app.include_router(employee.router, prefix="/employees", tags=["Employees"])
