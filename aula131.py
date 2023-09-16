#__dict__ e vars para atributos da instância

class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_nascimanto(self):
        return Pessoa.ano_atual- self.idade
    
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

'''
p1.nome = 'wewdsd'
p1.__dict__['ele'] = 'Rafa'
print(p1.__dict__) #contem os valores da instância
print(vars(p1))
'''
#print(p1.ele)

print(vars(p1))