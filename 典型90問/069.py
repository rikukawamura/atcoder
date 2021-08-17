def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, K = int_sp()
mod = 10**9+7

if N == 1:
    print(K)
else:
    ans = (K%mod) * ((K-1)%mod) * pow(K-2, N-2, mod) % mod
    print(ans)

