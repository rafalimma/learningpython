import random

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
# embaralhar lista

nomes = ['rafael', 'joão', 'luana']
random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
nomes_novos = random.sample(nomes, k=3)
print(nomes_novos)
# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
nomes_choices = random.choices(nomes, k=3)
print(nomes_choices)

random.seed(0)