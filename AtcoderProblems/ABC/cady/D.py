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
# こねくり回した．もっと賢いやり方を学びたい

def main():
    from collections import Counter
    K = int(input())
    S = list(input())
    T = list(input())
    col_S = Counter(list(map(int, S[:4])))
    col_T = Counter(list(map(int, T[:4])))


    S_T = list(map(int, S[:4])) + list(map(int, T[:4]))
    col_S_T = Counter(S_T)

    cards = {1:K, 2:K, 3:K, 4:K, 5:K, 6:K, 7:K, 8:K, 9:K}

    # カードの残り枚数
    for key, value in zip(col_S_T.keys(), col_S_T.values()):
        cards[key] -= value

    taka = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    aoki = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for key, value in zip(col_S.keys(), col_S.values()):
        taka[key] = value

    for key, value in zip(col_T.keys(), col_T.values()):
        aoki[key] = value


    taka_win = 0
    total = 0
    for i in range(1, 10):
        if cards[i] == 0:
            continue
        else:
            taka_score = 0
            tmp_cards = cards[i]
            cards[i] -= 1
            taka[i] += 1

            for key, value in zip(taka.keys(), taka.values()):
                taka_score += key * (10 ** value)

            for j in range(1, 10):
                if cards[j] == 0:
                    continue
                else:
                    aoki_score = 0
                    aoki[j] += 1

                    for key, value in zip(aoki.keys(), aoki.values()):
                        aoki_score += key * (10 ** value)

                    if taka_score > aoki_score:
                        taka_win += tmp_cards * cards[j]

                    aoki[j] -= 1

                    total += tmp_cards * cards[j]
            taka[i] -= 1
            cards[i] += 1

    print(taka_win/total)


if __name__ == '__main__':
    main()
