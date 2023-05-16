# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome':'Rafa',
    'sobrenome':'Lima',
    'idade':'17'
}

#print(p1.get('nome', 'Não existe'))

#pop
'''
nome = p1.pop('nome') # retorna o valor de nome e exclui a chave do dic
print(nome)
print(p1)
'''
#popitem
'''
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1) # remove a ultima chave do dicionário
'''

#update

p1.update({
    'nome': 'novo valor'
})

print(50 * '*')

p1.update(nome='raff', idade=33)
print(p1)

print(50 * '*')

tupla = ('nome', 'novo valor'), ('idade', 30)
p1.update(tupla)
print(p1)




