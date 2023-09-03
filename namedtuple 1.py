import pickle
from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as file:
    l = pickle.load(file)
    for i in l:
        for k, v in zip(Animal._fields, i):
            print(f'{k}: {v}')
        print()