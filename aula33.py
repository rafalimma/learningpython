"""
Repetiçoes
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito = quando um código não tem fim
"""
condicao = True

while condicao: #executa até a condição se tornar falsa
  nome  = input('qual o seu nome:')
  print(f'Seu nome é {nome}')
  if nome == 'sair':
    break #busca o while mais próximo
          #quando o break for verdadeiro ele sai
          #imediatamente do while
print('acabou') 

