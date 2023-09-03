import json
import csv
import datetime

with open(r'C:\Users\user\Downloads\exam_results.csv', encoding='utf-8') as exam, open(r'C:\Users\user\Downloads\best_scores.json', 'w', encoding='utf-8', newline='') as best:
    file = csv.DictReader(exam)
    file.fieldnames[2] = 'best_score'
    base = {}
    column = ['name','surname','best_score','date_and_time','email']
    for item in file:
        if item['email'] not in base:
            base[item['email']] = item
        else:
            if int(item['best_score']) > int(base[item['email']]['best_score']):
                base[item['email']] = item
            elif int(item['best_score']) == int(base[item['email']]['best_score']):
                if datetime.datetime.fromisoformat(item['date_and_time']) > datetime.datetime.fromisoformat(base[item['email']]['date_and_time']):
                    base[item['email']] = item
    v = sorted(base.values(), key=lambda x: x['email'])
    for row in v:
        row['best_score'] = int(row['best_score'])
    json.dump(v, best, indent=3)