#packages
#apartir do arquivo main vc importa as outras coisas
#from sys import path
#from aula105_package.modulo import soma_modulo
#print(*path, sep='\n')
#print(soma_modulo(3, 5))

print(__name__)
from aula105_package.modulo import falaoi, soma_modulo
falaoi()
print(soma_modulo(4, 9))

#da erro pois o python tentaq importar moduleb tbm
#todos as importações do programa precisam ser relacionadas com o mais

import aula105_package #voce quer importar codigo do modulo e não do pacote
print(aula105_package.soma_modulo(2,5))

