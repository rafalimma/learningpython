

class Usuario:
    def __init__(self, nome, senha):
        senha = self.senha
        nome = self.nome

    def fazer_login(self):
        print(f'{self.nome} logado com sucesso')

def log_acesso(func):
    def wrapper(*args, **kwargs):
        instancia = args 