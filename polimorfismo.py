class Veiculo:
    def __init__(self, nome):
        self.nome = nome
    
    def movimentar(self):
        print(f"movimentando {self.nome} ...")

class Carro(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
    
class Bicicleta(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
    
    def movimentar(self):
        return super().movimentar()
