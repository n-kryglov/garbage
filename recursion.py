# сумма по вложеному списку
# def recursive_sum(base):
#     if len(base) == 0:
#         return 0
#     else:
#         t = 0
#         for item in base:
#             if isinstance(item, list):
#                 t += recursive_sum(item)
#             else:
#                 t += item
#         return t

# вывод вложенного списка в одномерный
# def linear(base, l=None):
#     if l is None:
#         l = []
#     for item in base:
#         if isinstance(item, list):
#             l += linear(item)
#         else:
#             l.append(item)
#     return l
#
#tests
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))


#определяет и возвращает значение по ключу по вложенному словарю
# def get_value(nested_value, key):
#     if key in nested_value:
#         return nested_value[key]
#     else:
#         for item in nested_value.values():
#             if isinstance(item, dict) == True:
#                 ans = get_value(item, key)
#                 if ans == None:
#                     continue
#                 else:
#                     return ans
#
#tests
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
# print(get_value(data, 'cityName'))



#определяет все значения по ключу и возвращает множество
# def get_all_values(nested_value, key):
#     res = set()
#     for item in nested_value:
#         if item == key:
#             ans = nested_value[key]
#             res.add(ans)
#         else:
#             if isinstance(nested_value[item], dict) == True:
#                 ans = dict_travel(nested_value[item])
#                 res.update(ans)
#     return res

#tests
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_value(my_dict, 'top_grade')
#
# print(*sorted(result))
#
# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_value(my_dict, 'hobby')
#
# print(*sorted(result))
# my_dict = {
#            'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
#            'Timur': {'hobby': 'math'},
#            'Dima': {
#                    'hobby': 'CS',
#                    'sister':
#                        {
#                          'name': 'Anna',
#                          'hobby': 'TV',
#                          'age': 14
#                        }
#                    }
#            }
#
# result = get_all_values(my_dict, 'hobby')
# print(*sorted(result))


#выводит в лексикографическом порядке все пары ключ-значение в формате "k.k.k: v"
# def dict_travel(n_value, p=''):
#     for k, v in sorted(n_value.items()):
#         if isinstance(v, dict) == True:
#             dict_travel(v, p+'.'+k)
#         else:
#             print(f'{(p + "." + k)[1:]}: {v}')

#tests
#data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
# data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},'address': {'streetaddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'}, 'postalcode': '125315'}}
# dict_travel(data)

#
# def to_binary(number, a=[]):
#     if number == 0:
#         print(''.join(a[::-1]))
#     else:
#         if number >= 1:
#             r = number % 2
#             a.append(str(1) if r > 0 else str(0))
#             number = number//2
#             return to_binary(number)
#         else:
#             r = number * 2
#             a += str(1) if r >= 1 else str(0)
#             number = r - 1 if r > 1 else r
#             to_binary(number, a)
#
# print(to_binary(15))



# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
# print(min(films, key=lambda x: sum(films[x].values())))


# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
# print(numbers.index(max(numbers)))

#
# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
# r = {n: box - bud for n, bud, box in zip(names, budgets, box_offices)}
# for k in sorted(r):
#     print(f'{k}: {r[k]}$')

# def zip_longest(*args, fill='_'):
#     length = max([len(i) for i in args])
#     for item in args:
#         while len(item) < length:
#             item.append(fill)
#     return[item for item in zip(*args)]
#
#
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))


# r = 'Sorting1234'
# r = sorted(r)
# s = sorted(r, key=lambda x: (-x.islower()==True, x.islower()==False, x.isdigit()==True and int(x) % 2 == 0, x.isdigit()==True and int(x) % 2 != 0))
# print(('').join(s))

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
# r = list(map(int, filter(lambda x: isinstance(x, int) == True or isinstance(x, float) == True, data)))
# print(*r, sep='\n')

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
# r = list(map(lambda x: x[0].upper()+x[1:], filter(lambda x: len(x) > 4 and any([x[0].lower() == 'а', x[0].lower() == 'м']), names)))
# print(*sorted(r))

# from datetime import datetime, date
# def date_formatter(country_code):
#     country = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '$d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
#     pattern = country[country_code]
#     def c_d(date):
#         nonlocal pattern
#         return datetime.strptime(date, pattern)
#     return c_d
#
# date_ru = date_formatter('ru')
# today = date(2022, 1, 25)
# print(date_ru(today))

# import typing
# def top_grade(grades):
#     r = {}
#     r['name'] = grades['name']
#     m = max(grades['grades'])
#     r['top_grade'] = m
#     return r
#
# info = {'name': 'Timur', 'grades': [30, 57, 99]}
#
# print(top_grade(info))


# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     if step > 0:
#         for i in range(step):
#             numbers.insert(0, numbers.pop(-1))
#     else:
#         step %= len(numbers)
#         for i in range(step):
#             numbers.insert(0, numbers.pop(-1))
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, -2)
#
# print(numbers)


# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     r = {i: matrix for i, matrix in enumerate(matrix, 1)}
#     return r
# matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
#
# print(*matrix_to_dict.__annotations__.values())









