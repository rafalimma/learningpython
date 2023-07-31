import random
'''
def decoradora(func):
    def checador(*args, **kwargs):
        print('decoração checagem')
        #for arg in args:
        #    cheker(arg)
        
        res = func(*args, **kwargs) ###
        return res
    return checador

def cheker(dado):
    if not dado.isalpha():
        print('digite corrtamente')
    else: 
        print('ok')



@decoradora
def nome_letraalta(nome):
    return nome.upper()

dada = nome_letraalta('rafael')
print(dada)
'''
'''
def addcode(func):
    def inner(nome):
        code = random.randint(1, 100)
        code = str(code)
        final_name = nome
        return final_name + code
    return inner




name = input('Digite seu nome: ')
code = random.randint(1, 100)

@addcode
def cheker(name):
    for letter in name:
        if not letter.isalpha():
            raise TypeError('Digite corretmante.')
        

name_with_code = cheker(name)
print(name_with_code)
'''

#generator functions

def abobora(b=0, maximum=10):
    while True:
        yield b
        b += 1
        if b >= maximum:
            break
        

gen = abobora()
for i in gen:
    print(i) #não preciso usar next

