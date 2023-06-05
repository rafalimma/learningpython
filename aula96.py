# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # pausa a execução da função
        # se tiver o return em uma generator func, ele
        #levanta um execão com a palavra q eu coloquei 
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=10)
for n in gen:
    print(n)
# o print(next(gemerator)) #despausa a função e vai para o próximo pause