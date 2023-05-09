"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

def single(a, b, c): #os que estão nos parenteses são [parametros] #def"nome da função"
    #print(3 + 4)
    #print('avocado')
    print(a, b, c)
    ... #voco pode chamar a função ao longo do código
        #por exemplo voce que seja executada uma tarefa especifica
        #mais de uma vez no código

single(4, 5, 3)# aqui vão os argumentos para os parâmetros

def saudacao(nome = "sem nome"):
    print(f"Olá, {nome}")

saudacao("Rafa")
saudacao("Mario")
