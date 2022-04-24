# Implement NumberToPattern

import itertools


def read(file):
    with open(file) as f:
        index = int(f.readline().strip())
        k = int(f.readline().strip())
    return index, k


def number_to_pattern(index, k):
    strings = ['A', 'C', 'G', 'T']
    all_k_mers = [''.join(string) for string in itertools.product(strings, repeat=k)]
    return all_k_mers[index]


def main(file, export=True):
    index, k = read(f'./dataset/{file}.txt')
    pattern = number_to_pattern(index, k)
    print(pattern)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(pattern)


if __name__ == '__main__':
    main('sample_rosalind_ba1m')
    main('rosalind_ba1m')
