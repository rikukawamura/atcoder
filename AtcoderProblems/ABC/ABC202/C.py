import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# B_Cjの値を格納
D = [0] * (N+1)
for c in C:
    D[B[c-1]] += 1

pdb.set_trace()
count = 0
A_col = collections.Counter(A)
for a_key, a_value in zip(A_col.keys(), A_col.values()):
    count += D[a_key] * a_value

print(count)
