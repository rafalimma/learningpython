from pathlib import Path
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

workbook = Workbook()

workbook.create_sheet('RAFA', 0) # mudar ordem do nome da planilha
worksheet: Worksheet = workbook['RAFA']

