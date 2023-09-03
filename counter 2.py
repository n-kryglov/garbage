# from collections import Counter
# import csv , json
# base = {}
# prices = ''
# with open('prices.json', encoding='utf-8') as p:
#     prices = json.load(p)
#
# for i in range(1, 5):
#     with open('quarter' + str(i) + '.csv', encoding='utf-8') as file:
#         f = list(csv.DictReader(file))
#         for it in f:
#             g = list(it.values())
#             base[g[0]] = base.get(g[0], 0) + sum(map(int, g[1:]))
# for i in base:
#     base[i] = base.get(i) * prices[i]
# c = Counter(base)
# print(c.total())


# def print_numbers(start=0, end=100):
#     def rec(num):
#         if num <= end:
#             print(num)
#             rec(num + 1)
#     rec(start)
# print_numbers()

# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
#
# def p(numbers):
#     if len(numbers) > 0:
#         i = len(numbers) - 1
#         t = numbers.pop(i)
#         p(numbers)
#         print(f'Элемент {i}: {t}')
# p(numbers)


# def triangle(h=16, i=0, k=1):
#     if h > 0:
#         print(' '*(i),str(k) * h, sep='')
#         triangle(h-4, i+2, k+1)
#     if h > 4:
#         print(' '*(i),str(k) * h, sep='')
#
# triangle()