import pdb
import itertools

N = int(input())
divs = set()
x = 1
while x ** 2 <= N:
    if N % x == 0:
        divs.add(x)
        divs.add(N // x)
    x += 1
ans = list(divs)
ans.sort()

mv = float('INF')
for comb in itertools.combinations_with_replacement(ans, 2):
    if comb[0] * comb[1] == N:
        if comb[0]-1 + comb[1]-1 < mv:
            mv = comb[0]-1 + comb[1]-1
            #tmp_i, tmp_j = comb[0], comb[1]
#print(tmp_i, tmp_j)
print(mv)


