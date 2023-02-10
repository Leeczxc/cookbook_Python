if __name__ == '__main__':
    with open('./../somefile.txt', 'rb') as f:
        for x in f:
            print(x)
        for x in f:
            print(x.decode('utf-8'))