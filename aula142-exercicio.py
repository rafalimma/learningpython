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
        return self._motor # significa
        #que quando você acessar o atributo motor de um objeto Carro,
        #o método motor será chamado automaticamente para obter o valor do atributo _motor.
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

carro1 = Carro("Fastback")
carro1.motor = '1.0'
carro1.fabricante = 'Fiat'
print(carro1.nome)
print(carro1.motor)
print(carro1.fabricante)
