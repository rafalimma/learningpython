# *args permite que sua função receba qualquer numero de argumentos posicionais
# O python enpacota todos eles em uma tupla que se comporta como uma lista

def somar_lances(*args):
    return sum(args)

print(somar_lances(20, 40, 45, 90, 10))

# kwargs dicionário infinito recebe qualquer numero de argumentos nomeados
# python enpacota tudo em um dicionário

def cadastrar_produto(**kwargs):
    for chave, valor in kwargs.items(): # usa o .items()
        print(f"{chave}: {valor}")

cadastrar_produto(nome="TV", preco=2000, categoria="Eletrônico")

# Você pode misturar argumentos fixos com os flexíveis. A ordem deve ser sempre: (argumentos_fixos, *args, kwargs).

#PROCESSADOR DE LEILAO FLEXIVEL
# Sua função precisa ser capaz de receber qualquer quantidade de lances e também algumas configurações opcionais.

'''
Crie uma função chamada processar_lances_do_dia que aceita:
*lances: uma quantidade variável de números (os valores dos lances).
config: argumentos extras como moeda (ex: "BRL") e bonus (um valor fixo para somar a todos os lances).
'''
def processar_lances_do_dia(config, *args):
    bonus = config.get('bonus', 0)
    moeda = config.get('moeda', "BRL")
    leiloes_processados = [l + bonus for l in args if bonus > 0]
    l_final = {
        'total Lances': args,
        'lances com bonus': leiloes_processados,
        'moeda': moeda
    }
    # return f"R$ USD {leiloes_processados}" if moeda == "USD" else f"R$ BRL {leiloes_processados}"
    return l_final

config = {"bonus": 25, "moeda": "USD"}
leiloes = processar_lances_do_dia(config, 25, 90, 40, 100, 98, 120)
print(leiloes)


