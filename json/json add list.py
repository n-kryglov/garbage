import json

with open(r'C:\Users\user\Downloads\countries.json', encoding='utf-8') as countr, open(r'C:\Users\user\Downloads\religion.json', 'w', encoding='utf-8', newline='') as religion:
    file = json.load(countr)
    record = {}
    for item in file:
        count, relig = item.values()
        record[relig] = record.get(relig, []) + [count]
    json.dump(record, religion)