'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

saltos = []
while True:
    nome = input("Escreva seu nome: ")
    for dist in range(5):
        salto = input("Digite a distancia do salto: ")
        if salto.isdigit():
            salto = int(salto)
        saltos.append(salto)
    else:
        print("dada")

#ordem dos saltos:
    print(f"Primeiro salto: ", {saltos[0]})
    print(f"O segundo salto: ", {saltos[1]})
    print(f"O terceiro salto: ", {saltos[2]})
    print(f"O quarto salto: ", {saltos[3]})
    print(f"O quinto salto: ", {saltos[4]})

    maior = max(saltos)
    menor = min(saltos)
    print(f"O melhor salto foi: ", {maior})
    print(f"O pior salto foi: ", {menor})
#excluindo os extremos
    saltos.remove(menor)
    saltos.remove(maior)
#média sem extremos
    media = saltos[0] + saltos[1] + saltos[2]
    mediaf = (media/3)
    print("Resultado final:")
    print(f"O nome do atleta é: {nome}, e a média dos saltos é {mediaf}.")

