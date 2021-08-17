def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
import heapq
N = int(input())
S = li_int_sp()
T = li_int_sp()

q=[]
heapq.heapify(q)
get_enough = [False]*N # i番目の人が宝石を受け取ったかを管理
min_time = [-1]*N # i番目の人が宝石を受け取るまでの最短時間を管理

# 高橋君から貰う時間をとりあえず格納
for i, t in enumerate(T):
    heapq.heappush(q, (t, i))

while len(q) != 0:
    #pdb.set_trace()
    time, ind = heapq.heappop(q)
    if get_enough[ind] == True:
        continue
    min_time[ind] = time
    get_enough[ind] = True
    heapq.heappush(q, (time+S[ind], (ind+1)%N))
#pdb.set_trace()
for i in min_time:
    print(i)






