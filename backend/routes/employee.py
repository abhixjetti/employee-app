from typing import List

from bson import ObjectId
from fastapi import  HTTPException, APIRouter
from backend.Models.Employee import Employee
from backend.db_conect import connect_database

router = APIRouter()
db= connect_database()
employee_collection=db["employees"]


@router.post("/add-employee")
def add_employee(employee: Employee):
    employee_dict = employee.model_dump()
    result = employee_collection.insert_one(employee_dict)
    employee_dict["_id"] = str(result.inserted_id)
    return {
        "message":"employee added",
        "employee": employee_dict
    }
@router.get("/get-employees")
def get_employee():
    employees=[]
    for employee in employee_collection.find():
        employee["_id"] = str(employee["_id"])
        employees.append(employee)
    return {"employees": employees}
@router.put("/update-employee/{employee_id}")
def update_employee(employee: Employee,employee_id:str):
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(status_code=400, detail="invalid employee id")
    employee_dict = employee.model_dump()
    result = employee_collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": employee_dict}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="employee not found")
    return {"message":"employee updated"}

@router.delete("/delete-employee/{employee_id}")
def delete_employee(employee_id:str):
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(status_code=400, detail="invalid employee id")
    result = employee_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="employee not found")
    return {"message":"employee deleted"}
@router.get('/available-employees',response_model=List[Employee])
def get_available_employees():
    available_employees = employee_collection.find({'is_available':True})
    return available_employees
