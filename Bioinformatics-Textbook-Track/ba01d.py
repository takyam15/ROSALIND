# Find All Occurrences of a Pattern in a String


def read(file):
    with open(file) as f:
        pattern = f.readline().strip()
        string = f.readline().strip()
    return pattern, string


def find_pattern(pattern, string):
    indices = []
    pattern_len = len(pattern)
    for i in range(len(string)-pattern_len+1):
        substring = string[i:i+pattern_len]
        if substring == pattern:
            indices.append(i)
    return indices


def main(file, export=True):
    pattern, string = read(f'./dataset/{file}.txt')
    found = find_pattern(pattern, string)
    output = ' '.join([str(n) for n in found])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1d')
    main('rosalind_ba1d')
