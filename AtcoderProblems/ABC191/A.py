v,t,s,d = map(int, input().split())

x = d / v

if x >= t and x <= s:
    print('No')
else:
    print('Yes')