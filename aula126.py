# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
#atributos - dados dentro da classe
#métodos - funções dentro da classe
#método init, inicializa os atributos dentro da classe
#quando se cria uma classe se cria um molde que gera novos objs

string = 'Luiz' # str
print(string.upper())
print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Rafa', 'Limaa') #gerar nova instancia da classe
#p1.nome = 'Rafa'
#p1.sobrenome = 'Limaa'

p2 = Pessoa('Amanda', 'Limaa') #'python cria um novo obj e joga na nessa variável' 
#gerar nova instancia da classe
#p2.nome = 'Amanda'
#p2.sobrenome = 'Limaa'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

