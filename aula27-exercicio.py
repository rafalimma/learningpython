'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
'''

nome = (input('digite seu nome: '))
idade = (input('digite sua idade: '))

if nome and idade : #'' retorna falor falsy

    print(f'Seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print(f'seu nome: {nome} contém espaços')
    else:
        print('seu nome não contém espaços')

    lennome = len(nome)
    print(f'seu nome tem {lennome} caracteres')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')


else:
    print('Desculpe, você deixou campos vazios')


