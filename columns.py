import csv

def csv_columns(filename: str):
    with open(r''+filename) as data:
        text = csv.DictReader(data)
        res = {}
        for row in text:
            for key ,item in row.items():
                res[key] = res.get(key, []) + [item]
        return(res)

text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('grades.csv', 'w') as file:
    file.write(text)

print(csv_columns('grades.csv'))
