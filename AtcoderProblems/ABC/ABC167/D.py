import pdb

N, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

H = []
S = set()

n = 0
start = 0
#pdb.set_trace()
while True: # ダブリングの開始時刻を求める
    if n in S:
        start = H.index(n)
        break

    H.append(n) # 順番を保った記録
    S.add(n) # 訪れた王国を記録（順番は保っていない）
    n = A[n]

pdb.set_trace()
if K < len(H):
    print(H[K]+1)
else:
    print(H[(K-start) % (len(H) - start) + start]+1)