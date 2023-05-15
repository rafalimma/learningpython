# Manipulando chaves e valores em dicionários
'''
pessoal = {
    'nome':'Rafa',
    'sobrenome':'Lima',
    'endereços': [
        {'rua': 'dada', 'numero': 33},
        {'rua': 'dadyy', 'numero': 67},
    ]

}
'''
pessoa = {}

##
chave = 'nome'

pessoa['nome'] = 'Rafa'
pessoa['sobrenome'] = 'Lima'
print(pessoa)
print(pessoa['nome'])
del pessoa['nome']

print(pessoa)

print(pessoa.get('idade'))
