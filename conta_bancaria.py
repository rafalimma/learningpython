class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = valor + self.saldo
        return self.saldo
    
    def sacar(self, valor):
        if not valor >= 0 or valor > self.saldo:
            return 'Você não pode sacar valores negativos ou nulos'
        self.saldo = self.saldo - valor
        return self.saldo
    
    def exibir_saldo(self):
        print("seu saldo é:", self.saldo)
        return

conta = ContaBancaria("Rafael", 15000)
deposito = conta.depositar(300)
print(deposito)
saque = conta.sacar(20000)
print(saque)
print(conta.exibir_saldo())




