import pdb
import math
from decimal import Decimal

R, X, Y = map(int, input().split())

distance = Decimal(math.sqrt(X**2+Y**2))

min_step = distance/Decimal(R)
if min_step < 1:
    print(2)
else:
    print(math.ceil(min_step))