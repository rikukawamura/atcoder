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


    from itertools import accumulate

    N = int(input())
    x = []
    y = []
    for i in range(N):
        A, B = int_sp()
        if A == 1:
            x.append([i,B])
        else:
            y.append([i,B])
    if x != [] and y != []:
        x_ind, x_val = list(map(list, (zip(*x))))
        y_ind, y_val = list(map(list, (zip(*y))))

        x_total = [0] * N
        y_total = [0] * N
        for ind, val in zip(x_ind, x_val):
            x_total[ind] = val
        for ind, val in zip(y_ind, y_val):
            y_total[ind] = val

        x_acc = [0] + list(accumulate(x_total))
        y_acc = [0] + list(accumulate(y_total))
        # pdb.set_trace()
        Q = int(input())
        for _ in range(Q):
            L, R = int_sp()
            x2 = x_acc[R] - x_acc[L - 1]
            y2 = y_acc[R] - y_acc[L - 1]
            print(x2, y2)
    elif x != [] and y == []:
        x_ind, x_val = list(map(list, (zip(*x))))
        x_total = [0] * N
        for ind, val in zip(x_ind, x_val):
            x_total[ind] = val

        x_acc = [0] + list(accumulate(x_total))
        Q = int(input())
        for _ in range(Q):
            L, R = int_sp()
            x2 = x_acc[R] - x_acc[L - 1]
            print(x2, 0)
    else:
        y_ind, y_val = list(map(list, (zip(*y))))
        y_total = [0] * N
        for ind, val in zip(y_ind, y_val):
            y_total[ind] = val

        y_acc = [0] + list(accumulate(y_total))
        Q = int(input())
        for _ in range(Q):
            L, R = int_sp()
            y2 = y_acc[R] - y_acc[L - 1]
            print(0, y2)




if __name__ == '__main__':
    main()