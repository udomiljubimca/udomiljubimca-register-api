import logging
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from createuser import CreateUser
from docs import register_api_docs
from resend_email import Resend_verify_email
#from typing import Optional
from create_association import CreateAssociation

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI(openapi_tags = register_api_docs, openapi_url = "/api/latest/register-api/openapi.json")

class Item(BaseModel):
    email : str
    username : str
    firstName : str
    lastName : str
    secret: str

class Item_for_resend(BaseModel):
    username : str

class Item_association(BaseModel):
    email : str
    username_association : str
    secret : str
  
@app.post("/register-association", tags = ["Registracija udruzenja"])
async def register_association(item : Item_association):
    checkerica = CreateAssociation(item.email, item.username_association, item.secret).checker()
    if checkerica['exist'] == False:
        CreateAssociation(item.email, item.username_association, item.secret).new_association()
        check_user_id = CreateAssociation(item.email, item.username_association, item.secret).get_keycloak_user_id()
        if check_user_id["exist"] == False:
            print("association does not exist")
        else:
            CreateAssociation(item.email, item.username_association, item.secret).verify_email(check_user_id['user_id_keycloak'])
            print("The email has been successfully sent!")
            return {"message" : "The association has been successfully created!"}
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")
        
    


@app.post("/resend-email", tags = ["Ponovo posalji email verifikaciju"])
async def resend_email(item : Item_for_resend):
    check_user_id_for_resend = Resend_verify_email(item.username).resend(item.username)
    print(check_user_id_for_resend)
    if check_user_id_for_resend['exist'] == False:
        raise HTTPException(status_code = 404, detail = "username does not exist")
    else:
        Resend_verify_email(item.username).send(check_user_id_for_resend['user_id_keycloak'])
        return {"message" : "The email has been successfully sent!"}

@app.get("/health", tags = ["Provera rada aplikacije"])
async def index():
    return {"HEALTH" : "OK"}

@app.post("/register-user", tags = ["Registracija"])
async def register_user(item:Item):
    checkerica = CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).checker()
    
    if checkerica['exist'] == False:
        CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).new_user()
        check_user_id = CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).get_keycloak_user_id()
        if check_user_id["exist"] == False:
            print("user does not exist")
        else:
            CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).verify_email(check_user_id["user_id_keycloak"])
            print("The email has been successfully sent!")
        return {"message" : "The user has been successfully created!"}
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")