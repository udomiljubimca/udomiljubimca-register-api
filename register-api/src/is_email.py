import re

class Is_email_valid():
    def __init__(self, email):
        self.email = email

    def check(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if (re.search(regex, self.email)):
            return {"exist" : True}
        else:
            return {"exist" : False}

