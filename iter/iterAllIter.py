from  itertools import zip_longest
if __name__ == '__main__':
    xpts = [1, 2, 3]
    ypts = [4, 5, 6]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['x', 'y', 'z', 'q']
    for x, y in zip_longest(a, b, fillvalue=0):
        print(x, y)