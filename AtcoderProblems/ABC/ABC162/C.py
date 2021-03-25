import itertools
import math
from functools import reduce
import pdb


k = list(range(1, int(input())+1))
comb = itertools.product(k, repeat=3)
gcds = [math.gcd(math.gcd(i[0], i[1]), i[2]) for i in comb]
accum = list(itertools.accumulate(gcds))
print(accum[-1])
