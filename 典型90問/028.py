def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import accumulate

N = int(input())
roop = 10**3+1
papers = [[0] * (roop) for _ in range(roop)]
output = [0]*(N+1) # 重なっている紙の枚数を記録

for _ in range(N):
    lx, ly, rx, ry = int_sp()
    yoko = rx-lx
    tate = ry-ly
    papers[ly][lx] += 1
    papers[ry][rx] += 1
    papers[ly][lx + yoko] += -1
    papers[ry][rx - yoko] += -1

# x軸方向の累積和
for i in range(roop):
    papers[i] = list(accumulate(papers[i]))

# y軸方向の累積和
papers = list(map(list, (zip(*papers))))
for i in range(roop):
    papers[i] = list(accumulate(papers[i]))

# 元に戻す
papers = list(map(list, (zip(*papers))))

# 重なりを見ていく
for i in papers:
    for j in i:
        output[j] += 1

# 重なり(k = 1,2,3,...,N)なのでoutput[1:]
for i in output[1:]:
    print(i)