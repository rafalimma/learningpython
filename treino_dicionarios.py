alunos_dados = [
    {"nome": "Alice", "notas": [8.5, 9.0, 7.8]},
    {"nome": "Bob", "notas": [5.0, 4.5, 6.0]},
    {"nome": "Charlie", "notas": [7.0, 6.5, 7.5]},
    {"nome": "Deborah", "notas": [10.0, 3.0, 5.5]},
]

def calcula_media(alunos_dados):
    resultado_final = []
    statistics = {"aprovado": 0, "reprovado": 0}
    for aluno in alunos_dados:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = sum(notas)//len(notas)
        status = "aprovado" if media >= 7.0 else "reprovado"
        resumo = {
            "nome": nome,
            "media": media,
            "status": status
        }
        resultado_final.append(resumo)
        statistics[status] += 1
    return resultado_final, statistics
    
print(calcula_media(alunos_dados))
