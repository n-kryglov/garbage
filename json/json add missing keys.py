import json

with open(r'C:\Users\user\Downloads\people.json', encoding='utf-8') as people, open(r'C:\Users\user\Downloads\updated_people.json', 'w', encoding='utf-8', newline='') as up_people:
    file = json.load(people)
    sample = (max(file, key=lambda x: len(x))).keys()
    for item in sample:
        for dic in file:
            if item not in dic:
                dic[item] = None
            else:
                continue
    json.dump(file, up_people)