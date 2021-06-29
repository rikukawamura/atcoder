import pdb
import math


N = int(input())
A = sorted(list(map(int, input().split())))

ans = A[0]
for a in A[1:]:
    ans = math.gcd(a, ans)
    pdb.set_trace()
print(ans)