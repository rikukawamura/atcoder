import pdb

#　https://note.com/nanigashi/n/na06f4a4bf4ddを参考にした
# ...,x-2,x-1,x,x+1,x+2,...とxに-1,+1,-2,+2と幅を広げて探索する方法はc問題では頻出な気がする
x, n = map(int, input().split())
p_list = list(map(int, input().split()))

if n == 0:
   print(x)
else:
   for i in range(0,100):
       if not x-i in p_list:
           print(x-i)
           break
       elif not x+i in p_list:
           print(x+i)
           break