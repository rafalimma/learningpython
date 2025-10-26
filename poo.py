# classe define um tipo de objeto (molde)
# objeto é uma instancia concreta de uma classe
# método uma função definida dentro de uma classe que descreve
# um comportamento que os objetos dessa classe podem executar
# atributo é uma variável definida na classe que guarda informações do objeto

# propriedade é uma forma especial de acessar atributos
# com lógica embutida @property transforma método em propriedade


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura
#acessando com property

r = Retangulo(4, 5)
print(r.area) 

#acessando sem property

r = Retangulo(4,5)
print(r.area())

#Qual é o propósito do método __init__ em uma classe Python? É obrigatório
# defini-lo em todas as classes?
# inicializa os atributos da classe com valores iniciais
# vc só defini o __init__ se quiser que a classe faça algo ao ser instanciada



