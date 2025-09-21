# Crie uma classe Veiculo com atributos marca e ano. Depois, crie as subclasses Carro e Moto que
# herdem de Veiculo e adicionem um método específico (abrir_porta() para carro e empinar() para moto).

class Veiculo():
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def abrir_porta(self):
        return f'carro da {self.marca} esta abrindo a porta'
    
class Moto(Veiculo):
    def empinar(self):
        return f'moto do ano {self.ano} está empinando'
    
carro = Carro('chevrolet', '2010')
print(carro.abrir_porta())

moto = Moto('Ducatti', '2015')
print(moto.empinar())