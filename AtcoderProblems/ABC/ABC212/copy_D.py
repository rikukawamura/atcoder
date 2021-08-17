def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import queue
from itertools import accumulate

Q = int(input())
q = queue.Queue()
X = [li_int_sp() for _ in range(Q)]
#limit = 10
limit = 2*(10**5)+1

add_time = [0]*(limit)
i = 0
for x in X:
    if x[0] == 2:
        add_time[i] = x[1]
    i+=1
acc_add_time = list(accumulate(add_time))
#pdb.set_trace()

i = 0
for x in X:
    if x[0] == 1:
        q.put((x[1]+, i)) # 投入時の値と投入時の時間を保持
    elif x[0] == 2:
        acc_cnt = X[1]
    else:
        value, input_time = q.get()
        print(value+acc_add_time[i]-acc_add_time[input_time])
    i += 1


