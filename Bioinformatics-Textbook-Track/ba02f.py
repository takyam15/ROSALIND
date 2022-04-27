# Implement RandomizedMotifSearch


def read(file):
    with open(file) as f:
        k, t = [int(n) for n in f.readline().strip().split(' ')]
        strings = f.read().strip().split('\n')
    return k, t, strings


def main(file, export=True):
    k, t, strings = read(f'./dataset/{file}.txt')


if __name__ == '__main__':
    main('sample_rosalind_ba2f')
    #main('rosalind_ba2f')
