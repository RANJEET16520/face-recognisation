class user():
    def __init__(self,user_name):
        self.user_name = user_name
        self.first_name = ""
        self.last_name = ""
        self.password = "hell"

    def return_dict(self):
        result = {
                "user_name":self.user_name,
                "first_name":self.first_name,
                "last_name":self.last_name,
                "password":self.password
        }

    def generate_id():
        return 0
