# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome

class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome

golf = Carro('Golf')

volkswagen = Fabricante('Volksvagen')
golf.fabricante = volkswagen
motor_G8 = Motor('motor_G8')
golf.motor = motor_G8

print(golf.nome, golf.fabricante.nome, golf.motor.nome)

boxer = Carro('boxer')

porche = Fabricante('porche')
boxer.fabricante = porche
motor_G8 = Motor('motor_G8')
boxer.motor = motor_G8

print(boxer.nome, boxer.fabricante.nome, boxer.motor.nome)
