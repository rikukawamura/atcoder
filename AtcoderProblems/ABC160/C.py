import pdb

k, n = map(int, input().split())
a = list(map(int, input().split()))

li = []
for i in range(n - 1):
  li.append(a[i + 1] - a[i]) #liに対して配列Aの要素間の差分を追加

li.append(abs(a[0] + (k - a[-1]))) #配列の初項と末項のみ別で追加
print(sum(li) - max(li))