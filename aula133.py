# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 #atributo da classe

    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_classe(cls):
        print('Hey')
            
    @classmethod
    def criar_com_50anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_anonimo(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50anos('Rafael')
p3 = Pessoa('Anonimo', 24)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


#print(Pessoa.ano)
#Pessoa.metodo_classe()