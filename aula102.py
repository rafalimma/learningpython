# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
try:
    import sys
    sys.path.append('\Users\rafae\AppData\Local')
except ModuleNotFoundError:
    ...
import aula102_m #importei um módulo inteiro


print('este modulo se chama', __name__)
print(*sys.path, sep='\n')
# o primeiro módulo que é executado pelo python se chama main