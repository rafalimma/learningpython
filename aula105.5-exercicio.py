import copy
from produtos_package import produtos



# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = [       #usou o round p/ definir 2 casas após a vírgula
    {**p, 'preco': round(p['preco'] * 1.1, 2)} #criou e expandiu um novo dicionário
    for p in copy.deepcopy(produtos) #estou trocando os valores copiados da lista por valores novos
]

ordenados = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
ordenados_p = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)
print(*produtos, sep='\n')
print()
print(*ordenados, sep='\n')
'''
for indice in produtos:
    novo_prod = (indice['preco'] * 10)/100
    indice['preco'] = indice['preco'] + novo_prod
    print (indice['nome'], indice['preco'])
'''

