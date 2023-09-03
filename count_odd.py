from datetime import datetime, timedelta
s_date = datetime.strptime(input('Введите начальную дату:  '), '%d.%m.%Y')
while (s_date.day + s_date.month) % 2 == 0:
    s_date = s_date + timedelta(days=1)
s_date = s_date.toordinal()
f_date = datetime.strptime(input('Введите конечную дату:  '), '%d.%m.%Y').toordinal()
for date in range(s_date, f_date+1, 3):
    date = datetime.fromordinal(date)
    if date.weekday() != 0 and date.weekday() != 3:
        print(datetime.strftime(date, '%d.%m.%Y'))