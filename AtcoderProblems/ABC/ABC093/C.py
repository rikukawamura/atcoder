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
    X = sorted(li_int_sp(), reverse=True)
    #pdb.set_trace()
    count = 0
    A = X[0] % 2
    B = X[1] % 2
    C = X[2] % 2
    #pdb.set_trace()
    count = 0
    if A == B == C:
        count += (X[0]-X[1])//2
        count += (X[0]-X[2])//2
    elif (A == B) and (A != C):
        count += 1
        X[0] += 1
        X[1] += 1
        count += (X[0] - X[1]) // 2
        count += (X[0] - X[2]) // 2
    elif (A != B) and (A == C):
        count += 1
        X[0] += 1
        X[2] += 1
        count += (X[0] - X[1]) // 2
        count += (X[0] - X[2]) // 2
    elif (A != B) and (A != C):
        count += 1
        X[1] += 1
        X[2] += 1
        count += (X[0] - X[1]) // 2
        count += (X[0] - X[2]) // 2
    print(count)


if __name__ == '__main__':
    main()