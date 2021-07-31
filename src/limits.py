class LimitPassword():
    def __init__(self, password):
        self.password = password
    def is_password_valid(self):
        min = 8
        max = 12
        if len(password) >= min and len(password) <= max:
            return {"status": True}
        else:
            return {"status": False}

class LimitUsername():
    def __init__(self, username):
        self.username = username
    def is_username_valid(self):
        min = 5
        max = 20
        if len(username) >= min and len(username) <= max:
            return {"status": True}
        else:
            return {"status": False}