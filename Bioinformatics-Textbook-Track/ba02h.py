# Implement DistanceBetweenPatternAndStrings


def read(file):
    with open(file) as f:
        pattern = f.readline().strip()
        strings = f.readline().strip().split(' ')
    return pattern, strings


def main(file, export=True):
    pattern, strings = read(f'./dataset/{file}.txt')


if __name__ == '__main__':
    main('sample_rosalind_ba2h')
    #main('rosalind_ba2h')
