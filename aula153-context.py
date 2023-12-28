# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, caminho_arq, modo):
        print('init')
        self.caminho_arquivo = caminho_arq
        self.modo = modo
        self._arquivo = None
    def __enter__(self): #joga alguma coisa na variavel 'alguma_coisa'
        print('ABRINDO O ARQUIVO')
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        #raise class_exception(*exception_.args).with_traceback(traceback_)
        #print(class_exception)
        #print(exception_)
        #print(traceback_)
        #return True #tratei a excesão
        #exception_.add_note()
        exception_.add_note("nota -> isso é um erro comum")
        #raise ConnectionError('Não deu para conectar')

#instancia = MyContextManager('aula153.txt', 'w')
with MyOpen('aula153.txt', 'w') as arquivo:
    arquivo.write('linha1\n')
    arquivo.write('linha2\n', 123)
    arquivo.write('linha3\n')
    print("with", arquivo)
    
