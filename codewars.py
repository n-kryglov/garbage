# def find_outlier(integers):
#     even = all(i % 2 == 0 for i in integers[:5])
#     if even:
#         r = (i for i in integers if i % 2 != 0)
#     else:
#         r = (i for i in integers if i % 2 != 0)
#     return next(r)
#
# print(find_outlier([6654808, 410360, -8002620, -2879353, 2032916, -2589408, -1624502, -1679510, 3456632, -9326372, -1464754, -2379858, -9207650]))


# def sort_array(source_array):
#     x = sorted([x for x in source_array if x % 2 != 0])
#     r = []
#     for item in source_array:
#         if item % 2 != 0:
#             r.append(x.pop(0))
#         else:
#             r.append(item)
#     return r
# print(sort_array([5, 3, 2, 8, 1, 4]))


# def make_readable(seconds):
#     h = seconds // 3600
#     m = (seconds - h*3600) // 60
#     s = (seconds - h*3600) % 60
#     return f'{str(h).rjust(2, "0")}:{str(m).rjust(2, "0")}:{str(s).rjust(2, "0")}'
# print(make_readable(359999))

def mango(quantity, price):
    if quantity < 3:
        return price * quantity
    else:
        i = 0
        c = quantity
        while c > 0:
            c -= 3
            i += 1
        return i * 2 * price


print(mango(9, 5))

































