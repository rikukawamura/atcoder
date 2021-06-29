import pdb

N = int(input())
A = list(map(int, input().split()))

height = [[i, x] for i, x in enumerate(A, 1)]
height_sorted = sorted(height, key=lambda x:x[1], reverse=True)
for i in height_sorted:
    print(i[0])