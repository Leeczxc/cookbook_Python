print('ace', 1, 2)
print('ace', 1, 2, sep=',')
print('ace', 1, 2, sep=',', end='!!\n')


for i in range(5):
    print(i, end=' ')

# str.join

print(','.join(('ace', '1', '2', '3')))

# 对于不是字符串的语句可以使用下面的方式输出
row = ('ace', 1, 2, 3)
print(*row, sep=',')