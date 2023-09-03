import json, csv

with open(r'C:\Users\user\Downloads\students.json', encoding='utf-8') as students, open(r'C:\Users\user\Downloads\data.csv', 'w', encoding='utf-8', newline='') as out_data:
    file = json.load(students)
    base = []
    columns = ['name', 'phone']
    for item in file:
        if item['age'] > 17 and item['progress'] > 74:
            d = {'name': item['name'], 'phone': item['phone']}
            base.append(d)
    base = sorted(base, key= lambda x: x['name'])
    writer = csv.DictWriter(out_data, fieldnames=columns, delimiter=',')
    writer.writeheader()
    for row in base:
        writer.writerow(row)