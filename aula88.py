# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',

}
'''
(a1, a2), (b1, b2)= pessoa.items() #retorna os valores das chaves no desempacotamento
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
'''

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
print(pessoa, dados_pessoa)

pessoa_completa = {**pessoa, **dados_pessoa} #extração de valores
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostr0_args_nomeados(*args, **kwargs):
    print('não nomeados:', args)
    for chave, valor in kwargs.items():#porque precisa retornar chave e valor
        print(chave, valor)


#mostr0_args_nomeados(nome = 'Joana', qlq=123)
#mostr0_args_nomeados(**pessoa_completa)#vai desempacotar o q esta
#na função no dicionário.

configurações = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostr0_args_nomeados(**configurações)
