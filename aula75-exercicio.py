"""
exercicio - Crie funções que duplicam, triplicam e quadruplicam
o numero recebido como parâmetro.
"""
"""
while True:
    def mult2(numero):
        numero = int(numero)
        numero = numero * 2
        return numero
    def mult3(numero):
        numero = int(numero)
        numero = numero * 3
        return numero
    def mult4(numero):
        numero = int(numero)
        numero = numero * 4
        return numero

    numero = input('Digite um valor: ')
    mult2(numero)
    mult3(numero)
    mult4(numero)
    
    print(mult2(numero))
    print(mult3(numero))
    print(mult4(numero))

while True:
    def m(num):
        def m2(num2):
            num2 = num * 2
        return m2
            def m3(num3):
                num3 = num * 3
            return m3
                def m4(num4):
                    num4 = num * 4
                    return f'vezes 2:{num2},vezes 3:{num3}, vezes 4:{num4}'
                return m4


    num = int(input("Digite um número"))
    print(m(num))
"""

def multiplier(mult):
    def numero(num):
        return num * mult
    return numero

duplicar = multiplier(2)
triplicar = multiplier(3)
quadruplicar = multiplier(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))



