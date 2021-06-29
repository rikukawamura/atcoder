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

    total = []

    def dfs(x, y, count):
        #pdb.set_trace()
        # 範囲外や壁，及び訪れたことがある場合は探索を打ち切る
        if x < 0 or N <= x or y < 0 or 2 <= y:
            return
        elif x == N-1 and y == 1:
            count += graph[y][x]
            total.append(count)
            #count == 0
        count += graph[y][x]
        for k in range(2):
            # 現在地の下と右を探索
            dfs(x + dx[k], y + dy[k], count)

    N = int(input())
    cond = [list(map(int, input().split())) for _ in range(N)]
    graph = [[]*10**5 for _ in range(10**5)]
    pdb.set_trace()

    # 下方向と右方向の順に探索
    dx = [0, 1]
    dy = [1, 0]

    dfs(0,0,0)
    #pdb.set_trace()
    print(max(total))

if __name__ == '__main__':
    main()