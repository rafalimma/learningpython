#generator function (yield)
'''
def abobora(b=0, maximum=10):
    while True:
        yield b
        b += 1
        if b >= maximum:
            break
        

gen = abobora()
for i in gen:
    print(i) #não preciso usar next
'''
'''
Gerador de Números Primos
O objetivo deste exercício é criar uma generator function que gere números primos infinitamente. 
A generator function irá gerar os números primos um a um, e você pode utilizá-la para
imprimir os primeiros N números primos ou para qualquer outra finalidade que desejar.
Lembre-se de que um número primo é um número inteiro maior que 1 e que possui apenas dois divisores:
1 e ele mesmo.
'''

def generator(n=1, max=10):
    primos = set()
    while True:
        yield n
        n += 1
        if not n % 4 == 0:
            primos.add(n)
        if len(primos) >= max:
            print(primos)



n_primos = generator()
for i in n_primos:
    print(i)