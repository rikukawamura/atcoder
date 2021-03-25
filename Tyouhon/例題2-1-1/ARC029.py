import pdb
import itertools

N = int(input())
T = [int(input()) for _ in range(N)]

if N == 1:
    print(*T)

elif N == 2:
    print(max(T))

elif N == 3:
    min_time = float('INF')
    for t in itertools.permutations(T):
        T_1 = t[0]+t[1]
        T_2 = t[2]
        tmp = max(T_1, T_2)

        if tmp < min_time:
            min_time = tmp
    print(min_time)

elif N == 4:
    min_time = float('INF')
    for t in itertools.permutations(T):
        T_1 = t[0]+t[1]
        T_2 = t[2]+t[3]
        tmp = max(T_1, T_2)

        if tmp < min_time:
            min_time = tmp
    print(min_time)


