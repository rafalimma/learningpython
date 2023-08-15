# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
"""
def recursiva(inicio=0, fim=10):
    #caso Base
    print(inicio, fim)

    if inicio >= fim:
        return fim
    
    #caso recursivo
    #contar até chager no final
    inicio += 1
    return recursiva(inicio, fim)
    #salva essa função na call stack pra retornar o novo
    #valor na próxima função.

print(recursiva())
"""
def fat(n):
    if n == 1 or n == 0:
        return 1
    
    return n * fat(n - 1)

print(fat(7))
