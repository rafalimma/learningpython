# atributos de classe

class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_nascimanto(self):
        return Pessoa.ano_atual- self.idade
    
p1 = Pessoa('jõao', 23)
p2 = Pessoa('Mari', 20)
print(Pessoa.ano_atual)
print(p1.get_nascimanto())
print(p2.get_nascimanto())

