import pdb
import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

how_many = [0] * 5
if N % A == 0:
    how_many[0] = N/A
else:
    how_many[0] = math.ceil(N/A)

if N % B == 0:
    how_many[1] = N/B
else:
    how_many[1] = math.ceil(N/B)

if N % C == 0:
    how_many[2] = N/C
else:
    how_many[2] = math.ceil(N/C)

if N % D == 0:
    how_many[3] = N/D
else:
    how_many[3] = math.ceil(N/D)

if N % E == 0:
    how_many[4] = N/E
else:
    how_many[4] = math.ceil(N/E)

#pdb.set_trace()
max_val = max(how_many)

print(int(4+max_val))



