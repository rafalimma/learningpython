from pathlib import Path
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN  = PASTA_ORIGINAIS / 'relatorio1.pdf'

files = [
    PASTA_NOVA / f'page1.pdf',
    PASTA_NOVA / f'page0.pdf',
]
merger = PdfMerger()
for file in files:
    merger.append(files)

merger.write(PASTA_NOVA / 'MERGE.pdf')
merger.close()