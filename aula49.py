'''
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
'''




lista = [10, 20, 30, 40]

lista.append('Rafa')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear() #tira tudo da lista
lista.insert(0, 33)
print(nome)
print(lista)