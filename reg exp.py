# lst = ['good morning everyone', 'i am going to school', 'and it is raining', 'hi, beegeek',
# 'beegeek is an awesome place for programmers',
# 'beegeek rocks, rocks beegeek',
# 'i think beegeek is a great place to hangout']
import sys
from re import fullmatch, search
# ful = r'^(beegeek).*\1$'
# beg = r'^(beegeek)'
# end = r'(beegeek)$'
#lst = [txt.strip() for txt in sys.stdin]
# c = 0
# for item in lst:
#     _1 = search(r'beegeek', item)
#     _2 = fullmatch(ful, item)
#     _3 = search(beg, item)
#     _4 = search(end, item)
#     if _1 is not None:
#         if fullmatch(ful, item) is not None:
#             c += 3
#             continue
#         elif search(beg, item) is not None or search(end, item) is not None:
#             c += 2
#             continue
#         else:
#             c += 1
#     else:
#         continue
# print(c)

# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!
#
# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...
#
# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью.
#
# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!
#
# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...
#
# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''
#
# import re
# st = '^stepik'
# end = '(\.\.\.|!)$'
# st1 = re.findall(st, article, flags=re.I | re.M)
# end1 = re.findall(end, article, flags=re.I | re.M)
# print(len(st1))
# print(len(end1))

# import re
# txt = 'existing pessimist optimist this is'
# word = f'\w+{input()}\w+'
# c = re.findall(word, txt)
# print(c)


# html = ['<a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">', '<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>']
# import re
# str_tag = r'(<>?.*?>)'
# tag = r'<(\w+)>?'
# atr = r'\b([\w-]+)='
# d = {}
# for line in html:
#     find_tags = re.findall(str_tag, line)
#     for item in find_tags:
#         t = re.findall(tag, item)
#         if t != []:
#             a = re.findall(atr,item)
#             d[t[0]] = d.get(t[0], []) + a
#
# for i in sorted(d):
#     v = set(d[i])
#     v = ', '.join(sorted(v))
#     print(f'{i}: {v}')

# import re
# def change(string):
#     string = string.group()
#     if len(string) >= 2:
#         r = string[1]+string[0]+string[2:]
#         return r
#     else:
#         return string
# st = input('vvod')
# r2 = re.sub(r'\b(\w+)\b', change, st)
# print(r2)

# import re
# def mult(stg):
#     #print(stg.group(1), stg.group(2))
#     r = int(stg.group(1)) * stg.group(2)
#     print(r)
#     return r
# text = input('1: ')
# pat = r'(\d+)\((\w+)\)'
# ans ='1'
# while any(d.isdigit() for d in text):
#     text = re.sub(pat,mult, text)
# print(text)

# import re
# text = 'Ba-Ba-Ba-Ba-Barbara Ann'
# def change(st):
#     return st.group(1)
#
# pat = r'\b(\w+)(\W|\s)+(\1)'
# while re.search(pat, text) is not None:
#     text = re.sub(pat, change, text)
#     print(text)
# print(text)

import re
# text = [''"""hello everyone
# welcome to my project"""'',
#
# 'import math  # importing a useful math module',
#
# '# let\'s take a look at some functions',
#
# 'def circle_area(radius):',
#     """coming soon""",
#     'return math.pi * r ** 2  # my favorite formula',
#
# 'def triangle_area(base, height):',
#     """the function takes
#     the base and height
#     of a triangle and
#     returns its area""",
#     'return 0.5 * base * height']
#
# p_1_line = r'#.*\n'
# p_aline = r'#.+'

# import re
# f,i,o = input('1').split()
# s = input('2')
# rep = 'ФИО'
# f = f[:-2]
# i = i[:-2]
# o = o[:-2]
# print(f,i[0],o[0])
# pat = fr'{f}[а-я]+ {i[0]}[\.а-я]+ {o[0]}[\.а-я]+'
#
# r = re.sub(pat, rep, s)
# print(r)

# import re
# # Полная ссылка: https://example.com/test/42523/step/2?q=query&s=search#test
# # Протокол: https | Домен: example.com | Параметры: ?q=query&s=search | Якорь: #test
#
# p = r'\b(https?://[a-z.]+/[a-z0-9-_/]*[a-z=&0-9?]*[#a-z]*) ?\b'
# p2 = r'\b(?P<prot>https?)://(?P<domen>[a-z\.]*)[/.*=/\w]*(?P<param>\?[a-z\=\&\d]*)?(?P<anker>\#[a-z]+)? ?\b'
#
# s = '''В этом https://stepik.org/lesson/704265/step/2?unit=704697#test тексте https://example.com/ очень много
# https://keep.google.com/#home разных http://oldastoundingrelaxedlaugh.neverssl.com/online ссылок.
# Наступаешь на одни и те же грабли: https://vk.com/video-460389_160321403
# https://pikabu.ru/story/vse_schitayut_sebya_unikalnyimi_poka_ne_prikhoditsya_pokupat_domen_dlya_svoego_startapa_9132005#comments
# https://www.google.com/search?q=query https://yandex.ru/search/?lr=16&text=query
# https://www.google+com/ https://www.google?com/ https://www.google#com/'''
#
# r1 = re.findall(p, s)
# for link in r1:
#     print(f'Полная ссылка: {link}')
#     r2 = re.match(p2, link).groupdict()
#     print(f"Протокол: {r2['prot']} | Домен: {r2['domen']} | Параметры: {r2['param']} | Якорь: {r2['anker']}")
#     print()
import re
pattern = re.compile("^python", flags=re.IGNORECASE | re.MULTILINE)
print(pattern.search("Python is a programming language.\nPython is also a snake."))


























