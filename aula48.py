"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2] #depois de deletar o item da lista, o python reassume o proximo
#valor para o indice 2
#print(lista)
#print(lista[2])
lista.append(50)#adiciona ao final da lista
lista.append(60)
lista.pop(0) #remove o ultimo valor no momento, ou o índice
lista.append(70)
print(lista)
