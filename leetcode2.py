# transforma o numero em uma sequencia de caracteres
# binário e compara cada um com o próximo

def hasalterningbits(n):
    binario = bin(n)[2:]

    #percorre a string comparando o atual com o próximo
    for i in range(len(binario) - 1):
        if binario[i] == binario[i+1]:
            return False
    
    return True

'''
2. Abordagem Bitwise (Nível "Turing")Em testes de alta performance, eles adoram quando você resolve problemas de bits usando... bits.
Se um número tem bits alternados (ex: 1010), quando você o desloca para a direita (>> 1), você obtém 0101. 
Se você fizer uma operação XOR ($\oplus$) entre eles, o resultado será uma sequência só de números 1 (1111).
'''

def hasalterningbitsBitwise(n):
    f = n ^ (n >> 1)
    return (f & (f + 1)) == 0