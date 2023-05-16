# copy - retorna uma cópia rasa (shallow copy)

import copy

d1= {
    'c1' : 1,
    'c2' : 2,
    'list1': [0, 1, 2]
}
d2 = copy.deepcopy(d1)
#d2 = d1.copy() #d2 aponta pra d1

d2['c1'] = 10000 #quando utilizo .copy o valor de d1 nãovai ser mudado
#por d2.
d2['list1'][1] = 999999

#.copy() faz apenas uma copia rasa de valores imutáveis
# já o deepcopy é uma cópia mais profunda (valores mutáveis)

print(d1)
print(d2) # agora se tem 2 dicionários