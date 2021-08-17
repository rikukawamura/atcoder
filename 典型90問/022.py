def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))



import pdb
import math


ABC = li_int_sp()
gcds = math.gcd(math.gcd(ABC[0],ABC[1]), ABC[2])

pdb.set_trace()
output = 0
for i in ABC:
    output += i//gcds-1
print(output)

