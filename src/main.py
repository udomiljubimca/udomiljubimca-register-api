import logging
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
from createuser import CreateUser
from docs import register_api_docs
from resend_email import Resend_verify_email
from typing import Optional
from create_association import CreateAssociation
from is_email import Is_email_valid
import json
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI(openapi_tags = register_api_docs, openapi_prefix = "/api/latest/register-api")

class ItemUser(BaseModel):
    email : str
    username : str
    firstName : str
    lastName : str
    secret: str
    @validator("email")
    def email_must_be_lowercase(cls, v):
        return v.lower()
    @validator("username")
    def username_must_be_lowercase(cls, v):
        return v.lower()

class ItemForResend(BaseModel):
    username : str
    @validator("username")
    def username_must_be_lowercase(cls, v):
        return v.lower()

class ItemAssociation(BaseModel):
    email : str
    username : str
    number_association : Optional[int] = None
    place : Optional[str] = None
    phone_number : Optional[int] = None
    web : Optional[str] = None
    secret : str
    @validator("email")
    def email_must_be_lowercase(cls, v):
        return v.lower()
    @validator("username")
    def username_must_be_lowercase(cls, v):
        return v.lower()

@app.get("/health", tags = ["Provera rada aplikacije"])
async def index():
    return {"HEALTH" : "OK"}

@app.post("/register-user", tags = ["Registracija"])
async def register_user(item : ItemUser):
    checkerica = CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).checker()
    checkerica_email = Is_email_valid(item.email).check()
    if checkerica_email['exist'] == True and checkerica['exist'] == False:
        CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).new_user()
        check_user_id = CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).get_keycloak_user_id()
        CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).assign_keycloak_roles()
        CreateUser(item.email, item.username, item.firstName, item.lastName, item.secret).verify_email(check_user_id["user_id_keycloak"])
        
        return {"message" : "The user has been successfully created!"}
    elif checkerica_email['exist'] == False:
        raise HTTPException(status_code = 406, detail = "Email is not acceptable")
    elif checkerica['exist'] == True:
        raise HTTPException(status_code = 409, detail = "Username or email already exists")
    else:
        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/register-association", tags = ["Registracija udruzenja"])
async def register_association(item : ItemAssociation):
    checkerica = CreateAssociation(item.email, item.username, item.secret).checker()
    checkerica_email = Is_email_valid(item.email).check()
    if checkerica_email['exist'] == True and checkerica['exist'] == False:
        CreateAssociation(item.email, item.username, item.secret).new_association()
        check_association_id = CreateAssociation(item.email, item.username, item.secret).get_keycloak_user_id()
        CreateAssociation(item.email, item.username, item.secret).assign_keycloak_roles()
        CreateAssociation(item.email, item.username, item.secret).verify_email(check_association_id['user_id_keycloak'])
        return {"message" : "The association has been successfully created!"}
    elif checkerica_email['exist'] == False:
        raise HTTPException(status_code = 406, detail = "Email is not acceptable")
    elif checkerica['exist'] == True:
        raise HTTPException(status_code = 409, detail = "Association already exists")
    else:
        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/resend-email", tags = ["Ponovo posalji email verifikaciju"])
async def resend_email(item : ItemForResend):
    check_user_id_for_resend = Resend_verify_email(item.username).resend(item.username)
    if check_user_id_for_resend['exist'] == False:
        raise HTTPException(status_code = 404, detail = "username does not exist")
    else:
        Resend_verify_email(item.username).send(check_user_id_for_resend['user_id_keycloak'])
        return {"message" : "The email has been successfully sent!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")