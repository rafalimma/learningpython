# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence

class Mylist(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[0] = value
        self._index += 1

    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    def __iter__(self):
        return self
    def __next__(self):
        return self    

if __name__ == '__main__':
    lista = Mylist()
    lista.append('Rafael')
    lista.append('Jões')
    print(lista._data)
    # print(len(lista))
    for item in lista:
        print(item)
        