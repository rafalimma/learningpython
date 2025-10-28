import datetime

class Usuario:
    def __init__(self, nome, senha):
        senha = self.senha
        nome = self.nome

    def fazer_login(self):
        print(f'{self.nome} logado com sucesso')
        return True

def log_acesso(func):
    def wrapper(*args, **kwargs):
        instancia = args[0]
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("-" * 30)
        print(f"[{agora}] LOG: tentativa de acesso ao método -> {func.__name__}")

        if hasattr(instancia, 'nome'):
            print("usuário cadastrado: {instancia.nome}")

        print("-" * 30)
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper
