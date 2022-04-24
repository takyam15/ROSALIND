# Implement MotifEnumeration


import itertools


def read(file):
    with open(file) as f:
        k, d = f.readline().strip().split(' ')
        strings = f.read().strip().split('\n')
    return int(k), int(d), strings


def hamming_distance(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


def generate_all_k_mers(k):
    strings = ['A', 'C', 'G', 'T']
    return [''.join(string) for string in itertools.product(strings, repeat=k)]


def generate_d_neighborhood(pattern, d, k_mers):
    d_neighborhood = []
    for k_mer in k_mers:
        if hamming_distance(pattern, k_mer) <= d:
            d_neighborhood.append(k_mer)
    return d_neighborhood


def main(file, export=True):
    k, d, strings = read(f'./dataset/{file}.txt')
    k_mers = generate_all_k_mers(k)
    d_neighborhoods = []
    for string in strings:
        d_neighborhood = []
        for i in range(len(string)-k+1):
            pattern = string[i:i+k]
            d_neighborhood += generate_d_neighborhood(pattern, d, k_mers)
        d_neighborhoods.append(set(d_neighborhood))
    motifs = d_neighborhoods[0]
    for neighborhood in d_neighborhoods[1:]:
        motifs = motifs & neighborhood
    output = ' '.join(motifs)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)   


if __name__ == '__main__':
    main('sample_rosalind_ba2a')
    main('rosalind_ba2a')
