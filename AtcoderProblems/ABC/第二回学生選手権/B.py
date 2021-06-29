import pdb

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = set(A) ^ set(B)
#pdb.set_trace()
print(*sorted(AB))