class user:
    def __init__(self,id,email):
        self.id=id
        self.email=email
    @property
    def id(self):
        return self.id
    @property
    def email(self):
        return self.email
    @email.setter
    def email(self,email):
        self.email=email
    @id.setter
    def id(self,id):
        self.id=id

    @email.getter
    def email(self, email):
        return email

    @id.getter
    def id(self, id):
        return id