import pdb
import copy


N = int(input())
A = list(map(int, input().split()))
index_list = 0
t = 0

for i in range(1, 2*(10**5)+1):
    if i == 1 and i not in A[t:]:
        print(-1)
        exit()
    elif i in A[t:]:
        index_list += 1
        t = A[t:].index(i) + t
    else:
        break
print(N - index_list)

'''
N = int(input())
a = [int(s)-1 for s in input().split()]
result = 0
for i in range(N):
    if a[i] != (i - result):
        result += 1

if result == N:
    print(-1)
else:
    print(result)
'''

