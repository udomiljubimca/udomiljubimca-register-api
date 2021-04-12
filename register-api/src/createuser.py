from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

from fastapi import HTTPException

class CreateUser():
    def __init__(self, email, username, enabled, firstName, lastName, secret):
        self.email = email
        self.username = username
        self.enabled = enabled
        self.firstName = firstName
        self.lastName = lastName
        self.secret = secret
    def checker(self):
        KeycloakOpenID(server_url = "http://nginx/auth/",
                        client_id = "app",
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        keycloak_admin = KeycloakAdmin(server_url="http://nginx/auth/",
                                username = os.getenv('KYECLOAK_ADMIN_USER'),
                                password = os.getenv('KYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        users = keycloak_admin.get_users()
        emails = []
        for email in users:
            emails.append(email["email"])

        if self.email in emails:
            return {"exist": True}
        else:
            return {"exist": False}

    def new_user(self):
        KeycloakOpenID(server_url = "http://nginx/auth/",
                        client_id = "app",
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        keycloak_admin = KeycloakAdmin(server_url="http://nginx/auth/",
                                username = os.getenv('KYECLOAK_ADMIN_USER'),
                                password = os.getenv('KYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        keycloak_admin.create_user({"email": self.email,
                    "username": self.username,
                    "enabled": self.enabled,
                    "firstName": self.firstName,
                    "lastName": self.lastName,
                    "credentials": [
                        {
                            "value": self.secret,
                            "type": "password"
                        }
                    ]
                    })
        # else:
        #     return HTTPException(status_code=403, detail="User alredy exist!")
