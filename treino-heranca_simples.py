#Vamos criar um sistema simples de gerenciamento de funcionários em uma empresa
#onde temos duas classes: Funcionario e Gerente

class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario
        self.listag = []
        self.listaf = []
    
    @property
    def typee(self):
        self.salario = (int(self.salario))
        return self.salario

    def calcular_comissao(self, comissao = 50):
        print("oi")
        return self.salario + comissao
    
    def funcionarios(self):
        self.listaf.append(self.nome)
        self.listaf.append(self.salario)

    
class Gerente(Funcionario):
    def __init__(self, nome, salario, depart) -> None:
        super().__init__(nome, salario)
        self.departamento = depart

    @property
    def typee(self):
        self.salario = (int(self.salario))
        return self.salario

    def calcular_comissao(self, n_comissao = 1000):
        return super().calcular_comissao() + n_comissao
    
    def gerentes(self):
        self.listag.append(self.nome)
        self.listag.append(self.salario)
        self.listag.append(self.departamento)
while True:
    qtd_f = input("quantos funcionários tem na empresa? ")
    if qtd_f.isdigit():
        qtd_f = int(qtd_f)
        break
    else:
        print("digite um número")
        continue
n=0
while n <= qtd_f:
    opc = input("Gerente ou funcionário? (f:Funcionário, g:Gerente) ")
    opcoes = "fg"
    if not opc in opcoes:
        print("Digite corretamente.")
        continue
    if opc == "f":
        funcionario1 = Funcionario(
            input("Digite o nome do funcionário: "),
            input("Digite o salário do funcionário: "),
        )
        funcionario1.typee
        funcionario1.calcular_comissao()
        funcionario1.funcionarios()
        print(funcionario1.salario)
        print(funcionario1.listaf)
        n=n+1
    else:
        gerente1 = Gerente(
            input("Digite o nome do Gerente: "),
            input("Digite o salário do Gerente: "),
            input("Digite o departamento: "),
        )
        funcionario1.typee
        gerente1.calcular_comissao()
        gerente1.gerentes()
        print(gerente1.salario)
        print(gerente1.listag)
        n=n+1







    