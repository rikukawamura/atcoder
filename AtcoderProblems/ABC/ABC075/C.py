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
import pdb
import sys

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

sys.setrecursionlimit(10**7)

N, M = int_sp()
uf = UnionFind(N)
graph = []
for _ in range(M):
    a, b = int_sp()
    uf.union(a-1, b-1)
    graph.append([a, b])

root = 0
for i in uf.parents:
    if i < 0:
        root += 1

cnt = 0
for i in range(M):
    uf = UnionFind(N)
    for j, k in enumerate(graph):
        a = k[0]
        b = k[1]
        if i == j:
            continue
        uf.union(a-1, b-1)
    root2 = 0
    for i in uf.parents:
        if i < 0:
            root2 += 1
    if root2 > root:
        cnt += 1
print(cnt)









