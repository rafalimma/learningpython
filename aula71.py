"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

#def soma(x, y):
    #return x + y

def soma(*args): #args é tido oq eu passar de argumento não nomeado pra função
    total = 0
    for numero in args:
        total = total + numero
    return total


    #args = list(args) #coverte args para uma lista
    #print(args, type(args))

soma123  = soma(1, 2, 3)
print(soma123)
numeros = 1, 2, 3, 9, 12
soma1239  = soma(*numeros) # "*" desempacotar, tirar os valores da tuple
print(soma1239)
print(sum(numeros))

#print(sum(1, 2, 3, 4, 66))
