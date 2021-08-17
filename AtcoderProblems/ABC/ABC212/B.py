def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import Counter
mod = 10
indexs = [0,1,2,3,4,5,6,7,8,9]
X = list(map(int, list(input())))
pre = indexs.index(int(X[0]))
X_counter = Counter(X)
if len(X_counter) == 1:
    print('Weak')
    exit()

flag = True
for next in X[1:4]:
    #pdb.set_trace()
    next_index = indexs.index(next)
    if (pre+1)%mod != next_index:
        flag = False
        break
    pre = next_index
if not flag:
    print('Strong')
else:
    print('Weak')
