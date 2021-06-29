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
# 配列の操作でなんとかなる．

def main():
    from math import sqrt, atan2, pi, cos, sin, degrees, radians


    N = int(input())
    x_0, y_0 = int_sp()
    x_half, y_half = int_sp()

    #pdb.set_trace()
    x_center = (x_0+x_half) / 2
    y_center = (y_0+y_half) / 2

    r = sqrt((x_0-x_center)**2 + (y_0-y_center)**2)

    angle_0 = degrees(atan2(y_0-y_center, x_0-x_center))

    angle_n = 360 / N

    angle_1 = angle_0 + angle_n

    x_1 = x_center + (r * cos(radians(angle_1)))
    y_1 = y_center + (r * sin(radians(angle_1)))

    print(x_1, y_1)


if __name__ == '__main__':
    main()