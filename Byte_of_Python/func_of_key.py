def printMax(x, y):
    '''Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
printMax(4,8)
print(printMax.__doc__)