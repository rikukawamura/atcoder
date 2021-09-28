def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
X = input().split('.')
#pdb.set_trace()
if 0 <= int(X[1]) <= 2:
    print(X[0]+'-')
elif 3 <= int(X[1]) <= 6:
    print(X[0])
else:
    print(X[0]+'+')
