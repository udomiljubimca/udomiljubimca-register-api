class LimitPassword():
    def __init__(self, password):
        self.password = password
    def is_password_valid(self):
        min = 8
        max = 12
        if len(self.password) >= min and len(self.password) <= max:
            return {"status": True}
        else:
            return {"status": False}

class LimitUsername():
    def __init__(self, username):
        self.username = username
    def is_username_valid(self):
        min = 5
        max = 20
        if len(self.username) >= min and len(self.username) <= max:
            return {"status": True}
        else:
            return {"status": False}