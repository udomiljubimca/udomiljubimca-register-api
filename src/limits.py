""" 
Klase koje se upotrebljavaju za limitiranje.
"""

__all__ = ["LimitPassword", "LimitUsername"]
__version__ = "1.1"
__author__ = "Milos Zlatkovic"

class LimitPassword():
    """ Limitiranje password-a.

    Parametri:
    ---------------
        password : str

    Rezultat:
    ---------------
        password valid : -> True
    """
    def __init__(self, password):
        self.password = password
    def is_password_valid(self):
        """
        Password je limitiran na minimalno 8 i maksimalno 12 karaktera.
        """
        min = 8
        max = 12
        if len(self.password) >= min and len(self.password) <= max:
            return {"status": True}
        else:
            return {"status": False}

class LimitUsername():
    """ Limitiranje username-a.

    Parametri:
    ---------------
        username : str

    Rezultat:
    ---------------
        username valid : -> True
    """
    def __init__(self, username):
        self.username = username
    def is_username_valid(self):
        """
        Username je limitiran na minimalno 5 i maksimalno 20 karaktera.
        """
        min = 5
        max = 20
        if len(self.username) >= min and len(self.username) <= max:
            return {"status": True}
        else:
            return {"status": False}