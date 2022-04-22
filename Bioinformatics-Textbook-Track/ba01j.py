# Find Frequent Words with Mismatches and Reverse Complements

import itertools


def read(file):
    with open(file) as f:
        text = f.readline().strip()
        k, d = [int(n) for n in f.readline().strip().split(' ')]
        return text, k, d


def create_all_combinations(length, strings=['A', 'C', 'G', 'T']):
    all_combinations = [
        ''.join(string) for string in itertools.product(strings, repeat=length)
    ]
    return all_combinations


def hamming_distance(pattern, subtext):
    distance = 0
    for s, t in zip(pattern, subtext):
        if s != t:
            distance += 1
    return distance


def count_words(text, k, d):
    counts = {}
    for i in range(len(text)-k+1):
        subtext = text[i:i+k]
        for pattern in create_all_combinations(k):
            if hamming_distance(subtext, pattern) <= d:
                counts[pattern] = counts.get(pattern, 0) + 1
    return counts


def reverse_complement(string):
    rc_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    return ''.join([rc_dict[s] for s in string[::-1]])


def combine_reverse_complements(counts):
    combined_counts = {}
    for pattern in counts:
        if pattern not in combined_counts:
            combined_counts[pattern] = counts[pattern] + counts.get(reverse_complement(pattern), 0)
    return combined_counts


def find_words(counts):
    words = [
        word for word in counts if counts[word]==max(counts.values())
    ]
    return words


def main(file, export=True):
    text, k, d = read(f'./dataset/{file}.txt')
    counts = count_words(text, k, d)
    combined_counts = combine_reverse_complements(counts)
    words = find_words(combined_counts)
    output = ' '.join(words)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1j')
    main('rosalind_ba1j')
