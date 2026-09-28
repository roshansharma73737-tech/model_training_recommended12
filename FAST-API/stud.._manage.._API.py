from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field
from typing  import  Optional 


app = FastAPI(title="school_API")


# create the data Model :---->
class student(BaseModel):
    name:str = Field (min_length= 2 , max_length= 50)
    age : int = Field(gt=4,lt= 100)
    course : str
    email : Optional [str] = None

# Fake dictionary created --->
db = {}
counter = 1 

# CREATE THE " creation of the users "  MODEL--->

@app.post("/students", status_code=201)
def add_student(student: student):
    global counter
    db[counter] = student 
    counter +=1
    return {"id": counter -1, "student" :student }

#  READ THE DATABASE QUREY  PARMETER ---->

@app.get("/students")
def list_students(course :Optional[str] = None):
    if course :
        return {i: s for i, s in db.items() if s.course == course}
    return db 

#   Read one paramete  form the database --->

@app.get("/students")
def search_stud(course : Optional[str]= None ):
    if (course):
        return {"message" : f"this is students {course}"} 