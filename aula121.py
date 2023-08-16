# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'D:\\Documents\\Nova Pasta teste\\'
caminho_arquivo += 'aula121.txt'
print(caminho_arquivo)

#arquivo = open(caminho_arquivo, 'w')
#
#arquivo.close

with open(caminho_arquivo, 'w+') as arquivo:#abre e fecha o arquivo
    arquivo.write("opaa\n")
    arquivo.write("linha2\n")
    arquivo.writelines(
        ('linha3\n', 'linha4\n')
    )
    arquivo.seek(0, 0) #move para topo do arquio
    print(arquivo.read())

print("#"* 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())





