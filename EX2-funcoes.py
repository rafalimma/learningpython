# Exercícios com funções no Python

'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

def soma_imposto(taxa, custo):
    impostofinal = taxa * custo
    return impostofinal


imposto_vendas = float(input('Qual é a porcentagem de imposto sobre vendas?'))
custo = int(input('Qual é o custo do produto?'))

print(soma_imposto(imposto_vendas, custo))