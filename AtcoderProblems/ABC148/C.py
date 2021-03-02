import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

a, b = map(int, input().split())
print(my_lcm(a,b))