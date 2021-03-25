import collections


N = int(input())
S = [input() for x in range(N)]
col = collections.Counter(S)
S = {'AC': 0, 'TLE': 0, 'WA': 0, 'RE': 0}

if 'AC' in col:
    S['AC'] = col['AC']
if 'WA' in col:
    S['WA'] = col['WA']
if 'TLE' in col:
    S['TLE'] = col['TLE']
if 'RE' in col:
    S['RE'] = col['RE']


print('AC x {}'.format(S['AC']))
print('WA x {}'.format(S['WA']))
print('TLE x {}'.format(S['TLE']))
print('RE x {}'.format(S['RE']))

