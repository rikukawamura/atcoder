def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


class Bit:
    def __init__(self, n):
        #pdb.set_trace()
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


import pdb

n = int(input())
A = li_int_sp()
bit = Bit(n)
ans = 0
for i, a in enumerate(A):
    #pdb.set_trace()
    ans += i - bit.sum(A[i])
    bit.add(A[i], 1)
print(ans)