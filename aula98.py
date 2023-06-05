# Try, except, else e finally

a = 18
b = 0
#c = a / b # isso pode gerar um erro
try:
    print('l1'[10])
    c = a / b #tenta executar um código, e não pode viver sozinho
    #esse erro foi silenciado
    print('l2') # como ocorreu uma execao isso não é executado
except ZeroDivisionError:
    print('dividiu por 0')
except (NameError, IndexError) as error: #variável que recebe a instancia do erro:
    print('name ou index error')
    print('erro:', error.__class__.__name__)
except Exception:
    print('erro desconhecido')

print('ccc')