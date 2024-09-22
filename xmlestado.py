import xml.etree.ElementTree as ET
from xml.dom import minidom

brasil_capitais = {
    'AC': {
        'nome': 'Acre',
        'capital': 'Rio Branco'
    },
    'AL': {
        'nome': 'Alagoas',
        'capital': 'Maceió'
    },
    'AP': {
        'nome': 'Amapá',
        'capital': 'Macapá'
    },
    'AM': {
        'nome': 'Amazonas',
        'capital': 'Manaus'
    },
    'BA': {
        'nome': 'Bahia',
        'capital': 'Salvador'
    },
    'CE': {
        'nome': 'Ceará',
        'capital': 'Fortaleza'
    },
    'DF': {
        'nome': 'Distrito Federal',
        'capital': 'Brasília'
    },
    'ES': {
        'nome': 'Espírito Santo',
        'capital': 'Vitória'
    },
    'GO': {
        'nome': 'Goiás',
        'capital': 'Goiânia'
    },
    'MA': {
        'nome': 'Maranhão',
        'capital': 'São Luís'
    },
    'MT': {
        'nome': 'Mato Grosso',
        'capital': 'Cuiabá'
    },
    'MS': {
        'nome': 'Mato Grosso do Sul',
        'capital': 'Campo Grande'
    },
    'MG': {
        'nome': 'Minas Gerais',
        'capital': 'Belo Horizonte'
    },
    'PA': {
        'nome': 'Pará',
        'capital': 'Belém'
    },
    'PB': {
        'nome': 'Paraíba',
        'capital': 'João Pessoa'
    },
    'PR': {
        'nome': 'Paraná',
        'capital': 'Curitiba'
    },
    'PE': {
        'nome': 'Pernambuco',
        'capital': 'Recife'
    },
    'PI': {
        'nome': 'Piauí',
        'capital': 'Teresina'
    },
    'RJ': {
        'nome': 'Rio de Janeiro',
        'capital': 'Rio de Janeiro'
    },
    'RN': {
        'nome': 'Rio Grande do Norte',
        'capital': 'Natal'
    },
    'RS': {
        'nome': 'Rio Grande do Sul',
        'capital': 'Porto Alegre'
    },
    'RO': {
        'nome': 'Rondônia',
        'capital': 'Porto Velho'
    },
    'RR': {
        'nome': 'Roraima',
        'capital': 'Boa Vista'
    },
    'SC': {
        'nome': 'Santa Catarina',
        'capital': 'Florianópolis'
    },
    'SP': {
        'nome': 'São Paulo',
        'capital': 'São Paulo'
    },
    'SE': {
        'nome': 'Sergipe',
        'capital': 'Aracaju'
    },
    'TO': {
        'nome': 'Tocantins',
        'capital': 'Palmas'
    }
}

def montarxml(root, id, state, sigla, cidade):
    estado = ET.SubElement(root, 'ESTADO')
    idd = ET.SubElement(estado, 'ID')
    idd.text = id
    nome = ET.SubElement(estado, 'NOME')
    nome.text = state
    sigla_ = ET.SubElement(estado, 'SIGLA')
    sigla_.text = sigla
    capital = ET.SubElement(estado, 'CAPITAL')
    capital.text = cidade


    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

    with open("estado.xml", "w") as f:
            f.write(xmlstr)

root = ET.Element('ESTADOS')
id = 0
for sigla, valor in brasil_capitais.items():
    estado = valor['nome']
    capital = valor['capital']
    id += 1
    montarxml(root, str(id), estado, sigla, capital)

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

with open("estados2.xml", "w") as f:
    f.write(xmlstr)