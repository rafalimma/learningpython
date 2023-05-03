"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices
inexistentes na lista
"""
import os
lista = []
while True:
    ac = input("Selecione uma opção: [l]istar, [i]nserir, [a]pagar: ")
    if ac == "i":
        os.system("cls")
        novo_v = input("O que deseja inserir na lista: ")
        lista.append(novo_v)
    elif ac == "l":
        os.system('cls')
        if len(lista) == 0:
            print("Não ha nada para listar.")
        for i, valor in enumerate(lista):
            print(i, valor) #para cada i e para cada valor que
            #eu coloquei na lista enumerada(numera cada valor da lista)
            #print o valor e o indice que a lista enumerada criou

    elif ac == "a":
        os.system('cls')
        indice_str = input('Qual indice você deseja apagar? ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('digite corretamente um valor.')
        except IndexError:
            print("Este valor não existe na lista.")
    else:
         print("escolha um valor (inserir, apagar ou listar)")


