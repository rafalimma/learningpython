# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'aula132.json'

class LojaCarros:
    def __init__(self, nome, marca) -> None:
        self.nome = nome
        self.marca = marca

carro1 = LojaCarros('Golf R32', 'VolksWagen')
carro2 = LojaCarros('Camaro', 'GM')
carro3 = LojaCarros('3000-GT', 'Mitsubishi')

data = [vars(carro1), vars(carro2), vars(carro3)]

def fazendo_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(data, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É __MAIN__')
    fazendo_dump()

