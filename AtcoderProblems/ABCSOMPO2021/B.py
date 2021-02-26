s = input()

flag=False
for i, s in enumerate(s):
    if i % 2 == 0:
        if s.isupper():
            flag=True
    if i % 2 == 1:
        if s.islower():
            flag=True

if flag:
    print('No')
else:
    print('Yes')