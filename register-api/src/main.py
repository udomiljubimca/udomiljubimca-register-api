import logging
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
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

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.post("/register")
async def newreg(item:Item):
    CreateUser(item.email, item.username, item.enabled, item.firstName, item.lastName).new_user()
    return {"REGISTRATION" : "SUCCESSFUL"}

if __name__ == "__main__":
    uvicorn.run(app, port=8081, loop="asyncio")