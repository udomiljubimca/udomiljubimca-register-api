import json
import logging
from typing import Dict, Optional
import jwt
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.responses import RedirectResponse
from pydantic import BaseModel

#from kc_user import Make

APP_BASE_URL = "http://udomi-ljubimca.com.internal"
KEYCLOAK_BASE_URL = "http://udomi-ljubimca.com.internal/auth"
AUTH_URL = (
    f"{KEYCLOAK_BASE_URL}/realms/Clients"
    "/protocol/openid-connect/auth?client_id=app&response_type=code"
)
TOKEN_URL = (
    f"{KEYCLOAK_BASE_URL}/realms/Clients/protocol/openid-connect/token"
)

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

class Item(BaseModel):
    email : str
    username : str
    enabled : str
    first_Name : str
    last_Name : str
    realm_Roles :str
    attributes : str
    values : str

app = FastAPI()

usr = []


@app.get("/index")
async def index():
    
    return {"msg" : "Hello world from Python"}

@app.post("/register/")
async def register(item : Item):

    if any(x['username'] == item.username for x in usr):
        raise HTTPException(status_code = 400, detail = "username already exist")
    
    js = {"email" : item.email, "username" : item.username,"enabled" : item.enabled,"first_Name" : item.first_Name,"last_Name" : item.last_Name,"realm_Roles" : item.realm_Roles, "attributes" : item.attributes,"values" : item.values}
    
    #Make(js['email'], js['username'], js['enabled'], js['firstname'], js['lastName'], js['realmRoles'], js['attributes'], js['values']).pass_args()

    usr.append(js)
    
    return {"msg" : usr}


#"my.email@.gmail.com","ljudina","True","novak","djokovic","user_default","exemple","1,2,3,3,"
#Make(item.email, item.username, item.enabled, item.first_Name, item.last_Name, item.realm_Roles,item.attributes, item.values).pass_args

if __name__ == "__main__":
    uvicorn.run(app, port=8081, loop="asyncio")