'''
como o for funciona?
Iterável -> str, range, etc (__iter__) (elemento que pode
entregar uma coisa por vez.)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
# for letra in texto:
txt = 'Rafa' #iterável
iterador = iter(txt) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
        print('*')
    except StopIteration:
        break
        
