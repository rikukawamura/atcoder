def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
X = list(input())
while X != []:
    flag = False
    pdb.set_trace()
    if X[:2] == ['c', 'h']:
        del X[0]
        del X[1]
        flag = True
    elif X[0] == ['o']:
        del X[0]
        flag = True
    elif X[0] == ['k']:
        del X[0]
        flag = True
    elif X[0] == ['u']:
        del X[0]
        flag = True
    if not flag:
        break
print(X)