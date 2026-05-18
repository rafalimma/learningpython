'''
Imagine que você precisa processar uma lista com 10 milhões de lances de um leilão.
Se você usar uma função comum com return, o Python vai criar todos os 10 milhões de objetos na memória de uma só vez antes de te entregar o resultado. 
Se cada item gastar um pouco de memória, seu script pode simplesmente travar o servidor (Erro de Out of Memory).
'''

# solução geradores yield
'''
Devolve o valor atual para quem pediu.
Pausa a execução da função bem ali.
Lembra exatamente onde parou para continuar na próxima vez que for chamado.
'''
#usando return

# def gera_lances_pesado(n):
#     resultado = []
#     for i in range(n):
#         resultado.append(i)
#     return resultado

# # Se n for 100.000.000, sua memória RAM vai pro espaço aqui:
# lista = gera_lances_pesado(100000000)

# def gera_numeros_leve(n):
#     for i in range(n):
#         yield i

# meu_gerador = gera_numeros_leve(100000000)
# # o dado só existe depois que eu peço ele
# for numero in meu_gerador:
#     print(numero)
#     break

# pode consumir com um for ou com um next()

'''
Para entender o poder do yield, você vai criar um gerador que simula lances subindo infinitamente, mas sem gastar memória.
'''

def simulador_lances(lance_inicial, inc):
    while True:
        yield lance_inicial
        lance_inicial += inc
meu_leilao = simulador_lances(100, 50)

print(next(meu_leilao))
print(next(meu_leilao))
print(next(meu_leilao))