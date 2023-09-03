from zipfile import ZipFile
from datetime import datetime
b = {}
with ZipFile('workbook.zip') as file:
    for name in file.infolist():
        if name.is_dir() == False:
            n = name.filename.split('/')[-1]
            b[n] = {'Дата модификации файла:': datetime(*name.date_time),'Объем исходного файла:': str(name.file_size) + ' байт(а)', 'Объем сжатого файла:': str(name.compress_size) +' байт(а)'}
    for k in sorted(b):
        print(k)
        for kk, v in b[k].items():
            print(' ',kk, v)
        print()