# Exercícios com funções

#1) Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

#2) Crie uma função que fala se um numero é par ou impar.
#Retorne se o número é par ou impar.

#exercicio 1:

def mult(*args):
    total = 1
    for num in args:
        total = total * num
    return total

args = []
while len(args) < 5:
    n = input("Digite um valor: ")
    n = int(n)
    args.append(n)

multiplicação = mult(*args)
print(f"A multiplicação dos numeros que você digitou é:", multiplicação)

#exercicio 2:

while True:
    def ver(numero):
        if numero % 2 == 0:
            print("Esse número é par")
        else:
            print("Esse numero é impar")
    

    numero = input("Digite um número: ")
    numero = int(numero)
    ver(numero)