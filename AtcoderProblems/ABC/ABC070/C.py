import pdb
import math

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)


N = int(input())
T = [int(input()) for _ in range(N)]

output = 1
for t in T:
    output = my_lcm(output, t)
print(output)
