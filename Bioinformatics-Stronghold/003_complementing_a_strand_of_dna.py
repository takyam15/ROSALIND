def complement(s):
    complementing_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    sc = ''
    for char in s[::-1].strip():
        sc += complementing_dict[char]
    return sc


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_revc.txt') as f:
        s = f.read()
    sc = complement(s)
    print(sc)
    with open('./dataset/rosalind_revc.txt') as f:
        s = f.read()
    sc = complement(s)
    print(sc)
    with open('./submission/complementing_a_strand_of_dna.txt', mode='w') as f:
        f.write(sc)
