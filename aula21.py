'''
operadores lógicos
and (e)
or (ou)
not (não)
'''
'''
or - qualquer condição verdadeira avalia tuda a expressão como verdadeira
Se qualquer valor for considerado verdadeiro a expressão inteira
será avaliada naquele valor. Considerados falsy: 0 0.0 '' False
none: valor nulo
'''
entrada = input('(E)entrar (S)sair')
senha_digitada = input('senha:')

senha_permitida = '12345'
#pode-se usar o or para fazer com que ele avalie uma possibilidade diferente, para permitir mais de uma coisa

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('entrouu')
else:
    print('sair')
    #avaliação de curto circuito:
senha = input('Senha: ') or 'Sem senha'
print(senha)