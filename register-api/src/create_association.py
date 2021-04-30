from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os
  


class CreateAssociation():
    def __init__(self, email, username_association, secret):
        self.email = email
        self.username_association = username_association
        self.secret = secret
    def get_keycloak_user_id(self):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYECLOAK_ADMIN_USER'),
                                password = os.getenv('KEYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        user_id_keycloak = keycloak_admin.get_user_id(self.username_association)
        if user_id_keycloak == None:
            return {"exist" : False}
        else:
            #keycloak_admin.send_verify_email(user_id=user_id_keycloak)
            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}
    def verify_email(self, user_id_keycloak):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYECLOAK_ADMIN_USER'),
                                password = os.getenv('KEYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        keycloak_admin.send_verify_email(user_id=user_id_keycloak)
        
    def checker(self):
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYECLOAK_ADMIN_USER'),
                                password = os.getenv('KEYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        users = keycloak_admin.get_users()
        emails = []
        list_users = []

        for x in users:
            emails.append(x["email"])
            list_users.append(x["username"])

        if self.email in emails or self.username_association in list_users:
            return {"exist": True}
        else:
            return {"exist": False}


    def new_association(self):
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYECLOAK_ADMIN_USER'),
                                password = os.getenv('KEYECLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        keycloak_admin.create_user({"email": self.email,
                    "username": self.username_association,
                    "enabled": "True",
                    "credentials": [
                        {
                            "value": self.secret,
                            "type": "password"
                        }
                    ]
                    })
