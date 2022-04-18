def translate(s, rna_codon_dict):
    protein = ''
    for i in range(len(s)//3):
        codon = s[3*i:3*i+3]
        aa = rna_codon_dict[codon]
        if aa == 'Stop':
            break
        protein += aa
    return protein


if __name__ == '__main__':
    rna_codon_dict = {}
    with open('rna_codon_table.txt') as f:
        for line in f:
            chars = line.strip().split(' ')

            for i, char in enumerate(chars):
                if len(char) == 3:
                    rna_codon_dict[char] = chars[i+1]
    with open('./dataset/sample_rosalind_prot.txt') as f:
        s = f.read().strip()
    protein = translate(s, rna_codon_dict)
    print(protein)
    with open('./dataset/rosalind_prot.txt') as f:
        s = f.read().strip()
    protein = translate(s, rna_codon_dict)
    print(protein)
