import pdb

N = int(input())

AB = []
A_total = 0
B_total = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    AB.append(tmp)
    A_total += tmp[0]
    B_total += tmp[1]
    total = A_total + B_total
AB_sortA = sorted(AB, reverse=True, key=lambda x: 2*x[0]+x[1])

takahashi = 0
for i, n in enumerate(AB_sortA, 1):
    takahashi += sum(n)
    A_total -= n[0]
    if takahashi > A_total:
        print(i)
        exit()
