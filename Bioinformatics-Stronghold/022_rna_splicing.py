def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.strip().startswith('>'):
                label = line.strip().replace('>', '')
                fasta_dict[label] = ''
            else:
                fasta_dict[label] += line.strip()
    return fasta_dict


def create_translation_dict():
    codon_dict = {}
    with open('rna_codon_table.txt') as f:
        for line in f:
            chars = line.strip().split(' ')
            for i, char in enumerate(chars):
                if len(char) == 3:
                    codon_dict[char] = chars[i+1]
    return codon_dict


def transcribe_and_translate(dna, codon_dict):
    rna = dna.replace('T', 'U')
    protein = ''
    for i in range(len(rna)//3):
        codon = rna[i*3:i*3+3]
        if codon_dict.get(codon) == 'Stop':
            break
        protein += codon_dict.get(codon)
    return protein


def splice(dna, intron):
    return dna.replace(intron, '')


if __name__ == '__main__':
    fasta_dict = read_fasta('./dataset/sample_rosalind_splc.txt')
    codon_dict = create_translation_dict()
    for i, s in enumerate(fasta_dict):
        if i == 0:
            dna = fasta_dict[s]
        else:
            intron = fasta_dict[s]
            dna = splice(dna, intron)
    protein = transcribe_and_translate(dna, codon_dict)
    print(protein)
    fasta_dict = read_fasta('./dataset/rosalind_splc.txt')
    codon_dict = create_translation_dict()
    for i, s in enumerate(fasta_dict):
        if i == 0:
            dna = fasta_dict[s]
        else:
            intron = fasta_dict[s]
            dna = splice(dna, intron)
    protein = transcribe_and_translate(dna, codon_dict)
    print(protein)
    with open('./submission/rna_splicing.txt', mode='w') as f:
        f.write(protein)
