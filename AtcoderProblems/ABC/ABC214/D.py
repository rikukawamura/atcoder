from heapq import heappush, heappop
import pdb

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N = int(input())
edges = []
for i in range(N-1):
    u, v, w = int_sp()
    edges.append((w, u, v))
edges.sort()
#pdb.set_trace()

union = UnionFind(N)
ans = 0

for i in range(N-1):
    pre_node = edges[i][1]-1
    nxt_node = edges[i][2]-1
    w = edges[i][0]
    pre_cnt = union.size(pre_node)
    nxt_cnt = union.size(nxt_node)
    pdb.set_trace()
    ans += pre_cnt * nxt_cnt * w
    union.union(pre_node, nxt_node)
print(ans)
