def calculate_mod(numbers, base=1000000):
    mods = []
    product = 1
    for number in numbers:
        product *= number
        if product > base:
            mods.append(product % base)
            product = 1
    else:
        mods.append(product)
    if len(mods) > 1:
        return calculate_mod(mods, base)
    return mods[0]


def infer_mrna(s, codon_counts):
    counts = [codon_counts[aa] for aa in s.strip()] + [codon_counts['Stop']]
    return calculate_mod(counts)


if __name__ == '__main__':
    rna_codon_dict = {}
    with open('rna_codon_table.txt') as f:
        for line in f:
            chars = line.strip().split(' ')

            for i, char in enumerate(chars):
                if len(char) == 3:
                    rna_codon_dict[char] = chars[i+1]
    codon_counts = {}
    for codon, aa in rna_codon_dict.items():
        codon_counts[aa] = codon_counts.get(aa, 0) + 1
    with open('./dataset/sample_rosalind_mrna.txt') as f:
        s = f.read()
    answer = infer_mrna(s, codon_counts)
    print(answer)
    with open('./dataset/rosalind_mrna.txt') as f:
        s = f.read()
    answer = infer_mrna(s, codon_counts)
    print(answer)
    with open('./submission/inferring_mrna_from_protein.txt', mode='w') as f:
        f.write(str(answer))
