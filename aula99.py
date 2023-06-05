# Try, except, else e finally

try:
    print('abrir o arquvo')
    #8/0
except ZeroDivisionError:
    print('DIVIdiu 0')
else:
    print('not work')
finally:
    print('fechar arq') #finally sempre será executado

