import pdb
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
A += [N+1]
A += [0]
A = sorted(A, reverse=True)
white = sorted([A[i] - A[i+1] - 1 for i in range(M+1)])
sort_white = sorted(list(set(white)))
if white == []:
    print(1)
    exit()
# 0しか要素がない
elif sort_white[0] == 0 and len(sort_white) == 1:
    print(0)
    exit()
else:
    if sort_white[0] != 0:
        min_white = sort_white[0]
    else:
        min_white = sort_white[1]

num = 0
for i in white:
    num += math.ceil(i/min_white)

print(num)