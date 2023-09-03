def trans_to_bytes(size: int, format: str):
    """перевод размера файла в байты"""
    size_bytes = int(size) * base_format[format.upper()]
    return size_bytes

def trans_to_rsize(size: int):
    """перевод размера файла из байт в удобное для понимания значение"""
    count_div = 0
    while size > 1024:
        count_div += 1
        size = round(size / 1024)
    rsize = str(size) + ' ' + base_format[count_div]
    return rsize


base_format = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3, 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
base_files = {}
with open('C:/Users/user/Downloads/files.txt', encoding='utf-8') as file, open('C:/Users/user/Downloads/output.txt',
                                                                               'w', encoding='utf-8') as output_file:
    for line in file:
        full_name, size, unit = line.split()
        name, format = full_name.split('.')
        size_bytes = trans_to_bytes(size, unit)
        item = full_name, size_bytes
        base_files[format] = base_files.setdefault(format, list()) + [item]
    for group in sorted(base_files):
        list_gr = base_files[group]
        count_size = 0
        for name, size in sorted(list_gr):
            print(name, file=output_file)
            count_size += size
        print('-' * 10, file=output_file)
        print('Summary:', trans_to_rsize(count_size), file=output_file)
        print(file=output_file)
