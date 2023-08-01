#count é um iterador sem fim
#esta no método itertools

from itertools import count

c1 = count(10, 4)
r1 = range(10, 4)
#como checar se o obj é um iterator:
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('c1', hasattr(r1, '__iter__'))
print('c1', hasattr(r1, '__next__'))

#range é um iterável mas não um iterator
# é um iteravel
for i in c1:#pede o iterator do count, e o count
            #retorna ele mesmo pro for, e o for pede o next
    if i > 90:
        break
    print(i)

print(r1)
