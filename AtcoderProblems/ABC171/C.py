import pdb
import string

# 26真数問題
#　https://qiita.com/u2dayo/items/5f9dfee2ec0145402d75#c%E5%95%8F%E9%A1%8C-one-quadrillion-and-one-dalmatiansを参考
n = int(input())
alphabets = string.ascii_lowercase
alphabets = 'X' + alphabets
res = ''

while True:
    x = n % 26
    if x == 0:
        x = 26
    res += alphabets[x]
    n -= x

    if n == 0:
        break
    n //= 26

print(res[::-1])
