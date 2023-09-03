c = 0
for i in range(1000,10000):
    tmp = str(i)
    if int(tmp[0])+int(tmp[1])+int(tmp[2])+int(tmp[3]) == 20:
        c += i
print(c)