from itertools import dropwhile, islice

if __name__ == '__main__':
    # 使用dropwhile
    with open('etc/passwd') as f:
        for line in dropwhile(lambda line: not line.startswith('#'), f):
            print(line, end=' ')
    # 使用islice

    items = ['a', 'b', 'c', 'd', 1, 4, 5,]
    for x in islice(items, 3, None):
        print(x)