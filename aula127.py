#métodos em instâncias de classes Python
#Hard coded - É algo que foi escrito diretamnete no código
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self): #método - self é a instancia do método
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()

# o self é pra trazer os dados da classe