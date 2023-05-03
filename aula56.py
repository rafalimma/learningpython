"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('joao')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada)) #vira uma tupla

for item in lista_enumerada:
    print(item) #esta inumerando
#o enumerate cria uma tupla para enumerara a lista:
#(0, 'Maria') para colocar o indice e o valor

#se eu tirar a variável "lista_enumerada" e usar o enumerate
# na lista "for item in enumerate(lista)" eu posso ter quantos
# for eu quiser por ele sempre vai ter uma nova enumeração
# para consumir.for tupla_enumerada in enumerate(lista):


for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])




