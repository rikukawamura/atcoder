import pdb
import copy
import operator

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
scores = [k] * n
minus = [-1] * n

for i in a:
    minus_cp = copy.deepcopy(minus)
    minus_cp[i-1] = 0
    scores = map(operator.add, scores, minus_cp)
total_score = list(scores)

print(*['Yes' if x > 0 else 'No' for x in total_score], sep='\n')
