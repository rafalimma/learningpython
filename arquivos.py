
file = open('aqrquivos/arq.txt', 'r')
content = file.read()
print(content)
file = open('aqrquivos/arq.txt', 'a')
escrevendo = file.write('buenasss')
print(content)
file.close()

file