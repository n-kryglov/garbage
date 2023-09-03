import json
import csv

with open(r'C:\Users\user\Downloads\playgrounds.csv', encoding='utf-8') as ground, open(r'C:\Users\user\Downloads\addresses.json', 'w', encoding='utf-8', newline='') as out:
    file = list(csv.reader(ground, delimiter=';'))
    del file[0]
    base = {}
    for item in file:
        obj, adm_area, district, address = item
        if adm_area not in base:
            base[adm_area] = {}
            if district not in base[adm_area]:
                base[adm_area][district] = list()
                base[adm_area][district] = base[adm_area][district] + [address]
            else:
                base[adm_area][district] = base[adm_area][district] + [address]
        else:
            if district not in base[adm_area]:
                base[adm_area][district] = list()
                base[adm_area][district] = base[adm_area][district] + [address]
            else:
                base[adm_area][district] = base[adm_area][district] + [address]
    json.dump(base, out, indent=3, ensure_ascii=False)