from log import LogFileMixin

class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome #não pode usar esse atributo fora da classe pois é protegido
        self._ligado = False


    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligado(self):
        if not self._ligado:
            self._ligado = False
    
class Smartphone(Eletronico, LogFileMixin):

    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_sucess(msg)

    def desligado(self):
        super().desligado()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)