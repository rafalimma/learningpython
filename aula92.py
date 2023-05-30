# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set)) # é instancia de 
    
    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)): # ou int ou float
        print('INT FLOAT')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)

