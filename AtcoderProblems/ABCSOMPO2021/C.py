import pdb

n, k = map(int, input().split())
n = str(n)

a=n
i=0
while i!=k:
    if n=='0':
        break
    else:
        #pdb.set_trace()
        a = int(''.join(sorted(list(n), reverse=True))) - int(''.join(sorted(list(n), reverse=False)))
        n=str(a)
        i+=1

print(a)