import pdb
import string
import itertools

'''
パスワード全検索プログラム
'''
'''
password = input('パスワードを入力してください．\n')
while len(password) > 6:
    password = input('6文字以下のパスワードが設定可能です．\n')

can_selected = list(string.ascii_lowercase) + list(range(0, 10))

target = []
for i in password:
    for j in can_selected:
        if i == j:
            target.append(j)

print(''.join(target))
'''
N = 5
pass_list = []
choise = list(string.ascii_lowercase) + list(map(str, list(range(0, 10))))
for i in range(1, N+1):
    pass_list = [''.join(i) for i in product(choise, repeat=i)]
print(pass_list, len(pass_list))

