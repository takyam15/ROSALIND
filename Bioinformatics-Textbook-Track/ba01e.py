# Find Patterns Forming Clumps in a String


def read(file):
    with open(file) as f:
        genome = f.readline().strip()
        k, length, t = [int(n) for n in f.readline().strip().split(' ')]
    return genome, k, length, t


def count_patterns(k, string):
    pattern_counts = {}
    for i in range(len(string)-k+1):
        substring = string[i:i+k]
        pattern_counts[substring] = pattern_counts.get(substring, 0) + 1
    return pattern_counts


def find_k_mers(string, k, t):
    pattern_counts = count_patterns(k, string)
    return [
        pattern for pattern in pattern_counts if pattern_counts[pattern] == t
    ]


def main(file, export=True):
    genome, k, length, t = read(f'./dataset/{file}.txt')
    patterns = []
    for i in range(len(genome)-length+1):
        substring = genome[i:i+length]
        patterns += find_k_mers(substring, k, t)
    output = ' '.join(list(set(patterns)))
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1e')
    main('rosalind_ba1e')
