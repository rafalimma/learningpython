#texto = 'Python'

#i = 0
#size_str = len(texto) # usa-se owhile
#quando você não sabe presisamente quantas repetições tem 

texto = 'Python'
novo_txt = ''
for letra in texto:
    novo_txt += f'*{letra}'
    print(letra)
print(novo_txt + '*')
