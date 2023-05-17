# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


n = 0
acertos = 0

while n < len(perguntas):
    di1 = perguntas[n]
    print(di1['Pergunta'])
    print()

    j = 0
    for i in di1['Opções']:
        print(j, f')',i)
        if i == di1['Resposta']:
            resp = j
        j = j + 1
    print()

    res = int(input('Escolha uma opção: '))
    if res == resp:
        print('acertou')
        acertos = acertos + 1
    else:
        print('errou')
    n = n + 1

quantas = len(perguntas)
print()
print(f'Você acertou {acertos} de {quantas} perguntas')





