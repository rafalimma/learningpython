# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe


class A: #herda de object
    def __new__(cls, y): #ou *args
        instancia = super().__new__(cls)
        print('Antes de criar a instancia')
        instancia.x = 123
        return instancia

    def __init__(self, y) -> None:
        self.y = y
        print("sou o init")
    
    def __repr__(self):
        return f"A()"
    
a = A(345)
#a = object.__new__(A)
#a.__init__()
print(a)
print(a.x)