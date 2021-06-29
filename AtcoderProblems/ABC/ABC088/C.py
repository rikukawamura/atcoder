import pdb
import itertools
import numpy as np

C = [list(map(int, input().split())) for _ in range(3)]
C = np.array(C)
max_C = np.max(C)

count = 0
for i in list(itertools.product(range(max_C), repeat=6)):
    a_1, a_2, a_3, b_1, b_2, b_3 = i
    count += 1
print(count)