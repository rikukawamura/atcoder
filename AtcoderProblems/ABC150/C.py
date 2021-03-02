import itertools
import pdb

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

p_list = sorted([list(x) for x in itertools.permutations(p)])
q_list = sorted([list(x) for x in itertools.permutations(q)])
p_index = p_list.index(p)
q_index = q_list.index(q)

print(abs(p_index-q_index))