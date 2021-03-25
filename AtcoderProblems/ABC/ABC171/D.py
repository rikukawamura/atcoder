import pdb
import collections


N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
Q = int(input())

num = dict(collections.Counter(A))
for _ in range(Q):
    B, C = map(int, input().split())
    try:
        sum_A += (C - B) * num[B]
        if C in num:
            num.update({B:0, C:num[C]+num[B]})
        else:
            num[C] = num[B]
            num[B] = 0
        print(sum_A)
    except KeyError:
        print(sum_A)