# dir, hasattr e getattr em Python
string = ('Raffa yyy')
metodo = 'strip'

if hasattr(string, metodo): #checa se o método existe dentro da variável
    print('existe upper aqui')
    print(getattr(string, metodo)()) #chama o método em string que esta em uma variável
else:
    print('Não existe o método', metodo)