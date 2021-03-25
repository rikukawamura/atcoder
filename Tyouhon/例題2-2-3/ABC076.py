import re
import pdb


def solve(s, t):
    # 正規表現を使えるように'?'を'.'に変更
    s = s.replace('?', '.')
    ls, lt = len(s), len(t)
    # sよりもtが長い組み合わせは存在しない
    if ls < lt:
        return 'UNRESTORABLE'
    ans = []
    for i in range(ls - lt + 1):
        m = re.match(s[i:i + lt], t)
        if m is None:
            continue
        pdb.set_trace()
        ans.append((s[:i] + t + s[i + lt:]).replace('.', 'a'))
    if not ans:
        return 'UNRESTORABLE'
    return min(ans)


s = input().strip()
t = input().strip()

print(solve(s, t))