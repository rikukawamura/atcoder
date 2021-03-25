import itertools
import pdb

N = int(input())
L = list(map(int, input().split()))

print(L)
count = 0
output = []
for i in itertools.permutations(L, 3):
    print(i)
    if (i[0]+i[1])>i[2] and (i[0]+i[2])>i[1] and (i[1]+i[2])>i[0] and ((i[0] != i[1]) and (i[0] != i[2]) and i[1] != i[2]):
        output.append(i)
        count += 1
print(set(output))
print(count)

