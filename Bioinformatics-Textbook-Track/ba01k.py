# Generate the Frequency Array of a Strin

import itertools


def read(file):
    with open(file) as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    return text, k


def generate_all_k_mers(k):
    nucreotides = ['A', 'C', 'G', 'T']
    return [''.join(k_mer) for k_mer in itertools.product(nucreotides, repeat=k)]


def generate_frequency_dict(text, k):
    frequency_dict = {}
    for k_mer in generate_all_k_mers(k):
        frequency_dict[k_mer] = 0
    for i in range(len(text)-k+1):
        k_mer = text[i:i+k]
        frequency_dict[k_mer] += 1
    return frequency_dict


def main(file, export=True):
    text, k = read(f'./dataset/{file}.txt')
    frequency_dict = generate_frequency_dict(text, k)
    output = ' '.join([str(n) for n in frequency_dict.values()])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1k')
    main('rosalind_ba1k')
    