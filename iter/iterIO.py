CHUNKSIZE = 8192

# True
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)

# Iter方法
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass

if __name__ == '__main__':
    reader(r'./../somefile.txt')