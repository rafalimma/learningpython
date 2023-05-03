'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = "     Olha só    ,que coisa    "
lista_palavras_crua = frase.split(', ')

lista_frases = []
for i, frase in enumerate(lista_palavras_crua):
    lista_frases.append(lista_palavras_crua[i].strip()) #cortar o espeço do começo
    # e no fim da string
print(lista_palavras_crua)
print(lista_frases)

frases_unidas = '.'.join('abc') #somente iteráveis
print(frases_unidas)
