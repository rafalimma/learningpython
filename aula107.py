#variáveis livres + nonlocal

def fora(x):
    s = x #unica variável livre
    def dentro():
        #print(locals())
        return s #s é uma variavel livre dentro da função 'dentro'
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

def concatenar(string_inicial):
    valor_f = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_f #como a variável n esta definada nesse escopo
        #é necessário indicar para o python que ela não é local para assim
        #ele buscar o valor antigo.
        valor_f += valor_a_concatenar
        return valor_f
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

    