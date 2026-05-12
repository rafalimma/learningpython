'''
strip() -> faxineiro, remove espaços em branco ou outro caracter do inicio ao fim da linha
"  leilão  ".strip() → "leilão"

split() -> machado, corta a string em uma lista de partes baseando-se em um separador
"carro,moto,caminhão".split(",") → ['carro', 'moto', 'caminhão']

join() -> cola, pega uma lista e junta tudo em uma string só, o separador vem antes do comando
" - ".join(['2024', 'Maio', '12']) → "2024 - Maio - 12"
'''

# Imagine que você recebeu uma linha de um arquivo CSV que veio todo mal formatado. 
# Seu objetivo é limpar esses dados e exibir uma frase elegante.

linha_csv = "  notebook dell  ;  2500.7  ;  42  "
print(linha_csv)
produto = linha_csv.split(';')
lista_limpa = [a.strip() for a in produto]
texto_formatado = f"produto {lista_limpa[0]} preço {lista_limpa[1]}, quantidade {lista_limpa[2]}"
print(texto_formatado)