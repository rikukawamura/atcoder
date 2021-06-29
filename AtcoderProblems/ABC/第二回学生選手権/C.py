import pdb
import math

A, B = map(int, input().split())

max_gcd = 1
for i in range(1, 2*10**5):
    C = math.ceil(A / i)
    D = math.floor(B / i)
    E = i*C
    F = i*D
    if E >= A and F <= B and E < F:
        #pdb.set_trace()
        max_gcd = max(max_gcd, i)
print(max_gcd)