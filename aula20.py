'''
operadores lógicos
and (e)
or (ou)
not (não)
'''
'''
and - todas as condições precisam ser verdadeiras 
se qualquer valor da expressão for avaliado falso, a expressão inteira será avaliada naquele valor
0 0.0 "" False (falsy)
também existe o 'none' que para representar um não valor
'''

entrada = input('(E)entrar (S)sair')
senha_digitada = input('senha:')

senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrouu')
else:
    print('sair')
#avaiação de curto circuito:
print(True and False and True)

