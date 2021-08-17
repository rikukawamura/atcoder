def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import heapq
from itertools import accumulate

Q = int(input())
q = []
heapq.heapify(q)
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

i = 0
acc_time = 0
for x in X:
    #pdb.set_trace()
    if x[0] == 1:
        heapq.heappush(q, (x[1]-acc_time, i)) # 投入時の値と投入時の時間を保持
    elif x[0] == 2:
        acc_time += x[1]
    else:
        value, input_time = heapq.heappop(q)
        print(value+acc_time)
    i += 1


