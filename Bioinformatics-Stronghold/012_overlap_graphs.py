def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.startswith('>'):
                label = line.strip().replace('>', '')
                fasta_dict[label] = ''
            else:
                fasta_dict[label] += line.strip()
    return fasta_dict


def find_overlap_graphs(fasta_dict, k=3):
    overlap_graphs = []
    for label, string in fasta_dict.items():
        for label2, string2 in fasta_dict.items():
            if label != label2 and string[-k:] == string2[:k]:
                overlap_graphs.append(f'{label} {label2}')
    return overlap_graphs


if __name__ == '__main__':
    fasta_dict = read_fasta('./dataset/sample_rosalind_grph.txt')
    overlap_graphs = find_overlap_graphs(fasta_dict)
    answer = '\n'.join(overlap_graphs)
    print(answer)
    fasta_dict = read_fasta('./dataset/rosalind_grph.txt')
    overlap_graphs = find_overlap_graphs(fasta_dict)
    answer = '\n'.join(overlap_graphs)
    print(answer)
    with open('./submission/overlap_graphs.txt', mode='w') as f:
        f.write(answer)
