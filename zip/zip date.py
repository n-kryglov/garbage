from zipfile import ZipFile
from datetime import datetime
p = datetime(2021,11,30,14,22,00)
b = []
with ZipFile('workbook.zip') as file:
    for name in file.infolist():
        if name.is_dir() == False:
            d = datetime(*name.date_time)
            if d > p:
                n = name.filename.split('/')[-1]
                b.append(n)
    print(*sorted(b), sep='\n')