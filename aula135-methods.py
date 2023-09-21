# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Conection:
    def __init__(self, host='Localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        #setter
        self.user = user
        
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        return connection

#c1 = Conection()
c1 = Conection.create_with_auth('Rafael', 143)
#c1.set_user('Rafael')
#c1.set_password('AAAAAA')

print(c1.user)
print(c1.password)
