# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome':'Rafa',
    'sobrenome':'Lima',
    'idade':'17'
    #'altura': 2
}

pessoa.setdefault('altura', None) #se não tiver a chave ele usa um valor padrão
print(pessoa['altura'])
print(len(pessoa)) # retorna o número de chaves
print(pessoa.keys()) # retorna as chaves
print(list(pessoa.keys())) # podem ser covertidos pra listas e tuples
print(pessoa.values()) # retorna só os valores
print(list(pessoa.items())) # retorna chave e valor
for chave, valor in pessoa.items():
    print(chave, valor)





