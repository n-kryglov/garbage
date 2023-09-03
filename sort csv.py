import csv
from datetime import datetime
from collections import defaultdict

data = defaultdict()

for func in reversed([list, int, dict, set]):
    data.default_factory = func

print(data['key'])
print(data)
pat_date = '%d.%m.%Y %H:%M'
#with open('meetings.csv', encoding='utf-8') as file:
#    meet = list(csv.DictReader(file))
#    print(meet)
#    r = sorted(meet, key=lambda x: (datetime.strptime((x['meeting_date']+' '+x['meeting_time']), pat_date)))
#    for i in r:
#       print(i['surname'], i['name'])