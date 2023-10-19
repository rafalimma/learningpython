# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        print('Chamou upper')
        retorno =  super().upper()
        print('dada')
        return retorno
        #super() #retorna temporariamente a super classe, assim você pode
        #chamar métodos da classe pai

string = MinhaString('Luiz')
print(string.upper())

class A:
    atributo_a = 'valor a '

    def metodo(self):
        print('A')

class B(A): #tudo que está em A está em B
    atributo_b = 'valor b'
    def __init__(self, atributo, outra) -> None:
        super().__init__(atributo)
        self.outra_coisa  = outra

    def metodo(self): #método foi sobreposto ou seja o método q vai executar é o de B
        print('B')

class C(B): #tudo que tem em B está em C
    #C tem A e B, mas o método vai ser sobrepostos
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs) -> None:
        print('burlei os system')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()
        super(B, self).metodo() #pega o obj de cima
        print('C')

c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)

#print(c.atributo_a)
#print(c.atributo_b )
#print(c.atributo_c )
#c.metodo()
