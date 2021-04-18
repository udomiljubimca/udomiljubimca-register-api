import logging
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from createuser import CreateUser


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

class Item(BaseModel):
    email : str
    username : str
    enabled : str
    firstName : str
    lastName : str
    secret: str

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.post("/register")
async def register(item:Item):
    checkerica = CreateUser(item.email, item.username, item.enabled, item.firstName, item.lastName, item.secret).checker()
    if checkerica['exist'] == False:
        CreateUser(item.email, item.username, item.enabled, item.firstName, item.lastName, item.secret).new_user()
        return {"Msg" : "The user has been successfully created!"}
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")