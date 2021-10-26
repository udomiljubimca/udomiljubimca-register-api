""" 
Klase koje se upotrebljavaju za proveru validnosti email.
"""

__all__ = ["Is_email_valid"]
__version__ = "1.1"
__author__ = "Milos Zlatkovic"
#block imports
import re

class Is_email_valid():
    """ Provera za email.

    Parametri:
    ---------------
        email : str
    """
    def __init__(self, email):
        self.email = email

    def check(self):
        """Proveravamo specijalne simbole.

            Ako jeste email vracamo True.
        """
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if (re.search(regex, self.email)):
            return {"exist" : True}
        else:
            return {"exist" : False}

