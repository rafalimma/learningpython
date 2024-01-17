"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float =0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...
    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.detalhes(f'(Depósito {valor})')
        
    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')
        print("---")

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
        print("não foi possível sacar o valor desejado")
        self.detalhes(f'(Saque negado {valor})')
        return self.saldo

class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int, saldo: float=0, limite: float=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
        print("não foi possível sacar o valor desejado")
        print(f"Seu limite é {self.limite:.2f}")
        self.detalhes(f'(Saque negado {valor})')
        return self.saldo


class Banco():
    ...

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    print('###')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('###')

