import string
import collections
import pdb

a = list(input())
b = list(string.ascii_lowercase)
col = collections.Counter(a)
pdb.set_trace()

c = a.copy()
# 入力文字列が'a'ならそれより小さいのはないから，-1
if len(a)==1 and a[0]=='a':
    print(-1)
    exit()
# 'aaa'みたいな入力なら，一つ文字数が少ない'aa'を返す
elif len(col)==1 and 'a' in dict(col).keys():
    print(''.join(a[:-1]))
    exit()
# 'cba'みたいな入力なら，一つ文字数が少ない'cb'を返す
elif c[-1] == 'a':
    print(''.join(a[:-1]))
    exit()
# 最後尾の文字が'a'意外だったら，'a'に置換した物を返す
# riku -> rika
else:
    c[-1] = b[0]

print(''.join(c))
