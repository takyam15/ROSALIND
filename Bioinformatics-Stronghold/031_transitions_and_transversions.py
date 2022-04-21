def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.strip().startswith('>'):
                label = line.strip()
                fasta_dict[label] = ''
            else:
                fasta_dict[label] += line.strip()
    return fasta_dict


def count_trans(s, t):
    transition_counts = 0
    transversion_counts = 0
    for char1, char2 in zip(s, t):
        if char1 != char2:
            chars = ''.join(sorted([char1, char2]))
            if chars in ['AG', 'CT']:
                transition_counts += 1
            else:
                transversion_counts += 1
    return transition_counts / transversion_counts


if __name__ == '__main__':
    fasta_dict = read_fasta('./dataset/sample_rosalind_tran.txt')
    s, t = fasta_dict.values()
    ratio = count_trans(s, t)
    print(ratio)
    fasta_dict = read_fasta('./dataset/rosalind_tran.txt')
    s, t = fasta_dict.values()
    ratio = count_trans(s, t)
    print(ratio)
    with open('./submission/transitions_and_transversion.txt', mode='w') as f:
        f.write(str(ratio))
