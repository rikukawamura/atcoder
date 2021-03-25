import pdb
import itertools

N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
A_acc = list(itertools.accumulate(A))

total = 0
j = 0
for i, a in zip(range(N-1, 0, -1), A):
    total = total + (i*a) - (A_acc[-1]-A_acc[j])
    j += 1
print(total)
