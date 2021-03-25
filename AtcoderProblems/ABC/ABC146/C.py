import pdb


A, B, X = map(int, input().split())

def compare(N):
    return A * N + B * len(str(N)) <= X

left = 0
right = 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if compare(mid):
        left = mid
    else:
        right = mid
print(left)