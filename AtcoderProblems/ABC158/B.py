import pdb

#　配列が大きくなりすぎると，REとなるから注意
n, a, b = map(int, input().split())

c = n // (a+b)
bleus = a * c

amari = n % (a+b)

if amari > a:
    amari = a
bleus += amari
print(bleus)