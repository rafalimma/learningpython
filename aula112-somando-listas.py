"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
def soma(la, lb):
    intervalo_min = min(len(la), len(lb))
    return[
        la[i] + lb[i] for i in range(intervalo_min) #estou puxando o indice de cada um e fazendo
        #uma operação com eles 'la[i]'
    ]

lista_a  = [1, 2, 3, 4, 5, 6, 7]
lista_b  = [1, 2, 3, 4]

result = soma(lista_a, lista_b)
print(result)

# outra forma:
print('outra forma')
print()

lista_soma = []

for i in range(len(lista_b)): #ou enumerate
    lista_soma.append(lista_b[i] + lista_a[i])

print(lista_soma)

# outra forma:
print('outra forma')
print()

lista_soma2 = [
    x + y for x, y in zip(lista_a, lista_b) 
]# no x, y eu estou desempacotando os indices das listas
print(lista_soma2)
