import pdb
import math

# この解放思考は覚えておきたいところ
a, b, c, d = map(int, input().split())

#　最小公倍数を求める
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

def cant_division(x, c, d):
    both = my_lcm(c, d)
    c_div = x // c
    d_div = x // d
    both_div = x // both
    return x - (c_div + d_div - both_div)

a_num = cant_division(a-1, c, d)
b_num = cant_division(b, c, d)
print(b_num - a_num)



