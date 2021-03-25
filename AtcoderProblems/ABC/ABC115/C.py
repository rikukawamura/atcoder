import pdb
import numpy as np
import itertools

N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H = sorted(H)
diff = np.diff(np.array(H)).tolist()
diff_acc = list(itertools.accumulate(diff))

min = diff_acc[N-K-1]
#pdb.set_trace()
for i in range(N-K, len(diff_acc)):
    tmp = diff_acc[i] - diff_acc[i-(N-K)]
    if tmp < min:
        min = tmp
print(min)