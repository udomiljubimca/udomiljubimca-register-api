from keycloak.keycloak_admin import KeycloakAdmin, KeycloakOpenID
import os

# KYECLOAK_ADMIN_PASSWORD = os.getenv("KYECLOAK_ADMIN_PASSWORD")
# KYECLOAK_ADMIN_USER = os.getenv("KYECLOAK_ADMIN_USER")
# print(KYECLOAK_ADMIN_U, KYECLOAK_ADMIN_PA)

#try to getenv from docker env with pass,username

class Make(): #main class
    def __init__(self, email, username, enabled, firstName, lastName, realmRoles, attributes, values):  #private 
        self.email = email
        self.username = username
        self.enabled = enabled
        self.firstName = firstName
        self.lastName = lastName
        self.realmRoles = realmRoles
        self.attributes = attributes
        self.values = values

    def pass_args(self):
        keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="app",
                    realm_name="Clients",
                    client_secret_key="4f780e9b-4bc8-4302-bb84-1eda64d9acc0",
                    verify=True)

        keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                                    username="admin",
                                    password="",
                                    realm_name="master",
                                    verify=True)
        keycloak_admin.realm_name = "Clients"

     
        new_user = keycloak_admin.create_user({"email": self.email,
                            "username": self.username,
                            "enabled": self.enabled,
                            "firstName": self.firstName,
                            "lastName": self.lastName,
                            "realmRoles": [self.realmRoles, ],
                            "attributes": {self.attributes: self.values}})
                            
        print(self.email,self.username ,self.enabled ,self.firstName, self.lastName,self.realmRoles,self.attributes,self.values )
        


# Make("my.email@.gmail.com","ljudina","True","novak","djokovic","user_default","exemple","1,2,3,3,").pass_args()


#Create("my.email@.gmail.com","ljudina","True","novak","djokovic","user_default","exemple","1,2,3,3,")
#pass args "my.email@.gmail.com","ljudina","True","novak","djokovic","user_default","exemple","1,2,3,3,"



# keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
#                     client_id="app",
#                     realm_name="Clients",
#                     client_secret_key="Pa565w0rd",
#                     verify=True)


# keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
#                                username='admin',
#                                password='Pa565w0rd',
#                                realm_name="master",
#                                verify=True)
# keycloak_admin.realm_name = "Clients"

# new_user = keycloak_admin.create_user({"email": "example@example.com",
#                     "username": "example@example.com",
#                     "enabled": True,
#                     "firstName": "Example",
#                     "lastName": "Example",
#                     "realmRoles": ["user_default", ],
#                     "attributes": {"example": "1,2,3,3,"}})