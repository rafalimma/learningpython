#raise - lançando exceções (erros) 

#print(123)
#raise ValueError('deu erro') #raise levanta um erro
print(456)
'''
def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('dada')
        raise #relançando a execão
    
print(divide(8, 0))
'''
def divide(n, d):
    if not isinstance(d, (int, float)):
        raise TypeError('apenas númericos')
    
print(divide(8, '0'))
    