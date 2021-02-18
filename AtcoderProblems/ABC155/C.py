from collections import Counter
from sys import stdin
import pdb
n = int(input())
s = [stdin.readline()[:-1] for _ in range(n)]
#pdb.set_trace()
s = Counter(s)
ret = [letter for letter,count in s.most_common() if count == s.most_common()[0][1]]
ret = sorted(ret)
print(*ret, sep='\n')


