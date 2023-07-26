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
