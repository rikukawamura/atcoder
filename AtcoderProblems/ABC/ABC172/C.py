import pdb
from itertools import accumulate
from bisect import bisect_right

N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

acc_A = [0] + list(accumulate(A))
acc_B = list(accumulate(B))

total = 0
for num_a in range(len(acc_A)):
    rem = K - acc_A[num_a]
    if rem < 0:
        break
    num_b = bisect_right(acc_B, rem)
    total = max(total, num_a + num_b)

print(total)


