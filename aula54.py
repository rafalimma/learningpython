'''
introdução ao desempacotamento + tuples (tuplas)
'''

nomes = ['Maria', 'Helena', 'Luiz']
#quero criar variáveis, tirando cada valor da lista

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']
#a viriavel rsto chama o resto dos valores
# o "_" antes do valor que você quer ignora o ou os valores anteriores

print(nome3, _)