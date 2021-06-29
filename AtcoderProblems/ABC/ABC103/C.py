import pdb

N = int(input())
A = list(map(int, input().split()))
print(sum(list(map(lambda x: x-1, A))))