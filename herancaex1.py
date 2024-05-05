class Curso:
    def __init__(self, curso, n_materias) -> None:
        self.curso  = curso
        self.n_materias = n_materias
    
    def materias(self):
        print(f'Curso de {self.curso} de {self.n_materias}')
    
class Pessoa(Curso):
    def __init__(self, curso, n_materias, nome, idade):
        super().__init__(curso, n_materias)
        self.nome = nome
        self.idade = idade
    
    def nome_idade(self):
        print(f'{self.nome} tem {self.idade} de idade!! e faz {self.curso}')
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, n_materias):
        super().__init__(nome, idade, curso, n_materias)
    def aluno(self):
        print('')

class Professor(Pessoa):
    def __init__(self, curso, n_materias, nome, idade):
        super().__init__(curso, n_materias, nome, idade)
