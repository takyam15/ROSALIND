# Implement GibbsSampler


def read(file):
    with open(file) as f:
        k, t, n = f.readline.strip().split(' ')
        strings = f.read().strip().split('\n')
    return int(k), int(t), int(n), strings


def main(file, export=True):
    k, t, n, strings = read(f'./dataset/{file}.txt')


if __name__ == '__main__':
    main('sample_rosalind_ba2g')
    #main('rosalind_ba2g')
