# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar sintático)
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorarar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Ok, agora você foi decorada')
        return result
    return interna

#^função decoradora
@criar_funcao #o python vai usar o criar_função na funcao de baixo
def invertestring(string): #assim ele troca essa função pelo resultado da função da clousure
    print(f'{invertestring.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('"param" deve ser uma string')


invert_paramether_checker = criar_funcao(invertestring)
invertida = invert_paramether_checker('123')
print(invertida)

