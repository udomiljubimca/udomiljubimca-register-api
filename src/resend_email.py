""" 
Klase koje se upotrebljavaju za slanje email verifikacije ako nije stigla prvi put.
"""

__all__ = ["Resend_verify_email"]
__version__ = "1.1"
__author__ = "Milos Zlatkovic"

from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os


class Resend_verify_email():
    """
    Klasa za kreiranje udruzenja sadrzi metode.

    Parametri:
    ---------------

        username : str

            : -> Uzima user input.

    Variable:
    ---------------

        username : str

            : -> Cuvanje user inputa i slanje na Keycloak.

    Rezultat:
    ---------------
        : -> Resend email
    """
    def __init__(self, username):
        self.username = username

    def resend(self, username):
        """
        Uzmi Keycloak user id.

        Parametri:
        ---------------

            user_id_keycloak -> username : None -> bool(False) - ako nema username

            user_id_keycloak -> username : bool(True), user_id - ima username
        """
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
        """ Ponovo posalji email verifikaciju.

        user_id_keycloak -> send_verify_email
        
        send_verify_email : realm_name -> izvrsna komanda slanje verifikacije
        """
        keycloak_admin = KeycloakAdmin(server_url="{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                                username = os.getenv('KEYCLOAK_ADMIN_USER'),
                                password = os.getenv('KEYCLOAK_ADMIN_PASSWORD'),
                                realm_name = "master",
                                verify = True)
        keycloak_admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        # user_id_keycloak dobijamo iz prethodne funkcije koju saljemo iz main fajla
        keycloak_admin.send_verify_email(user_id=user_id_keycloak)