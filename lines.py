name = 'data.txt'
with open('C:/Users/user/Downloads/'+name, 'r') as file:
    content = [txt.strip('\n') for txt in file.readlines()]
    prom_lis = []
    res = []
    for line in content:
        if line.startswith('def ')==True or line.startswith('# ')==True:
            prom_lis.append(line)
    for ind in range(len(prom_lis)-2,-1,-1):
        if prom_lis[ind].startswith('# ')==True and prom_lis[ind+1].startswith('def ')==True:
            del prom_lis[ind+1]
            del prom_lis[ind]
        else:
            continue
    for item in prom_lis:
        tmp = item.split('(')
        res.append(tmp[0].strip('def '))
    if len(res) == 0:
        print('Best Programming Team')
    else:
        print(*res, sep='\n')