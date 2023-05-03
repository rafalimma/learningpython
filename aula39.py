'''
Calculadora com While
'''

while True:
    num1 = input('Digite um número: ')
    num2 = input('digite outro número: ')
    operação = input('qual operação quer fazer?(+-*//) ')

    inteiro = num1.isdigit() and num2.isdigit()

    if inteiro and operação == '+':
        print(int(num1) + int(num2))
    elif inteiro and operação == '-':
        print(int(num1) - int(num2))
    elif inteiro and operação == '*':
        print(int(num1) * int(num2))
    elif inteiro and operação == '//':
        print(int(num1) // int(num2))

    else:
        print('digite um valor válido')
        continue
    sair = input('quer sair [S]Sim ').lower().startswith('s')
    if sair is True:
        break
  # lower retorna a mesma string em letras minusculas

