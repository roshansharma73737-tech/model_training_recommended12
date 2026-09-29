from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="School API")

@app.get("/")
def homepage():
    return {"message" :"Welcome  to school api"}

# ---------- Data model 

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=4, lt=100)
    course: str
    email: Optional[str] = None


db = {}
counter = 1

# ---------- CREATE 

@app.post("/students", status_code=201)
def add_student(student: Student):
    global counter
    db[counter] = student
    counter += 1
    return {"id": counter - 1, "student": student}


@app.get("/students")
def list_students(course: Optional[str] = None):
    if course:
        return {i: s for i, s in db.items() if s.course == course}
    return db


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    return db[student_id]

# ---------- UPDATE 


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    db[student_id] = student
    return {"message": "Updated", "student": student}

# ---------- DELETE 


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    del db[student_id]
    return {"message": "Deleted"}