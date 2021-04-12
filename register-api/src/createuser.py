from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin

# Configure client

class CreateUser():
    def __init__(self, email, username, enabled, firstName, lastName):
        self.email = email
        self.username = username
        self.enabled = enabled
        self.firstName = firstName
        self.lastName = lastName

    def new_user(self):
        KeycloakOpenID(server_url="http://nginx/auth/",
                        client_id="app",
                        realm_name="udomiljubimcadev",
                        client_secret_key="")

        keycloak_admin = KeycloakAdmin(server_url="http://nginx/auth/",
                                username='admin',
                                password='',
                                realm_name="master",
                                verify=True)
        keycloak_admin.realm_name = "udomiljubimcadev"

        keycloak_admin.create_user({"email": self.email,
                    "username": self.username,
                    "enabled": self.enabled,
                    "firstName": self.firstName,
                    "lastName": self.lastName,
                    # "credentials": [
                    #     {
                    #         "value": "secret",
                    #         "type": "password"
                    #     }
                    # ]
                    })
