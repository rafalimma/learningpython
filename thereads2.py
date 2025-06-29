from time import sleep
from threading import Thread

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t = Thread(target=vai_demorar, args=('Olá mundo!', 5))
# t.start()
# t1 = Thread(target=vai_demorar, args=('Olá mundo again!', 5))
# t1.start()

# # for i in range(10):
# #     print(i)
# #     sleep(.5)

# while t1.is_alive():
#     print('Esperando a thread!')
#     sleep(2)

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print('não temos ingressos suficiemtes')
            return
        
        sleep(1)

        self.estoque -= quantidade
        print(f'você comprou {quantidade} ingressos.'
              f'Ainda temos {self.estoque}')

# if __name__ == '__main__':
#     Ingressos = Ingressos(10)
#     Ingressos.comprar(1)
#     Ingressos.comprar(1)
#     Ingressos.comprar(1)
#     Ingressos.comprar(1)

if __name__ == '__main__':
    Ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=Ingressos.comprar, args=(i, 1))
        t.start()

