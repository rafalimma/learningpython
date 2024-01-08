def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

def meu_palneta(metodo):
    def intern(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if resultado == 'Terra':
            return f'você esta em casa'
        else:
            print('voce esta longe de casa')
        return resultado
    return intern

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

@add_repr #== Time = add_repr(Time)
class Time:
    def __init__(self, nome):
        self.nome = nome

@add_repr #== Planeta = add_repr(Planeta)  
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_palneta
    def tamanho(self):
        return f'O tamanho do planeta {self.nome} é tal...'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
print()
print(terra.tamanho())
print(marte.tamanho())