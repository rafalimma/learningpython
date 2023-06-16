#recarregar módulos

import importlib
import aula104_m

print(aula104_m.v)
for i in range(10):
    importlib.reload(aula104_m) #python n pode importar again seu módulo
    print(i)
print('fim')