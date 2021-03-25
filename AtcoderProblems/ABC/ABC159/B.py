import pdb

s = input()
len_s = len(s)
t = s[:(len(s)-1)//2]
u = s[(len(s)+3)//2-1:]
#pdb.set_trace()
if s == s[::-1] and t == t[::-1] and u == u[::-1]:
    print('Yes')
else:
    print('No')