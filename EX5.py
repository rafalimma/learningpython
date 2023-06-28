galera = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['idade'] = int(input('idade: '))
print(pessoa)

