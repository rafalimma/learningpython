# Decoradores com parâmetros
def fabrica_de_decoradores(a,b,c): #pega os parametros do decorador
    def fabrica_de_funcoes(func): #pega a função (decorador em si)
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # onde a função vai ser executada
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

#func decoradora é usada para criar funções 
#@decoradora#linkei a função soma com a decoradora
@fabrica_de_decoradores
# a função aninhada ou seja a mais interna é a que vai substituir a função real
def soma(x, y): #o python passa a função para a função decoradora
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
dez_vezes_cinco = multiplica(10, 5)
