def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

#fazendo a função soma em lambda:

print(
    executa(
        lambda x, y: x + y, # a parte do final é o retorno
            2, 3 # -> executa(soma, 2, 3)
    ),
    #executa(soma, 2, 3)

)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
'''
duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m
)
'''

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4
    )
)

# Outra explicação sobre lambda:

#é uma função que não se tem um nome
preco = 1000
#imposto = 30% do valor
def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(preco)) #passo a variável apenas no print

calcular2imposto = lambda x : x * 0.3
                        #parametro #resposta(argumento)


precos = [100, 500, 10, 25]

impostos = list(map(lambda x: x * 0.3, precos)) #map atribui uma função para cada valor na lista
print(impostos)
