# class Square:
#     def __init__(self, num):
#         self.num = num
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i <= self.num:
#             self.i += 1
#             return self.i ** 2
#         raise StopIteration
#
# # squares = Square(2)
# #
# # print(next(squares))
# # print(next(squares))
#
# squares = Square(10)
#
# print(list(squares))
import datetime
# class Fibonacci:
#     def __init__(self):
#         self.f = 1
#         self.t = 1
#         self.a = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a < 2:
#             self.a += 1
#             return 1
#         else:
#             self.a = self.f + self.t
#             self.f = self.t
#             self.t = self.a
#             return self.a
#
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))

#import random
#
# class CardDeck:
#     def __init__(self):
#         self.m = [('2', 'пик'), ('3', 'пик'), ('4', 'пик'), ('5', 'пик'), ('6', 'пик'), ('7', 'пик'), ('8', 'пик'),
#                   ('9', 'пик'), ('10', 'пик'), ('валет', 'пик'), ('дама', 'пик'), ('король', 'пик'), ('туз', 'пик'),
#                   ('2', 'треф'), ('3', 'треф'), ('4', 'треф'), ('5', 'треф'), ('6', 'треф'), ('7', 'треф'),
#                   ('8', 'треф'), ('9', 'треф'), ('10', 'треф'), ('валет', 'треф'), ('дама', 'треф'), ('король', 'треф'),
#                   ('туз', 'треф'), ('2', 'бубен'), ('3', 'бубен'), ('4', 'бубен'), ('5', 'бубен'), ('6', 'бубен'),
#                   ('7', 'бубен'), ('8', 'бубен'), ('9', 'бубен'), ('10', 'бубен'), ('валет', 'бубен'),
#                   ('дама', 'бубен'), ('король', 'бубен'), ('туз', 'бубен'), ('2', 'червей'), ('3', 'червей'),
#                   ('4', 'червей'), ('5', 'червей'), ('6', 'червей'), ('7', 'червей'), ('8', 'червей'), ('9', 'червей'),
#                   ('10', 'червей'), ('валет', 'червей'), ('дама', 'червей'), ('король', 'червей'), ('туз', 'червей')]
#         #random.shuffle(self.m)
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.m:
#             a = list(self.m.pop(0))
#             return ' '.join(a)
#         raise StopIteration
#
#
# cards = CardDeck()
#
# print(next(cards))
# print(next(cards))

# def generate_ints(n):
#     for num in range(n):
#         yield num
# generator1 = generate_ints(5)           # создаем генератор, порождающий числа 0 1 2 3 4
#
# print(type(generator1))
#
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))


# from datetime import date, timedelta
# def dates(start: date, count=None):
#     try:
#         if count is None:
#             while True:
#                 yield start
#                 #start = start.replace(year=start.year, month=start.month, day= start.day+1)
#                 start = start + timedelta(days=1)
#         else:
#             for i in range(count):
#                 yield start
#                 #start = start.replace(year=start.year, month=start.month, day=start.day + 1)
#                 start = start + timedelta(days=1)
#     except StopIteration:
#         return
#     except OverflowError:
#         return
# generator = dates(date(9999, 1, 7))
#
# for _ in range(348):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# try:
#     print(next(generator))
# except StopIteration:
#     print('Error')


# from collections import namedtuple
#
# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
#
# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
# males = (item for item in persons if item[2] == 'male' and item[4] == 0 and item[1] == 'Swedish')
# age = max(males, key=lambda x: x[3])
# print(age[0])

# import csv
# with open('data2.csv', 'r', encoding='utf-8') as data:
#     file = (line.strip() for line in data.readlines())
#     file2 = (item.split(',') for item in file)
#     file3 = (int(el[1]) for el in file2 if el[2] == 'a')
#     print(sum(file3))


# import calendar
# from datetime import date, timedelta
# def years_days(years: int):
#     start = date(year=years, month=1, day=1)
#     if calendar.isleap(years):
#         yield from (start + timedelta(days=i) for i in range(1, 365))
#     else:
#         yield from (start + timedelta(days=i) for i in range(1, 366))
#     # for i in range(370):
#     #     yield start + timedelta(days=i)
#     #     print((start + timedelta(days=i)).year)
# dates = years_days(2013)
#
# print(*dates, sep='\n')

# def txt_to_dict():
#     with open('planets.txt', encoding='utf-8') as p:
#         file = (line.split('\n') for line in p.read().split('\n\n'))
#         block = {}
#         for item in file:
#             for el in item:
#                 k, v = el.split(' = ')
#                 block[k] = v
#             yield block
#             block = {}
#
#
# planets = txt_to_dict()
#
# print(next(planets))

# def pairwise(itr):
#     p = None
#     l = ''
#     for i in itr:
#         l = i
#         if p == None:
#             p = i
#             continue
#         yield p, i
#         p = i
#     yield l, None
#
# iterator = iter('stepik')
#
# print(*pairwise(iterator))

# def around(itr):
#     pre = None
#     l = ''
#     c = 0
#     for i in itr:
#         if c < 1:
#             l = i
#             c += 1
#             continue
#         if c == 1:
#             c += 1
#             yield pre, l, i
#             pre = l
#             l = i
#             continue
#         yield pre, l, i
#         pre = l
#         l = i
#         c += 1
#     if l:
#         yield l, i, None
#
# iterator = iter('hey')
#
# print(*around(iterator))

# def around(itr):
#     itr = list(itr)
#     pre1 = [None] + itr
#     par1 = itr[1:] + [None]
#     for pre, cur, par in zip(pre1, itr,par1):
#         yield pre, cur, par
#
# iterator = iter('hey')
#
# print(*around(iterator))
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*around(numbers))

# def find_outlier(integers):
#     even = all(i % 2 == 0 for i in integers[:5])
#     if even:
#         r = (i for i in integers if i % 2 != 0)
#     else:
#         r = (i for i in integers if i % 2 != 0)
#     return next(r)
#
# print(find_outlier([6654808, 410360, -8002620, -2879353, 2032916, -2589408, -1624502, -1679510, 3456632, -9326372, -1464754, -2379858, -9207650]))
#
# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)

# import string
# from itertools import cycle
# def alnum_sequence():
#     a = list(string.ascii_uppercase)
#     r = []
#     for i in range(1,27):
#         r.append(i)
#         r.append(a.pop(0))
#     print(r)
#
# alnum_sequence()
#print(*(next(alnum) for _ in range(55)))
# from string import ascii_lowercase
# from itertools import product
#
# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]
#
# s = product(letters, digits)
# for i in s:
#     print(*i, sep='', end=' ')
# stn = 'Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221'
# s = list(map(lambda x: x.strip(',+./!#$%^&*()@:"><=*'), stn.split()))
# for item in s:
#     if item[0] == '7':
#         r = list(map(lambda x: x.strip(), item.split('-')))
#         pr = [r[0]]
#         for i, el in enumerate(r[1:]):
#             if i in range(0, 2):
#                 if len(el) == 3 and all(j.isdigit() for j in el) == True:
#                     pr.append(el)
#             if i in range(2, 4):
#                 if len(el) == 2 and all(j.isdigit() for j in el) == True:
#                     pr.append(el)
#         if len(pr) >= 4:
#             print(('-').join(pr))
#     elif item[0] == '8':
#         r = list(map(lambda x: x.strip(), item.split('-')))
#         pr1 = [r[0]]
#         for i, el in enumerate(r[1:]):
#             if i == 0:
#                 if len(el) == 3 and all(j.isdigit() for j in el) == True:
#                     pr1.append(el)
#             if i in range(1, 3):
#                 if len(el) == 4 and all(j.isdigit() for j in el) == True:
#                     pr1.append(el)
#         if len(pr1) >= 4:
#             print(('-').join(pr1))

























