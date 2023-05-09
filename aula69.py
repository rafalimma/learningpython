"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
#tudo que esta dentro da função(variáveis) esta protejido na função
x = 1

def escopo():
    #global x #altera a variável do módulo (hierarquia maxima)
    x = 20

    def func():
        #global x
        x = 55
        y = 3           #y não será executado pois está protegido
        print(x, y)        #pela funcão (function) e so pode ser executado por ela
                        #dentro da outra função       
    func()
    print(x)

#print(x)#não é possível acessar a variável sem chamar a função
#ou executala fora do escopo que ela está.
print(x)
escopo()
print(x)#x continua sendo 1
