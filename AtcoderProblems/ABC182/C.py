import itertools
import sys

N = input()
list_N = list(map(int, list(N)))
output = 0
flag = False

if sum(list_N) % 3 == 0:
    print(output)
    sys.exit()

for output, j in enumerate(range(len(N))[::-1], 1):
    for i in itertools.permutations(list_N, j):
        if j == 0:
            print(-1)
            flag = True
            break

        if sum(i) % 3 == 0:
            print(output)
            flag = True
            break
    if flag:
        break


