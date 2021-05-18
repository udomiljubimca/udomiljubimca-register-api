from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os


class Resend_verify_email():
    def __init__(self, username):
        self.username = username

    def resend(self, username):
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

    def send(self, user_id_keycloak):
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        keycloak_admin.send_verify_email(user_id=user_id_keycloak)