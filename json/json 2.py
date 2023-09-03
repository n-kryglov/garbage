import json

with open(r'C:\Users\user\Downloads\data.json', encoding='utf-8') as file, open(r'C:\Users\user\Downloads\updated_data.json', 'w', encoding='utf-8', newline='') as out:
    res = []
    js = json.load(file)
    for ob in js:
        if isinstance(ob, str) == True:
            tmp = ob + '!'
            res.append(tmp)
        elif isinstance(ob, bool) == True:
            tmp = not ob
            res.append(tmp)
        elif isinstance(ob, int) == True:
            tmp = ob + 1
            res.append(tmp)
        elif isinstance(ob, list) == True:
            tmp = ob * 2
            res.append(tmp)
        elif isinstance(ob, dict) == True:
            ob["newkey"] = None
            res.append(ob)
    json.dump(res, out)