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


if __name__ == '__main__':
    fasta_dict = read_fasta('./dataset/sample_rosalind_sseq.txt')
    indices = []
    for i, label in enumerate(fasta_dict):
        if i == 0:
            s = fasta_dict[label]
        elif i == 1:
            t = fasta_dict[label]
    start = 0
    for string in t:
        target = s[start:]
        found_idx = target.find(string)
        indices.append(start + found_idx + 1)
        start += found_idx + 1
    answer = ' '.join([str(indice) for indice in indices])
    print(answer)
    fasta_dict = read_fasta('./dataset/rosalind_sseq.txt')
    indices = []
    for i, label in enumerate(fasta_dict):
        if i == 0:
            s = fasta_dict[label]
        elif i == 1:
            t = fasta_dict[label]
    start = 0
    for string in t:
        target = s[start:]
        found_idx = target.find(string)
        indices.append(start + found_idx + 1)
        start += found_idx + 1
    answer = ' '.join([str(indice) for indice in indices])
    print(answer)
    with open('./submission/finding_a_spliced_motif.txt', mode='w') as f:
        f.write(answer)
