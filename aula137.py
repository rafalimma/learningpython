# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor # _cor não deve ser usado

    @property
    def cor(self):
        return self._cor
    
    @cor.setter #precisa do self e do valor
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('não ')
        self._cor = valor

    
caneta = Caneta('Azul')
caneta.cor = 'Rosa'
# getter -> obter valor
print(caneta.cor)