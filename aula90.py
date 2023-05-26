import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)


#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },

]
'''
novos_produtos = [
    {**produto, 'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
'''
#print(novos_produtos)
#print(*novos_produtos, sep='\n')
#p(novos_produtos)

#lista = [n for n in range() if n < 5]
#print(lista)
# a esquerda do for é mapeamento, a direita é filtro
# no filtro vc pode ou não incluir o elemento a lista
novos_produtos = [
    {**produto, 'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] * 1.05 > 10
]

p(novos_produtos)

#for dentro de for em list comprehension
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y) #vai ser incluido na lista nova
    for x in range(3)
    for y in range(3)

]

lista = [
    [(x, letra) for letra in 'Rafaf']
    for x in range(3) #para cada x se tem uma letra

]        
print(lista)