import logging
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from createuser import CreateUser
from docs import register_api_docs

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI(openapi_tags = register_api_docs, openapi_url = "/api/latest/register-api/openapi.json")

class Item(BaseModel):
    email : str
    username : str
    firstName : str
    lastName : str
    secret: str

@app.get("/health", tags = ["Provera rada aplikacije"])
async def index():
    return {"HEALTH" : "OK"}

@app.post("/register", tags = ["Registracija"])
async def register(item:Item):
    checkerica = CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).checker()
    if checkerica['exist'] == False:
        CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).new_user()
        return {"message" : "The user has been successfully created!"}
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")


if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")