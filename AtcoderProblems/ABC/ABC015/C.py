def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, K = int_sp()
T = []
for _ in range(N):
    T.append(li_int_sp())

if N == 1:
    for i in T[0]:
        if i == 0:
            print('Found')
            exit()

elif N == 2:
    for i in T[0]:
        for j in T[1]:
            if i ^ j == 0:
                print('Found')
                exit()
elif N == 3:
    for i in T[0]:
        for j in T[1]:
            for k in T[2]:
                if i ^ j ^ k == 0:
                    print('Found')
                    exit()
elif N == 4:
    for i in T[0]:
        for j in T[1]:
            for k in T[2]:
                for l in T[3]:
                    if i ^ j ^ k ^ l == 0:
                        print('Found')
                        exit()

elif N == 5:
    for i in T[0]:
        for j in T[1]:
            for k in T[2]:
                for l in T[3]:
                    for n in T[4]:
                        if i ^ j ^ k ^ l ^ n == 0:
                            print('Found')
                            exit()
print('Nothing')