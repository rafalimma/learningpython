from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula177.csv'

lista_clientes = [
    {'Nome': 'Rafa LIma', 'Endereço': 'Rua 55'},
    {'Nome': 'Rafa LIma', 'Endereço': 'Rua 55'},
    {'Nome': 'Maria', 'Endereço': 'Rua 55'}
]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)
#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())
#no dicionário
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)
