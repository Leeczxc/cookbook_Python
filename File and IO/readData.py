# 读写数据

if __name__ == '__main__':
    # 读文件
    with open('./../somefile.txt', 'rt') as f:
        data = f.read()
        # for line in f :
    # 写文件
    with open('./../somefile.txt', 'wt') as f:
        f.write('dsa')
        print('dsa', file=f)


