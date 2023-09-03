from datetime import date
start = date(year=1, month=1, day=13)
res = {}
for year in range(1,10000):
    for mon in range(1,13):
        item = start.replace(year=year, month=mon)
        day = item.weekday()
        res[day] = res.get(day,0) + 1

for key, value in sorted(res.items()):
    print(value)
