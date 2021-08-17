def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import heapq

N, K = int_sp()
ab = []
b_list = []
for i in range(N):
    a, b = int_sp()
    b_list.append(b)
    ab.append([a, i])
heapq.heapify(ab)

#pdb.set_trace()
total = 0
for _ in range(K):
    tmp = heapq.heappop(ab)
    total += tmp[0]
    tmp[0] += b_list[tmp[1]]
    heapq.heappush(ab, tmp)
print(total)

