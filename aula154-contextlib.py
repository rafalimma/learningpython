# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arq, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arq, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula154.txt', 'w') as arquivo:
    arquivo.write('op bãoo\n')
    arquivo.write('linha2\n', 123)
    arquivo.write('linha3\n')
    print("with", arquivo)