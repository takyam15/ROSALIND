# Generate the d-Neighborhood of a String


import itertools


def read(file):
    with open(file) as f:
        pattern = f.readline().strip()
        d = int(f.readline().strip())
    return pattern, d


def hamming_distance(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


def generate_all_k_mers(k):
    strings = ['A', 'C', 'G', 'T']
    k_mers = [
        ''.join(string) for string in itertools.product(strings, repeat=k)
    ]
    return k_mers


def generate_d_neighborhood(pattern, d):
    d_neighborhood = []
    k_mers = generate_all_k_mers(len(pattern))
    for k_mer in k_mers:
        if hamming_distance(pattern, k_mer) <= d:
            d_neighborhood.append(k_mer)
    return d_neighborhood


def main(file, export=True):
    pattern, d = read(f'./dataset/{file}.txt')
    d_neighborhood = generate_d_neighborhood(pattern, d)
    output = '\n'.join(d_neighborhood)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1n')
    main('rosalind_ba1n')
