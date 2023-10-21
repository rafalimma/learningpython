# abstração
# Herença é um
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    
class LogFileMixin(Log): #adicionar funcionalidades na sua herança multipla
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':    
    l = LogFileMixin()
    l.log_error('qualquer coisa')