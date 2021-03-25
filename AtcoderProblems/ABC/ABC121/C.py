import pdb

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x:x[0])

cost = 0
flag = True
while flag:
    for a, b in AB:
        if b <= M:
            cost += a*b
            M -= b
        else:
            cost += a*M
            M -= M
        if M == 0:
            flag = False
print(cost)

