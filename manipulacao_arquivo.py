import csv
from pathlib import Path
#pega  a pasta que o script esta salvo agora:
root = Path(__file__).parent
'''
'r' -> read
'w' -> escrever (apaga o que tinha antes)
'a' -> append (adicional ao final)
'''

#manipulação de txt
# arquivo, o que eu quero fazer no arquivo, encoding

caminho_arquivo_txt = root / "notas.txt"
caminho_arquivo_csv = root / "dados_simples.csv"
#lendo
with open(caminho_arquivo_txt, 'r', encoding="utf-8") as arquivo_r:
    linhas = arquivo_r.readlines()

print(linhas)
#escrevendo
with open(caminho_arquivo_txt, 'w', encoding="utf-8") as arquivo:
    arquivo.write("escrevendo linha 1....")
print(linhas)

#manipulação de arquivo csv
#DictReader e DictWriter transformam cada linha em um dicionário
with open(caminho_arquivo_csv, 'r', encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=';')
    for linha in leitor:
        print(linha)

print()
print("exercício")
'''
Você tem uma lista de lances brutos que vieram de um sistema legado. 
Seu trabalho é ler esses dados, limpá-los e salvar um novo CSV "VIP" apenas com lances acima de 500 reais.
'''
print('escrevendo dados brutos')
dados_brutos = """produto;lance;cliente
  notebook dell  ; 2500 ; rafael silva 
geladeira brastemp; 450 ; maria oliveira
  iphone 15  ; 6000 ;  JOÃO AMORIM 
mouse gamer ; 150 ; ana costa """

# with open("lances_brutos.csv", 'w', encoding="utf-8") as lances_brutos:
#     lances_brutos.write(dados_brutos)

leiloes_vip = []
#limpando leiloes
caminho_lances_brutos = root / "lances_brutos.csv"
caminho_lances_vip = root / "lances_vip.csv"
with open(caminho_lances_brutos, 'r', encoding="utf-8") as lances_brutos:
    dados_brutos = csv.DictReader(lances_brutos, delimiter=';')
    for l in dados_brutos:
        produto = l['produto'].strip().title()
        lance = int(l['lance'].strip())
        cliente = l['cliente'].strip().upper()
        if not lance < 500:
            dados_vip = {
                "produto": produto,
                "lance": lance,
                "cliente": cliente
            }
            leiloes_vip.append(dados_vip)

colunas = ['produto', 'lance', 'cliente']

with open(caminho_lances_vip, 'w', encoding="utf-8", newline='') as arquivo_lances_vip:
    escritor = csv.DictWriter(arquivo_lances_vip, fieldnames=colunas, delimiter=";")
    escritor.writeheader()
    escritor.writerows(leiloes_vip)




