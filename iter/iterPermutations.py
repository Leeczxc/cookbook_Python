from itertools import permutations, combinations, combinations_with_replacement

if __name__=='__main__':
    items = ['a', 'b', 'c']
    for p in permutations(items):
        print(p)

    for c in combinations(items, 2):
        print(c)

    for c in combinations_with_replacement(items, 3):
        print(c)