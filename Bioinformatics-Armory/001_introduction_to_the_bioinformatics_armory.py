def count_nucreotides(s):
    nucreotide_counts = {}
    for char in s:
        nucreotide_counts[char] = nucreotide_counts.get(char, 0) + 1
    return nucreotide_counts


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ini.txt') as f:
        s = f.read().strip()
    nucreotide_counts = count_nucreotides(s)
    answer = f'{nucreotide_counts["A"]} {nucreotide_counts["C"]} {nucreotide_counts["G"]} {nucreotide_counts["T"]}'
    print(answer)
    with open('./dataset/rosalind_ini.txt') as f:
        s = f.read().strip()
    nucreotide_counts = count_nucreotides(s)
    answer = f'{nucreotide_counts["A"]} {nucreotide_counts["C"]} {nucreotide_counts["G"]} {nucreotide_counts["T"]}'
    print(answer)
    with open('./submission/introduction_to_the_bioinformatics_armory.txt', mode='w') as f:
        f.write(answer)
