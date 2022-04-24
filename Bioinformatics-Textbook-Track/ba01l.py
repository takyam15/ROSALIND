# Implement PatternToNumber


def read(file):
    with open(file) as f:
        pattern = f.read().strip()
    return pattern


def symbol_to_number(s):
    strings = ['A', 'C', 'G', 'T']
    return strings.index(s)


def pattern_to_number(pattern):
    if pattern:
        return 4 * pattern_to_number(pattern[:-1]) + symbol_to_number(pattern[-1])
    else:
        return 0


def main(file, export=True):
    pattern = read(f'./dataset/{file}.txt')
    number = pattern_to_number(pattern)
    print(number)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(str(number))


if __name__ == '__main__':
    main('sample_rosalind_ba1l')
    main('rosalind_ba1l')