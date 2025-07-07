
from pathlib import Path
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN  = PASTA_ORIGINAIS / 'relatorio1.pdf'

reader = PdfReader(RELATORIO_BACEN)
print(len(reader.pages))

page0 = reader.pages[0]
imagem0 = page0.images[0]

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
