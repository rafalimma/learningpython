# F strings

nome = "Rafael"
peso = 64
altura_emmetros = 1.80

imc_rafael = peso / altura_emmetros**2

print(nome ,"tem", altura_emmetros ,"de altura, pesa", peso ,"quilos e seu IMC é", imc_rafael)

lina_1 = f'{nome} tem {altura_emmetros:.2f} de altura'

print(lina_1)
lina_2 = f'pesa {peso} quilos e seu imc é {imc_rafael:.2f}'
print(lina_2)