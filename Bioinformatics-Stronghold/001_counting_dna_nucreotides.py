def count_nucreotides(s):
    nucreotides_counts = {}
    for char in s.strip():
        nucreotides_counts[char] = nucreotides_counts.get(char, 0) + 1
    return nucreotides_counts


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_dna.txt') as f:
        s = f.read()
    nucreotides_counts = count_nucreotides(s)
    answer = ' '.join([
        str(nucreotides_counts['A']),
        str(nucreotides_counts['C']),
        str(nucreotides_counts['G']),
        str(nucreotides_counts['T'])
    ])
    print(answer)
    with open('./dataset/rosalind_dna.txt') as f:
        s = f.read()
    nucreotides_counts = count_nucreotides(s)
    answer = ' '.join([
        str(nucreotides_counts['A']),
        str(nucreotides_counts['C']),
        str(nucreotides_counts['G']),
        str(nucreotides_counts['T'])
    ])
    print(answer)
    with open('./submission/counting_dna_nucreotides.txt', mode='w') as f:
        f.write(answer)
