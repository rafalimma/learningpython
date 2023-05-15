'''
Clousure e funções que retornam outras funções      
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # se tirar o parenteses aponta o espaço na memória


falar_bomdia = criar_saudacao('bom dia')
falar_boanoite = criar_saudacao('boa noite')
for nome in ['Maria', 'Rafael', 'Natália']:
    print(falar_bomdia(nome))
    print(falar_boanoite(nome))
