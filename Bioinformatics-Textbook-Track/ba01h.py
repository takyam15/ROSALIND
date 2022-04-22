# Find All Approximate Occurrences of a Pattern in a String


def read(file):
    with open(file) as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline().strip())
    return pattern, text, d


def hamming_distance(pattern, subtext):
    distance = 0
    for s, t in zip(pattern, subtext):
        if s != t:
            distance += 1
    return distance


def find_patterns(pattern, text, d):
    indices = []
    length = len(pattern)
    for i in range(len(text)-length+1):
        subtext = text[i:i+length]
        if hamming_distance(pattern, subtext) <= d:
            indices.append(i)
    return indices


def main(file, export=True):
    pattern, text, d = read(f'./dataset/{file}.txt')
    found = find_patterns(pattern, text, d)
    output = ' '.join([str(n) for n in found])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1h')
    main('rosalind_ba1h')
