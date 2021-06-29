import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
C_col = collections.Counter(C)

count = 0
for a, c, val in zip(range(len(A)), C_col.keys(), C_col.values()):
    pdb.set_trace()
    if A[a] == B[c-1]:
        count += val
print(count)




import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_col = collections.Counter(A)
B_col = collections.Counter(B)
C_col = collections.Counter(C)

count = 0
i = 0
for a, b, c in zip(A, B, C):
    pdb.set_trace()
    if A[i] == B[c-1]:
        count += C_col[c]
print(count)


import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_col = collections.Counter(A)
B_col = collections.Counter(B)
C_col = collections.Counter(C)


count = 0
for a in A:
    pdb.set_trace()
    if a in B:
        count += C_col[B.index(a)+1] * B_col[a]
print(count)