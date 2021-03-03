import pdb
import collections

#　自分の解答（TLE）
'''
n, m = map(int, input().split())
ps = [list(map(str, input().split())) for _ in range(m)]


ac_index = {}
for i in range(1, n+1):
    if [str(i), 'AC'] in ps:
        ac_index[i] = ps.index([str(i), 'AC'])

pena = 0
for num, index in zip(list(ac_index.keys()), list(ac_index.values())):
    pena += len([x for x in ps[:index+1] if x == [str(num), 'WA']])

print(len(ac_index), pena)
'''

# https://cocoinit23.com/abc151/を参考にした
n, m = map(int, input().split())
submit = [list(map(str, input().split())) for _ in range(m)]

ac = [0] * (n + 1)
wa = [0] * (n + 1)

for i in range(m):
    result = submit[i][1]
    question = int(submit[i][0])

    if result == 'AC' and ac[question] == 0:
        ac[question] = 1
    elif result == 'WA' and ac[question] == 0:
        wa[question] += 1

# ACが出なかった問題に対してのペナルティはないので，それらの問題に対するペナルティを0にする．
for i in range(n + 1):
    if ac[i] != 1:
        wa[i] = 0

print(sum(ac), sum(wa))








