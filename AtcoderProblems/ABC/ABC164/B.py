import math


a, b, c, d = map(int, input().split())

'''
while True:
    c -= b
    if c == 0:
        print('Yes')
        break
    a -= d
    if a == 0:
        print('No')
        break
'''

takahashi = math.ceil(a / d)
aoki = math.ceil(c / b)
if takahashi >= aoki:
    print('Yes')
else:
    print('No')