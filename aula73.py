"""
Higher order functions
funcoes de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', "dada")
print(v)

##################|
                 #|
def rafa(x, y):  #|
    return x, y  #|
def lima(ggg):   #|
    return ggg   #|
                 #|
pizza = rafa     #|
i = lima(pizza)  #|
                 #|
##################|

