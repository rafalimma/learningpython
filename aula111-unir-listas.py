# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    intervalo_max = min(len(lista1), len(lista2)) #menor lista tem 3 valores
    return [(lista1[i],lista2[i]) for i in range(intervalo_max)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

#ou
print(list(zip(l1, l2)))
#ou 
from itertools import zip_longest

print(list(zip_longest(l1, l2)))




'''
def dec(func):
    def lista_maior(*args, **kwargs):
        for arg in args:
            print(arg)
            adicionador(arg)
        result = func(*args, **kwargs)
        return result
    return lista_maior



def adicionador(param):
    for i in estados:
        indice = f'{i}, {param}'
        cidades_estado.append(indice)
        continue



@dec
def lista_menor(a):
    print(cidades_estado)


estados = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
cidades_estado = []

res = lista_menor(cidades)
print(res)
'''