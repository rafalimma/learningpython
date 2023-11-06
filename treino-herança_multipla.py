'''
Um exercício envolvendo herança múltipla pode ser criar um sistema simples de herança múltipla
para modelar uma entidade "Animal" que possui características de "Mamífero" e "Ave".
Vamos criar três classes: Animal, Mamifero, e Ave.
'''

class Animal:
    def __init__(self, nome, comida, som) -> None:
        self.nome = nome
        self.comida = comida
        self.som = som

    def emitir_som(self):
        print(f'{self.nome} --> {self.som}')
    def comer(self):
        print(f'{self.nome} está comendo {self.comida}')

class Mamifero(Animal):
    def __init__(self, nome, comida, som, tam) -> None:
        super().__init__(nome, comida, som)
        self.tam = tam
    def tam_mami(self):
        print(f'O tamanho do mamífero é {self.tam}')
class Ave(Animal):
    def __init__(self, nome, comida, som, tam) -> None:
        super().__init__(nome, comida, som)
        self.tam = tam