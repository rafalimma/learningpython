import json
from aula132_a import CAMINHO_ARQUIVO, LojaCarros, fazendo_dump

fazendo_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    c1 = LojaCarros(**dados[0])
    c2 = LojaCarros(**dados[1])
    c3 = LojaCarros(**dados[2])
    
    print(c1.nome, c1.marca)
    print(c2.nome, c2.marca)
    print(c3.nome, c3.marca)
