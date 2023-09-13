# Escopo da classe e de métodos da classe

class Animal:

    def __init__(self, nome):
        self.nome = nome

        var = 'valor'
        print(var)
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
        #qualquer método que tiver o self vai ter acesso a tudo da classe

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('zebra'))