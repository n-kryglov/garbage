import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

with open('contries.json', 'w') as file:
    json.dump(data, file)