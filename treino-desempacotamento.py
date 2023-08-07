'''
exercício em Python que envolve empacotamento e desempacotamento de dicionários. Neste exercício,
vamos criar uma função que recebe informações sobre um aluno (nome, idade e curso) como argumentos individuais e,
em seguida,
empacota essas informações em um dicionário.
Depois, vamos desempacotar o dicionário para obter as informações do aluno.
'''

def info(a, b, c):

    id = '123' if b < 18 else '345'
    aluno = {
        'nome': a,
        'idade': b,
        'curso': c,
        'id': id
    }
    return aluno

def desemp_info(aluno):
    nome = aluno['nome']
    idade = aluno['idade']
    curso = aluno['curso']
    id =aluno['id']
    return nome, idade, curso, id



nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
curso = input('Digite seu curso: ')
if nome.isdigit() or curso.isdigit():
    print('digite corretamente')

total_info = info(nome, idade, curso)
print(total_info)

desemp_total = desemp_info(total_info)
print(desemp_total)

