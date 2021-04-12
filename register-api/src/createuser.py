from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os
# Configure client

class CreateUser():
    def __init__(self, email, username, enabled, firstName, lastName, secret):
        self.email = email
        self.username = username
        self.enabled = enabled
        self.firstName = firstName
        self.lastName = lastName
        self.secret = secret

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
