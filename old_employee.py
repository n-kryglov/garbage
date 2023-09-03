from datetime import datetime
pattern = '%d.%m.%Y'
date_b = {}
for i in range(3):
    name, surname, date = input('Введите:  ').split()
    date = datetime.strptime(date, pattern)
    name = name + ' ' + surname
    date_b[date] = date_b.get(date, []) + [name]
mn = min(date_b)
val = date_b[mn]
if len(val) > 1:
    print(datetime.strftime(mn, pattern), len(val))
else:
    print(*val, datetime.strftime(mn, pattern))
