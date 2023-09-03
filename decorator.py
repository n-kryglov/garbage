# def sandwich(func):
#     def wrap(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         r = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return r
#     return wrap
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
# t = ['томат', 'салат', 'сыр', 'бекон']
# add_ingredients(t)


# def new_print(func):
#     def wrap(*args, **kwargs):
#         a = []
#         kw = {}
#         for i in args:
#             if isinstance(i, str) == True:
#                 a.append(i.upper())
#             else:
#                 a.append(i)
#         for k, v in kwargs.items():
#             if isinstance(v, str) == True:
#                 kw[k] = v.upper()
#             else:
#                 kw[k] = v
#         r = func(*a, **kw)
#         return r
#     return wrap
#
#
# print = new_print(print)
#
# print(111, 222, 333, sep='xxx')

# class TypeError(Exception):
#     pass
# class ValueError(Exception):
#     pass
#
# def takes_positive(func):
#     def wrap(*args, **kwargs):
#         try:
#             k = True
#             if all([type(x) is int for x in args]) == False:
#                 raise TypeError
#             if all([type(kwargs[x]) is int for x in kwargs]) == False:
#                 raise TypeError
#             if any([x <= 0 for x in args]) == True:
#                 raise ValueError
#             for x in kwargs.values():
#                 if x <= 0:
#                     raise ValueError
#             #if all([kwargs[x] <= 0 for x in kwargs]) == True:
#                 raise ValueError
#             r = func(*args, **kwargs)
#             return r
#         except TypeError:
#             return "<class 'TypeError'>"
#         except ValueError:
#             return "<class 'ValueError'>"
#     return wrap
#
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# import functools
# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             r = func(*args, **kwargs)
#             if isinstance(r, str) == False:
#                 raise TypeError
#             return r
#         except:
#             raise TypeError
#     return wrapper
#
# @returns_string
# def nothing():
#     return
#
# print(nothing.__name__)
# print(nothing.__doc__)
#
# try:
#     nothing()
# except TypeError as e:
#     print(type(e))

# import functools
# def prefix(string, to_the_end=False):
#     def foo(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if to_the_end:
#                 return func(*args, **kwargs) + string
#             else:
#                 return string + func(*args, **kwargs)
#         return wrapper
#     return foo
#
#
# @prefix('€')
# def get_bonus():
#     return '2000'

# print(get_bonus())


# import functools
# class MaxRetriesException(Exception):
#     pass
#
# def retry(times):
#     def repeat(func):
#         @functools.wraps(func)
#         def wrap(*args, **kwargs):
#             for i in range(times):
#                 try:
#                     r = func(*args, **kwargs)
#                     return r
#                 except Exception as e:
#                     pass
#             raise MaxRetriesException
#         return wrap
#     return repeat
#
# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
# beegeek()

# from functools import partial
# def add(a,b):
#     return a*b
#
# add_two = partial(add, 2)
#
# print(add_two('5'))

# from functools import partial, update_wrapper
#
# beegeek = partial(print, sep=', ')
#
# beegeek('beegeek', 'stepik', 'python', sep='-')

from functools import lru_cache

# @lru_cache
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(127))
# print(fibonacci.cache_info())
# from functools import lru_cache
#
#
# @lru_cache()
# def add_one(number):
#     print(number + 1, end=' ')
#
#
# numbers = [1, 2, 3, 1, 3, 4, 4, 1]

# for i in numbers:
#     add_one(i)

# for i in zip('bee', 'geek'):
#     print(i)

# x = map(print, ('bee', 'gee'))
#
# for i in x:
#     i

# def transpose(matrix: list):
#     x = [[i1, i2, i3] for i1, i2, i3 in zip(*matrix)]
#     print(x)
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for row in transpose(matrix):
#     print(row)
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    del numbers[0]
    print(i)



















