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


class Leilao:
    def __init__(self, local, leiloeiro, lance_minimo):
        self.local = local
        self.leiloeiro = leiloeiro,
        self.lance_minimo = lance_minimo
        self.lances_recebidos = []
    
    def receber_lances(self, valor):
        if valor >= self.lance_minimo:
            self.lances_recebidos.append(valor)
            print('lance adicionado')
        else:
            print(f"lance {valor} Muito baixo")

    def resumo(self):
        maior_lance = max(self.lances_recebidos)
        print(f"Máximo lance recebido {maior_lance}")
        



leilao = Leilao('santa felicidade', 'kron', 100000)

lance = leilao.receber_lances(290000)
maior_lance = leilao.resumo()