class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "som gerado"
    
# cachorro e gato herdam de animal
class Cachorro(Animal):
    def falar(self):
        return "au au!"
    
class Gato(Animal):
    def falar():
        return "miau miau"
    
animal = Cachorro("cachorro")
print(animal.nome)
print(animal.falar())
    