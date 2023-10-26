class Pessoa:
    def __init__(self, nome, genero, idade, roupa) -> None:
        self.nome = nome
        self.genero = genero
        self.idade = idade
        self.roupa = roupa
        self.enderecos = []


    @property
    def estilo(self):
        print('seu estilo é: ')
        return self.roupa
    
    @property
    def idade_verificator(self):
        if self.idade.isdigit():
            self.idade = int(self.idade)
        else:
            return True

    def mostrar(self):
        return f'O nome da pessoa é {self.nome}, tem {self.idade} anos do genero {self.genero}'
    def maior(self):
        if self.idade > 18:
            return f'Você tem {self.idade} e é de maior'
        return f'Você não tem mais de 18 anos'
    
    def data_secret(self, cpf, rg):
        self.enderecos.append(Adress(cpf, rg))

    
class Adress:
    def __init__(self, cpf, rg) -> None:
        self.cpf = cpf
        self.rg = rg

    def verificador_rg(self):
        if self.rg.isdigit():
            self.rg = int(self.rg)
        else:
            return True
        
    def verificador_cpf(self):
        if self.cpf.isdigit():
            self.cpf = int(self.cpf)
        else:
            return True

while True:
    pessoa1 = Pessoa (
        input('Digite seu nome: '),
        input('Digite seu genero: '),
        input('Digite sua idade: '),
        input('Digite seu estilo: '),
    )
    check = pessoa1.idade_verificator
    if check:
        print('use apenas números para a idade')
        continue
    print(pessoa1.estilo)
    print(pessoa1.mostrar())
    print(pessoa1.maior())
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")
    pessoa1.data_secret(cpf, rg)
    cpfcheck = pessoa1.verificator_cpf
    if cpfcheck:
        print('use apenas números para o CPF')
        continue
