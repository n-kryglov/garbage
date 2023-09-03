import json

with open(r'C:\Users\user\Downloads\pools.json', encoding='utf-8') as pools:
    file = json.load(pools)
    l, w = 0, 0
    add = ''
    for item in file:
        sched = item['WorkingHoursSummer']['Понедельник']
        if int(sched[:2]) <= 10 and int(sched[3:5]) == 0 and int(sched[6:8]) >= 12:
            tmp = item['DimensionsSummer']
            if int(tmp['Length']) > l:
                l, w, add = int(tmp['Length']), int(tmp['Width']), item['Address']
            elif int(tmp['Length']) == l:
                if int(tmp['Width']) > w:
                    l, w, add = int(tmp['Length']), int(tmp['Width']), item['Address']
    print(f'{l}x{w}', add, sep='\n')
