""" Klase koje se upotrebljavaju za registrovanje udruzenja.

Admin_conn omogucava konektovanje ka Keycloak API.
CreateAssociation kreiranje udruzenja
"""

__all__ = ["CreateAssociation"]   # limitiranje sta ce moci da se pozove kao import "javne" klase
__version__ = "1.5"  # verzija modula
__author__ = "Milos Zlatkovic"  # autor modula/klase

#block import
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os
from is_email import Is_email_valid

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

class CreateAssociation(Admin_conn):
    """
    Klasa za kreiranje udruzenja sadrzi metode.

    Parametri:
    ---------------
        email : str

        username : str

        secret : str

            : -> Uzima user input.

    Variable:
    ---------------
        email : str

        username : str

        secret : str

            : -> Cuvanje user inputa i slanje na Keycloak.

    Rezultat:
    ---------------
        : -> New Association
    """
    def __init__(self, email, username, secret):
        self.email = email
        self.username = username
        self.secret = secret
        self.admin = Admin_conn.__init__(self) # deklarisanje konekcije 

    def assign_keycloak_roles(self):
        """
        Dodaj role udruzenju.

        Parametri:
        ---------------
            client_id -> Vuce iz docker variable

            user_id -> Argument username : dobija iz variable username

            role_id -> Argumenti : (client_id, role_name : str -> role iz Keycloak panela)

            assign_client_role : Podaci se nalaze u variabli -> Izvrsna komanda daje role udruzenju
        """
        client_id = self.admin.get_client_id(os.getenv('KEYCLOAK_CLIENT_NAME'))
        user_id = self.admin.get_user_id(self.username)
        role_id = self.admin.get_client_role_id(client_id=client_id, role_name="association_role")
        # assign_client_role zahteva user_id(korisnikov id), client_id(Keycloak panel), id je role_id i ime role je user_role
        self.admin.assign_client_role(user_id, client_id,[{'id' : role_id, 'name':'association_role'}])

    def get_keycloak_user_id(self):
        """
        Uzmi Keycloak user id.

        Parametri:
        ---------------

            user_id_keycloak -> username : None -> bool(False) - ako nema username

            user_id_keycloak -> username : bool(True), user_id - ima username
        """
        # user_id_keycloak koristimo za proveru da li je id postojeci korisnik takodje koristimo za verify_email 
        user_id_keycloak = self.admin.get_user_id(self.username)
        if user_id_keycloak == None:
            return {"exist" : False}
        else:
            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def verify_email(self, user_id_keycloak:str):
        """
        Slanje email verifikacije.

        Parametri:
        ---------------

            realm_name -> Docker variabla

            user_id_keycloak -> provera da li user postoji

            send_verify_email : realm_name -> izvrsna komanda slanje verifikacije
        """
        self.admin.realm_name = os.getenv('CLIENT_RELM_NAME')
        # user_id_keycloak dobijamo iz prethodne funkcije koju saljemo iz main fajla
        self.admin.send_verify_email(user_id=user_id_keycloak)
        
    def checker(self):
        """
        Provera da li je username ili email vec registrovan u Keycloak-u.

        Parametri:
        ---------------
            users -> Uzima listu svih usera sa Keycloak-a.

            list_users -> list : proverava listu username-a

            emails -> list : proverava listu email-a 
        """
        #  KeycloakOpenID radi sa generalnim stvarima kao sto su(token, policies, permissions..) a KeycloakAdmin sa korisnicima
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )

        self.admin.realm_name = os.getenv('CLIENT_RELM_NAME')

        users = self.admin.get_users()
        emails = []
        list_users = []

        for x in users:
            """ Provera email-a i username-a.

                Dodajemo u listu i pravimo proveru da li postoji neko udruzenje sa istim email ili username\
                    jer su ove informacije jedinstvene na nivou svih korisnika.
            """
            emails.append(x["email"])
            list_users.append(x["username"])

        if self.email in emails or self.username in list_users:
            return {"exist" : True}
        else:
            return {"exist" : False}

    def new_association(self):
        """
        Kreira udruzenje na Keycloak-u.

        Parametri:
        ---------------
            email : str

            username : str

            secret : str

                : -> dict
        Rezultat:
        ---------------
            : -> New Association
        """
        KeycloakOpenID(server_url = "{}/auth/".format(os.getenv('KEYCLOAK_URL')),
                        client_id = os.getenv('KEYCLOAK_CLIENT_NAME'),
                        realm_name = os.getenv('CLIENT_RELM_NAME'),
                        client_secret_key = os.getenv('CLIENT_RELM_SECRET')
                        )
      
        email_check = Is_email_valid(self.email).check()

        if email_check['exist'] == True:
             # Kreiranje udruzenja zahteva dict za slanje informacija o udruzenju i zatim kreira jedno sa poslatim informacijama
            self.admin.create_user({"email": self.email,
                        "username": self.username,
                        "enabled": "True",
                        "firstName": "Test",
                        "lastName": "Test",
                        "credentials": [
                            {
                                "value": self.secret,
                                "type": "password"
                            }
                        ]
                        })
        else:
            return {"exist" : False}
