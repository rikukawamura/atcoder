import pdb
from collections import Counter
from collections import defaultdict
import itertools

n = int(input())
s = [str(Counter(sorted(list(input())))) for _ in range(n)]


#　要素の数をカウント
dic = Counter(s)

count = 0
for i in dic.keys():
    count += len(list(itertools.combinations(range(dic[i]), 2)))
print(count)