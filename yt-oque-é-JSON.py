#estrutuara de dados para transportar ou criar dados
import json
import os

pessoas = [
    {
        "nome": 'rafa',
        "sobrenome": 'lima', 
        "idade": 17,
        "assets": '12', 
    }
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)