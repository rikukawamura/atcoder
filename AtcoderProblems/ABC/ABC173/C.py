import pdb
import numpy as np
import itertools

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
c = np.array(c)

count = 0
for i in range(h):
    for del_line in itertools.combinations(list(range(h)), i):
        for j in range(w):
            for del_row in itertools.combinations(list(range(w)), j):
                del_c = np.delete(c, del_line, 0)
                del_c = np.delete(del_c, del_row, 1)
                if np.count_nonzero(del_c=='#') == k:
                    count += 1
print(count)


