""" Klase koje se upotrebljavaju za registrovanje korisnika.

Admin_conn omogucava konektovanje ka Keycloak API.
CreateUser kreiranje korisnika
"""

__all__ = ["CreateUser", "CreateUserUserService"]   # limitiranje sta ce moci da se pozove kao import "javne" klase
__version__ = "1.6"  # verzija modula
__author__ = "Milos Zlatkovic"  # autor modula/klase

#block import
from typing import Dict, Tuple
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os
from is_email import Is_email_valid
import requests

class Admin_conn:
    """
    Klasa koja konektuje na Keycloak admin panel.

    Argumente vuce iz Docker variabli za konekciju.
    """
    def __init__(self):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                    username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                    password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                    realm_name = "master",
                                    verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        
        return keycloak_admin

class CreateUser(Admin_conn):
    """
    Klasa za kreiranje korisnika sadrzi metode.

    Parametri:
    ---------------
        email : str

        username : str

        firstName : str

        lastName : str

        secret : str

            : -> Uzima user input.

    Variable:
    ---------------
        email : str

        username : str

        firstName : str

        lastName : str

        secret : str

            : -> Cuvanje user inputa i slanje na Keycloak.

    Rezultat:
    ---------------
        : -> New User
    """
    def __init__(self, email:str, username:str, firstName:str, lastName:str, secret:str):
        self.email = email
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.secret = secret
        self.admin = Admin_conn.__init__(self)

    def assign_keycloak_roles(self):
        client_id = self.admin.get_client_id(os.getenv('KEYCLOAK_CLIENT_NAME'))
        user_id = self.admin.get_user_id(self.username)
        role_id = self.admin.get_client_role_id(client_id=client_id, role_name="user_role")
        self.admin.assign_client_role(user_id, client_id,[{'id' : role_id, 'name':'user_role'}])

    def get_keycloak_user_id(self):
        user_id_keycloak = self.admin.get_user_id(self.username)
        if user_id_keycloak == None:
            return {"exist" : False}
        else:
            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def verify_email(self, user_id_keycloak):
        self.admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        self.admin.send_verify_email(user_id=user_id_keycloak)
        
    def checker(self):
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )
        users = self.admin.get_users()
        emails = []
        list_users = []

        for x in users:
            emails.append(x["email"])
            list_users.append(x["username"])

        if self.email in emails or self.username in list_users:
            return {"exist" : True}
        else:
            return {"exist" : False}

    def new_user(self):
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )
        email_check = Is_email_valid(self.email).check()
        if email_check['exist'] == True:
            self.admin.create_user({"email": self.email,
                        "username": self.username,
                        "enabled": "True",
                        "firstName": self.firstName,
                        "lastName": self.lastName,
                        "credentials": [
                            {
                                "value": self.secret,
                                "type": "password"
                            }
                        ]
                        })
        else:
            return {"exist" : False}
    
class CreateUserUserService():
    def __init__(self, email, username, firstName, lastName, about_me, city, age, terms_and_condition_accepted):
        self.email = email
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.about_me = about_me
        self.city = city
        self.age = age
        self.terms_and_condition_accepted = terms_and_condition_accepted

    def create_user(self):
        url = '{0}/insert-user'.format(os.getenv('USER_SERVICE_URL'))
        data = {"email" : self.email,"name" : self.firstName,"surname" : self.lastName,"about_me" : self.about_me,"city" : self.city,"age" : self.age,"terms_and_condition_accepted" : self.terms_and_condition_accepted}
        requests.post(url, json = data)
