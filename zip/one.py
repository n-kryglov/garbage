from zipfile import ZipFile
with ZipFile('workbook.zip') as file:
    n = ''
    c = 1
    for name in file.infolist():
        if name.is_dir() == False:
            t = int(name.compress_size) / int(name.file_size)
            if t < c:
                c = t
                n = name.filename.split('/')[-1]

    print(n)