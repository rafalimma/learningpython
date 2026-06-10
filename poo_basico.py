'''
A class é a planta (o blueprint). Ela define o que o objeto terá.
O método __init__ é o construtor. Ele é chamado automaticamente toda vez que você cria um novo objeto a partir daquela classe.
'''
# self refere-se ao proprio objeto que esta sendo criado

class Produto:
    def __init__(self, nome, preco_inicial):
        self.nome = nome,
        self.preco_atual = preco_inicial
        self.ativo = True
    # metodo comportameto do objeto
    def dar_lances(self, valor):
        self.preco_atual += valor
        print(f"novo lance em {self.nome} R$ {self.preco_atual}")

p1 = Produto("Latinha", 10)
p2 = Produto("Giz", 7)

p1.dar_lances(200)

'''
🛠️ Exercício de Hoje: O Sistema de Leiloeiro
Vamos criar uma classe que gerencia um Leilão.
'''