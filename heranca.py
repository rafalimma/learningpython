# clase pai
# classe filha que herda da classe pai

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def alimentar(self):
        pass
    def emitirSom(self):
        pass
class Gato(Animal):
    def __init__(self, nome, ):
        super().__init__(nome)
    def comer(self):
        print('O gato está se alimentando.')
    def emitirSom(self):
        print('Miau')
        return super().emitirSom()

gato = Gato("robson")

# Composição

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    def ligar(self):
        print('motor ligado')
    def desligado(self):
        print('motor deligado')

class Carro:
    def __init__(self, marca, modelo, tipo_motor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)

    def ligar(self):
        print('carro ligado')
        self.motor.ligar()
    
    def desligar(self):
        print('Carro desligado')
        self.motor.desligado()

carro = Carro('Fiat', 'Uno', 'fire')
carro.ligar()
        