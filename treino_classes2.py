class Pessoa:
    def __init__(self, nome, genero, idade, roupa) -> None:
        self.nome = nome
        self.genero = genero
        self.idade = idade
        self.roupa = roupa

    @property
    def estilo(self):
        print('seu estilo é: ')
        return self.roupa
    '''
    @property
    def idade_verificator(self):
        if self.idade.isdigit():
            return self.idade
        return 'É necessário fornecer um número como idade'
'''
    def mostrar(self):
        return f'O nome da pessoa é {self.nome}, tem {self.idade} anos do genero {self.genero}'
    def maior(self):
        if self.idade > 18:
            return f'Você tem {self.idade} e é de maior'
        return f'Você não tem mais de 18 anos'

while True:
    pessoa1 = Pessoa
    pessoa1.nome = input('Digite seu nome: ')
    pessoa1.genero = input('Digite seu genero: ')
    pessoa1.idade = (input('Digite sua idade: '))

    print(pessoa1.mostrar(self=pessoa1))
    print(pessoa1.maior(self=pessoa1))



