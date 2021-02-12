import pdb
import numpy as np

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
s = np.array(s)
pdb.set_trace()

for line in range(h):
    for row in range(w):
        if line == 1 or line == h-1:
