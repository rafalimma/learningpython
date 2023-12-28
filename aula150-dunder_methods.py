# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y, z="String") -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})' #representação de string do obj
    
    def __repr__(self):
        class_name = type(self).__name__ #ou:
        class_name = self.__class__.__name__ 
        return f'{class_name}(x={self.x!r},y={self.y!r}, z={self.z!r})'

p1 = Ponto(1,2)
p2 = Ponto(2,5)
print((p1)) #str
print(repr(p2)) #repr


class AstonMartin:
    def __init__(self, motor, cor, ano) -> None:
        self.motor = motor
        self.cor = cor
        self.ano = ano
        self.preco = float
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(motor={self.motor}, cor={self.cor}, preco={self.preco!r})'

carro = AstonMartin(1, 2, 3)
print(carro)

