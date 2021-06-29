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

# ----------------------------------------------------------------------------------------------------------
def main():
    A, B, K = map(int, input().split())
    a = A  # 残っているaの数
    b = B  # 残っているbの数
    ans = ""
    while a > 0 and b > 0:
        #pdb.set_trace()
        a_comb = comb(a - 1 + b, a - 1)
        if K <= a_comb:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            b -= 1
            K -= a_comb
    ans += "a" * a
    ans += "b" * b
    print(ans)


if __name__ == '__main__':
    main()

