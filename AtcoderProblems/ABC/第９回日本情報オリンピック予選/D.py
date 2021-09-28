def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


import pdb
from itertools import permutations
from collections import defaultdict
import math
#print(permutations_count(10, 4))
N = int(input())
K = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))

pair = defaultdict(int)
for i in permutations(cards, K):
    pair[''.join(list(map(str, i)))] += 1

print(len(pair))
