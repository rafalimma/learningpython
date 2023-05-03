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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) #extend retorna um valor -> None
#ou seja ele faz uma ação mas não entrega nada, ele mexe diretamente na
#lista a então não se pode atribuir ele a uma variável (vai resultar none)
print(lista_a)
