import sys
# Generator exprettion, iterables e Iterators no python
iterable = ['eu', 'tenho', '__iter__'] # ter os valores sequencialmente
iterator = iter(iterable) # tem iter e __next__ # te entregar um valor por vez
# next() retorna o próximo valor do iterator
print(next(iterator))

# Generator é uma função que pausa
generator = (
    n for n in range(10000)
)
lista = [n for n in range(100)] #aq todos os valores ja estão salvos na meméria
print(sys.getsizeof(generator))
print(sys.getsizeof(lista)) #tamanho da lista em bytes

for n in generator:
    print(n)

#vantagem: você não tem uma noção de tamanho no generator
#(não consegue acessar indices)