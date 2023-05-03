"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
print('Descubra os dois ultimos digitos do seu cpf.')
cpf = input("Digite 9 primeiros digitos do CPF: ")
ncpf = len(cpf)

if ncpf < 9 or ncpf > 9:
    print("Digite um cpf válido")
  
else:
    digitos9 = cpf[:9] #tirando os 9 primeiros digts para multiplicar
    contador_reg1 = 10
    resultado1 = 0

    for digito in digitos9:
        resultado1 += int(digito) *  contador_reg1
        contador_reg1 -= 1
#Fora do for:
    firstdigit = (resultado1 * 10) % 11
    firstdigit = firstdigit if firstdigit <= 9 else 0

#segundo digito do cpf: #inclua o firstdigit na contagem reg e no cpf:
    cpf = cpf + str(firstdigit)

    digitos10 = cpf[:10] #tirando os 10 primeiros digitos p multiplicar
    contador_reg2 = 11
    resultado2 = 0

    for digito in digitos10:
        resultado2 += int(digito) *contador_reg2
        contador_reg2 -= 1
#outside for:
    seconddigit = (resultado2 * 10) % 11
    seconddigit = seconddigit if seconddigit <= 9 else 0


    print(f"O penultimo digito do seu CPF é {firstdigit} e o ultimo é {seconddigit}")

