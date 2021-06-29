import pdb

N = int(input())
A = list(map(int, input().split()))

no = []
yes = []

count = 0
for a in A:
    if a == 2:
        count += 1
    if a%4 == 0:
        yes.append(a)
    else:
        no.append(a)

x = []
for n, y in zip(no, yes):
    x.append(n)
    x.append(y)

if count % 2 == 0:
    len_no = len(no) - count
if count % 2 == 1:
    len_no = len(no) - count + 1
pdb.set_trace()
if len_no - len(yes) >= 2:
    print('No')
else:
    print('Yes')

