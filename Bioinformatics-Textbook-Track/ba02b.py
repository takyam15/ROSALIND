# Find a Median String


import itertools


def read(file):
    with open(file) as f:
        k = int(f.readline().strip())
        strings = f.read().strip().split('\n')
    return k, strings


def hamming_distance(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


def generate_k_mers(k):
    nucreotides = ['A', 'C', 'G', 'T']
    k_mers = [
        ''.join(string) for string in itertools.product(nucreotides, repeat=k)
    ]
    return k_mers


def compute_min_hamming_distance(string, pattern):
    k = len(pattern)
    distances = []
    for i in range(len(string)-k+1):
        substring = string[i:i+k]
        distances.append(hamming_distance(pattern, substring))
    return min(distances)


def main(file, export=True):
    k, strings = read(f'./dataset/{file}.txt')
    k_mers = generate_k_mers(k)
    distances = {}
    for string in strings:
        for pattern in k_mers:
            distances[pattern] = distances.get(pattern, 0) + compute_min_hamming_distance(string, pattern)
    median_string = [pattern for pattern in distances if distances[pattern] == min(distances.values())][0]
    print(median_string)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(median_string)


if __name__ == '__main__':
    main('sample_rosalind_ba2b')
    main('rosalind_ba2b')
