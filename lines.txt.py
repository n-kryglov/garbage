with open('C:\Users\user\Downloads\lines.txt') as file:
    tmp = file.readlines()
    mx = max(tmp)
    for w in tmp:
        if len(w) == mx:
            print(w.strip())