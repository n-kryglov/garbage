from datetime import datetime
with open('C:/Users/user/Downloads/diary.txt', encoding='utf-8') as file, open('C:/Users/user/Downloads/diary_sort.txt',
                                                                               'w', encoding='utf-8') as output_file:
    dates = {}
    text = ''
    for line in file:
        try:
            date = datetime.strptime(line, '%d.%m.%Y; %H:%M\n')
        except:
            if line != '\n':
                tmp = line[-1:]
                if tmp != '\n' and len(line)>2:
                    line += '\n'
                dates[date] = dates.setdefault(date, '') + line
    for item in sorted(dates):
        print(item.strftime('%d.%m.%Y; %H:%M'), file=output_file)
        print(dates[item], file=output_file)