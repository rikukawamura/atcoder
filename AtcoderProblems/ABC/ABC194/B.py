import pdb
import copy

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

min_num = []
comb = []
for i in range(n):
    ab_cp = copy.deepcopy(ab)
    del ab_cp[i]
    for j in range(n-1):
        min_num.append(max(ab[i][0], ab_cp[j][1]))
        comb.append([ab[i][0], ab_cp[j][1]])

for i in range(n):
    min_num.append(ab[i][0]+ab[i][1])
print(min(min_num))




