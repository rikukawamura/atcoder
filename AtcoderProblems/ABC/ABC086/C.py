from math import factorial
import pdb


# ----------------------------------------------------------------------------------------------------------

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# リストのリストの単一の要素を抽出 (リストのset)
# [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, 1]] -> [[1, 1], [0, 1], [0, 0], [1, 0]]
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# ----------------------------------------------------------------------------------------------------------
def main():


    def dfs(x, y, t):
        pdb.set_trace()
        # 範囲外や壁，及び訪れたことがある場合は探索を打ち切る
        if x < 0 or cond[1] <= x or y < 0 or cond[2] <= y:
            return
        graph[y][x].append(t)
        for k in range(4):
            # 現在地の下と右を探索
            dfs(x + dx[k], y + dy[k], t+1)

    N = int(input())
    cond = [list(map(int, input().split())) for _ in range(N)]
    graph = [[[0]*(cond[1])] for _ in range(cond[2])]
    pdb.set_trace()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    #　スタートは(x, y, time) = (0, 0, 0)
    dfs(0,0,0)
    pdb.set_trace()
    print(max(total))

if __name__ == '__main__':
    main()