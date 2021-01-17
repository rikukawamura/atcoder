N = int(input())

strings = []
for i in range(N):
    strings.append(input())
strings = set(strings)

flag = False
for j in strings:
    if j[-1] != '!':
        if ('!' + j) in strings:
            print(j)
            flag = True
            break
    elif j[-1] == '!':
        if j[1:] in strings:
            print(j[1:])
            flag = True
            break

if not flag:
    print('satisfiable')















'''
N = int(input())

strings = []
for i in range(N):
    strings.append(input())

flag = False
for j in strings:
    for k in strings:
        if j[-1] != '!':
            if ('!' + j) in k:
                print(j)
                flag = True
                break
        elif j[-1] == '!':
            if j[1:] in k:
                print(j[1:])
                flag = True
                break
    if flag:
        break

if not flag:
    print('satisfiable')
'''