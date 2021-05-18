from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os
from is_email import Is_email_valid

class CreateUser():
    def __init__(self, email, username, firstName, lastName, secret):
        self.email = email
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.secret = secret

    def assign_keycloak_roles(self):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        client_id = keycloak_admin.get_client_id(os.getenv('KEYCLOAK_CLIENT_NAME'))
        user_id = keycloak_admin.get_user_id(self.username)
        role_id = keycloak_admin.get_client_role_id(client_id=client_id, role_name="user_role")
        keycloak_admin.assign_client_role(user_id, client_id,[{'id' : role_id, 'name':'user_role'}])
        
    def get_keycloak_user_id(self):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        user_id_keycloak = keycloak_admin.get_user_id(self.username)
        if user_id_keycloak == None:
            return {"exist" : False}
        else:
            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def verify_email(self, user_id_keycloak):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
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
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        users = keycloak_admin.get_users()
        emails = []
        list_users = []

        for x in users:
            emails.append(x["email"])
            list_users.append(x["username"])

        if self.email in emails or self.username in list_users:
            return {"exist": True}
        else:
            return {"exist": False}

    def new_user(self):
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        email_check = Is_email_valid(self.email).check()
        

        if email_check['exist'] == True:
            keycloak_admin.create_user({"email": self.email,
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
            return {"is_email" : False}