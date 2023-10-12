# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for enderecos in self.enderecos:
            print(enderecos.rua, enderecos.numero)

    def __del__(self):
        print('APAGANDO', self.nome)



class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)
        #esta coletando e apagando o lixo

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Av Brasil', 44)
cliente1.inserir_enderecos('Manoel Ribas', 60)

cliente1.listar_enderecos()

print('aqui termina o código')

