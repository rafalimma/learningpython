import copy
'''
Python que envolve o uso das funções deepcopy e funções lambda.
Neste exercício,
vamos criar uma cópia profunda de uma lista
de dicionários e depois usar uma função lambda para modificar os valores de um campo específico em cada dicionário.
'''

pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 22}
]

pessoas_copy = copy.deepcopy(pessoas)

pessoas_modified = lambda pessoas, anos  : {"nome": pessoas['nome'], "idade": pessoas['idade']+ anos}
anos = 5
for i in pessoas_copy:
    print(f' Dicionários atualizados: {pessoas_modified(i, anos)}')
