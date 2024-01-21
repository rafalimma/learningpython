# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime


# data = datetime(2024, 12, 12, 7, 20)
data = datetime.strptime('2024-12-12 07:20', '%Y-%m-%d %H:%M')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%m'), data.minute)


