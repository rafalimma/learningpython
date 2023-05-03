a = 'ACCC'
b = 'DADA'
c = 1.1
string = 'a={name1} b={nome2} c={nome3:.2f}' #colocar valores para não ter erro de alcançe
formato = string.format(name1=a,
                         nome2=b, nome3=c)


print(formato)
