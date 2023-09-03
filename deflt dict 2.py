#from collections import defaultdict
#сортировка по отделам/алфавиту
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]
# res = defaultdict(set)
# for i in staff_broken:
#     res[i[0]].add(i[1])
# for c in sorted(res):
#     print(f'{c}: {(", ").join(sorted(res[c]))}')
import sys
# обмен ключ/значение в словаре
# def flip_dict(dict_of_lists: dict):
#     res = defaultdict(list)
#     for k, v in dict_of_lists.items():
#         for i in v:
#             res[i].append(k)
#     return res
#
# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

#подсчет слов
# def best_sender(mes: list, sen: list):
#     res = defaultdict(int)
#     for m, s in zip(mes, sen):
#         res[s] += len(m.split())
#     print(res)
#     return max(res, key=lambda x: (res[x], x))
#
# messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
# senders = ['Bob', 'Charlie']
#
# print(best_sender(messages, senders))

#переворот словаря
# from collections import OrderedDict
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# for n in list(data.keys()):
#     data.move_to_end(n, last=False)
# print(data)
#
from collections import Counter
# s = 'Арбуз Малина арбуЗ Клубника арбуз банан малина черешня вишня арбуз клубника Банан'
# t = Counter([i.lower() for i in s.split()])
# f = list(map(lambda y: y[0], filter(lambda x: x[1] == max(t.values()), t.items())))
# print(max(f))



# s = 'Любимой песни слог Знакомый ритм слов Панацея от всего'
# t = Counter([len(i) for i in s.split()])
# for i in sorted(t.items(), key=lambda x: x[1]):
#     print(f'Слов длины {i[0]}: {i[1]}')

# s = ['Тимур 100', 'Анри 88', 'Дима 94', 'Артур 82', 'Владимир 90']
# r = Counter()
# for l in s: #sys.stdin:
#     b = l.split()
#     r.update(Counter({b[0]: int(b[1])}))
#
# print(r.most_common()[-2][0])

# witcher_inventory = Counter(doppler_trophy=1, alcohest=10, mahakaman_spirit=10,
#                             siren_vocal_cords=3, ghouls_blood=4)
#
# losses = dict(ducat=10, alcohest=20, mahakaman_spirit=5, ghouls_blood=4)
#
# witcher_inventory.subtract(losses)
#
# print(witcher_inventory)
# letters = Counter(s=0, b=1, e=4, t=-2, g=2, k=1)
#
# print(*letters.elements())
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# data = Counter(map(lambda x: x.split('.')[1], files))
# for k in sorted(data):
#     print(f'{k}: {data[k]}')

# d = 'лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви'
# d = Counter(d.split(','))
# p = {i: sum([ord(j) for j in i]) for i in d}
# w = max([len(x) for x in d.keys()])
# for k in sorted(d):
#     print(f'{k.ljust(w)}: {p[k]} UC x {d[k]} = {p[k] * d[k]}')

#
# with open('pythonzen.txt', encoding='utf-8') as d:
#     f = Counter([x.strip('\n').lower() for st in d.readlines() for x in st  if x.isalpha() == True])
#     for k in sorted(f):
#         print(f'{k}: {f[k]}')
# from collections import Counter
# import csv
# with open('name_log.csv', encoding='utf-8') as file:
#     f = list(csv.DictReader(file))
#     c = Counter([d['email'] for d in f])
#     for k in sorted(c):
#         print(f'{k}: {c[k]}')

# def scrabble(symbols: str, word:str):
#     word = word.lower()
#     symbols = symbols.lower()
#     w = Counter(word)
#     sym = Counter(symbols)
#     r = w & sym
#     return True if (w - r) == Counter() else False

# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# print(scrabble('begk', 'beegeek'))
# print(scrabble('beegeek', 'beegeek'))
