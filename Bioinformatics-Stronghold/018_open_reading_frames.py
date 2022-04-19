def read_fasta(file_path):
    dna_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.startswith('>'):
                label = line.strip().replace('>', '')
                dna_dict[label] = ''
            else:
                dna_dict[label] += line.strip()
    return dna_dict


def translate_protein(s, codon_dict, start_index=0):
    protein = ''
    for i in range(start_index, len(s)):
        codon = s[i:i+3]
        if codon_dict[codon] == 'M':
            protein += codon_dict[codon]
            reading = i + 3
            while reading <= len(s) - 3:
                codon = s[reading:reading+3]
                if codon_dict[codon] == 'Stop':
                    reading += 3
                    break
                protein += codon_dict[codon]
                reading += 3
            return protein, reading
    return protein, len(s)-1


def get_translated_proteins(s, codon_dict):
    print(s)
    proteins = []
    start_index = 0
    while True:
        protein, idx = translate_protein(s, codon_dict, start_index)
        if protein:
            proteins.append(protein)
            start_index = idx
        else:
            break
    return proteins


if __name__ == '__main__':
    codon_dict = {}
    answer = ''
    with open('rna_codon_table.txt') as f:
        for line in f:
            chars = line.strip().split(' ')

            for i, char in enumerate(chars):
                if len(char) == 3:
                    codon_dict[char] = chars[i+1]
    dna_dict = read_fasta('./dataset/sample_rosalind_orf.txt')
    for dna in dna_dict.values():
        proteins = get_translated_proteins(dna.replace('T', 'U'), codon_dict)
        answer += '\n'.join(proteins)
    print(answer)
