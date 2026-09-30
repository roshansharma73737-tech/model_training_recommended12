from fastapi import Depends, Header, HTTPException
from dotenv import load_dotenv
from fastapi import BackgroundTasks
from fastapi import FastAPI
import os


load_dotenv()
app = FastAPI(title="testing_api")
API_token = os.getenv("API_token")


def verify_token(token: str = Header(...)):
    if token != "API_token":
        raise HTTPException(status_code=401, detail="Invalid token  ! ")
    return token


def send_email(email: str):
    print(f"sending welcome  emailto {email}")


@app.post("/email/sending")
def sending(email: str , task: BackgroundTasks):
    task.add_task(send_email,email)
    return {"message": "Account created ! "}

@app.get("/admin/data")
def admin_data(token: str = Depends(verify_token)):
    return {"secret": "only logged-in users can see this"}
