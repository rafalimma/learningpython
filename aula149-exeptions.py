# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
#não 
class Erro(Exception):
    ...
class OutroErro(Exception):
    ...

def initial():
    erro = Erro('CK inválido')
    erro.add_note('Erro do Checklist.')
    raise erro

try:
    initial()
except (Erro) as error:
    print(error)
    print(error.__class__.__name__)
    new_error = OutroErro('Esse é um novo erro')
    raise new_error from error




'''
class MyError(Exception):
    ...
class OutroError(Exception):
    ...
def raising():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('erro tal')
    raise exception_

try:
    raising()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Lançando outro erro')
    raise exception_ from error
'''
